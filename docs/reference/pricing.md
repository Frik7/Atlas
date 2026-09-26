# Pricing Functions

The **Pricing Functions** category documents the mathematical pricing engines, dispatcher routines, and data selection utilities in the Atlas library.

---

## 🎛️ Pricing Dispatcher

The dispatcher chooses the appropriate selector and pricing function based on the instrument type.

| Function | Description |
| --- | --- |
| [`calculate_price`](#atlas.pricing.calculate_price) | Calculate the price of a financial instrument using registered models. |

---

## 🔍 Selector Utilities

Selectors extract and validate primitive inputs from high-level instrument schemas and market data snapshots.

| Function | Description |
| --- | --- |
| [`select_bsm_data`](#atlas.pricing._selectors.select_bsm_data) | Extract Black-Scholes-Merton option pricing parameters from market data and options. |
| [`select_fx_forward_data`](#atlas.pricing._selectors.select_fx_forward_data) | Extract FX Forward parameters from market data and contracts. |

---

## 🧮 Mathematical Pricers

Pricers are pure, stateless, and vectorized functions implementing the mathematical pricing formulations.

| Function | Description |
| --- | --- |
| [`black_scholes_merton_pricer`](#atlas.pricing.black_scholes_merton_pricer) | Compute the theoretical Black-Scholes-Merton contract price. |
| [`fx_forward_pricer`](#atlas.pricing.fx_forward_pricer) | Compute the present value of an FX Forward contract. |

---

## 🎛️ Pricing Dispatcher Details

::: atlas.pricing.calculate_price

---

## 🔍 Selector Utilities Details

::: atlas.pricing._selectors.select_bsm_data

::: atlas.pricing._selectors.select_fx_forward_data

---

## 🧮 Mathematical Pricers Details

::: atlas.pricing.black_scholes_merton_pricer

::: atlas.pricing.fx_forward_pricer
