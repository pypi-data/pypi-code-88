from .Core import *
from .BaseEventRegistry import *
from .ScriptTrigger import *

class EventRegistry(BaseEventRegistry, ):



    def __init__(runner: Core, ):
        pass


    def addScriptTrigger(self, rawmacro: ScriptTrigger, ) -> None:
        pass

    def removeScriptTrigger(self, rawmacro: ScriptTrigger, ) -> bool:
        pass

    def getScriptTriggers(self, ) -> list:
        pass


    pass
