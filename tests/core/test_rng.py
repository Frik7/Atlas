import numpy as np

from atlas.core.rng import SimpleRng, RandomNumberGenerator


def test_simple_rng_protocol_compliance() -> None:
    assert isinstance(SimpleRng(), RandomNumberGenerator)


def test_simple_rng_instantiation() -> None:
    rng = SimpleRng()
    assert isinstance(rng, SimpleRng)


def test_simple_rng_generate_shape() -> None:
    rng = SimpleRng()
    n_paths = 100
    n_steps = 50
    result = rng.generate(n_paths, n_steps)
    assert result.shape == (n_paths, n_steps)


def test_simple_rng_generate_type() -> None:
    rng = SimpleRng()
    n_paths = 10
    n_steps = 5
    result = rng.generate(n_paths, n_steps)
    assert result.dtype == np.float64 or result.dtype == float
