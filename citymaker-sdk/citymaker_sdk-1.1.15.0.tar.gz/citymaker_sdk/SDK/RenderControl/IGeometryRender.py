#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"heightOffset":{"t":"double","v":0,
"F":"gs"},"heightStyle":{"t":"gviHeightStyle","v":1,
"F":"gs"},"renderType":{"t":"gviRenderType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometryRender","F":"g"}}
#Events = {renderGroupField:{fn:null}}
class IGeometryRender:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._heightOffset=args.get("heightOffset")
		self._heightStyle=args.get("heightStyle")
		self._renderType=args.get("renderType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)

	@property
	def heightOffset(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["heightOffset"]

	@heightOffset.setter
	def heightOffset(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "heightOffset", val)
		args = {}
		args["heightOffset"] = PropsTypeData.get("heightOffset")
		args["heightOffset"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"heightOffset", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"heightOffset",JsonData)

	@property
	def heightStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["heightStyle"]

	@heightStyle.setter
	def heightStyle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "heightStyle", val)
		args = {}
		args["heightStyle"] = PropsTypeData.get("heightStyle")
		args["heightStyle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"heightStyle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"heightStyle",JsonData)

	@property
	def renderType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["renderType"]

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
