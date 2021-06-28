"""Different notations for specifying notes to be played"""

from __future__ import annotations
from .tools import I, ranged_modulus_operator
from typing import Set, Dict
from .musical_system import RBMS_Approximation
from .constants import JUST_INTONATION_RATIOS, JAZZ_INTERVAL_COLLECTIONS


class NoteCollection:
    """A collection of notes from a musical system

    :param notes: The notes in this note collection
    :type notes: List[int]

    :param duration: How long this note collection is held for
    :type duration: List[int]

    :param musical_system: The underlying musical system
    :type musical_system: RBMS_Approximation
    """

    def __init__(
        self,
        notes: set,
        duration=0,
        musical_system=RBMS_Approximation(
            440, JUST_INTONATION_RATIOS, 2, 2 ** (1 / 12), 12
        ),
    ):
        self.notes = notes
        self.duration = duration
        self.musical_system = musical_system

    def __eq__(self, other_NC):
        """True if they contain the same notes"""
        return self.notes == other_NC.notes

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        """Human readable representation of a note collection"""
        return str(self.notes)

    def generate_wave_function(self):
        """Generates the wave function determined by the current musical system"""
        raise NotImplementedError

    def compute_diatonic_distance(self, other_NC: NoteCollection) -> float:
        """Return how many notes the two note collections differ by dividided by the number of notes it has"""
        raise NotImplementedError


class RootedIntervalCollection(NoteCollection):
    """A note collection instantiated in a special way

    A rooted interval collection is a way to define a
    set of notes of a musical system.

    It does so specifying a note (denoted by root) from the system and
    a set of intervals measured with respect to the root.

    :param root: The root tone
    :type root: int

    :param intervals: The intervals above the root
    :type intervals: Set[int]

    """

    def __init__(
        self,
        root: int,
        interval_collection: Set[int],
        duration=0,
        musical_system=RBMS_Approximation(
            440, JUST_INTONATION_RATIOS, 2, 2 ** (1 / 12), 12
        ),
    ):
        """
        durations is measured in seconds, it is by default set to 0 seconds to represent no duration
        """
        self.root = root
        self.interval_collection = interval_collection
        super().__init__(self.generate_notes(), duration, musical_system)

    def __str__(self):
        """Human readable representation of a RIC"""
        return str(self.root) + " | " + str(self.interval_collection)

    def generate_notes(self) -> Set[int]:
        """Generate the notes that are defined by taking the root note and adding
        the notes in the interval collection

        :param :py:attr:`~root`: The root tone

        :param intervals: The intervals above the root
        :type intervals: Set[int]

        :return: A list of notes
        :rtype: Set[int]

        :Example:

        >>> ric = RootedIntervalCollection(5, {0, 4, 7, 11})
        >>> ric.generate_notes()
        {5, 9, 0, 11}

        """
        return {self.root + x for x in self.interval_collection}

    def compute_intervallic_complexity(self) -> float:
        """Computes the intervallic complexity of this rooted interval collection

        The intervallic complexity of a rooted interval collection is computed
        by considering all the possible intervals in the interval collection,
        assigning a complexity cost (derived from the ratios that the system approximates)
        and then summing all of the complexity costs.

        For example, if we consider the interval collection {0, 4, 7, 11}, we clearly
        have the intervals 0, 4, 7, 11, but additionally between 4 and 7, there is an interval of 3.
        and between 4 and 11 there is another interval of 7.

        :return: The intervallic complexity
        :rtype: float
        """
        interval_to_occurence = self.generate_interval_to_occurence()
        intervallic_complexity = 0
        for interval, occurence in interval_to_occurence.items():
            # ratio = self.musical_system.interval_to_ratio[interval]
            # ratio = self.musical_system.interval_to_ratio[interval]
            # ratio_complexity = self.musical_system.ratios_to_complexity[ratio] * occurence
            interval_complexity = (
                self.musical_system.interval_to_complexity[interval] * occurence
            )
            intervallic_complexity += interval_complexity
        return intervallic_complexity

    def generate_interval_to_occurence(self) -> Dict[int, int]:
        """Generate a dictionary that maps all possible intervals in this interval collection to the number of times it appears

        :return: A dictionary mapping intervals to occurence
        :rtype: Dict[int, int]
        """
        num_intervals = len(self.interval_collection)
        fixed_order_interval_collection = sorted(list(self.interval_collection))
        interval_to_occurence = {}
        for i in range(num_intervals):
            for j in range(i, num_intervals):
                if i < j:
                    interval_a = fixed_order_interval_collection[i]
                    interval_b = fixed_order_interval_collection[j]
                    interval_between = I(interval_a, interval_b)
                    fundamental_interval_between = ranged_modulus_operator(
                        interval_between, self.musical_system.num_notes
                    )
                    if interval_between not in interval_to_occurence:
                        interval_to_occurence[fundamental_interval_between] = 1
                    else:
                        interval_to_occurence[fundamental_interval_between] += 1
        return interval_to_occurence

    def get_fundamental_representation(self) -> RootedIntervalCollection:
        """Generate the fundamental representation of this interval collection

        The fundamental representation a rooted interval collection where the interval
        are within the range 0 ... num_notes - 1 where num_notes is defined by the
        musical system we are dealing with.

        In 12 tone equal temperament, num_notes is equal to 12.

        For example, if we have a rooted interval collection 13 | -3 1 2 24, then the
        fundamental representation would be 1 | 0 1 2 9

        :return: The funamental representation of this interavl collection
        :rtype: RootedIntervalCollection
        """
        fundamental_interval = {
            ranged_modulus_operator(i, self.musical_system.num_notes)
            for i in self.interval_collection
        }
        fundamental_root = ranged_modulus_operator(
            self.root, self.musical_system.num_notes
        )
        return RootedIntervalCollection(fundamental_root, fundamental_interval)


class DoubleRootedIntervalCollection(NoteCollection):
    """A rooted interval collection where the note in the RIC is an interval above another note"""

    pass


if __name__ == "__main__":
    C7 = RootedIntervalCollection(0, {0, 4, 7, 11})
    for interval_collection in JAZZ_INTERVAL_COLLECTIONS:
        chord = RootedIntervalCollection(0, interval_collection)
        print(interval_collection)
        # print(chord.musical_system.ratios_to_complexity)
        print(chord.compute_intervallic_complexity())
