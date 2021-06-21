from .MethodWrapper import *
from .Image import *
from .Rect import *
from .Item import *
from .TextHelper import *
from .ItemStackHelper import *
from .RenderElement import *

class IDraw2D():



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

    def removeElement(self, e: RenderElement, ) -> T:
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

    def removeText(self, t: str, ) -> T:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ) -> Image:
        pass

    def removeImage(self, i: Image, ) -> T:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, zIndex: int, ) -> Rect:
        pass

    def removeRect(self, r: Rect, ) -> T:
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

    def addItem(self, x: int, y: int, item: ItemStackHelper, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, item: ItemStackHelper, ) -> Item:
        pass

    def addItem(self, x: int, y: int, item: ItemStackHelper, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, item: ItemStackHelper, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, item: ItemStackHelper, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def addItem(self, x: int, y: int, zIndex: int, item: ItemStackHelper, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def removeItem(self, i: Item, ) -> T:
        pass

    def setOnInit(self, onInit: MethodWrapper, ) -> T:
        pass

    def setOnFailInit(self, catchInit: MethodWrapper, ) -> T:
        pass

    def render(self, matrixStack: MatrixStack, ) -> None:
        pass


    pass
