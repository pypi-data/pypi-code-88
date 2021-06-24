#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.ITable import ITable
Props={"createTime":{"t":"DateTime","v":"",
"F":"g"},"customData":{"t":"IPropertySet","v":None,
"F":"gs"},"defaultSubTypeCode":{"t":"int","v":0,
"F":"gs"},"featureDataSet":{"t":"IFeatureDataSet","v":None,
"F":"g"},"guid":{"t":"Guid","v":"",
"F":"g"},"hasSubTypes":{"t":"bool","v":False,
"F":"g"},"id":{"t":"int","v":0,
"F":"g"},"lastUpdateTime":{"t":"DateTime","v":"",
"F":"g"},"lockType":{"t":"gviLockType","v":0,
"F":"gs"},"readOnly":{"t":"bool","v":False,
"F":"g"},"subTypeCount":{"t":"int","v":0,
"F":"g"},"subTypeFieldIndex":{"t":"int","v":0,
"F":"g"},"temporalManager":{"t":"ITemporalManager","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IObjectClass","F":"g"}}
#Events = {alias:{fn:null}description:{fn:null}fidFieldName:{fn:null}guidString:{fn:null}name:{fn:null}subTypeFieldName:{fn:null}temporalColumnName:{fn:null}}
class IObjectClass(ITable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._createTime=args.get("createTime")
		self._customData=args.get("customData")
		self._defaultSubTypeCode=args.get("defaultSubTypeCode")
		self._featureDataSet=args.get("featureDataSet")
		self._guid=args.get("guid")
		self._hasSubTypes=args.get("hasSubTypes")
		self._id=args.get("id")
		self._lastUpdateTime=args.get("lastUpdateTime")
		self._lockType=args.get("lockType")
		self._readOnly=args.get("readOnly")
		self._subTypeCount=args.get("subTypeCount")
		self._subTypeFieldIndex=args.get("subTypeFieldIndex")
		self._temporalManager=args.get("temporalManager")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addSubType(self,arg0):  # 先定义函数 
		args = {
				"subType":{"t": "ISubTypeInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addSubType', 0, state)


	def close(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'close', 0, state)


	def deleteSubType(self,arg0):  # 先定义函数 
		args = {
				"subTypeCode":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteSubType', 0, state)


	def disableAttachment(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'disableAttachment', 0, state)


	def disableTemporal(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'disableTemporal', 0, state)


	def enableAttachment(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'enableAttachment', 0, state)


	def enableTemporal(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"defaultBirthDatetime":{"t": "S","v": arg0},
				"birthDateColumn":{"t": "S","v": arg1},
				"deathDateColumn":{"t": "S","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'enableTemporal', 0, state)


	def getAttachmentManager(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getAttachmentManager', 1, state)


	def getLocks(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getLocks', 1, state)


	def getSubType(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSubType', 1, state)


	def hasAttachments(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'hasAttachments', 1, state)


	def hasTemporal(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'hasTemporal', 1, state)


	def modifySubType(self,arg0):  # 先定义函数 
		args = {
				"subType":{"t": "ISubTypeInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'modifySubType', 0, state)

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
	def defaultSubTypeCode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["defaultSubTypeCode"]

	@defaultSubTypeCode.setter
	def defaultSubTypeCode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "defaultSubTypeCode", val)
		args = {}
		args["defaultSubTypeCode"] = PropsTypeData.get("defaultSubTypeCode")
		args["defaultSubTypeCode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"defaultSubTypeCode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"defaultSubTypeCode",JsonData)

	@property
	def featureDataSet(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"featureDataSet",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"featureDataSet",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "featureDataSet", res)
		return PropsValueData["featureDataSet"]

	@property
	def guid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["guid"]

	@property
	def hasSubTypes(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasSubTypes"]

	@property
	def id(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["id"]

	@property
	def lastUpdateTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lastUpdateTime"]

	@property
	def lockType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lockType"]

	@lockType.setter
	def lockType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "lockType", val)
		args = {}
		args["lockType"] = PropsTypeData.get("lockType")
		args["lockType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"lockType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"lockType",JsonData)

	@property
	def readOnly(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["readOnly"]

	@property
	def subTypeCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["subTypeCount"]

	@property
	def subTypeFieldIndex(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["subTypeFieldIndex"]

	@property
	def temporalManager(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"temporalManager",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"temporalManager",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "temporalManager", res)
		return PropsValueData["temporalManager"]

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
