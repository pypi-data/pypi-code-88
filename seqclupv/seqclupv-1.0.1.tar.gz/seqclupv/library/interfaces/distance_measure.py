"""
	This module contains an interface for the distance measures that are used to compute the distance between two
	data points in the 'SeqClu' algorithm.
"""
from abc import ABC, abstractmethod
from typing import Union

from numpy import ndarray


class IDistanceMeasure(ABC):

	@abstractmethod
	def calculateDistance(self, sequenceOne: Union[ndarray, list], sequenceTwo: Union[ndarray, list]) -> float:
		"""
			This method calculates the distance between two sequences.

			:param sequenceOne: The first sequence for which the distance should be computed.
			:param sequenceTwo: The second sequence for which the distance should be computed.
			:return: The distance between the two sequences.
		"""
		pass
