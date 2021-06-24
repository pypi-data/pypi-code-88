#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"defaultXYTolerance":{"t":"double","v":0,
"F":"g"},"edgeDirection":{"t":"gviEdgeDirection","v":0,
"F":"s"},"elevationModel":{"t":"gviNetworkElevationModel","v":0,
"F":"s"},"type":{"t":"gviNetworkType","v":0,
"F":"s"},"xYTolerance":{"t":"double","v":0,
"F":"s"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkLoader","F":"g"}}
#Events = {name:{fn:null}}
class INetworkLoader:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._defaultXYTolerance=args.get("defaultXYTolerance")
		self._edgeDirection=args.get("edgeDirection")
		self._elevationModel=args.get("elevationModel")
		self._type=args.get("type")
		self._xYTolerance=args.get("xYTolerance")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addNetworkAttribute(self,arg0):  # 先定义函数 
		args = {
				"na":{"t": "INetworkAttribute","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addNetworkAttribute', 0, state)


	def addSource(self,arg0):  # 先定义函数 
		args = {
				"ns":{"t": "INetworkSource","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addSource', 0, state)


	def breakIntersectEdgeSource(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'breakIntersectEdgeSource', 0, state)


	def canUseFeatureClass(self,arg0):  # 先定义函数 
		args = {
				"featureClassName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'canUseFeatureClass', 1, state)


	def loadNetwork(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'loadNetwork', 0, state)

	@property
	def defaultXYTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["defaultXYTolerance"]

	@property
	def edgeDirection(self):
		pass

	@edgeDirection.setter
	def edgeDirection(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "edgeDirection", val)
		args = {}
		args["edgeDirection"] = PropsTypeData.get("edgeDirection")
		args["edgeDirection"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"edgeDirection", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"edgeDirection",JsonData)

	@property
	def elevationModel(self):
		pass

	@elevationModel.setter
	def elevationModel(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "elevationModel", val)
		args = {}
		args["elevationModel"] = PropsTypeData.get("elevationModel")
		args["elevationModel"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"elevationModel", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"elevationModel",JsonData)

	@property
	def type(self):
		pass

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
	def xYTolerance(self):
		pass

	@xYTolerance.setter
	def xYTolerance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "xYTolerance", val)
		args = {}
		args["xYTolerance"] = PropsTypeData.get("xYTolerance")
		args["xYTolerance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"xYTolerance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"xYTolerance",JsonData)

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
