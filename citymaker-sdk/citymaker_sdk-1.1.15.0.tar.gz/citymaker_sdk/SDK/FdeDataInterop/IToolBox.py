#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IToolBox","F":"g"}}
class IToolBox:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def execute(self,arg0,arg1):  # 先定义函数 
		args = {
				"paramsIn":{"t": "IPropertySet","v": arg0},
				"rasterType":{"t": "gviRasterConnectionType","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'execute', 1, state)


	def fDBTilePartition(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"xmlString":{"t": "S","v": arg0},
				"dstFDBPath":{"t": "S","v": arg1},
				"tol":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'fDBTilePartition', 1, state)

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
