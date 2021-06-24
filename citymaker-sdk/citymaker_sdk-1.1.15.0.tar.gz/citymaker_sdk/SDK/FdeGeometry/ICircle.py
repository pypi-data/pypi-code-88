#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ICurve import ICurve
Props={"centerPoint":{"t":"IPoint","v":None,
"F":"gs"},"normal":{"t":"IVector3","v":None,
"F":"gs"},"radius":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICircle","F":"g"}}
class ICircle(ICurve):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._centerPoint=args.get("centerPoint")
		self._normal=args.get("normal")
		self._radius=args.get("radius")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def constructCenterAndRadius(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"center":{"t": "IPoint","v": arg0},
				"radius":{"t": "N","v": arg1},
				"normal":{"t": "IVector3","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'constructCenterAndRadius', 1, state)

	@property
	def centerPoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"centerPoint",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"centerPoint",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "centerPoint", res)
		return PropsValueData["centerPoint"]

	@centerPoint.setter
	def centerPoint(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "centerPoint", val)
		args = {}
		args["centerPoint"] = PropsTypeData.get("centerPoint")
		args["centerPoint"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"centerPoint", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"centerPoint",JsonData)

	@property
	def normal(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"normal",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"normal",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "normal", res)
		return PropsValueData["normal"]

	@normal.setter
	def normal(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "normal", val)
		args = {}
		args["normal"] = PropsTypeData.get("normal")
		args["normal"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"normal", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"normal",JsonData)

	@property
	def radius(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["radius"]

	@radius.setter
	def radius(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "radius", val)
		args = {}
		args["radius"] = PropsTypeData.get("radius")
		args["radius"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"radius", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"radius",JsonData)

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
