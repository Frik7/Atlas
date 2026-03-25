from dataclasses import dataclass
from datetime import date
from skans.domain.types.aliases import Price
from skans.domain.types.enums import Currency, OptionType


@dataclass(frozen=True, slots=True)
class FXOption:
    """
    Contractual definition of a European FX Option.
    The option_type (Call/Put) refers to the right regarding the base_currency.
    """

    base_currency: Currency
    quote_currency: Currency
    strike: Price
    maturity_date: date
    option_type: OptionType
