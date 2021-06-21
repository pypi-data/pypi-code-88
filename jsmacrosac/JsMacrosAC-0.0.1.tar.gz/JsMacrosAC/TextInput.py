from .Button import *

class TextInput(Button, ):

    onChange: Consumer = None
    mask: str = None
    content: str = None
    selStartIndex: int = None
    selEndIndex: int = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, color: int, borderColor: int, hilightColor: int, textColor: int, message: str, onClick: Consumer, onChange: Consumer, ):
        pass


    def setMessage(self, message: str, ) -> None:
        pass

    def updateSelStart(self, startIndex: int, ) -> None:
        pass

    def updateSelEnd(self, endIndex: int, ) -> None:
        pass

    def mouseClicked(self, mouseX: float, mouseY: float, button: int, ) -> bool:
        pass

    def mouseDragged(self, mouseX: float, mouseY: float, button: int, deltaX: float, deltaY: float, ) -> bool:
        pass

    def swapStartEnd(self, ) -> None:
        pass

    def keyPressed(self, keyCode: int, scanCode: int, modifiers: int, ) -> bool:
        pass

    def charTyped(self, chr: char, keyCode: int, ) -> bool:
        pass

    def clicked(self, mouseX: float, mouseY: float, ) -> bool:
        pass

    def setSelected(self, sel: bool, ) -> None:
        pass


    pass
