from __future__ import annotations
from typing import List, Tuple
from fractions import Fraction
from .notation import NoteCollection


class Music:
    """Represents notes that are played over time"""

    def __init__(self, measures: List[MusicMeasure]):
        self.measures = measures

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class MusicMeasure:
    def __init__(
        self,
        m_lines: List[MusicLine],
        beats_in_a_measure: int = 4,
        beat_duration: Fraction = 1,
    ):
        self.m_lines = m_lines
        self.beats_in_a_measure = beats_in_a_measure
        self.beat_duration = beat_duration
        self.measure_duration = sum(m_l.line_duration for m_l in m_lines)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class MusicMoment:
    def __init__(self, time: float, notes: NoteCollection, duration: Fraction):
        self.time = time
        self.notes = notes
        self.duration = duration

    def __str__(self):
        return f"Notes: {self.notes}, Held for: {self.duration}, At time: {self.time}"

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class MusicLine:
    """Due to the way we write music notes follow consecutively

    In order to write ideas like this:

    Note 1: ==========================
    Note 2:         ========

    Then one solution is to have two different clefs

    This class represents such a clef

    Note this is required because of the way we notate things sequentially in music
    """

    def __init__(self, m_moments: List[MusicMoment]):
        self.m_moments = m_moments
        self.line_duration = sum(m_m.duration for m_m in self.m_moments)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class StructuredMusic(Music):
    """Represents notes played over time that are related to an underlying structure

    In this case the structure is a set of notes which have a higher probability of being
    played than other notes.

    The structure is a note collection and can be specified using a RIC

    music_data is now allowed to use a special type of syntax on top of the previous method

    """

    pass
