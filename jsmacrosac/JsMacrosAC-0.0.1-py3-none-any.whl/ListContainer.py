from .IOverlayParent import *
from .MultiElementContainer import *

class ListContainer(MultiElementContainer, ):

    onSelect: Consumer = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, list: list, parent: IOverlayParent, onSelect: Consumer, ):
        pass


    def init(self, ) -> None:
        pass

    def addItem(self, name: str, ) -> None:
        pass

    def setSelected(self, index: int, ) -> None:
        pass

    def onScrollbar(self, page: float, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
