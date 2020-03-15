import numpy as np
import numpy.linalg as la

a = np.array([[0, 1], [1, 0]])
print(a, la.eig(a))

b = np.array([[2, 1], [1, 2]])
print(b, la.eig(b))

c = np.array([[-1, 0], [0, 1]])
print(c, la.eig(c))

d = np.array([1, 2])
e = np.array([-1, 2])
f = np.array([[1, 2], [-1, 2]])
print(la.det(f))
print(np.cross(d, e))

print(np.digitize(7.3,[7, 8, 9]))
