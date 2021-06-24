#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"length":{"t":"double","v":0,
"F":"g"},"x":{"t":"double","v":0,
"F":"gs"},"y":{"t":"double","v":0,
"F":"gs"},"z":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IVector3","F":"g"}}
class IVector3:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._length=args.get("length")
		self._x=args.get("x")
		self._y=args.get("y")
		self._z=args.get("z")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def add(self,arg0):  # 先定义函数 
		args = {
				"r":{"t": "IVector3","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'add', 1, state)


	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def crossProduct(self,arg0):  # 先定义函数 
		args = {
				"r":{"t": "IVector3","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'crossProduct', 1, state)


	def dotProduct(self,arg0):  # 先定义函数 
		args = {
				"r":{"t": "IVector3","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'dotProduct', 1, state)


	def multiplyByScalar(self,arg0):  # 先定义函数 
		args = {
				"r":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'multiplyByScalar', 0, state)


	def normalize(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'normalize', 0, state)


	def set(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1},
				"z":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)


	def setByVector(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setByVector', 0, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'valid', 1, state)

	@property
	def length(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["length"]

	@property
	def x(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["x"]

	@x.setter
	def x(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "x", val)
		args = {}
		args["x"] = PropsTypeData.get("x")
		args["x"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"x", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"x",JsonData)

	@property
	def y(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["y"]

	@y.setter
	def y(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "y", val)
		args = {}
		args["y"] = PropsTypeData.get("y")
		args["y"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"y", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"y",JsonData)

	@property
	def z(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["z"]

	@z.setter
	def z(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "z", val)
		args = {}
		args["z"] = PropsTypeData.get("z")
		args["z"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"z", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"z",JsonData)

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
