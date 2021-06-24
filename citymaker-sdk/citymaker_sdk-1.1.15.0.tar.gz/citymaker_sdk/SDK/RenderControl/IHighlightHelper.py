#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"color":{"t":"Color","v":"",
"F":"gs"},"maxZ":{"t":"double","v":10000,
"F":"gs"},"minZ":{"t":"double","v":-10000,
"F":"gs"},"visibleMask":{"t":"byte","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IHighlightHelper","F":"g"}}
class IHighlightHelper:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._color=args.get("color")
		self._maxZ=args.get("maxZ")
		self._minZ=args.get("minZ")
		self._visibleMask=args.get("visibleMask")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getRegion(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRegion', 1, state)


	def setCircleRegion(self,arg0,arg1):  # 先定义函数 
		args = {
				"center":{"t": "IPoint","v": arg0},
				"radius":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCircleRegion', 0, state)


	def setRegion(self,arg0):  # 先定义函数 
		args = {
				"geometry":{"t": "IGeometry","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRegion', 0, state)


	def setSectorRegion(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"start":{"t": "IPoint","v": arg0},
				"end":{"t": "IPoint","v": arg1},
				"horizontalAngle":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setSectorRegion', 0, state)

	@property
	def color(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["color"]

	@color.setter
	def color(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "color", val)
		args = {}
		args["color"] = PropsTypeData.get("color")
		args["color"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"color", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"color",JsonData)

	@property
	def maxZ(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxZ"]

	@maxZ.setter
	def maxZ(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxZ", val)
		args = {}
		args["maxZ"] = PropsTypeData.get("maxZ")
		args["maxZ"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxZ", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxZ",JsonData)

	@property
	def minZ(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minZ"]

	@minZ.setter
	def minZ(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minZ", val)
		args = {}
		args["minZ"] = PropsTypeData.get("minZ")
		args["minZ"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minZ", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minZ",JsonData)

	@property
	def visibleMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["visibleMask"]

	@visibleMask.setter
	def visibleMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "visibleMask", val)
		args = {}
		args["visibleMask"] = PropsTypeData.get("visibleMask")
		args["visibleMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"visibleMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visibleMask",JsonData)

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
