from typing import Callable
import numpy as np
from scipy.optimize import minimize

def calibrate_params(objective: Callable, initial: dict, bounds: dict = None):
    """
    Simple wrapper to calibrate parameters using scipy.minimize.
    objective: function(params_dict) -> scalar (lower is better)
    initial: dict of initial parameter values
    bounds: dict of (min, max) for each parameter
    Returns: dict of optimized parameters
    """
    keys = list(initial.keys())
    x0 = [initial[k] for k in keys]
    bnds = [bounds.get(k, (None, None)) if bounds else (None, None) for k in keys]

    def obj(x):
        params = {k: v for k, v in zip(keys, x)}
        return objective(params)

    res = minimize(obj, x0, bounds=bnds)
    return {k: float(v) for k, v in zip(keys, res.x)}
