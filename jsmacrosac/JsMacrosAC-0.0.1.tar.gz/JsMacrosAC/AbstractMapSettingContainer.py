from .SettingField import *
from .SettingsOverlay import *
from .AbstractSettingContainer import *

class AbstractMapSettingContainer(AbstractSettingContainer, ):

    setting: SettingField = None
    settingName: OrderedText = None
    map: list = None
    topScroll: int = None
    totalHeight: int = None
    defaultValue: Supplier = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: SettingsOverlay, group: str, ):
        pass


    def init(self, ) -> None:
        pass

    def onScrollbar(self, pages: float, ) -> None:
        pass

    def newField(self, key: str, ) -> None:
        pass

    def addField(self, key: str, value: T, ) -> None:
        pass

    def removeField(self, key: str, ) -> None:
        pass

    def changeValue(self, key: str, newValue: T, ) -> None:
        pass

    def changeKey(self, key: str, newKey: str, ) -> None:
        pass

    def addSetting(self, setting: SettingField, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
