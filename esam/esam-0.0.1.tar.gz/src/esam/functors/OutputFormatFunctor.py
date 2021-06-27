import logging
import sys, os
from abc import abstractmethod
from ..Constants import *
from .IOFormatFunctor import IOFormatFunctor

class OutputFormatFunctor(IOFormatFunctor):
    def __init__(self, name=INVALID_NAME):
        super().__init__(name)
        
    #Output Functors will be given expected to write the contents of self.data to self.file.
    #self.file will be overwritten!
    #RETURNS: nothing.
    #This is done to help enforce consistency.
    @abstractmethod
    def WriteFile(self):
        raise NotImplementedError

    def UserFunction(self, **kwargs):
        self.file = open(kwargs.get("file"), "w")
        self.WriteFile()
        
        #the point of no return.


