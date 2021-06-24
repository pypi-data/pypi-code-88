#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.createTime=args.get("createTime")
		self.customData=args.get("customData")
		self.defaultSubTypeCode=args.get("defaultSubTypeCode")
		self.featureDataSet=args.get("featureDataSet")
		self.guid=args.get("guid")
		self.hasSubTypes=args.get("hasSubTypes")
		self.id=args.get("id")
		self.lastUpdateTime=args.get("lastUpdateTime")
		self.lockType=args.get("lockType")
		self.readOnly=args.get("readOnly")
		self.subTypeCount=args.get("subTypeCount")
		self.subTypeFieldIndex=args.get("subTypeFieldIndex")
		self.temporalManager=args.get("temporalManager")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				super(IObjectClass, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
