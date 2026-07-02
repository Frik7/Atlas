from typing import Dict, Tuple
from atlas.domain.enums import Currency
from dataclasses import dataclass, field
import QuantLib as ql


@dataclass(frozen=True)
class EquitySpot:
    """Representation of an equity spot market price.

    Attributes:
        equity_ticker (str): The equity ticker symbol.
        currency (Currency): The currency in which the equity prices are denominated.
        value (float): The current spot price of the equity.
    """

    equity_ticker: str
    currency: Currency
    value: float


@dataclass(frozen=True)
class FixedRate:
    """Representation of a continuously compounded risk-free rate.

    Attributes:
        rate (float): The continuously compounded interest rate.
    """

    rate: float


@dataclass(frozen=True)
class StaticVolatility:
    """Representation of a constant implied volatility parameter.

    Attributes:
        volatility (float): The constant implied volatility value.
    """

    volatility: float


@dataclass(frozen=True)
class DividendRate:
    """Representation of a continuous dividend yield rate.

    Attributes:
        rate (float): The annual continuous dividend yield rate.
    """

    rate: float


@dataclass(frozen=True)
class FXSpot:
    """Representation of a Foreign Exchange spot exchange rate.

    Attributes:
        base_ccy (Currency): The base currency of the FX pair.
        quote_ccy (Currency): The quote currency of the FX pair.
        value (float): The spot exchange rate (value of base currency in terms
            of quote currency).
    """

    base_ccy: Currency
    quote_ccy: Currency
    value: float


@dataclass(frozen=True)
class MarketDataSnapshot:
    """Snapshot container holding all market variables at a specific valuation date.

    Attributes:
        valuation_date (ql.Date): The valuation date of the market snapshot.
        equity_spots (Dict[str, EquitySpot]): Dictionary of equity spots
            mapping tickers to prices.
        fixed_rate (Dict[Currency, FixedRate]): Dictionary of currency
            risk-free interest rates.
        volatility_rates (Dict[str, StaticVolatility]): Dictionary of asset
            implied volatilities.
        dividend_rates (Dict[str, DividendRate]): Dictionary of asset
            continuous dividend rates.
        fx_spots (Dict[Tuple[Currency, Currency], FXSpot]): Dictionary of FX
            spot exchange rates for currency pairs.
    """

    valuation_date: ql.Date
    equity_spots: Dict[str, EquitySpot]
    fixed_rate: Dict[Currency, FixedRate]
    volatility_rates: Dict[str, StaticVolatility]
    dividend_rates: Dict[str, DividendRate]
    fx_spots: Dict[Tuple[Currency, Currency], FXSpot] = field(default_factory=Dict)
