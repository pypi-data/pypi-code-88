from abc import abstractmethod
from typing import Callable, Tuple, Union

import numpy as np

from ._func import Func


class PosFunc(Func):
    @abstractmethod
    def __call__(self, t: float) -> Tuple[float, float]:
        """
        :param t: Time.
        :return: x, y positions.
        """
        pass


class Circulating(PosFunc):
    """Circulate in an elliptic trajectory.

    :param center: Coordinate(s) of the center of the circulation trajectory.
    :param size: Diameter(s) of the circulation trajectory.
    :param period: Circulation period.
    :param init_angle: Initial angle in degrees. 0° is rightward to the center.
        Increases in counterclockwise direction.
    :param clockwise: Whether to circulate in clockwise direction.
    """

    def __init__(
        self,
        center: Union[float, Tuple[float, float]],
        size: Union[Callable, float, Tuple[float, float]],
        period: float,
        init_angle: float,
        clockwise: bool,
    ):
        self.__center = center
        self.__size = size
        self.__period = period
        self.__init_angle = init_angle
        self.__clockwise = clockwise

    def __call__(self, t: float) -> Tuple[float, float]:
        theta = np.deg2rad(
            360 / self.__period * (t if self.__clockwise else -t)
            + self.__init_angle
        )
        size = self.__size(t) if callable(self.__size) else self.__size
        x, y = (
            size * np.array((np.cos(theta), np.sin(theta))) / 2 + self.__center
        )
        return x, y
