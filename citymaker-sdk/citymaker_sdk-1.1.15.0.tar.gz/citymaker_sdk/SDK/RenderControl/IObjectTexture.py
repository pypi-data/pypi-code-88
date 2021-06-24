#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"rotateAngle":{"t":"double","v":0,
"F":"gs"},"scaleX":{"t":"double","v":0,
"F":"gs"},"scaleY":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IObjectTexture","F":"g"}}
#Events = {fileName:{fn:null}}
class IObjectTexture:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._rotateAngle=args.get("rotateAngle")
		self._scaleX=args.get("scaleX")
		self._scaleY=args.get("scaleY")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def rotateAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["rotateAngle"]

	@rotateAngle.setter
	def rotateAngle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "rotateAngle", val)
		args = {}
		args["rotateAngle"] = PropsTypeData.get("rotateAngle")
		args["rotateAngle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"rotateAngle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rotateAngle",JsonData)

	@property
	def scaleX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["scaleX"]

	@scaleX.setter
	def scaleX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "scaleX", val)
		args = {}
		args["scaleX"] = PropsTypeData.get("scaleX")
		args["scaleX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"scaleX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"scaleX",JsonData)

	@property
	def scaleY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["scaleY"]

	@scaleY.setter
	def scaleY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "scaleY", val)
		args = {}
		args["scaleY"] = PropsTypeData.get("scaleY")
		args["scaleY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"scaleY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"scaleY",JsonData)

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
