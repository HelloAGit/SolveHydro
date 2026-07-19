import numpy as np
from hydrocomplex.formulas import routing

def test_muskingum_length():
    inflow = np.ones(10)
    out = routing.muskingum_routing(inflow, k=2.0, x=0.2)
    assert len(out) == len(inflow)
    assert out[0] == inflow[0]
