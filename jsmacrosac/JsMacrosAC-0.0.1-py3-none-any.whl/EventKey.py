from .BaseEvent import *

class EventKey(Object, BaseEvent):

    action: int = None
    key: str = None
    mods: str = None


    def __init__(key: int, scancode: int, action: int, mods: int, ):
        pass


    def toString(self, ) -> str:
        pass

    def getKeyModifiers(self, mods: int, ) -> str:
        pass

    def getModInt(self, mods: str, ) -> int:
        pass


    pass
