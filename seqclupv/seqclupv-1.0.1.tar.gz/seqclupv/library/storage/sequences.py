"""
    This module contains a class called 'SequenceStore' that stores the ambiguous sequence that have yet to be clustered
     in the 'SeqClu' algorithm.
"""

from typing import Dict

from numpy import ndarray

from seqclupv.library.utilities.hash_sequence import hashSequence


class SequenceStore:

    # PROPERTIES #

    @property
    def sequences(self) -> Dict[str, ndarray]:
        """
            This method is a property that returns the stored set of ambiguous sequenceStore. The sequenceStore are stored in a
            dictionary where key is the hash of the sequence and the value is the sequence itself.

            :return: A dictionary where key is the hash of the sequence and the value is the sequence itself.
        """
        return self._sequences

    @property
    def sequenceHistory(self) -> Dict[str, int]:
        """
            This method is a property that returns a dictionary where the key is the hash of some sequence and the
            value is the tick at which the sequence was added to the buffer.

            :return: A dictionary where the key is the hash of some sequence and the
            value is the tick at which the sequence was added to the buffer.
        """
        return self._sequenceHistory

    @property
    def lastUpdate(self) -> int:
        """
            This method is a property that returns the tick at which the buffer of sequenceStore was last updated.

            :return: The tick at which the buffer of sequenceStore was last updated.
        """
        return self._lastUpdate

    # CONSTRUCTOR #

    def __init__(self, tick: int) -> None:
        """
            This method initializes the buffer of sequenceStore with a given tick at which the buffer is
            initialized.

            :param tick: The tick at which the buffer of sequenceStore is initialized.
        """
        assert tick >= -1
        self._sequences = {}
        self._sequenceHistory = {}
        self._lastUpdate = tick

    # PUBLIC METHODS #

    def addToSequences(self, sequence: ndarray, tick: int) -> None:
        """
            This method adds an incoming sequence to the buffer of sequenceStore.

            :param sequence: The incoming sequence that needs to be added to the buffer of sequenceStore.
            :param tick: The tick at which the incoming sequence is promoted to a sequence.
            :return: void
        """
        sequenceHash = hashSequence(sequence)
        assert sequenceHash not in self.sequences

        self._sequences[sequenceHash] = sequence
        self._sequenceHistory[sequenceHash] = tick
        self._lastUpdate = tick

    def getSequence(self, sequenceHash: str) -> ndarray:
        """
            This method returns a sequence given its hash.

            :param sequenceHash: The hash of the sequence that is requested.
            :return: The requested sequence.
        """
        # A requested sequence identified by its hash must always be available in the 'sequenceStore' data structure.
        assert sequenceHash in self.sequences
        return self.sequences[sequenceHash]

    def lastUpdateSequence(self, sequenceHash: str) -> int:
        """
            This method returns the tick at which a sequence that is stored in the buffer was last updated.

            :param sequenceHash: The hash of the sequence for which the information about when the sequence was last
            updated is requested.
            :return: The tick at which a sequence that is stored in the buffer was last updated.
        """
        # Since the data structure will only keep track of current sequenceStore and this function is only intended for use
        # with sequenceStore, the constraint that the provided hash of the sequenceStore needs to be contained in the data
        # structure that stores the ticks at which sequenceStore were updated is added.
        assert sequenceHash in self.sequenceHistory
        return self.sequenceHistory[sequenceHash]

    def removeFromSequences(self, sequenceHash: str) -> None:
        """
            This method removes a sequence from the set of sequenceStore. This occurs when the sequence is fully processed
            and discarded.

            :param sequenceHash: The hash of the sequence.
            :return: void
        """
        assert sequenceHash in self.sequences

        del self.sequences[sequenceHash]
        del self.sequenceHistory[sequenceHash]
