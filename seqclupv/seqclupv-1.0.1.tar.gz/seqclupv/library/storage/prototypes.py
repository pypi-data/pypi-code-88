"""
    This module contains a class called 'PrototypeStore' that is responsible for storing the prototypes of one of the
    clusters that is obtained as a result of executing the 'SeqClu' algorithm.
"""

from typing import Dict, Optional, Set, Tuple

from numpy import ndarray


class PrototypeStore:

    # PROPERTIES #

    @property
    def fullyInitialized(self) -> bool:
        """
            This method is a property that returns a boolean indicating whether or not the data structure has been
            initialized in full.

            :return: A boolean indicating whether or not the data structure has been
            initialized in full.
        """
        return self._fullyInitialized

    @property
    def lastUpdate(self) -> int:
        """
            This method is a property that returns the tick at which the data structure of prototypes was last
            updated.

            :return: The tick at which the data structure of prototypes was last updated.
        """
        assert self._lastUpdate >= 0
        return self._lastUpdate

    @property
    def numRepresentativePrototypes(self) -> int:
        """
            This method is a property that returns the number of representative prototypes of some cluster.

            :return: The number of representative prototypes of the cluster.
        """
        assert not self.fullyInitialized or self.updatingPrototypes or self._numRepresentativePrototypes <= self._numPrototypes
        return self._numRepresentativePrototypes

    @property
    def numOtherPrototypes(self) -> int:
        """
            This method is a property that returns the number of prototypes that are not representative prototypes
            of some cluster.

            :return: The number of prototypes that are not representative prototypes of some cluster.
        """
        return self._numPrototypes - self._numRepresentativePrototypes

    @property
    def numPrototypes(self) -> int:
        """
            This method is a property that returns the total number of prototypes of some cluster.

            :return: The total number of prototypes of some cluster.
        """
        assert not self.fullyInitialized or self.updatingPrototypes or self._numPrototypes >= self._numRepresentativePrototypes
        return self._numPrototypes

    @property
    def otherPrototypeHashes(self) -> Set[str]:
        """
            This method is a property that returns the hashes of the prototypes that are not representative prototypes
            of some cluster.

            :return: The hashes of the prototypes that are not representative prototypes of some cluster.
        """
        assert not self.fullyInitialized or self.updatingPrototypes or len(self._otherPrototypeHashes) == self.numOtherPrototypes
        return self._otherPrototypeHashes

    @property
    def prototypeHistory(self) -> Dict[str, int]:
        """
            This method is a property that returns a dictionary where the key is the hash of some prototype and the
            value is the tick at which the prototype was last updated.

            :return: A dictionary where the key is the hash of some prototype and the value is the tick at which
            the prototype was last updated.
        """
        return self._prototypeHistory

    @property
    def prototypes(self) -> Dict[str, ndarray]:
        """
            This method is a property that returns a dictionary where the key is the hash of some prototype and the
            value is the prototype itself.

            :return: A dictionary where the key is the hash of some prototype and the value is the prototype itself.
        """
        assert not self.fullyInitialized or self.updatingPrototypes or len(self._prototypes) == self._numPrototypes
        return self._prototypes

    @property
    def representativePrototypesInitialized(self) -> bool:
        """
            This property stores a boolean value indicating whether or not the representative prototypes have been
            initialized.

            :return: A boolean value indicating whether or not the representative prototypes have been initialized.
        """
        return self._representativePrototypesInitialized

    @property
    def representativePrototypeHashes(self) -> Set[str]:
        """
            This method is a property that returns the hashes of the prototypes that are representative prototypes
            of some cluster.

            :return: The hashes of the prototypes that are representative prototypes of some cluster.
        """
        assert not self.fullyInitialized or self.updatingPrototypes or len(self._representativePrototypeHashes) == self._numRepresentativePrototypes
        return self._representativePrototypeHashes

    @property
    def updatingPrototypes(self) -> bool:
        """
            This property stores a boolean value indicating whether or not the prototypes are currently being updated.

            :return: A boolean value indicating whether or not the prototypes are currently being updated.
        """
        return self._updatingPrototypes

    # CONSTRUCTOR #

    def __init__(self, numRepresentativePrototypes: int, numPrototypes: int, tick: int) -> None:
        """
            This method initializes the 'PrototypeStore' class with a given number of representative prototypes, number
            of total prototypes and the tick at which the class is initialized.

            :param numRepresentativePrototypes: The number of representative prototypes.
            :param numPrototypes: The total number of prototypes.
            :param tick: The tick at which the class is initialized.
            :return: void
        """
        assert 0 < numRepresentativePrototypes < numPrototypes and numPrototypes > 0 and tick >= -1
        self._fullyInitialized = False
        self._lastUpdate = tick
        self._numRepresentativePrototypes = numRepresentativePrototypes
        self._numPrototypes = numPrototypes
        self._otherPrototypeHashes = set([])
        self._prototypeHistory = {}
        self._prototypes = {}
        self._representativePrototypesInitialized = False
        self._representativePrototypeHashes = set([])
        self._updatingPrototypes = False

    # PUBLIC METHODS #

    def addPrototype(self, prototype: Tuple[Optional[str], Optional[ndarray]], representative: bool,
                     tick: int, toReplaceHash: Optional[str]) -> None:
        """
            This method adds a prototype to the set of prototypes that is stored in this class.

            :param prototype: The sequence that needs to be added as prototype.
            :param representative: A boolean value indicating whether or not the sequence should become a representative
            prototype.
            :param tick: The tick at which the sequence is added to the set of prototypes that is stored in this class.
            :param toReplaceHash: An optional hash of the sequence that needs to be demoted to a regular sequence from
            a prototype.
            :return: void
        """
        prototypeHash, prototypeData = prototype
        # This method should never be called if the cluster prototypes has been initialized in full.
        assert (not self.fullyInitialized and toReplaceHash is None) or \
               (toReplaceHash is not None and toReplaceHash in self.prototypes)

        if toReplaceHash is not None:
            self._removePrototype(toReplaceHash, representative)
        # The private 'addPrototype' method can now be called.
        self._addPrototype(prototypeHash, representative, tick)
        # The private 'addPrototype' method terminated successfully, hence the prototype can be stored.
        self._prototypes[prototypeHash] = prototypeData

        # After a new prototype is added, check if the data structures storing the prototypes contain 'numPrototypes'
        # prototypes. If so, the prototypes is fully initialized and constraints on the prototypes are put in effect.
        if len(self.representativePrototypeHashes) == self.numRepresentativePrototypes:
            print(
                f"[SeqClu] Prototypes have been representative initialized at tick {tick} with {len(self.representativePrototypeHashes)} "
                f"and {len(self.otherPrototypeHashes)}")
            self._representativePrototypesInitialized = True
        if len(self.representativePrototypeHashes) + len(self.otherPrototypeHashes) == self.numPrototypes:
            print(f"[SeqClu] Prototypes have been fully initialized at tick {tick} with {len(self.representativePrototypeHashes)} "
                  f"and {len(self.otherPrototypeHashes)}")
            self._fullyInitialized = True

    def getPrototype(self, prototypeHash: str) -> ndarray:
        """
            This method returns a prototype given the hash of this prototype.

            :param prototypeHash: The hash of the prototype that is requested.
            :return: The requested prototype.
        """
        # A requested prototype identified by its hash must always be available in the 'prototypes' data structure.
        assert prototypeHash in self.prototypes
        return self.prototypes[prototypeHash]

    def lastUpdatePrototype(self, prototypeHash: str) -> Optional[int]:
        """
            This method returns the tick at which some prototype was last updated given the hash of this prototype.

            :param prototypeHash: The hash of the prototype for which information about when it was last updated
            is requested.
            :return: The tick at which the prototype corresponding to the given hash was last updated.
        """
        # Since the data structure will only keep track of current prototypes and this method is only intended for use
        # with prototypes, the constraint that the provided hash of the prototype needs to be contained in the data
        # structure that stores the ticks at which prototypes were updated is added.
        assert prototypeHash in self.prototypeHistory
        return self.prototypeHistory[prototypeHash]

    def updatePrototypes(self, newPrototypes: Dict[str, ndarray], newOtherPrototypeHashes: Set[str],
                         newRepresentativePrototypeHashes: Set[str], tick: int) -> Set[str]:
        """
            This method updates the prototypes stored in the prototype store.

            :param newPrototypes: The new prototypes as a dictionary where the keys are the hashes of the new prototypes
            and the values are the prototypes itself.
            :param newOtherPrototypeHashes: The hashes of new non-representative prototypes.
            :param newRepresentativePrototypeHashes: The hashes of new representative prototypes.
            :param tick: The tick at which the prototypes are updated.
            :return: The hashes of the prototypes that were removed.
        """
        assert len(newPrototypes) == self.numPrototypes
        assert len(newOtherPrototypeHashes) == self.numOtherPrototypes
        assert len(newRepresentativePrototypeHashes) == self.numRepresentativePrototypes
        assert set(newPrototypes.keys()) == newOtherPrototypeHashes.union(newRepresentativePrototypeHashes)
        assert newOtherPrototypeHashes.intersection(newRepresentativePrototypeHashes) == set([])

        self._updatingPrototypes = True
        removedPrototypeHashes: Set[str] = set([])

        for prototypeHash in self.prototypes.keys():
            if prototypeHash not in newPrototypes:
                removedPrototypeHashes.add(prototypeHash)
                if prototypeHash in self.representativePrototypeHashes:
                    self._removePrototype(prototypeHash, True)
                else:
                    self._removePrototype(prototypeHash, False)

        for prototypeHash in self.representativePrototypeHashes:
            if prototypeHash in newOtherPrototypeHashes:
                self.prototypeHistory[prototypeHash] = tick

        for prototypeHash in self.otherPrototypeHashes:
            if prototypeHash in newRepresentativePrototypeHashes:
                self.prototypeHistory[prototypeHash] = tick

        self._prototypes = newPrototypes
        self._representativePrototypeHashes = newRepresentativePrototypeHashes
        self._otherPrototypeHashes = newOtherPrototypeHashes

        for otherPrototypeHash in newOtherPrototypeHashes:
            if otherPrototypeHash not in self.prototypeHistory:
                self.prototypeHistory[otherPrototypeHash] = tick

        for representativePrototypeHash in newRepresentativePrototypeHashes:
            if representativePrototypeHash not in self.prototypeHistory:
                self.prototypeHistory[representativePrototypeHash] = tick

        self._updatingPrototypes = False
        self._lastUpdate = tick
        _ = self.numOtherPrototypes
        _ = self.numRepresentativePrototypes
        _ = self.numPrototypes

        return removedPrototypeHashes

    # PRIVATE METHODS #

    def _addPrototype(self, prototypeHash: str, representative: bool, tick: int) -> None:
        """
            This method adds a prototype to the set of prototypes that is stored in this class.

            :param prototypeHash: The hash of the sequence that needs to be added as prototype.
            :param representative: A boolean value indicating whether or not the sequence should become a representative
            prototype.
            :param tick: The tick at which the sequence is added to the set of prototypes that is stored in this class.
            :return: void
        """
        # The sequence that needs to become a prototype can never already be a prototype.
        assert prototypeHash not in self.representativePrototypeHashes and prototypeHash not in self.otherPrototypeHashes

        if representative:
            assert len(self.representativePrototypeHashes) < self.numRepresentativePrototypes
            self.representativePrototypeHashes.add(prototypeHash)
        else:
            assert len(self.otherPrototypeHashes) < self.numOtherPrototypes
            self.otherPrototypeHashes.add(prototypeHash)
        self.prototypeHistory[prototypeHash] = tick
        self._lastUpdate = tick

    def _removePrototype(self, prototypeHash: str, representative: bool) -> None:
        """
            This method removes a prototype from the set of prototypes that is stored in this class.

            :param prototypeHash: The hash of the sequence that needs to be removed from the set of prototypes.
            :param representative: A boolean value indicating whether or not the sequence is a representative prototype.
            :return: void
        """
        if representative:
            assert prototypeHash in self.representativePrototypeHashes
            self.representativePrototypeHashes.remove(prototypeHash)
        else:
            assert prototypeHash in self.otherPrototypeHashes
            self.otherPrototypeHashes.remove(prototypeHash)
        del self.prototypeHistory[prototypeHash]
