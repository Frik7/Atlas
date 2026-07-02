# Developer Onboarding & Contribution Guide

This guide details the onboarding workflow for new developers setting up their workspace, running validation tests, and contributing to the Atlas codebase.

---

## 1. Local Workspace Setup

Atlas requires Python 3.11 or higher.

### Step 1: Clone and Create Virtual Environment
Clone the repository and set up a virtual environment:
```bash
git clone https://github.com/Frik7/Atlas.git
cd Atlas
python -m venv .venv
```

### Step 2: Activate the Virtual Environment
* **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux**:
  ```bash
  source .venv/bin/activate
  ```

### Step 3: Install Dependencies
Install the package in editable mode along with all development tools:
```bash
pip install -e .[dev]
```

### Step 4: Install Pre-commit Hooks
Register the git hooks to validate styling, formatting, and docstrings before code is committed:
```bash
pre-commit install
```

---

## 2. Running Quality Checks

To maintain code quality, developers must run the following checks before opening Pull Requests:

### 1. Formatting (`black`)
Atlas enforces code formatting using Black. Run it locally via:
```bash
black .
```

### 2. Linting & Docstrings (`flake8`)
Atlas uses Flake8 to ensure PEP 8 compliance and Google-style docstrings (via `flake8-docstrings`). Verify code styling with:
```bash
flake8 src tests
```

### 3. Static Type Checks (`mypy`)
Atlas enforces strict type annotations across the entire library:
```bash
mypy src
```
*(Note: strict type declarations are configured in `pyproject.toml` and verified by Mypy.)*

### 4. Running Tests (`pytest`)
Execute the full test suite using:
```bash
pytest
```

---

## 3. Pre-commit Validation

When you run `git commit`, pre-commit hooks will automatically execute `black` and `flake8` checks on modified files.
If any hook fails, fix the reported formatting or styling errors and re-commit:
```bash
# Manually run pre-commit on all files to check status:
pre-commit run --all-files
```
