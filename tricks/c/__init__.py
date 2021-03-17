try:
    from .cython_wrappers import c_flat_arr_to_float32 as flat_arr_to_float32
except ImportError:
    from .cython_substitute import naive_flat_arr_to_float32 as flat_arr_to_float32


__all__ = ["flat_arr_to_float32"]
