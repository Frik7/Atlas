from typing import Iterable, Set, Dict

from skans.domain.portfolio import Position
from skans.domain.instruments.equity import EquityForward, EquityOption
from skans.domain.instruments.fx import FXForward, FXOption
from skans.market.environment import RiskFactorSchema


class DependencyResolver:
    """
    Scans a collection of Positions to determine the unique risk factors
    required for the market simulation.
    """

    def resolve(self, positions: Iterable[Position]) -> RiskFactorSchema:
        """
        Iterates over the position set to extract and deduplicate
        required risk factors, assigning them deterministic integer indices.
        """
        unique_factors: Set[str] = set()

        for pos in positions:
            inst = pos.instrument

            # Pattern matching on the Algebraic Data Type (Union)
            if isinstance(inst, (EquityForward, EquityOption)):
                unique_factors.add(inst.underlying_id)

            elif isinstance(inst, (FXForward, FXOption)):
                # Concatenate the string Enum values for FX pairs
                factor = f"{inst.base_currency.value}{inst.quote_currency.value}"
                unique_factors.add(factor)

            else:
                # Catches new instruments not yet supported
                raise TypeError(
                    f"Unsupported instrument type in resolver: {type(inst)}"
                )

        # Sort the factors alphabetically.
        # This guarantees that index assignment is completely deterministic
        # across different runs and operating systems.
        sorted_factors = sorted(list(unique_factors))

        factor_indices: Dict[str, int] = {
            factor: idx for idx, factor in enumerate(sorted_factors)
        }

        return RiskFactorSchema(factor_indices=factor_indices)
