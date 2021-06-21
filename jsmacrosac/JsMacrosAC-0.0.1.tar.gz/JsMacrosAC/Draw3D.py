from .Pos3D import *
from .Box import *
from .Line import *

class Draw3D(Object, ):



    def __init__():
        pass


    def getBoxes(self, ) -> list:
        pass

    def getLines(self, ) -> list:
        pass

    def addBox(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, fillColor: int, fill: bool, ) -> Box:
        pass

    def addBox(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, fillColor: int, fill: bool, cull: bool, ) -> Box:
        pass

    def addBox(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, alpha: int, fillColor: int, fillAlpha: int, fill: bool, ) -> Box:
        pass

    def addBox(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, alpha: int, fillColor: int, fillAlpha: int, fill: bool, cull: bool, ) -> Box:
        pass

    def removeBox(self, b: Box, ) -> self:
        pass

    def addLine(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, ) -> Line:
        pass

    def addLine(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, cull: bool, ) -> Line:
        pass

    def addLine(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, alpha: int, ) -> Line:
        pass

    def addLine(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, color: int, alpha: int, cull: bool, ) -> Line:
        pass

    def removeLine(self, l: Line, ) -> self:
        pass

    def addPoint(self, point: Pos3D, radius: float, color: int, ) -> Box:
        pass

    def addPoint(self, x: float, y: float, z: float, radius: float, color: int, ) -> Box:
        pass

    def addPoint(self, x: float, y: float, z: float, radius: float, color: int, alpha: int, cull: bool, ) -> Box:
        pass

    def render(self, ) -> None:
        pass


    pass
