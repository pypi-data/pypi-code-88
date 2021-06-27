# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

from functools import cmp_to_key as _cmp2key
from itertools import combinations as _combo
from math import (atan2 as _py_atan2, cos as _py_cos, radians as _py_radians, sin as _py_sin)

import numpy as np

from .cartesian import colinear_axis_aligned_check as caac, distance, normalize_angle


def rotate_2d(x, y, theta, origin_x=0.0, origin_y=0.0):
    """
    basic 2d rotation of cartesian coordinates, uses python/c math libraries

    :param x: x coordinate float cartesian
    :param y: y coordinate float cartesian
    :param theta: angle in DEGREES (CCW / math conventions)
    :param origin_x: origin of rotation, x coordinate, default origin
    :param origin_y: origin of rotation, y coordinate, default origin
    :return: tuple of (x',y') [rotated coordinates]
    """
    if theta is None:
        return x, y
    theta = _py_radians(theta)
    x_rot = origin_x + ((x - origin_x) * _py_cos(theta) - (y - origin_y) * _py_sin(theta))
    y_rot = origin_y + ((x - origin_x) * _py_sin(theta) + (y - origin_y) * _py_cos(theta))
    return x_rot, y_rot


def calculate_tsr_2d_2p(s1a, s1b, s2a, s2b):
    """
    Given a pair of corresponding coordinates for two different 2D coordinate systems, calculate
    a translation, scaling factor, and rotation for conversion between the two coordinate systems.

    :param s1a: point A in coordinate system 1 (tuple of (x,y))
    :param s1b: point B in coordinate system 1 (tuple of (x,y))
    :param s2a: point A in coordinate system 2 (tuple of (x,y))
    :param s2b: point B in coordinate system 2 (tuple of (x,y))
    :return: translation [float tuple of tX, tY], scaling factor [float tuple of sX, sY], and rotation [float, radians]
    """
    # establish difference calculations, basis
    s2_dx = s2b[0] - s2a[0]
    s2_dy = s2b[1] - s2a[1]
    # calculate rotation
    beta = _py_atan2(s2_dx, s2_dy)  # inverted slope
    alpha = _py_atan2(s1b[0] - s1a[0], s1b[1] - s1a[1])  # inverted slope
    theta = alpha - beta
    # recalculate s1a/s1b after matching up rotation
    s1a_x_ = ((s1a[0] * _py_cos(theta)) - (s1a[1] * _py_sin(theta)))
    s1a_y_ = ((s1a[0] * _py_sin(theta)) + (s1a[1] * _py_cos(theta)))
    s1b_x_ = ((s1b[0] * _py_cos(theta)) - (s1b[1] * _py_sin(theta)))
    s1b_y_ = ((s1b[0] * _py_sin(theta)) + (s1b[1] * _py_cos(theta)))
    # calculate scaling factor (after accounting for rotation)
    sx = s2_dx / (s1b_x_ - s1a_x_) if s2_dx != 0 and not np.isclose(s1b_x_, s1a_x_) else 1.0
    sy = s2_dy / (s1b_y_ - s1a_y_) if s2_dy != 0 and not np.isclose(s1b_y_, s1a_y_) else 1.0
    # calculate translation (accounting for scale and rotation)
    s1a_x_ *= sx
    s1a_y_ *= sy
    translation = (s2a[0] - s1a_x_, s2a[1] - s1a_y_)
    # return tuple of results
    return translation, (sx, sy), theta


def calculate_tsr_2d(cs1, cs2, discard_colinear=1e-03):
    """
    Given two arrays of corresponding coordinates for two different 2D coordinate systems, calculate the
    average transformation (translation, scale, and rotation) that best satisfies all of the given points.

    :param cs1: array of coordinate system 1 (2D, dim 0 = entries, dim 1 = len 2 of x,y) e.g. [[1,2],[2,3],[3,4],...]
    :param cs2: array of coordinate system 2 (2D, dim 0 = entries, dim 1 = len 2 of x,y) e.g. [[1,2],[2,3],[3,4],...]
    :param discard_colinear: tolerance for discarding colinear points. (default = 1e-03). Value of zero means don't discard colinear points.
    :return: average tsr transformation tuple
    """
    cs1 = np.asarray(cs1)
    cs2 = np.asarray(cs2)
    assert cs1.shape == cs2.shape and cs1.shape[0] >= 2 and len(cs1.shape) == 2 and cs1.shape[1] == 2
    shape = cs1.shape

    combinations = list(_combo(range(0, shape[0]), 2))
    tsr = np.zeros((len(combinations), 5), dtype=np.float64)
    calc_tsr = calculate_tsr_2d_2p
    i = 0
    for (p0, p1) in combinations:
        if discard_colinear and caac(cs1[[p0, p1], :], atol=discard_colinear):  # skip colinear points for transformation calculations
            continue
        (tx, ty), (sx, sy), rz = calc_tsr(cs1[p0], cs1[p1], cs2[p0], cs2[p1])  # m1, m2, w1, w2
        tsr[i] = [tx, ty, sx, sy, normalize_angle(rz, center_angle_radians=0)]
        i += 1  # advance i

    if i == 0:
        raise ValueError('calculate_tsr_2d(): all combinations of points were colinear!')
    tsr = tsr[:i]  # clip tsr to populated subset [done w/ variable assignment to facilitate debugging/verification]

    avg_tsr = np.average(tsr, axis=0)  # TODO: this averaging approach is rough and should also output residuals for user examination
    # residuals = tsr - avg_tsr  # TODO: returning residuals?
    return avg_tsr[0:2], avg_tsr[2:4], avg_tsr[4]


def transform_2d_coordinates(transformation, x, y):
    """
    Apply 2D TSR transformation to x, y given transformation

    :param transformation: transformation as: (tx, ty), (sx, sy), theta
    :param x: float or array of x
    :param y: float or array of y
    :return: x', y' (transformed coordinates)
    """
    (tx, ty), (sx, sy), theta = transformation
    x_ = sx * ((x * _py_cos(theta)) - (y * _py_sin(theta))) + tx
    y_ = sy * ((x * _py_sin(theta)) + (y * _py_cos(theta))) + ty
    return x_, y_


class TransformTSR2D(object):
    """
    Object to handle transformations of translation, scale, and rotation. Note that:
    1) implementation does not use matrices and is basically hacked together
    2) is meant to be compatible for many uses as a drop-in replacement for pyproj (basically for 2D affine/Helmert transformations only)
    """
    _xfm = None
    _inv = None  # TODO: it would be reasonable / convenient to compute matrices and handle inverse that way...
    _post = None  # post-forward-transformation adjustments # TODO: this should not exist; it's a lazy BS fix...

    # def __init__(self):
    #     pass

    @staticmethod
    def from_points(cs1, cs2):
        """
        Create 2D TSR transformation from average TSR calculated from the given corresponding coordinate sets

        :param cs1: array of coordinates for system 1 (e.g. [[1,2], [3,4], [5,6], ...])
        :param cs2: array of coordinates for system 2 (e.g. [[1,2], [3,4], [5,6], ...])
        :return: TransformTSR2D
        """
        result = TransformTSR2D()
        result._xfm = calculate_tsr_2d(cs1, cs2)
        result._inv = calculate_tsr_2d(cs2, cs1)
        return result

    @staticmethod
    def from_two_points(cs1a, cs1b, cs2a, cs2b):
        """
        Create 2D TSR transformation from TSR calculated between two corresponding points in two coordinate systems

        :param cs1a: Point A in System 1 (e.g. [1,2])
        :param cs1b: Point B in System 1 (e.g. [3,4])
        :param cs2a: Point A in System 2 (e.g. [10,20])
        :param cs2b: Point B in System 2 (e.g. [30,40])
        :return: TransformTSR2D
        """
        result = TransformTSR2D()
        result._xfm = calculate_tsr_2d_2p(cs1a, cs1b, cs2a, cs2b)
        result._inv = calculate_tsr_2d_2p(cs2a, cs2b, cs1a, cs1b)  # lazy way to compute inverse....
        return result

    @staticmethod
    def from_point_tsr(cs1a, cs2a, sx, sy, theta):
        """
        Create 2D TSR transformation from a known corresponding point between two coordinate systems as well as scale and rotation details

        :param cs1a: Point A in System 1 (e.g. [1,2])
        :param cs2a: Point A in System 2 (e.g. [10,20])
        :param sx: scaling parameter in the x-direction (1 = same scale between systems)
        :param sy: scaling parameter in the y-direction (1 = same scale between systems)
        :param theta: angle/rotation parameter (radians, math conventions)
        :return: TransformTSR2D
        """
        result = TransformTSR2D()
        cs1a = np.asarray(cs1a)
        cs2a = np.asarray(cs2a)
        # do translation by calculating axial distances from known anchor point after scale & rotate
        m0px = sx * ((cs1a[0, 0] * _py_cos(theta)) - (cs1a[0, 1] * _py_sin(theta)))
        m0py = sy * ((cs1a[0, 0] * _py_sin(theta)) + (cs1a[0, 1] * _py_cos(theta)))
        tx, ty = cs2a[0, 0] - m0px, cs2a[0, 1] - m0py
        # save forward transformation
        result._xfm = (tx, ty), (sx, sy), theta
        # determine inverse transformation by applying forward transformation # TODO: verify, latest incarnation is unchecked!
        cs1b = [(35 + tx + 100.0 * sx + cs1a[0, 0]), (35 + ty + 100.0 * sy + cs1a[0, 1])]  # arbitrary 2nd point
        cs2b = result.transform(cs1b[0], cs1b[1])  # apply forward TSR on arbitrary 2nd point
        result._inv = calculate_tsr_2d_2p((cs2a[0, 0], cs2a[0, 1]), cs2b, (cs1a[0, 0], cs1a[0, 1]), cs1b)
        return result

    @property
    def tsr(self):
        """ Returns (translation_x, translation_y), (scale_x, scale_y), angle_theta for forward transformation """
        return self._xfm

    @property
    def inverse_tsr(self):
        """ Returns (translation_x, translation_y), (scale_x, scale_y), angle_theta for inverse transformation """
        return self._inv

    @property
    def definition(self):
        """ String providing transformation details, provided for partial compatibility with pyproj API """
        return 'Transform2D: forward=%s; inverse=%s' % (self._xfm, self._inv)

    def nudge(self, tx=0.0, ty=0.0):
        """
        Modify the translation parameters (targeting the forward transformation) with the given parameters

        :param tx: adjustment/nudge to the x translation
        :param ty: adjustment/nudge to the y translation
        :return returns self to facilitate chaining
        """
        (xtx, xty), x_s, x_t = self._xfm
        (itx, ity), i_s, i_t = self._inv
        self._xfm = (xtx + tx, xty + ty), x_s, x_t
        self._inv = (itx - tx, ity - ty), i_s, i_t
        return self

    # def set_post_transform(self, sx=1.0, sy=1.0, theta=0.0):
    #     """
    #     Configure adjustments to be made to the transform after the initial transformation. Current implementation
    #     actually performs further transformations after forward transformation and reversed before inverse; however,
    #     that should be replaced with adjusting the forward and inverse transformation definitions.
    #
    #     :param sx: scale factor in x-direction, default=1.0
    #     :param sy: scale factor in y-direction, default=1.0
    #     :param theta: rotation/theta, default=0.0 (no rotation)
    #     :return: self
    #     """
    #     self._post = (0.0, 0.0), (sx, sy), theta
    #     return self

    def transform(self, x, y, inverse=False, **kwargs):
        """
        Perform transformation on given x and y coordinates

        :param x: array of x coordinates (or a single x coordinate)
        :param y: array of y coordinates (or a single y coordinate)
        :param inverse: whether to perform the inverse transformation
        :param kwargs: optionally supports a 'direction' kwarg to be compatible with FORWARD/INVERSE enum from pyproj
        :return: tuple of (x', y') [transformed coordinates]
        """
        if not inverse and 'direction' in kwargs:
            direction = kwargs.pop('direction', None)
            inverse = direction == 'INVERSE' or getattr(direction, 'value', None) == 'INVERSE'  # compat w/ pyproj API; IDENT not supported
        x = np.asarray(x)
        y = np.asarray(y)
        x, y = transform_2d_coordinates(self._inv if inverse else self._xfm, x, y)
        # TODO: implement post-transform? (...or leave it disabled)
        return x, y

    def inverse(self, x, y):
        """
        Perform inverse transformation on given x and y coordinates

        :param x: array of x coordinates (or a single x coordinate)
        :param y: array of y coordinates (or a single y coordinate)
        :return: tuple of (x', y') [transformed coordinates]
        """
        return self.transform(x, y, inverse=True)

    pass


@DeprecationWarning
def cw_sort_coordinates(points, reverse=False):
    """
    Function to sort a list of 2D coordinates such that the resulting coordinates are in a clockwise direction.
    This assumes math conventions for X and Y. (For image conventions or for CCW, just reverse the order.)

    TODO: finish this function, it's broken and shouldn't be used until fixed

    :param points: list of 2D points
    :param reverse: reverse sort order
    :return:
    """
    pts = np.asarray(points)
    assert len(pts.shape) == 2 and pts.shape[1] == 2

    if pts.shape[0] == 0:
        return pts

    c = np.average(pts, axis=0)

    def cmp(a, b):
        if a[0] - c[0] >= 0 > b[0] - c[0]:
            return 1
        elif a[0] - c[0] < 0 <= b[0] - c[0]:
            return -1
        elif a[0] - c[0] == 0 and b[0] - c[0] == 0:
            if a[1] - c[0] >= 0 or b[1] - c[1] >= 0:
                return 1 if a[1] > b[1] else -1
            return 1 if b[1] > a[1] else -1

        # cross product check
        det = (a[1] - c[1]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
        if det < 0:
            return 1
        elif det > 0:
            return -1
        else:  # distance check is last fall-back
            return 1 if distance(a, c) > distance(b, c) else -1

    return np.asarray(sorted(pts, key=_cmp2key(cmp), reverse=reverse))
