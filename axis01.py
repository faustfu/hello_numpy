import numpy as np

e = np.array([[1, 2, 3], [4, 5, 6]])  # create a 2D(2,3) array
f = np.array([e, e])

print(f)  # pack same shape arrays to form a new axis+1 array.

print(np.sum(f))  # sum every elements
print(f.sum(axis=0))  # sum by axis = 0
print(f.sum(axis=1))  # sum by axis = 1
print(f.sum(axis=2))  # sum by axis = 2
