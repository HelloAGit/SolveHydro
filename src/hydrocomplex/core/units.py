# Minimal unit helpers (extendable)
from typing import Tuple

def mm_to_m(depth_mm: float) -> float:
    return depth_mm / 1000.0

def m_to_mm(depth_m: float) -> float:
    return depth_m * 1000.0
