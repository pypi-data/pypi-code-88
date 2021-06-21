from .SelectCursor import *
from .AbstractRenderCodeCompiler import *
from .BaseScreen import *
from .History import *

class EditorScreen(BaseScreen, ):

    langs: list = None
    defaultStyle: Style = None
    history: History = None
    cursor: SelectCursor = None
    blockFirst: bool = None
    textRenderTime: long = None
    prevChar: char = None
    language: str = None
    codeCompiler: AbstractRenderCodeCompiler = None


    def __init__(parent: Screen, file: File, ):
        pass


    def getDefaultLanguage(self, ) -> str:
        pass

    def openAndScrollToIndex(self, file: File, startIndex: int, endIndex: int, ) -> None:
        pass

    def openAndScrollToLine(self, file: File, line: int, col: int, endCol: int, ) -> None:
        pass

    def setScroll(self, pages: float, ) -> None:
        pass

    def setLanguage(self, language: str, ) -> None:
        pass

    def init(self, ) -> None:
        pass

    def copyToClipboard(self, ) -> None:
        pass

    def pasteFromClipboard(self, ) -> None:
        pass

    def cutToClipboard(self, ) -> None:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, ) -> bool:
        pass

    def scrollToCursor(self, ) -> None:
        pass

    def save(self, ) -> None:
        pass

    def needSave(self, ) -> bool:
        pass

    def mouseScrolled(self, mouseX: float, mouseY: float, amount: float, ) -> bool:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def openParent(self, ) -> None:
        pass

    def mouseClicked(self, mouseX: float, mouseY: float, btn: int, ) -> bool:
        pass

    def selectWordAtCursor(self, ) -> None:
        pass

    def mouseDragged(self, mouseX: float, mouseY: float, button: int, deltaX: float, deltaY: float, ) -> bool:
        pass

    def updateSettings(self, ) -> None:
        pass

    def charTyped(self, chr: char, keyCode: int, ) -> bool:
        pass


    pass
