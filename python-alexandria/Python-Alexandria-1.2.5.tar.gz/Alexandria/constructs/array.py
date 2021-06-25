import numpy as np
from math import ceil

from Alexandria.constructs.type_safety import ensure_ndarray
from Alexandria.math.numbers import get_representative_decimals


"""
Slicing
"""


def find_nearest_entry(array, value):
    array = ensure_ndarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx, array[idx]


"""
Characteristics
"""


def span(a):
    a = ensure_ndarray(a)
    if a.size > 1:
        a_s = a + a.min() if a.min() < 0 else a
        return a_s.max() - a_s.min()
    elif a.size == 1:
        return 0


def internal_array_shape(x):
    x = ensure_ndarray(x)
    if x.ndim > 1:
        return np.array([x[n].shape for n in range(len(x))])
    else:
        return np.ones(x.shape)


"""
Manipulations
"""


def dx_v(t):
    """
    :return: Return vector of base dimension increments, where the base dimension is X in
                    f(X)
             for higher precision differentiation or integration with uneven measurements.
    """
    t = ensure_ndarray(t)
    dt_v = np.array(list([t[i + 1] - t[i]] for i in range(t.size - 1)))
    dt_v = np.append(dt_v, np.array([t[-1] - t[-2]]))
    return dt_v


"""
Console output
"""


def pretty_array(a):
    return np.array2string(a, precision=get_representative_decimals(np.min(a[np.nonzero(a)])), suppress_small=True)


"""
Creation
"""


def lists_to_ndarrays(*args):
    """
    Transform a series of lists into NumPy arrays, and return them contained in a parent NumPy array
    :param args: Number n of lists
    :return: Array of NumPy arrays
    """
    import inspect
    args, _, _, values = inspect.getargvalues(inspect.currentframe())
    inputs = np.array(values["args"], dtype=object).squeeze()
    for i in range(len(inputs)):
        if isinstance(inputs[i], np.ndarray):
            pass
        else:
            inputs[i] = np.array(inputs[i])
    return inputs