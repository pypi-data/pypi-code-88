"""
    This module contains the interface for fake data sources that store a predefined data set that the 'SeqClu'
    algorithm can request data to process from.
"""
from abc import ABC, abstractmethod
from typing import List, Union

from numpy import ndarray

from seqclupv.library.interfaces.data_source import IDataSource


class IFakeDataSource(IDataSource, ABC):

    @property
    @abstractmethod
    def data(self) -> List[Union[ndarray, list]]:
        """
            This property stores the data provided by the data source.

            :return: The data provided by the data source.
        """
        pass

    @property
    @abstractmethod
    def numClasses(self) -> int:
        """
            The number of classes that are present in the data provided by the data source.

            :return: An integer representing the number of classes that are
            present in the data provided by the data source.
        """
        pass
