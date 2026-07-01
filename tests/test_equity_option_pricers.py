import math
import QuantLib as ql
from atlas.domain.instruments.equities.options import EuropeanEquityOption
from atlas.domain.instruments.fx.fx_forward import FxForward
from atlas.domain.market.market_data import (
    MarketDataSnapshot,
    EquitySpot,
    FixedRate,
    StaticVolatility,
    DividendRate,
    FXSpot,
)
from atlas.domain.enums import Currency
from atlas.compute.pricing.pricing_dispatcher import calculate_price


def test_price_european_equity_option_call() -> None:
    valuation_date = ql.Date(22, 6, 2026)
    expiry_date = ql.Date(22, 6, 2027)  # exactly 1.0 year in Actual365Fixed

    option = EuropeanEquityOption(
        strike_price=100.0,
        expiry_date=expiry_date,
        equity_ticker="AAPL",
        option_type=1,  # call
        currency=Currency.USD,
    )

    market_data = MarketDataSnapshot(
        valuation_date=valuation_date,
        equity_spots={
            "AAPL": EquitySpot(equity_ticker="AAPL", currency=Currency.USD, value=100.0)
        },
        fixed_rate={Currency.USD: FixedRate(rate=0.05)},
        volatility_rates={"AAPL": StaticVolatility(volatility=0.2)},
        dividend_rates={"AAPL": DividendRate(rate=0.0)},
        fx_spots={},
    )

    price = calculate_price(option, market_data)

    # Reference BSM price for strike=100, spot=100, T=1, vol=0.2, q=0.0, r=0.05
    assert math.isclose(price, 10.4505856, rel_tol=1e-5)


def test_price_european_equity_option_put() -> None:
    valuation_date = ql.Date(22, 6, 2026)
    expiry_date = ql.Date(22, 6, 2027)

    option = EuropeanEquityOption(
        strike_price=100.0,
        expiry_date=expiry_date,
        equity_ticker="AAPL",
        option_type=-1,  # put
        currency=Currency.USD,
    )

    market_data = MarketDataSnapshot(
        valuation_date=valuation_date,
        equity_spots={
            "AAPL": EquitySpot(equity_ticker="AAPL", currency=Currency.USD, value=100.0)
        },
        fixed_rate={Currency.USD: FixedRate(rate=0.05)},
        volatility_rates={"AAPL": StaticVolatility(volatility=0.2)},
        dividend_rates={"AAPL": DividendRate(rate=0.0)},
        fx_spots={},
    )

    price = calculate_price(option, market_data)

    # Put-Call Parity: P = C + K * e^(-rT) - S * e^(-qT)
    # P = 10.4505856 + 100 * e^(-0.05) - 100 = 5.573528
    assert math.isclose(price, 5.573528, rel_tol=1e-5)


def test_price_fx_forward() -> None:
    valuation_date = ql.Date(22, 6, 2026)
    settlement_date = ql.Date(22, 6, 2027)

    fx_forward = FxForward(
        base_ccy=Currency.EUR,
        quote_ccy=Currency.USD,
        strike_forward_rate=1.10,
        notional=1_000_000.0,
        settlement_date=settlement_date,
    )

    market_data = MarketDataSnapshot(
        valuation_date=valuation_date,
        equity_spots={},
        fixed_rate={
            Currency.USD: FixedRate(rate=0.04),
            Currency.EUR: FixedRate(rate=0.03),
        },
        volatility_rates={},
        dividend_rates={},
        fx_spots={
            (Currency.EUR, Currency.USD): FXSpot(
                base_ccy=Currency.EUR, quote_ccy=Currency.USD, value=1.12
            )
        },
    )

    price = calculate_price(fx_forward, market_data)

    # T = 1.0
    # foreign_df = e^(-0.03) = 0.9704455
    # domestic_df = e^(-0.04) = 0.9607894
    # price = 1,000,000 * (1.12 * e^(-0.03) - 1.10 * e^(-0.04))
    # price = 1,000,000 * (1.12 * 0.9704455 - 1.10 * 0.9607894)
    # price = 1,000,000 * (1.08689896 - 1.05686834) = 30030.62
    expected_price = 1_000_000.0 * (1.12 * math.exp(-0.03) - 1.10 * math.exp(-0.04))
    assert math.isclose(price, expected_price, rel_tol=1e-5)
