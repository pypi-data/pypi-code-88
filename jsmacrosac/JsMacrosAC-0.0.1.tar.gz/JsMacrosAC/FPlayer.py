from .Inventory import *
from .MethodWrapper import *
from .ClientPlayerEntityHelper import *
from .Pos3D import *
from .BlockDataHelper import *
from .BaseLibrary import *
from .EntityHelper import *
from .PlayerInput import *

class FPlayer(BaseLibrary, ):



    def openInventory(self, ) -> Inventory:
        pass

    def getPlayer(self, ) -> ClientPlayerEntityHelper:
        pass

    def getGameMode(self, ) -> str:
        pass

    def rayTraceBlock(self, distance: float, fluid: bool, ) -> BlockDataHelper:
        pass

    def rayTraceEntity(self, ) -> EntityHelper:
        pass

    def writeSign(self, l1: str, l2: str, l3: str, l4: str, ) -> bool:
        pass

    def takeScreenshot(self, folder: str, callback: MethodWrapper, ) -> None:
        pass

    def takeScreenshot(self, folder: str, file: str, callback: MethodWrapper, ) -> None:
        pass

    def createPlayerInput(self, ) -> PlayerInput:
        pass

    def createPlayerInput(self, movementForward: float, movementSideways: float, yaw: float, ) -> PlayerInput:
        pass

    def createPlayerInput(self, movementForward: float, yaw: float, jumping: bool, sprinting: bool, ) -> PlayerInput:
        pass

    def createPlayerInput(self, movementForward: float, movementSideways: float, yaw: float, pitch: float, jumping: bool, sneaking: bool, sprinting: bool, ) -> PlayerInput:
        pass

    def createPlayerInputsFromCsv(self, csv: str, ) -> list:
        pass

    def createPlayerInputsFromJson(self, json: str, ) -> PlayerInput:
        pass

    def getCurrentPlayerInput(self, ) -> PlayerInput:
        pass

    def addInput(self, input: PlayerInput, ) -> None:
        pass

    def addInputs(self, inputs: list, ) -> None:
        pass

    def clearInputs(self, ) -> None:
        pass

    def predictInput(self, input: PlayerInput, ) -> Pos3D:
        pass

    def predictInput(self, input: PlayerInput, draw: bool, ) -> Pos3D:
        pass

    def predictInputs(self, inputs: list, ) -> list:
        pass

    def predictInputs(self, inputs: list, draw: bool, ) -> list:
        pass

    def moveForward(self, yaw: float, ) -> None:
        pass

    def moveBackward(self, yaw: float, ) -> None:
        pass


    pass
