from .BaseScreen import *
from .Core import *

class JsMacros(Object, ClientModInitializer):

    MOD_ID: str = None
    LOGGER: Logger = None
    keyBinding: KeyBinding = None
    prevScreen: BaseScreen = None
    core: Core = None


    def __init__():
        pass


    def onInitializeClient(self, ) -> None:
        pass

    def getKeyText(self, translationKey: str, ) -> str:
        pass

    def getScreenName(self, s: Screen, ) -> str:
        pass

    def getLocalizedName(self, keyCode: Key, ) -> str:
        pass

    def getMinecraft(self, ) -> MinecraftClient:
        pass

    def range(self, end: int, ) -> int:
        pass

    def range(self, start: int, end: int, ) -> int:
        pass

    def range(self, start: int, end: int, iter: int, ) -> int:
        pass


    pass
