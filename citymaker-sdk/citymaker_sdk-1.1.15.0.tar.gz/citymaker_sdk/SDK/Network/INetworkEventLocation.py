#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.Network.INetworkLocation import INetworkLocation
Props={"targetFacilityCount":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkEventLocation","F":"g"}}
class INetworkEventLocation(INetworkLocation):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._targetFacilityCount=args.get("targetFacilityCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getCutoff(self,arg0):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCutoff', 1, state)


	def setCutoff(self,arg0,arg1):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCutoff', 0, state)

	@property
	def targetFacilityCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["targetFacilityCount"]

	@targetFacilityCount.setter
	def targetFacilityCount(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "targetFacilityCount", val)
		args = {}
		args["targetFacilityCount"] = PropsTypeData.get("targetFacilityCount")
		args["targetFacilityCount"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"targetFacilityCount", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"targetFacilityCount",JsonData)

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
