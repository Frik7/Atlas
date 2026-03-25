from typing import cast
from skans.core.rng import RandomNumberGenerator, SimpleRng
import numpy as np


def geometric_brownian_motion(
    S0: float,
    mu: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    rng: RandomNumberGenerator | None = None,
) -> np.ndarray:
    """
    Geometric Brownian Motion Simulator.

    Parameters
    ----------
    S0 : float
        Initial level.
    mu : float
        Drift rate.
    sigma : float
        Volatility.
    T : float
        Time horizon.
    n_steps : int
        Number of steps.
    n_paths : int
        Number of paths.
    rng : RandomNumberGenerator | None
        Random number generator.

    Returns
    -------
    np.ndarray
        Simulated paths (n_paths, n_steps + 1)
    """
    dt = T / n_steps

    if rng is None:
        rng = SimpleRng()

    # Generate random normal variables
    Z = rng.generate(n_paths, n_steps)

    # Geometric Brownian Motion formula
    # S(t) = S0 * exp((mu - 0.5 * sigma^2) * t + sigma * W(t))

    # Calculate the exponent
    exponent = (mu - 0.5 * sigma**2) * dt + sigma * Z * np.sqrt(dt)

    # Accumulate the exponent
    accumulated_exponent = np.cumsum(exponent, axis=1)

    # Prepend zero to the accumulated exponent to account for S0 at t=0
    accumulated_exponent = np.hstack((np.zeros((n_paths, 1)), accumulated_exponent))

    paths = S0 * np.exp(accumulated_exponent)

    return cast(np.ndarray, paths)
