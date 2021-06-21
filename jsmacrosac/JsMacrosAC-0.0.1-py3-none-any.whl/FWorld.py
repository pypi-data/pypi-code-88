from .TextHelper import *
from .BlockDataHelper import *
from .BaseLibrary import *
from .ScoreboardsHelper import *
from .BlockPosHelper import *

class FWorld(BaseLibrary, ):

    serverInstantTPS: float = None
    server1MAverageTPS: float = None
    server5MAverageTPS: float = None
    server15MAverageTPS: float = None


    def isWorldLoaded(self, ) -> bool:
        pass

    def getLoadedPlayers(self, ) -> list:
        pass

    def getPlayers(self, ) -> list:
        pass

    def getBlock(self, x: int, y: int, z: int, ) -> BlockDataHelper:
        pass

    def getScoreboards(self, ) -> ScoreboardsHelper:
        pass

    def getEntities(self, ) -> list:
        pass

    def getDimension(self, ) -> str:
        pass

    def getBiome(self, ) -> str:
        pass

    def getTime(self, ) -> long:
        pass

    def getTimeOfDay(self, ) -> long:
        pass

    def getRespawnPos(self, ) -> BlockPosHelper:
        pass

    def getDifficulty(self, ) -> int:
        pass

    def getMoonPhase(self, ) -> int:
        pass

    def getSkyLight(self, x: int, y: int, z: int, ) -> int:
        pass

    def getBlockLight(self, x: int, y: int, z: int, ) -> int:
        pass

    def playSoundFile(self, file: str, volume: float, ) -> Clip:
        pass

    def playSound(self, id: str, ) -> None:
        pass

    def playSound(self, id: str, volume: float, ) -> None:
        pass

    def playSound(self, id: str, volume: float, pitch: float, ) -> None:
        pass

    def playSound(self, id: str, volume: float, pitch: float, x: float, y: float, z: float, ) -> None:
        pass

    def getBossBars(self, ) -> list:
        pass

    def isChunkLoaded(self, chunkX: int, chunkZ: int, ) -> bool:
        pass

    def getCurrentServerAddress(self, ) -> str:
        pass

    def getBiomeAt(self, x: int, z: int, ) -> str:
        pass

    def getServerTPS(self, ) -> str:
        pass

    def getTabListHeader(self, ) -> TextHelper:
        pass

    def getTabListFooter(self, ) -> TextHelper:
        pass

    def getServerInstantTPS(self, ) -> float:
        pass

    def getServer1MAverageTPS(self, ) -> float:
        pass

    def getServer5MAverageTPS(self, ) -> float:
        pass

    def getServer15MAverageTPS(self, ) -> float:
        pass


    pass
