from typing import Dict, Any
from atlas.domain.market.market_data import MarketDataSnapshot


def select_bsm_data(
    instrument: Any,
    market_data: MarketDataSnapshot,
) -> Dict[str, Any]:
    """Select the data required for the Black-Scholes-Merton pricer.

    Args:
        instrument (Any): The equity option instrument.
        market_data (MarketDataSnapshot): The market data snapshot.

    Returns:
        Dict[str, Any]: A dictionary containing the Black-Scholes-Merton data
            keys and values.
    """
    return {
        "valuation_date": market_data.valuation_date,
        "expiry_date": instrument.expiry_date,
        "spot_price": market_data.equity_spots[instrument.equity_ticker].value,
        "strike_price": instrument.strike_price,
        "risk_free_rate": market_data.fixed_rate[instrument.currency].rate,
        "dividend_yield": market_data.dividend_rates[instrument.equity_ticker].rate,
        "volatility": market_data.volatility_rates[instrument.equity_ticker].volatility,
        "option_type": instrument.option_type,
    }
