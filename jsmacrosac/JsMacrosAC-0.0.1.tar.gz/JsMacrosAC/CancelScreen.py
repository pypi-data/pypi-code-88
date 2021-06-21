from .RunningContextContainer import *
from .BaseScreen import *
from .ScriptContext import *

class CancelScreen(BaseScreen, ):



    def __init__(parent: Screen, ):
        pass


    def init(self, ) -> None:
        pass

    def addContainer(self, t: ScriptContext, ) -> None:
        pass

    def removeContainer(self, t: RunningContextContainer, ) -> None:
        pass

    def updatePos(self, ) -> None:
        pass

    def mouseScrolled(self, mouseX: float, mouseY: float, amount: float, ) -> bool:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def removed(self, ) -> None:
        pass

    def onClose(self, ) -> None:
        pass


    pass
