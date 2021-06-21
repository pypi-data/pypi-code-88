from .BaseLibrary import *

class FGlobalVars(BaseLibrary, ):

    globalRaw: list = None


    def putInt(self, name: str, i: int, ) -> int:
        pass

    def putString(self, name: str, str: str, ) -> str:
        pass

    def putDouble(self, name: str, d: float, ) -> float:
        pass

    def putBoolean(self, name: str, b: bool, ) -> bool:
        pass

    def putObject(self, name: str, o: Object, ) -> Object:
        pass

    def getType(self, name: str, ) -> str:
        pass

    def getInt(self, name: str, ) -> Integer:
        pass

    def getString(self, name: str, ) -> str:
        pass

    def getDouble(self, name: str, ) -> Double:
        pass

    def getBoolean(self, name: str, ) -> Boolean:
        pass

    def getObject(self, name: str, ) -> Object:
        pass

    def remove(self, key: str, ) -> None:
        pass

    def getRaw(self, ) -> list:
        pass


    pass
