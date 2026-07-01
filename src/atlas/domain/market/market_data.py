from typing import Dict, Tuple
from atlas.domain.enums import Currency
from dataclasses import dataclass, field
import QuantLib as ql


@dataclass(frozen=True)
class EquitySpot:
    equity_ticker: str
    currency: Currency
    value: float


@dataclass(frozen=True)
class FixedRate:
    rate: float


@dataclass(frozen=True)
class StaticVolatility:
    volatility: float


@dataclass(frozen=True)
class DividendRate:
    rate: float


@dataclass(frozen=True)
class FXSpot:
    base_ccy: Currency
    quote_ccy: Currency
    value: float


@dataclass(frozen=True)
class MarketDataSnapshot:
    """
    Market Data Container
    ---------------------

    Attributes:
        valuation_date (Date): Valuation date
        equity_spots (Dict[str, EquitySpot]): Dictionary of equity spots
        fixed_rates (Dict[Currency, FixedRate]): Dictionary of fixed rates
        volatility_rates (Dict[str, StaticVolatility]): Dictionary of vol surfaces
        dividend_rates (Dict[str, DividendRate]): Dictionary of dividend curves
    """

    valuation_date: ql.Date
    equity_spots: Dict[str, EquitySpot]
    fixed_rate: Dict[Currency, FixedRate]
    volatility_rates: Dict[str, StaticVolatility]
    dividend_rates: Dict[str, DividendRate]
    fx_spots: Dict[Tuple[Currency, Currency], FXSpot] = field(default_factory=Dict)
