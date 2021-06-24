#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISQLCheck","F":"g"}}
class ISQLCheck:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def checkSelectList(self,arg0):  # 先定义函数 
		args = {
				"selectList":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'checkSelectList', 1, state)


	def checkSQLStatement(self,arg0):  # 先定义函数 
		args = {
				"sql":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'checkSQLStatement', 1, state)


	def checkWhereClause(self,arg0):  # 先定义函数 
		args = {
				"whereClause":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'checkWhereClause', 1, state)

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
