---
name: Atlas Documentation Skill
description: Instructions for adding, modifying, and structuring documentation in the Atlas project, including Google-style docstrings with type annotations and linter configurations.
---

# Atlas Documentation Skill

Use this skill when you are asked to add or update documentation for the Atlas repository. It defines the folder organization, docstring standards, and quality verification workflows.

---

## 1. Documentation Structure & Locations

All repository documentation files live inside the [docs/](file:///c:/Users/FrikStrydom/Github/Atlas/docs/) directory. Do not create documentation files in other directories. Categorize new documents into the following subfolders:

* **User Documentation (`docs/user/`)**:
  * For user-facing guides, tutorials, and setup instructions.
  * Key files:
    * `getting_started.md`: Introduces the engine's capabilities and design philosophy.
    * `portfolio_valuation.md`: Explains how portfolios are compiled and valued in batch.
    * `market_data_pipeline.md`: Explains how market variables are formatted and injected.
* **Developer Documentation (`docs/developer/`)**:
  * For internal engine designs, diagrams, and onboarding instructions.
  * Key files:
    * `architecture.md`: Explains the stateless functional architecture layers.
    * `adding_instruments_pricers.md`: Checklist of files to modify when adding new products.
    * `contributing.md`: Workspace setup, type checking, and command references.
* **Mathematical Reference (`docs/reference/`)**:
  * For documenting quantitative pricing models and risk calculations.
  * Key files:
    * `mathematical_models.md`: Mathematical equations represented in LaTeX notation.

---

## 2. Docstring Style Guidelines

Code-level documentation must strictly adhere to the **Google Docstring Style** with explicit type annotations.

### Standard Format for Functions
1. Include a short one-line summary ending with a period.
2. Under `Args:`, format parameters as `name (type): description`.
3. Under `Returns:`, format the return value as `type: description`.
4. Wrap lines so they do not exceed 88 characters.
5. Do not leave a blank line immediately after the closing docstring triple quotes.

```python
def example_pricer(spot_price: float, strike_price: float) -> float:
    """Calculate the theoretical contract price.

    Args:
        spot_price (float): The current spot rate of the asset.
        strike_price (float): The contract execution strike price.

    Returns:
        float: The calculated contract price.
    """
    return spot_price - strike_price
```

### Standard Format for Classes / Dataclasses
Use `Attributes:` instead of `Args:` for dataclass attributes:

```python
@dataclass(frozen=True)
class ExampleInstrument:
    """Representation of a financial contract.

    Attributes:
        strike_price (float): The strike price.
        currency (Currency): The contract currency.
    """
    strike_price: float
    currency: Currency
```

---

## 3. Verification Workflow

After writing documentation or modifying docstrings, you must verify the changes:

1. **Formatting & Linter Checks**:
   * Run the pre-commit checks locally using:
     ```bash
     pre-commit run --all-files
     ```
   * Ensure that `black` and `flake8` (with `flake8-docstrings`) pass without any warnings.

2. **Unit Tests**:
   * Run unit tests within the virtual environment:
     ```bash
     .venv/Scripts/python -m pytest
     ```
   * Ensure all tests pass to confirm docstring edits did not introduce syntax errors.
