from .MultiElementContainer import *
from .IOverlayParent import *
from .Scrollbar import *

class OverlayContainer(MultiElementContainer, IOverlayParent):

    savedBtnStates: list = None
    scroll: Scrollbar = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: IOverlayParent, ):
        pass


    def removeButton(self, btn: AbstractButtonWidget, ) -> None:
        pass

    def openOverlay(self, overlay: self, ) -> None:
        pass

    def getFirstOverlayParent(self, ) -> IOverlayParent:
        pass

    def openOverlay(self, overlay: self, disableButtons: bool, ) -> None:
        pass

    def getChildOverlay(self, ) -> self:
        pass

    def closeOverlay(self, overlay: self, ) -> None:
        pass

    def setFocused(self, focused: Element, ) -> None:
        pass

    def onClick(self, mouseX: float, mouseY: float, button: int, ) -> None:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, ) -> bool:
        pass

    def close(self, ) -> None:
        pass

    def onClose(self, ) -> None:
        pass

    def renderBackground(self, matrices: MatrixStack, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
