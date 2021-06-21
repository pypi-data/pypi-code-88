from .IOverlayParent import *
from .ICategoryTreeParent import *
from .OverlayContainer import *

class SettingsOverlay(OverlayContainer, ICategoryTreeParent):



    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: IOverlayParent, ):
        pass


    def init(self, ) -> None:
        pass

    def clearCategory(self, ) -> None:
        pass

    def selectCategory(self, category: str, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, ) -> bool:
        pass

    def onClose(self, ) -> None:
        pass


    pass
