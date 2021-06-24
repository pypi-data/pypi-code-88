#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"bandCount":{"t":"int","v":0,
"F":"g"},"drawOrder":{"t":"double","v":0,
"F":"gs"},"imageHeight":{"t":"int","v":0,
"F":"g"},"imageWidth":{"t":"int","v":0,
"F":"g"},"opacity":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IImageryLayer","F":"g"}}
#Events = {connectionString:{fn:null}}
class IImageryLayer(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._bandCount=args.get("bandCount")
		self._drawOrder=args.get("drawOrder")
		self._imageHeight=args.get("imageHeight")
		self._imageWidth=args.get("imageWidth")
		self._opacity=args.get("opacity")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getExtent(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getExtent', 1, state)


	def getRasterSymbol(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRasterSymbol', 1, state)


	def getResolution(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getResolution', 1, state)


	def getWKT(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getWKT', 1, state)


	def setRasterSymbol(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IRasterSymbol","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRasterSymbol', 0, state)


	def setWKT(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setWKT', 1, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'valid', 1, state)

	@property
	def bandCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["bandCount"]

	@property
	def drawOrder(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["drawOrder"]

	@drawOrder.setter
	def drawOrder(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "drawOrder", val)
		args = {}
		args["drawOrder"] = PropsTypeData.get("drawOrder")
		args["drawOrder"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"drawOrder", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"drawOrder",JsonData)

	@property
	def imageHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["imageHeight"]

	@property
	def imageWidth(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["imageWidth"]

	@property
	def opacity(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["opacity"]

	@opacity.setter
	def opacity(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "opacity", val)
		args = {}
		args["opacity"] = PropsTypeData.get("opacity")
		args["opacity"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"opacity", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"opacity",JsonData)

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
