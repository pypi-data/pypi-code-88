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
"F":"gs"},"motionStyle":{"t":"gviDynamicMotionStyle","v":3,
"F":"gs"},"turnSpeed":{"t":"double","v":50,
"F":"gs"},"viewingDistance":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDynamicObject","F":"g"}}
#Events = {crsWKT:{fn:null}}
class IDynamicObject(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._autoRepeat=args.get("autoRepeat")
		self._index=args.get("index")
		self._motionStyle=args.get("motionStyle")
		self._turnSpeed=args.get("turnSpeed")
		self._viewingDistance=args.get("viewingDistance")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addWaypoint2(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"speed":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addWaypoint2', 1, state)


	def asXml(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asXml', 1, state)


	def clearWaypoints(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearWaypoints', 0, state)


	def deleteWaypoint(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteWaypoint', 1, state)


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


	def insertWaypoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertWaypoint', 1, state)


	def insertWaypoint2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IPoint","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertWaypoint2', 1, state)


	def modifyWaypoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modifyWaypoint', 1, state)


	def modifyWaypoint2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"position":{"t": "IPoint","v": arg1},
				"speed":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modifyWaypoint2', 1, state)


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


	def waypointsNumber(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'waypointsNumber', 1, state)


	def addWaypoint(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"speed":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addWaypoint', 1, state)

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
	def motionStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["motionStyle"]

	@motionStyle.setter
	def motionStyle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "motionStyle", val)
		args = {}
		args["motionStyle"] = PropsTypeData.get("motionStyle")
		args["motionStyle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"motionStyle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"motionStyle",JsonData)

	@property
	def turnSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["turnSpeed"]

	@turnSpeed.setter
	def turnSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "turnSpeed", val)
		args = {}
		args["turnSpeed"] = PropsTypeData.get("turnSpeed")
		args["turnSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"turnSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"turnSpeed",JsonData)

	@property
	def viewingDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["viewingDistance"]

	@viewingDistance.setter
	def viewingDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "viewingDistance", val)
		args = {}
		args["viewingDistance"] = PropsTypeData.get("viewingDistance")
		args["viewingDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"viewingDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"viewingDistance",JsonData)

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
