from .AbstractMapSettingContainer import *
from .MultiElementContainer import *

class MapSettingEntry(MultiElementContainer, ):



    def __init__(x: int, y: int, width: int, textRenderer: TextRenderer, parent: AbstractMapSettingContainer, key: str, value: T, ):
        pass


    def init(self, ) -> None:
        pass

    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def setKey(self, newKey: str, ) -> None:
        pass

    def setValue(self, newValue: T, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
