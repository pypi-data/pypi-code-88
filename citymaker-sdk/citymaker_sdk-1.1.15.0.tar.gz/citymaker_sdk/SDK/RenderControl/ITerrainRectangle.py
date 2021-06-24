#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"bottom":{"t":"double","v":0,
"F":"gs"},"depth":{"t":"double","v":0,
"F":"gs"},"fillStyle":{"t":"IFillStyle","v":None,
"F":"gs"},"left":{"t":"double","v":0,
"F":"gs"},"lineStyle":{"t":"ILineStyle","v":None,
"F":"gs"},"position":{"t":"IPosition","v":None,
"F":"gs"},"right":{"t":"double","v":0,
"F":"gs"},"top":{"t":"double","v":0,
"F":"gs"},"width":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainRectangle","F":"g"}}
class ITerrainRectangle(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._bottom=args.get("bottom")
		self._depth=args.get("depth")
		self._fillStyle=args.get("fillStyle")
		self._left=args.get("left")
		self._lineStyle=args.get("lineStyle")
		self._position=args.get("position")
		self._right=args.get("right")
		self._top=args.get("top")
		self._width=args.get("width")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getFdeGeometry(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFdeGeometry', 1, state)

	@property
	def bottom(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["bottom"]

	@bottom.setter
	def bottom(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "bottom", val)
		args = {}
		args["bottom"] = PropsTypeData.get("bottom")
		args["bottom"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"bottom", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"bottom",JsonData)

	@property
	def depth(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["depth"]

	@depth.setter
	def depth(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "depth", val)
		args = {}
		args["depth"] = PropsTypeData.get("depth")
		args["depth"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"depth", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"depth",JsonData)

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
	def left(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["left"]

	@left.setter
	def left(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "left", val)
		args = {}
		args["left"] = PropsTypeData.get("left")
		args["left"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"left", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"left",JsonData)

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
	def right(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["right"]

	@right.setter
	def right(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "right", val)
		args = {}
		args["right"] = PropsTypeData.get("right")
		args["right"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"right", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"right",JsonData)

	@property
	def top(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["top"]

	@top.setter
	def top(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "top", val)
		args = {}
		args["top"] = PropsTypeData.get("top")
		args["top"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"top", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"top",JsonData)

	@property
	def width(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["width"]

	@width.setter
	def width(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "width", val)
		args = {}
		args["width"] = PropsTypeData.get("width")
		args["width"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"width", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"width",JsonData)

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
