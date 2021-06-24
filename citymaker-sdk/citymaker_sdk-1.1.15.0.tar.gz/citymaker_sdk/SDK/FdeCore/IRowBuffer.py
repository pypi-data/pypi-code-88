#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"fieldCount":{"t":"int","v":0,
"F":"g"},"fields":{"t":"IFieldInfoCollection","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRowBuffer","F":"g"}}
class IRowBuffer:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._fieldCount=args.get("fieldCount")
		self._fields=args.get("fields")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,arg0):  # 先定义函数 
		args = {
				"cloneIsChangedFlag":{"t": "B","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def copyTo(self,arg0,arg1):  # 先定义函数 
		args = {
				"other":{"t": "IRowBuffer","v": arg0},
				"cloneIsChangedFlag":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'copyTo', 0, state)


	def fieldIndex(self,arg0):  # 先定义函数 
		args = {
				"fieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'fieldIndex', 1, state)


	def getValue(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getValue', 1, state)


	def isChanged(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isChanged', 1, state)


	def isNull(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isNull', 1, state)


	def setNull(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setNull', 0, state)


	def setValue(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setValue', 0, state)

	@property
	def fieldCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldCount"]

	@property
	def fields(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"fields",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fields",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "fields", res)
		return PropsValueData["fields"]

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
