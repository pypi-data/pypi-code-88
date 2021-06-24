#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"storeLocation":{"t":"gviResultStoreLocation","v":0,
"F":"gs"},"subFields":{"t":"string []","v":"",
"F":"gs"},"tables":{"t":"string []","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IQueryDef","F":"g"}}
#Events = {postfixClause:{fn:null}prefixClause:{fn:null}whereClause:{fn:null}}
class IQueryDef:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._storeLocation=args.get("storeLocation")
		self._subFields=args.get("subFields")
		self._tables=args.get("tables")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addSubField(self,arg0):  # 先定义函数 
		args = {
				"fieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addSubField', 1, state)


	def execute(self,arg0):  # 先定义函数 
		args = {
				"reuseRow":{"t": "B","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'execute', 1, state)


	def executeQuery(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"sql":{"t": "S","v": arg0},
				"params":{"t": "<O>","v": arg1},
				"bulkSize":{"t": "N","v": arg2},
				"location":{"t": "gviResultStoreLocation","v": arg3},
				"reuseRow":{"t": "B","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'executeQuery', 1, state)

	@property
	def storeLocation(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["storeLocation"]

	@storeLocation.setter
	def storeLocation(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "storeLocation", val)
		args = {}
		args["storeLocation"] = PropsTypeData.get("storeLocation")
		args["storeLocation"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"storeLocation", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"storeLocation",JsonData)

	@property
	def subFields(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["subFields"]

	@subFields.setter
	def subFields(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "subFields", val)
		args = {}
		args["subFields"] = PropsTypeData.get("subFields")
		args["subFields"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"subFields", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"subFields",JsonData)

	@property
	def tables(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tables"]

	@tables.setter
	def tables(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tables", val)
		args = {}
		args["tables"] = PropsTypeData.get("tables")
		args["tables"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tables", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tables",JsonData)

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
