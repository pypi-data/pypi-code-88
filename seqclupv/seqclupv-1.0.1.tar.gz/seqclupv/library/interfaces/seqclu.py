"""
    This module contains an interface for the 'SeqClu' algorithm. Some methods are already implemented.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union

from numpy import ndarray

from seqclupv.library.interfaces.data_source import IDataSource
from seqclupv.library.interfaces.distance_measure import IDistanceMeasure
from seqclupv.library.utilities.hash_sequence import hashSequence


class ISeqClu(ABC):

    # PROPERTIES #

    @property
    def classes(self) -> List[Union[chr, int]]:
        """
            This property stores the classes of the items that are present in the data set.

            :return: The classes of the items that are present in the data set.
        """
        return self._classes

    @property
    def dataSource(self) -> IDataSource:
        """
            This property stores the data source that is used to retrieve data that need to be processed by
            the algorithm.

            :return: The data source that is used to retrieve data that need to be processed by the algorithm.
        """
        return self._dataSource

    @property
    def distanceMeasure(self) -> IDistanceMeasure:
        """
            This property stores the distance measure that is used to compute the distance between two sequences.

            :return: The distance measure that is used to compute the distance between two sequences.
        """
        return self._distanceMeasure

    @property
    @abstractmethod
    def finalLabels(self) -> Dict[str, Union[chr, int]]:
        """
            This property stores the correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.

            :return: The correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.
        """
        pass

    @property
    def finish(self) -> bool:
        """
            This property stores a boolean value indicating whether or not the algorithm finished executing.

            :return: A boolean value indicating whether or not the algorithm finished executing.
        """
        return self._finish

    @property
    def numClusters(self) -> int:
        """
            This property stores the number of clusters that are used in the 'SeqClu' algorithm.

            :return: An integer representing the number of clusters that are used in the 'SeqClu' algorithm.
        """
        return self._numClusters

    @property
    def numPrototypes(self) -> int:
        """
            This property stores the number of prototypes that are used in the 'SeqClu' algorithm.

            :return: An integer representing the number of prototypes that are used in the 'SeqClu' algorithm.
        """
        return self._numPrototypes

    @property
    def tick(self) -> int:
        """
            This property stores the tick of the algorithm, which represents the moment in time relative to the start
            of the execution of the algorithm.

            :return: An integer representing the tick of the algorithm, which represents the moment in time relative
            to the start of the execution of the algorithm.
        """
        return self._tick

    @finish.setter
    def finish(self, value: bool) -> None:
        """
            This is the setter for the 'finish' property.

            :param value: The value that the 'finish' property should be set to.
            :return: void
        """
        self._finish = value

    # CONSTRUCTOR #

    def __init__(self, dataSource: IDataSource, distanceMeasure: IDistanceMeasure,
                 numClusters: int, numPrototypes: int) -> None:
        """
            This method initializes the 'SeqClu' algorithm with a data source, distance measure, number of clusters
            and number of prototypes.

            :param dataSource: The data source that should be used in the 'SeqClu' algorithm.
            :param distanceMeasure: The distance measure that should be used in the 'SeqClu' algorithm.
            :param numClusters: The number of clusters that should be used in the 'SeqClu' algorithm.
            :param numPrototypes: The number of prototypes that should be used in the 'SeqClu' algorithm.
            :return: void
        """
        self._classes = dataSource.classes
        self._dataSource = dataSource
        self._distanceMeasure = distanceMeasure
        self._finish = False
        self._numClusters = numClusters
        self._numPrototypes = numPrototypes
        self._tick = -1

    # PUBLIC METHODS #

    @abstractmethod
    def execute(self) -> None:
        """
            This method executes the 'SeqClu' algorithm from start to finish. The main loop over the data is
            implemented in here.

            :return: void
        """
        pass

    @abstractmethod
    def processSequence(self, sequence: Tuple[str, ndarray], considerCandidacy: bool) -> None:
        """
            This method processes one sequence of the data set that is processed in the 'SeqClu' algorithm.

            :param sequence: The sequence that should be processed in the 'SeqClu' algorithm.
            :param considerCandidacy: A boolean value indicating whether or not the algorithm should consider if the
            sequence could be a prototype for any of the clusters.
            :return: void
        """
        pass

    # PRIVATE METHODS #

    def _advanceTick(self) -> bool:
        """
            This method advances the tick of the algorithm.

            :return: A boolean value indicating whether or not sequences were processed during this tick.
        """
        # Increment the tick.
        self._tick += 1

        sequencesToProcess = self.dataSource.advanceTick()
        if not sequencesToProcess:
            return True

        for sequence in sequencesToProcess:
            sequenceHash = hashSequence(sequence)
            self.processSequence((sequenceHash, sequence), True)

        return False
