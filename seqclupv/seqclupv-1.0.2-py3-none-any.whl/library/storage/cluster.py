"""
    This module contains an implementation of the data structure that stores all relevant information about one of the
    clusters that are maintained as part of the 'SeqClu' algorithm.
"""

from typing import Dict, Optional, Set, Tuple

import numpy as np
from numpy import ndarray

from seqclupv.library.storage.prototype_frequencies import PrototypeFrequencyStore
from seqclupv.library.storage.prototypes import PrototypeStore
from seqclupv.library.interfaces.distance_measure import IDistanceMeasure

from seqclupv.library.utilities.hash_filter import isHashInKey
from seqclupv.library.utilities.hash_sequence import hashSequence


class ClusterStore:

    @property
    def averageDistance(self) -> float:
        """
            This property stores the average distance between any prototype and all other prototypes in the cluster.

            :return: The average distance between any prototype and all other prototypes in the cluster.
        """
        if self._averageDistance is None:
            self._averageDistance = self.averageSumOfDistances / (self.prototypes.numPrototypes - 1)
        return self._averageDistance

    @property
    def averageDistanceFromRepresentativeToNonRepresentative(self) -> float:
        """
            This property stores the average distance from representative prototypes to non-representative prototypes
            in the cluster.

            :return: The average distance from representative prototypes to non-representative prototypes
            in the cluster.
        """
        if self._averageDistanceFromRepresentativeToNonRepresentative is None:
            self._averageDistanceFromRepresentativeToNonRepresentative = \
                self._calculateAverageSumOfDistancesRepresentativeToNonRepresentative() \
                / self.prototypes.numOtherPrototypes
        return self._averageDistanceFromRepresentativeToNonRepresentative

    @property
    def averageRepresentativeness(self) -> float:
        """
            This property stores the average representativeness of prototypes in the cluster.

            :return: The average representativeness of prototypes in the cluster.
        """
        if self._averageRepresentativeness is None:
            self._averageRepresentativeness = self._calculateAverageRepresentativeness()
        return self._averageRepresentativeness

    @property
    def averageSumOfDistances(self) -> float:
        """
            This property stores the average sum of distances between all pairs of prototypes in the cluster.

            :return: The average sum of distances between all pairs of prototypes in the cluster.
        """
        if self._averageSumOfDistances is None:
            self._averageSumOfDistances = self._calculateAverageSumOfDistances(False)
        return self._averageSumOfDistances

    @property
    def distanceMeasure(self) -> IDistanceMeasure:
        """
            This property stores the distance measure that is used in the 'SeqClu' algorithm.

            :return: The distance measure that is used in the 'SeqClu' algorithm.
        """
        return self._distanceMeasure

    @property
    def distances(self) -> Dict[Tuple[str, str], float]:
        """
            This property stores the pair-wise distances between pairs of (candidate) prototypes.

            :return: The pair-wise distances between pairs of (candidate) prototypes.
        """
        return self._distances

    @property
    def error(self) -> float:
        """
            This property stores the error that is made in every approximation of the distance from an incoming
            sequence to the cluster.

            :return: The error that is made in every approximation of the distance from an incoming
            sequence to the cluster.
        """
        if self._error is None:
            self._error = (1 - self.averageRepresentativeness) \
                          * self.averageDistanceFromRepresentativeToNonRepresentative
        return self._error

    @property
    def identifier(self) -> int:
        """
            This property stores the identifier of the cluster.

            :return: An integer representing the identifier of the cluster.
        """
        return self._identifier

    @property
    def prototypeFrequencies(self) -> PrototypeFrequencyStore:
        return self._prototypeFrequencies

    @property
    def prototypes(self) -> PrototypeStore:
        """
            This property stores the prototypes of the cluster.

            :return: The prototypes of the cluster.
        """
        return self._prototypes

    @property
    def sumsOfDistances(self) -> Dict[Tuple[str, bool], float]:
        """
            This property stores the sum of distances from a given prototype to all other prototypes in the cluster.

            :return: The sum of distances from a given prototype to all other prototypes in the cluster.
        """
        return self._sumsOfDistances

    @property
    def upperBound(self) -> float:
        """
            This property stores the upper bound of the distance between some incoming sequence and the cluster for the
            sequence to be considered as a candidate prototype.

            :return: The upper bound of the distance between some incoming sequence and the cluster for the
            sequence to be considered as a candidate prototype.
        """
        if self._upperBound is None:
            self._upperBound = self.averageDistance + self.error
        return self._upperBound

    def __init__(self, identifier: int, numRepresentativePrototypes: int, numPrototypes: int,
                 distanceMeasure: IDistanceMeasure, tick: int) -> None:
        """
            This method initializes the cluster given its identifier, the number of (representative) prototypes, the
            distance measure that should be used and the tick at which the cluster was initialized.

            :param identifier: The identifier of the cluster.
            :param numRepresentativePrototypes: The number of representative prototypes.
            :param numPrototypes: The number of prototypes.
            :param distanceMeasure: The distance measure that should be used by the cluster.
            :param tick: The tick at which the cluster was initialized.
        """
        self._averageDistance: Optional[float] = None
        self._averageDistanceFromRepresentativeToNonRepresentative: Optional[float] = None
        self._averageRepresentativeness: Optional[float] = None
        self._averageSumOfDistances: Optional[float] = None
        self._distanceMeasure = distanceMeasure
        self._distances = {}
        self._error = None
        self._identifier = identifier
        self._prototypeFrequencies = PrototypeFrequencyStore(numPrototypes)
        self._prototypes = PrototypeStore(numRepresentativePrototypes, numPrototypes, tick)
        self._sumsOfDistances = {}
        self._sumsOfRepresentativeDistances = {}
        self._upperBound: Optional[float] = None

    def computeAverageDistance(self, sequence: Tuple[Optional[str], Optional[ndarray]], representative: bool) -> float:
        """
            This method computes the average distance between some sequence and either the representative prototypes
            or all prototypes.

            :param sequence: The sequence for which the average distance between itself and some set of prototypes
            needs to be computed.
            :param representative: A boolean value indicating whether or not the distance to the representative
            prototypes should be computed. If this value is false, the distance to all prototypes is computed instead.
            :return: The average distance between the given sequence and either the representative prototypes or all
            prototypes.
        """
        sumOfDistances = self.sumOfDistancesOf(sequence, representative)
        if representative:
            return sumOfDistances / self.prototypes.numRepresentativePrototypes
        return sumOfDistances / self.prototypes.numPrototypes

    def isCandidate(self, sequence: Tuple[Optional[str], Optional[ndarray]],
                    minimumRepresentativeness: float, clusterAssignment: bool) -> Tuple[float, bool, bool]:
        """
            This method checks if a given sequence is a candidate prototype for the cluster.

            :param sequence: The sequence for which needs to be checked whether or not it is a candidate to become
            a prototype for the cluster.
            :param minimumRepresentativeness: The minimum representativeness that the prototypes should have in order
            for approximation of the distance to the cluster to be used. If the prototypes are not representative
            enough, the accurate distance to the cluster is computed instead.
            :param clusterAssignment: A boolean value indicating whether or not to approximate the distance to the
            cluster.
            :return: A tuple containing either the approximated or accurate distance from the sequence to the cluster,
            a boolean value indicating whether or not the sequence is a candidate prototype and whether or not the
            distance from the sequence to the cluster was approximated.
        """
        if clusterAssignment and self.isRepresentativeEnough(minimumRepresentativeness):
            approximatedDistance = self.computeAverageDistance(sequence, True)
            return approximatedDistance, approximatedDistance < self.upperBound, True
        else:
            accurateDistance = self.computeAverageDistance(sequence, False)
            return accurateDistance, accurateDistance < self.averageDistance, False

    def isRepresentativeEnough(self, minimumRepresentativeness: float) -> bool:
        """
            This method determines whether or not the representative prototypes of the cluster are representative
            enough.

            :param minimumRepresentativeness: The minimum average representativeness the representative prototypes
            should have for them to be considered representative enough.
            :return: A boolean value indicating whether or not the representative prototypes of the cluster are
            representative enough.
        """
        return self.averageRepresentativeness >= minimumRepresentativeness

    def pairwiseDistanceOf(self, sequenceOne: Tuple[Optional[str], Optional[ndarray]],
                           sequenceTwo: Tuple[Optional[str], Optional[ndarray]]) -> float:
        """
            This method calculates the distance of two sequences.
            The result of this computation is memoized and if the distance is requested again at a later point in time,
            the calculation is not done again to save time.

            :param sequenceOne: The first sequence for which the distance should be computed.
            :param sequenceTwo: The second sequence for which the distance should be computed.
            :return: The computed distance between the two sequences.
        """
        sequenceOneHash, _ = sequenceOne
        sequenceTwoHash, _ = sequenceTwo
        if sequenceOneHash is not None and sequenceTwoHash is not None:
            if sequenceOneHash == sequenceTwoHash:
                return 0
            if (sequenceOneHash, sequenceTwoHash) in self.distances:
                return self.distances[(sequenceOneHash, sequenceTwoHash)]
            if (sequenceTwoHash, sequenceOneHash) in self.distances:
                return self.distances[(sequenceTwoHash, sequenceOneHash)]

        sequenceOneArray: ndarray = self._getSequence(sequenceOne)
        sequenceTwoArray: ndarray = self._getSequence(sequenceTwo)

        result = self.distanceMeasure.calculateDistance(sequenceOneArray, sequenceTwoArray)
        # Memoize the computed result since it has not been computed before.
        if sequenceOneHash is None:
            sequenceOneHash = hashSequence(sequenceOneArray)
        if sequenceTwoHash is None:
            sequenceTwoHash = hashSequence(sequenceTwoArray)
        self.distances[(sequenceOneHash, sequenceTwoHash)] = result
        self.distances[(sequenceTwoHash, sequenceOneHash)] = result

        return result

    def processSequenceIndefinitely(self, sequenceHash: str) -> None:
        """
            This method processes a sequence indefinitely, which means it is no longer a (candidate) prototype, but
            merely a sequence. As a result, all the stored information related to this sequence needs to be removed
            from the data structures that make up the cluster. This involves removing all pair-wise distances involving
            the sequence and removing the sequence from the data structure storing the sums of distances.

            :param sequenceHash: The hash of the sequence that needs to be processed indefinitely.
            :return: void
        """
        distancesToRemove = list(filter(lambda dictKey: isHashInKey(dictKey, sequenceHash), self.distances.keys()))
        minKey = None
        minDistance = np.inf
        for key in distancesToRemove:
            hashOne, hashTwo = key
            if (hashOne == sequenceHash or hashTwo == sequenceHash) and \
                    (hashOne in self.prototypes.prototypes or hashTwo in self.prototypes.prototypes):
                distance = self.distances[key]
                if distance < minDistance:
                    minDistance = distance
                    minKey = key
        if minKey is not None:
            hashOne, hashTwo = minKey
            if hashOne != sequenceHash:
                self.prototypeFrequencies.closestPrototypeObserved(hashOne, 1)
            else:
                self.prototypeFrequencies.closestPrototypeObserved(hashTwo, 1)

        for key in distancesToRemove:
            del self.distances[key]

        if (sequenceHash, True) in self.sumsOfDistances:
            del self.sumsOfDistances[(sequenceHash, True)]

        if (sequenceHash, False) in self.sumsOfDistances:
            del self.sumsOfDistances[(sequenceHash, False)]

    def representativenessOfSequence(self, sequence: Tuple[Optional[str], Optional[ndarray]]) -> float:
        """
            This method calculates the representativeness of a sequence relative to the prototypes of the cluster.

            :param sequence: The sequence for which the representativeness should be calculated.
            :return: A float value between 0 and 1 representing the representativeness of the sequence relative to
            the prototypes of the cluster.
        """
        sumOfDistances = self.sumOfDistancesOf(sequence, False)
        result = self.averageSumOfDistances / (2 * sumOfDistances)
        return result

    def sumOfDistancesOf(self, sequence: Tuple[Optional[str], Optional[ndarray]],
                         representative: bool) -> float:
        """
            This method computes the sum of distances between some sequence and either the representative prototypes
            or all prototypes.

            :param sequence: The sequence for which the sum of distances to either the representative prototypes
            or all prototypes needs to be computed.
            :param representative: A boolean value indicating whether or not the distance to the representative
            prototypes should be computed. If this value is false, the distance to all prototypes is computed instead.
            :return: The computed sum of distances. This sum of distances is also memoized such that it can be re-used
            at a later point in time.
        """
        sequenceHash, _ = sequence
        assert sequenceHash is not None
        if representative:
            if (sequenceHash, True) not in self.sumsOfDistances:
                sumOfDistances = self._sumOfDistancesOf(sequence, True, False)
                self.sumsOfDistances[(sequenceHash, True)] = sumOfDistances
            return self.sumsOfDistances[(sequenceHash, True)]

        # This function applies memoization to memoize the result of computations that were carried out previously.
        if (sequenceHash, False) not in self.sumsOfDistances:
            if (sequenceHash, True) in self.sumsOfDistances:
                otherSumOfDistances = self._sumOfDistancesOf(sequence, False, True)
                self.sumsOfDistances[(sequenceHash, False)] = self.sumsOfDistances[(sequenceHash,
                                                                                    True)] + otherSumOfDistances
            else:
                sumOfDistances = self._sumOfDistancesOf(sequence, False, False)
                # TODO: Also store sumsOfDistances[(sequenceHash, True)]?
                self.sumsOfDistances[(sequenceHash, False)] = sumOfDistances
        return self.sumsOfDistances[(sequenceHash, False)]

    def updatePrototypes(self, newPrototypes: Dict[str, ndarray], newOtherPrototypeHashes: Set[str],
                         newRepresentativePrototypeHashes: Set[str], tick: int) -> Set[str]:
        """
            This method updates the prototypes of the cluster.

            :param newPrototypes: The new prototypes as a dictionary where the keys are the hashes of the new prototypes
            and the values are the prototypes itself.
            :param newOtherPrototypeHashes: The hashes of new non-representative prototypes.
            :param newRepresentativePrototypeHashes: The hashes of new representative prototypes.
            :param tick: The tick at which the prototypes are updated.
            :return: The hashes of the prototypes that were removed.
        """
        assert len(self.prototypeFrequencies.frequencies) == self.prototypeFrequencies.numPrototypes
        newPrototypeHashes = set(newPrototypes.keys())
        oldPrototypeHashes = set(self.prototypeFrequencies.frequencies.keys())
        addedPrototypeHashes = newPrototypeHashes.difference(oldPrototypeHashes)
        removedPrototypeHashes = oldPrototypeHashes.difference(newPrototypeHashes)
        assert len(addedPrototypeHashes) == len(removedPrototypeHashes)

        self._computeRequiredDistances(newPrototypes, removedPrototypeHashes)
        self.prototypeFrequencies.updatePrototypes(newPrototypeHashes, addedPrototypeHashes,
                                                   removedPrototypeHashes, self.distances)

        result = self.prototypes.updatePrototypes(newPrototypes, newOtherPrototypeHashes,
                                                  newRepresentativePrototypeHashes, tick)
        if len(result) > 0:
            # TODO: We should discard only the discardable information here.
            self._averageSumOfDistances = None
            self._averageDistance = None
            self._upperBound = None
            self._error = None
            self._averageRepresentativeness = None
            self._averageDistanceFromRepresentativeToNonRepresentative = None
            self._sumsOfDistances = {}
            self._sumsOfRepresentativeDistances = {}

        return result

    # PRIVATE METHODS #

    def _calculateAverageRepresentativeness(self) -> float:
        """
            This method calculates the average representativeness of the representative prototypes of the cluster.

            :return: The average representativeness of the representative prototypes of the cluster.
        """
        result = 0
        for prototypeHash in self.prototypes.representativePrototypeHashes:
            result += self.representativenessOfSequence((prototypeHash, None))
        return result / self.prototypes.numRepresentativePrototypes

    def _calculateAverageSumOfDistances(self, representative: bool) -> float:
        """
            This method calculates the average sum of distances from any of the prototypes to all other prototypes
            in the cluster.

            :param representative: A boolean value indicating whether or not only the representative prototypes or all
            prototypes should be considered.
            :return: The computed average sum of distances for either the representative prototypes or all prototypes.
        """
        result = 0

        if representative:
            prototypeHashes = self.prototypes.representativePrototypeHashes
        else:
            prototypeHashes = self.prototypes.prototypes.keys()

        for prototypeHash in prototypeHashes:
            sumOfDistances = self.sumOfDistancesOf((prototypeHash, None), representative)
            result += sumOfDistances

        if representative:
            result /= self.prototypes.numRepresentativePrototypes
        else:
            result /= self.prototypes.numPrototypes

        return result

    def _calculateAverageSumOfDistancesRepresentativeToNonRepresentative(self) -> float:
        """
            This method calculates the average sum of distances from the representative prototypes to
            the non-representative prototypes.

            :return: A float representing the average sum of distances from the representative prototypes to
            the non-representative prototypes.
        """
        result = 0
        for representativePrototypeHash in self.prototypes.representativePrototypeHashes:
            result += self._sumOfDistancesOf((representativePrototypeHash, None), False, True)
        return result / self.prototypes.numRepresentativePrototypes

    def _computeRequiredDistances(self, newPrototypes: Dict[str, ndarray], removedPrototypeHashes: Set[str]) -> None:
        """
            This method computes the pair-wise distances that are required to update the prototypes of the cluster.
            These distances are memoized in the 'distances' data structure.

            :param newPrototypes: The new prototypes as a dictionary, where the keys are the prototype hashes and the
            values are the prototypes itself.
            :param removedPrototypeHashes: The set of hashes of the prototypes that were removed.
            :return: void
        """
        for newPrototypeHashOne, newPrototypeDataOne in newPrototypes.items():
            for removedPrototypeHash in removedPrototypeHashes:
                if (newPrototypeHashOne, removedPrototypeHash) not in self.distances \
                        and (removedPrototypeHash, newPrototypeHashOne) not in self.distances:
                    distance = self.distanceMeasure.calculateDistance(newPrototypeDataOne,
                                                                      self.prototypes.prototypes[removedPrototypeHash])
                    self.distances[(newPrototypeHashOne, removedPrototypeHash)] = distance
                    self.distances[(removedPrototypeHash, newPrototypeHashOne)] = distance
            for newPrototypeHashTwo, newPrototypeDataTwo in newPrototypes.items():
                if (newPrototypeHashOne, newPrototypeHashTwo) not in self.distances \
                        and (newPrototypeHashTwo, newPrototypeHashOne) not in self.distances:
                    distance = self.distanceMeasure.calculateDistance(newPrototypeDataOne, newPrototypeDataTwo)
                    self.distances[(newPrototypeHashOne, newPrototypeHashTwo)] = distance
                    self.distances[(newPrototypeHashTwo, newPrototypeHashOne)] = distance

    def _getSequence(self, sequence: Tuple[Optional[str], Optional[ndarray]]) -> ndarray:
        """
            This method retrieves the sequence as an array from a tuple containing an optional sequence hash and an
            optional sequence array.

            :param sequence: A tuple containing an optional sequence hash and an
            optional sequence array.
            :return: The sequence as an array.
        """
        sequenceHash, sequenceData = sequence
        if sequenceHash is not None and sequenceHash in self.prototypes.prototypes:
            return self.prototypes.getPrototype(sequenceHash)
        if sequenceData is not None:
            return sequenceData
        raise ValueError("The provided tuple of a sequence hash and an optional sequence cannot be traced to "
                         "a sequence.\nNOTE: This should never happen!")

    def _sumOfDistancesOf(self, sequence: Tuple[Optional[str], Optional[ndarray]],
                          representative: bool, onlyNonRepresentativePrototypes: bool) -> float:
        """
            This method computes the sum of distances between some sequence and either representative prototypes,
            non-representative prototypes or all prototypes.

            :param sequence: The sequence for which the sum of distances should be computed.
            :param representative: A boolean value indicating whether or not the sum of distances should be computed
            for the representative prototypes.
            :param onlyNonRepresentativePrototypes: A boolean value indicating whether or not the sum of distances
            should be computed only for the non-representative prototypes.
            :return: The sum of distances for the sequence and the given set of prototypes to compare to.
        """
        assert not (representative and onlyNonRepresentativePrototypes)
        result = 0
        # In this case, the sum of distances between the given sequence and all representative prototypes in the
        # cluster needs to be computed.
        if representative:
            comparePrototypeHashes = self.prototypes.representativePrototypeHashes
        # In this case, the sum of distances between the given sequence and all other prototypes in the cluster
        # needs to be computed.
        elif onlyNonRepresentativePrototypes:
            comparePrototypeHashes = self.prototypes.otherPrototypeHashes
        else:
            comparePrototypeHashes = self.prototypes.prototypes.keys()

        for comparePrototypeHash in comparePrototypeHashes:
            prototype = (comparePrototypeHash, None)
            result += self.pairwiseDistanceOf(sequence, prototype)

        # The result is a tuple of the sum of distances and an optional float containing the error in the computation.
        return result
