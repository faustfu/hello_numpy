# benchmark
import time
import numpy as np


def calculate_time():
    a = np.random.randn(100000)
    b = list(a)  # convert a ndarray to be a normal list.

    start_time = time.time()
    for _ in range(1000):
        sum_1 = np.sum(a)
    print('Using numpy %f sec' % (time.time()-start_time))

    start_time = time.time()
    for _ in range(1000):
        sum_2 = sum(b)
    print('Not using numpy %f sec' % (time.time()-start_time))


calculate_time()
