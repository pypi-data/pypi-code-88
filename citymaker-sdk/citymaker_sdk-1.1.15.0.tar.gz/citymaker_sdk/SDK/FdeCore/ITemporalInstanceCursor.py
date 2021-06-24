#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITemporalInstanceCursor","F":"g"}}
class ITemporalInstanceCursor:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def delete(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'delete', 0, state)


	def nextInstance(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'nextInstance', 1, state)


	def update(self,arg0):  # 先定义函数 
		args = {
				"row":{"t": "IRowBuffer","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'update', 0, state)

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
