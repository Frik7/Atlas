import pytest
from datetime import date
from atlas.domain.portfolio import Position
from atlas.domain.instruments.equity import EquityForward, EquityOption
from atlas.domain.instruments.fx import FXForward, FXOption
from atlas.domain.types.enums import Currency, OptionType
from atlas.market.resolver import DependencyResolver


def test_resolve_empty_positions() -> None:
    """Verify it returns an empty RiskFactorSchema for empty input."""
    resolver = DependencyResolver()
    schema = resolver.resolve([])
    assert schema.factor_indices == {}


def test_resolve_equity_instruments() -> None:
    """Verify it extracts underlying_id and assigns deterministic indices for Equity."""
    resolver = DependencyResolver()

    # Use different IDs to check sorting/indexing
    pos1 = Position(
        position_id="P1",
        instrument=EquityForward(
            underlying_id="AAPL",
            strike=150.0,
            maturity_date=date(2025, 1, 1),
            currency=Currency.USD,
        ),
    )
    pos2 = Position(
        position_id="P2",
        instrument=EquityOption(
            underlying_id="MSFT",
            strike=300.0,
            maturity_date=date(2025, 1, 1),
            currency=Currency.USD,
            option_type=OptionType.CALL,
        ),
    )

    schema = resolver.resolve([pos2, pos1])  # Pass in non-alphabetical order

    # Expected: AAPL -> 0, MSFT -> 1 (sorted alphabetically)
    assert schema.factor_indices == {"AAPL": 0, "MSFT": 1}


def test_resolve_fx_instruments() -> None:
    """Verify it extracts concatenated currency pairs for FX."""
    resolver = DependencyResolver()

    pos1 = Position(
        position_id="P1",
        instrument=FXForward(
            base_currency=Currency.ZAR,
            quote_currency=Currency.USD,
            strike=1.1,
            maturity_date=date(2025, 1, 1),
        ),
    )
    # Deduplication test: another position with same FX pair
    pos2 = Position(
        position_id="P2",
        instrument=FXOption(
            base_currency=Currency.ZAR,
            quote_currency=Currency.USD,
            strike=1.15,
            maturity_date=date(2025, 1, 1),
            option_type=OptionType.PUT,
        ),
    )

    schema = resolver.resolve([pos1, pos2])

    assert schema.factor_indices == {"ZARUSD": 0}


def test_resolve_mixed_instruments() -> None:
    """Verify it handles both types, deduplicates, and sorts alphabetically."""
    resolver = DependencyResolver()

    pos_equity = Position(
        position_id="P1",
        instrument=EquityForward("AAPL", 150.0, date(2025, 1, 1), Currency.USD),
    )
    pos_fx = Position(
        position_id="P2",
        instrument=FXForward(Currency.ZAR, Currency.USD, 1.3, date(2025, 1, 1)),
    )

    schema = resolver.resolve([pos_equity, pos_fx])

    # Alphabetical: AAPL, ZARUSD
    assert schema.factor_indices == {"AAPL": 0, "ZARUSD": 1}


def test_resolve_unsupported_instrument() -> None:
    """Verify it raises TypeError for unknown instrument types."""
    resolver = DependencyResolver()

    # Creating a dummy "Position" with an unsupported type
    class UnsupportedInstrument:
        pass

    pos = Position(
        position_id="FAIL", instrument=UnsupportedInstrument()  # type: ignore
    )

    with pytest.raises(TypeError, match="Unsupported instrument type in resolver"):
        resolver.resolve([pos])
