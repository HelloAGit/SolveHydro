import numpy as np

def muskingum_routing(inflow, k=1.0, x=0.2):
    """
    Simple Muskingum routing.
    inflow: array-like
    k: storage time constant (time step units)
    x: weighting factor (0 <= x <= 0.5)
    """
    I = np.asarray(inflow, dtype=float)
    n = len(I)
    O = np.zeros(n)
    dt = 1.0
    C0 = (-k * x + 0.5 * dt) / (k * (1 - x) + 0.5 * dt)
    C1 = (k * x + 0.5 * dt) / (k * (1 - x) + 0.5 * dt)
    C2 = (k * (1 - x) - 0.5 * dt) / (k * (1 - x) + 0.5 * dt)
    # initialize
    O[0] = I[0]
    for t in range(1, n):
        O[t] = C0 * I[t] + C1 * I[t-1] + C2 * O[t-1]
    return O
