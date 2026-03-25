from dataclasses import dataclass
from datetime import date
from skans.domain.types.aliases import Price
from skans.domain.types.enums import OptionType, Currency


@dataclass(frozen=True, slots=True)
class EquityOption:
    """
    Contractual definition of an European Equity Option.
    """

    underlying_id: str
    strike: Price
    maturity_date: date
    currency: Currency
    option_type: OptionType
