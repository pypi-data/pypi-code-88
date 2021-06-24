#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"fileCacheEnabled":{"t":"bool","v":True,
"F":"gs"},"fileCacheSize":{"t":"int","v":0,
"F":"gs"},"memoryCacheEnabled":{"t":"bool","v":False,
"F":"gs"},"memoryCacheSize":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICacheManager","F":"g"}}
#Events = {fileCachePath:{fn:null}}
class ICacheManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._fileCacheEnabled=args.get("fileCacheEnabled")
		self._fileCacheSize=args.get("fileCacheSize")
		self._memoryCacheEnabled=args.get("memoryCacheEnabled")
		self._memoryCacheSize=args.get("memoryCacheSize")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getTileCacheFileName(self,arg0):  # 先定义函数 
		args = {
				"layerInfo":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getTileCacheFileName', 1, state)

	@property
	def fileCacheEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fileCacheEnabled"]

	@fileCacheEnabled.setter
	def fileCacheEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fileCacheEnabled", val)
		args = {}
		args["fileCacheEnabled"] = PropsTypeData.get("fileCacheEnabled")
		args["fileCacheEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fileCacheEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fileCacheEnabled",JsonData)

	@property
	def fileCacheSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fileCacheSize"]

	@fileCacheSize.setter
	def fileCacheSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fileCacheSize", val)
		args = {}
		args["fileCacheSize"] = PropsTypeData.get("fileCacheSize")
		args["fileCacheSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fileCacheSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fileCacheSize",JsonData)

	@property
	def memoryCacheEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["memoryCacheEnabled"]

	@memoryCacheEnabled.setter
	def memoryCacheEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "memoryCacheEnabled", val)
		args = {}
		args["memoryCacheEnabled"] = PropsTypeData.get("memoryCacheEnabled")
		args["memoryCacheEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"memoryCacheEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"memoryCacheEnabled",JsonData)

	@property
	def memoryCacheSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["memoryCacheSize"]

	@memoryCacheSize.setter
	def memoryCacheSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "memoryCacheSize", val)
		args = {}
		args["memoryCacheSize"] = PropsTypeData.get("memoryCacheSize")
		args["memoryCacheSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"memoryCacheSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"memoryCacheSize",JsonData)

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
