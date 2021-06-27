import logging
import sys, os
from ..Constants import *
from .DataFunctor import DataFunctor

#A IOFormatFunctor is used for reading or writing structured data to / from a file.
#If you inherit from this, you must still override the abstract method UserFunction, from UserFunctor.
class IOFormatFunctor(DataFunctor):
    def __init__(self, name=INVALID_NAME):
        super().__init__(name)

        self.requiredKWArgs.append("file")

    #See DataFunctor.Clear() for more details.
    def Clear(self):
        super().Clear()
        self.file = None

    #Override of UserFunctor method.
    def PostCall(self, **kwargs):
        self.file.close()
