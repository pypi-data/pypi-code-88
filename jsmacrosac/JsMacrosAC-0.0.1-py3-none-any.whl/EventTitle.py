from .TextHelper import *
from .BaseEvent import *

class EventTitle(Object, BaseEvent):

    type: str = None
    message: TextHelper = None


    def __init__(type: str, message: str, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
