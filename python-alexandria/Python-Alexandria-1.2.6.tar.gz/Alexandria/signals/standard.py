import numpy as np

from Alexandria.math.differentiation import forward_euler

from Alexandria.constructs.array import find_nearest_entry


def u(t):
    return np.array([1 if i > 0 else 0 for i in t]).flatten()


def r(t):
    return np.array([max(0, i) for i in t]).flatten()


def square(f, t):
    """
    :param f: Signal formula
    :param t: Time vector
    :return:  Signal vector
    """
    base           = 1/forward_euler(t, f)
    center_idx     = find_nearest_entry(f, 0)[0]
    center         = t[center_idx]
    l_idx          = find_nearest_entry(t, center - base/2)[0]
    u_idx          = find_nearest_entry(t, center + base/2)[0]

    s              = np.zeros(t.shape)
    s[l_idx:u_idx] = 1

    return s


def triangular(f, t):
    s = np.convolve(square(f, t), square(f, t), 'same')
    s = s/s.max()
    return s

