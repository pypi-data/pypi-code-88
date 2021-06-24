#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"ruleCount":{"t":"int","v":0,
"F":"g"},"symbol":{"t":"IGeometrySymbol","v":None,
"F":"gs"},"visibleMask":{"t":"byte","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometryRenderScheme","F":"g"}}
class IGeometryRenderScheme:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._ruleCount=args.get("ruleCount")
		self._symbol=args.get("symbol")
		self._visibleMask=args.get("visibleMask")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addRule(self,arg0):  # 先定义函数 
		args = {
				"rule":{"t": "IRenderRule","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addRule', 0, state)


	def clearRules(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearRules', 0, state)


	def getRule(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRule', 1, state)

	@property
	def ruleCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["ruleCount"]

	@property
	def symbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"symbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"symbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "symbol", res)
		return PropsValueData["symbol"]

	@symbol.setter
	def symbol(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "symbol", val)
		args = {}
		args["symbol"] = PropsTypeData.get("symbol")
		args["symbol"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"symbol", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"symbol",JsonData)

	@property
	def visibleMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["visibleMask"]

	@visibleMask.setter
	def visibleMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "visibleMask", val)
		args = {}
		args["visibleMask"] = PropsTypeData.get("visibleMask")
		args["visibleMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"visibleMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visibleMask",JsonData)

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
