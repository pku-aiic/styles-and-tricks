import numpy as np

from typing import Any
from typing import List

try:
    from .cython_utils import *
except ImportError:
    raise


def c_flat_arr_to_float32(array: List[Any]) -> np.ndarray:
    return flat_arr_to_float32(array)  # type: ignore


__all__ = [
    "c_flat_arr_to_float32",
]
