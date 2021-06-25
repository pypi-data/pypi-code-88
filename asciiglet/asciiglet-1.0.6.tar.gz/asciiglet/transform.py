import math

import numpy as np

from .vector import Vector
from .abstract_object import AbstractObject


def lerp(x1: float, x2: float, y1: float, y2: float, x: float):
    return ((y2 - y1) * x + x2 * y1 - x1 * y2) / (x2 - x1)


class Transform(AbstractObject):
    def __init__(
        self,
        pos=Vector.new(0.0, 0.0),
        angle=0,
        scale=Vector.new(1.0, 1.0),
        parent=None,
    ):
        super().__init__()

        self.gameObject = None

        self._pos = pos
        self._angle = angle
        self._scale = scale

        self.parent = None
        self.children = []

        self.setParent(parent)

    def __destroy__(self):
        self.gameObject = None
        super().__destroy__()

    @property
    def pos(self):
        if self.parent is not None:
            return self.parent.pos + self._pos
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def angle(self):
        if self.parent is not None:
            return self.parent.angle + self._angle
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = math.fmod(value, 360.0)

    @property
    def scale(self):
        if self.parent is not None:
            return self.parent.scale * self._scale
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value

    def setParent(self, parent):
        if self.parent is not None:
            self.parent.children.remove(self)

        self.parent = parent
        if parent is not None:
            self.parent.children.append(self)

    def forward(self):
        return Vector.rotate(Vector.new(1.0, 0.0), self.angle)

    def face(self, transform):
        forward = self.forward()
        target = transform.pos - self.pos

        face_angle = Vector.angleRotateTo(forward, target)
        self.angle += face_angle

    def copy(self):
        return Transform(
            np.copy(self.pos),
            np.copy(self.angle),
            np.copy(self.scale)
        )

    def from_perspective(self, transform, origin=Vector.new(0.0, 0.0)):
        """
        Output how self would look like, if transform was it's perspective.
        """
        pos = Vector.rotate(
            self.pos * transform.scale, transform.angle, origin=origin
        ) + transform.pos
        scale = self.scale * transform.scale
        angle = self.angle + transform.angle

        return Transform(pos=pos, scale=scale, angle=angle)
