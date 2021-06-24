#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"lastInsertId":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFdeCursor","F":"g"}}
class IFdeCursor:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._lastInsertId=args.get("lastInsertId")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def close(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'close', 0, state)


	def deleteRow(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'deleteRow', 0, state)


	def findField(self,arg0):  # 先定义函数 
		args = {
				"fieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'findField', 1, state)


	def flush(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'flush', 0, state)


	def getFields(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFields', 1, state)


	def insertRow(self,arg0):  # 先定义函数 
		args = {
				"rb":{"t": "IRowBuffer","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'insertRow', 0, state)


	def nextRow(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'nextRow', 1, state)


	def updateRow(self,arg0):  # 先定义函数 
		args = {
				"row":{"t": "IRowBuffer","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'updateRow', 0, state)

	@property
	def lastInsertId(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lastInsertId"]

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
