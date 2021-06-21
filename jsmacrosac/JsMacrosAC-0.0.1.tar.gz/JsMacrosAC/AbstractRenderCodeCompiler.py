from .EditorScreen import *

class AbstractRenderCodeCompiler(Object, ):



    def __init__(language: str, screen: EditorScreen, ):
        pass


    def recompileRenderedText(self, text: str, ) -> None:
        pass

    def getRightClickOptions(self, index: int, ) -> list:
        pass

    def getRenderedText(self, ) -> str:
        pass

    def getSuggestions(self, ) -> list:
        pass


    pass
