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
    """Calculate the present value of an FX Forward contract.

    Args:
        valuation_date (ql.Date): The valuation date.
        settlement_date (ql.Date): The forward settlement date.
        strike_forward_rate (float): The contracted forward exchange rate.
        notional (float): The base currency contract notional.
        spot_exchange_rate (float): The current spot exchange rate.
        foreign_interest_rate (float): The interest rate of the foreign
            (base) currency.
        domestic_interest_rate (float): The interest rate of the domestic
            (quote) currency.

    Returns:
        float: The present value of the forward contract.
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
