from .IOverlayParent import *
from .OverlayContainer import *

class SelectorDropdownOverlay(OverlayContainer, ):



    def __init__(x: int, y: int, width: int, height: int, choices: list, textRenderer: TextRenderer, parent: IOverlayParent, onChoice: Consumer, ):
        pass


    def init(self, ) -> None:
        pass

    def onScroll(self, page: float, ) -> None:
        pass

    def onClick(self, mouseX: float, mouseY: float, button: int, ) -> None:
        pass

    def setSelected(self, sel: int, ) -> None:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, ) -> bool:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
