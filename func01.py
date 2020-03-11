import numpy as np

a = np.arange(10).reshape((2, -1))
print(a)
b = np.resize(a, (2, 3))  # clone all items and force to reshape by new axis.
print(b)
c = np.append(b, [[7, 8, 9]], axis=0)  # append new dimension in axis=0
print(c)
d = np.append(c, [[7], [7], [7]], axis=1)  # append new dimension in axis=1
print(d)

print(np.all(a))  # check if all items are true.
print(np.all(a < 10))  # check if all items are smaller then 10.

print(np.all(a, axis=0))  # check if all items along axis=0 are true.
print(np.all(a, axis=1))  # check if all items along axis=1 are true.
# check if all items along axis=1 are true and keep axes.
print(np.all(a, axis=1, keepdims=True))

print(np.any(a))  # check if some items are true.

print('----')
e = np.array([4, 3, 6, 2, 7, 1])
print(e)
# return a tuple which contains index array of matched items.
print(np.where(e < 3))
f = np.array([[4, 3, 6], [2, 7, 1]])
g = np.array([[777, 777, 777], [777, 777, 777]])
print(f)
# return a tuple which contains index array of matched items.
print(np.where(f < 3))
# return an array which contains comparison results.
print(np.where(f < 3, 'yes', 'no'))
# return an masked array which contains matched results.
print(np.where(f < 3, f, g))

print(np.amax(f), np.amin(f))  # return max/min item
print(f.max(), f.min())  # return max/min item

print(np.amax(f, axis=0))  # return max item along axis=0
print(np.amax(f, axis=1))  # return max item along axis=1
print('----')
print(f)
# flattern the array to be a 1D array and return the index of max/min item.
print(np.argmax(f), np.argmin(f))
# flattern the array to be a 1D array and return the index of max item.
# return a array which contains the index of max item along axis=0.
print(np.argmax(f, axis=0))
# return a array which contains the index of max item along axis=1.
print(np.argmax(f, axis=1))
print('----')
print(f)
print(f.transpose())  # switch axes
print(f.transpose((0, 1)))  # switch axes with specified order
print(f.T)  # switch axes by its property:T
print('----')
print(f)
print(np.sort(f))  # return new sorted array
print(np.argsort(f))  # return new sorted index
print(np.sort(f, axis=0))  # sort by axis=0 and return new sorted array
print(np.sort(f, axis=1))  # sort by axis=1 and return new sorted array
print(np.sort(f, axis=None))  # return new sorted 1D array
print(f)
f.sort() # sort the array and reset it
print(f)
