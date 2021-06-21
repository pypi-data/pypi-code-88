from .MultiElementContainer import *
from .ScriptTrigger import *
from .MacroScreen import *

class MacroContainer(MultiElementContainer, ):



    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, macro: ScriptTrigger, parent: MacroScreen, ):
        pass


    def getRawMacro(self, ) -> ScriptTrigger:
        pass

    def init(self, ) -> None:
        pass

    def setEventType(self, type: str, ) -> None:
        pass

    def setFile(self, f: File, ) -> None:
        pass

    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def onKey(self, translationKey: str, ) -> bool:
        pass

    def buildKeyName(self, translationKeys: str, ) -> str:
        pass

    def setKey(self, translationKeys: str, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
