# Adding New Instruments & Pricers

This document provides a step-by-step developer checklist for extending Atlas. By separating concerns into distinct layers, adding a new instrument or pricing model is straightforward and does not affect existing code.

Let's walkthrough the steps required to add a new product (e.g. an **Equity Barrier Option** or **Interest Rate Swap**).

---

## Extension Checklist

1. [ ] **Define the Instrument Model**
   * Add the instrument's contract parameters as an immutable data structure (using Python `@dataclass(frozen=True)` or simple classes) in `src/atlas/domain/instruments/`.
   * For example:
     ```python
     # domain/instruments/equities/barrier_options.py
     @dataclass(frozen=True)
     class EquityBarrierOption:
         strike_price: float
         barrier_level: float
         expiry_date: ql.Date
         equity_ticker: str
         option_type: int
         currency: Currency
     ```

2. [ ] **Write the Mathematical Pricer**
   * Implement a stateless, pure pricing function inside `src/atlas/compute/pricing/`.
   * Keep arguments simple (use dates, floats, arrays, and standard Python/NumPy types). Avoid importing domain objects or market snapshots inside this function.
   * Write Google-style docstrings with detailed parameter descriptions.

3. [ ] **Write the Selector**
   * Implement a selector function in `src/atlas/compute/selectors/`.
   * This function should extract data from the `MarketDataSnapshot` and instrument parameters, and return a dictionary of keys mapping to the pricer's parameter names.
   * Example:
     ```python
     def select_barrier_option_data(instrument, market_data) -> Dict[str, Any]:
         return {
             "spot_price": market_data.equity_spots[instrument.equity_ticker].value,
             "strike_price": instrument.strike_price,
             "barrier_level": instrument.barrier_level,
             # ... other mappings
         }
     ```

4. [ ] **Register with the Pricing Dispatcher**
   * Import your selector and pricer into `src/atlas/compute/pricing/pricing_dispatcher.py`.
   * Add the instrument class name mapping to the `PRICER_REGISTRY`:
     ```python
     PRICER_REGISTRY: Dict[str, Tuple[Callable, Callable]] = {
         # ...
         "EquityBarrierOption": (select_barrier_option_data, barrier_option_pricer),
     }
     ```

5. [ ] **Write the Instrument Compiler (Optional)**
   * If the instrument will be priced inside portfolios, write or extend a compiler inside `src/atlas/compiliers/` to batch-convert tuples of the new instrument into flat NumPy arrays.

6. [ ] **Add Unit Tests**
   * Write tests for the compiler under `tests/test_<instrument>_compiler.py`.
   * Write tests for the selector, pricer, and dispatcher under `tests/test_<instrument>_pricers.py`.
   * Verify using `pytest`.
