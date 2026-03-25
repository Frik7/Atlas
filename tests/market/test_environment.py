import pytest
import numpy as np
from atlas.market.environment import RiskFactorSchema, MarketEnvironment


def test_risk_factor_schema_get_index_success() -> None:
    """Test successful index retrieval from RiskFactorSchema."""
    indices = {"SPX": 0, "NDX": 1, "RUT": 2}
    schema = RiskFactorSchema(factor_indices=indices)

    assert schema.get_index("SPX") == 0
    assert schema.get_index("NDX") == 1
    assert schema.get_index("RUT") == 2


def test_risk_factor_schema_get_index_failure() -> None:
    """Test KeyError with descriptive message when factor is missing."""
    indices = {"SPX": 0}
    schema = RiskFactorSchema(factor_indices=indices)

    with pytest.raises(KeyError) as excinfo:
        schema.get_index("MISSING")

    assert "Risk factor 'MISSING' not present in the Market Environment." in str(
        excinfo.value
    )
    assert "Available factors: ['SPX']" in str(excinfo.value)


def test_market_environment_initialization() -> None:
    """Test successful initialization of MarketEnvironment."""
    indices = {"Factor1": 0}
    schema = RiskFactorSchema(factor_indices=indices)
    # Shape: (Paths, Timesteps + 1, RiskFactors)
    state = np.zeros((10, 5, 1))
    dt = 0.01

    env = MarketEnvironment(schema=schema, state_tensor=state, dt=dt)

    assert env.schema == schema
    assert np.array_equal(env.state_tensor, state)
    assert env.dt == dt


def test_market_environment_read_only_tensor() -> None:
    """Test that state_tensor is made read-only in __post_init__."""
    indices = {"Factor1": 0}
    schema = RiskFactorSchema(factor_indices=indices)
    state = np.zeros((2, 2, 1))
    dt = 1.0

    env = MarketEnvironment(schema=schema, state_tensor=state, dt=dt)

    # Check if flags.writeable is False
    assert env.state_tensor.flags.writeable is False

    # Attempting to modify should raise ValueError
    with pytest.raises(ValueError, match="assignment destination is read-only"):
        env.state_tensor[0, 0, 0] = 1.0
