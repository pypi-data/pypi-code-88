#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"array":{"t":"Array","v":None,
"F":"gs"},"isEmpty":{"t":"bool","v":None,
"F":"g"},"length":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDoubleArray","F":"g"}}
class IDoubleArray:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._array=args.get("array")
		self._isEmpty=args.get("isEmpty")
		self._length=args.get("length")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def append(self,arg0):  # 先定义函数 
		args = {
				"value":{"t": "Number","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'append', 0, state)


	def clear(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clear', 0, state)


	def get(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "Number","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'get', 1, state)


	def set(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "Number","v": arg0},
				"newVal":{"t": "Number","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)

	@property
	def array(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["array"]

	@array.setter
	def array(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "array", val)
		args = {}
		args["array"] = PropsTypeData.get("array")
		args["array"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"array", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"array",JsonData)

	@property
	def isEmpty(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEmpty"]

	@property
	def length(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["length"]

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
