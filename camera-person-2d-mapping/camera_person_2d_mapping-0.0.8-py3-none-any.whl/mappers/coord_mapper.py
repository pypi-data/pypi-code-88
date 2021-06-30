from ..enums import AxisType
from ..mathematics import linear_equation_function, intersection
from ..models import ReferencePointConfiguration, Coord2D, Resolution, ImageSection, ImageSections, Line
from ..util import split_coords, get_line_coords

from typing import Callable
import cv2
import math
import numpy as np


def coord_mapper(
        video_configuration: ReferencePointConfiguration,
        plan_configuration: ReferencePointConfiguration = None,
) -> Callable[[Coord2D], Coord2D]:
    """
    Given a :class:`VideoConfiguration` object, a function that takes a :class:`Coord2D` and map's it to another
    :class:`Coord2D` with the x attribute representing the distance from the point zero of the
    :class:`VideoConfiguration` in the X axis, and y representing the distance in the Y axis. If not all the needed
    reference points necessary for the mapping of any given :class:`Coord2D`, then the result with be a :class:`Coord2D`
    of x and y equal to infinite.

    This function can also take a configuration for a plan image. When such argument is passed, the mapping function
    will return a :class:`Coord2D` of the representing pixel in the image of the given configuration data.

    :param video_configuration: object containing the necessary data to build the :class:`Coord2D` mapping function.
    :param plan_configuration: object containing the necessary data for the mapping function to return a
           :class:`Coord2D` mapping to another image.
    :return: a function that takes a :class:`Coord2D` and returns the mapped :class:`Coord2D` given the
             :class:`VideoConfiguration`.
    """
    video_sections = _to_image_sections(video_configuration)

    video_s0_mapper = _transformed_section_mapper_function(
        video_configuration.p0,
        video_configuration.p1,
        video_configuration.p1d,
        video_configuration.p2,
        video_configuration.p2d,
        _perspective_transform(video_sections.s0),
        video_configuration.resolution,
    )
    video_s1_mapper = _transformed_section_mapper_function(
        video_configuration.p0,
        video_configuration.p3,
        video_configuration.p3d,
        video_configuration.p2,
        video_configuration.p2d,
        _perspective_transform(video_sections.s1),
        video_configuration.resolution,
    )
    video_s2_mapper = _transformed_section_mapper_function(
        video_configuration.p0,
        video_configuration.p1,
        video_configuration.p1d,
        video_configuration.p4,
        video_configuration.p4d,
        _perspective_transform(video_sections.s2),
        video_configuration.resolution,
    )
    video_s3_mapper = _transformed_section_mapper_function(
        video_configuration.p0,
        video_configuration.p3,
        video_configuration.p3d,
        video_configuration.p4,
        video_configuration.p4d,
        _perspective_transform(video_sections.s3),
        video_configuration.resolution,
    )

    is_coord_in_s0_section = _image_section_coord_validator_function(video_sections.s0)
    is_coord_in_s1_section = _image_section_coord_validator_function(video_sections.s1)
    is_coord_in_s2_section = _image_section_coord_validator_function(video_sections.s2)
    is_coord_in_s3_section = _image_section_coord_validator_function(video_sections.s3)

    if plan_configuration is not None:
        plan_sections = _to_image_sections(plan_configuration)
        plan_s0_mapper = _transformed_section_mapper_function(
            plan_configuration.p0,
            plan_configuration.p1,
            plan_configuration.p1d,
            plan_configuration.p2,
            plan_configuration.p2d,
            _perspective_transform(plan_sections.s0),
            plan_configuration.resolution,
            distance_to_pixel=True,
        )
        plan_s1_mapper = _transformed_section_mapper_function(
            plan_configuration.p0,
            plan_configuration.p3,
            plan_configuration.p3d,
            plan_configuration.p2,
            plan_configuration.p2d,
            _perspective_transform(plan_sections.s1),
            plan_configuration.resolution,
            distance_to_pixel=True,
        )
        plan_s2_mapper = _transformed_section_mapper_function(
            plan_configuration.p0,
            plan_configuration.p1,
            plan_configuration.p1d,
            plan_configuration.p4,
            plan_configuration.p4d,
            _perspective_transform(plan_sections.s2),
            plan_configuration.resolution,
            distance_to_pixel=True,
        )
        plan_s3_mapper = _transformed_section_mapper_function(
            plan_configuration.p0,
            plan_configuration.p3,
            plan_configuration.p3d,
            plan_configuration.p4,
            plan_configuration.p4d,
            _perspective_transform(plan_sections.s3),
            plan_configuration.resolution,
            distance_to_pixel=True,
        )

        def _map(coord: Coord2D):
            if is_coord_in_s0_section(coord):
                return plan_s0_mapper(video_s0_mapper(coord))
            elif is_coord_in_s1_section(coord):
                return plan_s1_mapper(video_s1_mapper(coord))
            elif is_coord_in_s2_section(coord):
                return plan_s2_mapper(video_s2_mapper(coord))
            elif is_coord_in_s3_section(coord):
                return plan_s3_mapper(video_s3_mapper(coord))
            else:
                print(f"{coord} is invalid")
                return Coord2D(math.inf, math.inf)

        return _map

    else:
        def _map(coord: Coord2D):
            if is_coord_in_s0_section(coord):
                return video_s0_mapper(coord)
            elif is_coord_in_s1_section(coord):
                return video_s1_mapper(coord)
            elif is_coord_in_s2_section(coord):
                return video_s2_mapper(coord)
            elif is_coord_in_s3_section(coord):
                return video_s3_mapper(coord)
            else:
                return Coord2D(math.inf, math.inf)

        return _map


def _image_section_coord_validator_function(image_section: ImageSection) -> Callable[[Coord2D], bool]:
    """
    Builds a function to validate if a given :class:`Coord2D` is inside the :class:`ImageSection` provided.
    :param image_section: :class:`ImageSection` that is used to validate the :class:`Coord2D` in the resulting function.
    :return: a function that takes a :class:`Coord2D` and return a boolean to stating if that :class:`Coord2D` is inside
             the provided :class:`ImageSection`.
    """
    x_min_func = linear_equation_function(
        *reversed(split_coords(np.array([image_section.p0, image_section.p2])))
    )
    x_max_func = linear_equation_function(
        *reversed(split_coords(np.array([image_section.p1, image_section.p3])))
    )
    y_min_func = linear_equation_function(
        *split_coords(np.array([image_section.p0, image_section.p1]))
    )
    y_max_func = linear_equation_function(
        *split_coords(np.array([image_section.p2, image_section.p3]))
    )
    return lambda coord: x_min_func(coord.y) <= coord.x <= x_max_func(coord.y) \
        and y_min_func(coord.x) <= coord.y <= y_max_func(coord.x)


def _perspective_transform(image_section: ImageSection) -> np.ndarray:
    """
    Given a :class:`ImageSection`, a perspective transform matrix is built from :func:`cv2::getPerspectiveTransform`
    with the mean width and height of the given :class:`ImageSection`.
    :param image_section: object containing the coordinated of a image section used to create the perspective transform
           matrix.
    :return: a perspective transform matrix built from :func:`cv2::getPerspectiveTransform`.
    """
    p0, p1, p2, p3 = image_section.__dict__.values()
    width, height = _to_transformed_resolution(image_section)
    return cv2.getPerspectiveTransform(
        np.float32([[p0.x, p0.y], [p1.x, p1.y], [p2.x, p2.y], [p3.x, p3.y]]),
        np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    )


def _transformed_section_mapper_function(
        p0: Coord2D,
        px: Coord2D,
        pxd: float,
        py: Coord2D,
        pyd: float,
        transform: np.ndarray,
        resolution: Resolution,
        distance_to_pixel: bool = False,
) -> Callable[[Coord2D], Coord2D]:
    """
    A linear function is built based on a perspective matrix from a image to turn it in to a flat plane. This is done
    using three :class:`Coord2D`, one representing the point zero, one representing a point in the X axis and one the Y
    axis. It's also used the real world distance between the point zero, and the points provider for the X and Y axis.

    In case any of the values used as argument is None or infinite, a function that maps everything to infinite is
    built.

    :param p0: point zero of the transform.
    :param px: point in the X axis of the transform.
    :param pxd: real world distance between the point zero and the point in the X axis.
    :param py: point in the Y axis of the transform.
    :param pyd: real world distance between the point zero and the point in the Y axis.
    :param transform: a perspective transform matrix for the given section to be transformed.
    :return: a function that takes a :class:`Coord2D` as argument and return a :class:`Coord2D` of the real world
             distance of the given :class:`Coord2D` from the point zero in the real world.
    """
    if p0 is None or p0.x is None or p0.y is None or abs(p0.x) == math.inf or abs(p0.y) == math.inf \
            or px is None or px.x is None or px.y is None or abs(px.x) == math.inf or abs(px.y) == math.inf \
            or py is None or py.x is None or py.y is None or abs(py.x) == math.inf or abs(py.y) == math.inf \
            or pxd is None or pyd is None or abs(pxd) == math.inf or abs(pyd) == math.inf\
            or (not distance_to_pixel and transform is None):

        def _map(p: Coord2D) -> Coord2D:
            return Coord2D(math.inf, math.inf)

        return _map

    if distance_to_pixel:

        if _intercepts_at_x(p0, px, resolution):
            x_func = linear_equation_function(np.array([0, pxd]), np.array([p0.x, px.x]))
            y_func = linear_equation_function(np.array([0, pyd]), np.array([p0.y, py.y]))
        else:
            x_func = linear_equation_function(np.array([0, pxd]), np.array([p0.y, px.y]))
            y_func = linear_equation_function(np.array([0, pyd]), np.array([p0.x, py.x]))

        def _map(p: Coord2D) -> Coord2D:
            return Coord2D(y_func(p.y), x_func(p.x))

        return _map

    else:

        intercepts_at_x = _intercepts_at_x(p0, px, resolution)

        p0 = _transform_coord(p0, transform)
        px = _transform_coord(px, transform)
        py = _transform_coord(py, transform)

        if intercepts_at_x:
            x_func = linear_equation_function(np.array([p0.x, px.x]), np.array([0, pxd]))
            y_func = linear_equation_function(np.array([p0.y, py.y]), np.array([0, pyd]))
        else:
            x_func = linear_equation_function(np.array([p0.x, px.x]), np.array([0, pyd]))
            y_func = linear_equation_function(np.array([p0.y, py.y]), np.array([0, pxd]))

        def _map(p: Coord2D) -> Coord2D:
            x, y = _transform_coord(p, transform)
            return Coord2D(x_func(x), y_func(y))

        return _map


def _intercepts_at_x(p0: Coord2D, p1: Coord2D, resolution: Resolution) -> bool:
    """
    Validates if the two given points intercept the image resolution on sides, making the two points a equivalent of a
    x line on the given image.

    :param p0: first point of the line.
    :param p1: second point of the line.
    :param resolution: resolution of the testes image
    :return: true if the two given points intercept the image resolution on sides, making the two points a equivalent
             of a x line on the given image.
    """
    if p0.x == p1.x:
        return False
    func = linear_equation_function(*split_coords(np.array([p0, p1])))
    y_min = func(0)
    y_max = func(resolution.width)
    return 0 <= y_min <= resolution.height and 0 <= y_max <= resolution.height


def _to_image_sections(configuration: ReferencePointConfiguration) -> ImageSections:
    """
    Based on a provided :class:`VideoConfiguration`, a :class:`ImageSections` objects is generated for the four
    contained image sections provided by the :class:`VideoConfiguration`.

    :param configuration: a object containing coordinate details of four image sections.
    :return: a :class:`ImageSections` based on the :class:`VideoConfiguration`.
    """
    resolution = configuration.resolution
    x_coords = get_line_coords(configuration, AxisType.X, include_inf=False)
    y_coords = get_line_coords(configuration, AxisType.Y, include_inf=False)

    func_x = linear_equation_function(*split_coords(x_coords))
    func_y = linear_equation_function(*split_coords(y_coords))

    p0 = intersection(
        Line(Coord2D(0, func_x(0)), Coord2D(resolution.width, func_x(resolution.width))),
        Line(Coord2D(0, func_y(0)), Coord2D(resolution.width, func_y(resolution.width))),
    )
    p1 = Coord2D(0, 0)
    p2 = intersection(
        Line(Coord2D(0, func_y(0)), Coord2D(resolution.width, func_y(resolution.width))),
        Line(Coord2D(0, 0), Coord2D(resolution.width, 0)),
    )
    p3 = Coord2D(resolution.width, 0)
    p4 = intersection(
        Line(Coord2D(0, func_x(0)), Coord2D(resolution.width, func_x(resolution.width))),
        Line(Coord2D(resolution.width, 0), Coord2D(resolution.width, resolution.height)),
    )
    p5 = Coord2D(resolution.width, resolution.height)
    p6 = intersection(
        Line(Coord2D(0, func_y(0)), Coord2D(resolution.width, func_y(resolution.width))),
        Line(Coord2D(0, resolution.height), Coord2D(resolution.width, resolution.height)),
    )
    p7 = Coord2D(0, resolution.height)
    p8 = intersection(
        Line(Coord2D(0, func_x(0)), Coord2D(resolution.width, func_x(resolution.width))),
        Line(Coord2D(0, 0), Coord2D(0, resolution.width)),
    )

    return ImageSections(
        s0=ImageSection(p1, p2, p8, p0),
        s1=ImageSection(p2, p3, p0, p4),
        s2=ImageSection(p8, p0, p7, p6),
        s3=ImageSection(p0, p4, p6, p5),
    )


def _to_transformed_resolution(image_section: ImageSection) -> Resolution:
    """
    Based on a provided :class:`ImageSection`, a transformed :class:`Resolution` is generated. This is done by taking
    the mean value of the width and height values of the :class:`ImageSection`.

    :param image_section: object containing the :class:`Coord2D` of the edges of a certain image.
    :return: a transformed :class:`Resolution` object.
    """
    p0, p1, p2, p3 = image_section.__dict__.values()
    width = ((p1.x - p0.x) + (p3.x - p2.x)) / 2
    height = ((p2.y - p0.y) + (p3.y - p1.y)) / 2
    return Resolution(round(width), round(height))


def _transform_coord(coord: Coord2D, transform: np.ndarray) -> Coord2D:
    """
    Transforms a :class:`Coord2D` given a transform matrix.

    :param coord: :class:`Coord2D` to be transformed.
    :param transform: a perspective transform to transform the :class:`Coord2D`.
    :return: a transformed :class:`Coord2D`.
    """
    x = transform[0][0] * coord.x + transform[0][1] * coord.y + transform[0][2]
    x /= transform[2][0] * coord.x + transform[2][1] * coord.y + transform[2][2]
    y = transform[1][0] * coord.x + transform[1][1] * coord.y + transform[1][2]
    y /= transform[2][0] * coord.x + transform[2][1] * coord.y + transform[2][2]
    return Coord2D(x, y)
