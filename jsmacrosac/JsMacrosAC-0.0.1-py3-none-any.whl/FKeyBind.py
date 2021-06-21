from .BaseLibrary import *

class FKeyBind(BaseLibrary, ):

    pressedKeys: list = None


    def getKeyCode(self, keyName: str, ) -> Key:
        pass

    def getKeyBindings(self, ) -> list:
        pass

    def setKeyBind(self, bind: str, key: str, ) -> None:
        pass

    def key(self, keyName: str, keyState: bool, ) -> None:
        pass

    def keyBind(self, keyBind: str, keyState: bool, ) -> None:
        pass

    def getPressedKeys(self, ) -> list:
        pass


    pass
