"""
    This module contains an implementation of the offline version of the 'SeqClu' algorithm that is based on
    Partitioning Around Medoids (PAM).
"""

import time
from typing import Dict, List, Tuple

import numpy as np
from numpy import ndarray

from seqclupv.library.data_source.fake_data_source import FakeDataSource
from seqclupv.library.interfaces.distance_measure import IDistanceMeasure
from seqclupv.library.interfaces.seqclu import ISeqClu
from seqclupv.library.utilities.hash_sequence import hashSequence


class SeqCluBaselineOffline(ISeqClu):

    # STATIC METHODS #

    @staticmethod
    def initializeClusters(numClusters: int, numPrototypes: int) -> ndarray:
        """
            This method initializes the clusters of the 'SeqClu' algorithm given a number of clusters and prototypes.

            :param numClusters: The number of clusters that should be used in the 'SeqClu' algorithm.
            :param numPrototypes: The number of prototypes that should be used in the 'SeqClu' algorithm.'
            :return: The indices of the prototypes for all the clusters, stored in a two-dimensional array.
        """
        result: ndarray = np.empty((numClusters, numPrototypes), dtype=int)
        for i in range(numClusters):
            result[i, :] = [j for j in range(i * numPrototypes, (i + 1) * numPrototypes)]
        return result

    # PROPERTIES #

    @property
    def currentConfigurationCost(self) -> float:
        """
            This property stores the cost of the current configuration.

            :return: A float representing the cost of the current configuration.
        """
        return self._currentConfigurationCost

    @property
    def data(self) -> List[ndarray]:
        """
            This property stores the data that are processed by the 'SeqClu' algorithm.

            :return: The data that are processed by the 'SeqClu' algorithm.
        """
        return self._data

    @property
    def dataSize(self) -> int:
        """
            This property stores the number of sequences that the data set contains.

            :return: An integer representing the number of sequences that the data set contains.
        """
        return self._dataSize

    @property
    def distances(self) -> ndarray:
        """
            This property stores the pair-wise distances for all pairs of sequences in the data set that is processed
            by the 'SeqClu' algorithm.

            :return: A two-dimensional array that contains the pair-wise distances for all pairs of sequences in the
            data set that is processed by the 'SeqClu' algorithm.
        """
        return self._distances

    @property
    def clusters(self) -> ndarray:
        """
            This property stores the current configuration as a two-dimensional array containing the indices of the
            prototypes for every cluster.

            :return: The current configuration as a two-dimensional array containing the indices of the
            prototypes for every cluster.
        """
        return self._clusters

    @property
    def finalLabels(self) -> Tuple[ndarray, Dict[str, int]]:
        """
            This property stores the correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.

            :return: The correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.
        """
        test = set([])
        resultTwo: Dict[str, int] = {}
        result = np.empty((self.dataSize,), dtype=int)
        for i, cluster in enumerate(self.clusters):
            for prototypeIdx in cluster:
                prototypeHash = hashSequence(self.data[prototypeIdx])
                resultTwo[prototypeHash] = self.classes[i]
                result[prototypeIdx] = i
                test.add(prototypeIdx)
        for i, nonPrototypeIdx in enumerate(self._getNonPrototypeIndices(self.clusters)):
            nonPrototypeHash = hashSequence(self.data[nonPrototypeIdx])
            resultTwo[nonPrototypeHash] = self.classes[self.labels[i]]
            result[nonPrototypeIdx] = self.labels[i]
            test.add(nonPrototypeIdx)
        return result, resultTwo

    @property
    def labels(self) -> ndarray:
        """
            This property stores the labels of all sequences that are not prototypes in the 'SeqClu' algorithm.

            :return: The labels of all sequences that are not prototypes in the 'SeqClu' algorithm.
        """
        return self._labels

    @property
    def maxTicks(self) -> int:
        """
            This property stores the maximum number of ticks the algorithm is allowed to execute.

            :return: An integer representing the maximum number of ticks the algorithm is allowed to execute.
        """
        return self._maxTicks

    @property
    def time(self) -> float:
        """
            This property stores the time it took the algorithm to initialize itself.

            :return: A float representing the number of seconds it took the algorithm to initialize itself.
        """
        return self._time

    # CONSTRUCTOR #

    def __init__(self, fakeDataSource: FakeDataSource, distanceMeasure: IDistanceMeasure,
                 numClusters: int, numPrototypes: int, maxTicks: int) -> None:
        """
            This method initializes the 'SeqClu' algorithm with a data source, distance measure, number of clusters
            and number of prototypes.

            :param fakeDataSource: The fake data source that should be used in the 'SeqClu' algorithm.
            :param distanceMeasure: The distance measure that should be used in the 'SeqClu' algorithm.
            :param numClusters: The number of clusters that should be used in the 'SeqClu' algorithm.
            :param numPrototypes: The number of prototypes that should be used in the 'SeqClu' algorithm.
            :param maxTicks: The maximum number of ticks that the algorithm is allowed to execute.
            :return: void
        """
        super().__init__(fakeDataSource, distanceMeasure, numClusters, numPrototypes)
        self._data = fakeDataSource.data
        self._dataSize = fakeDataSource.dataSize
        startTime = time.perf_counter()
        self._distances = np.empty((self.dataSize, self.dataSize))
        self._computeDistances()
        self._maxTicks = maxTicks
        self._clusters = SeqCluBaselineOffline.initializeClusters(numClusters, numPrototypes)
        self._labels, self._currentConfigurationCost = self._computeConfigurationCost(self.clusters,
                                                                                      self._getNonPrototypeIndices(self.clusters))
        endTime = time.perf_counter()
        self._time = endTime - startTime

    # PUBLIC METHODS #

    def execute(self) -> None:
        """
            This method executes the 'SeqClu' algorithm from start to finish. The main loop over the data is
            implemented in here.

            :return: void
        """
        for tick in range(self.maxTicks):
            print(f"[SeqCluBaselineOffline]: Tick {tick}")
            if self.finish:
                break

            oldClusters = self.clusters.copy()

            self._executeOptimalSwap(self._getNonPrototypeIndices(self.clusters))

            # Convergence is obtained once the prototypes for all clusters no longer change.
            if np.all(oldClusters == self.clusters):
                break

    # PUBLIC METHODS #

    def processSequence(self, sequence: Tuple[str, ndarray], considerCandidacy: bool) -> None:
        """
            Since this algorithm is the offline variant of the algorithm, sequences are not processed one-by-one, but
            all at once in an iterative fashion. This method should never be called.
        """
        raise ValueError("This function should never be called.")

    # PRIVATE METHODS #

    def _computeConfigurationCost(self, clusters: ndarray, nonPrototypeIndices: ndarray) -> Tuple[ndarray, float]:
        """
            This method computes the cost of a given configuration of cluster prototypes as well as the predicted
            labels for the given configuration.

            :param clusters: The configuration of cluster prototypes.
            :param nonPrototypeIndices: The indices of the sequences that are not prototypes.
            :return: The predicted labels for the given configuration and the cost for the given configuration.
        """
        resultCost = 0
        resultLabels = np.empty((len(nonPrototypeIndices),), dtype=int)
        for idx, nonPrototypeIdx in enumerate(nonPrototypeIndices):
            label, distance = self._lowestDistanceToCluster(clusters, nonPrototypeIdx)
            resultLabels[idx] = label
            resultCost += distance
        return resultLabels, resultCost

    def _computeDistances(self) -> None:
        """
            This method computes the pair-wise distances for all pairs of sequences in the data set.

            :return: void
        """
        length = len(self.data)
        for i, sequenceOne in enumerate(self.data):
            print(f"[SeqCluBaselineOffline] Computing distances is at iteration {i} of {length}.")
            for j, sequenceTwo in enumerate(self.data):
                if i == j:
                    self.distances[i][j] = 0
                    continue
                distance = self.distanceMeasure.calculateDistance(sequenceOne, sequenceTwo)
                self.distances[i][j] = distance
                self.distances[j][i] = distance

    def _distanceToCluster(self, prototypeIndices: ndarray, sequenceIdx: int) -> float:
        """
            This method computes the distance from some sequence, identified by its index, and a set of prototypes,
            identified by their indices.

            :param prototypeIndices: The indices of the prototypes for which the distance
            to the sequence needs to be computed.
            :param sequenceIdx: The index of the sequence for which the distance to the prototypes needs to be computed.
            :return: The distance from the given sequence to the given set of prototypes.
        """
        return np.sum(self.distances[sequenceIdx][prototypeIndices])

    def _executeOptimalSwap(self, nonPrototypeIndices: ndarray) -> None:
        """
            This method executes the optimal swap as defined in the Partitioning Around Medoids (PAM) algorithm.

            :param nonPrototypeIndices: The indices of the data that are not prototypes.
            :return: void
        """
        costImprovement = 0
        improvedConfiguration = None
        improvedLabels = None

        for prototypeIndices in self.clusters:
            for prototypeIdx in prototypeIndices:
                for nonPrototypeIdx in nonPrototypeIndices:
                    swapConfiguration = np.where(self.clusters == prototypeIdx, nonPrototypeIdx, self.clusters)
                    swapLabels, swapConfigurationCost = self._computeConfigurationCost(swapConfiguration,
                                                                                       self._getNonPrototypeIndices(swapConfiguration))
                    swapCostImprovement = self.currentConfigurationCost - swapConfigurationCost
                    if swapCostImprovement > 0 and swapCostImprovement > costImprovement:
                        costImprovement = swapCostImprovement
                        improvedConfiguration = swapConfiguration
                        improvedLabels = swapLabels

        if improvedConfiguration is not None and improvedLabels is not None:
            self._clusters = improvedConfiguration
            self._currentConfigurationCost -= costImprovement
            self._labels = improvedLabels

    def _getNonPrototypeIndices(self, clusters: ndarray) -> ndarray:
        """
            This method returns the indices of the data that are not prototypes.

            :param clusters: The clusters that are represented as 'numClusters' * 'numPrototypes' prototypes.
            :return: The indices of the data that are not prototypes stored in a NumPy array.
        """
        return np.delete(np.arange(self.dataSize), clusters.flatten())

    def _lowestDistanceToCluster(self, clusters: ndarray, sequenceIdx: int) -> Tuple[int, float]:
        """
            This method computes the lowest distance from a given sequence to any of the clusters.

            :param clusters: The clusters that should be considered.
            :param sequenceIdx: The index of the sequence.
            :return: A tuple containing the cluster index that minimizes the distance from the given sequence to the
            cluster as well as this distance.
        """
        lowestClusterIdx = -1
        lowestDistance = np.inf
        for cIdx in range(self.numClusters):
            distance = self._distanceToCluster(clusters[cIdx], sequenceIdx)
            if distance < lowestDistance:
                lowestClusterIdx = cIdx
                lowestDistance = distance
        return lowestClusterIdx, lowestDistance
