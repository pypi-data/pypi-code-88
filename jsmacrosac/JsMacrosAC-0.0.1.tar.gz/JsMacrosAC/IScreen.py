from .MethodWrapper import *
from .Rect import *
from .Item import *
from .TextFieldWidgetHelper import *
from .ButtonWidgetHelper import *
from .ItemStackHelper import *

class IScreen():



    def getScreenClassName(self, ) -> str:
        pass

    def getTitleText(self, ) -> str:
        pass

    def getButtonWidgets(self, ) -> list:
        pass

    def getTextFields(self, ) -> list:
        pass

    def addButton(self, x: int, y: int, width: int, height: int, text: str, callback: MethodWrapper, ) -> ButtonWidgetHelper:
        pass

    def addButton(self, x: int, y: int, width: int, height: int, zIndex: int, text: str, callback: MethodWrapper, ) -> ButtonWidgetHelper:
        pass

    def removeButton(self, btn: ButtonWidgetHelper, ) -> self:
        pass

    def addTextInput(self, x: int, y: int, width: int, height: int, message: str, onChange: MethodWrapper, ) -> TextFieldWidgetHelper:
        pass

    def addTextInput(self, x: int, y: int, width: int, height: int, zIndex: int, message: str, onChange: MethodWrapper, ) -> TextFieldWidgetHelper:
        pass

    def removeTextInput(self, inp: TextFieldWidgetHelper, ) -> self:
        pass

    def setOnMouseDown(self, onMouseDown: MethodWrapper, ) -> self:
        pass

    def setOnMouseDrag(self, onMouseDrag: MethodWrapper, ) -> self:
        pass

    def setOnMouseUp(self, onMouseUp: MethodWrapper, ) -> self:
        pass

    def setOnScroll(self, onScroll: MethodWrapper, ) -> self:
        pass

    def setOnKeyPressed(self, onKeyPressed: MethodWrapper, ) -> self:
        pass

    def setOnClose(self, onClose: MethodWrapper, ) -> self:
        pass

    def close(self, ) -> None:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, ) -> Rect:
        pass

    def addRect(self, x1: int, y1: int, x2: int, y2: int, color: int, alpha: int, rotation: float, ) -> Rect:
        pass

    def removeRect(self, r: Rect, ) -> self:
        pass

    def addItem(self, x: int, y: int, id: str, ) -> Item:
        pass

    def addItem(self, x: int, y: int, id: str, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, id: str, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def addItem(self, x: int, y: int, item: ItemStackHelper, ) -> Item:
        pass

    def addItem(self, x: int, y: int, item: ItemStackHelper, overlay: bool, ) -> Item:
        pass

    def addItem(self, x: int, y: int, item: ItemStackHelper, overlay: bool, scale: float, rotation: float, ) -> Item:
        pass

    def removeItem(self, i: Item, ) -> self:
        pass

    def reloadScreen(self, ) -> self:
        pass


    pass
