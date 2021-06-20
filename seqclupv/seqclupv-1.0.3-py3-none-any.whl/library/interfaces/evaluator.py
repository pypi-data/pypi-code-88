"""
	This module contains the interface for evaluators that can assess the performance of the variants of the 'SeqClu'
	algorithm.
"""
from abc import ABC, abstractmethod


class IEvaluator(ABC):

	# PUBLIC METHODS #

	@abstractmethod
	def evaluate(self) -> None:
		"""
			This method evaluates the performance of the variants of the 'SeqClu' algorithm.

			:return: void
		"""
		pass
