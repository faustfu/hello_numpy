import numpy as np


def zscore(x, axis=None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd

    return zscore

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)

    return result

a = np.array([[1, 2, 3], [5, 5.5, 6]])
print(zscore(a))
print(zscore(a, axis=1))
print(min_max(a))
print(min_max(a, axis=1))
