from .TextHelper import *
from .RenderElement import *

class Text(Object, RenderElement):

    text: self = None
    scale: float = None
    rotation: float = None
    x: int = None
    y: int = None
    color: int = None
    width: int = None
    shadow: bool = None
    zIndex: int = None


    def __init__(text: str, x: int, y: int, color: int, zIndex: int, shadow: bool, scale: float, rotation: float, ):
        pass


    def setScale(self, scale: float, ) -> self:
        pass

    def setRotation(self, rotation: float, ) -> self:
        pass

    def setPos(self, x: int, y: int, ) -> self:
        pass

    def setText(self, text: str, ) -> self:
        pass

    def setText(self, text: TextHelper, ) -> self:
        pass

    def getText(self, ) -> TextHelper:
        pass

    def getWidth(self, ) -> int:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def getZIndex(self, ) -> int:
        pass


    pass
