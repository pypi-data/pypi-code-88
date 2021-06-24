#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.FdeCore.IResourceManager import IResourceManager
Props={"createTime":{"t":"DateTime","v":"",
"F":"g"},"customData":{"t":"IPropertySet","v":None,
"F":"gs"},"dataSource":{"t":"IDataSource","v":None,
"F":"g"},"guid":{"t":"Guid","v":"",
"F":"g"},"id":{"t":"int","v":0,
"F":"g"},"isCheckOut":{"t":"bool","v":False,
"F":"g"},"isCheckOutAsMaster":{"t":"bool","v":False,
"F":"g"},"lastUpdateTime":{"t":"DateTime","v":"",
"F":"g"},"spatialReference":{"t":"ISpatialCRS","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureDataSet","F":"g"}}
#Events = {alias:{fn:null}description:{fn:null}guidString:{fn:null}name:{fn:null}}
class IFeatureDataSet(IResourceManager):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.createTime=args.get("createTime")
		self.customData=args.get("customData")
		self.dataSource=args.get("dataSource")
		self.guid=args.get("guid")
		self.id=args.get("id")
		self.isCheckOut=args.get("isCheckOut")
		self.isCheckOutAsMaster=args.get("isCheckOutAsMaster")
		self.lastUpdateTime=args.get("lastUpdateTime")
		self.spatialReference=args.get("spatialReference")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def getFeaturesFromBaseLyr2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"fc_name":{"t": "S","v": arg0},
				"geoType":{"t": "gviGeometryType","v": arg1},
				"spatialRel":{"t": "gviSpatialRel","v": arg2},
				"position":{"t": "<IVector3>","v": arg3}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getFeaturesFromBaseLyr2', 1, state)


	def getFeatureQuery(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc_name":{"t": "S","v": arg0},
				"queryFilter":{"t": "S","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getFeatureQuery', 1, state)


	def createFeatureClass(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"fields":{"t": "IFieldInfoCollection","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFeatureClass', 1, state)


	def createObjectClass(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"fields":{"t": "IFieldInfoCollection","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createObjectClass', 1, state)


	def deleteByName(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteByName', 1, state)


	def getNamesByType(self,arg0):  # 先定义函数 
		args = {
				"dataSetType":{"t": "gviDataSetType","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getNamesByType', 1, state)


	def getNetworkManager(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getNetworkManager', 1, state)


	def openFeatureClass(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openFeatureClass', 1, state)


	def openObjectClass(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openObjectClass', 1, state)

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
				super(IFeatureDataSet, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
