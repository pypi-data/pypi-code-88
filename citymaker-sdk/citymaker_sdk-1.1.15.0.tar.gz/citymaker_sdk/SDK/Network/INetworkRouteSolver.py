#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.Network.INetworkSolver import INetworkSolver
Props={"locationOrderPolicy":{"t":"gviNetworkLocationOrderPolicy","v":1,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkRouteSolver","F":"g"}}
class INetworkRouteSolver(INetworkSolver):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._locationOrderPolicy=args.get("locationOrderPolicy")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getRoute(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRoute', 1, state)

	@property
	def locationOrderPolicy(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["locationOrderPolicy"]

	@locationOrderPolicy.setter
	def locationOrderPolicy(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "locationOrderPolicy", val)
		args = {}
		args["locationOrderPolicy"] = PropsTypeData.get("locationOrderPolicy")
		args["locationOrderPolicy"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"locationOrderPolicy", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"locationOrderPolicy",JsonData)

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
