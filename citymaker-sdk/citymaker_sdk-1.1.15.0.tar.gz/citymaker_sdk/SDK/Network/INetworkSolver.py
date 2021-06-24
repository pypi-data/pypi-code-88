#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"barrierCount":{"t":"int","v":0,
"F":"g"},"isBuildRouteLine":{"t":"bool","v":False,
"F":"gs"},"isUseHierarchy":{"t":"bool","v":False,
"F":"gs"},"locationCount":{"t":"int","v":0,
"F":"g"},"locationSearchTolerance":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkSolver","F":"g"}}
#Events = {hierarchyAttributeName:{fn:null}impedanceAttributeName:{fn:null}}
class INetworkSolver:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._barrierCount=args.get("barrierCount")
		self._isBuildRouteLine=args.get("isBuildRouteLine")
		self._isUseHierarchy=args.get("isUseHierarchy")
		self._locationCount=args.get("locationCount")
		self._locationSearchTolerance=args.get("locationSearchTolerance")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addBarrier(self,arg0):  # 先定义函数 
		args = {
				"nb":{"t": "INetworkBarrier","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addBarrier', 0, state)


	def addLocation(self,arg0):  # 先定义函数 
		args = {
				"networkLocation":{"t": "INetworkLocation","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addLocation', 0, state)


	def clearBarriers(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearBarriers', 0, state)


	def clearLocations(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearLocations', 0, state)


	def getBarrier(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getBarrier', 1, state)


	def getLocation(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getLocation', 1, state)


	def getRestrictionAttributeNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRestrictionAttributeNames', 1, state)


	def loadNetworkData(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'loadNetworkData', 0, state)


	def setRestrictionAttributeName(self,arg0):  # 先定义函数 
		args = {
				"attributeName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRestrictionAttributeName', 0, state)


	def solve(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'solve', 1, state)

	@property
	def barrierCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["barrierCount"]

	@property
	def isBuildRouteLine(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isBuildRouteLine"]

	@isBuildRouteLine.setter
	def isBuildRouteLine(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isBuildRouteLine", val)
		args = {}
		args["isBuildRouteLine"] = PropsTypeData.get("isBuildRouteLine")
		args["isBuildRouteLine"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isBuildRouteLine", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isBuildRouteLine",JsonData)

	@property
	def isUseHierarchy(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isUseHierarchy"]

	@isUseHierarchy.setter
	def isUseHierarchy(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isUseHierarchy", val)
		args = {}
		args["isUseHierarchy"] = PropsTypeData.get("isUseHierarchy")
		args["isUseHierarchy"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isUseHierarchy", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isUseHierarchy",JsonData)

	@property
	def locationCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["locationCount"]

	@property
	def locationSearchTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["locationSearchTolerance"]

	@locationSearchTolerance.setter
	def locationSearchTolerance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "locationSearchTolerance", val)
		args = {}
		args["locationSearchTolerance"] = PropsTypeData.get("locationSearchTolerance")
		args["locationSearchTolerance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"locationSearchTolerance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"locationSearchTolerance",JsonData)

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
