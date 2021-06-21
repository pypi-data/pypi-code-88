from .MethodWrapper import *
from .BaseScreen import *
from .IScreen import *

class ScriptScreen(BaseScreen, ):



    def __init__(title: str, dirt: bool, ):
        pass


    def setParent(self, parent: IScreen, ) -> None:
        pass

    def setOnRender(self, onRender: MethodWrapper, ) -> None:
        pass

    def render(self, matrices: MatrixStack, mouseX: int, mouseY: int, delta: float, ) -> None:
        pass

    def onClose(self, ) -> None:
        pass


    pass
