from dataclasses import dataclass
from typing import Tuple, Dict, Union
from functools import cached_property

from skans.domain.types.aliases import Quantity
from skans.domain.types.enums import LongShort
from skans.domain.instruments import EquityForward, EquityOption, FXForward, FXOption

# Algebraic Data Type (Tagged Union) representing all valid instruments
AnyInstrument = Union[EquityForward, EquityOption, FXForward, FXOption]


@dataclass(frozen=True, slots=True)
class Position:
    """Represents a unique position in the portfolio to be priced"""

    position_id: str
    instrument: AnyInstrument


@dataclass(frozen=True, slots=True)
class Trade:
    """Represents a scaled, directional exposure to a Position, with added metadata"""

    trade_id: str
    position_id: str
    counterparty_id: str
    quantity: Quantity
    direction: LongShort


@dataclass(frozen=True)
class Portfolio:
    portfolio_id: str
    trades: Tuple[Trade, ...]

    @cached_property
    def _trade_index(self) -> Dict[str, Trade]:
        return {t.trade_id: t for t in self.trades}

    def get_trade(self, trade_id: str) -> Trade:
        try:
            return self._trade_index[trade_id]
        except KeyError:
            raise KeyError(f"Trade '{trade_id}' not found.")

    def __len__(self) -> int:
        return len(self.trades)


@dataclass(frozen=True, slots=True)
class NettingSet:
    """
    A legal boundary for offsetting exposures.
    The Exposure Engine aggregates values at this level.
    """

    netting_set_id: str
    counterparty_id: str
    trade_ids: frozenset[str]
