#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"drawLine":{"t":"bool","v":False,
"F":"gs"},"lineColor":{"t":"Color","v":"",
"F":"gs"},"lockMode":{"t":"gviLockMode","v":0,
"F":"gs"},"marginColor":{"t":"Color","v":"",
"F":"gs"},"marginHeight":{"t":"int","v":0,
"F":"gs"},"marginWidth":{"t":"int","v":0,
"F":"gs"},"maxVisualDistance":{"t":"double","v":0,
"F":"gs"},"minVisualDistance":{"t":"double","v":0,
"F":"gs"},"pivotAlignment":{"t":"gviPivotAlignment","v":0,
"F":"gs"},"priority":{"t":"int","v":1,
"F":"gs"},"textAttribute":{"t":"ITextAttribute","v":None,
"F":"gs"},"verticalOffset":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITextSymbol","F":"g"}}
class ITextSymbol:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._drawLine=args.get("drawLine")
		self._lineColor=args.get("lineColor")
		self._lockMode=args.get("lockMode")
		self._marginColor=args.get("marginColor")
		self._marginHeight=args.get("marginHeight")
		self._marginWidth=args.get("marginWidth")
		self._maxVisualDistance=args.get("maxVisualDistance")
		self._minVisualDistance=args.get("minVisualDistance")
		self._pivotAlignment=args.get("pivotAlignment")
		self._priority=args.get("priority")
		self._textAttribute=args.get("textAttribute")
		self._verticalOffset=args.get("verticalOffset")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)

	@property
	def drawLine(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["drawLine"]

	@drawLine.setter
	def drawLine(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "drawLine", val)
		args = {}
		args["drawLine"] = PropsTypeData.get("drawLine")
		args["drawLine"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"drawLine", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"drawLine",JsonData)

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
	def marginColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["marginColor"]

	@marginColor.setter
	def marginColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "marginColor", val)
		args = {}
		args["marginColor"] = PropsTypeData.get("marginColor")
		args["marginColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"marginColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"marginColor",JsonData)

	@property
	def marginHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["marginHeight"]

	@marginHeight.setter
	def marginHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "marginHeight", val)
		args = {}
		args["marginHeight"] = PropsTypeData.get("marginHeight")
		args["marginHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"marginHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"marginHeight",JsonData)

	@property
	def marginWidth(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["marginWidth"]

	@marginWidth.setter
	def marginWidth(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "marginWidth", val)
		args = {}
		args["marginWidth"] = PropsTypeData.get("marginWidth")
		args["marginWidth"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"marginWidth", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"marginWidth",JsonData)

	@property
	def maxVisualDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxVisualDistance"]

	@maxVisualDistance.setter
	def maxVisualDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxVisualDistance", val)
		args = {}
		args["maxVisualDistance"] = PropsTypeData.get("maxVisualDistance")
		args["maxVisualDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxVisualDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxVisualDistance",JsonData)

	@property
	def minVisualDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minVisualDistance"]

	@minVisualDistance.setter
	def minVisualDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minVisualDistance", val)
		args = {}
		args["minVisualDistance"] = PropsTypeData.get("minVisualDistance")
		args["minVisualDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minVisualDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minVisualDistance",JsonData)

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
	def priority(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["priority"]

	@priority.setter
	def priority(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "priority", val)
		args = {}
		args["priority"] = PropsTypeData.get("priority")
		args["priority"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"priority", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"priority",JsonData)

	@property
	def textAttribute(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"textAttribute",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textAttribute",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "textAttribute", res)
		return PropsValueData["textAttribute"]

	@textAttribute.setter
	def textAttribute(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "textAttribute", val)
		args = {}
		args["textAttribute"] = PropsTypeData.get("textAttribute")
		args["textAttribute"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"textAttribute", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"textAttribute",JsonData)

	@property
	def verticalOffset(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["verticalOffset"]

	@verticalOffset.setter
	def verticalOffset(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "verticalOffset", val)
		args = {}
		args["verticalOffset"] = PropsTypeData.get("verticalOffset")
		args["verticalOffset"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"verticalOffset", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"verticalOffset",JsonData)

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
