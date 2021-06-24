#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"completeMapFactor":{"t":"float","v":0.5,
"F":"gs"},"isEmpty":{"t":"bool","v":False,
"F":"g"},"primitiveCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDrawGroup","F":"g"}}
#Events = {completeMapTextureName:{fn:null}lightMapTextureName:{fn:null}}
class IDrawGroup:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._completeMapFactor=args.get("completeMapFactor")
		self._isEmpty=args.get("isEmpty")
		self._primitiveCount=args.get("primitiveCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addPrimitive(self,arg0):  # 先定义函数 
		args = {
				"primitive":{"t": "IDrawPrimitive","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addPrimitive', 1, state)


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
		return CM.AddPrototype(self,args, 'getPrimitive', 1, state)


	def insertPrimitive(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"primitive":{"t": "IDrawPrimitive","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertPrimitive', 1, state)


	def removePrimitive(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"count":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'removePrimitive', 1, state)


	def setPrimitive(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"primitive":{"t": "IDrawPrimitive","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setPrimitive', 1, state)

	@property
	def completeMapFactor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["completeMapFactor"]

	@completeMapFactor.setter
	def completeMapFactor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "completeMapFactor", val)
		args = {}
		args["completeMapFactor"] = PropsTypeData.get("completeMapFactor")
		args["completeMapFactor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"completeMapFactor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"completeMapFactor",JsonData)

	@property
	def isEmpty(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEmpty"]

	@property
	def primitiveCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["primitiveCount"]

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
