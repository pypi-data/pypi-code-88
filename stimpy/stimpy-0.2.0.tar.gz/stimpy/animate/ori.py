from abc import abstractmethod
from typing import Callable, Tuple

import numpy as np

from ._func import Func


class OriFunc(Func):
    @abstractmethod
    def __call__(self, t: float) -> float:
        """
        :param t: Time.
        :return: Orientation in degrees.
        """
        pass


class Tangential(OriFunc):
    def __init__(
        self,
        pos_func: Callable[[float], Tuple[float, float]],
        dt: float = 1e-2,
        init_ori: float = 0,
    ):
        """Orient the stimulus tangentially to its trajectory.

        :param pos_func: Position as function of time.
        :param dt: Approximate time between consecutive frames.
        """
        self.__pos_func = pos_func
        self.__dt = dt
        self.__init_ori = init_ori
        self.__prev_ori = init_ori

    def __call__(self, t: float):
        old_value = np.array(self.__pos_func(t - self.__dt))
        new_value = np.array(self.__pos_func(t))
        if all(old_value == new_value):
            return self.__prev_ori
        ori = (
            np.rad2deg(np.arctan2(*(new_value - old_value))) + self.__init_ori
        )
        self.__prev_ori = ori
        return ori
