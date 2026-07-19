# SolveHydro
Solving complex hydrological problems.

## Installation

```bash
pip install .
```

Install with optional extras:

```bash
pip install ".[test]"     # pytest + pytest-cov
pip install ".[ml]"       # scikit-learn
pip install ".[gridded]"  # xarray
```

## CLI usage

```bash
hydrocomplex --help

# Compute NSE / KGE metrics
hydrocomplex metrics --obs observed.csv --sim simulated.csv

# Run Muskingum routing
hydrocomplex muskingum --inflow inflow.csv --k 1.0 --x 0.2
```

## Python package build

```bash
pip install build
python -m build          # creates dist/*.whl and dist/*.tar.gz
```

## Docker

**Build the image:**

```bash
docker build -t hydrocomplex .
```

**Run (prints CLI help by default):**

```bash
docker run --rm hydrocomplex
```

**Override the command** to run the CLI with local data files:

```bash
docker run --rm -v "$(pwd)/data:/data" hydrocomplex \
    hydrocomplex metrics --obs /data/obs.csv --sim /data/sim.csv
```

## Running tests

```bash
pip install ".[test]"
pytest
```

