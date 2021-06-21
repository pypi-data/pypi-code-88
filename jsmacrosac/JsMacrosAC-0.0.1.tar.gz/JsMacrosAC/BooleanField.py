from .SettingField import *
from .AbstractSettingField import *
from .AbstractSettingContainer import *

class BooleanField(AbstractSettingField, ):



    def __init__(x: int, y: int, width: int, textRenderer: TextRenderer, parent: AbstractSettingContainer, field: SettingField, ):
        pass


    def init(self, ) -> None:
        pass

    def setPos(self, x: int, y: int, width: int, height: int, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
