from datetime import date
import pytest
from atlas.domain.instruments.fx.forward import FXForward
from atlas.domain.types.enums import Currency


def test_fx_forward_instantiation() -> None:
    """Test that FXForward can be instantiated with valid data."""
    forward = FXForward(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
    )

    assert forward.base_currency == Currency.USD
    assert forward.quote_currency == Currency.ZAR
    assert forward.strike == 19.50
    assert forward.maturity_date == date(2025, 6, 20)


def test_fx_forward_frozen() -> None:
    """Test that FXForward is frozen and cannot be modified."""
    forward = FXForward(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
    )

    with pytest.raises(AttributeError):
        forward.strike = 20.0  # type: ignore[misc]


def test_fx_forward_slots() -> None:
    """Test that FXForward uses slots for memory efficiency."""
    forward = FXForward(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
    )

    assert not hasattr(forward, "__dict__")


def test_fx_forward_equality() -> None:
    """Test that two FXForward instances with the same data are equal."""
    f1 = FXForward(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
    )
    f2 = FXForward(
        base_currency=Currency.USD,
        quote_currency=Currency.ZAR,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
    )
    f3 = FXForward(
        base_currency=Currency.ZAR,
        quote_currency=Currency.USD,
        strike=19.50,
        maturity_date=date(2025, 6, 20),
    )

    assert f1 == f2
    assert f1 != f3
    assert hash(f1) == hash(f2)
