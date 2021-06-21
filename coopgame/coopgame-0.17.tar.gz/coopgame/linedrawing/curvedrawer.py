import pygame
from coopgame.colors import Color
from typing import List, Dict, Callable
from coopstructs.curves import Arc, CubicBezier, LineCurve, Curve, Orientation, CatmullRom, CircularArc
from coopstructs.geometry import Line
import numpy as np


class CurveDrawer:

    def __init__(self):
        pass

    def draw_curves(self,
                    curves: Dict[Curve, Color],
                    surface: pygame.Surface,
                    draw_control_points: bool = True,
                    draw_control_lines: bool = True,
                    control_point_color: Color = Color.RED,
                    control_point_size: int = None,
                    control_line_color: Color = Color.GREY,
                    draw_scale_matrix=None):
        for curve, color in curves.items():
            if type(curve) == CubicBezier:
                self.draw_bezier(surface,
                                 curve,
                                 color,
                                 draw_points=draw_control_points,
                                 control_point_color=control_point_color,
                                 control_point_size=control_point_size,
                                 draw_control_lines=draw_control_lines,
                                 control_line_color=control_line_color,
                                 draw_scale_matrix=draw_scale_matrix)
            elif type(curve) == LineCurve:
                self.draw_line(surface,
                               curve,
                               color,
                               draw_points=draw_control_points,
                               control_point_color=control_point_color,
                               control_point_size=control_point_size,
                               draw_scale_matrix=draw_scale_matrix)
            elif type(curve) == Arc:
                self.draw_arc(surface,
                              curve,
                              color,
                              draw_points=draw_control_points,
                              control_point_color=control_point_color,
                              control_point_size=control_point_size,
                              draw_scale_matrix=draw_scale_matrix)
            elif type(curve) == CatmullRom:
                self.draw_catmullrom(surface,
                                     curve,
                                     color,
                                     draw_points=draw_control_points,
                                     control_point_color=control_point_color,
                                     control_point_size=control_point_size,
                                     draw_scale_matrix=draw_scale_matrix)
            elif type(curve) == CircularArc:
                self.draw_circulararc(surface,
                                      curve,
                                      color,
                                      draw_points=draw_control_points,
                                      control_point_color=control_point_color,
                                      control_point_size=control_point_size,
                                      draw_scale_matrix=draw_scale_matrix)
            else:
                raise NotImplementedError(f"Unahanlded curve type {curve}")

    def draw_bezier(self,
                    screen,
                    curve: CubicBezier,
                    curve_color: Color,
                    draw_points: bool = False,
                    control_point_color: Color = Color.RED,
                    control_point_size: int = None,
                    draw_control_lines: bool = False,
                    control_line_color: Color = Color.GREY,
                    draw_scale_matrix=None):

        if draw_scale_matrix is None:
            draw_scale_matrix = np.identity(4)

        # Convert control points into np.arrays
        arrays_of_points = []
        for point in curve.control_points:
            arrays_of_points.append(np.array([point.x, point.y, 0, 1]))

        # Translate the points via the scaling matrix
        translated_points = draw_scale_matrix.dot(np.transpose(np.array(arrays_of_points))).transpose()

        # Draw control points
        if control_point_size is None:
            control_point_size = 4

        if draw_points:
            for ii in range(len(translated_points)):
                pygame.draw.circle(screen, control_point_color.value,
                                   (int(translated_points[ii][0]), int(translated_points[ii][1])), control_point_size)
            # for p in curve.control_points:
            #     pygame.draw.circle(screen, control_point_color.value, (int(p.x), int(p.y)), 4)

        # Draw control "lines"
        if draw_control_lines:
            pygame.draw.lines(screen,
                              control_line_color.value,
                              False,
                              [(translated_points[ii][0], translated_points[ii][1])
                               for ii in range(len(translated_points))])
            # pygame.draw.lines(screen, control_line_color.value, False, [(x.x, x.y) for x in curve.control_points])

        # Draw bezier curve
        b_points = curve.compute_bezier_points([(translated_points[ii][0], translated_points[ii][1])
                                                for ii in range(len(translated_points))])
        # b_points = curve.compute_bezier_points([(x.x, x.y) for x in curve.control_points])
        if b_points is not None and len(b_points) > 1:
            pygame.draw.lines(screen, curve_color.value, False, b_points, 2)

    def draw_line(self,
                  surface: pygame.Surface,
                  line: Line,
                  color: Color,
                  draw_points: bool = False,
                  control_point_color: Color = Color.RED,
                  control_point_size: int = None,
                  draw_scale_matrix=None):
        if draw_scale_matrix is None:
            draw_scale_matrix = np.identity(4)

        # Convert Origin/Destination into np.arrays
        origin = np.array([line.origin.x, line.origin.y, 0, 1])
        destination = np.array([line.destination.x, line.destination.y, 0, 1])

        # Translate the points via the scaling matrix
        translated_points = draw_scale_matrix.dot(np.transpose(np.array([origin, destination]))).transpose()

        # Draw the lines
        pygame.draw.line(surface, color.value, (translated_points[0][0], translated_points[0][1]),
                         (translated_points[1][0], translated_points[1][1]))

        # Draw the points
        if control_point_size is None:
            control_point_size = 4

        if draw_points:
            pygame.draw.circle(surface, control_point_color.value,
                               (int(translated_points[0][0]), int(translated_points[0][1])), control_point_size)
            pygame.draw.circle(surface, control_point_color.value,
                               (int(translated_points[1][0]), int(translated_points[1][1])), control_point_size)

    def draw_arc(self,
                 surface: pygame.Surface,
                 arc: Arc,
                 color: Color,
                 draw_points: bool = False,
                 control_point_color: Color = Color.RED,
                 control_point_size: int = None,
                 draw_scale_matrix=None):

        if draw_scale_matrix is None:
            draw_scale_matrix = np.identity(4)

        # Convert control points into np.arrays
        control_points = arc.compute_curve_points()
        arrays_of_points = []
        for point in control_points:
            arrays_of_points.append(np.array([point.x, point.y, 0, 1]))

        # Translate the points via the scaling matrix
        translated_points = draw_scale_matrix.dot(np.transpose(np.array(arrays_of_points))).transpose()

        # Draw Lines
        pygame.draw.lines(surface, color.value, False, [(translated_points[ii][0], translated_points[ii][1])
                                                        for ii in range(len(translated_points))], 2)

        # Draw the points
        if control_point_size is None:
            control_point_size = 4

        if draw_points:
            pygame.draw.circle(surface, control_point_color.value,
                               (int(translated_points[0][0]), int(translated_points[0][1])), control_point_size)
            pygame.draw.circle(surface, control_point_color.value,
                               (int(translated_points[-1][0]), int(translated_points[-1][1])), control_point_size)

    def draw_catmullrom(self,
                        screen,
                        curve: CatmullRom,
                        curve_color: Color,
                        draw_points: bool = False,
                        control_point_color: Color = Color.RED,
                        control_point_size: int = None,
                        draw_control_lines: bool = False,
                        control_line_color: Color = Color.GREY,
                        draw_scale_matrix=None):

        if draw_scale_matrix is None:
            draw_scale_matrix = np.identity(4)

        # Convert control points into np.arrays
        arrays_of_points = []
        for point in curve.control_points:
            arrays_of_points.append(np.array([point.x, point.y, 0, 1]))

        # Translate the points via the scaling matrix
        translated_points = draw_scale_matrix.dot(np.transpose(np.array(arrays_of_points))).transpose()

        # Draw control points
        if control_point_size is None:
            control_point_size = 4

        if draw_points:
            for ii in range(len(translated_points)):
                pygame.draw.circle(screen, control_point_color.value,
                                   (int(translated_points[ii][0]), int(translated_points[ii][1])), control_point_size)

        # Draw control "lines"
        if draw_control_lines:
            pygame.draw.lines(screen,
                              control_line_color.value,
                              False,
                              [(translated_points[ii][0], translated_points[ii][1])
                               for ii in range(len(translated_points))])

        # Draw CatmullRom curve
        b_points = curve.compute_catmull_points([(translated_points[ii][0], translated_points[ii][1])
                                                 for ii in range(len(translated_points))])
        # b_points = curve.compute_catmull_points(curve.control_points)

        if b_points is not None and len(b_points) > 1:
            pygame.draw.lines(screen, curve_color.value, False, [(point.x, point.y) for point in b_points], 2)

    def draw_circulararc(self,
                         screen,
                         curve: CircularArc,
                         curve_color: Color,
                         draw_points: bool = False,
                         control_point_color: Color = Color.RED,
                         control_point_size: int = None,
                         draw_control_lines: bool = False,
                         control_line_color: Color = Color.GREY,
                         draw_scale_matrix=None):
        if draw_scale_matrix is None:
            draw_scale_matrix = np.identity(4)

        # Convert control points into np.arrays
        arrays_of_points = []
        for point in curve.control_points:
            arrays_of_points.append(np.array([point.x, point.y, 0, 1]))

        # Translate the points via the scaling matrix
        translated_points = draw_scale_matrix.dot(np.transpose(np.array(arrays_of_points))).transpose()

        # Draw control points
        if control_point_size is None:
            control_point_size = 4

        if draw_points:
            for ii in range(len(translated_points)):
                pygame.draw.circle(screen, control_point_color.value,
                                   (int(translated_points[ii][0]), int(translated_points[ii][1])), control_point_size)

        # Draw control "lines"
        if draw_control_lines:
            pygame.draw.lines(screen,
                              control_line_color.value,
                              False,
                              [(translated_points[ii][0], translated_points[ii][1])
                               for ii in range(len(translated_points))])

        # Draw circulararc_points
        b_points = curve.compute_circulararc_points()

        # Convert
        arrays_of_points = []
        for point in b_points:
            arrays_of_points.append(np.array([point.x, point.y, 0, 1]))

        # Translate the points via the scaling matrix
        translated_points = draw_scale_matrix.dot(np.transpose(np.array(arrays_of_points))).transpose()

        if translated_points is not None and len(translated_points) > 1:
            pygame.draw.lines(screen, curve_color.value, False, [(point[0], point[1]) for point in translated_points],
                              2)

    def draw_curve_builder(self):
        pass