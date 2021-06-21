from .PlayerEntityHelper import *
from .ScoreboardObjectiveHelper import *
from .BaseHelper import *
from .TeamHelper import *

class ScoreboardsHelper(BaseHelper, ):



    def __init__(board: Scoreboard, ):
        pass


    def getObjectiveForTeamColorIndex(self, index: int, ) -> ScoreboardObjectiveHelper:
        pass

    def getObjectiveSlot(self, slot: int, ) -> ScoreboardObjectiveHelper:
        pass

    def getPlayerTeamColorIndex(self, entity: PlayerEntityHelper, ) -> int:
        pass

    def getTeams(self, ) -> list:
        pass

    def getPlayerTeam(self, p: PlayerEntityHelper, ) -> TeamHelper:
        pass

    def getCurrentScoreboard(self, ) -> ScoreboardObjectiveHelper:
        pass

    def toString(self, ) -> str:
        pass


    pass
