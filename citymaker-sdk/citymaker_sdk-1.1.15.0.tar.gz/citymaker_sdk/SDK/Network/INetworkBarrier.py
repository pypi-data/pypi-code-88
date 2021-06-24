#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"constraintBarrierType":{"t":"gviConstraintBarrierType","v":1,
"F":"gs"},"shape":{"t":"IGeometry","v":None,
"F":"gs"},"type":{"t":"gviNetworkBarrierType","v":1,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkBarrier","F":"g"}}
#Events = {name:{fn:null}}
class INetworkBarrier:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._constraintBarrierType=args.get("constraintBarrierType")
		self._shape=args.get("shape")
		self._type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def getCost(self,arg0):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCost', 1, state)


	def setCost(self,arg0,arg1):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCost', 0, state)

	@property
	def constraintBarrierType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["constraintBarrierType"]

	@constraintBarrierType.setter
	def constraintBarrierType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "constraintBarrierType", val)
		args = {}
		args["constraintBarrierType"] = PropsTypeData.get("constraintBarrierType")
		args["constraintBarrierType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"constraintBarrierType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"constraintBarrierType",JsonData)

	@property
	def shape(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"shape",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"shape",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "shape", res)
		return PropsValueData["shape"]

	@shape.setter
	def shape(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "shape", val)
		args = {}
		args["shape"] = PropsTypeData.get("shape")
		args["shape"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"shape", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"shape",JsonData)

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

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
