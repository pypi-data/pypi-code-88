#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"symbolType":{"t":"gviGeometrySymbolType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometrySymbol","F":"g"}}
#Events = {script:{fn:null}}
class IGeometrySymbol:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._symbolType=args.get("symbolType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)


	def setResourceDataSet(self,arg0):  # 先定义函数 
		args = {
				"dataSet":{"t": "IFeatureDataSet","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setResourceDataSet', 0, state)

	@property
	def symbolType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["symbolType"]

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
