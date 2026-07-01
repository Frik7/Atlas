import numpy as np
import QuantLib as ql
from atlas.domain.instruments.equities.options import EuropeanEquityOption
from atlas.compiliers.equity_option_compiler import compile_equity_options
from atlas.domain.enums import Currency


def test_compile_equity_options_empty() -> None:
    portfolio = ()
    (
        strikes,
        expiry_dates,
        underlying_ids,
        option_types,
        currencies,
    ) = compile_equity_options(portfolio)

    assert len(strikes) == 0
    assert len(expiry_dates) == 0
    assert len(underlying_ids) == 0
    assert len(option_types) == 0
    assert len(currencies) == 0

    assert strikes.dtype == np.float64
    assert expiry_dates.dtype == object
    assert underlying_ids.dtype == object
    assert option_types.dtype == np.int32
    assert currencies.dtype == object


def test_compile_equity_options_populated() -> None:
    d1 = ql.Date(22, 6, 2026)
    d2 = ql.Date(23, 6, 2026)

    opt1 = EuropeanEquityOption(
        strike_price=100.0,
        expiry_date=d1,
        equity_ticker="AAPL",
        option_type=1,
        currency=Currency.USD,
    )
    opt2 = EuropeanEquityOption(
        strike_price=150.0,
        expiry_date=d2,
        equity_ticker="MSFT",
        option_type=-1,
        currency=Currency.EUR,
    )

    portfolio = (opt1, opt2)
    (
        strikes,
        expiry_dates,
        underlying_ids,
        option_types,
        currencies,
    ) = compile_equity_options(portfolio)

    np.testing.assert_array_equal(strikes, np.array([100.0, 150.0], dtype=np.float64))
    np.testing.assert_array_equal(expiry_dates, np.array([d1, d2], dtype=object))
    np.testing.assert_array_equal(
        underlying_ids, np.array(["AAPL", "MSFT"], dtype=object)
    )
    np.testing.assert_array_equal(option_types, np.array([1, -1], dtype=np.int32))
    np.testing.assert_array_equal(currencies, np.array(["USD", "EUR"], dtype=object))
