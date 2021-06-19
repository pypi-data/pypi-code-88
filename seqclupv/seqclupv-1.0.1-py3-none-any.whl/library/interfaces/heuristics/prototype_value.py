"""
    This module contains the interface for a heuristic function that calculates the value of a (candidate) prototype
    given the representativeness and weight of the prototype.
"""

from abc import ABC, abstractmethod


class IPrototypeValue(ABC):

    @abstractmethod
    def evaluate(self, representativeness: float, weight: float) -> float:
        """
            This method evaluates the function that returns the linear combination of the representativeness and
            weight of some prototype.

            :param representativeness: The representativeness of some prototype.
            :param weight: The weight of some prototype.
            :return: The value of the prototype.
        """
        pass
