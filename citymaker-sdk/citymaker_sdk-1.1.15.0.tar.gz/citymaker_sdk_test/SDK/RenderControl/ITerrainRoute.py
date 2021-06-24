#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.RenderControl.IRObject import IRObject
Props={"autoRepeat":{"t":"bool","v":0,
"F":"gs"},"isExporting":{"t":"bool","v":False,
"F":"g"},"waypointsNumber":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainRoute","F":"g"}}
#Events = {crsWKT:{fn:null}slideImageName:{fn:null}}
class ITerrainRoute(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.autoRepeat=args.get("autoRepeat")
		self.isExporting=args.get("isExporting")
		self.waypointsNumber=args.get("waypointsNumber")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def addWaypoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addWaypoint', 1, state)


	def addWaypoint2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addWaypoint2', 1, state)


	def addWaypointByMatrix(self,arg0,arg1):  # 先定义函数 
		args = {
				"mat":{"t": "IMatrix","v": arg0},
				"speed":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addWaypointByMatrix', 1, state)


	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)


	def cancelExport(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'cancelExport', 0, state)


	def deleteWaypoint(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteWaypoint', 1, state)


	def exportVideo(self,arg0,arg1):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"fPS":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'exportVideo', 0, state)


	def fromXml(self,arg0):  # 先定义函数 
		args = {
				"xmlStringValue":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'fromXml', 1, state)


	def getWaypoint(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getWaypoint', 1, state)


	def getWaypoint2(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getWaypoint2', 1, state)


	def getWaypointByMatrix(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getWaypointByMatrix', 1, state)


	def insertWaypoint(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"speed":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertWaypoint', 1, state)


	def insertWaypoint2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IPoint","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"speed":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertWaypoint2', 1, state)


	def insertWaypointByMatrix(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"mat":{"t": "IMatrix","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertWaypointByMatrix', 1, state)


	def modifyWaypoint(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"speed":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modifyWaypoint', 1, state)


	def modifyWaypoint2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IPoint","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"speed":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modifyWaypoint2', 1, state)


	def modifyWaypointByMatrix(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"mat":{"t": "IMatrix","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modifyWaypointByMatrix', 1, state)


	def pause(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'pause', 0, state)


	def play(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'play', 0, state)


	def stop(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stop', 0, state)

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
				super(ITerrainRoute, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
