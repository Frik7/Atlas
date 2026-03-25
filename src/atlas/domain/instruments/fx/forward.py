from dataclasses import dataclass
from datetime import date
from skans.domain.types.aliases import Price
from skans.domain.types.enums import Currency


@dataclass(frozen=True, slots=True)
class FXForward:
    """
    Contractual definition of an FX Forward.
    Represents the obligation to exchange base_currency for quote_currency
    at the strike price on the maturity_date.
    """

    base_currency: Currency
    quote_currency: Currency
    strike: Price
    maturity_date: date
