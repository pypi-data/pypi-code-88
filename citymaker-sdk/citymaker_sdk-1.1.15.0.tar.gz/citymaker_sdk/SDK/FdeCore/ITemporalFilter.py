#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.ISpatialFilter import ISpatialFilter
Props={"endDatetime":{"t":"DateTime","v":"",
"F":"gs"},"startDatetime":{"t":"DateTime","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITemporalFilter","F":"g"}}
class ITemporalFilter(ISpatialFilter):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._endDatetime=args.get("endDatetime")
		self._startDatetime=args.get("startDatetime")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def endDatetime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["endDatetime"]

	@endDatetime.setter
	def endDatetime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "endDatetime", val)
		args = {}
		args["endDatetime"] = PropsTypeData.get("endDatetime")
		args["endDatetime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"endDatetime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"endDatetime",JsonData)

	@property
	def startDatetime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["startDatetime"]

	@startDatetime.setter
	def startDatetime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "startDatetime", val)
		args = {}
		args["startDatetime"] = PropsTypeData.get("startDatetime")
		args["startDatetime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"startDatetime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"startDatetime",JsonData)

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
