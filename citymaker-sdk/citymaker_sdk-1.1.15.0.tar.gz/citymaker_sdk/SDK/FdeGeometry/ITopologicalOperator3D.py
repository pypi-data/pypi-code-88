#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITopologicalOperator3D","F":"g"}}
class ITopologicalOperator3D:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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
