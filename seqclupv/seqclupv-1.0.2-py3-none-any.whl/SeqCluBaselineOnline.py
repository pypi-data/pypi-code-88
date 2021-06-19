"""
    This module contains a naive implementation of the online version of the 'SeqClu' algorithm that is used to compare
    the results of the developed variants of the 'SeqClu' algorithm to the results of the implementation contained in
    this module that serves as the baseline.
"""

from typing import Dict, List, Optional, Tuple, Union

import numpy as np
from numpy import ndarray

from seqclupv.library.data_source.fake_data_source import FakeDataSource
from seqclupv.library.interfaces.distance_measure import IDistanceMeasure
from seqclupv.library.interfaces.seqclu import ISeqClu
from seqclupv.library.utilities.hash_sequence import hashSequence


class SeqCluBaselineOnline(ISeqClu):

    # PROPERTIES #

    @property
    def clusters(self) -> ndarray:
        return self._clusters

    @property
    def distances(self) -> Dict[Tuple[str, str], float]:
        return self._distances

    @property
    def labels(self) -> Dict[str, Union[chr, int]]:
        return self._labels

    @property
    def finalLabels(self) -> Dict[str, Union[chr, int]]:
        """
            This property stores the correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.

            :return: The correct labels as a dictionary where the keys are the hashes of the sequences
            and the values are the correct labels.
        """
        result = {}
        for clusterIdx, prototypeHashes in enumerate(self.clusters):
            for prototypeHash in prototypeHashes:
                result[prototypeHash] = self.classes[clusterIdx]
        result.update(self.labels)
        return result

    @property
    def numProcessed(self) -> int:
        return self._numProcessed

    @property
    def prototypes(self) -> List[Dict[str, ndarray]]:
        return self._prototypes

    # CONSTRUCTOR #

    def __init__(self, dataSource: FakeDataSource, distanceMeasure: IDistanceMeasure,
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
        super().__init__(dataSource, distanceMeasure, numClusters, numPrototypes)
        self._distances = {}
        self._labels = {}
        self._numProcessed = 0
        prototypesList = []
        for _ in range(numClusters):
            prototypesList.append({})
        self._prototypes = prototypesList
        self._clusters = self._initializeClusters(dataSource)

    # PUBLIC METHODS #

    def alreadyProcessed(self, sequenceHash: str) -> bool:
        # Check if the sequence is already stored as a prototype of any of the clusters or as a candidate.
        if sequenceHash in self.labels:
            return True
        for clusterIdx in range(self.numClusters):
            if sequenceHash in self.prototypes[clusterIdx]:
                return True
        return False

    def execute(self) -> None:
        """
            This method executes the 'SeqClu' algorithm from start to finish. The main loop over the data is
            implemented in here.

            :return: void
        """
        iteration = 0
        while not self.finish:
            iteration += 1
            print(f"[SeqClu] Iteration {iteration}.")
            finish = self._advanceTick()
            if finish:
                print("[SeqClu] The algorithm finished executing. Processing the buffer and returning...")
                break

    def processSequence(self, sequence: Tuple[str, ndarray], considerCandidacy: bool) -> None:
        """
            This method processes one sequence of the data set that is processed in the 'SeqClu' algorithm.

            :param sequence: The sequence that should be processed in the 'SeqClu' algorithm.
            :param considerCandidacy: A boolean value indicating whether or not the algorithm should consider if the
            sequence could be a prototype for any of the clusters.
            :return: void
        """
        if self.alreadyProcessed(sequence[0]):
            return
        sequenceHash, sequenceData = sequence
        minDistance = np.inf
        minIdx = -1

        for clusterIdx, cluster in enumerate(self.clusters):
            distance = 0
            for prototypeHash in cluster:
                distance += self._getDistance(clusterIdx, sequence, (prototypeHash, None))
            distance = distance / self.numPrototypes

            if minDistance > distance:
                minDistance = distance
                minIdx = clusterIdx

        self._updatePrototypes(minIdx, sequence)

        self._labels[sequenceHash] = self.classes[minIdx]

    # PRIVATE METHODS #

    def isPrototypeForMultiple(self, prototypeHash: str) -> bool:
        counter = 0
        for clusterIdx in range(self.numClusters):
            counter += np.count_nonzero(self.clusters[clusterIdx] == prototypeHash)
        if counter == 0:
            raise ValueError("Invalid function call, the provided hash does not correspond to a prototype for any"
                             " of the clusters.")
        return counter > 1

    def _getDistance(self, clusterIdx: int, sequenceOne: Tuple[str, Optional[ndarray]],
                     sequenceTwo: Tuple[str, Optional[ndarray]]) -> float:
        sequenceHashOne, sequenceDataOne = sequenceOne
        sequenceHashTwo, sequenceDataTwo = sequenceTwo

        if (sequenceHashOne, sequenceHashTwo) in self.distances:
            return self.distances[(sequenceHashOne, sequenceHashTwo)]
        if (sequenceHashTwo, sequenceHashOne) in self.distances:
            return self.distances[(sequenceHashTwo, sequenceHashOne)]
        if sequenceDataOne is None:
            sequenceDataOne = self.prototypes[clusterIdx][sequenceHashOne]
        if sequenceDataTwo is None:
            sequenceDataTwo = self.prototypes[clusterIdx][sequenceHashTwo]

        distance = self.distanceMeasure.calculateDistance(sequenceDataOne, sequenceDataTwo)
        self.distances[(sequenceHashOne, sequenceHashTwo)] = distance
        self.distances[(sequenceHashTwo, sequenceHashOne)] = distance

        return distance

    def _initializeClusters(self, dataSource: FakeDataSource) -> ndarray:
        result = np.empty((self.numClusters, self.numPrototypes), dtype=object)
        # NOTE: The first numClusters * numPrototypes sequences could contain identical sequences.
        for i in range(self.numClusters):
            for j, sequence in enumerate(dataSource.data[i * self.numPrototypes:i * self.numPrototypes + self.numPrototypes]):
                sequenceHash = hashSequence(sequence)
                result[i][j] = sequenceHash
                self.prototypes[i][sequenceHash] = sequence
        dataSource.currentIndex = self.numClusters * self.numPrototypes
        return result

    def _updatePrototypes(self, minIdx: int, sequence: Tuple[str, ndarray]) -> None:
        sequenceHash, sequenceData = sequence
        prototypeHashes = self.clusters[minIdx]
        sums = []
        for i, prototypeHashOne in enumerate(prototypeHashes):
            s = 0
            for j, prototypeHashTwo in enumerate(prototypeHashes):
                if i != j:
                    s += self._getDistance(minIdx, (prototypeHashOne, None), (prototypeHashTwo, None))
            sums.append(s)
        zipped = list(zip(sums, [i for i in range(self.numPrototypes)]))
        zipped.sort(key=lambda x: x[0])

        toReplaceIdx = zipped[-1][1]
        toReplaceHash = prototypeHashes[toReplaceIdx]
        assert self.clusters[minIdx][toReplaceIdx] == toReplaceHash
        if not self.isPrototypeForMultiple(toReplaceHash):
            del self.prototypes[minIdx][toReplaceHash]
        self.clusters[minIdx][toReplaceIdx] = sequenceHash
        self.labels[toReplaceHash] = self.classes[minIdx]
        self.prototypes[minIdx][sequenceHash] = sequenceData
