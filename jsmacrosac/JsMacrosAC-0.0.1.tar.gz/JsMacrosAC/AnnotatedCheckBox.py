from .Button import *

class AnnotatedCheckBox(Button, ):

    value: bool = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, color: int, borderColor: int, hilightColor: int, textColor: int, message: str, initialValue: bool, onPress: Consumer, ):
        pass


    def onPress(self, ) -> None:
        pass

    def setMessage(self, message: str, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
