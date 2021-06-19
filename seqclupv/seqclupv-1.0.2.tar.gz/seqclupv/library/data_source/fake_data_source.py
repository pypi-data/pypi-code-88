"""
    This module contains an implementation of a fake data source that feeds a random number of elements of a predefined
    data set to the 'SeqClu' algorithm at every tick.
"""

from random import randint
from typing import Dict, List, Optional, Union

from numpy import ndarray

from seqclupv.library.interfaces.data_generator import IDataGenerator
from seqclupv.library.interfaces.fake_data_source import IFakeDataSource
from seqclupv.library.utilities.construct_stream import constructStream
from seqclupv.library.utilities.hash_sequence import hashSequence


class FakeDataSource(IFakeDataSource, IDataGenerator):

    # STATIC METHODS #

    @staticmethod
    def combineGeneratedData(clusters: List[List[Union[ndarray, list]]], classes: List[Union[int, chr]],
                             numPrototypes: int) -> tuple:
        """
            This method combines the data that were generated from multiple data sources into one data stream.

            :param clusters: The logical clusters with all the different classes for all the data generators.
            :param classes: All the classes that should be present in the data provided by the data source.
            :param numPrototypes: The number of prototypes used in the 'SeqClu' algorithm.
            :return: The class dictionary, indices, labels and pair-wise distances of the data,
            as well as the data itself
        """
        classDictionary = {k: v for v, k in enumerate(classes)}
        trajectory, randomList = constructStream(clusters, classes, numPrototypes)

        print(f"[SeqCluCLI] The number of incoming sequences is {len(randomList)}.")
        print(f"[SeqCluCLI] The total number of sequences is {len(trajectory)}.")

        data = [x for (x, y) in trajectory]
        indices = [x for x, y in enumerate(data)]
        labels = [y for (x, y) in trajectory]

        return classDictionary, indices, labels, None, data

    # PROPERTIES #

    @property
    def actualLabels(self) -> Optional[Dict[str, Union[chr, int]]]:
        """
            This property stores the correct labels of the data in the data source.

            :return: The correct labels of the data in the data set.
        """
        return self._actualLabels

    @property
    def classes(self) -> List[Union[chr, int]]:
        """
            This property stores all the classes that are present in the data source.

            :return: All the classes that are present in the data set.
        """
        return self._classes

    @property
    def currentIndex(self) -> int:
        """
            This property stores the current index of the data provided by the data source.

            :return: An integer representing the current index of the data provided by the data source.
        """
        return self._currentIndex

    @property
    def currentTick(self) -> int:
        """
            This property stores the current tick of the algorithm.

            :return: An integer representing the current tick of the algorithm.
        """
        return self._currentTick

    @property
    def data(self) -> List[Union[ndarray, list]]:
        """
            This property stores the data provided by the data source.

            :return: The data provided by the data source.
        """
        return self._data

    @property
    def dataSize(self) -> Optional[int]:
        """
            This property stores the amount of data that are provided by the data source.

            :return: An integer representing the amount of data that are provided by the data source.
        """
        return self._dataSize

    @property
    def dataGenerators(self) -> List[IDataGenerator]:
        """
            This property stores the data generators that are used to generate the data provided by the data source.

            :return: A list of data generators that are used to generate the data provided by the data source.
        """
        return self._dataGenerators

    @property
    def maxPerTick(self) -> int:
        """
            This property stores the maximum number of data that can be provided by the data source per tick.

            :return: An integer representing the maximum number of data
            that can be provided by the data source per tick.
        """
        return self._maxPerTick

    @property
    def numClasses(self) -> int:
        """
            The number of classes that are present in the data provided by the data source.

            :return: An integer representing the number of classes that are
            present in the data provided by the data source.
        """
        return self._numClasses

    @property
    def numPrototypes(self) -> int:
        """
            The number of prototypes that are used in the 'SeqClu' algorithm.

            :return: An integer representing the number of prototypes that are used in the 'SeqClu' algorithm.
        """
        return self._numPrototypes

    @currentIndex.setter
    def currentIndex(self, value: int) -> None:
        """
            This is the setter for the 'currentIndex' property.

            :param value: The value that the 'currentIndex' property needs to be set to.
            :return: void
        """
        self._currentIndex = value

    @data.setter
    def data(self, value: ndarray) -> None:
        """
            This is the setter for the 'data' property.

            :param value: The value that the 'data' property needs to be set to.
            :return: void
        """
        self._data = value

    # CONSTRUCTOR #

    def __init__(self, maxPerTick: int, dataGenerators: List[IDataGenerator],
                 numPrototypes: int, computeDistances: bool, classes: List[Union[chr, int]]) -> None:
        """
            This method initializes the data source given the maximum number of data per tick, the data generators
            that should be used to generate the data provided by the data source and the number of prototypes
            that is used in the 'SeqClu' algorithm.

            :param maxPerTick: The maximum number of data that can be provided by the data source per tick.
            :param dataGenerators: The data generators that should be used to
            generate the data provided by the data source.
            :param numPrototypes: The number of prototypes that is used in the 'SeqClu' algorithm.
            :param computeDistances: A boolean value indicating whether or not the pair-wise distances between items
            in the data set should be computed.
            :param classes: All the classes that should be present in the data provided by the data source.
        """
        super().__init__(numPrototypes, computeDistances)
        self._actualLabels = None
        self._currentIndex = 0
        self._currentTick = -1
        self._dataGenerators = dataGenerators
        self._dataSize = None
        self._maxPerTick = maxPerTick
        self._classes = classes
        self._numClasses = len(self.classes)
        self._numPrototypes = numPrototypes

    # PUBLIC METHODS #

    def advanceTick(self) -> List[Union[ndarray, list]]:
        """
            This method advances the state of the data source by one tick. The method returns a list of sequences
            that should be processed by the 'SeqClu' algorithm during the next tick.

            :return: A list of sequences that should be processed by the 'SeqClu' algorithm during the next tick.
        """
        assert self.dataSize is not None
        print(f"[SeqClu] Current index of data is {self.currentIndex}.")
        numberOfElementsToFeed: int = randint(1, self.maxPerTick)
        print(f"[SeqClu] The number of elements that will be processed in this iteration is {numberOfElementsToFeed}.")
        toReturn = None
        if self.currentIndex + numberOfElementsToFeed >= self.dataSize:
            if self.currentIndex >= self.dataSize:
                numberOfElementsToFeed = 0
                toReturn = []
            else:
                numberOfElementsToFeed = self.dataSize - self.currentIndex
        if toReturn is None:
            toReturn = self.data[self.currentIndex:self.currentIndex + numberOfElementsToFeed]
        self._currentIndex += numberOfElementsToFeed
        return toReturn

    def generateData(self) -> List[Union[ndarray, list]]:
        """
            This method generates a data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.

            :return: A data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.
        """
        if len(self.dataGenerators) == 1:
            dataGenerator = self.dataGenerators[0]
            if dataGenerator.data is None:
                dataGenerator.generateData()
            self._data = dataGenerator.data
            self._classDictionary = dataGenerator.classDictionary
            self._classes = dataGenerator.classes
            self._distances = dataGenerator.distances
            self._indices = dataGenerator.indices
            self._labels = dataGenerator.labels
        else:
            clusters: List[List[Union[ndarray, list]]] = list(
                map(lambda x: x.generateData() if x.data is None else x.data, self.dataGenerators))
            self._classDictionary, self._indices, self._labels,\
                self._distances, self._data = FakeDataSource.combineGeneratedData(clusters, self.classes,
                                                                                  self.numPrototypes)
        self._dataSize = len(self.data)
        actualLabels = {}
        for i, label in enumerate(self.labels):
            actualLabels[hashSequence(self.data[i])] = label
        self._actualLabels = actualLabels
        return self.data

    def reset(self) -> None:
        """
            This method sets the current index of the data provided by the data source back to zero to reset the
            data source.

            :return: void
        """
        self._currentIndex = 0
