"""
	This module contains the interface for the data sources that are used by the 'SeqClu' algorithm to request
	data at every tick.
"""
from abc import ABC, abstractmethod
from typing import List, Union

from numpy import ndarray


class IDataSource(ABC):

	# PROPERTIES #

	@property
	@abstractmethod
	def classes(self) -> List[Union[chr, int]]:
		"""
			This property stores all the classes that are present in the data source.

			:return: All the classes that are present in the data set.
		"""
		pass

	@abstractmethod
	def advanceTick(self) -> List[Union[ndarray, list]]:
		"""
			This method advances the state of the data source by one tick. The method returns a list of sequences
			that should be processed by the 'SeqClu' algorithm during the next tick.

			:return: A list of sequences that should be processed by the 'SeqClu' algorithm during the next tick.
		"""
		pass
