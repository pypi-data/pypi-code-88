from abc import abstractmethod

from ._func import Func


class Opacity(Func):
    @abstractmethod
    def __call__(self, t: float) -> float:
        """
        :param t: Time.
        :return: Opacity.
        """
