import numpy as np


def center(x):
    mean_x = np.nanmean(x)
    return [ xi-mean_x for xi in x]

