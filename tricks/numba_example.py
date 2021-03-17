import numba as nb
import numpy as np


@nb.jit(nopython=True)
def rolling_sum(x: np.ndarray, window: int) -> np.ndarray:
    out_length = x.shape[0] - window + 1
    out = np.zeros(out_length)
    out[0] = np.sum(x[:window])
    for i in range(1, out_length):
        out[i] = out[i - 1] - x[i - 1] + x[i - 1 + window]
    return out


if __name__ == "__main__":
    from cftool.misc import timeit
    from cftool.misc import StrideArray
    from cftool.stat import RollingStat

    def timing(w: int) -> None:
        print("-" * 30)
        with timeit(f"numba ({w})"):
            for _ in range(10):
                r1 = rolling_sum(array, w)
        with timeit(f"numpy ({w})"):
            for _ in range(10):
                r2 = StrideArray(array).roll(w).sum(1)
        with timeit(f"cython ({w})"):
            for _ in range(10):
                r3 = RollingStat.sum(array, w)
        assert np.allclose(r1, r2)
        assert np.allclose(r2, r3)

    array = np.random.random(10 ** 6)
    timing(10)
    timing(100)
    timing(1000)
    timing(100)
    timing(10)
