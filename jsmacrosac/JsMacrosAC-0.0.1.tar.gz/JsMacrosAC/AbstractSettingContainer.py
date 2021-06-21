from .SettingField import *
from .MultiElementContainer import *
from .Scrollbar import *
from .SettingsOverlay import *

class AbstractSettingContainer(MultiElementContainer, ):

    group: str = None
    scroll: Scrollbar = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, parent: SettingsOverlay, group: str, ):
        pass


    def addSetting(self, setting: SettingField, ) -> None:
        pass


    pass
