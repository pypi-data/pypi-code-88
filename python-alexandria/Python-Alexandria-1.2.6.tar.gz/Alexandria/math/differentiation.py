import numpy as np
from scipy.interpolate import UnivariateSpline

from Alexandria.math.algorithms import largest_prime_factor

from Alexandria.constructs.array import find_nearest_entry


def derivative(x, y):
    n = largest_prime_factor(len(x))
    _x = x[0::n]
    _y = y[0::n]
    return UnivariateSpline(_x, _y).derivative()(x)


def forward_euler(x, y, x0=None):
    point = lambda u, w=0: u[find_nearest_entry(x, x0 if not isinstance(x0, type(None)) else x[0])[0] + w]
    return (point(y, 1) - point(y))/(point(x, 1) - point(x))
