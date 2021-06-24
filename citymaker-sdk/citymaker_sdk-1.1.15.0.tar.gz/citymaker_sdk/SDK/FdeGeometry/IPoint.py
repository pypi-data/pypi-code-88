#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IGeometry import IGeometry
Props={"id":{"t":"double","v":0,
"F":"gs"},"position":{"t":"IVector3","v":None,
"F":"gs"},"x":{"t":"double","v":0,
"F":"gs"},"y":{"t":"double","v":0,
"F":"gs"},"z":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPoint","F":"g"}}
#Events = {m:{fn:null}}
class IPoint(IGeometry):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._id=args.get("id")
		self._position=args.get("position")
		self._x=args.get("x")
		self._y=args.get("y")
		self._z=args.get("z")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def setCoords(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1},
				"z":{"t": "N","v": arg2},
				"m":{"t": "N","v": arg3},
				"id":{"t": "N","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCoords', 0, state)

	@property
	def id(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["id"]

	@id.setter
	def id(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "id", val)
		args = {}
		args["id"] = PropsTypeData.get("id")
		args["id"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"id", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"id",JsonData)

	@property
	def position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"position",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "position", res)
		return PropsValueData["position"]

	@position.setter
	def position(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "position", val)
		args = {}
		args["position"] = PropsTypeData.get("position")
		args["position"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"position", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",JsonData)

	@property
	def x(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["x"]

	@x.setter
	def x(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "x", val)
		args = {}
		args["x"] = PropsTypeData.get("x")
		args["x"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"x", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"x",JsonData)

	@property
	def y(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["y"]

	@y.setter
	def y(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "y", val)
		args = {}
		args["y"] = PropsTypeData.get("y")
		args["y"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"y", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"y",JsonData)

	@property
	def z(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["z"]

	@z.setter
	def z(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "z", val)
		args = {}
		args["z"] = PropsTypeData.get("z")
		args["z"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"z", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"z",JsonData)

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
