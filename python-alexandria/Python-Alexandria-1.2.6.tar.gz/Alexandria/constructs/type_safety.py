import numpy as np


def ensure_ndarray(a):
    return np.asarray(a) if not isinstance(a, np.ndarray) else a
