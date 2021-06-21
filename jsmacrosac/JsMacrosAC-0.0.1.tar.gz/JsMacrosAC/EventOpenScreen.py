from .BaseEvent import *
from .IScreen import *

class EventOpenScreen(Object, BaseEvent):

    screen: IScreen = None
    screenName: str = None


    def __init__(screen: Screen, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
