import pandas as pd
import numpy as np

def ensure_datetime_index(series: pd.Series, freq: str = None) -> pd.Series:
    s = series.copy()
    if not isinstance(s.index, pd.DatetimeIndex):
        s.index = pd.to_datetime(s.index)
    if freq:
        s = s.asfreq(freq)
    return s

def rolling_mean(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=1).mean()
