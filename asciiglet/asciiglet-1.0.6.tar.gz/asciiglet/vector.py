import numpy as np

from math import cos, sin, sqrt


class Vector:
    @classmethod
    def new(cls, x, y):
        return np.array([x, y])

    @classmethod
    def rotate(cls, v, angle, origin=None):
        if origin is None:
            origin = cls.new(0.0, 0.0)

        t = np.deg2rad(angle)

        rot = np.array([[cos(t), sin(t)], [-sin(t), cos(t)]])

        return np.dot(v - origin, rot) + origin

    @classmethod
    def angleBetween(cls, v1, v2):
        unit_v1 = v1 / np.linalg.norm(v1)
        unit_v2 = v2 / np.linalg.norm(v2)

        return np.rad2deg(np.arccos(np.dot(unit_v1, unit_v2)))

    @classmethod
    def angleRotateTo(cls, v1, v2, normal=np.array([1.0])):
        angle = np.rad2deg(np.arctan2(v1[0], v1[1]) - np.arctan2(v2[0], v2[1]))
        # In case arctan ever outputs angles greater than 360.
        # return ((angle - 180) % 360) - 180

        if angle > 180:
            angle = 180 - angle
        elif angle < -180:
            angle = -180 - angle

        return angle

        # More than 2 dimensional variant. Kinda.

        """
        unit_v1 = v1 / np.linalg.norm(v1)
        unit_v2 = v2 / np.linalg.norm(v2)

        angle = np.arccos(np.dot(unit_v1, unit_v2))

        c = np.cross(unit_v1, unit_v2)

        if np.dot(normal, c) < 0:
            angle = -angle

        return np.rad2deg(angle)
        """

    @classmethod
    def scale_to_length(cls, v, length):
        unit_v = v / np.linalg.norm(v)
        return unit_v * length

    @classmethod
    def magnitudeSquared(cls, v):
        return v[0] ** 2 + v[1] ** 2

    @classmethod
    def magnitude(cls, v):
        return sqrt(v[0] ** 2 + v[1] ** 2)

    @classmethod
    def as_polar(cls, v):
        return cls.magnitude(v), cls.angleRotateTo(Vector.new(1.0, 0.0), v)
