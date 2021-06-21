from .Vec3D import *

class Box(Object, ):

    pos: Vec3D = None
    color: int = None
    fillColor: int = None
    fill: bool = None
    cull: bool = None


    def __init__(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, fillColor: int, fill: bool, cull: bool, ):
        pass


    def setPos(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, ) -> None:
        pass

    def setColor(self, color: int, ) -> None:
        pass

    def setFillColor(self, fillColor: int, ) -> None:
        pass

    def setColor(self, color: int, alpha: int, ) -> None:
        pass

    def setAlpha(self, alpha: int, ) -> None:
        pass

    def setFillColor(self, fillColor: int, alpha: int, ) -> None:
        pass

    def setFillAlpha(self, alpha: int, ) -> None:
        pass

    def setFill(self, fill: bool, ) -> None:
        pass

    def render(self, ) -> None:
        pass


    pass
