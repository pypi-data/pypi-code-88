#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"attributeMask":{"t":"gviAttributeMask","v":7,
"F":"gs"},"guid":{"t":"Guid","v":"",
"F":"g"},"saveInCepFile":{"t":"bool","v":False,
"F":"gs"},"type":{"t":"gviObjectType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRObject","F":"g"}}
#Events = {name:{fn:null}}
class IRObject:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._attributeMask=args.get("attributeMask")
		self._guid=args.get("guid")
		self._saveInCepFile=args.get("saveInCepFile")
		self._type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getClientData(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getClientData', 1, state)


	def setClientData(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"val":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setClientData', 0, state)

	@property
	def attributeMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["attributeMask"]

	@attributeMask.setter
	def attributeMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "attributeMask", val)
		args = {}
		args["attributeMask"] = PropsTypeData.get("attributeMask")
		args["attributeMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"attributeMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"attributeMask",JsonData)

	@property
	def guid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["guid"]

	@property
	def saveInCepFile(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["saveInCepFile"]

	@saveInCepFile.setter
	def saveInCepFile(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "saveInCepFile", val)
		args = {}
		args["saveInCepFile"] = PropsTypeData.get("saveInCepFile")
		args["saveInCepFile"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"saveInCepFile", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"saveInCepFile",JsonData)

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

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
