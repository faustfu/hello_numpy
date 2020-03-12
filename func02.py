import numpy as np
import numpy.linalg as la

a = np.array([1, 2])
b = np.array([3, 4])
c = np.matrix([1, 2])  # create a matrix(2D array)
d = np.matrix([3, 4])  # create a matrix(2D array)

print(np.dot(a, b))
# error: shapes (1,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)
# print(np.dot(c, d))

e = np.array([[3, 0], [0, 4]])  # [[x1,y1],[x2,y2]] two vectors
print(la.det(e)/2) # calculate area of the triangle by determinant

print(la.eig(e)) # return a tuple of eigenvalue array and eigenvector array