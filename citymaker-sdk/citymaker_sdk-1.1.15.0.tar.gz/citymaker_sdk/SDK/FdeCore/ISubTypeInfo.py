#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"code":{"t":"int","v":0,
"F":"gs"},"fieldDomainInfoCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISubTypeInfo","F":"g"}}
#Events = {name:{fn:null}}
class ISubTypeInfo:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._code=args.get("code")
		self._fieldDomainInfoCount=args.get("fieldDomainInfoCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addFieldDomainInfo(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IFieldDomainInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addFieldDomainInfo', 0, state)


	def getFieldDomainInfo(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFieldDomainInfo', 1, state)

	@property
	def code(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["code"]

	@code.setter
	def code(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "code", val)
		args = {}
		args["code"] = PropsTypeData.get("code")
		args["code"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"code", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"code",JsonData)

	@property
	def fieldDomainInfoCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldDomainInfoCount"]

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
