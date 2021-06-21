from enum import Enum
from abc import ABC, abstractmethod
from coopstructs.vectors import Vector2
import math
import pygame
from coopgame.colors import Color
from typing import List
from coopstructs.geometry import Rectangle
import numpy as np

class CurveType(Enum):
    HORIZONTAL = 1 #stop using
    VERTICAL = 2 #stop using
    UP_LEFT = 3
    UP_RIGHT = 4
    RIGHT_UP = 5
    RIGHT_DOWN = 6
    DOWN_RIGHT = 7
    DOWN_LEFT = 8
    LEFT_DOWN = 9
    LEFT_UP = 10
    UP = 11
    RIGHT = 12
    DOWN = 13
    LEFT = 14


class Curve(ABC):
    def __init__(self, curve_type: CurveType, origin: Vector2):
        self.curve_type = curve_type
        self.origin = origin

    def __str__(self):
        return f"{self.curve_type.name} starting at {self.origin}"

    @abstractmethod
    def end_point(self):
        pass

    @abstractmethod
    def draw(self, screen, color):
        pass

    @abstractmethod
    def line_representation(self) -> List:
        pass

class Arc(Curve):
    def __init__(self, curve_type: CurveType, origin: Vector2, arc_box_size: Vector2):
        super().__init__(curve_type, origin)
        self.arc_box_size = arc_box_size
        self.arc_rad_start = None
        self.arc_rad_end = None
        self.define_arc_radian_start_end()
        self._arc_box = self.arc_box()
        self.mid_point = Vector2(self._arc_box[0] + self._arc_box[2] / 2.0, self._arc_box[1] + self._arc_box[3] / 2.0)

    def line_representation(self):
        return self.compute_curve_lines()

    def define_arc_radian_start_end(self):
        if self.curve_type == CurveType.DOWN_LEFT:
            self.arc_rad_start = 2 * math.pi
            self.arc_rad_end = 3 * math.pi / 2
        elif self.curve_type == CurveType.DOWN_RIGHT:
            self.arc_rad_start = math.pi
            self.arc_rad_end = 3 * math.pi / 2
        elif self.curve_type == CurveType.LEFT_DOWN:
            self.arc_rad_start = math.pi / 2
            self.arc_rad_end = math.pi
        elif self.curve_type == CurveType.LEFT_UP:
            self.arc_rad_start = 3 * math.pi / 2
            self.arc_rad_end = math.pi
        elif self.curve_type == CurveType.UP_LEFT:
            self.arc_rad_start = 0
            self.arc_rad_end = math.pi / 2
        elif self.curve_type == CurveType.UP_RIGHT:
            self.arc_rad_start = math.pi
            self.arc_rad_end = math.pi / 2
        elif self.curve_type == CurveType.RIGHT_DOWN:
            self.arc_rad_start = math.pi / 2
            self.arc_rad_end = 0
        elif self.curve_type == CurveType.RIGHT_UP:
            self.arc_rad_start = 3 * math.pi / 2
            self.arc_rad_end = 2 * math.pi
        else:
            raise Exception(f"Invalid Curvetype: {self.curve_type} to draw")

    def end_point(self):
        if self.curve_type in (CurveType.DOWN_LEFT,  CurveType.LEFT_DOWN):
            return Vector2(int(self.origin.x - self.arc_box_size.x / 2), int(self.origin.y + self.arc_box_size.y / 2))
        elif self.curve_type in (CurveType.LEFT_UP, CurveType.UP_LEFT):
            return Vector2(int(self.origin.x - self.arc_box_size.x / 2), int(self.origin.y - self.arc_box_size.y / 2))
        elif self.curve_type in (CurveType.UP_RIGHT, CurveType.RIGHT_UP):
            return Vector2(int(self.origin.x + self.arc_box_size.x / 2), int(self.origin.y - self.arc_box_size.y / 2))
        elif self.curve_type in (CurveType.RIGHT_DOWN, CurveType.DOWN_RIGHT):
            return Vector2(int(self.origin.x + self.arc_box_size.x / 2), int(self.origin.y + self.arc_box_size.y / 2))
        else:
            raise Exception("Incorrect Curve type with orientation")

    def compute_curve_lines(self):
        b_points = self.compute_curve_points()
        if b_points is None:
            return None

        ret = []
        for ii in range(0, len(b_points)):
            if ii == 0:
                continue
            else:
                start = Vector2(b_points[ii - 1].x, b_points[ii - 1].y)
                end = Vector2(b_points[ii].x, b_points[ii].y)
                ret.append(Line(start, end))
        return ret

    def compute_curve_points(self, numPoints=None) -> List[Vector2]:
        if numPoints is None:
            numPoints = 30
        if numPoints < 2:
            return None

        ret = []
        increment = (self.arc_rad_end - self.arc_rad_start) / (numPoints - 1)
        for ii in range(0, numPoints):
            next = self.point_along_arc(self.arc_rad_start + increment * ii, self.mid_point, self.arc_box_as_rectangle())
            ret.append(next)

        return ret

    def arc_box_as_rectangle(self) -> Rectangle:
        return Rectangle(x=self._arc_box[0], y=self._arc_box[1], width=self._arc_box[2], height=self._arc_box[3])

    def point_along_arc(self, radians: float, rotation_point: Vector2, arc_box: Rectangle):
        a = arc_box.width / 2
        b = arc_box.height / 2

        x = a * math.cos(radians)
        y = - b * math.sin(radians)

        return Vector2(int(x), int(y)) + rotation_point

    def arc_box(self):
        if self.curve_type == CurveType.DOWN_LEFT:
            return [self.origin.x - self.arc_box_size.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.DOWN_RIGHT:
            return [self.origin.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.LEFT_DOWN:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.LEFT_UP:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y - self.arc_box_size.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.UP_LEFT:
            return [self.origin.x - self.arc_box_size.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.UP_RIGHT:
            return [self.origin.x, self.origin.y - self.arc_box_size.y / 2,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.RIGHT_UP:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y - self.arc_box_size.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        elif self.curve_type == CurveType.RIGHT_DOWN:
            return [self.origin.x - self.arc_box_size.x / 2, self.origin.y,
                    self.arc_box_size.x, self.arc_box_size.y]
        else:
            raise Exception("Incorrect Curve type with orientation")

    def draw(self, surface: pygame.Surface, color:Color = None, draw_scale_matrix = None):
        if color is None:
            color = Color.WHITE

        start = min(self.arc_rad_start, self.arc_rad_end)
        end = max(self.arc_rad_start, self.arc_rad_end)
        pygame.draw.arc(surface, color.value, self._arc_box, start, end, 2)

    def length(self):
        return (self.arc_rad_end - self.arc_rad_start) * (self.origin - self.mid_point).length()



class Line(Curve):
    def __init__(self, origin: Vector2, destination: Vector2):
        orientation = None
        if origin.x == destination.x and origin.y > destination.y:
            orientation = CurveType.UP
        elif origin.x == destination.x and origin.y < destination.y:
            orientation = CurveType.DOWN
        elif origin.x < destination.x and origin.y == destination.y:
            orientation = CurveType.RIGHT
        elif origin.x > destination.x and origin.y == destination.y:
            orientation = CurveType.LEFT
        elif origin.x > destination.x and origin.y > destination.y:
            orientation = CurveType.UP_LEFT
        elif origin.x > destination.x and origin.y < destination.y:
            orientation = CurveType.DOWN_LEFT
        elif origin.x < destination.x and origin.y > destination.y:
            orientation = CurveType.UP_RIGHT
        elif origin.x < destination.x and origin.y < destination.y:
            orientation = CurveType.DOWN_RIGHT

        super().__init__(orientation, origin)

        self.destination = destination
        self.length = self.length()

    def line_representation(self):
        return [self]

    def end_point(self):
        return self.destination

    def length(self):
        try:
            return math.sqrt((self.destination.x - self.origin.x) ** 2 + (self.destination.y - self.origin.y) ** 2)
        except Exception as e:
            print(f"Destination: {self.destination}\n"
                  f"Origin: {self.origin}\n"
                  f"{e}")
            raise

    def draw(self, surface: pygame.Surface, color: Color = None, draw_scale_matrix = None):
        if draw_scale_matrix is None:
            draw_scale_matrix = np.identity(4)


        if color is None:
            color = Color.WHITE

        origin = np.array([self.origin.x, self.origin.y, 0, 1])
        destination = np.array([self.destination.x, self.destination.y, 0, 1])

        translated_points = draw_scale_matrix.dot(np.transpose(np.array([origin, destination]))).transpose()

        pygame.draw.line(surface, color.value, (translated_points[0][0], translated_points[0][1]), (translated_points[1][0], translated_points[1][1]))

class Bezier(Curve):
    def __init__(self, control_points: List[Vector2]):
        Curve.__init__(self, CurveType.BEZIER, control_points[0])
        self.control_points = control_points

    def line_representation(self):
        return self.compute_curve_lines()

    def end_point(self):
        return self.control_points[-1]

    def draw(self, screen, color, draw_points: bool = False, draw_lines: bool = False):
        ### Draw control points
        if draw_points:
            for p in self.control_points:
                pygame.draw.circle(screen, Color.YELLOW.value, (int(p.x), int(p.y)), 4)

        ### Draw control "lines"
        pygame.draw.lines(screen, color.GREY.value, False, [(x.x, x.y) for x in self.control_points])

        ### Draw bezier curve
        b_points = self.compute_bezier_points([(x.x, x.y) for x in self.control_points])
        pygame.draw.lines(screen, color.value, False, b_points, 2)

    def compute_curve_lines(self):
        b_points = self.compute_bezier_points([(x.x, x.y) for x in self.control_points])
        ret = []
        for ii in range(0, len(b_points)):
            if ii == 0:
                continue
            else:
                start = Vector2(b_points[ii - 1][0], b_points[ii - 1][1])
                end = Vector2(b_points[ii][0], b_points[ii][1])
                ret.append(Line(start, end))
        return ret

    def compute_bezier_points(self, vertices, numPoints=None):
        if numPoints is None:
            numPoints = 30
        if numPoints < 2 or len(vertices) != 4:
            return None

        result = []

        b0x = vertices[0][0]
        b0y = vertices[0][1]
        b1x = vertices[1][0]
        b1y = vertices[1][1]
        b2x = vertices[2][0]
        b2y = vertices[2][1]
        b3x = vertices[3][0]
        b3y = vertices[3][1]

        # Compute polynomial coefficients from Bezier points
        ax = -b0x + 3 * b1x + -3 * b2x + b3x
        ay = -b0y + 3 * b1y + -3 * b2y + b3y

        bx = 3 * b0x + -6 * b1x + 3 * b2x
        by = 3 * b0y + -6 * b1y + 3 * b2y

        cx = -3 * b0x + 3 * b1x
        cy = -3 * b0y + 3 * b1y

        dx = b0x
        dy = b0y

        # Set up the number of steps and step size
        numSteps = numPoints - 1  # arbitrary choice
        h = 1.0 / numSteps  # compute our step size

        # Compute forward differences from Bezier points and "h"
        pointX = dx
        pointY = dy

        firstFDX = ax * (h * h * h) + bx * (h * h) + cx * h
        firstFDY = ay * (h * h * h) + by * (h * h) + cy * h

        secondFDX = 6 * ax * (h * h * h) + 2 * bx * (h * h)
        secondFDY = 6 * ay * (h * h * h) + 2 * by * (h * h)

        thirdFDX = 6 * ax * (h * h * h)
        thirdFDY = 6 * ay * (h * h * h)

        # Compute points at each step
        result.append((int(pointX), int(pointY)))

        for i in range(numSteps):
            pointX += firstFDX
            pointY += firstFDY

            firstFDX += secondFDX
            firstFDY += secondFDY

            secondFDX += thirdFDX
            secondFDY += thirdFDY

            result.append((int(pointX), int(pointY)))

        return result