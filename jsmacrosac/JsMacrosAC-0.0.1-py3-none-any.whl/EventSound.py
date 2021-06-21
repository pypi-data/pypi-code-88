from .BaseEvent import *
from .Pos3D import *

class EventSound(Object, BaseEvent):

    sound: str = None
    volume: float = None
    pitch: float = None
    position: Pos3D = None


    def __init__(sound: str, volume: float, pitch: float, x: float, y: float, z: float, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
