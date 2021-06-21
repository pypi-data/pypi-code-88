from .TriggerType import *

class ScriptTrigger(Object, ):

    triggerType: TriggerType = None
    event: str = None
    scriptFile: str = None
    enabled: bool = None


    def __init__(triggerType: TriggerType, event: str, scriptFile: str, enabled: bool, ):
        pass


    def equals(self, macro: self, ) -> bool:
        pass

    def toString(self, ) -> str:
        pass

    def copy(self, m: self, ) -> self:
        pass

    def copy(self, ) -> self:
        pass

    def getTriggerType(self, ) -> TriggerType:
        pass

    def getEvent(self, ) -> str:
        pass

    def getScriptFile(self, ) -> str:
        pass

    def getEnabled(self, ) -> bool:
        pass


    pass
