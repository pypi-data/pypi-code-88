#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"customData":{"t":"IPropertySet","v":None,
"F":"gs"},"domainType":{"t":"gviDomainType","v":0,
"F":"g"},"fieldType":{"t":"gviFieldType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDomain","F":"g"}}
#Events = {description:{fn:null}name:{fn:null}owner:{fn:null}}
class IDomain:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._customData=args.get("customData")
		self._domainType=args.get("domainType")
		self._fieldType=args.get("fieldType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def isMemberOf(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "O","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isMemberOf', 1, state)

	@property
	def customData(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"customData",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"customData",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "customData", res)
		return PropsValueData["customData"]

	@customData.setter
	def customData(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "customData", val)
		args = {}
		args["customData"] = PropsTypeData.get("customData")
		args["customData"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"customData", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"customData",JsonData)

	@property
	def domainType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["domainType"]

	@property
	def fieldType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldType"]

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
