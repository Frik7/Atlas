import numpy as np
from typing import Tuple
from atlas.domain.instruments.equities.options import EuropeanEquityOption


def compile_equity_options(portfolio: Tuple[EuropeanEquityOption, ...]) -> Tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    """
    Compile a portfolio of European equity options into a tuple of numpy arrays.

    Args:
        portfolio: A tuple of EuropeanEquityOption objects.

    Returns:
        A tuple of numpy arrays corresponding to the option characteristics in order:
        (strikes, expiry_dates, underlying_ids, option_types, currencies)
    """
    strikes = np.array([opt.strike_price for opt in portfolio], dtype=np.float64)
    expiry_dates = np.array([opt.expiry_date for opt in portfolio], dtype=object)
    underlying_ids = np.array([opt.equity_ticker for opt in portfolio], dtype=object)
    option_types = np.array([opt.option_type for opt in portfolio], dtype=np.int32)
    currencies = np.array([opt.currency for opt in portfolio], dtype=object)

    return (
        strikes,
        expiry_dates,
        underlying_ids,
        option_types,
        currencies,
    )
