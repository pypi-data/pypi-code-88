from .BaseEvent import *
from .BaseWrappedException import *
from .Core import *
from .ContextContainer import *
from .ScriptContext import *
from .ScriptTrigger import *

class BaseLanguage(Object, ):

    extension: str = None


    def __init__(extension: str, runner: Core, ):
        pass


    def trigger(self, macro: ScriptTrigger, event: BaseEvent, then: Runnable, catcher: Consumer, ) -> ContextContainer:
        pass

    def trigger(self, script: str, then: Runnable, catcher: Consumer, ) -> ContextContainer:
        pass

    def retrieveLibs(self, context: ContextContainer, ) -> list:
        pass

    def retrieveOnceLibs(self, ) -> list:
        pass

    def retrievePerExecLibs(self, context: ContextContainer, ) -> list:
        pass

    def wrapException(self, ex: Throwable, ) -> BaseWrappedException:
        pass

    def createContext(self, ) -> ScriptContext:
        pass

    def extension(self, ) -> str:
        pass


    pass
