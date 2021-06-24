#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"data":{"t":"IBinaryBuffer","v":None,
"F":"gs"},"dataLength":{"t":"int","v":0,
"F":"g"},"featureId":{"t":"int","v":0,
"F":"gs"},"guid":{"t":"Guid","v":"",
"F":"g"},"id":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IAttachment","F":"g"}}
#Events = {mimeType:{fn:null}name:{fn:null}}
class IAttachment:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._data=args.get("data")
		self._dataLength=args.get("dataLength")
		self._featureId=args.get("featureId")
		self._guid=args.get("guid")
		self._id=args.get("id")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def data(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"data",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"data",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "data", res)
		return PropsValueData["data"]

	@data.setter
	def data(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "data", val)
		args = {}
		args["data"] = PropsTypeData.get("data")
		args["data"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"data", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"data",JsonData)

	@property
	def dataLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["dataLength"]

	@property
	def featureId(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["featureId"]

	@featureId.setter
	def featureId(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "featureId", val)
		args = {}
		args["featureId"] = PropsTypeData.get("featureId")
		args["featureId"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"featureId", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"featureId",JsonData)

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
