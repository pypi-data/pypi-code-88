# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

from bisect import bisect_left, bisect_right
from math import copysign, fabs

import numpy as np


# region Sorted Array VALUE Functions

def snap_to_nearest_edge(x, arr):
    """
    For a sorted array `arr`, return the value in `arr` that is nearest to the provided `x`.

    This is typically used for cartesian grid calculations. That is, determine the nearest
    edge/grid line to the given value.

    :param x: target value
    :param arr: sorted list of values
    :return: value from `arr` with smallest absolute difference from `x`
    """
    hi = bisect_right(arr, x)
    if hi == 0:
        return arr[0]  # should we just return the value if we're outside the bounds?
    elif hi == len(arr):
        return arr[-1]  # should we just return the value if we're outside the bounds?
    else:
        return min(arr[hi - 1], arr[hi], key=lambda v: abs(v - x))


def snap_to_nearest_edge_np(x, arr):
    """
    Similar to `snap_to_nearest_edge` except implemented with numpy (and via index) instead of bisect.

    :param x: target value
    :param arr: sorted list of values
    :return: value from `arr` with smallest absolute difference from `x`
    """
    idx = np.searchsorted(arr, x, side='left')
    if idx > 0 and (idx == len(arr) or fabs(x - arr[idx - 1]) < fabs(x - arr[idx])):
        return arr[idx - 1]
    else:
        return arr[idx]


def snap_to_mid(x, arr):
    """
    For a sorted array `arr`, return the midpoint of the two values that surround the provided `x`
    (as much as possible). If `x` sits outside the array, then the midpoint of the last pair of
    values in the array is used.

    This is typically used for cartesian grid calculations. That is, determine the midpoint of the
    grid cell that the given value falls into.

    :param x: target value
    :param arr:  sorted list of values
    :return: midpoint of pair of values from `arr` that surround (or edge pair if `x` is outside the range of `arr`)
    """
    lo = bisect_left(arr, x)
    hi = lo + 1
    if hi >= len(arr):  # nothing to snap to, so we just assume we should use the last grid cell
        hi = len(arr) - 1
        lo = hi - 1
    return 0.5 * (arr[lo] + arr[hi])  # return midpoint


# endregion

# region Sorted Array INDEX (or hybrid) Functions

# TODO: develop more numpy-oriented functions, these functions originally tried to minimize numpy usage for some terrible reason...

def snap_to_edge(x, arr, lean='nearest', return_index=False, return_value=True):
    """
    Utility function to handle getting indices and/or values that correspond with a given x in a given sorted array. The
    function supports "leaning" to the left, nearest, or right edge within the sorted array.

    This function goes a little overboard being configurable since it is used internally in a lot of places...

    And there is no point in using this function if both `return_index` and `return_value` are false,
    but no checks are performed to identify thoughtless programmers.
    If you want to do that, who am I to stop you?!

    :param x: the value to locate
    :param arr: the sorted array in which to locate the value
    :param lean: whether to lean "left", "right", or "nearest";
    for "nearest", if the surrounding values are equidistant, the lean is to the left
    :param return_index: boolean that indicates the result should include the index
    :param return_value: boolean that indicates the result should include the value
    :return: (value, index); value; index; None; result depends on `return_index` and `return_value`.
    The value comes before the index in a tuple if both `return_index` and `return_value` are true.
    """
    # TODO: inclusion/edge settings?
    # TODO: change return_* to a string that also lets the user specify the return order (e.g. 'i', 'v', 'iv', or 'vi')

    i = bisect_right(arr, x)
    if i == 0:  # left-most edge is an edge, so we keep it...
        pass  # preserve i == 0 / no further actions required
    elif i == len(arr):  # right-most edge is an edge already
        i -= 1
    elif lean == 'left' and x >= arr[i - 1]:  # seeking left edge but overstepped, so back up
        i -= 1
    elif lean == 'nearest':  # nearest is based on array value distance
        i = min(i - 1, i, key=lambda index: abs(arr[index] - x))
    elif lean == 'right' and x == arr[i - 1]:  # if we overstepped, back up
        i -= 1
    elif lean not in ('left', 'nearest', 'right'):
        raise ValueError("lean must be either 'left', 'nearest', or 'right'")

    # (arr is not None and len(arr) > 0) is done to maintain compatibility with any iterables including numpy arrays
    if return_value and (arr is not None and len(arr) > 0) and not return_index:
        return arr[i]
    elif return_index and return_value and (arr is not None and len(arr) > 0):
        return arr[i], i
    elif return_index and not return_value:
        return i
    elif return_index and return_index and (arr is None or len(arr) == 0):  # TODO: [REVIEW] what was my intention here??
        return None, i
    return None


def index_of(x, arr, lean='nearest'):
    """
    Return the index associated with the value x for the given arr. The lean
    is the rule-set for the result--options are: left, right, nearest.
    :param x:
    :param arr:
    :param lean:
    :return:
    """
    return snap_to_edge(x, arr, lean, return_index=True, return_value=False)


def index_restrict(i, arr):
    """
    Quick Internal Function - ensure that index i is appropriately bounded for the given arr;
    i.e. 0 <= i < len(arr)
    :param i:
    :param arr:
    :return:
    """
    if i < 0:
        i = 0
    elif i > len(arr) - 1:
        i = len(arr) - 1
    return i


def index_filter(lo=None, hi=None, size=None, left_offset=0, right_offset=0, slice_adjust=0):
    """
    Utility function that accepts either None or possible index boundaries for an array of given size and
    "edge offset" characteristics and returns corrected lower and upper bound indices.

    The "edge offset" approach is that there may be a number of indices that are 'unavailable' on
    either the left/bottom edge and/or right/top edge of the indices. This can be particularly true for
    sorted arrays used for grids--e.g. there may be an extra set of values at the boundaries that aren't
    meaningful for the problem at hand--so the left and right offsets might both be 1. For a general
    case sorted array, both edge offset values would be 0--and this is the default case for the function.

    :param lo: the "requested" lower bound target (or None to mean the lower bound itself)
    :param hi: the "requested" upper bound target (or None to mean the upper bound itself)
    :param size: the size of the array or set of indexed values in question
    (this is actually REQUIRED, despite the function signature providing a default of None)
    :param left_offset: the left edge offset, defaults to zero
    :param right_offset: the right edge offset, defaults to zero
    :param slice_adjust: value to add to right edge on return, defaults to zero, can be set to 1 if producing slicing parameters
    :return: tuple of (lo, hi); values corrected for the size and edge offsets
    """
    lo = left_offset + (lo if lo is not None else 0)
    hi_limit = left_offset + size - right_offset
    # ensure that boundaries are within acceptable domain
    if lo < left_offset:
        lo = left_offset
    if hi is None:
        hi = hi_limit
    else:
        hi += left_offset
        if hi > hi_limit:
            hi = hi_limit
    return lo, hi + slice_adjust


def index_subset(start, stop, arr, return_values=False, use_nearest=False):
    """
    Return the index boundaries for the subset of a sorted array that FULLY encloses
    the given start and stop values range.

    :param start: minimum value in range (None substitutes 0th entry in arr)
    :param stop: maximum value in range (None substitutes last entry in arr)
    :param arr: sorted array of numeric values
    :param return_values: boolean whether to include the values corresponding to the resulting indices
    :param use_nearest: find the nearest edges to boundaries rather than guaranteeing FULL enclosure
    :return: (lo_index, hi_index); if return_values==True then: (lo_index, hi_index), (lo_value, hi_value)
    """
    # start and stop defaults are provided for convenience for certain usages where only one of start/stop is defined
    if start is None:  # default for start is minimum value if None is given
        start = arr[0]
    if stop is None:  # default for stop is maximum value if None is given
        stop = arr[-1]

    low, ilo = snap_to_edge(min(start, stop), arr, 'left' if not use_nearest else 'nearest', return_index=True, return_value=True)
    high, ihi = snap_to_edge(max(start, stop), arr, 'right' if not use_nearest else 'nearest', return_index=True, return_value=True)

    # TODO: add functionality to control 'extra' border cells??

    if return_values:
        return (ilo, ihi), (low, high)
    return ilo, ihi


def escape_distance(i, arr, arr2, direction, return_signed=False):
    """
    Index Distance to travel within arr (starting from i) such that the value is not in arr2

    :param i:
    :param arr:
    :param arr2:
    :param direction: integer of +1 or -1 for positive or negative direction
    :param return_signed: whether or not to returned a signed (+/-) value; False (default) is just magnitude
    :return:
    """
    delta = int(copysign(1, direction))
    position = i
    while 0 <= position < len(arr):
        if arr[position] not in arr2:  # TODO: floating point comparison tolerance
            break
        position += delta
    distance = int((abs(position - i)))
    if return_signed:
        return int(copysign(distance, delta))
    return distance


def range_shift(lo, hi, arr, directed_distance):  # partial=None
    # if we're only shifting 1, then we 'partially' shift the range /
    # that is, we only shift one of the hi or lo direction, the other stays at the edge of where it was previously
    # but if we need to move multiple steps, then we need to fully shift the range over

    if directed_distance < 0:
        new_lo = index_restrict(lo + directed_distance, arr)
        new_hi = index_restrict(hi + directed_distance + 1, arr)
    elif directed_distance > 0:
        new_lo = index_restrict(lo + directed_distance - 1, arr)
        new_hi = index_restrict(hi + directed_distance, arr)
    else:
        new_lo = lo
        new_hi = hi
    return new_lo, new_hi


def index_split_range_on_alternate_list(lo, hi, arr, arr2, return_as_values=True, repair_arr_in_place=False):
    """
    Split a given lo, hi range into multiple ranges based on a subset of values of arr provided in arr2

    :param lo: index range lower bound (from)
    :param hi: index range upper bound (to)
    :param arr: full sorted list of array data (in)
    :param arr2: subset of sorted array data to split on (split on)
    :param return_as_values: whether to return value pairs or index pairs (True = values, False = index pairs)
    :param repair_arr_in_place: if not all of the values from arr2 are in arr, then the missing values will be added to arr
    and arr will be sorted in-place. This allows for 'on-the-fly' repairs of arr by reference, but is somewhat beyond the
    expected scope of this function and likely belongs elsewhere--but it's somewhat convenient here since it makes it
    easier to make use of this function given that it is intended for use when all of arr2 is contained in arr.
    :return:
    """
    if not arr2:  # really nothing to do if we don't have any fixed lines...
        indices = [(lo, hi)]
    else:
        # the fixed_lines must be part of the array - using np all close because equality is tough...
        # line in arr for line in arr2
        arr2_in_arr_hits = [np.allclose(line, arr[index_of(line, arr)]) for line in arr2]
        if not all(arr2_in_arr_hits) and not repair_arr_in_place:
            raise RuntimeError('Not all lines in arr2 are in arr for `index_split_range_on_alternate_list`')
        elif not all(arr2_in_arr_hits):
            # go through all misses and add them to arr
            for i, hit in enumerate(arr2_in_arr_hits):
                if not hit:
                    arr.append(arr2[i])  # add missing entries
            arr.sort()  # re-sort in place

        start, stop = arr[lo], arr[hi]
        (fl_lo, fl_hi), (fl_start, fl_stop) = index_subset(start, stop, arr2, return_values=True, use_nearest=True)
        matches = [arr[i] in arr2 for i in range(lo, hi + 1)]

        # if fully enclosed or outside boundaries then there is nothing to do...
        if all(matches) and hi - lo >= 1:  # if includes all fixed lines, then boundaries only?
            # FIXME: this needs work to be finished...
            # lo_escape = escape_distance(lo, arr, arr2, -1)
            # hi_escape = escape_distance(hi, arr, arr2, +1)
            # indices = [range_shift(lo, lo, arr, -lo_escape, partial=True),
            #            range_shift(hi, hi, arr, hi_escape, partial=True)]
            indices = [(index_restrict(lo - 1, arr), lo), (hi, index_restrict(hi + 1, arr))]
        elif (start >= fl_start and stop <= fl_stop) or stop <= fl_start or start >= fl_stop:
            indices = [(lo, hi)]  # so just return a list with the original range
        # elif lo == hi and fl_start == start:  # single index equal to a fixed line! do something different??
        #     # then return a pair of indices on either side of the fixed line
        #     indices = [(index_restrict(lo - 1, arr), hi), (lo, index_restrict(hi + 1, arr))]
        else:
            stops = sorted(set(
                [lo] +
                [index_of(line, arr) for line in arr2[fl_lo:fl_hi + 1] if start <= line <= stop] +
                [hi]))
            indices = [(stops[i], stops[i + 1]) for i in range(len(stops) - 1)]

            # TODO: review if this stripping operation should be in here...
            # strip out index ranges that are entirely composed of values from arr2
            indices = [(i, j) for (i, j) in indices if not all(arr[k] in arr2 for k in range(i, j + 1))]

    if not return_as_values:
        return indices
    return [(arr[i], arr[j]) for (i, j) in indices]


# endregion


def replace_subset(lo, hi, arr, new_values, unique_resort=False):
    """
    Replace a subset of a sorted arr with new_values. Can also ensure the resulting outcome is unique and sorted
    with the unique_resort option.

    :param lo:
    :param hi:
    :param arr:
    :param new_values:
    :param unique_resort:
    :return:
    """
    result = arr[:lo] + new_values + arr[hi + 1:]
    if unique_resort:
        result = sorted(set(result))
    return result


def precision_limited_unique_sorted_list(data, precision=6):
    if isinstance(data, (float, int)):
        data = [data]
    # noinspection PyTypeChecker
    return [float(v) for v in np.unique(np.around(data, decimals=precision))]


def np_concat_sorted_unique(*arrays):
    return np.unique(np.hstack(tuple(arrays)))
