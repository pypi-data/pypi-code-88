#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IGeometry import IGeometry
Props={"centroid":{"t":"IPoint","v":None,
"F":"g"},"isClosed":{"t":"bool","v":False,
"F":"g"},"pointOnSurface":{"t":"IPoint","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISurface","F":"g"}}
class ISurface(IGeometry):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._centroid=args.get("centroid")
		self._isClosed=args.get("isClosed")
		self._pointOnSurface=args.get("pointOnSurface")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def area(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'area', 1, state)


	def getBoundary(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getBoundary', 1, state)


	def isPointOnSurface(self,arg0):  # 先定义函数 
		args = {
				"pointValue":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isPointOnSurface', 1, state)

	@property
	def centroid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"centroid",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"centroid",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "centroid", res)
		return PropsValueData["centroid"]

	@property
	def isClosed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isClosed"]

	@property
	def pointOnSurface(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"pointOnSurface",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pointOnSurface",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "pointOnSurface", res)
		return PropsValueData["pointOnSurface"]

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
