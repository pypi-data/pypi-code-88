from .BaseEvent import *

class EventEXPChange(Object, BaseEvent):

    progress: float = None
    total: int = None
    level: int = None


    def __init__(progress: float, total: int, level: int, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
