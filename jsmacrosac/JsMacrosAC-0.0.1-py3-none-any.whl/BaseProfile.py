from .BaseEvent import *
from .BaseEventRegistry import *
from .Core import *

class BaseProfile(Object, ):

    LOGGER: Logger = None
    joinedThreadStack: list = None
    profileName: str = None


    def __init__(runner: Core, logger: Logger, ):
        pass


    def logError(self, ex: Throwable, ) -> None:
        pass

    def getRegistry(self, ) -> BaseEventRegistry:
        pass

    def loadOrCreateProfile(self, profileName: str, ) -> None:
        pass

    def loadProfile(self, pName: str, ) -> bool:
        pass

    def saveProfile(self, ) -> None:
        pass

    def triggerEvent(self, event: BaseEvent, ) -> None:
        pass

    def triggerEventJoin(self, event: BaseEvent, ) -> None:
        pass

    def triggerEventNoAnything(self, event: BaseEvent, ) -> None:
        pass

    def triggerEventJoinNoAnything(self, event: BaseEvent, ) -> None:
        pass

    def init(self, defaultProfile: str, ) -> None:
        pass

    def getCurrentProfileName(self, ) -> str:
        pass

    def renameCurrentProfile(self, profile: str, ) -> None:
        pass


    pass
