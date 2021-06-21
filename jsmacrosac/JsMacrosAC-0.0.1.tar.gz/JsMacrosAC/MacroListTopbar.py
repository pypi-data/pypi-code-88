from .MultiElementContainer import *
from .TriggerType import *
from .MacroScreen import *

class MacroListTopbar(MultiElementContainer, ):

    deftype: TriggerType = None


    def __init__(parent: MacroScreen, x: int, y: int, width: int, height: int, textRenderer: TextRenderer, deftype: TriggerType, ):
        pass


    def init(self, ) -> None:
        pass

    def updateType(self, type: TriggerType, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
