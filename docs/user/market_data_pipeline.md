# Market Data Pipeline & Selectors

Pricing engines require complex market parameters (spot prices, dividend rates, risk-free discount curves, and volatility surfaces). Atlas simplifies this using a decoupled pipeline that feeds raw market data snapshot containers into stateless selectors.

---

## 1. Market Data Containers

All market variables at a given evaluation point are collected inside the frozen container class: `MarketDataSnapshot` (`src/atlas/domain/market/market_data.py`).

The container holds the following immutable records:
* **`valuation_date`** (`ql.Date`): The reference date for curves, discount factors, and model time fractions.
* **`equity_spots`** (`Dict[str, EquitySpot]`): Map of equity ticker names to spot records (containing spot price, asset currency, etc.).
* **`fixed_rate`** (`Dict[Currency, FixedRate]`): Map of currencies to risk-free interest rates.
* **`volatility_rates`** (`Dict[str, StaticVolatility]`): Map of tickers to implied volatility values.
* **`dividend_rates`** (`Dict[str, DividendRate]`): Map of tickers to annual dividend yields.
* **`fx_spots`** (`Dict[Tuple[Currency, Currency], FXSpot]`): Map of currency pairs to FX spot rates.

### Example Construction
Here is how you populate a snapshot programmatically:

```python
import QuantLib as ql
from atlas.domain.market.market_data import (
    MarketDataSnapshot, EquitySpot, FixedRate, StaticVolatility, DividendRate, FXSpot
)
from atlas.domain.enums import Currency

snapshot = MarketDataSnapshot(
    valuation_date=ql.Date(2, 7, 2026),
    equity_spots={
        "AAPL": EquitySpot(equity_ticker="AAPL", currency=Currency.USD, value=100.0)
    },
    fixed_rate={
        Currency.USD: FixedRate(rate=0.05)
    },
    volatility_rates={
        "AAPL": StaticVolatility(volatility=0.20)
    },
    dividend_rates={
        "AAPL": DividendRate(rate=0.01)
    },
    fx_spots={}
)
```

---

## 2. The Selector Pattern

Because pricing functions are written as pure functions with simple mathematical inputs (e.g. standard floats, dates, ints), we need a bridge to map domain instruments and `MarketDataSnapshot` structures into these flat arguments. 

This bridge is called a **Selector**. Selectors live in `src/atlas/compute/selectors/`.

A selector is a pure function that follows this signature:
`select_data(instrument: Instrument, market_data: MarketDataSnapshot) -> Dict[str, Any]`

The returned dictionary keys correspond **exactly** to the keyword arguments expected by the target pricing function.

### Example: BSM Selector
The `select_bsm_data` selector extracts values for the Black-Scholes-Merton pricer:

```python
def select_bsm_data(
    instrument: EuropeanEquityOption,
    market_data: MarketDataSnapshot,
) -> Dict[str, Any]:
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
```

---

## 3. Feeding the Dispatcher

The dispatcher (`calculate_price` in `src/atlas/compute/pricing/pricing_dispatcher.py`) uses a registry to tie specific instrument types to their corresponding selector and pricing function.

Under the hood, the dispatcher performs three simple, stateless steps:
1. Look up the instrument class type in the registry.
2. Run the **Selector** function to build the input kwargs dict.
3. Unpack the dictionary (`**kwargs`) directly into the **Pricer** function.

```python
# The dispatcher's internal logic:
pricing_data = selector_function(instrument, market_data)
return pricing_function(**pricing_data)
```

This decoupled pipeline ensures that adding new instruments or models never requires editing existing pricing formulas, keeping the code highly maintainable and modular.
