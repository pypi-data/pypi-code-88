#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IGeometry import IGeometry
Props={"colors":{"t":"nt32 []","v":"",
"F":"gs"},"ids":{"t":"nt32 []","v":"",
"F":"gs"},"measurements":{"t":"IDoubleArray","v":"",
"F":"gs"},"positions":{"t":"IDoubleArray","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPointCloud","F":"g"}}
class IPointCloud(IGeometry):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._colors=args.get("colors")
		self._ids=args.get("ids")
		self._measurements=args.get("measurements")
		self._positions=args.get("positions")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def colors(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["colors"]

	@colors.setter
	def colors(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "colors", val)
		args = {}
		args["colors"] = PropsTypeData.get("colors")
		args["colors"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"colors", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"colors",JsonData)

	@property
	def ids(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["ids"]

	@ids.setter
	def ids(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "ids", val)
		args = {}
		args["ids"] = PropsTypeData.get("ids")
		args["ids"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"ids", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"ids",JsonData)

	@property
	def measurements(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"measurements",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"measurements",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "measurements", res)
		return PropsValueData["measurements"]

	@measurements.setter
	def measurements(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "measurements", val)
		args = {}
		args["measurements"] = PropsTypeData.get("measurements")
		args["measurements"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"measurements", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"measurements",JsonData)

	@property
	def positions(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"positions",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"positions",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "positions", res)
		return PropsValueData["positions"]

	@positions.setter
	def positions(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "positions", val)
		args = {}
		args["positions"] = PropsTypeData.get("positions")
		args["positions"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"positions", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"positions",JsonData)

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
