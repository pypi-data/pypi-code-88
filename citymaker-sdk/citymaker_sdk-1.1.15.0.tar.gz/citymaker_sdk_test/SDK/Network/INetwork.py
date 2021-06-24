#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.defaultXYTolerance=args.get("defaultXYTolerance")
		self.edgeDirection=args.get("edgeDirection")
		self.elevationModel=args.get("elevationModel")
		self.isDirty=args.get("isDirty")
		self.type=args.get("type")
		self.xYTolerance=args.get("xYTolerance")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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

	def __getattr__(self,name):
		if name in Props:
			attrVal=Props[name]
			if name =="_HashCode":
				return CM.dict_get(attrVal, "v", None)
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("g") > -1:
				if CP.ClassFN.get(t) is not None and "PickResult" not in Props["propertyType"]["v"] and name != "propertyType":
					PropsTypeData = CM.getPropsTypeData(self._HashCode)
					PropsValueData = CM.getPropsValueData(self._HashCode)
					jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),name,None)
					res=socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,jsonData)
					CM.addPropsValue(PropsValueData["_HashCode"], name, res)
					return PropsValueData[name]
				else:
					PropsValueData = CM.getPropsValueData(self._HashCode)
					if name == "fullScreen":
						res=CM.isFull()
					CM.addPropsValue(PropsValueData.get("_HashCode"), name, res)
					return PropsValueData[name]

	def __setattr__(self,name,value):
		if name in Props:
			attrVal=Props[name]
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("s") > -1:
				if name =="_HashCode":
					CM.dict_set(attrVal, "F", value)
					return
				PropsTypeData = CM.getPropsTypeData(self._HashCode)
				PropsValueData = CM.getPropsValueData(self._HashCode)
				CM.addPropsValue(PropsValueData.get("_HashCode"), name, value)
				if name == "fullScreen":
					res=CM.isFull()
					return
				args = {}
				args[name] = PropsTypeData.get(name)
				args[name]["v"] = value
				JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),name, args)
				socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,JsonData)
				super(INetwork, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
