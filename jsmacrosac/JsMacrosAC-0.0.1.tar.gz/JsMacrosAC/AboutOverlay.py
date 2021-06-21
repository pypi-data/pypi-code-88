from .IOverlayParent import *
from .OverlayContainer import *

class AboutOverlay(OverlayContainer, ):



    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: IOverlayParent, ):
        pass


    def init(self, ) -> None:
        pass

    def setMessage(self, message: str, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
