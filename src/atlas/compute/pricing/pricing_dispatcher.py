from typing import Any, Callable, Dict, Tuple
from atlas.compute.pricing.equities import black_scholes_merton_pricer
from atlas.compute.pricing.fx import fx_forward_pricer
from atlas.compute.selectors.select_equity_option_data import select_bsm_data
from atlas.compute.selectors.select_fx_forward_data import select_fx_forward_data
from atlas.domain.market.market_data import MarketDataSnapshot

PRICER_REGISTRY: Dict[str, Tuple[Callable, Callable]] = {
    "EuropeanEquityOption": (select_bsm_data, black_scholes_merton_pricer),
    "FxForward": (select_fx_forward_data, fx_forward_pricer),
}


def calculate_price(instrument: Any, market_data: MarketDataSnapshot) -> float:
    """ """

    instrument_type = type(instrument).__name__

    if instrument_type not in PRICER_REGISTRY:
        raise ValueError(f"No selector or pricing function found for {instrument_type}")

    selector_function, pricing_function = PRICER_REGISTRY[instrument_type]

    pricing_data = selector_function(instrument, market_data)

    return pricing_function(**pricing_data)
