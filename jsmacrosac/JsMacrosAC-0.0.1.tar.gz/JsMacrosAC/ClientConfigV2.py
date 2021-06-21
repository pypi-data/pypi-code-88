from .MacroSortMethod import *

class ClientConfigV2(Object, ):

    sortMethod: MacroSortMethod = None
    disableKeyWhenScreenOpen: bool = None
    editorTheme: list = None
    editorLinterOverrides: list = None
    editorHistorySize: int = None
    editorSuggestions: bool = None
    editorFont: str = None


    def __init__():
        pass


    def languages(self, ) -> list:
        pass

    def getFonts(self, ) -> list:
        pass

    def getThemeData(self, ) -> list:
        pass

    def getSortComparator(self, ) -> Comparator:
        pass

    def fromV1(self, v1: JsonObject, ) -> None:
        pass


    pass
