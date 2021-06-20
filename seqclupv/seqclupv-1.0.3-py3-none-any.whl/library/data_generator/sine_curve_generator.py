"""
    This module contains a class that is responsible for generating data from a sine curve that are passed to the
    'SeqClu' algorithm.
"""

import random
from typing import List, Union, Tuple

import numpy as np
from numpy import ndarray

from seqclupv.library.interfaces.data_generator import IDataGenerator


class CurveGenerator(IDataGenerator):

    # PROPERTIES #

    @property
    def error(self) -> float:
        """
            This property stores the error factor that is used to add
            noise to the sine curve with a random number generator.

            :return: A float representing the error factor.
        """
        return self._error

    @property
    def freq(self) -> Tuple[float, float]:
        """
            This property stores the lower and upper bound used to draw a sample from a uniform distribution that
            will be used as the frequency.

            :return: Two floats representing the lower and upper bound used to draw a sample from a uniform distribution
            that will be used as the frequency.
        """
        return self._freq

    @property
    def n(self) -> int:
        """
            This property stores the number of sequences that should be generated.

            :return: An integer that represents the number of sequences that should be generated.
        """
        return self._n

    @property
    def phase(self) -> int:
        """
            This property stores the phase that is used to generate the sine curve.

            :return: An integer that represents the phase that is used to generate the sine curve.
        """
        return self._phase

    @property
    def samplingRate(self) -> int:
        """
            Defines how the rate at which samples are generated. The higher the value, the fewer samples are generated.

            :return: An integer representing the rate at which samples are generated.
        """
        return self._samplingRate

    # CONSTRUCTOR #

    def __init__(self, n: int, freq: Tuple[float, float], samplingRate: int, error: float, phase: int,
                 numPrototypes: int, computeDistances: bool) -> None:
        """
            This method initializes the data generator that is applicable to the sine curve data set with the parameters
            that are required to generate the data set.

            :param n: The amount of samples that are generated.
            :param freq: The lower and upper bound of the distribution that generates the frequency of a sample.
            :param samplingRate: The rate at which samples are generated.
            :param error: The error factor used to add noise to samples.
            :param phase: The phase that is used to generate the sine curve.
            :param numPrototypes: The number of prototypes that will be used in the 'SeqClu' algorithm.
            :param computeDistances: A boolean value indicating whether or not the pair-wise distances between items
            in the data set should be computed.
            :return: void
        """
        super().__init__(numPrototypes, computeDistances)
        self._error = error
        self._freq = freq
        self._n = n
        self._phase = phase
        self._samplingRate = samplingRate

    # PUBLIC METHODS #

    def generateData(self) -> List[Union[ndarray, list]]:
        """
            This method generates a data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.

            :return: A data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.
        """
        trajectory = []
        for i in range(self.n):
            freq = random.uniform(self.freq[0], self.freq[1])
            line = np.arange(1, 101, self.samplingRate)
            error = [random.random() * self.error for _ in range(len(line))]
            l = np.sin((freq * line) + self.phase) + error
            trajectory.append(l)
        return trajectory
