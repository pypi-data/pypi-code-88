#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
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
		self._createTime=args.get("createTime")
		self._customData=args.get("customData")
		self._dataSource=args.get("dataSource")
		self._guid=args.get("guid")
		self._id=args.get("id")
		self._isCheckOut=args.get("isCheckOut")
		self._isCheckOutAsMaster=args.get("isCheckOutAsMaster")
		self._lastUpdateTime=args.get("lastUpdateTime")
		self._spatialReference=args.get("spatialReference")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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
	def guid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["guid"]

	@property
	def id(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["id"]

	@property
	def isCheckOut(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isCheckOut"]

	@property
	def isCheckOutAsMaster(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isCheckOutAsMaster"]

	@property
	def lastUpdateTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["lastUpdateTime"]

	@property
	def spatialReference(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"spatialReference",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"spatialReference",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "spatialReference", res)
		return PropsValueData["spatialReference"]

	@spatialReference.setter
	def spatialReference(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "spatialReference", val)
		args = {}
		args["spatialReference"] = PropsTypeData.get("spatialReference")
		args["spatialReference"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"spatialReference", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"spatialReference",JsonData)

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
