from datetime import date
import pytest
from atlas.domain.instruments.equity.option import EquityOption
from atlas.domain.types.enums import OptionType, Currency


def test_equity_option_instantiation() -> None:
    """Test that EquityOption can be instantiated with valid data."""
    option = EquityOption(
        underlying_id="AAPL",
        strike=150.0,
        maturity_date=date(2025, 12, 19),
        currency=Currency.USD,
        option_type=OptionType.CALL,
    )

    assert option.underlying_id == "AAPL"
    assert option.strike == 150.0
    assert option.maturity_date == date(2025, 12, 19)
    assert option.currency == Currency.USD
    assert option.option_type == OptionType.CALL


def test_equity_option_frozen() -> None:
    """Test that EquityOption is frozen and cannot be modified."""
    option = EquityOption(
        underlying_id="AAPL",
        strike=150.0,
        maturity_date=date(2025, 12, 19),
        currency=Currency.USD,
        option_type=OptionType.CALL,
    )

    with pytest.raises(AttributeError):
        option.strike = 160.0  # type: ignore[misc]


def test_equity_option_slots() -> None:
    """Test that EquityOption uses slots for memory efficiency."""
    option = EquityOption(
        underlying_id="AAPL",
        strike=150.0,
        maturity_date=date(2025, 12, 19),
        currency=Currency.USD,
        option_type=OptionType.CALL,
    )

    assert not hasattr(option, "__dict__")
