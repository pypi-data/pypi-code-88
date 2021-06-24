#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"fillStyle":{"t":"IFillStyle","v":None,
"F":"gs"},"headX":{"t":"double","v":0,
"F":"gs"},"headY":{"t":"double","v":0,
"F":"gs"},"lineStyle":{"t":"ILineStyle","v":None,
"F":"gs"},"position":{"t":"IPosition","v":None,
"F":"gs"},"style":{"t":"byte","v":0,
"F":"gs"},"tailX":{"t":"double","v":0,
"F":"gs"},"tailY":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainArrow","F":"g"}}
class ITerrainArrow(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._fillStyle=args.get("fillStyle")
		self._headX=args.get("headX")
		self._headY=args.get("headY")
		self._lineStyle=args.get("lineStyle")
		self._position=args.get("position")
		self._style=args.get("style")
		self._tailX=args.get("tailX")
		self._tailY=args.get("tailY")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getFdeGeometry(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFdeGeometry', 1, state)

	@property
	def fillStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"fillStyle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fillStyle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "fillStyle", res)
		return PropsValueData["fillStyle"]

	@fillStyle.setter
	def fillStyle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fillStyle", val)
		args = {}
		args["fillStyle"] = PropsTypeData.get("fillStyle")
		args["fillStyle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fillStyle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fillStyle",JsonData)

	@property
	def headX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["headX"]

	@headX.setter
	def headX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "headX", val)
		args = {}
		args["headX"] = PropsTypeData.get("headX")
		args["headX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"headX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"headX",JsonData)

	@property
	def headY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["headY"]

	@headY.setter
	def headY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "headY", val)
		args = {}
		args["headY"] = PropsTypeData.get("headY")
		args["headY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"headY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"headY",JsonData)

	@property
	def lineStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"lineStyle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lineStyle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "lineStyle", res)
		return PropsValueData["lineStyle"]

	@lineStyle.setter
	def lineStyle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "lineStyle", val)
		args = {}
		args["lineStyle"] = PropsTypeData.get("lineStyle")
		args["lineStyle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"lineStyle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lineStyle",JsonData)

	@property
	def position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"position",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "position", res)
		return PropsValueData["position"]

	@position.setter
	def position(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "position", val)
		args = {}
		args["position"] = PropsTypeData.get("position")
		args["position"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"position", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",JsonData)

	@property
	def style(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["style"]

	@style.setter
	def style(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "style", val)
		args = {}
		args["style"] = PropsTypeData.get("style")
		args["style"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"style", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"style",JsonData)

	@property
	def tailX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tailX"]

	@tailX.setter
	def tailX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tailX", val)
		args = {}
		args["tailX"] = PropsTypeData.get("tailX")
		args["tailX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tailX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tailX",JsonData)

	@property
	def tailY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tailY"]

	@tailY.setter
	def tailY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tailY", val)
		args = {}
		args["tailY"] = PropsTypeData.get("tailY")
		args["tailY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tailY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tailY",JsonData)

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
