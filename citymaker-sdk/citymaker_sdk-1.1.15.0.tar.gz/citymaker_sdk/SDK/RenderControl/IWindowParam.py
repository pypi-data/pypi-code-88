#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"animationTime":{"t":"double","v":0,
"F":"gs"},"closeButtonEnabled":{"t":"bool","v":True,
"F":"gs"},"hastitle":{"t":"bool","v":False,
"F":"gs"},"hideOnClick":{"t":"bool","v":True,
"F":"gs"},"isPopupWindow":{"t":"byte","v":1,
"F":"gs"},"minButtonVisible":{"t":"bool","v":True,
"F":"gs"},"offsetX":{"t":"int","v":0,
"F":"gs"},"offsetY":{"t":"int","v":0,
"F":"gs"},"position":{"t":"gviHTMLWindowPosition","v":0,
"F":"gs"},"resizable":{"t":"bool","v":True,
"F":"gs"},"rgnTransparentColor":{"t":"Color","v":0,
"F":"gs"},"round":{"t":"int","v":-1,
"F":"gs"},"showWindow":{"t":"byte","v":0,
"F":"gs"},"sizeX":{"t":"int","v":0,
"F":"gs"},"sizeY":{"t":"int","v":0,
"F":"gs"},"topmost":{"t":"bool","v":False,
"F":"gs"},"transparence":{"t":"byte","v":255,
"F":"gs"},"winId":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IWindowParam","F":"g"}}
#Events = {animation:{fn:null}filePath:{fn:null}resetOnHide:{fn:null}rgnTemplateFile:{fn:null}}
class IWindowParam:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._animationTime=args.get("animationTime")
		self._closeButtonEnabled=args.get("closeButtonEnabled")
		self._hastitle=args.get("hastitle")
		self._hideOnClick=args.get("hideOnClick")
		self._isPopupWindow=args.get("isPopupWindow")
		self._minButtonVisible=args.get("minButtonVisible")
		self._offsetX=args.get("offsetX")
		self._offsetY=args.get("offsetY")
		self._position=args.get("position")
		self._resizable=args.get("resizable")
		self._rgnTransparentColor=args.get("rgnTransparentColor")
		self._round=args.get("round")
		self._showWindow=args.get("showWindow")
		self._sizeX=args.get("sizeX")
		self._sizeY=args.get("sizeY")
		self._topmost=args.get("topmost")
		self._transparence=args.get("transparence")
		self._winId=args.get("winId")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def animationTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["animationTime"]

	@animationTime.setter
	def animationTime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "animationTime", val)
		args = {}
		args["animationTime"] = PropsTypeData.get("animationTime")
		args["animationTime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"animationTime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"animationTime",JsonData)

	@property
	def closeButtonEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["closeButtonEnabled"]

	@closeButtonEnabled.setter
	def closeButtonEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "closeButtonEnabled", val)
		args = {}
		args["closeButtonEnabled"] = PropsTypeData.get("closeButtonEnabled")
		args["closeButtonEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"closeButtonEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"closeButtonEnabled",JsonData)

	@property
	def hastitle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hastitle"]

	@hastitle.setter
	def hastitle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "hastitle", val)
		args = {}
		args["hastitle"] = PropsTypeData.get("hastitle")
		args["hastitle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"hastitle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"hastitle",JsonData)

	@property
	def hideOnClick(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hideOnClick"]

	@hideOnClick.setter
	def hideOnClick(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "hideOnClick", val)
		args = {}
		args["hideOnClick"] = PropsTypeData.get("hideOnClick")
		args["hideOnClick"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"hideOnClick", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"hideOnClick",JsonData)

	@property
	def isPopupWindow(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isPopupWindow"]

	@isPopupWindow.setter
	def isPopupWindow(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isPopupWindow", val)
		args = {}
		args["isPopupWindow"] = PropsTypeData.get("isPopupWindow")
		args["isPopupWindow"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isPopupWindow", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isPopupWindow",JsonData)

	@property
	def minButtonVisible(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minButtonVisible"]

	@minButtonVisible.setter
	def minButtonVisible(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minButtonVisible", val)
		args = {}
		args["minButtonVisible"] = PropsTypeData.get("minButtonVisible")
		args["minButtonVisible"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minButtonVisible", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minButtonVisible",JsonData)

	@property
	def offsetX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["offsetX"]

	@offsetX.setter
	def offsetX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "offsetX", val)
		args = {}
		args["offsetX"] = PropsTypeData.get("offsetX")
		args["offsetX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"offsetX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"offsetX",JsonData)

	@property
	def offsetY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["offsetY"]

	@offsetY.setter
	def offsetY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "offsetY", val)
		args = {}
		args["offsetY"] = PropsTypeData.get("offsetY")
		args["offsetY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"offsetY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"offsetY",JsonData)

	@property
	def position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
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
	def resizable(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["resizable"]

	@resizable.setter
	def resizable(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "resizable", val)
		args = {}
		args["resizable"] = PropsTypeData.get("resizable")
		args["resizable"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"resizable", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"resizable",JsonData)

	@property
	def rgnTransparentColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["rgnTransparentColor"]

	@rgnTransparentColor.setter
	def rgnTransparentColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "rgnTransparentColor", val)
		args = {}
		args["rgnTransparentColor"] = PropsTypeData.get("rgnTransparentColor")
		args["rgnTransparentColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"rgnTransparentColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rgnTransparentColor",JsonData)

	@property
	def round(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["round"]

	@round.setter
	def round(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "round", val)
		args = {}
		args["round"] = PropsTypeData.get("round")
		args["round"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"round", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"round",JsonData)

	@property
	def showWindow(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["showWindow"]

	@showWindow.setter
	def showWindow(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "showWindow", val)
		args = {}
		args["showWindow"] = PropsTypeData.get("showWindow")
		args["showWindow"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"showWindow", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"showWindow",JsonData)

	@property
	def sizeX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["sizeX"]

	@sizeX.setter
	def sizeX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "sizeX", val)
		args = {}
		args["sizeX"] = PropsTypeData.get("sizeX")
		args["sizeX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"sizeX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"sizeX",JsonData)

	@property
	def sizeY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["sizeY"]

	@sizeY.setter
	def sizeY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "sizeY", val)
		args = {}
		args["sizeY"] = PropsTypeData.get("sizeY")
		args["sizeY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"sizeY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"sizeY",JsonData)

	@property
	def topmost(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["topmost"]

	@topmost.setter
	def topmost(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "topmost", val)
		args = {}
		args["topmost"] = PropsTypeData.get("topmost")
		args["topmost"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"topmost", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"topmost",JsonData)

	@property
	def transparence(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["transparence"]

	@transparence.setter
	def transparence(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "transparence", val)
		args = {}
		args["transparence"] = PropsTypeData.get("transparence")
		args["transparence"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"transparence", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"transparence",JsonData)

	@property
	def winId(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["winId"]

	@winId.setter
	def winId(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "winId", val)
		args = {}
		args["winId"] = PropsTypeData.get("winId")
		args["winId"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"winId", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"winId",JsonData)

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
