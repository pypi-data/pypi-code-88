#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderRule import IRenderRule
Props={"compareOperator":{"t":"gviCompareType","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IComparedRenderRule","F":"g"}}
#Events = {compareVariant:{fn:null}}
class IComparedRenderRule(IRenderRule):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._compareOperator=args.get("compareOperator")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def compareOperator(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["compareOperator"]

	@compareOperator.setter
	def compareOperator(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "compareOperator", val)
		args = {}
		args["compareOperator"] = PropsTypeData.get("compareOperator")
		args["compareOperator"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"compareOperator", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"compareOperator",JsonData)

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
