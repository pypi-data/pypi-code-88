from dataclasses import dataclass


class _ModelCommon:

    def __getitem__(self, item):
        return self.__dict__[dir(self)[item + 31]]

    def __iter__(self):
        for key in self.__dict__:
            yield self.__dict__[key]


@dataclass(frozen=True, order=True)
class Coord2D(_ModelCommon):
    """
    Representation of a 2 dimension coordinate.
    """
    x: float
    y: float


@dataclass(frozen=True, order=True)
class Detection(_ModelCommon):
    """
    Representation of a detection using the following format.

    p0----------++
    ||          ||
    ||          ||
    ||          ||
    ++----------p1
    """
    p0: Coord2D
    p1: Coord2D
    confidence: float


@dataclass(frozen=True, order=True)
class ImageSection(_ModelCommon):
    """
    Representation of a image section of four coordinates using the following format.

    p0----------p1
    ||          ||
    ||          ||
    ||          ||
    p2----------p3
    """
    p0: Coord2D
    p1: Coord2D
    p2: Coord2D
    p3: Coord2D


@dataclass(frozen=True, order=True)
class ImageSections(_ModelCommon):
    """
    The representation of multiple image sections forming a complete image in the following format.

    +----------+----------+
    |          |          |
    |    S0    |    S1    |
    |          |          |
    +----------+----------+
    |          |          |
    |    S2    |    S3    |
    |          |          |
    +----------+----------+
    """
    s0: ImageSection
    s1: ImageSection
    s2: ImageSection
    s3: ImageSection


@dataclass(frozen=True, order=True)
class Line(_ModelCommon):
    """
    The representation of a line from two coordinates.
    """
    p0: Coord2D
    p1: Coord2D


@dataclass(frozen=True, order=True)
class Resolution(_ModelCommon):
    """
    The representation of a resolution.
    """
    width: int
    height: int


@dataclass(frozen=True, order=True)
class TrackedDetection(Detection):
    track_id: str


@dataclass(frozen=True, order=True)
class ReferencePointConfiguration(_ModelCommon):
    """
    The representation of a reference point configuration from a image using the following format.

           ||
           p2
           ||
    --p1---p0---p3--
           ||
           p4
           ||
    """

    resolution: Resolution

    p0: Coord2D

    p1: Coord2D
    p1d: float

    p2: Coord2D
    p2d: float

    p3: Coord2D
    p3d: float

    p4: Coord2D
    p4d: float
