#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"fieldCount":{"t":"int","v":0,
"F":"g"},"fields":{"t":"IFieldInfoCollection","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRowBuffer","F":"g"}}
class IRowBuffer:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.fieldCount=args.get("fieldCount")
		self.fields=args.get("fields")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				super(IRowBuffer, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
