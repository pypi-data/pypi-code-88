#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"avgNumPoints":{"t":"int","v":0,
"F":"g"},"envelope":{"t":"IEnvelope","v":None,
"F":"g"},"geometryColumnType":{"t":"gviGeometryColumnType","v":0,
"F":"gs"},"hasId":{"t":"bool","v":False,
"F":"gs"},"hasM":{"t":"bool","v":False,
"F":"gs"},"hasRenderIndex":{"t":"bool","v":False,
"F":"g"},"hasSpatialIndex":{"t":"bool","v":False,
"F":"g"},"hasZ":{"t":"bool","v":False,
"F":"gs"},"maxM":{"t":"double","v":0,
"F":"gs"},"minM":{"t":"double","v":0,
"F":"gs"},"vertexAttribute":{"t":"gviVertexAttribute","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometryDef","F":"g"}}
class IGeometryDef:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._avgNumPoints=args.get("avgNumPoints")
		self._envelope=args.get("envelope")
		self._geometryColumnType=args.get("geometryColumnType")
		self._hasId=args.get("hasId")
		self._hasM=args.get("hasM")
		self._hasRenderIndex=args.get("hasRenderIndex")
		self._hasSpatialIndex=args.get("hasSpatialIndex")
		self._hasZ=args.get("hasZ")
		self._maxM=args.get("maxM")
		self._minM=args.get("minM")
		self._vertexAttribute=args.get("vertexAttribute")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)

	@property
	def avgNumPoints(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["avgNumPoints"]

	@property
	def envelope(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"envelope",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"envelope",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "envelope", res)
		return PropsValueData["envelope"]

	@property
	def geometryColumnType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["geometryColumnType"]

	@geometryColumnType.setter
	def geometryColumnType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "geometryColumnType", val)
		args = {}
		args["geometryColumnType"] = PropsTypeData.get("geometryColumnType")
		args["geometryColumnType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"geometryColumnType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometryColumnType",JsonData)

	@property
	def hasId(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasId"]

	@hasId.setter
	def hasId(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "hasId", val)
		args = {}
		args["hasId"] = PropsTypeData.get("hasId")
		args["hasId"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"hasId", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"hasId",JsonData)

	@property
	def hasM(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasM"]

	@hasM.setter
	def hasM(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "hasM", val)
		args = {}
		args["hasM"] = PropsTypeData.get("hasM")
		args["hasM"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"hasM", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"hasM",JsonData)

	@property
	def hasRenderIndex(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasRenderIndex"]

	@property
	def hasSpatialIndex(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasSpatialIndex"]

	@property
	def hasZ(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasZ"]

	@hasZ.setter
	def hasZ(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "hasZ", val)
		args = {}
		args["hasZ"] = PropsTypeData.get("hasZ")
		args["hasZ"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"hasZ", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"hasZ",JsonData)

	@property
	def maxM(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxM"]

	@maxM.setter
	def maxM(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxM", val)
		args = {}
		args["maxM"] = PropsTypeData.get("maxM")
		args["maxM"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxM", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxM",JsonData)

	@property
	def minM(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minM"]

	@minM.setter
	def minM(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minM", val)
		args = {}
		args["minM"] = PropsTypeData.get("minM")
		args["minM"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minM", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minM",JsonData)

	@property
	def vertexAttribute(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["vertexAttribute"]

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
