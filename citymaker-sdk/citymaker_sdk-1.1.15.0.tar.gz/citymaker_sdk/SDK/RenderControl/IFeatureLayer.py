#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"compareRenderRuleVariants":{"t":"IPropertySet","v":None,
"F":"gs"},"cullMode":{"t":"gviCullFaceMode","v":1,
"F":"gs"},"drawOrder":{"t":"int","v":0,
"F":"gs"},"enableTemporal":{"t":"bool","v":False,
"F":"gs"},"featureClassId":{"t":"Guid","v":"",
"F":"g"},"featureClassInfo":{"t":"IFeatureClassInfo","v":None,
"F":"g"},"forceCullMode":{"t":"bool","v":False,
"F":"gs"},"geometryType":{"t":"gviGeometryColumnType","v":0,
"F":"g"},"hiddenFeatures":{"t":"int []","v":"",
"F":"gs"},"time":{"t":"DateTime","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureLayer","F":"g"}}
#Events = {geometryFieldName:{fn:null}}
class IFeatureLayer(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._compareRenderRuleVariants=args.get("compareRenderRuleVariants")
		self._cullMode=args.get("cullMode")
		self._drawOrder=args.get("drawOrder")
		self._enableTemporal=args.get("enableTemporal")
		self._featureClassId=args.get("featureClassId")
		self._featureClassInfo=args.get("featureClassInfo")
		self._forceCullMode=args.get("forceCullMode")
		self._geometryType=args.get("geometryType")
		self._hiddenFeatures=args.get("hiddenFeatures")
		self._time=args.get("time")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getEnableGroupColor(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEnableGroupColor', 1, state)


	def getGeometryRender(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getGeometryRender', 1, state)


	def getGroupColor(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getGroupColor', 1, state)


	def getGroupVisibleMask(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getGroupVisibleMask', 1, state)


	def getTextRender(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getTextRender', 1, state)


	def getWKT(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getWKT', 1, state)


	def highlightFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"fids":{"t": "<N>","v": arg0},
				"colorValue":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'highlightFeatures', 1, state)


	def resetAllVisibleMask(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'resetAllVisibleMask', 1, state)


	def resetFeatureVisibleMask(self,arg0):  # 先定义函数 
		args = {
				"featureId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'resetFeatureVisibleMask', 1, state)


	def setEnableGroupColor(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0},
				"newVal":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setEnableGroupColor', 0, state)


	def setFeaturesVisibleMask(self,arg0,arg1):  # 先定义函数 
		args = {
				"fids":{"t": "<N>","v": arg0},
				"visibleMask":{"t": "gviViewportMask","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setFeaturesVisibleMask', 1, state)


	def setGeometryRender(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IGeometryRender","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setGeometryRender', 1, state)


	def setGroupColor(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0},
				"newVal":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setGroupColor', 0, state)


	def setGroupVisibleMask(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0},
				"visibleMask":{"t": "gviViewportMask","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setGroupVisibleMask', 0, state)


	def setTextRender(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "ITextRender","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setTextRender', 1, state)


	def unhighlightFeature(self,arg0):  # 先定义函数 
		args = {
				"featureId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightFeature', 1, state)


	def unhighlightFeatures(self,arg0):  # 先定义函数 
		args = {
				"fids":{"t": "<N>","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightFeatures', 1, state)


	def highlightFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"featureId":{"t": "N","v": arg0},
				"colorValue":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'highlightFeature', 1, state)


	def unhighlightAll(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightAll', 1, state)


	def setFeatureVisibleMask(self,arg0,arg1):  # 先定义函数 
		args = {
				"featureId":{"t": "N","v": arg0},
				"visibleMask":{"t": "gviViewportMask","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setFeatureVisibleMask', 1, state)


	def setFLToolTipTextRender(self,arg0):  # 先定义函数 
		args = {
				"text":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setFLToolTipTextRender', 0, state)


	def setFLGeometryRender(self,arg0):  # 先定义函数 
		args = {
				"color":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setFLGeometryRender', 0, state)


	def setValueMapGeometryRender(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"groupField":{"t": "S","v": arg0},
				"max":{"t": "Number","v": arg1},
				"min":{"t": "Number","v": arg2},
				"color":{"t": "S","v": arg3}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setValueMapGeometryRender', 0, state)


	def setBgFLSymbol(self,):  # 先定义函数 
		args = {}
		state = "new"
		CM.AddPrototype(self,args, 'setBgFLSymbol', 0, state)


	def setUnSelectSymbol(self,):  # 先定义函数 
		args = {}
		state = "new"
		CM.AddPrototype(self,args, 'setUnSelectSymbol', 0, state)


	def setFLMouseSelectMask(self,arg0):  # 先定义函数 
		args = {
				"maskType":{"t": "gviViewportMask","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setFLMouseSelectMask', 0, state)

	@property
	def compareRenderRuleVariants(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"compareRenderRuleVariants",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"compareRenderRuleVariants",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "compareRenderRuleVariants", res)
		return PropsValueData["compareRenderRuleVariants"]

	@compareRenderRuleVariants.setter
	def compareRenderRuleVariants(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "compareRenderRuleVariants", val)
		args = {}
		args["compareRenderRuleVariants"] = PropsTypeData.get("compareRenderRuleVariants")
		args["compareRenderRuleVariants"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"compareRenderRuleVariants", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"compareRenderRuleVariants",JsonData)

	@property
	def cullMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["cullMode"]

	@cullMode.setter
	def cullMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "cullMode", val)
		args = {}
		args["cullMode"] = PropsTypeData.get("cullMode")
		args["cullMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"cullMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"cullMode",JsonData)

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
	def enableTemporal(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["enableTemporal"]

	@enableTemporal.setter
	def enableTemporal(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "enableTemporal", val)
		args = {}
		args["enableTemporal"] = PropsTypeData.get("enableTemporal")
		args["enableTemporal"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"enableTemporal", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"enableTemporal",JsonData)

	@property
	def featureClassId(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["featureClassId"]

	@property
	def featureClassInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"featureClassInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"featureClassInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "featureClassInfo", res)
		return PropsValueData["featureClassInfo"]

	@property
	def forceCullMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["forceCullMode"]

	@forceCullMode.setter
	def forceCullMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "forceCullMode", val)
		args = {}
		args["forceCullMode"] = PropsTypeData.get("forceCullMode")
		args["forceCullMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"forceCullMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"forceCullMode",JsonData)

	@property
	def geometryType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["geometryType"]

	@property
	def hiddenFeatures(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hiddenFeatures"]

	@hiddenFeatures.setter
	def hiddenFeatures(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "hiddenFeatures", val)
		args = {}
		args["hiddenFeatures"] = PropsTypeData.get("hiddenFeatures")
		args["hiddenFeatures"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"hiddenFeatures", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"hiddenFeatures",JsonData)

	@property
	def time(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["time"]

	@time.setter
	def time(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "time", val)
		args = {}
		args["time"] = PropsTypeData.get("time")
		args["time"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"time", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"time",JsonData)

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
