"""
Basic statistics module.
This module provides functions for calculating statistics of data, including
averages, variance, and standard deviation.
Calculating averages
--------------------
==================  ==================================================
Function            Description
==================  ==================================================
mean                Arithmetic mean (average) of data.
fmean               Fast, floating point arithmetic mean.
geometric_mean      Geometric mean of data.
harmonic_mean       Harmonic mean of data.
median              Median (middle value) of data.
median_low          Low median of data.
median_high         High median of data.
median_grouped      Median, or 50th percentile, of grouped data.
mode                Mode (most common value) of data.
multimode           List of modes (most common values of data).
quantiles           Divide data into intervals with equal probability.
pvariance           Population variance of data.
variance            Sample variance of data.
pstdev              Population standard deviation of data.
stdev               Sample standard deviation of data.
covariance          Sample covariance for two variables.

==================  ====================================================
A single exception is defined: StatisticsError is a subclass of ValueError.
"""

__all__ = [
    'NormalDist',
    'StatisticsError',
    'correlation',
    'covariance',
    'fmean',
    'geometric_mean',
    'harmonic_mean',
    'linear_regression',
    'mean',
    'median',
    'median_grouped',
    'median_high',
    'median_low',
    'mode',
    'multimode',
    'pstdev',
    'pvariance',
    'quantiles',
    'stdev',
    'variance',
]

import math
import numbers
import random

from fractions import Fraction
from decimal import Decimal
from itertools import groupby, repeat
from bisect import bisect_left, bisect_right
from math import hypot, sqrt, fabs, exp, erf, tau, log, fsum
from operator import itemgetter, mul
from collections import Counter, namedtuple

# === Exceptions ===

class StatisticsError(ValueError):
    pass


# === Private utilities ===

def _sum(data, start=0):
    """_sum(data [, start]) -> (type, sum, count)
    Return a high-precision sum of the given numeric data as a fraction,
    together with the type to be converted to and the count of items.
    """
    count = 0
    n, d = _exact_ratio(start)
    partials = {d: n}
    partials_get = partials.get
    T = _coerce(int, type(start))
    for typ, values in groupby(data, type):
        T = _coerce(T, typ)  # or raise TypeError
        for n, d in map(_exact_ratio, values):
            count += 1
            partials[d] = partials_get(d, 0) + n
    if None in partials:
        # The sum will be a NAN or INF. We can ignore all the finite
        # partials, and just look at this special one.
        total = partials[None]
        assert not _isfinite(total)
    else:
        # Sum all the partial sums using builtin sum.
        # FIXME is this faster if we sum them in order of the denominator?
        total = sum(Fraction(n, d) for d, n in sorted(partials.items()))
    return (T, total, count)


def _isfinite(x):
    try:
        return x.is_finite()  # Likely a Decimal.
    except AttributeError:
        return math.isfinite(x)  # Coerces to float first.


def _coerce(T, S):
    """Coerce types T and S to a common type, or raise TypeError.
    Coercion rules are currently an implementation detail. See the CoerceTest
    test class in test_statistics for details.
    """
    # See http://bugs.python.org/issue24068.
    assert T is not bool, "initial type T is bool"
    # If the types are the same, no need to coerce anything. Put this
    # first, so that the usual case (no coercion needed) happens as soon
    # as possible.
    if T is S:  return T
    # Mixed int & other coerce to the other type.
    if S is int or S is bool:  return T
    if T is int:  return S
    # If one is a (strict) subclass of the other, coerce to the subclass.
    if issubclass(S, T):  return S
    if issubclass(T, S):  return T
    # Ints coerce to the other type.
    if issubclass(T, int):  return S
    if issubclass(S, int):  return T
    # Mixed fraction & float coerces to float (or float subclass).
    if issubclass(T, Fraction) and issubclass(S, float):
        return S
    if issubclass(T, float) and issubclass(S, Fraction):
        return T
    # Any other combination is disallowed.
    msg = "don't know how to coerce %s and %s"
    raise TypeError(msg % (T.__name__, S.__name__))


def _exact_ratio(x):
    """Return Real number x to exact (numerator, denominator) pair.
    """
    try:
        # Optimise the common case of floats. We expect that the most often
        # used numeric type will be builtin floats, so try to make this as
        # fast as possible.
        if type(x) is float or type(x) is Decimal:
            return x.as_integer_ratio()
        try:
            # x may be an int, Fraction, or Integral ABC.
            return (x.numerator, x.denominator)
        except AttributeError:
            try:
                # x may be a float or Decimal subclass.
                return x.as_integer_ratio()
            except AttributeError:
                # Just give up?
                pass
    except (OverflowError, ValueError):
        # float NAN or INF.
        assert not _isfinite(x)
        return (x, None)
    msg = "can't convert type '{}' to numerator/denominator"
    raise TypeError(msg.format(type(x).__name__))


def _convert(value, T):
    """Convert value to given numeric type T."""
    if type(value) is T:
        # This covers the cases where T is Fraction, or where value is
        # a NAN or INF (Decimal or float).
        return value
    if issubclass(T, int) and value.denominator != 1:
        T = float
    try:
        # FIXME: what do we do if this overflows?
        return T(value)
    except TypeError:
        if issubclass(T, Decimal):
            return T(value.numerator) / T(value.denominator)
        else:
            raise

def _find_lteq(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def _find_rteq(a, l, x):
    'Locate the rightmost value exactly equal to x'
    i = bisect_right(a, x, lo=l)
    if i != (len(a) + 1) and a[i - 1] == x:
        return i - 1
    raise ValueError


def _fail_neg(values, errmsg='negative value'):
    """Iterate over values, failing if any are less than zero."""
    for x in values:
        if x < 0:
            raise StatisticsError(errmsg)
        yield x


# === Measures of central tendency (averages) ===

def mean(data):
    """Return the sample arithmetic mean of data.
    """
    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 1:
        raise StatisticsError('mean requires at least one data point')
    T, total, count = _sum(data)
    assert count == n
    return _convert(total / n, T)


def fmean(data, weights=None):
    """Convert data to floats and compute the arithmetic mean.
    This runs faster than the mean() function and it always returns a float.
    If the input dataset is empty, it raises a StatisticsError.
    """
    try:
        n = len(data)
    except TypeError:
        # Handle iterators that do not define __len__().
        n = 0
        def count(iterable):
            nonlocal n
            for n, x in enumerate(iterable, start=1):
                yield x
        data = count(data)
    if weights is None:
        total = fsum(data)
        if not n:
            raise StatisticsError('fmean requires at least one data point')
        return total / n
    try:
        num_weights = len(weights)
    except TypeError:
        weights = list(weights)
        num_weights = len(weights)
    num = fsum(map(mul, data, weights))
    if n != num_weights:
        raise StatisticsError('data and weights must be the same length')
    den = fsum(weights)
    if not den:
        raise StatisticsError('sum of weights must be non-zero')
    return num / den


def geometric_mean(data):
    """Convert data to floats and compute the geometric mean.
    Raises a StatisticsError if the input dataset is empty.
    """
    try:
        return exp(fmean(map(log, data)))
    except ValueError:
        raise StatisticsError('geometric mean requires a non-empty dataset '
                              ' containing positive numbers') from None


def harmonic_mean(data, weights=None):
    """Return the harmonic mean of data.
    The harmonic mean is the reciprocal of the arithmetic mean of the
    reciprocals of the data.  It can be used for averaging ratios or
    rates, for example speeds.
    If ``data`` is empty, or any element is less than zero,
    ``harmonic_mean`` will raise ``StatisticsError``.
    """
    if iter(data) is data:
        data = list(data)
    errmsg = 'harmonic mean does not support negative values'
    n = len(data)
    if n < 1:
        raise StatisticsError('harmonic_mean requires at least one data point')
    elif n == 1 and weights is None:
        x = data[0]
        if isinstance(x, (numbers.Real, Decimal)):
            if x < 0:
                raise StatisticsError(errmsg)
            return x
        else:
            raise TypeError('unsupported type')
    if weights is None:
        weights = repeat(1, n)
        sum_weights = n
    else:
        if iter(weights) is weights:
            weights = list(weights)
        if len(weights) != n:
            raise StatisticsError('Number of weights does not match data size')
        _, sum_weights, _ = _sum(w for w in _fail_neg(weights, errmsg))
    try:
        data = _fail_neg(data, errmsg)
        T, total, count = _sum(w / x if w else 0 for w, x in zip(weights, data))
    except ZeroDivisionError:
        return 0
    if total <= 0:
        raise StatisticsError('Weighted sum must be positive')
    return _convert(sum_weights / total, T)

# FIXME: investigate ways to calculate medians without sorting? Quickselect?
def median(data):
    """Return the median (middle value) of numeric data.
    When the number of data points is odd, return the middle data point.
    When the number of data points is even, the median is interpolated by
    taking the average of the two middle values.
    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2


def median_low(data):
    """Return the low median of numeric data.
    When the number of data points is odd, the middle value is returned.
    When it is even, the smaller of the two middle values is returned.
    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        return data[n // 2 - 1]


def median_high(data):
    """Return the high median of data.
    When the number of data points is odd, the middle value is returned.
    When it is even, the larger of the two middle values is returned.
    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    return data[n // 2]


def median_grouped(data, interval=1):
    """Return the 50th percentile (median) of grouped continuous data.
    This calculates the median as the 50th percentile, and should be
    used when your data is continuous and grouped. 
    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    elif n == 1:
        return data[0]
    # Find the value at the midpoint. Remember this corresponds to the
    # centre of the class interval.
    x = data[n // 2]
    for obj in (x, interval):
        if isinstance(obj, (str, bytes)):
            raise TypeError('expected number but got %r' % obj)
    try:
        L = x - interval / 2  # The lower limit of the median interval.
    except TypeError:
        # Mixed type. For now we just coerce to float.
        L = float(x) - float(interval) / 2

    # Uses bisection search to search for x in data with log(n) time complexity
    # Find the position of leftmost occurrence of x in data
    l1 = _find_lteq(data, x)
    # Find the position of rightmost occurrence of x in data[l1...len(data)]
    # Assuming always l1 <= l2
    l2 = _find_rteq(data, l1, x)
    cf = l1
    f = l2 - l1 + 1
    return L + interval * (n / 2 - cf) / f


def mode(data):
    """Return the most common data point from discrete or nominal data.
    ``mode`` assumes discrete data, and returns a single value.
    If *data* is empty, ``mode``, raises StatisticsError.
    """
    pairs = Counter(iter(data)).most_common(1)
    try:
        return pairs[0][0]
    except IndexError:
        raise StatisticsError('no mode for empty data') from None


def multimode(data):
    """Return a list of the most frequently occurring values.
    Will return more than one result if there are multiple modes
    or an empty list if *data* is empty.
    """
    counts = Counter(iter(data)).most_common()
    maxcount, mode_items = next(groupby(counts, key=itemgetter(1)), (0, []))
    return list(map(itemgetter(0), mode_items))

# === Measures of spread ===

def _ss(data, c=None):
    """Return sum of square deviations of sequence data.
    """
    if c is not None:
        T, total, count = _sum((x-c)**2 for x in data)
        return (T, total)
    c = mean(data)
    T, total, count = _sum((x-c)**2 for x in data)
    # The following sum should mathematically equal zero, but due to rounding
    # error may not.
    U, total2, count2 = _sum((x - c) for x in data)
    assert T == U and count == count2
    total -= total2 ** 2 / len(data)
    assert not total < 0, 'negative sum of square deviations: %f' % total
    return (T, total)


def variance(data, xbar=None):
    """Return the sample variance of data.
    data should be an iterable of Real-valued numbers, with at least two
    values. The optional argument xbar, if given, should be the mean of
    the data. 
    """
    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 2:
        raise StatisticsError('variance requires at least two data points')
    T, ss = _ss(data, xbar)
    return _convert(ss / (n - 1), T)


def pvariance(data, mu=None):
    """Return the population variance of ``data``.
    data should be a sequence or iterable of Real-valued numbers, with at least one
    value. The optional argument mu, if given, should be the mean of
    the data. 
    """
    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 1:
        raise StatisticsError('pvariance requires at least one data point')
    T, ss = _ss(data, mu)
    return _convert(ss / n, T)


def stdev(data, xbar=None):
    """Return the square root of the sample variance.
    """
    var = variance(data, xbar)
    try:
        return var.sqrt()
    except AttributeError:
        return math.sqrt(var)


def pstdev(data, mu=None):
    """Return the square root of the population variance.
    """
    var = pvariance(data, mu)
    try:
        return var.sqrt()
    except AttributeError:
        return math.sqrt(var)


# === Statistics for relations between two inputs ===

# See https://en.wikipedia.org/wiki/Covariance
#     https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
#     https://en.wikipedia.org/wiki/Simple_linear_regression


def covariance(x, y, /):
    """Covariance
    Return the sample covariance of two inputs *x* and *y*. Covariance
    is a measure of the joint variability of two inputs.
    """
    n = len(x)
    if len(y) != n:
        raise StatisticsError('covariance requires that both inputs have same number of data points')
    if n < 2:
        raise StatisticsError('covariance requires at least two data points')
    xbar = fsum(x) / n
    ybar = fsum(y) / n
    sxy = fsum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    return sxy / (n - 1)

