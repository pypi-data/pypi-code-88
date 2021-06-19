"""
    This module contains an interface for classes that are responsible for generating data that is passed to the
    'SeqClu' algorithm.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Union, Optional

from numpy import ndarray


class IDataGenerator(ABC):

    # PROPERTIES #

    @property
    def classes(self) -> Optional[chr]:
        """
            This property stores the identifiers of items that are present in the data set.

            :return: A list of integers that represent the identifiers of
            the classes of the items that are present in the data set.
        """
        return self._classes

    @property
    def classDictionary(self) -> Dict[str, int]:
        """
            This property stores a mapping from class identifiers to indices.

            :return: A dictionary in which the keys are the identifiers of the classes of the items
            that are present in the data set and the values are the indices of the classes that can be used to
            retrieve the data that belong to a given class from a two-dimensional list containing all items in the data
            set.
        """
        return self._classDictionary

    @property
    def computeDistances(self) -> bool:
        """
            This property stores a boolean value indicating whether or not the pair-wise distances between items in the
            data set should be computed.

            :return: A boolean value indicating whether or not the pair-wise distances between items in the
            data set should be computed.
        """
        return self._computeDistances

    @property
    def data(self) -> Optional[List[ndarray]]:
        """
            This property stores the data in the data set.

            :return: A list of sequences that are present in the data set.
        """
        return self._data

    @property
    def distances(self) -> Optional[ndarray]:
        """
            This property stores the pair-wise distances of items in the data set.

            :return: A two-dimensional array of pair-wise distances where indices i,j represent the indices of the
            two items in the list of sequences stored in the 'data' property.
        """
        return self._distances

    @property
    def indices(self) -> Optional[List[int]]:
        """
            This property stores the indices of items in the data set.

            :return: A list of indices of items in the data set.
        """
        return self._indices

    @property
    def labels(self) -> Optional[List[chr]]:
        """
            This property stores the labels of items in the data set.

            :return: A list of labels of items in the data set.
        """
        return self._labels

    @property
    def numPrototypes(self) -> int:
        """
            This property stores the number of prototypes that should be drawn from the data set.

            :return: An integer representing the number of prototypes that should be drawn from the data set.
        """
        return self._numPrototypes

    @abstractmethod
    def generateData(self) -> List[Union[ndarray, list]]:
        """
            This method generates a data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.

            :return: A data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.
        """
        pass

    def __init__(self, numPrototypes: int, computeDistances: bool) -> None:
        """
            This method initializes the properties of the class.

            :param numPrototypes: The number of prototypes that will be used in the 'SeqClu' algorithm.
            :return: void
        """
        self._classes = None
        self._classDictionary = None
        self._computeDistances = computeDistances
        self._data = None
        self._distances = None
        self._indices = None
        self._labels = None
        self._numPrototypes = numPrototypes
