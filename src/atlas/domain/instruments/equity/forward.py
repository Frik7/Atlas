from dataclasses import dataclass
from datetime import date
from skans.domain.types.aliases import Price
from skans.domain.types.enums import Currency


@dataclass(frozen=True, slots=True)
class EquityForward:
    """
    Contractual definition of an Equity Forward.
    """

    underlying_id: str
    strike: Price
    maturity_date: date
    currency: Currency
