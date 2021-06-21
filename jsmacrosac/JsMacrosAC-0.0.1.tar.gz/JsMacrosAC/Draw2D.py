from .MethodWrapper import *
from .Image import *
from .Rect import *
from .TextHelper import *
from .Item import *
from .ItemStackHelper import *
from .RenderElement import *
from .IDraw2D import *

class Draw2D(DrawableHelper, IDraw2D):

    onInit: MethodWrapper = None
    catchInit: MethodWrapper = None


    def __init__():
        pass


    def getWidth(self, ) -> int:
        pass

    def getHeight(self, ) -> int:
        pass

    def getTexts(self, ) -> list:
        pass

    def getRects(self, ) -> list:
        pass

    def getItems(self, ) -> list:
        pass

    def getImages(self, ) -> list:
        pass

    def getElements(self, ) -> list:
        pass

    def removeElement(self, e: RenderElement, ) -> self:
        pass

    def reAddElement(self, e: RenderElement, ) -> RenderElement:
        pass

    def addText(self, text: str, x: int, y: int, color: int, shadow: bool, ) -> str:
        pass

    def addText(self, text: str, x: int, y: int, color: int, zIndex: int, shadow: bool, ) -> str:
        pass

    def addText(self, text: str, x: int, y: int, color: int, shadow: bool, scale: float, rotation: float, ) -> str:
        pass

    def addText(self, text: str, x: int, y: int, color: int, zIndex: int, shadow: bool, scale: float, rotation: float, ) -> str:
        pass

    def addText(self, text: TextHelper, x: int, y: int, color: int, shadow: bool, ) -> str:
        pass

    def addText(self, text: TextHelper, x: int, y: int, color: int, zIndex: int, shadow: bool, ) -> str:
        pass

    def addText(self, text: TextHelper, x: int, y: int, color: int, shadow: bool, scale: float, rotation: float, ) -> str:
        pass

    def addText(self, text: TextHelper, x: int, y: int, color: int, zIndex: int, shadow: bool, scale: float, rotation: float, ) -> str:
        pass

    def removeText(self, t: str, ) -> self:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ) -> Image:
        pass

    def removeImage(self, i: Image, ) -> self:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, zIndex: int, ) -> Rect:
        pass

    def removeRect(self, r: Rect, ) -> self:
        pass

    def addItem(self, x: int, y: int, id: str, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, id: str, ) -> Item:
        pass

    def addItem(self, x: int, y: int, id: str, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, id: str, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, id: str, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, id: str, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def addItem(self, x: int, y: int, Item: ItemStackHelper, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, item: ItemStackHelper, ) -> Item:
        pass

    def addItem(self, x: int, y: int, Item: ItemStackHelper, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, item: ItemStackHelper, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, item: ItemStackHelper, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, item: ItemStackHelper, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def removeItem(self, i: Item, ) -> self:
        pass

    def init(self, ) -> None:
        pass

    def render(self, matrixStack: MatrixStack, ) -> None:
        pass

    def setOnInit(self, onInit: MethodWrapper, ) -> self:
        pass

    def setOnFailInit(self, catchInit: MethodWrapper, ) -> self:
        pass


    pass
