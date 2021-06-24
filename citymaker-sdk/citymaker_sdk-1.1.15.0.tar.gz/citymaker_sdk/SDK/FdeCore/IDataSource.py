#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"connectionInfo":{"t":"IConnectionInfo","v":None,
"F":"g"},"createTime":{"t":"DateTime","v":"",
"F":"g"},"customData":{"t":"IPropertySet","v":None,
"F":"gs"},"databaseTime":{"t":"DateTime","v":"",
"F":"g"},"guid":{"t":"Guid","v":"",
"F":"g"},"isEditing":{"t":"bool","v":False,
"F":"g"},"sQLCheck":{"t":"ISQLCheck","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDataSource","F":"g"}}
#Events = {description:{fn:null}fdeSchemaPrefix:{fn:null}guidString:{fn:null}}
class IDataSource:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._connectionInfo=args.get("connectionInfo")
		self._createTime=args.get("createTime")
		self._customData=args.get("customData")
		self._databaseTime=args.get("databaseTime")
		self._guid=args.get("guid")
		self._isEditing=args.get("isEditing")
		self._sQLCheck=args.get("sQLCheck")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addDomain(self,arg0):  # 先定义函数 
		args = {
				"domain":{"t": "IDomain","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addDomain', 0, state)


	def changePassword(self,arg0):  # 先定义函数 
		args = {
				"newPassword":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'changePassword', 0, state)


	def close(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'close', 0, state)


	def createFeatureDataset(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"spatialCRS":{"t": "ISpatialCRS","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFeatureDataset', 1, state)


	def createQueryDef(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createQueryDef', 1, state)


	def createTable(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"tableName":{"t": "S","v": arg0},
				"primaryKey":{"t": "S","v": arg1},
				"fields":{"t": "IFieldInfoCollection","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTable', 1, state)


	def deleteDomain(self,arg0):  # 先定义函数 
		args = {
				"domain":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteDomain', 0, state)


	def deleteFeatureDataset(self,arg0):  # 先定义函数 
		args = {
				"featureDatasetName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteFeatureDataset', 0, state)


	def deleteTableByName(self,arg0):  # 先定义函数 
		args = {
				"tableName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteTableByName', 0, state)


	def escapeObjectName(self,arg0):  # 先定义函数 
		args = {
				"objectName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'escapeObjectName', 1, state)


	def executeUpdate(self,arg0):  # 先定义函数 
		args = {
				"sql":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'executeUpdate', 0, state)


	def getDomainByName(self,arg0):  # 先定义函数 
		args = {
				"domain":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getDomainByName', 1, state)


	def getDomainNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getDomainNames', 1, state)


	def getFDBVersion(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFDBVersion', 1, state)


	def getFeatureDatasetNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFeatureDatasetNames', 1, state)


	def getLocks(self,arg0):  # 先定义函数 
		args = {
				"classId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getLocks', 1, state)


	def getTableNames(self,arg0):  # 先定义函数 
		args = {
				"includeFdbTable":{"t": "B","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getTableNames', 1, state)


	def hasCapability(self,arg0):  # 先定义函数 
		args = {
				"capability":{"t": "gviFdbCapability","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'hasCapability', 1, state)


	def modifyDomain(self,arg0):  # 先定义函数 
		args = {
				"domain":{"t": "IDomain","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'modifyDomain', 0, state)


	def openFeatureDataset(self,arg0):  # 先定义函数 
		args = {
				"featureDataSetName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openFeatureDataset', 1, state)


	def openTable(self,arg0):  # 先定义函数 
		args = {
				"tableName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openTable', 1, state)


	def ping(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'ping', 1, state)


	def queryDomainRefFields(self,arg0):  # 先定义函数 
		args = {
				"domainId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'queryDomainRefFields', 1, state)


	def reOpen(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'reOpen', 0, state)


	def startEditing(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'startEditing', 0, state)


	def stopEditing(self,arg0):  # 先定义函数 
		args = {
				"save":{"t": "B","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'stopEditing', 0, state)

	@property
	def connectionInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"connectionInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"connectionInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "connectionInfo", res)
		return PropsValueData["connectionInfo"]

	@property
	def createTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["createTime"]

	@property
	def customData(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"customData",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"customData",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "customData", res)
		return PropsValueData["customData"]

	@customData.setter
	def customData(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "customData", val)
		args = {}
		args["customData"] = PropsTypeData.get("customData")
		args["customData"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"customData", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"customData",JsonData)

	@property
	def databaseTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["databaseTime"]

	@property
	def guid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["guid"]

	@property
	def isEditing(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEditing"]

	@property
	def sQLCheck(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"sQLCheck",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"sQLCheck",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "sQLCheck", res)
		return PropsValueData["sQLCheck"]

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
