# Atlas Financial Engineering Engine

Welcome to **Atlas**, a high-performance quantitative finance library designed for derivative pricing, exposure simulation, and XVA calculations. 

Atlas is engineered for quantitative analysts and software developers who require **stateless, vectorized, and modular** financial analytics.

---

## 🚀 Key Features

* **Functional Paradigm**: Data models are separated from pricing calculations. All math pricers are pure, stateless functions.
* **Vectorized Valuation**: Built-in compilers transform structured portfolios into contiguous NumPy arrays for massive batch execution.
* **Mathematical Precision**: Validated against industry-standard libraries (like QuantLib) with strict analytical modeling.
* **Type-Safe & Scalable**: Fully type-hinted and verified using Mypy strict mode.

---

## 📖 Documentation Structure

Explore the documentation by section:

### 👥 User Guides
* **[Getting Started](user/getting_started.md)**: Design philosophy, key concepts, and basic option pricing.
* **[Portfolio Valuation](user/portfolio_valuation.md)**: Compile and value multi-instrument portfolios in batch.
* **[Market Data Pipeline](user/market_data_pipeline.md)**: Structure rates, yields, and volatilities using snapshots.

### 💻 Developer Resources
* **[Architecture](developer/architecture.md)**: Explore the engine's layers from domain models to compilers.
* **[Adding Instruments & Pricers](developer/adding_instruments_pricers.md)**: Step-by-step checklist to expand engine capabilities.
* **[Contributing](developer/contributing.md)**: Setup, type checking, and pre-commit validation.

### 📐 Quantitative Reference
* **[Mathematical Reference Models](reference/mathematical_models.md)**: Comprehensive LaTeX formulations for Black-Scholes-Merton and FX Forward pricing.
* **[API Reference](reference/api.md)**: Auto-generated interface documentation for modules, classes, and pricing routines.

---

## 🛠 Quick Example

Price a European Option in isolation with a simple function call:

```python
import QuantLib as ql
from atlas.compute.pricing.equities.equity_option_pricers import black_scholes_merton_pricer

# Value options directly using primitive types
price = black_scholes_merton_pricer(
    valuation_date=ql.Date(2, 7, 2026),
    expiry_date=ql.Date(18, 12, 2026),
    spot_price=100.0,
    strike_price=105.0,
    risk_free_rate=0.05,
    dividend_yield=0.02,
    volatility=0.20,
    option_type=1  # 1 = Call, -1 = Put
)

print(f"BSM Call Option Price: {price:.4f}")
```
