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
"F":"gs"},"elevationModel":{"t":"gviNetworkElevationModel","v":0,
"F":"gs"},"isDirty":{"t":"bool","v":False,
"F":"g"},"type":{"t":"gviNetworkType","v":0,
"F":"g"},"xYTolerance":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetwork","F":"g"}}
#Events = {name:{fn:null}}
class INetwork:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._defaultXYTolerance=args.get("defaultXYTolerance")
		self._edgeDirection=args.get("edgeDirection")
		self._elevationModel=args.get("elevationModel")
		self._isDirty=args.get("isDirty")
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
				"networkSource":{"t": "INetworkSource","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addSource', 0, state)


	def buildNetwork(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'buildNetwork', 0, state)


	def canUseFeatureClass(self,arg0):  # 先定义函数 
		args = {
				"featureClassName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'canUseFeatureClass', 1, state)


	def createClosestFacilitySolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createClosestFacilitySolver', 1, state)


	def createFindAncestorsSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createFindAncestorsSolver', 1, state)


	def createFindConnectedSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createFindConnectedSolver', 1, state)


	def createFindDisconnectedSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createFindDisconnectedSolver', 1, state)


	def createFindLoopsSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createFindLoopsSolver', 1, state)


	def createRouteSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createRouteSolver', 1, state)


	def createTraceDownstreamSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createTraceDownstreamSolver', 1, state)


	def createTraceUpstreamSolver(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createTraceUpstreamSolver', 1, state)


	def deleteNetworkAttribute(self,arg0):  # 先定义函数 
		args = {
				"nan":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteNetworkAttribute', 0, state)


	def deleteSource(self,arg0):  # 先定义函数 
		args = {
				"sourceName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteSource', 0, state)


	def establishFlowDirection(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'establishFlowDirection', 0, state)


	def featureDataset(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'featureDataset', 1, state)


	def getAttribute(self,arg0):  # 先定义函数 
		args = {
				"attributeName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAttribute', 1, state)


	def getAttributeNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getAttributeNames', 1, state)


	def getLogicalNetwork(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getLogicalNetwork', 1, state)


	def getNetworkSource(self,arg0):  # 先定义函数 
		args = {
				"sourceName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getNetworkSource', 1, state)


	def getNetworkSourceNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getNetworkSourceNames', 1, state)


	def griddingPolygons(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"geoCollection":{"t": "IGeometryCollection","v": arg0},
				"edgeNetworkSourceName":{"t": "S","v": arg1},
				"edgeNetworkSourceGeoColumnName":{"t": "S","v": arg2},
				"junctionNetworkSourceName":{"t": "S","v": arg3},
				"junctionNetworkSourceGeoColumnName":{"t": "S","v": arg4},
				"gridSize":{"t": "N","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'griddingPolygons', 0, state)

	@property
	def defaultXYTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["defaultXYTolerance"]

	@property
	def edgeDirection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["edgeDirection"]

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
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["elevationModel"]

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
	def isDirty(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isDirty"]

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

	@property
	def xYTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["xYTolerance"]

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
