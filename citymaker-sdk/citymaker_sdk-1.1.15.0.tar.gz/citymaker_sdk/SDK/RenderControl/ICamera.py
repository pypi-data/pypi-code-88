#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"flyTime":{"t":"double","v":8.0,
"F":"gs"},"flySpeed":{"t":"float","v":0,
"F":"gs"},"walkSpeed":{"t":"float","v":10.0,
"F":"gs"},"autoClipPlane":{"t":"bool","v":True,
"F":"gs"},"canRedo":{"t":"bool","v":False,
"F":"g"},"canUndo":{"t":"bool","v":False,
"F":"g"},"collisionDetectionMode":{"t":"gviCollisionDetectionMode","v":1,
"F":"gs"},"envelope":{"t":"IEnvelope","v":None,
"F":"gs"},"farClipPlane":{"t":"float","v":10000.0,
"F":"gs"},"flyMode":{"t":"gviFlyMode","v":1,
"F":"gs"},"nearClipPlane":{"t":"float","v":1.0,
"F":"gs"},"undergroundMode":{"t":"bool","v":False,
"F":"gs"},"verticalFieldOfView":{"t":"float","v":45,
"F":"gs"},"walkHeight":{"t":"float","v":1.8,
"F":"gs"},"walkMode":{"t":"gviWalkMode","v":-1,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICamera","F":"g"}}
class ICamera:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._flyTime=args.get("flyTime")
		self._flySpeed=args.get("flySpeed")
		self._walkSpeed=args.get("walkSpeed")
		self._autoClipPlane=args.get("autoClipPlane")
		self._canRedo=args.get("canRedo")
		self._canUndo=args.get("canUndo")
		self._collisionDetectionMode=args.get("collisionDetectionMode")
		self._envelope=args.get("envelope")
		self._farClipPlane=args.get("farClipPlane")
		self._flyMode=args.get("flyMode")
		self._nearClipPlane=args.get("nearClipPlane")
		self._undergroundMode=args.get("undergroundMode")
		self._verticalFieldOfView=args.get("verticalFieldOfView")
		self._walkHeight=args.get("walkHeight")
		self._walkMode=args.get("walkMode")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def redo(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'redo', 0, state)


	def undo(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'undo', 0, state)


	def screenToWorld(self,arg0,arg1):  # 先定义函数 
		args = {
				"wx":{"t": "N","v": arg0},
				"wy":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'screenToWorld', 1, state)


	def lookAtFeature(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"datasetName":{"t": "S","v": arg0},
				"fcName":{"t": "S","v": arg1},
				"geoFieldName":{"t": "S","v": arg2},
				"fidFlyTo":{"t": "Number","v": arg3}
		}
		state = "new"
		CM.AddPrototype(self,args, 'lookAtFeature', 0, state)


	def getCamera(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getCamera', 1, state)


	def setCamera(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"flags":{"t": "gviSetCameraFlags","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCamera', 0, state)


	def flyToLocation(self,arg0,arg1):  # 先定义函数 
		args = {
				"locationGuid":{"t": "S","v": arg0},
				"flag":{"t": "Number","v": arg1}
		}
		state = "new"
		CM.AddPrototype(self,args, 'flyToLocation', 0, state)


	def flyToObject(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectId":{"t": "G","v": arg0},
				"actionCode":{"t": "gviActionCode","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'flyToObject', 0, state)


	def asMatrix(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asMatrix', 1, state)


	def flyAround(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"cCW":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'flyAround', 0, state)


	def fromMatrix(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IMatrix","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'fromMatrix', 0, state)


	def getAimingAngles(self,arg0,arg1):  # 先定义函数 
		args = {
				"position1":{"t": "IVector3","v": arg0},
				"position2":{"t": "IVector3","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAimingAngles', 1, state)


	def getAimingAngles2(self,arg0,arg1):  # 先定义函数 
		args = {
				"position1":{"t": "IPoint","v": arg0},
				"position2":{"t": "IPoint","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAimingAngles2', 1, state)


	def getAimingPoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"range":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAimingPoint', 1, state)


	def getAimingPoint2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"range":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAimingPoint2', 1, state)


	def getCamera2(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getCamera2', 1, state)


	def lookAt(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"distance":{"t": "N","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'lookAt', 0, state)


	def lookAt2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"distance":{"t": "N","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'lookAt2', 0, state)


	def lookAtEnvelope(self,arg0):  # 先定义函数 
		args = {
				"env":{"t": "IEnvelope","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'lookAtEnvelope', 0, state)


	def lookAtEnvelope2(self,arg0,arg1):  # 先定义函数 
		args = {
				"crsWKT":{"t": "S","v": arg0},
				"env":{"t": "IEnvelope","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'lookAtEnvelope2', 0, state)


	def setCamera2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"flags":{"t": "gviSetCameraFlags","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCamera2', 0, state)


	def stop(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stop', 0, state)


	def worldToScreen(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"worldX":{"t": "N","v": arg0},
				"worldY":{"t": "N","v": arg1},
				"worldZ":{"t": "N","v": arg2},
				"mode":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'worldToScreen', 1, state)


	def zoomIn(self,arg0):  # 先定义函数 
		args = {
				"delta":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'zoomIn', 0, state)


	def zoomOut(self,arg0):  # 先定义函数 
		args = {
				"delta":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'zoomOut', 0, state)

	@property
	def flyTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["flyTime"]

	@flyTime.setter
	def flyTime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "flyTime", val)
		args = {}
		args["flyTime"] = PropsTypeData.get("flyTime")
		args["flyTime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"flyTime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"flyTime",JsonData)

	@property
	def flySpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["flySpeed"]

	@flySpeed.setter
	def flySpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "flySpeed", val)
		args = {}
		args["flySpeed"] = PropsTypeData.get("flySpeed")
		args["flySpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"flySpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"flySpeed",JsonData)

	@property
	def walkSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["walkSpeed"]

	@walkSpeed.setter
	def walkSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "walkSpeed", val)
		args = {}
		args["walkSpeed"] = PropsTypeData.get("walkSpeed")
		args["walkSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"walkSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"walkSpeed",JsonData)

	@property
	def autoClipPlane(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["autoClipPlane"]

	@autoClipPlane.setter
	def autoClipPlane(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "autoClipPlane", val)
		args = {}
		args["autoClipPlane"] = PropsTypeData.get("autoClipPlane")
		args["autoClipPlane"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"autoClipPlane", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"autoClipPlane",JsonData)

	@property
	def canRedo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["canRedo"]

	@property
	def canUndo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["canUndo"]

	@property
	def collisionDetectionMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["collisionDetectionMode"]

	@collisionDetectionMode.setter
	def collisionDetectionMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "collisionDetectionMode", val)
		args = {}
		args["collisionDetectionMode"] = PropsTypeData.get("collisionDetectionMode")
		args["collisionDetectionMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"collisionDetectionMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"collisionDetectionMode",JsonData)

	@property
	def envelope(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"envelope",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"envelope",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "envelope", res)
		return PropsValueData["envelope"]

	@envelope.setter
	def envelope(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "envelope", val)
		args = {}
		args["envelope"] = PropsTypeData.get("envelope")
		args["envelope"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"envelope", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"envelope",JsonData)

	@property
	def farClipPlane(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["farClipPlane"]

	@farClipPlane.setter
	def farClipPlane(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "farClipPlane", val)
		args = {}
		args["farClipPlane"] = PropsTypeData.get("farClipPlane")
		args["farClipPlane"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"farClipPlane", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"farClipPlane",JsonData)

	@property
	def flyMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["flyMode"]

	@flyMode.setter
	def flyMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "flyMode", val)
		args = {}
		args["flyMode"] = PropsTypeData.get("flyMode")
		args["flyMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"flyMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"flyMode",JsonData)

	@property
	def nearClipPlane(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["nearClipPlane"]

	@nearClipPlane.setter
	def nearClipPlane(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "nearClipPlane", val)
		args = {}
		args["nearClipPlane"] = PropsTypeData.get("nearClipPlane")
		args["nearClipPlane"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"nearClipPlane", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"nearClipPlane",JsonData)

	@property
	def undergroundMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["undergroundMode"]

	@undergroundMode.setter
	def undergroundMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "undergroundMode", val)
		args = {}
		args["undergroundMode"] = PropsTypeData.get("undergroundMode")
		args["undergroundMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"undergroundMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"undergroundMode",JsonData)

	@property
	def verticalFieldOfView(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["verticalFieldOfView"]

	@verticalFieldOfView.setter
	def verticalFieldOfView(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "verticalFieldOfView", val)
		args = {}
		args["verticalFieldOfView"] = PropsTypeData.get("verticalFieldOfView")
		args["verticalFieldOfView"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"verticalFieldOfView", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"verticalFieldOfView",JsonData)

	@property
	def walkHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["walkHeight"]

	@walkHeight.setter
	def walkHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "walkHeight", val)
		args = {}
		args["walkHeight"] = PropsTypeData.get("walkHeight")
		args["walkHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"walkHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"walkHeight",JsonData)

	@property
	def walkMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["walkMode"]

	@walkMode.setter
	def walkMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "walkMode", val)
		args = {}
		args["walkMode"] = PropsTypeData.get("walkMode")
		args["walkMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"walkMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"walkMode",JsonData)

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
