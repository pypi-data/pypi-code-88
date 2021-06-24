#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.FdeGeometry.IPolygon import IPolygon
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"Polygon","F":"g"}}
class Polygon(IPolygon):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def moveModel(self,arg0):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'MoveModel', 1, state)


	def rotateModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'RotateModel', 1, state)


	def scaleModel(self,arg0):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'ScaleModel', 1, state)


	def moveFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0},
				"mode":{"t": "N","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'MoveFeature', 1, state)


	def rotateFeature(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"mode":{"t": "N","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'RotateFeature', 1, state)


	def scaleFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0},
				"mode":{"t": "N","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'ScaleFeature', 1, state)


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
		return CM.AddPrototype(self,args, 'Buffer2D', 1, state)


	def convexHull2D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'ConvexHull2D', 1, state)


	def difference2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Difference2D', 1, state)


	def intersection2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Intersection2D', 1, state)


	def isSimple2D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'IsSimple2D', 1, state)


	def simplify2D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'Simplify2D', 1, state)


	def symmetricDifference2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SymmetricDifference2D', 1, state)


	def union2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Union2D', 1, state)


	def distance2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Distance2D', 1, state)


	def distance3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Distance3D', 1, state)


	def distanceEx2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'DistanceEx2D', 1, state)


	def distanceEx3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'DistanceEx3D', 1, state)


	def nearestPoint2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'NearestPoint2D', 1, state)


	def nearestPoint3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'NearestPoint3D', 1, state)


	def contains2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Contains2D', 1, state)


	def crosses2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Crosses2D', 1, state)


	def disjoint2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Disjoint2D', 1, state)


	def equals2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Equals2D', 1, state)


	def intersects2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Intersects2D', 1, state)


	def overlaps2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Overlaps2D', 1, state)


	def touches2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Touches2D', 1, state)


	def within2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Within2D', 1, state)


	def contains3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Contains3D', 1, state)


	def crosses3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Crosses3D', 1, state)


	def disjoint3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Disjoint3D', 1, state)


	def equals3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Equals3D', 1, state)


	def intersects3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Intersects3D', 1, state)


	def overlaps3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Overlaps3D', 1, state)


	def touches3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Touches3D', 1, state)


	def within3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Within3D', 1, state)


	def buffer3D(self,arg0):  # 先定义函数 
		args = {
				"dis":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Buffer3D', 1, state)


	def convexHull3D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'ConvexHull3D', 1, state)


	def difference3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Difference3D', 1, state)


	def intersection3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Intersection3D', 1, state)


	def isSimple3D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'IsSimple3D', 1, state)


	def simplify3D(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'Simplify3D', 1, state)


	def symmetricDifference3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SymmetricDifference3D', 1, state)


	def union3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Union3D', 1, state)

	def __getattr__(self,name):
		if name in Props:
			attrVal=Props[name]
			if name =="_HashCode":
				return CM.dict_get(attrVal, "v", None)
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("g") > -1:
				if CP.ClassFN.get(t) is not None and "PickResult" not in Props["propertyType"]["v"] and name != "propertyType":
					PropsTypeData = CM.getPropsTypeData(self._HashCode)
					PropsValueData = CM.getPropsValueData(self._HashCode)
					jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),name,None)
					res=socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,jsonData)
					CM.addPropsValue(PropsValueData["_HashCode"], name, res)
					return PropsValueData[name]
				else:
					PropsValueData = CM.getPropsValueData(self._HashCode)
					if name == "fullScreen":
						res=CM.isFull()
					CM.addPropsValue(PropsValueData.get("_HashCode"), name, res)
					return PropsValueData[name]

	def __setattr__(self,name,value):
		if name in Props:
			attrVal=Props[name]
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("s") > -1:
				if name =="_HashCode":
					CM.dict_set(attrVal, "F", value)
					return
				PropsTypeData = CM.getPropsTypeData(self._HashCode)
				PropsValueData = CM.getPropsValueData(self._HashCode)
				CM.addPropsValue(PropsValueData.get("_HashCode"), name, value)
				if name == "fullScreen":
					res=CM.isFull()
					return
				args = {}
				args[name] = PropsTypeData.get(name)
				args[name]["v"] = value
				JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),name, args)
				socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,JsonData)
				super(Polygon, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
