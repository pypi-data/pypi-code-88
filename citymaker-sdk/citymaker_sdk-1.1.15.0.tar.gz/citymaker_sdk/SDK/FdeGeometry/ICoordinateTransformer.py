#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICoordinateTransformer","F":"g"}}
class ICoordinateTransformer:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def inverseTransformXY(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'inverseTransformXY', 1, state)


	def inverseTransformXYArray(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'inverseTransformXYArray', 1, state)


	def inverseTransformXYZ(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'inverseTransformXYZ', 1, state)


	def inverseTransformXYZArray(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'inverseTransformXYZArray', 1, state)


	def transformXY(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'transformXY', 1, state)


	def transformXYArray(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'transformXYArray', 1, state)


	def transformXYZ(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'transformXYZ', 1, state)


	def transformXYZArray(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'transformXYZArray', 1, state)


	def coordinateTransform(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"sourceWKT":{"t": "S","v": arg1},
				"targetWKT":{"t": "S","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'coordinateTransform', 1, state)

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
