from __future__ import annotations

from typing import List, Type

from psychopy import visual


class StimulusData:
    """Class for storing stimulus properties.

    :param stimulus_type: Type of visual stimulus.
    :param kwargs: Keyword arguments for the constructor of ``stimulus_type``.
    """

    def __init__(self, stimulus_type: Type[visual.BaseVisualStim], **kwargs):
        self.__stimulus_type = stimulus_type
        self.__kwargs = kwargs

    @property
    def stimulus_type(self):
        return self.__stimulus_type

    @property
    def kwargs(self):
        return self.__kwargs.copy()


class Stimuli:
    """Class for grouping multiple stimuli."""

    def __init__(self):
        self.__stimulus_data: List[StimulusData] = []
        self.__begin: List[float] = []
        self.__dur: List[float] = []

    def __iter__(self):
        return zip(self.__stimulus_data, self.__begin, self.__dur)

    def append(self, stimulus_data: StimulusData, begin: float, dur: float):
        self.__stimulus_data.append(stimulus_data)
        self.__begin.append(begin)
        self.__dur.append(dur)
