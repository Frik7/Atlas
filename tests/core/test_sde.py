import numpy as np

from atlas.core.sde import geometric_brownian_motion
from atlas.core.rng import SimpleRng


def test_geometric_brownian_motion_default_rng() -> None:
    S0 = 100.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    n_steps = 100
    n_paths = 1000

    # Should run without error
    paths = geometric_brownian_motion(S0, mu, sigma, T, n_steps, n_paths)
    assert paths.shape == (n_paths, n_steps + 1)


def test_geometric_brownian_motion_custom_rng() -> None:
    S0 = 100.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    n_steps = 100
    n_paths = 1000
    rng = SimpleRng()

    paths = geometric_brownian_motion(S0, mu, sigma, T, n_steps, n_paths, rng=rng)
    assert paths.shape == (n_paths, n_steps + 1)


def test_geometric_brownian_motion_initial_value() -> None:
    S0 = 100.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    n_steps = 100
    n_paths = 100

    paths = geometric_brownian_motion(S0, mu, sigma, T, n_steps, n_paths)
    assert np.all(paths[:, 0] == S0)


def test_geometric_brownian_motion_variance_scaling() -> None:
    S0 = 100.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    n_steps = 100
    n_paths = 10000

    paths = geometric_brownian_motion(S0, mu, sigma, T, n_steps, n_paths)
    S_T = paths[:, -1]

    # Calculate log returns of the final price relative to S0
    log_returns = np.log(S_T / S0)

    variance = np.var(log_returns)
    expected_variance = sigma**2 * T

    # Check if variance is close to expected value
    assert np.isclose(variance, expected_variance, rtol=0.2)
