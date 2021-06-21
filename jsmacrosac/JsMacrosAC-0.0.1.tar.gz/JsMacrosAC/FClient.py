from .MethodWrapper import *
from .TickSync import *
from .BaseLibrary import *
from .OptionsHelper import *

class FClient(BaseLibrary, ):

    tickSynchronizer: TickSync = None


    def getMinecraft(self, ) -> MinecraftClient:
        pass

    def runOnMainThread(self, runnable: MethodWrapper, ) -> None:
        pass

    def getGameOptions(self, ) -> OptionsHelper:
        pass

    def mcVersion(self, ) -> str:
        pass

    def getFPS(self, ) -> str:
        pass

    def connect(self, ip: str, ) -> None:
        pass

    def connect(self, ip: str, port: int, ) -> None:
        pass

    def disconnect(self, ) -> None:
        pass

    def disconnect(self, callback: MethodWrapper, ) -> None:
        pass

    def waitTick(self, ) -> None:
        pass

    def waitTick(self, i: int, ) -> None:
        pass


    pass
