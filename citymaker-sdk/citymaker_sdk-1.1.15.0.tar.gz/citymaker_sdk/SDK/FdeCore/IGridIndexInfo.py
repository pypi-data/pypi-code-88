#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.IIndexInfo import IIndexInfo
Props={"l1":{"t":"double","v":0,
"F":"gs"},"l2":{"t":"double","v":0,
"F":"gs"},"l3":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGridIndexInfo","F":"g"}}
#Events = {geoColumnName:{fn:null}}
class IGridIndexInfo(IIndexInfo):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._l1=args.get("l1")
		self._l2=args.get("l2")
		self._l3=args.get("l3")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def l1(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["l1"]

	@l1.setter
	def l1(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "l1", val)
		args = {}
		args["l1"] = PropsTypeData.get("l1")
		args["l1"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"l1", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"l1",JsonData)

	@property
	def l2(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["l2"]

	@l2.setter
	def l2(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "l2", val)
		args = {}
		args["l2"] = PropsTypeData.get("l2")
		args["l2"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"l2", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"l2",JsonData)

	@property
	def l3(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["l3"]

	@l3.setter
	def l3(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "l3", val)
		args = {}
		args["l3"] = PropsTypeData.get("l3")
		args["l3"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"l3", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"l3",JsonData)

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
