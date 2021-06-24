#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IReplicationFactory","F":"g"}}
class IReplicationFactory:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def createCheckIn(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"sourceDataSource":{"t": "IDataSource","v": arg0},
				"featureDataSetName":{"t": "S","v": arg1},
				"conflictDetectedType":{"t": "gviConflictDetectedType","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCheckIn', 1, state)


	def createCheckOut(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"destinationDataSource":{"t": "IDataSource","v": arg0},
				"sourceDataSource":{"t": "IDataSource","v": arg1},
				"featureDataSetName":{"t": "S","v": arg2},
				"conflictDetectedType":{"t": "gviConflictDetectedType","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCheckOut', 1, state)


	def createReplicationClass(self,arg0,arg1):  # 先定义函数 
		args = {
				"connection":{"t": "IConnectionInfo","v": arg0},
				"featureDataSetName":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createReplicationClass', 1, state)


	def undoCheckOut(self,arg0,arg1):  # 先定义函数 
		args = {
				"srcDS":{"t": "IDataSource","v": arg0},
				"featureDataSetName":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'undoCheckOut', 0, state)

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
