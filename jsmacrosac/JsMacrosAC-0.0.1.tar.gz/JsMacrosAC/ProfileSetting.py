from .SettingsOverlay import *
from .AbstractMapSettingContainer import *

class ProfileSetting(AbstractMapSettingContainer, ):



    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: SettingsOverlay, group: str, ):
        pass


    def addField(self, key: str, value: list, ) -> None:
        pass

    def removeField(self, key: str, ) -> None:
        pass

    def changeKey(self, key: str, newKey: str, ) -> None:
        pass


    pass
