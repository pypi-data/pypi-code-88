# author: Drew Botwinick, Botwinick Innovations
# title: occasionally trivial support functions for merging data for python 2/3 [only numpy as dependency]
# license: 3-clause BSD

import numpy as np

nd_max = np.maximum
nd_min = np.minimum
nd_sum = np.add
nd_product = np.multiply


def nd_abs_max(d1, d2, preserve_sign=True):
    """
    Function to return the element-wise absolute maximum value in an array. By default,
    this function will preserve the sign, meaning the value with a greater magnitude will be returned
    with its original sign (so when comparing 50 to -75, the result would be -75).

    NOTE / TODO: sign preservation functionality when abs(value1) == abs(value2) is not well-defined and should be addressed

    Removing the sign preservation basically makes this function a composite of abs and maximum.

    :param d1: data array source #1
    :param d2: data array source #2
    :param preserve_sign: whether or not to preserve the signs of the output, default is True
    :return: data array containing absolute maximum values by element-wise comparison
    """
    d1, d2 = np.asarray(d1), np.asarray(d2)
    ad1, ad2 = np.abs(d1), np.abs(d2)
    if not preserve_sign:
        return np.maximum(ad1, ad2)
    return np.choose(ad1 > ad2, d1, d2)


def nd_abs_min(d1, d2, preserve_sign=True):
    """
    Function to return the element-wise absolute minimum value in an array. By default,
    this function will preserve the sign, meaning the value with a lesser magnitude will be returned
    with its original sign (so when comparing 3 to -2, the result would be -2).

    NOTE / TODO: sign preservation functionality when abs(value1) == abs(value2) is not well-defined and should be addressed

    Removing the sign preservation basically makes this function a composite of abs and minimum.

    :param d1: data array source #1
    :param d2: data array source #2
    :param preserve_sign: whether or not to preserve the signs of the output, default is True
    :return: data array containing absolute minimum values by element-wise comparison
    """
    d1, d2 = np.asarray(d1), np.asarray(d2)
    ad1, ad2 = np.abs(d1), np.abs(d2)
    if not preserve_sign:
        return np.minimum(ad1, ad2)
    return np.choose(ad1 < ad2, d1, d2)
