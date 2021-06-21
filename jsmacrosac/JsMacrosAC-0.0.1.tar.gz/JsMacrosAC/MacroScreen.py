from .BaseScreen import *
from .MacroContainer import *
from .ScriptTrigger import *

class MacroScreen(BaseScreen, ):



    def __init__(parent: Screen, ):
        pass


    def mouseScrolled(self, mouseX: float, mouseY: float, amount: float, ) -> bool:
        pass

    def addMacro(self, macro: ScriptTrigger, ) -> None:
        pass

    def setFile(self, macro: MacroContainer, ) -> None:
        pass

    def setEvent(self, macro: MacroContainer, ) -> None:
        pass

    def runFile(self, ) -> None:
        pass

    def confirmRemoveMacro(self, macro: MacroContainer, ) -> None:
        pass

    def removeMacro(self, macro: MacroContainer, ) -> None:
        pass

    def setMacroPos(self, ) -> None:
        pass

    def editFile(self, file: File, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def updateSettings(self, ) -> None:
        pass

    def onClose(self, ) -> None:
        pass


    pass
