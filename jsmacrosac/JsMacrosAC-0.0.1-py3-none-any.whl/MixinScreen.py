from .MethodWrapper import *
from .Image import *
from .Rect import *
from .TextHelper import *
from .Item import *
from .ButtonWidgetHelper import *
from .ItemStackHelper import *
from .TextFieldWidgetHelper import *
from .IScreen import *
from .RenderElement import *

class MixinScreen(AbstractParentElement, IScreen):

    width: int = None
    height: int = None


    def __init__():
        pass


    def onClose(self, ) -> None:
        pass

    def tick(self, ) -> None:
        pass

    def shouldCloseOnEsc(self, ) -> bool:
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

    def getTextFields(self, ) -> list:
        pass

    def getButtonWidgets(self, ) -> list:
        pass

    def getElements(self, ) -> list:
        pass

    def removeElement(self, e: RenderElement, ) -> IScreen:
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

    def removeText(self, t: str, ) -> IScreen:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ) -> Image:
        pass

    def addImage(self, x: int, y: int, width: int, height: int, zIndex: int, id: str, imageX: int, imageY: int, regionWidth: int, regionHeight: int, textureWidth: int, textureHeight: int, rotation: float, ) -> Image:
        pass

    def removeImage(self, i: Image, ) -> IScreen:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, zIndex: int, ) -> Rect:
        pass

    def removeRect(self, r: Rect, ) -> IScreen:
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

    def removeItem(self, i: Item, ) -> IScreen:
        pass

    def getScreenClassName(self, ) -> str:
        pass

    def getTitleText(self, ) -> str:
        pass

    def addButton(self, x: int, y: int, width: int, height: int, text: str, callback: MethodWrapper, ) -> ButtonWidgetHelper:
        pass

    def addButton(self, x: int, y: int, width: int, height: int, zIndex: int, text: str, callback: MethodWrapper, ) -> ButtonWidgetHelper:
        pass

    def removeButton(self, btn: ButtonWidgetHelper, ) -> IScreen:
        pass

    def addTextInput(self, x: int, y: int, width: int, height: int, message: str, onChange: MethodWrapper, ) -> TextFieldWidgetHelper:
        pass

    def addTextInput(self, x: int, y: int, width: int, height: int, zIndex: int, message: str, onChange: MethodWrapper, ) -> TextFieldWidgetHelper:
        pass

    def removeTextInput(self, inp: TextFieldWidgetHelper, ) -> IScreen:
        pass

    def close(self, ) -> None:
        pass

    def setOnMouseDown(self, onMouseDown: MethodWrapper, ) -> IScreen:
        pass

    def setOnMouseDrag(self, onMouseDrag: MethodWrapper, ) -> IScreen:
        pass

    def setOnMouseUp(self, onMouseUp: MethodWrapper, ) -> IScreen:
        pass

    def setOnScroll(self, onScroll: MethodWrapper, ) -> IScreen:
        pass

    def setOnKeyPressed(self, onKeyPressed: MethodWrapper, ) -> IScreen:
        pass

    def setOnInit(self, onInit: MethodWrapper, ) -> IScreen:
        pass

    def setOnFailInit(self, catchInit: MethodWrapper, ) -> IScreen:
        pass

    def setOnClose(self, onClose: MethodWrapper, ) -> IScreen:
        pass

    def reloadScreen(self, ) -> IScreen:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, info: CallbackInfo, ) -> None:
        pass

    def mouseClicked(self, mouseX: float, mouseY: float, button: int, ) -> bool:
        pass

    def mouseDragged(self, mouseX: float, mouseY: float, button: int, deltaX: float, deltaY: float, ) -> bool:
        pass

    def mouseReleased(self, mouseX: float, mouseY: float, button: int, ) -> bool:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, info: CallbackInfoReturnable, ) -> None:
        pass

    def mouseScrolled(self, mouseX: float, mouseY: float, amount: float, ) -> bool:
        pass

    def removed(self, info: CallbackInfo, ) -> None:
        pass

    def handleCustomClickEvent(self, style: Style, cir: CallbackInfoReturnable, ) -> None:
        pass


    pass
