#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.IDomain import IDomain
Props={"codeCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICodedValueDomain","F":"g"}}
class ICodedValueDomain(IDomain):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._codeCount=args.get("codeCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addCode(self,arg0,arg1):  # 先定义函数 
		args = {
				"val":{"t": "O","v": arg0},
				"name":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'addCode', 0, state)


	def deleteCode(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "O","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteCode', 0, state)


	def getCodeName(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCodeName', 1, state)


	def getCodeNameByValue(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "O","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCodeNameByValue', 1, state)


	def getCodeValue(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCodeValue', 1, state)

	@property
	def codeCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["codeCount"]

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
