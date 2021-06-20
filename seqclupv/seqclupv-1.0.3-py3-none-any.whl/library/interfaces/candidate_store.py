"""
    This module contains an interface for the data structure that stores the candidate prototypes for all clusters
    that are maintained as part of the 'SeqClu' algorithm.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional, Set, Tuple

from numpy import ndarray


class ICandidateStore(ABC):

    @property
    @abstractmethod
    def candidates(self) -> Dict[str, Tuple[ndarray, Set[int]]]:
        """
            This property returns the candidate prototypes along with the indices of the clusters that the
            sequences are candidates for that are stored in the candidate store.

            :return: The candidate prototypes stored in the candidate store.
        """
        pass

    @property
    @abstractmethod
    def candidateHistory(self) -> Dict[str, int]:
        """
            This property returns a dictionary where the keys are the candidate hashes and the values are the ticks at
            which the candidate prototypes were last updated.

            :return: A dictionary where the keys are the candidate hashes and the values are the ticks at
            which the candidate prototypes were last updated.
        """
        pass

    @property
    @abstractmethod
    def lastUpdate(self) -> int:
        """
            This property returns the tick at which the candidate store was last updated.

            :return: An integer representing the tick at which the candidate store was last updated.
        """
        pass

    @abstractmethod
    def addToCandidates(self, candidate: ndarray, candidateFor: Set[int], tick: int) -> None:
        """
            This method adds a sequence to the candidate store for a set of clusters at a given tick.

            :param candidate: The sequence that is added as a candidate to the candidate store.
            :param candidateFor: The set of clusters that the sequence is a candidate for.
            :param tick: The tick at which the candidate is added to the candidate store.
            :return: void
        """
        pass

    @abstractmethod
    def getCandidate(self, candidateHash: str) -> Tuple[ndarray, Set[int]]:
        """
            This method returns a candidate prototype given its hash along with the indices of the clusters that the
            sequence is a candidate for.

            :param candidateHash: The hash of the candidate prototypes that needs to be returned along with the indices
            of the clusters that the sequence is a candidate for.
            :return: The candidate prototype given its hash along with the indices of the clusters that the
            sequence is a candidate for.
        """
        pass

    @abstractmethod
    def lastUpdateCandidate(self, candidateHash: str) -> Optional[int]:
        """
            This method returns the tick at which the candidate was last updated.

            :param candidateHash: The hash of the candidate for which the tick at which it was last updated needs to
            be returned.
            :return: An integer representing the tick at which the candidate was last updated.
        """
        pass

    @abstractmethod
    def removeFromCandidates(self, candidateHash: str) -> None:
        """
            This method removes a candidate, identified by its hash, from the candidate store.

            :param candidateHash: The hash of the candidate that needs to be removed from the candidate store.
            :return: void
        """
        pass
