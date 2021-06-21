from .MultiElementContainer import *
from .IContainerParent import *

class CheckBoxContainer(MultiElementContainer, ):

    message: str = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, defaultState: bool, message: str, parent: IContainerParent, setState: Consumer, ):
        pass


    def init(self, ) -> None:
        pass

    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
