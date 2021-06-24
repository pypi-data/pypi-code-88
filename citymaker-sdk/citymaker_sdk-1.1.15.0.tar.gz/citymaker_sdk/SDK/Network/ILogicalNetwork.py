#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ILogicalNetwork","F":"g"}}
class ILogicalNetwork:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getEdgeElement(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"featureClassID":{"t": "N","v": arg0},
				"featureID":{"t": "N","v": arg1},
				"subID":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEdgeElement', 1, state)


	def getEdgeElements(self,arg0,arg1):  # 先定义函数 
		args = {
				"featureClassID":{"t": "N","v": arg0},
				"featureID":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEdgeElements', 1, state)


	def getJunctionElement(self,arg0,arg1):  # 先定义函数 
		args = {
				"featureClassID":{"t": "N","v": arg0},
				"featureID":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getJunctionElement', 1, state)

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
