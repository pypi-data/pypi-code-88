#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"length":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IBinaryBuffer","F":"g"}}
class IBinaryBuffer:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._length=args.get("length")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asString(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asString', 1, state)


	def asStringBase64(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asStringBase64', 1, state)


	def fromString(self,arg0):  # 先定义函数 
		args = {
				"stringValue":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'fromString', 0, state)


	def fromStringBase64(self,arg0):  # 先定义函数 
		args = {
				"stringValue":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'fromStringBase64', 0, state)


	def asByteArray(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asByteArray', 1, state)


	def fromByteArray(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "byte[]","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'fromByteArray', 1, state)

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
