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
    """Calculate the Black-Scholes-Merton option price.

    Args:
        valuation_date (ql.Date): The valuation date.
        expiry_date (ql.Date): The option expiry date.
        spot_price (float): The underlying spot price.
        strike_price (float): The option strike price.
        risk_free_rate (float): The continuously compounded risk-free interest rate.
        dividend_yield (float): The continuous dividend yield of the underlying.
        volatility (float): The implied volatility of the underlying.
        option_type (int): 1 for Call, -1 for Put.

    Returns:
        float: The calculated option price.
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
