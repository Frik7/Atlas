from datetime import date
import pytest
from atlas.domain.portfolio import Position, Trade, Portfolio, NettingSet
from atlas.domain.instruments.equity.forward import EquityForward
from atlas.domain.types.enums import Currency, LongShort


@pytest.fixture
def sample_instrument() -> EquityForward:
    return EquityForward(
        underlying_id="MSFT",
        strike=300.0,
        maturity_date=date(2025, 6, 20),
        currency=Currency.USD,
    )


def test_position_instantiation(sample_instrument: EquityForward) -> None:
    """Test that Position can be instantiated with valid data."""
    position = Position(position_id="POS001", instrument=sample_instrument)
    assert position.position_id == "POS001"
    assert position.instrument == sample_instrument


def test_position_immutability(sample_instrument: EquityForward) -> None:
    """Test that Position is frozen and cannot be modified."""
    position = Position(position_id="POS001", instrument=sample_instrument)
    with pytest.raises(AttributeError):
        position.position_id = "POS002"  # type: ignore[misc]


def test_trade_instantiation() -> None:
    """Test that Trade can be instantiated with valid data."""
    trade = Trade(
        trade_id="TRD001",
        position_id="POS001",
        counterparty_id="CPTY001",
        quantity=100.0,
        direction=LongShort.LONG,
    )
    assert trade.trade_id == "TRD001"
    assert trade.position_id == "POS001"
    assert trade.counterparty_id == "CPTY001"
    assert trade.quantity == 100.0
    assert trade.direction == LongShort.LONG


def test_trade_immutability() -> None:
    """Test that Trade is frozen and cannot be modified."""
    trade = Trade(
        trade_id="TRD001",
        position_id="POS001",
        counterparty_id="CPTY001",
        quantity=100.0,
        direction=LongShort.LONG,
    )
    with pytest.raises(AttributeError):
        trade.quantity = 200.0  # type: ignore[misc]


@pytest.fixture
def sample_portfolio() -> Portfolio:
    trades = (
        Trade("T1", "P1", "C1", 10.0, LongShort.LONG),
        Trade("T2", "P2", "C2", 20.0, LongShort.SHORT),
    )
    return Portfolio(portfolio_id="PORT001", trades=trades)


def test_portfolio_instantiation(sample_portfolio: Portfolio) -> None:
    """Test Portfolio instantiation and trade count."""
    assert sample_portfolio.portfolio_id == "PORT001"
    assert len(sample_portfolio) == 2


def test_portfolio_get_trade(sample_portfolio: Portfolio) -> None:
    """Test retrieving a trade by ID."""
    trade = sample_portfolio.get_trade("T1")
    assert trade.trade_id == "T1"
    assert trade.quantity == 10.0


def test_portfolio_get_trade_not_found(sample_portfolio: Portfolio) -> None:
    """Test that get_trade raises KeyError if trade ID is missing."""
    with pytest.raises(KeyError, match="Trade 'UNKNOWN' not found."):
        sample_portfolio.get_trade("UNKNOWN")


def test_portfolio_trade_index_caching(sample_portfolio: Portfolio) -> None:
    """Test that _trade_index is cached (using cached_property)."""
    index1 = sample_portfolio._trade_index
    index2 = sample_portfolio._trade_index
    assert index1 is index2


def test_nettingset_instantiation() -> None:
    """Test that NettingSet can be instantiated with valid data."""
    trade_ids = frozenset(["T1", "T2"])
    ns = NettingSet(
        netting_set_id="NS001",
        counterparty_id="CPTY001",
        trade_ids=trade_ids,
    )
    assert ns.netting_set_id == "NS001"
    assert ns.counterparty_id == "CPTY001"
    assert ns.trade_ids == trade_ids


def test_nettingset_immutability() -> None:
    """Test that NettingSet is frozen and cannot be modified."""
    ns = NettingSet(
        netting_set_id="NS001",
        counterparty_id="CPTY001",
        trade_ids=frozenset(["T1"]),
    )
    with pytest.raises(AttributeError):
        ns.netting_set_id = "NS002"  # type: ignore[misc]
