# Mathematical Reference Models

This document details the exact quantitative pricing models and mathematical formulas implemented in the **Atlas** engine.

---

## 1. Black-Scholes-Merton (BSM) Model

The BSM analytical model evaluates European options on stocks/underlying assets that pay continuous dividend yields.

### Mathematical Formulation
The present value (premium) of a European Call Option ($C$) or European Put Option ($P$) is given by:

$$
C = S_0 e^{-q T} N(d_1) - K e^{-r T} N(d_2)
$$

$$
P = K e^{-r T} N(-d_2) - S_0 e^{-q T} N(-d_1)
$$

where:
* \(S_0\) is the current spot price of the underlying asset.
* \(K\) is the strike price of the option contract.
* \(r\) is the risk-free continuously compounded interest rate.
* \(q\) is the continuous dividend yield rate.
* \(\sigma\) is the implied volatility of the underlying asset price.
* \(T\) is the time-to-expiry fraction (computed using Actual/365 Fixed year-fraction conventions).
* \(N(x)\) is the cumulative distribution function of the standard normal distribution:

$$
N(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{t^2}{2}} dt
$$

The variables \(d_1\) and \(d_2\) are defined as:

$$
d_1 = \frac{\ln\left(\frac{S_0}{K}\right) + \left(r - q + \frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}
$$

$$
d_2 = d_1 - \sigma\sqrt{T}
$$

### Implementation Notes
* Implemented in [equity_option_pricers.py](file:///c:/Users/FrikStrydom/Github/Atlas/src/atlas/compute/pricing/equities/equity_option_pricers.py).
* Validated against QuantLib values in the test suites.

---

## 2. FX Forward Pricing

An FX Forward contract prices an agreement to exchange currencies at a fixed rate at a future settlement date.

### Covered Interest Rate Parity Formula
Under no-arbitrage conditions, the theoretical forward rate ($F$) is determined by foreign/domestic interest rate spreads:

$$
F = S_0 e^{(r_d - r_f)T}
$$

where:
* \(S_0\) is the current FX Spot exchange rate (domestic currency per unit of foreign currency).
* \(r_d\) is the continuously compounded interest rate of the domestic currency (the quote currency).
* \(r_f\) is the continuously compounded interest rate of the foreign currency (the base currency).
* \(T\) is the year fraction from valuation date to settlement date.

### Valuation (Present Value)
The present value (PV) of the forward contract to exchange foreign currency notional (\(N_f\)) at contract rate (\(K\)) is:

$$
\text{PV} = N_f \cdot \left( S_0 e^{-r_f T} - K e^{-r_d T} \right)
$$

### Implementation Notes
* Implemented in [fx_forward_pricer.py](file:///c:/Users/FrikStrydom/Github/Atlas/src/atlas/compute/pricing/fx/fx_forward_pricer.py).
* Validated against analytic calculations in the test suites.
