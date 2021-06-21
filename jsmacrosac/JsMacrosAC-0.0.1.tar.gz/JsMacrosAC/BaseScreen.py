from .IOverlayParent import *
from .OverlayContainer import *

class BaseScreen(Screen, IOverlayParent):



    def trimmed(self, textRenderer: TextRenderer, str: StringVisitable, width: int, ) -> OrderedText:
        pass

    def reload(self, ) -> None:
        pass

    def removed(self, ) -> None:
        pass

    def openOverlay(self, overlay: OverlayContainer, ) -> None:
        pass

    def getFirstOverlayParent(self, ) -> IOverlayParent:
        pass

    def getChildOverlay(self, ) -> OverlayContainer:
        pass

    def openOverlay(self, overlay: OverlayContainer, disableButtons: bool, ) -> None:
        pass

    def closeOverlay(self, overlay: OverlayContainer, ) -> None:
        pass

    def removeButton(self, btn: AbstractButtonWidget, ) -> None:
        pass

    def addButton(self, button: T, ) -> T:
        pass

    def setFocused(self, focused: Element, ) -> None:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, ) -> bool:
        pass

    def mouseScrolled(self, mouseX: float, mouseY: float, amount: float, ) -> bool:
        pass

    def mouseClicked(self, mouseX: float, mouseY: float, button: int, ) -> bool:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def shouldCloseOnEsc(self, ) -> bool:
        pass

    def updateSettings(self, ) -> None:
        pass

    def onClose(self, ) -> None:
        pass

    def openParent(self, ) -> None:
        pass


    pass
