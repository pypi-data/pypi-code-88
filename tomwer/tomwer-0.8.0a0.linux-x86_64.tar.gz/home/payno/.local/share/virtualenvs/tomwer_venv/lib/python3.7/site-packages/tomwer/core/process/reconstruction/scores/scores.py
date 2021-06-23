# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "18/02/2021"


from silx.utils.enum import Enum as _Enum
import numpy
import sys
import logging

_logger = logging.getLogger(__name__)


class ScoreMethod(_Enum):
    STD = "standard deviation"
    TV = "total variation"


class ComputedScore:
    def __init__(self, tv, std):
        self._tv = tv
        self._std = std

    @property
    def total_variation(self):
        return self._tv

    @property
    def std(self):
        return self._std

    def get(self, method: ScoreMethod):
        method = ScoreMethod.from_value(method)
        if method is ScoreMethod.TV:
            return self.total_variation
        elif method is ScoreMethod.STD:
            return self.std
        else:
            raise ValueError("{} is an unrecognized method".format(method))


def compute_score_contrast_std(data: numpy.ndarray):
    """
    Compute a contrast score by simply computing the standard deviation of
    the frame
    :param numpy.ndarray data: frame for which we should compute the score
    :return: score of the frame
    :rtype: float
    """
    if data is None:
        return None
    else:
        return data.std() * 100


def compute_tv_score(data: numpy.ndarray):
    """
    Compute the data score as image total variation

    :param numpy.ndarray data: frame for which we should compute the score
    :return: score of the frame
    :rtype: float
    """
    tv = numpy.sum(
        numpy.sqrt(
            numpy.gradient(data, axis=0) ** 2 + numpy.gradient(data, axis=1) ** 2
        )
    )
    # adapt score to:
    #    - get growing score: the higher the score is the better the cor is.
    #      this is the 1 / tv part
    #    - look more "friendly" (10e5 part)
    return (1.0 / tv) * float(10e5)


_METHOD_TO_FCT = {
    ScoreMethod.STD: compute_score_contrast_std,
    ScoreMethod.TV: compute_tv_score,
}


def compute_score(data: numpy.ndarray, method: ScoreMethod) -> float:
    """

    :param numpy.ndarray data: frame for which we should compute the score
    :param str method:
    :return: score of the frame
    :rtype: float
    """
    method = ScoreMethod.from_value(method)
    fct = _METHOD_TO_FCT.get(method, None)
    if data.ndim == 3:
        if data.shape[0] == 1:
            data = data.reshape(data.shape[1], data.shape[2])
        elif data.shape[2] == 1:
            data = data.reshape(data.shape[0], data.shape[1])
        else:
            raise ValueError("Data is expected to be 2D. Not {}".format(data.ndim))
    elif data.ndim == 2:
        pass
    else:
        raise ValueError("Data is expected to be 2D. Not {}".format(data.ndim))

    if fct is not None:
        return fct(data)
    else:
        raise ValueError("{} is not handled".format(method))


def get_disk_mask_radius(datasets_) -> int:
    """compute the radius to use for the mask"""
    radius = sys.maxsize
    # get min radius
    for cor, (url, data) in datasets_.items():
        assert data.ndim is 2, "data is expected to be 2D"
        min_ = numpy.array(data.shape).min()
        if radius >= min_:
            radius = min_
    return radius // 2


def apply_roi(data, radius, url) -> numpy.array:
    """compute the square included in the circle of radius and centered
    in the middle of the data"""
    half_width = int(radius / 2 ** 0.5)
    center = numpy.array(data.shape[:]) // 2
    min_x, max_x = center[0] - half_width, center[0] + half_width
    min_y, max_y = center[1] - half_width, center[1] + half_width
    try:
        return data[min_y:max_y, min_x:max_x]
    except Exception:
        _logger.error(
            "Fail to apply roi for {}. Take the entire dataset".format(url.path())
        )
        return data
