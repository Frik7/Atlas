from typing import Any, Dict
from atlas.domain.instruments.fx.fx_forward import FxForward
from atlas.domain.market.market_data import MarketDataSnapshot


def select_fx_forward_data(
    instrument: FxForward,
    market_data: MarketDataSnapshot,
) -> Dict[str, Any]:
    """Select the data required for the FX Forward pricer.

    Args:
        instrument (FxForward): The FX forward instrument.
        market_data (MarketDataSnapshot): The market data snapshot.

    Returns:
        Dict[str, Any]: A dictionary containing the FX forward data keys and values.
    """
    valuation_date = market_data.valuation_date
    settlement_date = instrument.settlement_date
    strike_forward_rate = instrument.strike_forward_rate
    notional = instrument.notional
    spot_exchange_rate = market_data.fx_spots[
        (instrument.base_ccy, instrument.quote_ccy)
    ].value
    foreign_interest_rate = market_data.fixed_rate[instrument.quote_ccy].rate
    domestic_interest_rate = market_data.fixed_rate[instrument.base_ccy].rate

    return {
        "valuation_date": valuation_date,
        "settlement_date": settlement_date,
        "strike_forward_rate": strike_forward_rate,
        "notional": notional,
        "spot_exchange_rate": spot_exchange_rate,
        "foreign_interest_rate": foreign_interest_rate,
        "domestic_interest_rate": domestic_interest_rate,
    }
