#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"length":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDataCopy","F":"g"}}
class IDataCopy:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._length=args.get("length")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def copyClass(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"destDS":{"t": "IDataSource","v": arg0},
				"destFDS":{"t": "S","v": arg1},
				"destClassName":{"t": "S","v": arg2},
				"srcDS":{"t": "IDataSource","v": arg3},
				"srcFDS":{"t": "S","v": arg4},
				"srcClassName":{"t": "S","v": arg5},
				"parameters":{"t": "IDataCopyParam","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'copyClass', 1, state)


	def copyDataset(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"destDS":{"t": "IDataSource","v": arg0},
				"destFDS":{"t": "S","v": arg1},
				"srcDS":{"t": "IDataSource","v": arg2},
				"srcFDS":{"t": "S","v": arg3},
				"parameters":{"t": "IDataCopyParam","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'copyDataset', 1, state)


	def copySubType(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"destDS":{"t": "IDataSource","v": arg0},
				"destFDS":{"t": "S","v": arg1},
				"destClassName":{"t": "S","v": arg2},
				"destSubTypeField":{"t": "S","v": arg3},
				"srcDS":{"t": "IDataSource","v": arg4},
				"srcFDS":{"t": "S","v": arg5},
				"srcClassName":{"t": "S","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'copySubType', 1, state)


	def copyTable(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"destDS":{"t": "IDataSource","v": arg0},
				"destClassName":{"t": "S","v": arg1},
				"srcDS":{"t": "IDataSource","v": arg2},
				"srcFDS":{"t": "S","v": arg3},
				"srcClassName":{"t": "S","v": arg4},
				"parameters":{"t": "IDataCopyParam","v": arg5}
		}
		state = ""
		return CM.AddPrototype(self,args, 'copyTable', 1, state)

	@property
	def length(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["length"]

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
