#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IGeometrySymbol import IGeometrySymbol
Props={"boundarySymbol":{"t":"ICurveSymbol","v":None,
"F":"gs"},"color":{"t":"Color","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISolidSymbol","F":"g"}}
class ISolidSymbol(IGeometrySymbol):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._boundarySymbol=args.get("boundarySymbol")
		self._color=args.get("color")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def boundarySymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"boundarySymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"boundarySymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "boundarySymbol", res)
		return PropsValueData["boundarySymbol"]

	@boundarySymbol.setter
	def boundarySymbol(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "boundarySymbol", val)
		args = {}
		args["boundarySymbol"] = PropsTypeData.get("boundarySymbol")
		args["boundarySymbol"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"boundarySymbol", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"boundarySymbol",JsonData)

	@property
	def color(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["color"]

	@color.setter
	def color(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "color", val)
		args = {}
		args["color"] = PropsTypeData.get("color")
		args["color"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"color", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"color",JsonData)

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
