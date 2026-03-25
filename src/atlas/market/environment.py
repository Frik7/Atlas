"""
Market Environment DTOs for the Skans Risk Engine.
Provides the memory-efficient handoff between the Generator and the Engine.
"""

from dataclasses import dataclass
from typing import Dict
import numpy as np


@dataclass(frozen=True)
class RiskFactorSchema:
    """
    Translates string-based risk factor identifiers into integer tensor indices.
    This enables string-free, zero-copy array slicing in the Valuation Engine.
    """

    factor_indices: Dict[str, int]

    def get_index(self, factor_name: str) -> int:
        """
        Retrieves the integer index for a given risk factor.

        Raises:
            KeyError: If the risk factor is not found in the simulated environment.
        """
        try:
            return self.factor_indices[factor_name]
        except KeyError:
            raise KeyError(
                f"Risk factor '{factor_name}' not present in the Market Environment. "
                f"Available factors: {list(self.factor_indices.keys())}"
            )


@dataclass(frozen=True)
class MarketEnvironment:
    """
    The immutable envelope containing the generated market state.

    Attributes:
        schema: The index mapping for the tensor's 3rd dimension.
        state_tensor: 3D NumPy array of shape (Paths, Timesteps + 1, RiskFactors).
        dt: The time step increment (e.g., 1/252 for daily steps).
    """

    schema: RiskFactorSchema
    state_tensor: np.ndarray
    dt: float

    def __post_init__(self) -> None:
        """
        Defensive programming: Lock the tensor to prevent accidental in-place
        mutation by the Valuation Engine.
        """
        self.state_tensor.flags.writeable = False
