#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"alignment":{"t":"gviPivotAlignment","v":0,
"F":"gs"},"depth":{"t":"float","v":0,
"F":"gs"},"rotation":{"t":"float","v":0,
"F":"gs"},"textStyle":{"t":"ITextAttribute","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IOverlayLabel","F":"g"}}
#Events = {imageName:{fn:null}text:{fn:null}}
class IOverlayLabel(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._alignment=args.get("alignment")
		self._depth=args.get("depth")
		self._rotation=args.get("rotation")
		self._textStyle=args.get("textStyle")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getHeight(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getHeight', 1, state)


	def getWidth(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getWidth', 1, state)


	def getX(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getX', 1, state)


	def getY(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getY', 1, state)


	def setHeight(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setHeight', 0, state)


	def setWidth(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setWidth', 0, state)


	def setX(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setX', 0, state)


	def setY(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setY', 0, state)

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
	def rotation(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["rotation"]

	@rotation.setter
	def rotation(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "rotation", val)
		args = {}
		args["rotation"] = PropsTypeData.get("rotation")
		args["rotation"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"rotation", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rotation",JsonData)

	@property
	def textStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"textStyle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textStyle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "textStyle", res)
		return PropsValueData["textStyle"]

	@textStyle.setter
	def textStyle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "textStyle", val)
		args = {}
		args["textStyle"] = PropsTypeData.get("textStyle")
		args["textStyle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"textStyle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textStyle",JsonData)

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
