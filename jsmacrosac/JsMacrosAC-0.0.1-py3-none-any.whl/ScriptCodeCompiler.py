from .EditorScreen import *
from .AbstractRenderCodeCompiler import *

class ScriptCodeCompiler(AbstractRenderCodeCompiler, ):



    def __init__(language: str, screen: EditorScreen, scriptFile: str, ):
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
