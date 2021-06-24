#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"count":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPropertySet","F":"g"}}
class IPropertySet:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._count=args.get("count")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getAllKeys(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getAllKeys', 1, state)


	def getProperty(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getProperty', 1, state)


	def setProperty(self,arg0,arg1):  # 先定义函数 
		args = {
				"key":{"t": "S","v": arg0},
				"value":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setProperty', 0, state)

	@property
	def count(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["count"]

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
