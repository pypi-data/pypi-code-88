# author: Drew Botwinick, Botwinick Innovations
# title: inflections and fitting support libraries for python 2 [inflit]
# license: 3-clause BSD

import numpy as np
from scipy.fftpack import fft, fftfreq
from scipy.interpolate import Akima1DInterpolator
from scipy.signal import find_peaks_cwt, savgol_filter

from .series import thin_series_data


# region Generic Supporting Functions

def _window_size_1d(arr_size, window_size, force_odd=True):
    # window_size between 0 and 1 means take the value to be a percentage of the total size
    if 0 < window_size < 1:
        window_size = int(window_size * arr_size)

    if force_odd and window_size % 2 == 0:  # force window size to be odd
        window_size += 1

    return window_size


def _arg_sign_changes(data):
    dnz = data.nonzero()
    return dnz[0][np.where(np.abs(np.diff(np.sign(data[dnz]))) == 2)[0]]


def _arg_fft_threshold_freq(data, threshold=0.5, method='abs'):
    data = np.asarray(data)
    spectrum = fft(data)
    freq = fftfreq(data.size)
    if method == 'abs':
        t = spectrum.min() + abs(spectrum.max() - spectrum.min()) * threshold
        return freq[np.abs(spectrum) > t]
    else:
        raise ValueError('invalid method: "%s"' % method)


# endregion

# region Filtering and Application


def apply_function_to_segments(x, y, subset_boundaries, function):
    """
    Apply a function to subsets of a coordinate dataset where each set is bounded by given indices.

    The intention of this function is to apply some some sort of operator to portions of a curve bounded
    by inflection points. By separating on inflection points, the behaviors of the curve can be preserved
    while using more generic/simplified operators on each segment.

    :param x: array of x-coordinate values
    :param y: array of y-coordinate values
    :param subset_boundaries: list/array of indices that represent the boundaries of each subset / segment
    :param function: a function with signature fn(x,y) where x and y are both 1D coordinate value arrays, it should
    return a new/updated 1D y coordinate array that should represent the updated values for that segment
    :return: (x_, y_) containing the updated x coordinates [should actually be the same?] and updated y coordinates
    """
    x = np.asarray(x)
    y = np.asarray(y)

    # empty lists that will contain results from isolated segments (i.e. regions between inflection points)
    x_ = []
    y_ = []

    # calculation for a particular segment
    def calc_segment(pos, edge):
        sub_x = x[pos:edge + 1]
        sub_y = y[pos:edge + 1]
        # sub_gradient = np.gradient(sub_y)

        sub_y_ = function(sub_x, sub_y)

        x_.append(sub_x)
        y_.append(sub_y_)

    # run through segments, bounded by inflection points, and calculate each one
    pos = 0
    for edge in subset_boundaries:
        calc_segment(pos, edge)
        pos = edge + 1
    if pos < x.size:
        calc_segment(pos, x.size - 1)

    # consolidate into 1 set of data
    x_ = np.concatenate(x_)
    y_ = np.concatenate(y_)

    return x_, y_


# endregion

# region PPoly Data Fit and Filter

def pp_fit_1d(x, y, thin=True, rtol=0, atol=1E-06, poly='akima'):
    if thin:
        x, y = thin_series_data(x, y, rtol, atol)

    if poly == 'akima':
        return Akima1DInterpolator(x, y)
    # TODO: implement additional poly fit methods
    else:
        raise ValueError('invalid poly fit method: "%s"' % poly)
    pass


# noinspection PyIncorrectDocstring
def pp_signal_peaks(t, a, p=50, sign=0, **kwargs):
    """
    Function to produce "peaks" from a time-series (or similar) signal. Peaks are determined
    by searching for inflection points with an (absolute) value greater than the p-th percentile.

    Note that this function assumes that the amplitude range crosses the axis a=0.

    :param t: times (x values) [...]
    :param a: amplitudes (y values) [...]
    :param p: percentile for determining peaks [1, 99]
    :param sign: desired sign of peaks (+1/0/-1); positive peaks / any peaks / negative peaks
    :param ret: what to return and in what order, string, default = 'tp'; options are:
            't' = inflection times [associated with inflection points]
            'p' = inflection points
            'f' = function [polyfit function]
            'd' = derivative [polyfit derivative function]
    :param return_fn: whether or not to return the function, default is False. Deprecated. New code shouldn't use this.
    :param return_der: whether or not to return the derivative, default is False. Deprecated. New code shouldn't use this.
    :param kwargs: any additional kwargs are passed through to 'pp_fit_1d' which backs the interpolation routines
    :return: (t', a'); resulting times and peaks; also fn if 'return_fn' == True, also derivative if 'return_der' == True
    """

    ret = kwargs.pop('ret', 'tp')  # default is inflection times, inflection points
    # for backwards compatibility (why I'm preserving that when so few things use this I don't know...)
    if kwargs.pop('return_fn', False) and 'f' not in ret:
        ret += 'f'
    if kwargs.pop('return_der', False) and 'd' not in ret:
        ret += 'd'

    fn = pp_fit_1d(t, a, **kwargs)  # piecewise fit function
    der = fn.derivative()  # calculate derivative
    it = der.roots()  # inflection times  # TODO: option to return inflection point times?
    ip = fn(it)  # values at inflection points  # TODO: option to return inflection point values?
    target = np.percentile(np.abs(a), p)  # target abs percentile value

    if sign > 0:
        subset = ip > target
    elif sign < 0:
        subset = ip < -target
    else:  # any peaks (use absolute filter)
        subset = np.abs(ip) > target

    ret_prototype = 'tpfd'  # character string aligned to results list
    results = [it[subset], ip[subset], fn, der]  # list of results, in order matching ret_prototype
    # return ordered subset of results list leveraging ret characters location in ret_prototype
    return tuple([results[ret_prototype.index(r)] for r in ret])


# endregion

# region Inflection Points (1D, Experimental, Old)

def inflection_points_1d(y, window_size=0.01, method='cwt'):
    """
    Determine inflection points for a 1D dataset. It is generally assumed that the positions/order of the 1D dataset
    is meaningful, i.e. that the dataset is the output of a single function over a particular domain.

    :param y: 1D array of data points
    :param window_size: either a float between 0 and 1 (exclusive) that contains the percentage of data that
    should be in each window (i.e. 0.05 means 5% of the dataset) or if an integer > 1, then the exact size of
    the window
    :param method: method by which to determine the derivative of the given function (data points):

    method = 'savgol': Use 2x Savgol Filters to smooth a dataset, calculate its derivative, and
    look for where the sign flips between positive and negative to indicate inflection points.
    method = 'gradient': Compute the gradient of the dataset, look for sign flips
    method = 'cwt': Smooth data using cwt and look for peaks, uses window_size to calculate widths for the
    CWT matrix.

    :return: numpy array of indices [corresponding to positions in the given y array] of inflection points
    """
    y = np.asarray(y).squeeze()
    assert len(y.shape) == 1
    window_size = _window_size_1d(y.size, window_size, force_odd=True)

    if method == 'savgol':
        y_ = savgol_filter(y, window_size, polyorder=4, deriv=0)
        d = np.round(savgol_filter(y_, window_size, polyorder=3, deriv=1), 7)
        result = _arg_sign_changes(d)
        # TODO: use fft freq to find noise/oscillations and collapse neighboring segments that have similar signals
    elif method == 'gradient':
        d = np.gradient(y)
        # noinspection PyTypeChecker
        result = _arg_sign_changes(d)
        # TODO: use fft freq to find noise/oscillations and collapse neighboring segments that have similar signals
    elif method == 'cwt':
        result = find_peaks_cwt(y, np.arange(int(0.10 * window_size) or 1, window_size))
    else:
        raise ValueError('unrecognized method: "%s"' % method)

        # pass2 = []
        # i0 = 0  # last index
        # for i1 in pass1:
        #     if i1 == i0:
        #         continue
        #
        #     pass
        # result = pass1
    # else:
    #     result = []

    # TODO: look for close inflection points, (relative to window_size?), and collapse them if "reasonable"...

    return result


def _inflection_points_time_series(t, y, noise_uniqueness_threshold=70):
    """
    Experimental Approach to filter out time series inflection points using an approach that is
    over-engineered.

    The idea is that 'bad' data tends to involve oscillations between similar values, while good data tends
    to be more dynamic, so looking for more uniqueness in the gradient of the values is a good indicator of
    where there is value.

    This is kept here because it might be worth fixing up properly at some point and using again, but for
    the moment, it's use is strongly discouraged since it is incomplete and not validated.

    :param t:
    :param y:
    :param noise_uniqueness_threshold:
    :return:
    """
    times = np.asarray(t)
    positions = np.asarray(y)

    dp = np.abs(np.gradient(positions))
    # dpt = times[dp.nonzero()]
    # dps = dp[dp.nonzero()]

    # this can probably be done better, but still deciding what I want, so doing it manually to figure out details
    # basically a window-view of gradient data for a fixed time ranges
    time_bin_count = int((times.max() - times.min()) / 15.0)  # break into 15ms windows
    bin_width = len(times) / time_bin_count
    time_bins = np.zeros((time_bin_count, 2), dtype=np.int64)
    bin_variance = np.zeros(time_bin_count)  # TODO: remove bin_variance if it's not being used...
    bin_unique = np.zeros(time_bin_count)

    pos = 0
    for b in range(time_bin_count):
        bin_end = pos + bin_width + 1
        if bin_end > times.size:
            bin_end = times.size
        bin_variance[b] = np.var(dp[pos:bin_end], ddof=1)
        bin_unique[b] = np.unique(dp[pos:bin_end]).size
        time_bins[b,] = pos, bin_end - 1
        pos = bin_end

    prop_unique = bin_unique / np.diff(time_bins, axis=1).squeeze()
    threshold = np.percentile(prop_unique, noise_uniqueness_threshold)

    # this is meant to be a more flexible approach (dynamic bins)
    # threshold = 1.0 - np.percentile(prop_unique, unique_threshold_parameter)
    # inflection_indices = []
    # pos = 0
    # for t in xrange(1, times.size):
    #     subset = dp[pos:t + 1]
    #     subset = subset[np.abs(subset) > 1E-05]
    #     if subset.size > 0 and float(subset.size - np.unique(subset).size) / subset.size > threshold:
    #         inflection_indices.append(t)
    #         pos = t
    #     pass
    #
    # inflection_indices = np.asarray(inflection_indices)
    inflection_indices = time_bins[prop_unique > threshold][:, 1]

    return inflection_indices


# endregion

# region Median Absolute Deviation


def _mad_outlier(points, threshold=3.5):
    """
    Returns a boolean array with True if points are outliers and False
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor.
    """

    if len(points.shape) == 1:
        points = points[:, None]
    median = np.median(points, axis=0)
    diff = np.sqrt(np.sum((points - median) ** 2, axis=-1))
    mad = np.median(diff)

    modified_z_score = 0.6745 * diff / mad

    return modified_z_score  # > threshold


def mad_outlier_windows(points, window_size=25, window_overlap=0.5, threshold=3.5):
    overlap = int(window_overlap * window_size)
    windows = range(0, len(points), overlap)
    hit_count = np.zeros_like(points, dtype=np.float64)
    for window in windows:
        hit_count[window:window + window_size + 1] += _mad_outlier(points[window:window + window_size + 1])

    return hit_count > threshold


def median_abs_deviation_filter_1d(y, threshold=3, window_size=0.05):
    y = np.asarray(y).squeeze()
    assert len(y.shape) == 1
    window_size = _window_size_1d(y.size, window_size, force_odd=False)

    pass

# endregion
