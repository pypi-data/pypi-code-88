#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.connectionInfo=args.get("connectionInfo")
		self.createTime=args.get("createTime")
		self.customData=args.get("customData")
		self.databaseTime=args.get("databaseTime")
		self.guid=args.get("guid")
		self.isEditing=args.get("isEditing")
		self.sQLCheck=args.get("sQLCheck")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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

	def __getattr__(self,name):
		if name in Props:
			attrVal=Props[name]
			if name =="_HashCode":
				return CM.dict_get(attrVal, "v", None)
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("g") > -1:
				if CP.ClassFN.get(t) is not None and "PickResult" not in Props["propertyType"]["v"] and name != "propertyType":
					PropsTypeData = CM.getPropsTypeData(self._HashCode)
					PropsValueData = CM.getPropsValueData(self._HashCode)
					jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),name,None)
					res=socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,jsonData)
					CM.addPropsValue(PropsValueData["_HashCode"], name, res)
					return PropsValueData[name]
				else:
					PropsValueData = CM.getPropsValueData(self._HashCode)
					if name == "fullScreen":
						res=CM.isFull()
					CM.addPropsValue(PropsValueData.get("_HashCode"), name, res)
					return PropsValueData[name]

	def __setattr__(self,name,value):
		if name in Props:
			attrVal=Props[name]
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("s") > -1:
				if name =="_HashCode":
					CM.dict_set(attrVal, "F", value)
					return
				PropsTypeData = CM.getPropsTypeData(self._HashCode)
				PropsValueData = CM.getPropsValueData(self._HashCode)
				CM.addPropsValue(PropsValueData.get("_HashCode"), name, value)
				if name == "fullScreen":
					res=CM.isFull()
					return
				args = {}
				args[name] = PropsTypeData.get(name)
				args[name]["v"] = value
				JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),name, args)
				socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,JsonData)
				super(IDataSource, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
