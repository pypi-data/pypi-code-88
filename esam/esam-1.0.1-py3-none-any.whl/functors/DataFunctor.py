import logging
import sys, os
from ..Constants import *
from ..UserFunctor import UserFunctor
from ..DataContainer import DataContainer

#A DataFunctor is used for manipulating the contents of a DataContainer
class DataFunctor(UserFunctor):
    def __init__(self, name=INVALID_NAME):
        super().__init__(name)
        
        self.requiredKWArgs.append("data")

    #Make sure we can use the same functor object for multiple invocations
    #Override this if you add anything to your class that needs to be reset between calls.
    def Clear(self):
        self.data = DataContainer()

    #Override of UserFunctor method.
    def PreCall(self, **kwargs):
        self.Clear()
        self.data = kwargs.get("data")
        