from .MethodWrapper import *
from .BaseEvent import *

class EventCustom(Object, BaseEvent):

    eventName: str = None


    def __init__(eventName: str, ):
        pass


    def trigger(self, ) -> None:
        pass

    def trigger(self, callback: MethodWrapper, ) -> None:
        pass

    def triggerJoin(self, ) -> None:
        pass

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

    def registerEvent(self, ) -> None:
        pass


    pass
