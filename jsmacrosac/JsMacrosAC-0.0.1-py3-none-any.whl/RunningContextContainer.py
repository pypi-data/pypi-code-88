from .ScriptContext import *
from .MultiElementContainer import *
from .CancelScreen import *

class RunningContextContainer(MultiElementContainer, ):

    t: WeakReference = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: CancelScreen, t: ScriptContext, ):
        pass


    def init(self, ) -> None:
        pass

    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
