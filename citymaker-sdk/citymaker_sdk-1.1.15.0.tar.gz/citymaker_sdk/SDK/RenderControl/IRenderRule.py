#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"otherwise":{"t":"bool","v":False,
"F":"gs"},"ruleType":{"t":"gviRenderRuleType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRenderRule","F":"g"}}
#Events = {lookUpField:{fn:null}}
class IRenderRule:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._otherwise=args.get("otherwise")
		self._ruleType=args.get("ruleType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def otherwise(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["otherwise"]

	@otherwise.setter
	def otherwise(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "otherwise", val)
		args = {}
		args["otherwise"] = PropsTypeData.get("otherwise")
		args["otherwise"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"otherwise", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"otherwise",JsonData)

	@property
	def ruleType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["ruleType"]

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
