import numpy as np
import pandas as pd
import pytest

@pytest.fixture
def sample_obs():
    return pd.Series([1.0, 2.0, 3.0, 4.0])

@pytest.fixture
def sample_sim():
    return pd.Series([1.1, 1.9, 3.2, 3.8])
