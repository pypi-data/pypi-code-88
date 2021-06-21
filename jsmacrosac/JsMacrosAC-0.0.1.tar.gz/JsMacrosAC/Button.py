
class Button(AbstractPressableButtonWidget, ):

    horizCenter: bool = None
    onPress: Consumer = None
    hovering: bool = None
    forceHover: bool = None


    def __init__(x: int, y: int, width: int, height: int, textRenderer: TextRenderer, color: int, borderColor: int, hilightColor: int, textColor: int, message: str, onPress: Consumer, ):
        pass


    def setPos(self, x: int, y: int, width: int, height: int, ) -> self:
        pass

    def cantRenderAllText(self, ) -> bool:
        pass

    def setMessage(self, message: str, ) -> None:
        pass

    def setColor(self, color: int, ) -> None:
        pass

    def setHilightColor(self, color: int, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def onClick(self, mouseX: float, mouseY: float, ) -> None:
        pass

    def onRelease(self, mouseX: float, mouseY: float, ) -> None:
        pass

    def onPress(self, ) -> None:
        pass


    pass
