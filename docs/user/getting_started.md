# Getting Started with Atlas

Welcome to **Atlas**, a high-performance financial engineering engine designed for derivative pricing, exposure calculations, and XVA calculations. 

Atlas is designed for quantitative analysts and software engineers who need modular, stateless, and vectorized pricing capabilities.

---

## 1. Design Methodology

Atlas is built entirely on a **functional programming paradigm**. Rather than tying pricing mathematical logic to heavy object states, we separate **data representation** from **computation**:

1. **Domain Models (`src/atlas/domain/`)**: Pure data structures (Python dataclasses or simple classes) that represent financial instruments (e.g., European Options, FX Forwards) and market states.
2. **Selectors (`src/atlas/compute/selectors/`)**: Functions that extract specific variables from a generic market data snapshot and pair them with instrument parameters to build inputs for a specific pricer.
3. **Pricers (`src/atlas/compute/pricing/`)**: Stateless, pure mathematical functions that take primitive values (floats, dates, arrays) and return valuation results (e.g., present value, Greeks).
4. **Compilers (`src/atlas/compiliers/`)**: Vectorization utilities that compile large tuples of structured instruments into flat NumPy arrays for highly efficient batch execution.

### The Power of Modularity
Because our mathematical pricing functions are stateless, they can be utilized:
* **In isolation**: Call the pricer directly in scratch scripts or other libraries with primitive numbers, without needing any instrument classes or market data wrappers.
* **In composition**: Combine them through the dispatching pipeline for automated portfolio-wide valuation.

---

## 2. Engine Capabilities

Currently, Atlas supports the following financial instruments and pricing models:

| Asset Class | Instrument Type | Pricing Model / Method | Key Outputs |
| :--- | :--- | :--- | :--- |
| **Equities** | European Option | Black-Scholes-Merton (BSM) Analytical Model | Premium (PV), Greeks |
| **Foreign Exchange (FX)** | FX Forward | Covered Interest Rate Parity | Forward Rate, PV |

---

## 3. Quick Start (Isolated Pricing)

You can call the pure mathematical pricing functions directly. Here is a simple example showing how to import and price a European option in isolation using the Black-Scholes-Merton pricer:

```python
import QuantLib as ql
from atlas.compute.pricing.equities.equity_option_pricers import black_scholes_merton_pricer

# Define the valuation and contract dates
valuation_date = ql.Date(2, 7, 2026)
expiry_date = ql.Date(18, 12, 2026)

# Execute pricing directly with primitive arguments
price = black_scholes_merton_pricer(
    valuation_date=valuation_date,
    expiry_date=expiry_date,
    spot_price=100.0,
    strike_price=105.0,
    risk_free_rate=0.05,
    dividend_yield=0.02,
    volatility=0.20,
    option_type=1  # 1 for Call, -1 for Put
)

print(f"BSM Call Price: {price:.4f}")
```

---

## 4. Where to Go Next

To explore more advanced features, navigate to the following sections:

* **[Portfolio Valuation](file:///c:/Users/FrikStrydom/Github/Atlas/docs/user/portfolio_valuation.md)**: Learn how to price entire collections of trades using NumPy compilers and vectorization.
* **[Market Data Pipeline](file:///c:/Users/FrikStrydom/Github/Atlas/docs/user/market_data_pipeline.md)**: Understand how market yield curves, spot rates, and volatility surfaces are organized using the `MarketDataSnapshot` class.
* **[Mathematical Reference](file:///c:/Users/FrikStrydom/Github/Atlas/docs/reference/mathematical_models.md)**: Review the exact mathematical equations and formulations used under the hood.

### Interactive Notebook Demos
You can also run live pricing examples using the Jupyter Notebooks located in the repository's `demos/` directory:
* [European Equity Option Notebook](file:///c:/Users/FrikStrydom/Github/Atlas/demos/european_equity_option_pricer.ipynb)
* [FX Forward Notebook](file:///c:/Users/FrikStrydom/Github/Atlas/demos/fx_forward_pricer.ipynb)
