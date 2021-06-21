from .Vec3D import *

class Line(Object, ):

    pos: Vec3D = None
    color: int = None
    cull: bool = None


    def __init__(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, cull: bool, ):
        pass


    def setPos(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, ) -> None:
        pass

    def setColor(self, color: int, ) -> None:
        pass

    def setColor(self, color: int, alpha: int, ) -> None:
        pass

    def setAlpha(self, alpha: int, ) -> None:
        pass

    def render(self, ) -> None:
        pass


    pass
