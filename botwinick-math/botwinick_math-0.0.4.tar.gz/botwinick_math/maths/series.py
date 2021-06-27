# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

import numpy as np

from .sorted import index_subset


def averaging_time_windows(times, averaging_time, comparison_tolerance=0.0, avoid_overlap=False):
    """
    this is pretty old code for determining time windows for averaging times. it should be checked/vetted before
    being used too seriously.

    :param times: list of times
    :param averaging_time: time span for averaging
    :param comparison_tolerance: fudge factor to allow for easier float comparison near time step boundaries
    :param avoid_overlap: whether or not the windows should be exclusive or rolling (avoid overlap = exclusive)
    :return: list of (t_min, t_max) tuples for windows
    """
    result = []

    i = 0
    r = times[0]
    for t in times:
        # if we've hit our averaging time, then we need to save and advance
        if t - r >= averaging_time - comparison_tolerance:
            result.append((r, t))  # store result
            if i + 1 < len(times):
                i += 1
            # advance r0 when we find an averaging time
            r = times[i] if not avoid_overlap else t
    return result


def averaging_time_window_weights(times, time_windows):
    weights = []
    diffs = np.diff(times, n=1, axis=0)
    for (r, t) in time_windows:
        tlo, thi = index_subset(r, t, times, use_nearest=True)
        weights.append(diffs[tlo:thi + 1] / np.sum(diffs[tlo:thi + 1]))
    return weights


def thin_series_data(x, y, rtol=0, atol=1E-06):
    """
    Thin out time series data by removing points that are surrounded by the same (or very similar) y coordinates.

    This is a relatively conservative way to thin data.

    Note that if x and y are numpy arrays, the resulting arrays will be views of the original data.

    :param x: array of times / x-coordinates
    :param y: array of positions / y-coordinates
    :param rtol: relative tolerance
    :param atol: absolute tolerance
    :return: tuple of thinned out (x, y)
    """
    x = np.asarray(x)
    y = np.asarray(y)

    # first method just looked at adjacent points, but this caused a few errors in 'flat peaks'
    # real_variations = np.abs(np.ediff1d(y, to_begin=[0.0])) > similarity_threshold

    real_variations = np.ones(y.size, dtype=bool)
    # Aside from the 1st and last point, remove points whose y values are equal to
    # both the point before and the point after it.
    real_variations[1:-1] = np.logical_or(
        ~np.isclose(y[1:-1], y[:-2], rtol=rtol, atol=atol),
        ~np.isclose(y[1:-1], y[2:], rtol=rtol, atol=atol)
    )

    t_ = x[real_variations]
    y_ = y[real_variations]

    return t_, y_
