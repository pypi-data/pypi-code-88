#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.compareRenderRuleVariants=args.get("compareRenderRuleVariants")
		self.cullMode=args.get("cullMode")
		self.drawOrder=args.get("drawOrder")
		self.enableTemporal=args.get("enableTemporal")
		self.featureClassId=args.get("featureClassId")
		self.featureClassInfo=args.get("featureClassInfo")
		self.forceCullMode=args.get("forceCullMode")
		self.geometryType=args.get("geometryType")
		self.hiddenFeatures=args.get("hiddenFeatures")
		self.time=args.get("time")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				"max":{"t": "N","v": arg1},
				"min":{"t": "N","v": arg2},
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

	def __getattr__(self,name):
		if name in Props:
			attrVal=Props[name]
			if name =="_HashCode":
				return CM.dict_get(attrVal, "v", None)
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("g") > -1:
				if CP.ClassFN.get(t) is not None and "PickResult" not in Props["propertyType"]["v"] and name != "propertyType":
					PropsTypeData = CM.getPropsTypeData(self._HashCode)
					PropsValueData = CM.getPropsValueData(self._HashCode)
					jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),name,None)
					res=socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,jsonData)
					CM.addPropsValue(PropsValueData["_HashCode"], name, res)
					return PropsValueData[name]
				else:
					PropsValueData = CM.getPropsValueData(self._HashCode)
					if name == "fullScreen":
						res=CM.isFull()
					CM.addPropsValue(PropsValueData.get("_HashCode"), name, res)
					return PropsValueData[name]

	def __setattr__(self,name,value):
		if name in Props:
			attrVal=Props[name]
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("s") > -1:
				if name =="_HashCode":
					CM.dict_set(attrVal, "F", value)
					return
				PropsTypeData = CM.getPropsTypeData(self._HashCode)
				PropsValueData = CM.getPropsValueData(self._HashCode)
				CM.addPropsValue(PropsValueData.get("_HashCode"), name, value)
				if name == "fullScreen":
					res=CM.isFull()
					return
				args = {}
				args[name] = PropsTypeData.get(name)
				args[name]["v"] = value
				JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),name, args)
				socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,JsonData)
				super(IFeatureLayer, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
