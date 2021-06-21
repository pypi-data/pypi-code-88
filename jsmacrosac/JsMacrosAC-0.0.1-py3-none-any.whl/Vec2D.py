from .Pos2D import *
from .Vec3D import *

class Vec2D(Object, ):

    x1: float = None
    y1: float = None
    x2: float = None
    y2: float = None


    def __init__(x1: float, y1: float, x2: float, y2: float, ):
        pass


    def getX1(self, ) -> float:
        pass

    def getY1(self, ) -> float:
        pass

    def getX2(self, ) -> float:
        pass

    def getY2(self, ) -> float:
        pass

    def getDeltaX(self, ) -> float:
        pass

    def getDeltaY(self, ) -> float:
        pass

    def getStart(self, ) -> Pos2D:
        pass

    def getEnd(self, ) -> Pos2D:
        pass

    def getMagnitude(self, ) -> float:
        pass

    def add(self, vec: self, ) -> self:
        pass

    def multiply(self, vec: self, ) -> self:
        pass

    def dotProduct(self, vec: self, ) -> float:
        pass

    def reverse(self, ) -> self:
        pass

    def toString(self, ) -> str:
        pass

    def to3D(self, ) -> Vec3D:
        pass


    pass
