from .Core import *
from .ScriptTrigger import *
from .IEventListener import *

class BaseEventRegistry(Object, ):

    oldEvents: list = None
    events: list = None


    def __init__(runner: Core, ):
        pass


    def clearMacros(self, ) -> None:
        pass

    def addScriptTrigger(self, rawmacro: ScriptTrigger, ) -> None:
        pass

    def addListener(self, event: str, listener: IEventListener, ) -> None:
        pass

    def removeListener(self, event: str, listener: IEventListener, ) -> bool:
        pass

    def removeListener(self, listener: IEventListener, ) -> bool:
        pass

    def removeScriptTrigger(self, rawmacro: ScriptTrigger, ) -> bool:
        pass

    def getListeners(self, ) -> list:
        pass

    def getListeners(self, key: str, ) -> list:
        pass

    def getScriptTriggers(self, ) -> list:
        pass

    def addEvent(self, eventName: str, ) -> None:
        pass

    def addEvent(self, clazz: Class, ) -> None:
        pass


    pass
