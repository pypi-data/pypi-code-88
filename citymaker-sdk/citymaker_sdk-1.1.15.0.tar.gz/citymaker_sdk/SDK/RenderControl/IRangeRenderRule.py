#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderRule import IRenderRule
Props={"includeMax":{"t":"bool","v":True,
"F":"gs"},"includeMin":{"t":"bool","v":True,
"F":"gs"},"maxValue":{"t":"double","v":0,
"F":"gs"},"minValue":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRangeRenderRule","F":"g"}}
class IRangeRenderRule(IRenderRule):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._includeMax=args.get("includeMax")
		self._includeMin=args.get("includeMin")
		self._maxValue=args.get("maxValue")
		self._minValue=args.get("minValue")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def includeMax(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["includeMax"]

	@includeMax.setter
	def includeMax(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "includeMax", val)
		args = {}
		args["includeMax"] = PropsTypeData.get("includeMax")
		args["includeMax"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"includeMax", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"includeMax",JsonData)

	@property
	def includeMin(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["includeMin"]

	@includeMin.setter
	def includeMin(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "includeMin", val)
		args = {}
		args["includeMin"] = PropsTypeData.get("includeMin")
		args["includeMin"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"includeMin", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"includeMin",JsonData)

	@property
	def maxValue(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxValue"]

	@maxValue.setter
	def maxValue(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxValue", val)
		args = {}
		args["maxValue"] = PropsTypeData.get("maxValue")
		args["maxValue"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxValue", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxValue",JsonData)

	@property
	def minValue(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minValue"]

	@minValue.setter
	def minValue(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minValue", val)
		args = {}
		args["minValue"] = PropsTypeData.get("minValue")
		args["minValue"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minValue", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minValue",JsonData)

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
