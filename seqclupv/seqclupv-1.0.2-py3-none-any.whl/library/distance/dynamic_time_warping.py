"""
	This module contains an implementation of the 'Dynamic Time Warping' distance measure that is used in the 'SeqClu'
	algorithm to compute the distance between two sequences.
"""

from seqclupv.library.interfaces.distance_measure import IDistanceMeasure

from numpy import ndarray
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


class DynamicTimeWarping(IDistanceMeasure):

	# PROPERTIES #

	@property
	def timesCalled(self) -> int:
		"""
			This property stores the counter on the amount of times that the distance measure is used to compute the
			distance between two sequences.

			:return: An integer representing the counter on the amount of times that the distance measure is used to
			compute the distance between two sequences.
		"""
		return self._timesCalled

	# CONSTRUCTOR #

	def __init__(self) -> None:
		"""
			This method initializes the distance measure by setting the counter on the amount of times that the distance
			measure is used to compute the distance between two sequences to zero.
		"""
		self._timesCalled = 0

	# PUBLIC METHODS #

	def calculateDistance(self, sequenceOne: ndarray, sequenceTwo: ndarray) -> float:
		"""
			This method calculates the distance between two sequences.

			:param sequenceOne: The first sequence for which the distance should be computed.
			:param sequenceTwo: The second sequence for which the distance should be computed.
			:return: The distance between the two sequences.
		"""
		self._timesCalled += 1
		return fastdtw(sequenceOne, sequenceTwo, dist=euclidean)[0]

	def reset(self) -> None:
		"""
			This method resets the counter on the amount of times that the distance measure is used to compute the
			distance between two sequences.

			:return: void
		"""
		self._timesCalled = 0
