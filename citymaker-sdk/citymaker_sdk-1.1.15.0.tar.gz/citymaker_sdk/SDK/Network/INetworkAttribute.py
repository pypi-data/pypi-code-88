#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"fieldType":{"t":"gviFieldType","v":0,
"F":"gs"},"isUseByDefault":{"t":"bool","v":False,
"F":"gs"},"usageType":{"t":"gviNetworkAttributeUsageType","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkAttribute","F":"g"}}
#Events = {name:{fn:null}}
class INetworkAttribute:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._fieldType=args.get("fieldType")
		self._isUseByDefault=args.get("isUseByDefault")
		self._usageType=args.get("usageType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getDefaultEvaluator(self,arg0):  # 先定义函数 
		args = {
				"elementType":{"t": "gviNetworkElementType","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getDefaultEvaluator', 1, state)


	def getEvaluator(self,arg0,arg1):  # 先定义函数 
		args = {
				"networkSource":{"t": "INetworkSource","v": arg0},
				"edgeDirection":{"t": "gviEdgeDirection","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEvaluator', 1, state)


	def setDefaultEvaluator(self,arg0,arg1):  # 先定义函数 
		args = {
				"elementType":{"t": "gviNetworkElementType","v": arg0},
				"evaluator":{"t": "INetworkEvaluator","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultEvaluator', 0, state)


	def setEvaluator(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"networkSource":{"t": "INetworkSource","v": arg0},
				"edgeDirection":{"t": "gviEdgeDirection","v": arg1},
				"ne":{"t": "INetworkEvaluator","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setEvaluator', 0, state)

	@property
	def fieldType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldType"]

	@fieldType.setter
	def fieldType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fieldType", val)
		args = {}
		args["fieldType"] = PropsTypeData.get("fieldType")
		args["fieldType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fieldType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fieldType",JsonData)

	@property
	def isUseByDefault(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isUseByDefault"]

	@isUseByDefault.setter
	def isUseByDefault(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isUseByDefault", val)
		args = {}
		args["isUseByDefault"] = PropsTypeData.get("isUseByDefault")
		args["isUseByDefault"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isUseByDefault", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isUseByDefault",JsonData)

	@property
	def usageType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["usageType"]

	@usageType.setter
	def usageType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "usageType", val)
		args = {}
		args["usageType"] = PropsTypeData.get("usageType")
		args["usageType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"usageType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"usageType",JsonData)

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
