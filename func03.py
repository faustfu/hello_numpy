import numpy as np
import numpy.linalg as la

a = np.array([[1,2,3],[2,4,7]])
print(a)
print(la.matrix_rank(a)) # get rank

b = np.array([[1,2,3],[2,4,6]])
print(b)
print(la.matrix_rank(b))
