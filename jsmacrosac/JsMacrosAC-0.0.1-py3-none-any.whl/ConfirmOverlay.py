from .IOverlayParent import *
from .OverlayContainer import *

class ConfirmOverlay(OverlayContainer, ):

    hcenter: bool = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, message: str, parent: IOverlayParent, accept: Consumer, ):
        pass


    def setMessage(self, message: str, ) -> None:
        pass

    def init(self, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
