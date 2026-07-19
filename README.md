# SolveHydro

SolveHydro is a Python package for solving complex hydrological problems with modular utilities for runoff, routing, metrics, calibration, and reproducible case studies.

## Project structure

- `src/hydrocomplex/` – main package source code
  - `core/` – core hydrology components
  - `formulas/` – reusable hydrology formulas
  - `calibration/` – calibration-related utilities
  - `cli.py` – command-line entry point
- `tests/` – automated test suite
  - `unit/test_metrics.py` – tests for metrics functionality
  - `unit/test_routing.py` – tests for routing functionality
- `case_studies/flood/` – flood forecasting example case study
  - `config.yaml` – inputs and parameters
  - `README.md` – case study notes

## Installation

```bash
pip install -e .
```

Optional dependencies:

- `.[test]` for testing tools
- `.[ml]` for scikit-learn support
- `.[gridded]` for xarray-based workflows

## Development

Run tests locally:

```bash
pip install -e .[test]
pytest
```

See `CONTRIBUTING.md` for contribution guidelines.

## Case study

The repository includes a minimal reproducible flood forecasting example in `case_studies/flood/`. It currently includes a configuration file and supporting documentation, with a notebook planned for an end-to-end workflow covering preprocess, runoff, routing, and metrics.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
