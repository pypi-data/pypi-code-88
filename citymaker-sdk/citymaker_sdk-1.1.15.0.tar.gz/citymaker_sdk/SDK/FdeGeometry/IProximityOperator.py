#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IProximityOperator","F":"g"}}
class IProximityOperator:
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
