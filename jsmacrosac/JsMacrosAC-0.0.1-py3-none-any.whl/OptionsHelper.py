from .BaseHelper import *

class OptionsHelper(BaseHelper, ):



    def __init__(options: GameOptions, ):
        pass


    def getCloudMode(self, ) -> int:
        pass

    def setCloudMode(self, mode: int, ) -> self:
        pass

    def getGraphicsMode(self, ) -> int:
        pass

    def setGraphicsMode(self, mode: int, ) -> self:
        pass

    def getResourcePacks(self, ) -> list:
        pass

    def getEnabledResourcePacks(self, ) -> list:
        pass

    def setEnabledResourcePacks(self, enabled: str, ) -> self:
        pass

    def isRightHanded(self, ) -> bool:
        pass

    def setRightHanded(self, val: bool, ) -> None:
        pass

    def getFov(self, ) -> float:
        pass

    def setFov(self, fov: float, ) -> self:
        pass

    def getRenderDistance(self, ) -> int:
        pass

    def setRenderDistance(self, d: int, ) -> None:
        pass

    def getWidth(self, ) -> int:
        pass

    def getHeight(self, ) -> int:
        pass

    def setWidth(self, w: int, ) -> None:
        pass

    def setHeight(self, h: int, ) -> None:
        pass

    def setSize(self, w: int, h: int, ) -> None:
        pass

    def getGamma(self, ) -> float:
        pass

    def setGamma(self, gamma: float, ) -> None:
        pass

    def setVolume(self, vol: float, ) -> None:
        pass

    def setVolume(self, category: str, volume: float, ) -> None:
        pass

    def getVolumes(self, ) -> list:
        pass

    def setGuiScale(self, scale: int, ) -> None:
        pass

    def getGuiScale(self, ) -> int:
        pass

    def getVolume(self, category: str, ) -> float:
        pass


    pass
