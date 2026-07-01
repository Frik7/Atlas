from dataclasses import dataclass
from atlas.domain.enums import Currency
import QuantLib as ql


@dataclass(frozen=True, slots=True)
class EuropeanEquityOption:
    """
    European equity option schema definition.

    Args:
        strike_price (float): Strike price of the option
        expiry (int): Expiry timestamp of the option
        equity_ticker (str): Identifier of the underlying equity
        option_type (int): Option type (1=call, -1=put)
        currency (str): Currency of the option
    """

    strike_price: float
    expiry_date: ql.Date
    equity_ticker: str
    option_type: int
    currency: Currency
