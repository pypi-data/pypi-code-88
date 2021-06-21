from .MethodWrapper import *
from .BaseLibrary import *
from .ContextContainer import *
from .EventCustom import *
from .ConfigManager import *
from .IEventListener import *
from .BaseProfile import *

class FJsMacros(BaseLibrary, ):



    def getProfile(self, ) -> BaseProfile:
        pass

    def getConfig(self, ) -> ConfigManager:
        pass

    def getRunningThreads(self, ) -> list:
        pass

    def getOpenContexts(self, ) -> list:
        pass

    def runScript(self, file: str, ) -> ContextContainer:
        pass

    def runScript(self, file: str, callback: MethodWrapper, ) -> ContextContainer:
        pass

    def runScript(self, language: str, script: str, ) -> ContextContainer:
        pass

    def runScript(self, language: str, script: str, callback: MethodWrapper, ) -> ContextContainer:
        pass

    def open(self, path: str, ) -> None:
        pass

    def on(self, event: str, callback: MethodWrapper, ) -> IEventListener:
        pass

    def once(self, event: str, callback: MethodWrapper, ) -> IEventListener:
        pass

    def off(self, listener: IEventListener, ) -> bool:
        pass

    def off(self, event: str, listener: IEventListener, ) -> bool:
        pass

    def listeners(self, event: str, ) -> list:
        pass

    def createCustomEvent(self, eventName: str, ) -> EventCustom:
        pass


    pass
