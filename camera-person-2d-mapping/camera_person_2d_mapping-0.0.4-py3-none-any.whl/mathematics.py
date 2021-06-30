import math

import numpy as np
from typing import Any, Callable

from .models import Line, Coord2D


def intersection(l0: Line, l1: Line) -> Coord2D:
    """
    Calculates the :class:`Coord2D` of intersection between the two provided :class:`Line` objects.
    :param l0: first line.
    :param l1: second line.
    :return: the :class:`Coord2D` of intersection between the two provided :class:`Line` objects.
    """
    a1 = l0.p1.y - l0.p0.y
    b1 = l0.p0.x - l0.p1.x
    c1 = a1 * l0.p0.x + b1 * l0.p0.y

    a2 = l1.p1.y - l1.p0.y
    b2 = l1.p0.x - l1.p1.x
    c2 = a2 * l1.p0.x + b2 * l1.p0.y

    det = a1 * b2 - a2 * b1

    if det == 0:
        return Coord2D(math.inf, math.inf)

    x = ((b2 * c1) - (b1 * c2)) / det
    y = ((a1 * c2) - (a2 * c1)) / det
    return Coord2D(round(x), round(y))


def linear_equation_function(x: np.ndarray, y: np.ndarray) -> Callable[[Any], float]:
    """
    Builds a linear equation function given the x and y arrays.

    :param x: independent variable array.
    :param y: dependent variable array.
    :return: a linear function built from the two provided arrays.
    """
    x = x.reshape((1, x.shape[0])).T
    x = np.concatenate((x, np.ones(x.shape)), axis=1).astype(np.float64)
    y = y.astype(np.float64)
    w = np.linalg.lstsq(x, y, rcond=None)[0]
    return lambda value: np.dot(np.concatenate((np.array([value]), np.array([1]))), w)
