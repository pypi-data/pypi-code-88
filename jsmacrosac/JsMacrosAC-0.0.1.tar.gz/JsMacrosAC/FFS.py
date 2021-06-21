from .BaseLibrary import *
from .FileHandler import *

class FFS(BaseLibrary, ):



    def list(self, path: str, ) -> str:
        pass

    def exists(self, path: str, ) -> bool:
        pass

    def isDir(self, path: str, ) -> bool:
        pass

    def getName(self, path: str, ) -> str:
        pass

    def makeDir(self, path: str, ) -> bool:
        pass

    def move(self, from: str, to: str, ) -> None:
        pass

    def copy(self, from: str, to: str, ) -> None:
        pass

    def unlink(self, path: str, ) -> bool:
        pass

    def combine(self, patha: str, pathb: str, ) -> str:
        pass

    def getDir(self, path: str, ) -> str:
        pass

    def open(self, path: str, ) -> FileHandler:
        pass


    pass
