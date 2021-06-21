from .ColorMapSetting import *
from .MapSettingEntry import *

class ColorEntry(MapSettingEntry, ):



    def __init__(x: int, y: int, width: int, textRenderer: TextRenderer, parent: ColorMapSetting, key: str, value: short, ):
        pass


    def convertColorToString(self, color: short, ) -> str:
        pass

    def convertStringToColor(self, color: str, ) -> short:
        pass

    def convertColorToInt(self, color: short, ) -> int:
        pass

    def init(self, ) -> None:
        pass


    pass
