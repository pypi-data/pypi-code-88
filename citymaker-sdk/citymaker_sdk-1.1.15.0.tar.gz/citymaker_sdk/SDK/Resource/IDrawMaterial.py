#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"cullMode":{"t":"gviCullFaceMode","v":1,
"F":"gs"},"depthBias":{"t":"double","v":0,
"F":"gs"},"diffuseColor":{"t":"Color","v":"",
"F":"gs"},"enableBlend":{"t":"bool","v":False,
"F":"gs"},"enableLight":{"t":"bool","v":False,
"F":"gs"},"specularColor":{"t":"Color","v":"",
"F":"gs"},"wrapModeS":{"t":"gviTextureWrapMode","v":1,
"F":"gs"},"wrapModeT":{"t":"gviTextureWrapMode","v":1,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDrawMaterial","F":"g"}}
#Events = {textureName:{fn:null}}
class IDrawMaterial:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._cullMode=args.get("cullMode")
		self._depthBias=args.get("depthBias")
		self._diffuseColor=args.get("diffuseColor")
		self._enableBlend=args.get("enableBlend")
		self._enableLight=args.get("enableLight")
		self._specularColor=args.get("specularColor")
		self._wrapModeS=args.get("wrapModeS")
		self._wrapModeT=args.get("wrapModeT")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
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
	def depthBias(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["depthBias"]

	@depthBias.setter
	def depthBias(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "depthBias", val)
		args = {}
		args["depthBias"] = PropsTypeData.get("depthBias")
		args["depthBias"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"depthBias", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"depthBias",JsonData)

	@property
	def diffuseColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["diffuseColor"]

	@diffuseColor.setter
	def diffuseColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "diffuseColor", val)
		args = {}
		args["diffuseColor"] = PropsTypeData.get("diffuseColor")
		args["diffuseColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"diffuseColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"diffuseColor",JsonData)

	@property
	def enableBlend(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["enableBlend"]

	@enableBlend.setter
	def enableBlend(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "enableBlend", val)
		args = {}
		args["enableBlend"] = PropsTypeData.get("enableBlend")
		args["enableBlend"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"enableBlend", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"enableBlend",JsonData)

	@property
	def enableLight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["enableLight"]

	@enableLight.setter
	def enableLight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "enableLight", val)
		args = {}
		args["enableLight"] = PropsTypeData.get("enableLight")
		args["enableLight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"enableLight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"enableLight",JsonData)

	@property
	def specularColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["specularColor"]

	@specularColor.setter
	def specularColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "specularColor", val)
		args = {}
		args["specularColor"] = PropsTypeData.get("specularColor")
		args["specularColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"specularColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"specularColor",JsonData)

	@property
	def wrapModeS(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["wrapModeS"]

	@wrapModeS.setter
	def wrapModeS(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "wrapModeS", val)
		args = {}
		args["wrapModeS"] = PropsTypeData.get("wrapModeS")
		args["wrapModeS"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"wrapModeS", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"wrapModeS",JsonData)

	@property
	def wrapModeT(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["wrapModeT"]

	@wrapModeT.setter
	def wrapModeT(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "wrapModeT", val)
		args = {}
		args["wrapModeT"] = PropsTypeData.get("wrapModeT")
		args["wrapModeT"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"wrapModeT", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"wrapModeT",JsonData)

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
