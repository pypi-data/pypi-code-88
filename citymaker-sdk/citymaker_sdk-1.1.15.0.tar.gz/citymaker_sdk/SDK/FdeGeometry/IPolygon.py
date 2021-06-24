#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ISurfacePatch import ISurfacePatch
Props={"exteriorRing":{"t":"IRing","v":None,
"F":"g"},"interiorRingCount":{"t":"int","v":0,
"F":"g"},"isCoplanar":{"t":"bool","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPolygon","F":"g"}}
class IPolygon(ISurfacePatch):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._exteriorRing=args.get("exteriorRing")
		self._interiorRingCount=args.get("interiorRingCount")
		self._isCoplanar=args.get("isCoplanar")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addInteriorRing(self,arg0):  # 先定义函数 
		args = {
				"interiorRing":{"t": "IRing","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addInteriorRing', 1, state)


	def close(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'close', 0, state)


	def deleteInteriorRing(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteInteriorRing', 1, state)


	def getInteriorRing(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getInteriorRing', 1, state)


	def queryNormal(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'queryNormal', 1, state)

	@property
	def exteriorRing(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"exteriorRing",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"exteriorRing",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "exteriorRing", res)
		return PropsValueData["exteriorRing"]

	@property
	def interiorRingCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["interiorRingCount"]

	@property
	def isCoplanar(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isCoplanar"]

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
