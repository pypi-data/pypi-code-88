#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"dynamicPlacement":{"t":"bool","v":False,
"F":"gs"},"minimizeOverlap":{"t":"bool","v":False,
"F":"gs"},"removeDuplicate":{"t":"bool","v":False,
"F":"gs"},"renderType":{"t":"gviRenderType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITextRender","F":"g"}}
#Events = {expression:{fn:null}}
class ITextRender:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._dynamicPlacement=args.get("dynamicPlacement")
		self._minimizeOverlap=args.get("minimizeOverlap")
		self._removeDuplicate=args.get("removeDuplicate")
		self._renderType=args.get("renderType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)

	@property
	def dynamicPlacement(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["dynamicPlacement"]

	@dynamicPlacement.setter
	def dynamicPlacement(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "dynamicPlacement", val)
		args = {}
		args["dynamicPlacement"] = PropsTypeData.get("dynamicPlacement")
		args["dynamicPlacement"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"dynamicPlacement", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"dynamicPlacement",JsonData)

	@property
	def minimizeOverlap(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minimizeOverlap"]

	@minimizeOverlap.setter
	def minimizeOverlap(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minimizeOverlap", val)
		args = {}
		args["minimizeOverlap"] = PropsTypeData.get("minimizeOverlap")
		args["minimizeOverlap"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minimizeOverlap", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minimizeOverlap",JsonData)

	@property
	def removeDuplicate(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["removeDuplicate"]

	@removeDuplicate.setter
	def removeDuplicate(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "removeDuplicate", val)
		args = {}
		args["removeDuplicate"] = PropsTypeData.get("removeDuplicate")
		args["removeDuplicate"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"removeDuplicate", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"removeDuplicate",JsonData)

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
