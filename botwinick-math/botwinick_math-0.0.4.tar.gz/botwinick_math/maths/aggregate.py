# author: Drew Botwinick, Botwinick Innovations
# title: occasionally trivial support functions for aggregating data for python 2/3 [only numpy as dependency]
# NOTE: these functions are generally tested meant for 1D although they may apply or be easily extended to nd
# license: 3-clause BSD

import numpy as np

flat_max = np.max
flat_min = np.min
flat_percentile = np.percentile
flat_mean = np.average


def flat_abs_maximum(data, preserve_sign=True):
    """
    Function to return the absolute maximum value in an array. By default,
    this function will preserve the sign, meaning that if an array contains [-75, -25, 0, 25, 50]
    then the function will return -75 because that value has the highest magnitude but it will return
    the original value (preserving the sign).

    Removing the sign preservation basically makes this function a composite of abs and max.

    :param data: data array source
    :param preserve_sign: whether or not to preserve the sign of the output, default is True
    :return: largest absolute value in the data array
    """
    data = np.asarray(data)
    abs_data = np.abs(data)
    subset = np.unravel_index(np.argmax(abs_data), data.shape)
    return data[subset] if preserve_sign else abs_data[subset]


def flat_abs_minimum(data, preserve_sign=True):
    """
    Function to return the absolute minimum value in an array. Note that, by default, this function will
    reserve the sign.

    For example, if an array contains [-100, -24, 1, 2] then the function will return 1 because that value
    has the smallest magnitude. If an array contained [-100, -50, -2, -1] the the function would return -1
    because that value has the smallest magnitude; however, the sign would preserved (by default).

    Removing the sign preservation basically makes this function a composite of abs and min.

    :param data: data array source
    :param preserve_sign: whether or not to preserve the sign of the output, default is True
    :return: smallest absolute value in the data array
    """
    data = np.asarray(data)
    abs_data = np.abs(data)
    subset = np.unravel_index(np.argmin(abs_data), data.shape)
    return data[subset] if preserve_sign else abs_data[subset]


def partition_top(data, n, return_indices=False):
    """
    Function to return the average of the top n values in an array

    :param data: data array source
    :param n:  the number of values of interest (n)
    :param return_indices: whether to return the indices array
    :return: top n values if n < data.size or all values if n is None, <=0 or >= data.size, also index array if `return_indices`
    """
    data = np.asarray(data)
    if n is None or n <= 0 or n >= data.size:
        return data
    n = min(data.size, n) - 1
    idx = np.argpartition(data, n)[:n]
    result = data[idx]
    if return_indices:
        return result, idx
    return result


def flat_top_average(data, n):
    """
    Function to return the average of the top n values in an array

    :param data: data array source
    :param n:  the number of values of interest (n)
    :return: average of top n values if n < data.size or average of data if n > data.size
    """
    return np.average(partition_top(data, n, return_indices=False))
