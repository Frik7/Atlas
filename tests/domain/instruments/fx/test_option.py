from datetime import date
import pytest
from atlas.domain.instruments.fx.option import FXOption
from atlas.domain.types.enums import Currency, OptionType


def test_fx_option_instantiation() -> None:
    """Test that FXOption can be instantiated with valid data."""
    option = FXOption(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
        option_type=OptionType.CALL,
    )

    assert option.base_currency == Currency.USD
    assert option.quote_currency == Currency.ZAR
    assert option.strike == 19.50
    assert option.maturity_date == date(2025, 6, 20)
    assert option.option_type == OptionType.CALL


def test_fx_option_frozen() -> None:
    """Test that FXOption is frozen and cannot be modified."""
    option = FXOption(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
        option_type=OptionType.CALL,
    )

    with pytest.raises(AttributeError):
        option.strike = 20.0  # type: ignore[misc]


def test_fx_option_slots() -> None:
    """Test that FXOption uses slots for memory efficiency."""
    option = FXOption(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
        option_type=OptionType.CALL,
    )

    assert not hasattr(option, "__dict__")


def test_fx_option_equality() -> None:
    """Test that two FXOption instances with the same data are equal."""
    o1 = FXOption(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
        option_type=OptionType.CALL,
    )
    o2 = FXOption(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
        option_type=OptionType.CALL,
    )
    o3 = FXOption(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
        option_type=OptionType.PUT,
    )

    assert o1 == o2
    assert o1 != o3
    assert hash(o1) == hash(o2)
