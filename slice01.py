# 1. Slice for 1D array is same.
import numpy as np

a = np.arange(10)
print(a[:])

b = np.arange(10).reshape(2, 5)
print(b[::-1, 1:3])
