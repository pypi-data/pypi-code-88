#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"infinityDatetime":{"t":"DateTime","v":"",
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITemporalManager","F":"g"}}
class ITemporalManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._infinityDatetime=args.get("infinityDatetime")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def dead(self,arg0,arg1):  # 先定义函数 
		args = {
				"fid":{"t": "N","v": arg0},
				"deathDatetime":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'dead', 0, state)


	def getKeyDatetimes(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getKeyDatetimes', 1, state)


	def insert(self,arg0,arg1):  # 先定义函数 
		args = {
				"birthDate":{"t": "S","v": arg0},
				"row":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insert', 1, state)


	def search(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "ITemporalFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'search', 1, state)

	@property
	def infinityDatetime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["infinityDatetime"]

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
