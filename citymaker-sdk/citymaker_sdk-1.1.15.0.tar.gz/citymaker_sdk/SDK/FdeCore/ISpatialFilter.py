#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.IQueryFilter import IQueryFilter
Props={"geometry":{"t":"IGeometry","v":None,
"F":"gs"},"spatialRel":{"t":"gviSpatialRel","v":2,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISpatialFilter","F":"g"}}
#Events = {geometryField:{fn:null}}
class ISpatialFilter(IQueryFilter):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._geometry=args.get("geometry")
		self._spatialRel=args.get("spatialRel")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def geometry(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"geometry",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometry",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "geometry", res)
		return PropsValueData["geometry"]

	@geometry.setter
	def geometry(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "geometry", val)
		args = {}
		args["geometry"] = PropsTypeData.get("geometry")
		args["geometry"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"geometry", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometry",JsonData)

	@property
	def spatialRel(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["spatialRel"]

	@spatialRel.setter
	def spatialRel(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "spatialRel", val)
		args = {}
		args["spatialRel"] = PropsTypeData.get("spatialRel")
		args["spatialRel"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"spatialRel", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"spatialRel",JsonData)

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
