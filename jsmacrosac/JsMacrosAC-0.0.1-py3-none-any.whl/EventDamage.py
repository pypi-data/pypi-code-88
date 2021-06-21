from .BaseEvent import *
from .EntityHelper import *

class EventDamage(Object, BaseEvent):

    attacker: EntityHelper = None
    source: str = None
    health: float = None
    change: float = None


    def __init__(source: DamageSource, health: float, change: float, ):
        pass


    def toString(self, ) -> str:
        pass


    pass
