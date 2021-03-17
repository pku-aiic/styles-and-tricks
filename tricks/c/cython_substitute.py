import numpy as np

from typing import Any
from typing import List


def naive_flat_arr_to_float32(array: List[Any]) -> np.ndarray:
    return np.array(array, np.float32)


__all__ = [
    "naive_flat_arr_to_float32",
]
