# author: Drew Botwinick, Botwinick Innovations
# title: math / precision related functions
# license: 3-clause BSD

import numpy as np

_py_round = round


# noinspection PyShadowingBuiltins
def round(value, precision=6):
    """
    Override function that mimics the functionality of python's round except:
    1) The default precision is 6 decimal places
    2) Rounding values of negative zero results in positive zero

    :param value: value to round and scrub
    :param precision: rounding precision
    :return: rounded value
    :rtype: float
    """
    value = _py_round(value, precision)  # perform rounding
    if value == -0.0:  # I just think negative zero is ugly; not sure if it'd be a problem or not...
        value = 0.0
    return value


def snap_to_increment(value, inc, offset=0.0):
    """
    Snap given value(s) to a given increment/base (with option for offset). For example, counting by 5s or 0.5s, etc.

    This is meant to provide similar functionality to functions used for sorted arrays without requiring the existence
    of the array if it's a uniform grid pattern.

    TODO: add nearest, left, right snapping preferences to this function

    :param value: the value or values to adjust. Assumed it will be a float or numpy array.
    :param inc: The increment or base value (e.g. 5 or 0.5 or 0.25, etc.). Our precision in a way...
    :param offset: An optional offset, We might want to be counting by 5s from 1 (e.g. 1, 6, 11, ...) so offset allows that.
    :return: new value or values.
    """
    return inc * np.around(value / inc) + offset


def precise_tuple(values, precision=4):
    if precision is not None:
        return tuple([round(v, precision) for v in values])
    return tuple(values)


def precise_list(values, precision=4):
    if precision is not None:
        return [round(v, precision) for v in values]
    return list(values)
