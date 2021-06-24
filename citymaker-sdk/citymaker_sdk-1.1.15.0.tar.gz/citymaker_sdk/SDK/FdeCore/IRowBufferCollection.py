#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"count":{"t":"int","v":0,
"F":"g"},"isEmpty":{"t":"bool","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRowBufferCollection","F":"g"}}
class IRowBufferCollection:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._count=args.get("count")
		self._isEmpty=args.get("isEmpty")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def add(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IRowBuffer","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'add', 0, state)


	def clear(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clear', 0, state)


	def get(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'get', 1, state)


	def removeAt(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'removeAt', 0, state)


	def set(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"val":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)


	def trimToSize(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'trimToSize', 0, state)

	@property
	def count(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["count"]

	@property
	def isEmpty(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEmpty"]

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
