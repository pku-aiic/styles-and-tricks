import numpy as np

from cftool.misc import timeit
from cftool.misc import allclose

x = np.arange(4).reshape([2, 2])
print("x", x)
print("ii->i", np.einsum("ii->i", x))
print("ij,ij->ij", np.einsum("ij,ij->ij", x, x))
print("ij,ij->i", np.einsum("ij,ij->i", x, x))
print("ij,jk->ik", np.einsum("ij,jk->ik", x, x))

# B1, T1, D
x1 = np.random.random([128, 32, 8])
# B2, T2, D
x2 = np.random.random([64, 16, 8])
# inner products (B1, B2, T1, T2)
with timeit("naive"):
    inner1 = (x1[..., None, :, None, :] * x2[None, :, None, ...]).sum(4)
with timeit("einsum"):
    inner2 = np.einsum("ijm,klm->ikjl", x1, x2)
with timeit("optimized"):
    inner3 = np.einsum("ijm,klm->ikjl", x1, x2, optimize=True)
assert allclose(inner1, inner2, inner3)
