from .RenderElement import *

class Rect(Object, RenderElement):

    rotation: float = None
    x1: int = None
    y1: int = None
    x2: int = None
    y2: int = None
    color: int = None
    zIndex: int = None


    def __init__(x1: int, y1: int, x2: int, y2: int, color: int, rotation: float, zIndex: int, ):
        pass


    def setColor(self, color: int, ) -> self:
        pass

    def setColor(self, color: int, alpha: int, ) -> self:
        pass

    def setAlpha(self, alpha: int, ) -> self:
        pass

    def setPos(self, x1: int, y1: int, x2: int, y2: int, ) -> self:
        pass

    def setRotation(self, rotation: float, ) -> self:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def getZIndex(self, ) -> int:
        pass


    pass
