from .BaseLanguage import *
from .ContextContainer import *

class LibraryRegistry(Object, ):

    libraries: list = None
    perExec: list = None
    perLanguage: list = None
    perExecLanguage: list = None


    def __init__():
        pass


    def getLibraries(self, language: BaseLanguage, context: ContextContainer, ) -> list:
        pass

    def getOnceLibraries(self, language: BaseLanguage, ) -> list:
        pass

    def getPerExecLibraries(self, language: BaseLanguage, context: ContextContainer, ) -> list:
        pass

    def addLibrary(self, clazz: Class, ) -> None:
        pass


    pass
