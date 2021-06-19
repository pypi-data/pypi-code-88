"""
    This module contains an implementation of a heuristic functions that are used in variants of the 'SeqClu' algorithm.
    The heuristic function calculates the value of a (candidate) prototype based on a linear combination of the
    representativeness and the weight of the (candidate) prototype.
"""

from seqclupv.library.interfaces.heuristics.prototype_value import IPrototypeValue


class LinearPrototypeValue(IPrototypeValue):

    # PROPERTIES #

    @property
    def ratio(self) -> float:
        """
            Returns the value 'a' in a:1 where a:1 is the ratio between the representativeness and the weight.

            :return: The value 'a' in a:1 where a:1 is the ratio between the representativeness and the weight.
        """
        return self._ratio

    # CONSTRUCTORS #

    def __init__(self, ratio: float) -> None:
        """
            This method initializes the function that returns the linear combination of the representativeness and
            weight of a prototype.

            :param ratio: The value 'a' in a:1 where a:1 is the ratio between the representativeness and the weight.
        """
        self._ratio = ratio

    def evaluate(self, representativeness: float, weight: float) -> float:
        """
            This method evaluates the function that returns the linear combination of the representativeness and
            weight of some prototype.

            :param representativeness: The representativeness of some prototype.
            :param weight: The weight of some prototype.
            :return: The value of the prototype.
        """
        weightRatio = 1 / (self.ratio + 1)
        representativenessRatio = 1 - weightRatio
        result = representativenessRatio * representativeness + weightRatio * weight
        return result
