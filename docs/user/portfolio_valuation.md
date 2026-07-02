# Portfolio Valuation & Batch Processing

In quantitative finance, pricing large portfolios trade-by-trade can introduce significant overhead. Atlas addresses this by introducing **Compilers** (`src/atlas/compiliers/`). 

Compilers transform collections of high-level domain objects into flat NumPy arrays. These arrays can then be processed efficiently in batch loops or passed directly to vectorized math functions.

---

## 1. The Compilation Pattern

A compiler function follows the signature:
`compile_instruments(portfolio: Tuple[Instrument, ...]) -> Tuple[np.ndarray, ...]`

For example, the `compile_equity_options` compiler extracts contract parameters from a portfolio of `EuropeanEquityOption` instruments and packages them into type-specific NumPy arrays:

```python
from atlas.domain.instruments.equities.options import EuropeanEquityOption
from atlas.domain.enums import Currency
from atlas.compiliers.equity_option_compiler import compile_equity_options
import QuantLib as ql

# 1. Define a portfolio of European equity options
portfolio = (
    EuropeanEquityOption(
        strike_price=100.0,
        expiry_date=ql.Date(18, 12, 2026),
        equity_ticker="AAPL",
        option_type=1,  # Call
        currency=Currency.USD
    ),
    EuropeanEquityOption(
        strike_price=95.0,
        expiry_date=ql.Date(18, 12, 2026),
        equity_ticker="AAPL",
        option_type=-1,  # Put
        currency=Currency.USD
    ),
    EuropeanEquityOption(
        strike_price=110.0,
        expiry_date=ql.Date(18, 6, 2027),
        equity_ticker="MSFT",
        option_type=1,  # Call
        currency=Currency.USD
    )
)

# 2. Compile the portfolio into flat NumPy arrays
(
    strikes,
    expiry_dates,
    underlying_ids,
    option_types,
    currencies
) = compile_equity_options(portfolio)

print("Compiled strikes array:", strikes)
print("Compiled underlying tickers:", underlying_ids)
```

---

## 2. Batch Pricing Workflow

Once compiled, you can price the portfolio using selectors and pricing functions. Below is an example of batch pricing a compiled portfolio by mapping the compiled arrays over the pricing engine:

```python
import QuantLib as ql
import numpy as np
from atlas.domain.market.market_data import MarketDataSnapshot, EquitySpot, FixedRate, StaticVolatility, DividendRate
from atlas.domain.enums import Currency
from atlas.compute.pricing.equities.equity_option_pricers import black_scholes_merton_pricer

# Set up market data snapshot
valuation_date = ql.Date(2, 7, 2026)
market_data = MarketDataSnapshot(
    valuation_date=valuation_date,
    equity_spots={
        "AAPL": EquitySpot(equity_ticker="AAPL", currency=Currency.USD, value=100.0),
        "MSFT": EquitySpot(equity_ticker="MSFT", currency=Currency.USD, value=350.0),
    },
    fixed_rate={Currency.USD: FixedRate(rate=0.05)},
    volatility_rates={
        "AAPL": StaticVolatility(volatility=0.20),
        "MSFT": StaticVolatility(volatility=0.25),
    },
    dividend_rates={
        "AAPL": DividendRate(rate=0.01),
        "MSFT": DividendRate(rate=0.005),
    },
    fx_spots={}
)

# Batch pricing using the compiled NumPy arrays
prices = []
for i in range(len(strikes)):
    ticker = underlying_ids[i]
    currency = currencies[i]
    
    # Retrieve market parameters for the specific option
    spot = market_data.equity_spots[ticker].value
    r = market_data.fixed_rate[currency].rate
    q = market_data.dividend_rates[ticker].rate
    vol = market_data.volatility_rates[ticker].volatility
    
    # Execute the pure mathematical pricer
    price = black_scholes_merton_pricer(
        valuation_date=valuation_date,
        expiry_date=expiry_dates[i],
        spot_price=spot,
        strike_price=strikes[i],
        risk_free_rate=r,
        dividend_yield=q,
        volatility=vol,
        option_type=option_types[i]
    )
    prices.append(price)

print("Portfolio Prices:", prices)
```

---

## 3. Advantages of this Pattern

* **Memory Efficiency**: Compiling complex domain objects into flat NumPy arrays reduces Python object overhead, making it highly suitable for passing to low-level extensions (e.g., Cython, Numba, or C++ wrappers).
* **Parallelization**: Since the compiled arrays are independent of thread-unsafe Python objects, they can be processed concurrently using libraries like `multiprocessing` or vectorized calculations.
* **Separation of Concerns**: The compilation step separates the data structure (how a trade is saved) from the pricing payload (the exact floating-point inputs the mathematical solver needs).
