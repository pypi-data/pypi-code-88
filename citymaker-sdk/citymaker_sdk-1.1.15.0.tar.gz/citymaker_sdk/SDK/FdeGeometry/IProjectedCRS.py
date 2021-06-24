#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ISpatialCRS import ISpatialCRS
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IProjectedCRS","F":"g"}}
class IProjectedCRS(ISpatialCRS):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getGeographicCRS(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getGeographicCRS', 1, state)


	def getLinearUnit(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getLinearUnit', 1, state)


	def getParameter(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getParameter', 1, state)


	def setLinearUnit(self,arg0,arg1):  # 先定义函数 
		args = {
				"unitsName":{"t": "S","v": arg0},
				"toMeter":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setLinearUnit', 1, state)


	def setParameter(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"value":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setParameter', 1, state)


	def setProjection(self,arg0):  # 先定义函数 
		args = {
				"projection":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setProjection', 1, state)

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
