from .RenderElement import *

class Image(Object, RenderElement):

    rotation: float = None
    x: int = None
    y: int = None
    width: int = None
    height: int = None
    imageX: int = None
    imageY: int = None
    regionWidth: int = None
    regionHeight: int = None
    textureWidth: int = None
    textureHeight: int = None
    zIndex: int = None


    def __init__(x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ):
        pass


    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def setRotation(self, rotation: float, ) -> self:
        pass

    def setImage(self, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> None:
        pass

    def getImage(self, ) -> str:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def getZIndex(self, ) -> int:
        pass


    pass
