# How to create a ndarray
import numpy as np

print(np.array([1, 2, 3, 4]))  # create an 1D array
print(np.arange(10))  # create an 1D array in range
print(np.arange(1, 5, 2))  # create an 1D array in range
# create an 1D array of float point number in range
print(np.arange(1.2, 5.4, 1.4))
# create an 1D array of integer number in range
print(np.arange(1.2, 5.4, 1.4, dtype=np.int))

a = np.arange(1.2, 5.4, 1.4, dtype=np.int)
print(a.ndim)  # get axis of the array(1D, 2D, ...)
print(a.size)  # get total size of the array
print(a.shape)  # get shape of dimension of the array

print(np.zeros((2, 4)))  # create an 2D array in shape.
print(np.ones((2, 4)))  # create an 2D array of '1' in shape.
# create an 2D array of random number in shape.
print(np.random.random((2, 4)))

# create a new 2D array by old 1D array elements and new shape.
b = a.reshape((2, 2))
print(b)
print(b[1, 0])  # access by location
print(b[1, :])  # access by slice

print(b * 3 + 2)  # do operations with all elements

c = np.array([1, 2, 3])
d = np.array([2, 2, 1])
print(c + d)  # do operations with two same shape arrays
print(c * d)
print(c / d)

print(np.linspace(1, 2, 4))  # create a 1D array by same gap.
