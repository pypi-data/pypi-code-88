import logging
import sys, os
from ..Constants import *
from .OutputFormatFunctor import OutputFormatFunctor

class OutputSavedJSON(OutputFormatFunctor):
    def __init__(self, name=INVALID_NAME):
        super().__init__(name)

    #Uses Serializable.ToJSON of self.data to write to self.file
    def WriteFile(self):
        self.file.write(self.data.ToJSON())

