from .MethodWrapper import *
from .PerExecLanguageLibrary import *
from .IFWrapper import *

class FWrapper(PerExecLanguageLibrary, IFWrapper):

    tasks: LinkedBlockingQueue = None


    def methodToJava(self, c: Function, ) -> MethodWrapper:
        pass

    def methodToJavaAsync(self, c: Function, ) -> MethodWrapper:
        pass

    def deferCurrentTask(self, ) -> None:
        pass

    def stop(self, ) -> None:
        pass


    pass
