from .BaseEvent import *
from .Core import *
from .ContextContainer import *
from .ScriptTrigger import *
from .IEventListener import *

class BaseListener(Object, IEventListener):



    def __init__(trigger: ScriptTrigger, runner: Core, ):
        pass


    def getRawTrigger(self, ) -> ScriptTrigger:
        pass

    def runScript(self, event: BaseEvent, ) -> ContextContainer:
        pass

    def equals(self, o: Object, ) -> bool:
        pass

    def toString(self, ) -> str:
        pass


    pass
