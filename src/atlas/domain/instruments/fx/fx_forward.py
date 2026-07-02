import QuantLib as ql
from dataclasses import dataclass
from atlas.domain.enums import Currency


@dataclass(frozen=True, slots=True)
class FxForward:
    """Representation of a Foreign Exchange (FX) Forward contract.

    Attributes:
        base_ccy (Currency): Base currency.
        quote_ccy (Currency): Quote currency.
        strike_forward_rate (float): Forward rate (base_ccy/quote_ccy).
        notional (float): Notional amount (base currency).
        settlement_date (ql.Date): Settlement date.
    """

    base_ccy: Currency
    quote_ccy: Currency
    strike_forward_rate: float
    notional: float
    settlement_date: ql.Date
