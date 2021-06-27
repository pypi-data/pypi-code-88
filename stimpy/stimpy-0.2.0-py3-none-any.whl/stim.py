from __future__ import annotations

from typing import Type

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
