#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IGeometryCollection import IGeometryCollection
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IMultiPolygon","F":"g"}}
class IMultiPolygon(IGeometryCollection):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addSurface(self,arg0):  # 先定义函数 
		args = {
				"surface":{"t": "ISurface","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addSurface', 1, state)


	def generalize(self,arg0):  # 先定义函数 
		args = {
				"maxAllowOffset":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'generalize', 1, state)


	def getArea(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getArea', 1, state)


	def addPolygon(self,arg0):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addPolygon', 1, state)


	def getPolygon(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygon', 1, state)


	def moveModel(self,arg0):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'moveModel', 1, state)


	def rotateModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'rotateModel', 1, state)


	def scaleModel(self,arg0):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'scaleModel', 1, state)


	def moveFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0},
				"mode":{"t": "Number","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'moveFeature', 1, state)


	def rotateFeature(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"mode":{"t": "Number","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'rotateFeature', 1, state)


	def scaleFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0},
				"mode":{"t": "Number","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'scaleFeature', 1, state)


	def move2D(self,arg0,arg1):  # 先定义函数 
		args = {
				"dX":{"t": "N","v": arg0},
				"dY":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'move2D', 0, state)


	def move3D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"dX":{"t": "N","v": arg0},
				"dY":{"t": "N","v": arg1},
				"dZ":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'move3D', 0, state)


	def rotate2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"centerX":{"t": "N","v": arg0},
				"centerY":{"t": "N","v": arg1},
				"angle":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'rotate2D', 0, state)


	def rotate3D(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"axisX":{"t": "N","v": arg0},
				"axisY":{"t": "N","v": arg1},
				"axisZ":{"t": "N","v": arg2},
				"centerX":{"t": "N","v": arg3},
				"centerY":{"t": "N","v": arg4},
				"centerZ":{"t": "N","v": arg5},
				"angle":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'rotate3D', 0, state)


	def scale2D(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"centerX":{"t": "N","v": arg2},
				"centerY":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'scale2D', 0, state)


	def scale3D(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"scaleZ":{"t": "N","v": arg2},
				"centerX":{"t": "N","v": arg3},
				"centerY":{"t": "N","v": arg4},
				"centerZ":{"t": "N","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'scale3D', 0, state)


	def buffer2D(self,arg0,arg1):  # 先定义函数 
		args = {
				"dis":{"t": "N","v": arg0},
				"style":{"t": "gviBufferStyle","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'buffer2D', 1, state)


	def convexHull2D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'convexHull2D', 1, state)


	def difference2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'difference2D', 1, state)


	def intersection2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'intersection2D', 1, state)


	def isSimple2D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'isSimple2D', 1, state)


	def simplify2D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'simplify2D', 1, state)


	def symmetricDifference2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'symmetricDifference2D', 1, state)


	def union2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'union2D', 1, state)


	def buffer3D(self,arg0):  # 先定义函数 
		args = {
				"dis":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'buffer3D', 1, state)


	def convexHull3D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'convexHull3D', 1, state)


	def difference3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'difference3D', 1, state)


	def intersection3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'intersection3D', 1, state)


	def isSimple3D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'isSimple3D', 1, state)


	def simplify3D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'simplify3D', 1, state)


	def symmetricDifference3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'symmetricDifference3D', 1, state)


	def union3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'union3D', 1, state)

	@property
	def propertyType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["propertyType"]

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
