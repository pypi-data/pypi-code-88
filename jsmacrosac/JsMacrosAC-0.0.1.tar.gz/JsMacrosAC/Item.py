from .ItemStackHelper import *
from .RenderElement import *

class Item(Object, RenderElement):

    item: ItemStack = None
    ovText: str = None
    overlay: bool = None
    scale: float = None
    rotation: float = None
    x: int = None
    y: int = None
    zIndex: int = None


    def __init__(x: int, y: int, zIndex: int, id: str, overlay: bool, scale: float, rotation: float, ):
        pass


    def setPos(self, x: int, y: int, ) -> self:
        pass

    def setScale(self, scale: float, ) -> self:
        pass

    def setRotation(self, rotation: float, ) -> self:
        pass

    def setOverlay(self, overlay: bool, ) -> self:
        pass

    def setOverlayText(self, ovText: str, ) -> self:
        pass

    def setItem(self, i: ItemStackHelper, ) -> self:
        pass

    def setItem(self, id: str, count: int, ) -> self:
        pass

    def getItem(self, ) -> ItemStackHelper:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def getZIndex(self, ) -> int:
        pass


    pass
