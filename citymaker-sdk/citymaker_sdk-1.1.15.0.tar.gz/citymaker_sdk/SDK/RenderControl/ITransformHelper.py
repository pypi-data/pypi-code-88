#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"type":{"t":"gviEditorType","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITransformHelper","F":"g"}}
#Events = {crsWKT:{fn:null}}
class ITransformHelper:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def setPosition(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPosition', 0, state)


	def setPosition2(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPosition2', 0, state)


	def setPosition3(self,arg0,arg1):  # 先定义函数 
		args = {
				"env":{"t": "IEnvelope","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPosition3', 0, state)

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

	@type.setter
	def type(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "type", val)
		args = {}
		args["type"] = PropsTypeData.get("type")
		args["type"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"type", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"type",JsonData)

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
