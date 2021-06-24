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
"F":"gs"},"fontSize":{"t":"int","v":12,
"F":"gs"},"iconColor":{"t":"Color","v":"",
"F":"gs"},"italic":{"t":"bool","v":False,
"F":"gs"},"limitScreenSize":{"t":"bool","v":True,
"F":"gs"},"lineColor":{"t":"Color","v":"",
"F":"gs"},"lineLength":{"t":"double","v":0.0,
"F":"gs"},"lineToGround":{"t":"gviLineToGroundType","v":0,
"F":"gs"},"lockMode":{"t":"gviLockMode","v":0,
"F":"gs"},"maxImageSize":{"t":"int","v":-1,
"F":"gs"},"maxViewingHeight":{"t":"double","v":1000,
"F":"gs"},"minViewingHeight":{"t":"double","v":0,
"F":"gs"},"multilineJustification":{"t":"gviMultilineJustification","v":1,
"F":"gs"},"pivotAlignment":{"t":"gviPivotAlignment","v":1,
"F":"gs"},"scale":{"t":"double","v":1.0,
"F":"gs"},"showTextBehavior":{"t":"gviShowTextOptions","v":0,
"F":"gs"},"textColor":{"t":"Color","v":"",
"F":"gs"},"textOnImage":{"t":"bool","v":False,
"F":"gs"},"underline":{"t":"bool","v":False,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ILabelStyle","F":"g"}}
#Events = {fontName:{fn:null}frameFileName:{fn:null}textAlignment:{fn:null}}
class ILabelStyle:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._backgroundColor=args.get("backgroundColor")
		self._bold=args.get("bold")
		self._fontSize=args.get("fontSize")
		self._iconColor=args.get("iconColor")
		self._italic=args.get("italic")
		self._limitScreenSize=args.get("limitScreenSize")
		self._lineColor=args.get("lineColor")
		self._lineLength=args.get("lineLength")
		self._lineToGround=args.get("lineToGround")
		self._lockMode=args.get("lockMode")
		self._maxImageSize=args.get("maxImageSize")
		self._maxViewingHeight=args.get("maxViewingHeight")
		self._minViewingHeight=args.get("minViewingHeight")
		self._multilineJustification=args.get("multilineJustification")
		self._pivotAlignment=args.get("pivotAlignment")
		self._scale=args.get("scale")
		self._showTextBehavior=args.get("showTextBehavior")
		self._textColor=args.get("textColor")
		self._textOnImage=args.get("textOnImage")
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
	def fontSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fontSize"]

	@fontSize.setter
	def fontSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fontSize", val)
		args = {}
		args["fontSize"] = PropsTypeData.get("fontSize")
		args["fontSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fontSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fontSize",JsonData)

	@property
	def iconColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["iconColor"]

	@iconColor.setter
	def iconColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "iconColor", val)
		args = {}
		args["iconColor"] = PropsTypeData.get("iconColor")
		args["iconColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"iconColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"iconColor",JsonData)

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
	def limitScreenSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["limitScreenSize"]

	@limitScreenSize.setter
	def limitScreenSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "limitScreenSize", val)
		args = {}
		args["limitScreenSize"] = PropsTypeData.get("limitScreenSize")
		args["limitScreenSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"limitScreenSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"limitScreenSize",JsonData)

	@property
	def lineColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lineColor"]

	@lineColor.setter
	def lineColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "lineColor", val)
		args = {}
		args["lineColor"] = PropsTypeData.get("lineColor")
		args["lineColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"lineColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lineColor",JsonData)

	@property
	def lineLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lineLength"]

	@lineLength.setter
	def lineLength(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "lineLength", val)
		args = {}
		args["lineLength"] = PropsTypeData.get("lineLength")
		args["lineLength"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"lineLength", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lineLength",JsonData)

	@property
	def lineToGround(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lineToGround"]

	@lineToGround.setter
	def lineToGround(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "lineToGround", val)
		args = {}
		args["lineToGround"] = PropsTypeData.get("lineToGround")
		args["lineToGround"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"lineToGround", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lineToGround",JsonData)

	@property
	def lockMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lockMode"]

	@lockMode.setter
	def lockMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "lockMode", val)
		args = {}
		args["lockMode"] = PropsTypeData.get("lockMode")
		args["lockMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"lockMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lockMode",JsonData)

	@property
	def maxImageSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxImageSize"]

	@maxImageSize.setter
	def maxImageSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxImageSize", val)
		args = {}
		args["maxImageSize"] = PropsTypeData.get("maxImageSize")
		args["maxImageSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxImageSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxImageSize",JsonData)

	@property
	def maxViewingHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxViewingHeight"]

	@maxViewingHeight.setter
	def maxViewingHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxViewingHeight", val)
		args = {}
		args["maxViewingHeight"] = PropsTypeData.get("maxViewingHeight")
		args["maxViewingHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxViewingHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxViewingHeight",JsonData)

	@property
	def minViewingHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minViewingHeight"]

	@minViewingHeight.setter
	def minViewingHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minViewingHeight", val)
		args = {}
		args["minViewingHeight"] = PropsTypeData.get("minViewingHeight")
		args["minViewingHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minViewingHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minViewingHeight",JsonData)

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
	def pivotAlignment(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["pivotAlignment"]

	@pivotAlignment.setter
	def pivotAlignment(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "pivotAlignment", val)
		args = {}
		args["pivotAlignment"] = PropsTypeData.get("pivotAlignment")
		args["pivotAlignment"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"pivotAlignment", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pivotAlignment",JsonData)

	@property
	def scale(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["scale"]

	@scale.setter
	def scale(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "scale", val)
		args = {}
		args["scale"] = PropsTypeData.get("scale")
		args["scale"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"scale", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"scale",JsonData)

	@property
	def showTextBehavior(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["showTextBehavior"]

	@showTextBehavior.setter
	def showTextBehavior(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "showTextBehavior", val)
		args = {}
		args["showTextBehavior"] = PropsTypeData.get("showTextBehavior")
		args["showTextBehavior"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"showTextBehavior", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"showTextBehavior",JsonData)

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
	def textOnImage(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["textOnImage"]

	@textOnImage.setter
	def textOnImage(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "textOnImage", val)
		args = {}
		args["textOnImage"] = PropsTypeData.get("textOnImage")
		args["textOnImage"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"textOnImage", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textOnImage",JsonData)

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
