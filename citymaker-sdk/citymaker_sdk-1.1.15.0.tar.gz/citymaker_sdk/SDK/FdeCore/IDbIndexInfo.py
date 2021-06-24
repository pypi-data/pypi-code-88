#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.IIndexInfo import IIndexInfo
Props={"fieldCount":{"t":"int","v":0,
"F":"g"},"unique":{"t":"bool","v":False,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDbIndexInfo","F":"g"}}
#Events = {name:{fn:null}}
class IDbIndexInfo(IIndexInfo):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._fieldCount=args.get("fieldCount")
		self._unique=args.get("unique")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def appendFieldDefine(self,arg0,arg1):  # 先定义函数 
		args = {
				"field":{"t": "S","v": arg0},
				"sortAsc":{"t": "B","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'appendFieldDefine', 1, state)


	def deleteFieldDefine(self,arg0):  # 先定义函数 
		args = {
				"field":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteFieldDefine', 0, state)


	def getFieldAscending(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFieldAscending', 1, state)


	def getFieldName(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFieldName', 1, state)


	def setSortAsc(self,arg0,arg1):  # 先定义函数 
		args = {
				"field":{"t": "S","v": arg0},
				"sortAsc":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setSortAsc', 0, state)

	@property
	def fieldCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldCount"]

	@property
	def unique(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["unique"]

	@unique.setter
	def unique(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "unique", val)
		args = {}
		args["unique"] = PropsTypeData.get("unique")
		args["unique"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"unique", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"unique",JsonData)

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
