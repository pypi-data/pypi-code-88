from .BaseHelper import *
from .TextHelper import *
from .RenderElement import *

class ButtonWidgetHelper(BaseHelper, RenderElement):

    zIndex: int = None


    def __init__(btn: T, ):
        pass


    def getX(self, ) -> int:
        pass

    def getY(self, ) -> int:
        pass

    def setPos(self, x: int, y: int, ) -> self:
        pass

    def getWidth(self, ) -> int:
        pass

    def setLabel(self, label: str, ) -> self:
        pass

    def setLabel(self, helper: TextHelper, ) -> self:
        pass

    def getLabel(self, ) -> TextHelper:
        pass

    def getActive(self, ) -> bool:
        pass

    def setActive(self, t: bool, ) -> self:
        pass

    def setWidth(self, width: int, ) -> self:
        pass

    def click(self, ) -> self:
        pass

    def click(self, await: bool, ) -> self:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def getZIndex(self, ) -> int:
        pass


    pass
