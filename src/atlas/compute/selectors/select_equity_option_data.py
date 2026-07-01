from typing import Dict, Any
from atlas.domain.market.market_data import MarketDataSnapshot


def select_bsm_data(
    instrument: Any,
    market_data: MarketDataSnapshot,
) -> Dict[str, Any]:
    """
    Selects the required instrument and market data to be used in the
    Black-Scholes-Merton pricer.

    Args:
        instrument: The equity option instrument.
        market_data: The market data snapshot.

    Returns:
        A dictionary containing the Black-Scholes-Merton data.
        The keys in this dictionary should correspond to the arguments
        expected by the Black-Scholes-Merton pricer.
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
