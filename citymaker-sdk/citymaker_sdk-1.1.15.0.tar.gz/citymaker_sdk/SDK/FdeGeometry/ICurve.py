#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IGeometry import IGeometry
Props={"endPoint":{"t":"IPoint","v":None,
"F":"gs"},"isClosed":{"t":"bool","v":False,
"F":"g"},"length":{"t":"double","v":0,
"F":"g"},"midpoint":{"t":"IPoint","v":None,
"F":"g"},"startPoint":{"t":"IPoint","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICurve","F":"g"}}
class ICurve(IGeometry):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._endPoint=args.get("endPoint")
		self._isClosed=args.get("isClosed")
		self._length=args.get("length")
		self._midpoint=args.get("midpoint")
		self._startPoint=args.get("startPoint")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def reverseOrientation(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'reverseOrientation', 0, state)

	@property
	def endPoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"endPoint",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"endPoint",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "endPoint", res)
		return PropsValueData["endPoint"]

	@endPoint.setter
	def endPoint(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "endPoint", val)
		args = {}
		args["endPoint"] = PropsTypeData.get("endPoint")
		args["endPoint"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"endPoint", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"endPoint",JsonData)

	@property
	def isClosed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isClosed"]

	@property
	def length(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["length"]

	@property
	def midpoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"midpoint",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"midpoint",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "midpoint", res)
		return PropsValueData["midpoint"]

	@property
	def startPoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"startPoint",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"startPoint",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "startPoint", res)
		return PropsValueData["startPoint"]

	@startPoint.setter
	def startPoint(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "startPoint", val)
		args = {}
		args["startPoint"] = PropsTypeData.get("startPoint")
		args["startPoint"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"startPoint", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"startPoint",JsonData)

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
