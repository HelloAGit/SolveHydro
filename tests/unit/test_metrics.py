from hydrocomplex.core import metrics
import numpy as np

def test_nse_perfect():
    obs = np.array([1,2,3,4])
    sim = np.array([1,2,3,4])
    assert metrics.nse(obs, sim) == 1.0

def test_kge_basic():
    obs = np.array([1,2,3,4])
    sim = np.array([1.1,1.9,3.2,3.8])
    val = metrics.kge(obs, sim)
    assert -1.0 <= val <= 1.0
