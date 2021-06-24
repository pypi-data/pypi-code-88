#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRObject import IRObject
Props={"depthTestMode":{"t":"gviDepthTestMode","v":0,
"F":"gs"},"envelope":{"t":"IEnvelope","v":None,
"F":"g"},"maxVisibleDistance":{"t":"double","v":0,
"F":"gs"},"minVisibleDistance":{"t":"double","v":-100000,
"F":"gs"},"minVisiblePixels":{"t":"float","v":15,
"F":"gs"},"visibleMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"mouseSelectMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"viewingDistance":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRenderable","F":"g"}}
class IRenderable(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._depthTestMode=args.get("depthTestMode")
		self._envelope=args.get("envelope")
		self._maxVisibleDistance=args.get("maxVisibleDistance")
		self._minVisibleDistance=args.get("minVisibleDistance")
		self._minVisiblePixels=args.get("minVisiblePixels")
		self._visibleMask=args.get("visibleMask")
		self._mouseSelectMask=args.get("mouseSelectMask")
		self._viewingDistance=args.get("viewingDistance")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def unhighlight(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'unhighlight', 0, state)


	def highlight(self,arg0):  # 先定义函数 
		args = {
				"c":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'highlight', 0, state)


	def selectRObjectByGuid(self,arg0):  # 先定义函数 
		args = {
				"guid":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'selectRObjectByGuid', 0, state)


	def setRenderSymbol(self,arg0):  # 先定义函数 
		args = {
				"color":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setRenderSymbol', 0, state)

	@property
	def depthTestMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["depthTestMode"]

	@depthTestMode.setter
	def depthTestMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "depthTestMode", val)
		args = {}
		args["depthTestMode"] = PropsTypeData.get("depthTestMode")
		args["depthTestMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"depthTestMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"depthTestMode",JsonData)

	@property
	def envelope(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"envelope",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"envelope",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "envelope", res)
		return PropsValueData["envelope"]

	@property
	def maxVisibleDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxVisibleDistance"]

	@maxVisibleDistance.setter
	def maxVisibleDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxVisibleDistance", val)
		args = {}
		args["maxVisibleDistance"] = PropsTypeData.get("maxVisibleDistance")
		args["maxVisibleDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxVisibleDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxVisibleDistance",JsonData)

	@property
	def minVisibleDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minVisibleDistance"]

	@minVisibleDistance.setter
	def minVisibleDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minVisibleDistance", val)
		args = {}
		args["minVisibleDistance"] = PropsTypeData.get("minVisibleDistance")
		args["minVisibleDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minVisibleDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minVisibleDistance",JsonData)

	@property
	def minVisiblePixels(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minVisiblePixels"]

	@minVisiblePixels.setter
	def minVisiblePixels(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minVisiblePixels", val)
		args = {}
		args["minVisiblePixels"] = PropsTypeData.get("minVisiblePixels")
		args["minVisiblePixels"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minVisiblePixels", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minVisiblePixels",JsonData)

	@property
	def visibleMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["visibleMask"]

	@visibleMask.setter
	def visibleMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "visibleMask", val)
		args = {}
		args["visibleMask"] = PropsTypeData.get("visibleMask")
		args["visibleMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"visibleMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visibleMask",JsonData)

	@property
	def mouseSelectMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["mouseSelectMask"]

	@mouseSelectMask.setter
	def mouseSelectMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "mouseSelectMask", val)
		args = {}
		args["mouseSelectMask"] = PropsTypeData.get("mouseSelectMask")
		args["mouseSelectMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"mouseSelectMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"mouseSelectMask",JsonData)

	@property
	def viewingDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["viewingDistance"]

	@viewingDistance.setter
	def viewingDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "viewingDistance", val)
		args = {}
		args["viewingDistance"] = PropsTypeData.get("viewingDistance")
		args["viewingDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"viewingDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"viewingDistance",JsonData)

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
