import QuantLib as ql
from math import exp


def fx_forward_pricer(
    valuation_date: ql.Date,
    settlement_date: ql.Date,
    strike_forward_rate: float,
    notional: float,
    spot_exchange_rate: float,
    foreign_interest_rate: float,
    domestic_interest_rate: float,
) -> float:
    """
    FX Forward Pricing
    ----------------

    Args:
        valuation_date (ql.Date): Valuation date
        settlement_date (ql.Date): Settlement date
        strike_forward_rate (float): Strike forward rate (base_ccy/quote_ccy)
        notional (float): Notional (base_ccy)
        spot_exchange_rate (float): Spot exchange rate (base_ccy/quote_ccy)
        foreign_interest_rate (float): Foreign interest rate (quote_ccy)
        domestic_interest_rate (float): Domestic interest rate (base_ccy)
    Returns:
        float: FX Forward price (base_ccy)
    """

    dc_act365 = ql.Actual365Fixed()
    year_fraction = dc_act365.yearFraction(valuation_date, settlement_date)

    # FX Forward price
    foreign_df = exp(-foreign_interest_rate * year_fraction)
    domestic_df = exp(-domestic_interest_rate * year_fraction)
    fx_forward_price = notional * (
        spot_exchange_rate * domestic_df - strike_forward_rate * foreign_df
    )

    return fx_forward_price
