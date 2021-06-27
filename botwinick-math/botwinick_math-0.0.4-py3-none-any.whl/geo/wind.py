# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

from math import (atan2 as _py_atan2, floor as _py_floor)

from .cartesian import PI, TWO_PI, normalize_angle

WIND_ROSE_CONVENTION_OFFSET = PI * 1.5


def convert_angle_math_wind(angle_radians):
    """
    Function to convert a single angle between math (CCW, 0 at "East") and wind conventions (CW, 0 at "North")

    :param angle_radians: the input angle in radians
    :type angle_radians: float
    :return:  the angle (still in radians) shifted to account for the different origin between the two conventions
    :rtype: float
    """
    return normalize_angle(WIND_ROSE_CONVENTION_OFFSET - angle_radians)


def wind_angle_between(x1, y1, x2, y2):
    """
    Wind Convention Angle/Heading calculated for winds oriented from (x1,y1) to (x2,y2)

    :param x1: x-coordinate for source point
    :param y1: y-coordinate for source point
    :param x2: x-coordinate for destination point
    :param y2: y-coordinate for destination point
    :return: wind angle in radians
    """
    theta = _py_atan2(y1 - y2, x1 - x2)
    return normalize_angle(2.5 * PI - theta)


def angle_to_list_index(angle, list_length, angle_offset=0.0, clockwise=False):
    """
    Function to convert an angle to the corresponding index in a 1D list/array of wind data. This is typically used
    as part of quantitative studies when the likelihood associated with wind directions is stored in a 1D array for a particular
    condition.

    :param angle: the angle (radians) to lookup
    :param list_length: the list length / number of angles in the array representing 2PI / 360 deg
    :param angle_offset: positive angle offset (radians) that will be added to the angle when processed
    :param clockwise: boolean to indicate the direction associated with increasing angle values. For math conventions,
    False (counterclockwise is the default). For wind conventions, clockwise would be True.
    :return: int representing the index for the given angle and parameters in the 1D list
    """
    sector_size = TWO_PI / list_length
    angle = normalize_angle((-1.0 if clockwise else 1.0) * angle + angle_offset, center_angle_radians=PI)
    return int(_py_floor(angle / sector_size)) if angle != 0 else 0


def list_index_to_angle(index, list_length, interval=True, angle_offset=0.0, clockwise=False):
    """
    Function to convert a list index to the center angle (or an angle interval) for the given index for a 1D list/array of wind data.
    This is typically used as part of quantitative studies when the likelihood associated with wind directions is stored in a 1D array
    for a particular condition.

    :param index: the index (int) to lookup
    :param list_length: the list length / number of angles in the array representing 2PI / 360 deg
    :param interval: boolean to indicate if the result should be a tuple of the angles bounding the selected sector (True) or the
    midpoint angle associated with the sector (False)
    :param angle_offset: positive angle offset (radians) that will be added to the angle when processed
    :param clockwise: boolean to indicate the direction associated with increasing angle values. For math conventions,
    False (counterclockwise is the default). For wind conventions, clockwise would be True.
    :return: float of midpoint angle in radians or tuple of 2 floats representing bounding angles in radians
    """
    if index < 0 or index >= list_length:
        raise ValueError('index out of bounds')
    sector_size = TWO_PI / list_length
    cw = -1.0 if clockwise else 1.0
    angle = cw * (sector_size * index) + angle_offset
    if interval:
        # TODO: check that interval sector ordering is consistent w/ clockwise/counterclockwise (i.e. add in `cw` factor as needed)
        return normalize_angle(angle + 0.5 * sector_size), normalize_angle(angle - 0.5 * sector_size)
    else:
        return normalize_angle(angle)
