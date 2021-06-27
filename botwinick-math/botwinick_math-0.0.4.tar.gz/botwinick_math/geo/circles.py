# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

from math import pi


def r2a(radius):
    """
    Circle: radius to area
    :param radius: radius
    :return: area
    """
    return pi * radius ** 2.0


def a2r(area):
    """
    Circle: area to radius
    :param area: area
    :return: radius
    """
    return (area / pi) ** 0.5


def d2a(diameter):
    """
    Circle: diameter to area
    :param diameter: diameter
    :return: area
    """
    return 0.25 * pi * diameter ** 2.0


def a2d(area):
    """
    Circle: area to diameter
    :param area: area
    :return: diameter
    """
    return 2.0 * (area / pi) ** 0.5
