#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"alphaBand":{"t":"int","v":0,
"F":"gs"},"alphaEnabled":{"t":"bool","v":False,
"F":"gs"},"backgroundEnabled":{"t":"bool","v":False,
"F":"gs"},"backgroundKey":{"t":"Color","v":"",
"F":"gs"},"backgroundValue":{"t":"Color","v":"",
"F":"gs"},"blueBand":{"t":"int","v":0,
"F":"gs"},"blueEnabled":{"t":"bool","v":False,
"F":"gs"},"greenBand":{"t":"int","v":0,
"F":"gs"},"greenEnable":{"t":"bool","v":False,
"F":"gs"},"redBand":{"t":"int","v":0,
"F":"gs"},"redEnabled":{"t":"bool","v":False,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRasterSymbol","F":"g"}}
class IRasterSymbol:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._alphaBand=args.get("alphaBand")
		self._alphaEnabled=args.get("alphaEnabled")
		self._backgroundEnabled=args.get("backgroundEnabled")
		self._backgroundKey=args.get("backgroundKey")
		self._backgroundValue=args.get("backgroundValue")
		self._blueBand=args.get("blueBand")
		self._blueEnabled=args.get("blueEnabled")
		self._greenBand=args.get("greenBand")
		self._greenEnable=args.get("greenEnable")
		self._redBand=args.get("redBand")
		self._redEnabled=args.get("redEnabled")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def alphaBand(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["alphaBand"]

	@alphaBand.setter
	def alphaBand(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "alphaBand", val)
		args = {}
		args["alphaBand"] = PropsTypeData.get("alphaBand")
		args["alphaBand"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"alphaBand", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"alphaBand",JsonData)

	@property
	def alphaEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["alphaEnabled"]

	@alphaEnabled.setter
	def alphaEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "alphaEnabled", val)
		args = {}
		args["alphaEnabled"] = PropsTypeData.get("alphaEnabled")
		args["alphaEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"alphaEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"alphaEnabled",JsonData)

	@property
	def backgroundEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["backgroundEnabled"]

	@backgroundEnabled.setter
	def backgroundEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "backgroundEnabled", val)
		args = {}
		args["backgroundEnabled"] = PropsTypeData.get("backgroundEnabled")
		args["backgroundEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"backgroundEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"backgroundEnabled",JsonData)

	@property
	def backgroundKey(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["backgroundKey"]

	@backgroundKey.setter
	def backgroundKey(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "backgroundKey", val)
		args = {}
		args["backgroundKey"] = PropsTypeData.get("backgroundKey")
		args["backgroundKey"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"backgroundKey", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"backgroundKey",JsonData)

	@property
	def backgroundValue(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["backgroundValue"]

	@backgroundValue.setter
	def backgroundValue(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "backgroundValue", val)
		args = {}
		args["backgroundValue"] = PropsTypeData.get("backgroundValue")
		args["backgroundValue"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"backgroundValue", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"backgroundValue",JsonData)

	@property
	def blueBand(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["blueBand"]

	@blueBand.setter
	def blueBand(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "blueBand", val)
		args = {}
		args["blueBand"] = PropsTypeData.get("blueBand")
		args["blueBand"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"blueBand", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"blueBand",JsonData)

	@property
	def blueEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["blueEnabled"]

	@blueEnabled.setter
	def blueEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "blueEnabled", val)
		args = {}
		args["blueEnabled"] = PropsTypeData.get("blueEnabled")
		args["blueEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"blueEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"blueEnabled",JsonData)

	@property
	def greenBand(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["greenBand"]

	@greenBand.setter
	def greenBand(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "greenBand", val)
		args = {}
		args["greenBand"] = PropsTypeData.get("greenBand")
		args["greenBand"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"greenBand", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"greenBand",JsonData)

	@property
	def greenEnable(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["greenEnable"]

	@greenEnable.setter
	def greenEnable(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "greenEnable", val)
		args = {}
		args["greenEnable"] = PropsTypeData.get("greenEnable")
		args["greenEnable"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"greenEnable", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"greenEnable",JsonData)

	@property
	def redBand(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["redBand"]

	@redBand.setter
	def redBand(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "redBand", val)
		args = {}
		args["redBand"] = PropsTypeData.get("redBand")
		args["redBand"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"redBand", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"redBand",JsonData)

	@property
	def redEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["redEnabled"]

	@redEnabled.setter
	def redEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "redEnabled", val)
		args = {}
		args["redEnabled"] = PropsTypeData.get("redEnabled")
		args["redEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"redEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"redEnabled",JsonData)

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
