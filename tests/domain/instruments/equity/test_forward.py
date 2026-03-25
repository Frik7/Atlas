from datetime import date
import pytest
from atlas.domain.instruments.equity.forward import EquityForward
from atlas.domain.types.enums import Currency


def test_equity_forward_instantiation() -> None:
    """Test that EquityForward can be instantiated with valid data."""
    forward = EquityForward(
        underlying_id="MSFT",
        strike=300.0,
        maturity_date=date(2025, 6, 20),
        currency=Currency.USD,
    )

    assert forward.underlying_id == "MSFT"
    assert forward.strike == 300.0
    assert forward.maturity_date == date(2025, 6, 20)
    assert forward.currency == Currency.USD


def test_equity_forward_frozen() -> None:
    """Test that EquityForward is frozen and cannot be modified."""
    forward = EquityForward(
        underlying_id="MSFT",
        strike=300.0,
        maturity_date=date(2025, 6, 20),
        currency=Currency.USD,
    )

    with pytest.raises(AttributeError):
        forward.strike = 310.0  # type: ignore[misc]


def test_equity_forward_slots() -> None:
    """Test that EquityForward uses slots for memory efficiency."""
    forward = EquityForward(
        underlying_id="MSFT",
        strike=300.0,
        maturity_date=date(2025, 6, 20),
        currency=Currency.USD,
    )

    assert not hasattr(forward, "__dict__")
