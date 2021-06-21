from .IOverlayParent import *
from .TextInput import *
from .OverlayContainer import *

class TextPrompt(OverlayContainer, ):

    ti: TextInput = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, message: str, defaultText: str, parent: IOverlayParent, accept: Consumer, ):
        pass


    def init(self, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
