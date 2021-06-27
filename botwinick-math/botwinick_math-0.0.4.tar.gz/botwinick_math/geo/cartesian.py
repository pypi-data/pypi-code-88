# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

from math import floor as _py_floor, pi as _pi

import numpy as np
from scipy.spatial.distance import euclidean as _ssd_euclidean

from ..maths.precision import snap_to_increment as _snap

distance = _ssd_euclidean

PI = _pi
TWO_PI = _pi * 2


def normalize_angle(angle_radians, center_angle_radians=PI):
    """
    Normalize a given angle to a 2-pi interval around the 'center angle'

    :param angle_radians: angle to normalize
    :type angle_radians: float
    :param center_angle_radians: middle of target interval, default value is pi for an interval between 0 and 2-pi
    :type center_angle_radians: float
    :return: normalized angle in radians
    :rtype: float
    """
    return angle_radians - TWO_PI * _py_floor((angle_radians + PI - center_angle_radians) / TWO_PI)


def colinear_axis_aligned_check(points, atol):
    """
    Check if the given n-dimensional cartesian coordinates lie on the same *AXIS-ALIGNED* line given
    an acceptable tolerance.

    Effectively this function just checks if there is a single consistent coordinate among all of the points
    within the given tolerance.

    :param points: list of n-dimensional points that represent multiple cartesian coordinates, e.g. [[0,2], [1,2], [2,2], [3,2]]
    :param atol: absolute tolerance for comparison (1e-03 = 3 decimal places) (0.5 = w/in 0.5)
    :return:
    """
    pts = np.array(points, copy=False, ndmin=2)
    shape = pts.shape
    if shape[0] < 2:  # cannot be colinear if there aren't enough points to determine a line
        return False
    # shape must be two dimensions, d0 = number of points, must be >=2, d1 = coordinate components, must be 2D+
    assert len(shape) == 2 and shape[1] >= 2
    return np.isclose(pts[0], pts[1:], 0, atol).any()


def colinear_check_2d(points, atol=0.01):
    """
    Check if given points are colinear for a 2D points array

    :param points: array of points, e.g. [[1,2],[2,3],[10,500]]
    :param atol: comparison tolerance for related points on each axis
    :return:
    """
    if len(points) < 2:  # cannot be colinear if there aren't enough points to determine a line
        return False
    elif len(points) == 2:  # if there are only two points, then it has to be a line...
        return True

    # so here we want to process situation with 3 or more points
    pts = _snap(np.asarray(points), atol)
    shape = pts.shape
    # shape must be two dimensions, d0 = number of points, must be >=3, d1 = coordinate components, must be 2D+
    assert len(shape) == 2 and shape[1] == 2

    # TODO: use more efficient approach?, this was hacked in quickly to have a working solution for small data sets

    (x1, y1), (x2, y2) = pts[0], pts[1]
    x3, y3 = pts[2:, 0], pts[2:, 1]
    areas = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return np.asarray(areas.nonzero()).any()


def max_distance(points, return_points=False):
    """
    Return maximum distance from an array of points by comparing all points against the origin point (first entry in the array).

    Note that the current implementation is basically flawed because it compares all points against an assumed origin (points[0]).
    This means that it doesn't actually guarantee that it finds the maximum distance; however, if the given set of coordinates are
    an ordered path (e.g. from GIS), then it should still function properly (as the assumed origin is actually correct).

    :param points: array of points, e.g. [[1,2],[2,3],[10,500]]
    :param return_points: whether or not to return the points (as numpy array) or only the max distance
    :return: max distance (or tuple of (max distance, points array) if return_points is True)
    """
    pts = np.asarray(points)
    shape = pts.shape
    # shape must be two dimensions, d0 = number of points, must be >2, d1 = coordinate components, must be 2D+
    assert len(shape) == 2 and shape[0] >= 2 and shape[1] >= 2

    # TODO: this is flawed because it fixes the origin for all distance calculations so it might not be the maximum (works for paths though)
    i0 = 0
    origin = pts[i0]
    distances = np.array([distance(origin, pt) for pt in pts[1:]])

    i1 = np.argmax(distances)
    if not return_points:
        return distances[i1]
    return distances[i1], np.stack((pts[i0], pts[1 + i1]), axis=0)


class Line2D(object):
    _points = None
    _mb = None
    _dxy = None

    def __init__(self, pt1, pt2):
        """
        Simple class to represent a 2D cartesian line given two points

        :param pt1: point #1 (x,y)
        :param pt2: point #2 (x,y)
        """
        pt1, pt2 = np.asarray(pt1), np.asarray(pt2)
        assert pt1.size == pt2.size == 2
        self._points = points = np.stack((pt1, pt2), axis=0)
        dx, dy = self._dxy = np.diff(points, axis=0).squeeze()
        if dx != 0:
            m = dy / dx
            b = pt2[1] - m * pt2[0]
        else:
            m = np.nan
            b = pt2[1]
        self._mb = m, b

    def x(self, y):
        """
        Return x-value associated with the given y-value

        :param y: y-value
        :return: x-value
        """
        m, b = self._mb
        return ((y - b) / m) if m is not np.nan else np.nan

    def y(self, x):
        """
        Return y-value associated with the given x-value

        :param x: x-value
        :return: y-value
        """
        m, b = self._mb
        return (m * x + b) if m is not np.nan else b

    def fn(self, desired_axis, value):
        """
        Given an axis value (0=x, 1=y), return the other value given an input from the target axis. This function
        is useful to basically switch between function of a line or inverse by switching the input in a programmatic way.

        :param desired_axis: 0=x, 1=y; identifies the desired result
        :param value: the value associated with the "other axis". E.g. if desired_axis is x/0, then value would be y and x would be returned
        :return: other corresponding coordinate (matching the desired axis) given the input value
        """
        if desired_axis == 0:
            return self.x(value)
        elif desired_axis == 1:
            return self.y(value)
        else:
            raise ValueError('invalid axis')

    @property
    def start(self):
        """
        numpy friendly property of given starting coordinates of line
        """
        return self._points[0]

    @property
    def end(self):
        """
        numpy friendly property of given ending coordinates of line
        """
        return self._points[1]

    @property
    def slope(self):
        """
        slope of the given line
        """
        return self._mb[0]

    @property
    def intercept(self):
        """
        y-intercept for the given line
        """
        return self._mb[1]

    @property
    def dx(self):
        """
        delta x for the given coordinate pairs
        """
        return self._dxy[0]

    @property
    def dy(self):
        """
        delta y for the given coordinate pairs
        """
        return self._dxy[1]

    @property
    def dxy(self):
        """
        numpy friendly array containing [dx, dy]
        """
        return self._dxy

    pass
