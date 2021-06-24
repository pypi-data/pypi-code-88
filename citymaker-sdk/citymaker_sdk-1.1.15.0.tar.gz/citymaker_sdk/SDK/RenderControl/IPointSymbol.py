#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IGeometrySymbol import IGeometrySymbol
Props={"alignment":{"t":"gviPivotAlignment","v":0,
"F":"gs"},"color":{"t":"Color","v":"",
"F":"gs"},"occlusionTransparent":{"t":"bool","v":True,
"F":"gs"},"shrinkDistanceRatio":{"t":"double","v":1.0,
"F":"gs"},"size":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPointSymbol","F":"g"}}
class IPointSymbol(IGeometrySymbol):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._alignment=args.get("alignment")
		self._color=args.get("color")
		self._occlusionTransparent=args.get("occlusionTransparent")
		self._shrinkDistanceRatio=args.get("shrinkDistanceRatio")
		self._size=args.get("size")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def alignment(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["alignment"]

	@alignment.setter
	def alignment(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "alignment", val)
		args = {}
		args["alignment"] = PropsTypeData.get("alignment")
		args["alignment"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"alignment", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"alignment",JsonData)

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
	def occlusionTransparent(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["occlusionTransparent"]

	@occlusionTransparent.setter
	def occlusionTransparent(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "occlusionTransparent", val)
		args = {}
		args["occlusionTransparent"] = PropsTypeData.get("occlusionTransparent")
		args["occlusionTransparent"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"occlusionTransparent", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"occlusionTransparent",JsonData)

	@property
	def shrinkDistanceRatio(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["shrinkDistanceRatio"]

	@shrinkDistanceRatio.setter
	def shrinkDistanceRatio(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "shrinkDistanceRatio", val)
		args = {}
		args["shrinkDistanceRatio"] = PropsTypeData.get("shrinkDistanceRatio")
		args["shrinkDistanceRatio"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"shrinkDistanceRatio", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"shrinkDistanceRatio",JsonData)

	@property
	def size(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["size"]

	@size.setter
	def size(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "size", val)
		args = {}
		args["size"] = PropsTypeData.get("size")
		args["size"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"size", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"size",JsonData)

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
