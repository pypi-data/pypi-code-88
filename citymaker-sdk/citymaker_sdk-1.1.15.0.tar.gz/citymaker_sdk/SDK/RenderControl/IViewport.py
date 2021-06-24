#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"activeView":{"t":"int","v":0,
"F":"gs"},"cameraInfoVisible":{"t":"bool","v":False,
"F":"gs"},"cameraViewBindMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"compassVisibleMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"logoVisible":{"t":"bool","v":False,
"F":"gs"},"pipLocationMode":{"t":"gviPIPLocationMode","v":0,
"F":"gs"},"pipRatioH":{"t":"double","v":0.5,
"F":"gs"},"pipRatioV":{"t":"double","v":0.5,
"F":"gs"},"showBorderLine":{"t":"bool","v":True,
"F":"gs"},"splitRatioH":{"t":"double","v":0,
"F":"gs"},"splitRatioV":{"t":"double","v":0,
"F":"gs"},"viewportMode":{"t":"gviViewportMode","v":1,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IViewport","F":"g"}}
class IViewport:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._activeView=args.get("activeView")
		self._cameraInfoVisible=args.get("cameraInfoVisible")
		self._cameraViewBindMask=args.get("cameraViewBindMask")
		self._compassVisibleMask=args.get("compassVisibleMask")
		self._logoVisible=args.get("logoVisible")
		self._pipLocationMode=args.get("pipLocationMode")
		self._pipRatioH=args.get("pipRatioH")
		self._pipRatioV=args.get("pipRatioV")
		self._showBorderLine=args.get("showBorderLine")
		self._splitRatioH=args.get("splitRatioH")
		self._splitRatioV=args.get("splitRatioV")
		self._viewportMode=args.get("viewportMode")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def activeView(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["activeView"]

	@activeView.setter
	def activeView(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "activeView", val)
		args = {}
		args["activeView"] = PropsTypeData.get("activeView")
		args["activeView"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"activeView", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"activeView",JsonData)

	@property
	def cameraInfoVisible(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["cameraInfoVisible"]

	@cameraInfoVisible.setter
	def cameraInfoVisible(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "cameraInfoVisible", val)
		args = {}
		args["cameraInfoVisible"] = PropsTypeData.get("cameraInfoVisible")
		args["cameraInfoVisible"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"cameraInfoVisible", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"cameraInfoVisible",JsonData)

	@property
	def cameraViewBindMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["cameraViewBindMask"]

	@cameraViewBindMask.setter
	def cameraViewBindMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "cameraViewBindMask", val)
		args = {}
		args["cameraViewBindMask"] = PropsTypeData.get("cameraViewBindMask")
		args["cameraViewBindMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"cameraViewBindMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"cameraViewBindMask",JsonData)

	@property
	def compassVisibleMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["compassVisibleMask"]

	@compassVisibleMask.setter
	def compassVisibleMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "compassVisibleMask", val)
		args = {}
		args["compassVisibleMask"] = PropsTypeData.get("compassVisibleMask")
		args["compassVisibleMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"compassVisibleMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"compassVisibleMask",JsonData)

	@property
	def logoVisible(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["logoVisible"]

	@logoVisible.setter
	def logoVisible(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "logoVisible", val)
		args = {}
		args["logoVisible"] = PropsTypeData.get("logoVisible")
		args["logoVisible"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"logoVisible", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"logoVisible",JsonData)

	@property
	def pipLocationMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["pipLocationMode"]

	@pipLocationMode.setter
	def pipLocationMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "pipLocationMode", val)
		args = {}
		args["pipLocationMode"] = PropsTypeData.get("pipLocationMode")
		args["pipLocationMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"pipLocationMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pipLocationMode",JsonData)

	@property
	def pipRatioH(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["pipRatioH"]

	@pipRatioH.setter
	def pipRatioH(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "pipRatioH", val)
		args = {}
		args["pipRatioH"] = PropsTypeData.get("pipRatioH")
		args["pipRatioH"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"pipRatioH", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pipRatioH",JsonData)

	@property
	def pipRatioV(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["pipRatioV"]

	@pipRatioV.setter
	def pipRatioV(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "pipRatioV", val)
		args = {}
		args["pipRatioV"] = PropsTypeData.get("pipRatioV")
		args["pipRatioV"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"pipRatioV", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pipRatioV",JsonData)

	@property
	def showBorderLine(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["showBorderLine"]

	@showBorderLine.setter
	def showBorderLine(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "showBorderLine", val)
		args = {}
		args["showBorderLine"] = PropsTypeData.get("showBorderLine")
		args["showBorderLine"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"showBorderLine", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"showBorderLine",JsonData)

	@property
	def splitRatioH(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["splitRatioH"]

	@splitRatioH.setter
	def splitRatioH(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "splitRatioH", val)
		args = {}
		args["splitRatioH"] = PropsTypeData.get("splitRatioH")
		args["splitRatioH"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"splitRatioH", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"splitRatioH",JsonData)

	@property
	def splitRatioV(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["splitRatioV"]

	@splitRatioV.setter
	def splitRatioV(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "splitRatioV", val)
		args = {}
		args["splitRatioV"] = PropsTypeData.get("splitRatioV")
		args["splitRatioV"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"splitRatioV", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"splitRatioV",JsonData)

	@property
	def viewportMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["viewportMode"]

	@viewportMode.setter
	def viewportMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "viewportMode", val)
		args = {}
		args["viewportMode"] = PropsTypeData.get("viewportMode")
		args["viewportMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"viewportMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"viewportMode",JsonData)

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
