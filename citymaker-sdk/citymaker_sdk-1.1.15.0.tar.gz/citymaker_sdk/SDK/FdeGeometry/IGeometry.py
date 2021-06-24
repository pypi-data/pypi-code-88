#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"dimension":{"t":"gviGeometryDimension","v":0,
"F":"g"},"envelope":{"t":"IEnvelope","v":None,
"F":"g"},"geometryType":{"t":"gviGeometryType","v":0,
"F":"g"},"isEmpty":{"t":"bool","v":False,
"F":"g"},"isValid":{"t":"bool","v":False,
"F":"g"},"spatialCRS":{"t":"ISpatialCRS","v":None,
"F":"gs"},"vertexAttribute":{"t":"gviVertexAttribute","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometry","F":"g"}}
class IGeometry:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._dimension=args.get("dimension")
		self._envelope=args.get("envelope")
		self._geometryType=args.get("geometryType")
		self._isEmpty=args.get("isEmpty")
		self._isValid=args.get("isValid")
		self._spatialCRS=args.get("spatialCRS")
		self._vertexAttribute=args.get("vertexAttribute")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asBinary(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asBinary', 1, state)


	def asWKT(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asWKT', 1, state)


	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def clone2(self,arg0):  # 先定义函数 
		args = {
				"vertexAttr":{"t": "gviVertexAttribute","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'clone2', 1, state)


	def hasId(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'hasId', 1, state)


	def hasM(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'hasM', 1, state)


	def hasZ(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'hasZ', 1, state)


	def project(self,arg0):  # 先定义函数 
		args = {
				"sRSTarget":{"t": "ISpatialCRS","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'project', 1, state)


	def setEmpty(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setEmpty', 0, state)

	@property
	def dimension(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["dimension"]

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
	def geometryType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["geometryType"]

	@property
	def isEmpty(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEmpty"]

	@property
	def isValid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isValid"]

	@property
	def spatialCRS(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"spatialCRS",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"spatialCRS",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "spatialCRS", res)
		return PropsValueData["spatialCRS"]

	@spatialCRS.setter
	def spatialCRS(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "spatialCRS", val)
		args = {}
		args["spatialCRS"] = PropsTypeData.get("spatialCRS")
		args["spatialCRS"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"spatialCRS", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"spatialCRS",JsonData)

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
