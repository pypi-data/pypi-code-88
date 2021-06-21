from .BaseEvent import *
from .Core import *
from .BaseProfile import *

class Profile(BaseProfile, ):



    def __init__(runner: Core, ):
        pass


    def loadProfile(self, profileName: str, ) -> bool:
        pass

    def triggerEventJoin(self, event: BaseEvent, ) -> None:
        pass

    def triggerEventJoinNoAnything(self, event: BaseEvent, ) -> None:
        pass

    def logError(self, ex: Throwable, ) -> None:
        pass

    def initRegistries(self, ) -> None:
        pass


    pass
