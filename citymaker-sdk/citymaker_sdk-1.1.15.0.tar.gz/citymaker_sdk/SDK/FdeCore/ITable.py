#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"dataSource":{"t":"IDataSource","v":None,
"F":"g"},"primaryKeys":{"t":"string []","v":"",
"F":"g"},"type":{"t":"gviDataSetType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITable","F":"g"}}
#Events = {tableName:{fn:null}}
class ITable:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._dataSource=args.get("dataSource")
		self._primaryKeys=args.get("primaryKeys")
		self._type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addDbIndex(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "IDbIndexInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addDbIndex', 0, state)


	def addField(self,arg0):  # 先定义函数 
		args = {
				"field":{"t": "IFieldInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addField', 0, state)


	def asyncSearch(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"customData":{"t": "S","v": arg0},
				"filter":{"t": "IQueryFilter","v": arg1},
				"reuseRow":{"t": "B","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'asyncSearch', 1, state)


	def createRowBuffer(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createRowBuffer', 1, state)


	def delete(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'delete', 1, state)


	def deleteDbIndex(self,arg0):  # 先定义函数 
		args = {
				"indexName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteDbIndex', 0, state)


	def deleteField(self,arg0):  # 先定义函数 
		args = {
				"fieldName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteField', 0, state)


	def deleteRow(self,arg0):  # 先定义函数 
		args = {
				"id":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteRow', 0, state)


	def getCount(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCount', 1, state)


	def getDbIndexInfos(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getDbIndexInfos', 1, state)


	def getFields(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFields', 1, state)


	def getRow(self,arg0):  # 先定义函数 
		args = {
				"id":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRow', 1, state)


	def getRows(self,arg0,arg1):  # 先定义函数 
		args = {
				"ids":{"t": "<N>","v": arg0},
				"reuseRow":{"t": "B","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRows', 1, state)


	def insert(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'insert', 1, state)


	def modifyField(self,arg0):  # 先定义函数 
		args = {
				"field":{"t": "IFieldInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'modifyField', 0, state)


	def rebuildDbIndex(self,arg0):  # 先定义函数 
		args = {
				"indexName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'rebuildDbIndex', 0, state)


	def search(self,arg0,arg1):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0},
				"reuseRow":{"t": "B","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'search', 1, state)


	def store(self,arg0):  # 先定义函数 
		args = {
				"row":{"t": "IRowBuffer","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'store', 0, state)


	def truncate(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'truncate', 0, state)


	def update(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'update', 1, state)


	def updateRows(self,arg0,arg1):  # 先定义函数 
		args = {
				"rows":{"t": "IRowBufferCollection","v": arg0},
				"updateNotChangeValue":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'updateRows', 0, state)

	@property
	def dataSource(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"dataSource",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"dataSource",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "dataSource", res)
		return PropsValueData["dataSource"]

	@property
	def primaryKeys(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["primaryKeys"]

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

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
