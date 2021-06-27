from abc import ABC, abstractmethod


class Func(ABC):
    """Abstract base class for functions of time."""

    @abstractmethod
    def __call__(self, t: float):
        """
        :param t: Time.
        :return: Value of an attribute of the stimulus at time t.
        """
        pass
