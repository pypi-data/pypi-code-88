"""
    This module contains an implementation of a data structure that stores how often a prototype has been observed to
    be the closest to one of the prototypes of that cluster.
"""

from typing import Dict, Optional, Set, Tuple

import numpy as np


class PrototypeFrequencyStore:

    # STATIC METHODS #

    @staticmethod
    def computeSumOfDistances(prototypeHashes: Set[str], distances: Dict[Tuple[str, str], float]) -> float:
        """
            This method computes the sum of distances between all pairs of prototypes identified by a set of prototype
            hashes given a dictionary of pair-wise distances.

            :param prototypeHashes: The hashes of the prototypes for which
            the sum of pair-wise distances needs to be computed.
            :param distances: The pair-wise distances stored in a dictionary identified by a tuple of prototype hashes
            that identify the two prototypes.
            :return: The sum of distances for the given prototypes and dictionary of distances.
        """
        result = 0
        for prototypeOneHash in prototypeHashes:
            for prototypeTwoHash in prototypeHashes:
                if prototypeOneHash == prototypeTwoHash:
                    continue
                if (prototypeOneHash, prototypeTwoHash) in distances:
                    result += distances[(prototypeOneHash, prototypeTwoHash)]
                elif (prototypeTwoHash, prototypeOneHash) in distances:
                    result += distances[(prototypeTwoHash, prototypeOneHash)]
                else:
                    raise ValueError("[SeqClu] Distance is not present in dictionary.")
        return result

    # PROPERTIES #

    @property
    def frequencies(self) -> Dict[str, Optional[int]]:
        """
            This property stores the amount of times a prototype has been observed as being closest to an incoming
            sequence as a dictionary where the keys are the hashes of the prototypes.

            :return: A dictionary where the keys are the hashes of the prototypes and the values are the amounts of
            times a prototype has been observed as being closest to an incoming sequence.
        """
        return self._frequencies

    @property
    def numPrototypes(self) -> int:
        """
            This property stores the number of prototypes that will be used in the 'SeqClu' algorithm.

            :return: An integer representing the number of prototypes that will be used in the 'SeqClu' algorithm.
        """
        return self._numPrototypes

    @property
    def totalObservations(self) -> int:
        """
            This property stores the total number of observations that was made.

            :return: An integer representing the total number of observations that was made.
        """
        return self._totalObservations

    # CONSTRUCTOR #

    def __init__(self, numPrototypes: int) -> None:
        """
            This method initializes the data structure storing information about the prototype frequencies.

            :param numPrototypes: The number of prototypes that will be used in the 'SeqClu' algorithm.
        """
        self._frequencies = {}
        self._numPrototypes = numPrototypes
        self._totalObservations = 0

    # PUBLIC METHODS #

    def closestPrototypeObserved(self, prototypeHash: str, numVotes: int) -> None:
        """
            This method adds a given amount of votes to the amount of votes that a prototype already has.

            :param prototypeHash: The hash of the prototype that should get votes.
            :param numVotes: The number of votes that the prototype should get.
            :return: void
        """
        assert prototypeHash in self.frequencies
        if self.frequencies[prototypeHash] is None:
            self.frequencies[prototypeHash] = numVotes
        else:
            self.frequencies[prototypeHash] += numVotes
        self._totalObservations += numVotes

    def getWeight(self, prototypeHash: str) -> float:
        """
            This method calculates the weight of a prototype, identified by its hash, and returns this value.

            :param prototypeHash: The hash of the prototype for which the weight needs to be calculated and returned.
            :return: The weight of the prototype identified by its hash.
        """
        assert prototypeHash in self.frequencies
        assert len(self.frequencies) == self.numPrototypes
        if self.frequencies[prototypeHash] is None:
            return 0
        result = self.frequencies[prototypeHash] / self.totalObservations
        return self.frequencies[prototypeHash] / self.totalObservations

    def initializePrototype(self, prototypeHash: str) -> None:
        """
            This method initializes a prototype given its hash.

            :param prototypeHash: The hash of the prototype for which an entry needs to be added to the prototype
            frequencies data structure.
            :return: void
        """
        assert prototypeHash not in self.frequencies
        self.frequencies[prototypeHash] = None

    def updatePrototypes(self, newPrototypeHashes: Set[str], addedPrototypeHashes: Set[str],
                         removedPrototypeHashes: Set[str], distances: Dict[Tuple[str, str], float]) -> None:
        """
            This method updates the prototypes that are stored in the prototype frequencies store given sets of
            updated prototype hashes, newly added prototype hashes and rmeoved prototype hashes, as well as
            a dictionary of pair-wise distances for all pairs of prototypes, regardless of whether or not these
            prototypes are discarded.

            :param newPrototypeHashes: The hashes of the updated prototypes.
            :param addedPrototypeHashes: The hashes of the newly dded prototypes.
            :param removedPrototypeHashes: The hashes of the removed prototypes.
            :param distances: The pair-wise distances for all pairs of prototypes, regardless of whether or not these
            prototypes are discarded.
            :return: void
        """
        print(f"[SeqClu] Updating prototypes...")

        # Initialize new prototypes with empty.
        for prototypeHash in addedPrototypeHashes:
            self.frequencies[prototypeHash] = None

        self._distributeVotes(newPrototypeHashes, removedPrototypeHashes, distances)

        # Sanity check.
        assert len(self.frequencies) == self.numPrototypes

    # PRIVATE METHODS #

    def _distributeVotes(self, newPrototypeHashes: Set[str], removedPrototypeHashes: Set[str],
                         distances: Dict[Tuple[str, str], float]) -> None:
        """
            This method distributes the votes of a discarded prototype to all other prototypes in the store.

            :param newPrototypeHashes: The hashes of the updated prototypes.
            :param removedPrototypeHashes: The hashes of the removed prototypes.
            :param distances: The pair-wise distances for all pairs of prototypes, regardless of whether or not these
            prototypes are discarded.
            :return: void
        """
        # 1. Compute sum of distances from prototype to all other prototypes.
        sumOfDistances = PrototypeFrequencyStore.computeSumOfDistances(newPrototypeHashes, distances)

        for toRemovePrototypeHash in removedPrototypeHashes:
            numVotes = self._removePrototype(toRemovePrototypeHash)
            if numVotes == 0:
                continue
            fractions = np.empty((self.numPrototypes,), dtype=float)
            for i, prototypeHash in enumerate(newPrototypeHashes):
                # 2. Compute fraction of distance to some prototype to removed prototype over the sum of distances.
                # This number is the percentage of the distance that comes from that prototype. The lower, the better.
                if (toRemovePrototypeHash, prototypeHash) in distances:
                    fractions[i] = distances[(toRemovePrototypeHash, prototypeHash)] / sumOfDistances
                elif (prototypeHash, toRemovePrototypeHash) in distances:
                    fractions[i] = distances[(prototypeHash, toRemovePrototypeHash)] / sumOfDistances
                else:
                    raise ValueError("Distance is not in dictionary.")
            # 3. Compute 1 - the number in step 2.
            fractions = 1 - fractions
            # 4. Normalize all values by the sum of these values to make sure
            # its sum sums to 1 and the transferred votes are therefore the same.
            fractions /= np.sum(fractions)
            for i, prototypeHash in enumerate(newPrototypeHashes):
                fraction = fractions[i]
                self.closestPrototypeObserved(prototypeHash, int(fraction * numVotes))

    def _removePrototype(self, toRemoveHash: str) -> int:
        """
            This method removes a prototype from the prototype frequencies store.

            :param toRemoveHash: The hash of the prototype that needs to be removed.
            :return: The amount of votes that the prototype had.
        """
        assert toRemoveHash in self.frequencies
        numVotes = self.frequencies[toRemoveHash]
        del self.frequencies[toRemoveHash]
        if numVotes is None:
            return 0
        self._totalObservations -= numVotes
        return numVotes
