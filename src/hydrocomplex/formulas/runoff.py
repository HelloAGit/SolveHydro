import numpy as np

def scs_cn_runoff(precip_mm, cn, area_km2=1.0):
    """
    SCS-CN runoff depth (mm) for a single precipitation value or array.
    S = (25400 / CN) - 254  (mm)
    Q = (P - 0.2S)^2 / (P + 0.8S) for P > 0.2S else 0
    """
    P = np.asarray(precip_mm)
    S = (25400.0 / cn) - 254.0
    Ia = 0.2 * S
    Q = np.where(P > Ia, ((P - Ia)**2) / (P + 0.8 * S), 0.0)
    # return runoff depth in mm; user can convert to volume using area
    return Q

def unit_hydrograph_conv(precip_series, uh):
    """
    Convolve effective rainfall with unit hydrograph.
    precip_series: array-like effective rainfall (mm or volume)
    uh: unit hydrograph ordinates (same time step)
    """
    import numpy as np
    return np.convolve(precip_series, uh)[:len(precip_series)]
