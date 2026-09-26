# Domain Reference

The **Domain Reference** documents the core data models, instruments, and market data snapshot structures used across the Atlas engine.

---

## 🏛️ Instruments & Enums

These schemas model the financial contracts and their attributes (such as currencies and expiry schedules).

| Class | Description |
| --- | --- |
| [`Currency`](#atlas.domain.enums.Currency) | Enum representing supported currencies (USD, EUR, GBP, ZAR, etc.). |
| [`EuropeanEquityOption`](#atlas.domain.instruments.equities.options.EuropeanEquityOption) | Schema definition for a European-style option on an equity underlying. |
| [`FxForward`](#atlas.domain.instruments.fx.fx_forward.FxForward) | Schema definition for a Foreign Exchange (FX) Forward contract. |

---

## 📈 Market Data Snapshot

These schemas represent market variables and containers that feed rate and volatility curves to the pricing engines.

| Class | Description |
| --- | --- |
| [`MarketDataSnapshot`](#atlas.domain.market.market_data.MarketDataSnapshot) | A container holding rate, yield, spot, and volatility variables at a specific valuation date. |
| [`EquitySpot`](#atlas.domain.market.market_data.EquitySpot) | Market spot price of an equity asset. |
| [`FixedRate`](#atlas.domain.market.market_data.FixedRate) | Continuously compounded risk-free rate parameters. |
| [`StaticVolatility`](#atlas.domain.market.market_data.StaticVolatility) | Constant implied volatility parameters. |
| [`DividendRate`](#atlas.domain.market.market_data.DividendRate) | Continuous dividend yield rate parameters. |
| [`FXSpot`](#atlas.domain.market.market_data.FXSpot) | Foreign Exchange spot exchange rate. |

---

## 🏛️ Instruments & Enums Details

::: atlas.domain.enums.Currency

::: atlas.domain.instruments.equities.options.EuropeanEquityOption

::: atlas.domain.instruments.fx.fx_forward.FxForward

---

## 📈 Market Data Snapshot Details

::: atlas.domain.market.market_data.MarketDataSnapshot

::: atlas.domain.market.market_data.EquitySpot

::: atlas.domain.market.market_data.FixedRate

::: atlas.domain.market.market_data.StaticVolatility

::: atlas.domain.market.market_data.DividendRate

::: atlas.domain.market.market_data.FXSpot
