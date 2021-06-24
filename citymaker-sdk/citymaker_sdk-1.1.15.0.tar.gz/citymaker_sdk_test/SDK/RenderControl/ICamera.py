#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.flyTime=args.get("flyTime")
		self.flySpeed=args.get("flySpeed")
		self.walkSpeed=args.get("walkSpeed")
		self.autoClipPlane=args.get("autoClipPlane")
		self.canRedo=args.get("canRedo")
		self.canUndo=args.get("canUndo")
		self.collisionDetectionMode=args.get("collisionDetectionMode")
		self.envelope=args.get("envelope")
		self.farClipPlane=args.get("farClipPlane")
		self.flyMode=args.get("flyMode")
		self.nearClipPlane=args.get("nearClipPlane")
		self.undergroundMode=args.get("undergroundMode")
		self.verticalFieldOfView=args.get("verticalFieldOfView")
		self.walkHeight=args.get("walkHeight")
		self.walkMode=args.get("walkMode")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				"fidFlyTo":{"t": "N","v": arg3}
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
				"flag":{"t": "N","v": arg1}
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
				super(ICamera, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
