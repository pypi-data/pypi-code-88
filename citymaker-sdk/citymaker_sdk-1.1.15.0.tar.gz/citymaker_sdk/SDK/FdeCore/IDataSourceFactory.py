#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDataSourceFactory","F":"g"}}
class IDataSourceFactory:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def createDataSource(self,arg0,arg1):  # 先定义函数 
		args = {
				"connectionInfo":{"t": "IConnectionInfo","v": arg0},
				"repository":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createDataSource', 1, state)


	def getDataBaseNames(self,arg0,arg1):  # 先定义函数 
		args = {
				"connectionInfo":{"t": "IConnectionInfo","v": arg0},
				"onlyFdb":{"t": "B","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getDataBaseNames', 1, state)


	def hasDataSource(self,arg0):  # 先定义函数 
		args = {
				"connectionInfo":{"t": "IConnectionInfo","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'hasDataSource', 1, state)


	def hasDataSourceByString(self,arg0):  # 先定义函数 
		args = {
				"connectionString":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'hasDataSourceByString', 1, state)


	def openDataSource(self,arg0):  # 先定义函数 
		args = {
				"connectionInfo":{"t": "IConnectionInfo","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openDataSource', 1, state)


	def openDataSourceByString(self,arg0):  # 先定义函数 
		args = {
				"connectionString":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openDataSourceByString', 1, state)


	def openSelectFeatureClass(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'openSelectFeatureClass', 1, state)


	def setResourceDataSet(self,arg0,arg1):  # 先定义函数 
		args = {
				"connectInfoStr":{"t": "S","v": arg0},
				"datasetName":{"t": "S","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'setResourceDataSet', 1, state)

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
