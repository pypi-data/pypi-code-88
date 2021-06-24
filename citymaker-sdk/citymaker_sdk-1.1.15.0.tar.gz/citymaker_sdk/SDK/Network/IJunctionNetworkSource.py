#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.Network.INetworkSource import INetworkSource
Props={"connectivityPolicy":{"t":"gviNetworkJunctionConnectivityPolicy","v":1,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IJunctionNetworkSource","F":"g"}}
#Events = {defaultSourceSinkField:{fn:null}elevationFieldName:{fn:null}sourceSinkField:{fn:null}}
class IJunctionNetworkSource(INetworkSource):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._connectivityPolicy=args.get("connectivityPolicy")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getClassConnectivityGroups(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getClassConnectivityGroups', 1, state)


	def getSubTypeConnectivityGroups(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getSubTypeConnectivityGroups', 1, state)


	def setClassConnectivityGroup(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setClassConnectivityGroup', 0, state)


	def setSubTypeConnectivityGroups(self,arg0,arg1):  # 先定义函数 
		args = {
				"subTypeCode":{"t": "N","v": arg0},
				"groupId":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setSubTypeConnectivityGroups', 0, state)

	@property
	def connectivityPolicy(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["connectivityPolicy"]

	@connectivityPolicy.setter
	def connectivityPolicy(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "connectivityPolicy", val)
		args = {}
		args["connectivityPolicy"] = PropsTypeData.get("connectivityPolicy")
		args["connectivityPolicy"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"connectivityPolicy", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"connectivityPolicy",JsonData)

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
