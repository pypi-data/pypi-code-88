#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"backgroundColor":{"t":"Color","v":"",
"F":"gs"},"bold":{"t":"bool","v":False,
"F":"gs"},"italic":{"t":"bool","v":False,
"F":"gs"},"multilineJustification":{"t":"gviMultilineJustification","v":0,
"F":"gs"},"outlineColor":{"t":"Color","v":"",
"F":"gs"},"textColor":{"t":"Color","v":"",
"F":"gs"},"textSize":{"t":"int","v":0,
"F":"gs"},"underline":{"t":"bool","v":False,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITextAttribute","F":"g"}}
#Events = {font:{fn:null}}
class ITextAttribute:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._backgroundColor=args.get("backgroundColor")
		self._bold=args.get("bold")
		self._italic=args.get("italic")
		self._multilineJustification=args.get("multilineJustification")
		self._outlineColor=args.get("outlineColor")
		self._textColor=args.get("textColor")
		self._textSize=args.get("textSize")
		self._underline=args.get("underline")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def backgroundColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["backgroundColor"]

	@backgroundColor.setter
	def backgroundColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "backgroundColor", val)
		args = {}
		args["backgroundColor"] = PropsTypeData.get("backgroundColor")
		args["backgroundColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"backgroundColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"backgroundColor",JsonData)

	@property
	def bold(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["bold"]

	@bold.setter
	def bold(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "bold", val)
		args = {}
		args["bold"] = PropsTypeData.get("bold")
		args["bold"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"bold", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"bold",JsonData)

	@property
	def italic(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["italic"]

	@italic.setter
	def italic(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "italic", val)
		args = {}
		args["italic"] = PropsTypeData.get("italic")
		args["italic"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"italic", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"italic",JsonData)

	@property
	def multilineJustification(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["multilineJustification"]

	@multilineJustification.setter
	def multilineJustification(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "multilineJustification", val)
		args = {}
		args["multilineJustification"] = PropsTypeData.get("multilineJustification")
		args["multilineJustification"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"multilineJustification", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"multilineJustification",JsonData)

	@property
	def outlineColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["outlineColor"]

	@outlineColor.setter
	def outlineColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "outlineColor", val)
		args = {}
		args["outlineColor"] = PropsTypeData.get("outlineColor")
		args["outlineColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"outlineColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"outlineColor",JsonData)

	@property
	def textColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["textColor"]

	@textColor.setter
	def textColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "textColor", val)
		args = {}
		args["textColor"] = PropsTypeData.get("textColor")
		args["textColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"textColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textColor",JsonData)

	@property
	def textSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["textSize"]

	@textSize.setter
	def textSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "textSize", val)
		args = {}
		args["textSize"] = PropsTypeData.get("textSize")
		args["textSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"textSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textSize",JsonData)

	@property
	def underline(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["underline"]

	@underline.setter
	def underline(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "underline", val)
		args = {}
		args["underline"] = PropsTypeData.get("underline")
		args["underline"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"underline", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"underline",JsonData)

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
