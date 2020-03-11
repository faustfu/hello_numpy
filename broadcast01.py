# 1. Broadcasting occurs as calculating with two different shape arrays. Smaller array will broadcast if possible.
import numpy as np

a = np.array([[1, 2]])
b = np.array([3, 4])
print(a, b)
print(a+b)  # 1)b add new axis-0(=1), 2)do add operation.

print('----')
c = np.array([[1, 2], [3, 4]])
d = np.array([5, 6])
print(c)
print(d)
# 1)b add new axis-0(=1),
# 2)b duplicate items of every axis to increase the dimension until match another array's dimension(=2),
# 3)If dimensions of every axis are equal, do add operation.
print(c+d)