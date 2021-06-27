import numpy as np


def np_count_consecutive(arr):
    test = np.asarray(arr)
    # counts = np.diff(np.where(np.concatenate(([test[0]], test[1:] != test[:-1], [True])))[0])[::2]
    counts = np.diff(np.flatnonzero(np.concatenate(([True], test[1:] != test[:-1], [True]))))
    return counts
