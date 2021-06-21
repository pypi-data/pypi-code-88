from .Vec2D import *
from .Pos3D import *

class Vec3D(Vec2D, ):

    z1: float = None
    z2: float = None


    def __init__(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, ):
        pass


    def getZ1(self, ) -> float:
        pass

    def getZ2(self, ) -> float:
        pass

    def getDeltaZ(self, ) -> float:
        pass

    def getStart(self, ) -> Pos3D:
        pass

    def getEnd(self, ) -> Pos3D:
        pass

    def getMagnitude(self, ) -> float:
        pass

    def add(self, vec: self, ) -> self:
        pass

    def multiply(self, vec: self, ) -> self:
        pass

    def getPitch(self, ) -> float:
        pass

    def getYaw(self, ) -> float:
        pass

    def dotProduct(self, vec: self, ) -> float:
        pass

    def crossProduct(self, vec: self, ) -> self:
        pass

    def reverse(self, ) -> self:
        pass

    def toString(self, ) -> str:
        pass


    pass
