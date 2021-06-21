from .SettingField import *
from .SettingsOverlay import *
from .AbstractSettingContainer import *

class PrimitiveSettingGroup(AbstractSettingContainer, ):



    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: SettingsOverlay, group: str, ):
        pass


    def init(self, ) -> None:
        pass

    def onScrollbar(self, page: float, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def addSetting(self, setting: SettingField, ) -> None:
        pass


    pass
