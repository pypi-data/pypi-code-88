#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.depthTestMode=args.get("depthTestMode")
		self.envelope=args.get("envelope")
		self.maxVisibleDistance=args.get("maxVisibleDistance")
		self.minVisibleDistance=args.get("minVisibleDistance")
		self.minVisiblePixels=args.get("minVisiblePixels")
		self.visibleMask=args.get("visibleMask")
		self.mouseSelectMask=args.get("mouseSelectMask")
		self.viewingDistance=args.get("viewingDistance")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				super(IRenderable, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
