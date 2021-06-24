#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IUtility","F":"g"}}
class IUtility:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def createFixedBillboard(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"text":{"t": "S","v": arg0},
				"textAttribute":{"t": "ITextAttribute","v": arg1},
				"height":{"t": "N","v": arg2},
				"width":{"t": "N","v": arg3},
				"doubleFace":{"t": "B","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFixedBillboard', 1, state)

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
