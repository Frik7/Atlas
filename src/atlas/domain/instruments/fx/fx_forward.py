import QuantLib as ql
from dataclasses import dataclass
from atlas.domain.enums import Currency


@dataclass(frozen=True, slots=True)
class FxForward:
    """
    Args:
    base_ccy: Base currency
    quote_ccy: Quote currency
    strike_forward_rate: Forward rate (base_ccy/quote_ccy)
    notional: Notional amount (base currency)
    settlement_date: Settlement date
    """

    base_ccy: Currency
    quote_ccy: Currency
    strike_forward_rate: float
    notional: float
    settlement_date: ql.Date
