from .MethodWrapper import *
from .StringHashTrie import *
from .AutoCompleteSuggestion import *
from .TextHelper import *
from .BaseEvent import *
from .SelectCursor import *
from .EditorScreen import *
from .TextBuilder import *

class CodeCompileEvent(Object, BaseEvent):

    cursor: SelectCursor = None
    code: str = None
    language: str = None
    screen: EditorScreen = None
    textLines: list = None
    autoCompleteSuggestions: list = None
    rightClickActions: MethodWrapper = None


    def __init__(code: str, language: str, screen: EditorScreen, ):
        pass


    def genPrismNodes(self, ) -> list:
        pass

    def createMap(self, ) -> list:
        pass

    def createTextBuilder(self, ) -> TextBuilder:
        pass

    def createSuggestion(self, startIndex: int, suggestion: str, ) -> AutoCompleteSuggestion:
        pass

    def createSuggestion(self, startIndex: int, suggestion: str, displayText: TextHelper, ) -> AutoCompleteSuggestion:
        pass

    def createPrefixTree(self, ) -> StringHashTrie:
        pass

    def getThemeData(self, ) -> list:
        pass


    pass
