from .Pos3D import *
from .BaseEvent import *

class EventSignEdit(Object, BaseEvent):

    pos: Pos3D = None
    closeScreen: bool = None
    signText: list = None


    def __init__(signText: list, x: int, y: int, z: int, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
