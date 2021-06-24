#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ILine import ILine
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"Line","F":"g"}}
class Line(ILine):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def distance2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'distance2D', 1, state)


	def distance3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'distance3D', 1, state)


	def distanceEx2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'distanceEx2D', 1, state)


	def distanceEx3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'distanceEx3D', 1, state)


	def nearestPoint2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'nearestPoint2D', 1, state)


	def nearestPoint3D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'nearestPoint3D', 1, state)


	def contains2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'contains2D', 1, state)


	def crosses2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'crosses2D', 1, state)


	def disjoint2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'disjoint2D', 1, state)


	def equals2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'equals2D', 1, state)


	def intersects2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'intersects2D', 1, state)


	def overlaps2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'overlaps2D', 1, state)


	def touches2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'touches2D', 1, state)


	def within2D(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IGeometry","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'within2D', 1, state)


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
