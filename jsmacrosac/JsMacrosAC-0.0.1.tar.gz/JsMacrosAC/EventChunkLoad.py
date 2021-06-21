from .BaseEvent import *

class EventChunkLoad(Object, BaseEvent):

    x: int = None
    z: int = None
    isFull: bool = None


    def __init__(x: int, z: int, isFull: bool, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
