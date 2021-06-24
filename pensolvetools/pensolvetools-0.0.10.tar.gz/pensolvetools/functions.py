import numpy as np


def small(x, n):
    a = np.sort(x)
    return a[n-1]


def large(x, n):
    a = np.sort(x)[::-1]
    return a[n-1]


def linest(ys, xs, const=True, stats=False):
    if const:
        return np.array(np.mean(ys / xs))  # This may not be correct?
    else:
        return np.polyfit(xs, ys, 1)


def geomean(x):
    a = np.log(x)
    return np.exp(a.sum()/len(a))


def match(x0, x, match_type=1):
    if match_type == 0:
        return np.where(np.array(x) == x0)[0][0].item()
    elif match_type == -1:
        return len(x) - np.searchsorted(np.array(x)[::-1], x0, side="left")
    elif match_type == 1:
        return np.searchsorted(x, x0, side="right") - 1


def p_max(params):
    p_all = []
    for param in params:
        if hasattr(param, "__len__"):
            if param.size == 1:
                param = [np.asscalar(param)]
            p_all += list(param)
        else:
            p_all += [param]
    return max(p_all)


def p_min(params):
    p_all = []
    for param in params:
        if hasattr(param, "__len__"):
            if param.size == 1:
                param = [np.asscalar(param)]
            p_all += list(param)
        else:
            p_all += [param]
    return min(p_all)


def p_sum(params):
    p_all = 0
    for param in params:
        if hasattr(param, "__len__"):
            p_all += sum(param)
        else:
            p_all += param
    return p_all


def lookup(x, x0, y, approx=True):
    """
    Equivalent to the spreadsheet LOOKUP,
    but supports the approx option like VLOOKUP

    :param x:
    :param x0:
    :param y:
    :param approx:
    :return:
    """
    if isinstance(x[0], str):
        x0 = str(x0)
    if not approx:  # need exact match
        return y[np.where(x0 == x)[0][0]]
    else:
        inds = np.searchsorted(x, x0, side='right') - 1
        return y[inds]


def vlookup(x0, vals, ind, approx=True):
    """
    Equivalent to the spreadsheet VLOOKUP function

    :param vals: array_like
        2d array of values - first column is searched for index
    :param x0:
    :param ind:
    :param approx:
    :return:
    """
    if isinstance(vals[0][0], str):
        x0 = str(x0)
    if not approx:  # need exact match
        return vals[int(ind)][np.where(x0 == vals[0])[0][0]]
    else:
        inds = np.searchsorted(vals[0], x0, side='right') - 1
        return vals[ind][int(inds)]


# def lookup(x0, x, y=None):  # TODO: delete
#     if y is None:
#         y = x
#     inds = np.searchsorted(x, x0, side='right') - 1
#     return y[inds]


def p_or(**args):
    if len(args) != 2:
        return np.logical_or.reduce(np.array(args))
    return np.logical_or(*args)


def p_and(**args):
    if len(args) != 2:
        return np.logical_and.reduce(np.array(args))
    return np.logical_and(*args)


def concat(parts):
    return ''.join([str(x) for x in parts])


class SheetObj(object):
    pass
