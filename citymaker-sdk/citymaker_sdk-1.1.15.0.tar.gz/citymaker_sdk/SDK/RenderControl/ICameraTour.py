#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRObject import IRObject
Props={"autoRepeat":{"t":"bool","v":False,
"F":"gs"},"index":{"t":"int","v":0,
"F":"gs"},"isExporting":{"t":"bool","v":False,
"F":"g"},"time":{"t":"double","v":0,
"F":"gs"},"totalTime":{"t":"double","v":0,
"F":"g"},"waypointsNumber":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICameraTour","F":"g"}}
#Events = {crsWKT:{fn:null}slideImageName:{fn:null}}
class ICameraTour(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._autoRepeat=args.get("autoRepeat")
		self._index=args.get("index")
		self._isExporting=args.get("isExporting")
		self._time=args.get("time")
		self._totalTime=args.get("totalTime")
		self._waypointsNumber=args.get("waypointsNumber")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addWaypoint2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"duration":{"t": "N","v": arg2},
				"mode":{"t": "gviCameraTourMode","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'addWaypoint2', 0, state)


	def addWaypointByMatrix(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"mat":{"t": "IMatrix","v": arg0},
				"duration":{"t": "N","v": arg1},
				"mode":{"t": "gviCameraTourMode","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'addWaypointByMatrix', 0, state)


	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)


	def cancelExport(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'cancelExport', 0, state)


	def clearWaypoints(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearWaypoints', 0, state)


	def exportFrameSequence(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"width":{"t": "N","v": arg1},
				"height":{"t": "N","v": arg2},
				"fPS":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportFrameSequence', 1, state)


	def exportPanoramaFrameSequence(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"width":{"t": "N","v": arg1},
				"fPS":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportPanoramaFrameSequence', 1, state)


	def exportVideo(self,arg0,arg1):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"fPS":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportVideo', 1, state)


	def fromAse(self,arg0):  # 先定义函数 
		args = {
				"file":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'fromAse', 0, state)


	def fromXml(self,arg0):  # 先定义函数 
		args = {
				"xmlStringValue":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'fromXml', 1, state)


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


	def insertWaypoint2(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IPoint","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"duration":{"t": "N","v": arg3},
				"mode":{"t": "gviCameraTourMode","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'insertWaypoint2', 0, state)


	def insertWaypointByMatrix(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"mat":{"t": "IMatrix","v": arg1},
				"duration":{"t": "N","v": arg2},
				"mode":{"t": "gviCameraTourMode","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'insertWaypointByMatrix', 0, state)


	def modifyWaypoint2(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IPoint","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"duration":{"t": "N","v": arg3},
				"mode":{"t": "gviCameraTourMode","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'modifyWaypoint2', 0, state)


	def modifyWaypointByMatrix(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"mat":{"t": "IMatrix","v": arg1},
				"duration":{"t": "N","v": arg2},
				"mode":{"t": "gviCameraTourMode","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'modifyWaypointByMatrix', 0, state)


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


	def addWaypoint(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"duration":{"t": "N","v": arg2},
				"mode":{"t": "gviCameraTourMode","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'addWaypoint', 0, state)


	def insertWaypoint(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"duration":{"t": "N","v": arg3},
				"mode":{"t": "gviCameraTourMode","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'insertWaypoint', 0, state)


	def modifyWaypoint(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2},
				"duration":{"t": "N","v": arg3},
				"mode":{"t": "gviCameraTourMode","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modifyWaypoint', 1, state)


	def deleteWaypoint(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteWaypoint', 0, state)


	def getWaypoint(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getWaypoint', 1, state)

	@property
	def autoRepeat(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["autoRepeat"]

	@autoRepeat.setter
	def autoRepeat(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "autoRepeat", val)
		args = {}
		args["autoRepeat"] = PropsTypeData.get("autoRepeat")
		args["autoRepeat"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"autoRepeat", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"autoRepeat",JsonData)

	@property
	def index(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["index"]

	@index.setter
	def index(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "index", val)
		args = {}
		args["index"] = PropsTypeData.get("index")
		args["index"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"index", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"index",JsonData)

	@property
	def isExporting(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isExporting"]

	@property
	def time(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["time"]

	@time.setter
	def time(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "time", val)
		args = {}
		args["time"] = PropsTypeData.get("time")
		args["time"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"time", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"time",JsonData)

	@property
	def totalTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["totalTime"]

	@property
	def waypointsNumber(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["waypointsNumber"]

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
