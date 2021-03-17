import numpy as np

from typing import Any
from typing import List
from cftool.misc import timeit
from tricks.c.cython_wrappers import c_flat_arr_to_float32
from tricks.c.cython_substitute import naive_flat_arr_to_float32


def timing(array: List[Any], msg: str) -> None:
    with timeit(f"naive ({msg})"):
        x1 = naive_flat_arr_to_float32(array)
    with timeit(f"c ({msg})"):
        x2 = c_flat_arr_to_float32(array)
    assert np.allclose(x1, x2)


timing(np.random.random(10 ** 6).tolist(), "float")
timing(np.random.randint(0, 10 ** 6, 10 ** 6).tolist(), "int")
timing(np.random.random(10 ** 6).astype(np.str_).tolist(), "str")
