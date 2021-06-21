
class Scrollbar(AbstractButtonWidget, ):



    def __init__(x: int, y: int, width: int, height: int, color: int, borderColor: int, hilightColor: int, scrollPages: float, onChange: Consumer, ):
        pass


    def setPos(self, x: int, y: int, width: int, height: int, ) -> self:
        pass

    def setScrollPages(self, scrollPages: float, ) -> None:
        pass

    def scrollToPercent(self, percent: float, ) -> None:
        pass

    def onClick(self, mouseX: float, mouseY: float, ) -> None:
        pass

    def onChange(self, ) -> None:
        pass

    def mouseDragged(self, mouseX: float, mouseY: float, button: int, deltaX: float, deltaY: float, ) -> bool:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass


    pass
