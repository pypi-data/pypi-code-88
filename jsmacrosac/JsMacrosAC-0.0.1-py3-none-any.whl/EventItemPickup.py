from .BaseEvent import *
from .ItemStackHelper import *

class EventItemPickup(Object, BaseEvent):

    item: ItemStackHelper = None


    def __init__(item: ItemStack, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
