from typing import Protocol, runtime_checkable
import numpy as np


@runtime_checkable
class RandomNumberGenerator(Protocol):
    """
    Interface for any type of random number generator.
    """

    def generate(self, n_paths: int, n_steps: int) -> np.ndarray:
        """Returns a 2D matrix of stadard normal random variables"""
        ...


class SimpleRng:
    """
    Implementation of the Standard Mersenne Twister using numpy.
    """

    def generate(self, n_paths: int, n_steps: int) -> np.ndarray:
        """Returns a 2D matrix of stadard normal random variables (paths * steps)"""
        return np.random.randn(n_paths, n_steps)
