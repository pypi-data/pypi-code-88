#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"isEnable":{"t":"bool","v":False,
"F":"gs"},"maxViewHeight":{"t":"double","v":0,
"F":"gs"},"minViewHeight":{"t":"double","v":0,
"F":"gs"},"worldPosition":{"t":"IPoint","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IOverlayUILabel","F":"g"}}
class IOverlayUILabel(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._isEnable=args.get("isEnable")
		self._maxViewHeight=args.get("maxViewHeight")
		self._minViewHeight=args.get("minViewHeight")
		self._worldPosition=args.get("worldPosition")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getCanvas(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getCanvas', 1, state)


	def setAnchor(self,arg0,arg1):  # 先定义函数 
		args = {
				"left":{"t": "IUIDim","v": arg0},
				"top":{"t": "IUIDim","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setAnchor', 0, state)

	@property
	def isEnable(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEnable"]

	@isEnable.setter
	def isEnable(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isEnable", val)
		args = {}
		args["isEnable"] = PropsTypeData.get("isEnable")
		args["isEnable"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isEnable", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isEnable",JsonData)

	@property
	def maxViewHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxViewHeight"]

	@maxViewHeight.setter
	def maxViewHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxViewHeight", val)
		args = {}
		args["maxViewHeight"] = PropsTypeData.get("maxViewHeight")
		args["maxViewHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxViewHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxViewHeight",JsonData)

	@property
	def minViewHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minViewHeight"]

	@minViewHeight.setter
	def minViewHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minViewHeight", val)
		args = {}
		args["minViewHeight"] = PropsTypeData.get("minViewHeight")
		args["minViewHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minViewHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minViewHeight",JsonData)

	@property
	def worldPosition(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"worldPosition",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"worldPosition",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "worldPosition", res)
		return PropsValueData["worldPosition"]

	@worldPosition.setter
	def worldPosition(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "worldPosition", val)
		args = {}
		args["worldPosition"] = PropsTypeData.get("worldPosition")
		args["worldPosition"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"worldPosition", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"worldPosition",JsonData)

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
