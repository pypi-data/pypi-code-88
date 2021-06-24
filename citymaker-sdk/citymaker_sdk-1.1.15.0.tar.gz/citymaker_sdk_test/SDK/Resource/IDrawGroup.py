#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"CompleteMapFactor":{"t":"float","v":0.5,
"F":"gs"},"IsEmpty":{"t":"bool","v":False,
"F":"g"},"PrimitiveCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDrawGroup","F":"g"}}
#Events = {CompleteMapTextureName:{fn:null}LightMapTextureName:{fn:null}}
class IDrawGroup:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.CompleteMapFactor=args.get("CompleteMapFactor")
		self.IsEmpty=args.get("IsEmpty")
		self.PrimitiveCount=args.get("PrimitiveCount")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def addPrimitive(self,arg0):  # 先定义函数 
		args = {
				"primitive":{"t": "IDrawPrimitive","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'AddPrimitive', 1, state)


	def clear(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clear', 0, state)


	def computeNormal(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'computeNormal', 0, state)


	def getPrimitive(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'GetPrimitive', 1, state)


	def insertPrimitive(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"primitive":{"t": "IDrawPrimitive","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'InsertPrimitive', 1, state)


	def removePrimitive(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"count":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'RemovePrimitive', 1, state)


	def setPrimitive(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"primitive":{"t": "IDrawPrimitive","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SetPrimitive', 1, state)

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
				super(IDrawGroup, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
