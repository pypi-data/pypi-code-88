#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"currentId":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITemporalCursor","F":"g"}}
class ITemporalCursor:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._currentId=args.get("currentId")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def dead(self,arg0):  # 先定义函数 
		args = {
				"deathDatetime":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'dead', 0, state)


	def getTemporalInstances(self,arg0):  # 先定义函数 
		args = {
				"reuseTemporalInstance":{"t": "B","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getTemporalInstances', 1, state)


	def insert(self,arg0,arg1):  # 先定义函数 
		args = {
				"startDatetime":{"t": "S","v": arg0},
				"row":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'insert', 0, state)


	def moveNext(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'moveNext', 1, state)


	def resetBirthDatetime(self,arg0):  # 先定义函数 
		args = {
				"newBirthDatetime":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'resetBirthDatetime', 0, state)

	@property
	def currentId(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["currentId"]

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
