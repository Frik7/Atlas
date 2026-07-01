import QuantLib as ql
import scipy.stats as stats
from math import exp, log, sqrt


def black_scholes_merton_pricer(
    valuation_date: ql.Date,
    expiry_date: ql.Date,
    spot_price: float,
    strike_price: float,
    risk_free_rate: float,
    dividend_yield: float,
    volatility: float,
    option_type: int,
) -> float:
    """
    Args:
        option: European equity option
        market_data: Market data container
    """

    dc_act365 = ql.Actual365Fixed()
    T = dc_act365.yearFraction(valuation_date, expiry_date)

    d1 = (
        log(spot_price / strike_price)
        + (risk_free_rate - dividend_yield + 0.5 * volatility**2) * T
    ) / (volatility * sqrt(T))
    d2 = d1 - volatility * sqrt(T)

    Nd1 = stats.norm.cdf(option_type * d1)
    Nd2 = stats.norm.cdf(option_type * d2)

    bsm_price = option_type * (
        spot_price * exp(-dividend_yield * T) * Nd1
    ) - option_type * (strike_price * exp(-risk_free_rate * T) * Nd2)

    return float(bsm_price)
