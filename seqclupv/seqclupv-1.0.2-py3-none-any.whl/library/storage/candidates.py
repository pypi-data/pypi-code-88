"""
    This module contains a class called 'CandidateStore' that stores the candidate prototypes that are used in the
    'SeqClu' algorithm.
"""

from typing import Dict, Optional, Set, Tuple

from numpy import ndarray

from seqclupv.library.interfaces.candidate_store import ICandidateStore


class CandidateStore(ICandidateStore):

    # PROPERTIES #

    @property
    def candidates(self) -> Dict[str, Tuple[ndarray, Set[int]]]:
        """
            This method is a property that returns the stored set of candidateStore. The candidateStore are stored in a
            dictionary where key is the hash of the candidate and the value is a tuple containing the candidate itself
            and a set of cluster identifiers for which this sequence is a candidate prototype.

            :return: A dictionary where key is the hash of the candidate and the value is a tuple containing the
            candidate itself and a set of cluster identifiers for which this sequence is a candidate prototype.
        """
        return self._candidates

    @property
    def candidateHistory(self) -> Dict[str, int]:
        """
            This method is a property that returns a dictionary where the key is the hash of some candidate and the
            value is the tick at which the candidate was added to the buffer.

            :return: A dictionary where the key is the hash of some candidate and the
            value is the tick at which the candidate was added to the buffer.
        """
        return self._candidateHistory

    @property
    def lastUpdate(self) -> int:
        """
            This method is a property that returns the tick at which the buffer of candidateStore was last updated.

            :return: The tick at which the buffer of candidateStore was last updated.
        """
        return self._lastUpdate

    # CONSTRUCTOR #

    def __init__(self, numRepresentativePrototypes: int, numPrototypes: int, tick: int) -> None:
        """
            This method initializes the buffer of candidateStore with a given number of representative prototypes, total
            number of prototypes, the maximum size of the buffer of candidateStore and the tick at which the buffer is
            initialized.

            :param numRepresentativePrototypes: The number of representative prototypes.
            :param numPrototypes: The total number of prototypes.
            :param tick: The tick at which the buffer of candidateStore is initialized.
        """
        assert 0 < numRepresentativePrototypes < numPrototypes and numPrototypes > 0 and tick >= -1
        self._candidates = {}
        self._candidateHistory = {}
        self._lastUpdate = tick

    # PUBLIC METHODS #

    def addToCandidates(self, candidate: Tuple[Optional[str], Optional[ndarray]],
                        candidateFor: Set[int], tick: int) -> None:
        """
            This method adds an incoming sequence to the buffer of candidateStore.

            :param candidate: The incoming sequence that needs to be added to the buffer of candidateStore.
            :param candidateFor: The identifiers of the clusters that the incoming sequence is a candidate for.
            :param tick: The tick at which the incoming sequence is promoted to a candidate.
            :return: void
        """
        candidateHash, candidateData, = candidate
        assert candidateHash not in self.candidates

        self._candidates[candidateHash] = candidateData, candidateFor
        self._candidateHistory[candidateHash] = tick
        self._lastUpdate = tick

    def getCandidate(self, candidateHash: str) -> Tuple[ndarray, Set[int]]:
        """
            This method returns a candidate given its hash.

            :param candidateHash: The hash of the candidate that is requested.
            :return: A two-tuple containing the candidate itself and the identifiers of the clusters that the sequence
            is a candidate for.
        """
        # A requested candidate identified by its hash must always be available in the 'candidateStore' data structure.
        assert candidateHash in self.candidates
        return self.candidates[candidateHash]

    def lastUpdateCandidate(self, candidateHash: str) -> int:
        """
            This method returns the tick at which a candidate that is stored in the buffer was last updated.

            :param candidateHash: The hash of the candidate for which the information about when the candidate was last
            updated is requested.
            :return: The tick at which a candidate that is stored in the buffer was last updated.
        """
        # Since the data structure will only keep track of current candidateStore and this function is only intended
        # for use with candidateStore, the constraint that the provided hash of the candidateStore needs to be contained
        # in the data structure that stores the ticks at which candidateStore were updated is added.
        assert candidateHash in self.candidateHistory
        return self.candidateHistory[candidateHash]

    def removeFromCandidates(self, candidateHash: str) -> None:
        """
            This method removes a sequence from the set of candidateStore. This occurs when the sequence is fully processed
            and either promoted to a prototype or discarded.

            :param candidateHash: The hash of the candidate.
            :return: void
        """
        assert candidateHash in self.candidates

        del self.candidates[candidateHash]
        del self.candidateHistory[candidateHash]
