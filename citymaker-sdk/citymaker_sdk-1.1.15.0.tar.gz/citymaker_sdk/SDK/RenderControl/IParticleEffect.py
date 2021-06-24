#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"damping":{"t":"double","v":0,
"F":"gs"},"emissionDirectionEulerAngle":{"t":"IEulerAngle","v":None,
"F":"gs"},"emissionMaxAngle":{"t":"double","v":0,
"F":"gs"},"emissionMaxMoveSpeed":{"t":"double","v":0,
"F":"gs"},"emissionMaxParticleSize":{"t":"double","v":0,
"F":"gs"},"emissionMaxRate":{"t":"double","v":0,
"F":"gs"},"emissionMaxRotationSpeed":{"t":"double","v":0,
"F":"gs"},"emissionMaxScaleSpeed":{"t":"double","v":0,
"F":"gs"},"emissionMinAngle":{"t":"double","v":0,
"F":"gs"},"emissionMinMoveSpeed":{"t":"double","v":0,
"F":"gs"},"emissionMinParticleSize":{"t":"double","v":0,
"F":"gs"},"emissionMinRate":{"t":"double","v":0,
"F":"gs"},"emissionMinRotationSpeed":{"t":"double","v":0,
"F":"gs"},"emissionMinScaleSpeed":{"t":"double","v":0,
"F":"gs"},"emitterType":{"t":"gviEmitterType","v":0,
"F":"g"},"particleAspectRatio":{"t":"double","v":0,
"F":"gs"},"particleBillboardType":{"t":"gviParticleBillboardType","v":0,
"F":"gs"},"particleBirthColor":{"t":"Color","v":"",
"F":"gs"},"particleDeathColor":{"t":"Color","v":"",
"F":"gs"},"particleMaxLifeTime":{"t":"double","v":0,
"F":"gs"},"particleMinLifeTime":{"t":"double","v":0,
"F":"gs"},"verticalAcceleration":{"t":"double","v":0,
"F":"gs"},"windAcceleration":{"t":"double","v":0,
"F":"gs"},"windDirection":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IParticleEffect","F":"g"}}
#Events = {imageName:{fn:null}}
class IParticleEffect(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._damping=args.get("damping")
		self._emissionDirectionEulerAngle=args.get("emissionDirectionEulerAngle")
		self._emissionMaxAngle=args.get("emissionMaxAngle")
		self._emissionMaxMoveSpeed=args.get("emissionMaxMoveSpeed")
		self._emissionMaxParticleSize=args.get("emissionMaxParticleSize")
		self._emissionMaxRate=args.get("emissionMaxRate")
		self._emissionMaxRotationSpeed=args.get("emissionMaxRotationSpeed")
		self._emissionMaxScaleSpeed=args.get("emissionMaxScaleSpeed")
		self._emissionMinAngle=args.get("emissionMinAngle")
		self._emissionMinMoveSpeed=args.get("emissionMinMoveSpeed")
		self._emissionMinParticleSize=args.get("emissionMinParticleSize")
		self._emissionMinRate=args.get("emissionMinRate")
		self._emissionMinRotationSpeed=args.get("emissionMinRotationSpeed")
		self._emissionMinScaleSpeed=args.get("emissionMinScaleSpeed")
		self._emitterType=args.get("emitterType")
		self._particleAspectRatio=args.get("particleAspectRatio")
		self._particleBillboardType=args.get("particleBillboardType")
		self._particleBirthColor=args.get("particleBirthColor")
		self._particleDeathColor=args.get("particleDeathColor")
		self._particleMaxLifeTime=args.get("particleMaxLifeTime")
		self._particleMinLifeTime=args.get("particleMinLifeTime")
		self._verticalAcceleration=args.get("verticalAcceleration")
		self._windAcceleration=args.get("windAcceleration")
		self._windDirection=args.get("windDirection")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getBoxEmitter(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"width":{"t": "N","v": arg1},
				"height":{"t": "N","v": arg2},
				"depth":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'getBoxEmitter', 0, state)


	def getCircleEmitter(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"radius":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'getCircleEmitter', 0, state)


	def getPointEmitter(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'getPointEmitter', 0, state)


	def getPosition(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getPosition', 1, state)


	def setBoxEmitter(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"width":{"t": "N","v": arg1},
				"height":{"t": "N","v": arg2},
				"depth":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'setBoxEmitter', 0, state)


	def setCircleEmitter(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"radius":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCircleEmitter', 0, state)


	def setPointEmitter(self,arg0):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPointEmitter', 0, state)


	def setTextureTileRange(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"hTile":{"t": "N","v": arg0},
				"vTile":{"t": "N","v": arg1},
				"startTile":{"t": "N","v": arg2},
				"endTile":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'setTextureTileRange', 0, state)


	def start(self,arg0):  # 先定义函数 
		args = {
				"duration":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'start', 1, state)


	def stop(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stop', 0, state)

	@property
	def damping(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["damping"]

	@damping.setter
	def damping(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "damping", val)
		args = {}
		args["damping"] = PropsTypeData.get("damping")
		args["damping"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"damping", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"damping",JsonData)

	@property
	def emissionDirectionEulerAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"emissionDirectionEulerAngle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionDirectionEulerAngle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "emissionDirectionEulerAngle", res)
		return PropsValueData["emissionDirectionEulerAngle"]

	@emissionDirectionEulerAngle.setter
	def emissionDirectionEulerAngle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionDirectionEulerAngle", val)
		args = {}
		args["emissionDirectionEulerAngle"] = PropsTypeData.get("emissionDirectionEulerAngle")
		args["emissionDirectionEulerAngle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionDirectionEulerAngle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionDirectionEulerAngle",JsonData)

	@property
	def emissionMaxAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMaxAngle"]

	@emissionMaxAngle.setter
	def emissionMaxAngle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMaxAngle", val)
		args = {}
		args["emissionMaxAngle"] = PropsTypeData.get("emissionMaxAngle")
		args["emissionMaxAngle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMaxAngle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMaxAngle",JsonData)

	@property
	def emissionMaxMoveSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMaxMoveSpeed"]

	@emissionMaxMoveSpeed.setter
	def emissionMaxMoveSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMaxMoveSpeed", val)
		args = {}
		args["emissionMaxMoveSpeed"] = PropsTypeData.get("emissionMaxMoveSpeed")
		args["emissionMaxMoveSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMaxMoveSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMaxMoveSpeed",JsonData)

	@property
	def emissionMaxParticleSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMaxParticleSize"]

	@emissionMaxParticleSize.setter
	def emissionMaxParticleSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMaxParticleSize", val)
		args = {}
		args["emissionMaxParticleSize"] = PropsTypeData.get("emissionMaxParticleSize")
		args["emissionMaxParticleSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMaxParticleSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMaxParticleSize",JsonData)

	@property
	def emissionMaxRate(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMaxRate"]

	@emissionMaxRate.setter
	def emissionMaxRate(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMaxRate", val)
		args = {}
		args["emissionMaxRate"] = PropsTypeData.get("emissionMaxRate")
		args["emissionMaxRate"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMaxRate", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMaxRate",JsonData)

	@property
	def emissionMaxRotationSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMaxRotationSpeed"]

	@emissionMaxRotationSpeed.setter
	def emissionMaxRotationSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMaxRotationSpeed", val)
		args = {}
		args["emissionMaxRotationSpeed"] = PropsTypeData.get("emissionMaxRotationSpeed")
		args["emissionMaxRotationSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMaxRotationSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMaxRotationSpeed",JsonData)

	@property
	def emissionMaxScaleSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMaxScaleSpeed"]

	@emissionMaxScaleSpeed.setter
	def emissionMaxScaleSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMaxScaleSpeed", val)
		args = {}
		args["emissionMaxScaleSpeed"] = PropsTypeData.get("emissionMaxScaleSpeed")
		args["emissionMaxScaleSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMaxScaleSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMaxScaleSpeed",JsonData)

	@property
	def emissionMinAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMinAngle"]

	@emissionMinAngle.setter
	def emissionMinAngle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMinAngle", val)
		args = {}
		args["emissionMinAngle"] = PropsTypeData.get("emissionMinAngle")
		args["emissionMinAngle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMinAngle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMinAngle",JsonData)

	@property
	def emissionMinMoveSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMinMoveSpeed"]

	@emissionMinMoveSpeed.setter
	def emissionMinMoveSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMinMoveSpeed", val)
		args = {}
		args["emissionMinMoveSpeed"] = PropsTypeData.get("emissionMinMoveSpeed")
		args["emissionMinMoveSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMinMoveSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMinMoveSpeed",JsonData)

	@property
	def emissionMinParticleSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMinParticleSize"]

	@emissionMinParticleSize.setter
	def emissionMinParticleSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMinParticleSize", val)
		args = {}
		args["emissionMinParticleSize"] = PropsTypeData.get("emissionMinParticleSize")
		args["emissionMinParticleSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMinParticleSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMinParticleSize",JsonData)

	@property
	def emissionMinRate(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMinRate"]

	@emissionMinRate.setter
	def emissionMinRate(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMinRate", val)
		args = {}
		args["emissionMinRate"] = PropsTypeData.get("emissionMinRate")
		args["emissionMinRate"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMinRate", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMinRate",JsonData)

	@property
	def emissionMinRotationSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMinRotationSpeed"]

	@emissionMinRotationSpeed.setter
	def emissionMinRotationSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMinRotationSpeed", val)
		args = {}
		args["emissionMinRotationSpeed"] = PropsTypeData.get("emissionMinRotationSpeed")
		args["emissionMinRotationSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMinRotationSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMinRotationSpeed",JsonData)

	@property
	def emissionMinScaleSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionMinScaleSpeed"]

	@emissionMinScaleSpeed.setter
	def emissionMinScaleSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionMinScaleSpeed", val)
		args = {}
		args["emissionMinScaleSpeed"] = PropsTypeData.get("emissionMinScaleSpeed")
		args["emissionMinScaleSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionMinScaleSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionMinScaleSpeed",JsonData)

	@property
	def emitterType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emitterType"]

	@property
	def particleAspectRatio(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["particleAspectRatio"]

	@particleAspectRatio.setter
	def particleAspectRatio(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "particleAspectRatio", val)
		args = {}
		args["particleAspectRatio"] = PropsTypeData.get("particleAspectRatio")
		args["particleAspectRatio"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"particleAspectRatio", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"particleAspectRatio",JsonData)

	@property
	def particleBillboardType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["particleBillboardType"]

	@particleBillboardType.setter
	def particleBillboardType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "particleBillboardType", val)
		args = {}
		args["particleBillboardType"] = PropsTypeData.get("particleBillboardType")
		args["particleBillboardType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"particleBillboardType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"particleBillboardType",JsonData)

	@property
	def particleBirthColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["particleBirthColor"]

	@particleBirthColor.setter
	def particleBirthColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "particleBirthColor", val)
		args = {}
		args["particleBirthColor"] = PropsTypeData.get("particleBirthColor")
		args["particleBirthColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"particleBirthColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"particleBirthColor",JsonData)

	@property
	def particleDeathColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["particleDeathColor"]

	@particleDeathColor.setter
	def particleDeathColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "particleDeathColor", val)
		args = {}
		args["particleDeathColor"] = PropsTypeData.get("particleDeathColor")
		args["particleDeathColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"particleDeathColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"particleDeathColor",JsonData)

	@property
	def particleMaxLifeTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["particleMaxLifeTime"]

	@particleMaxLifeTime.setter
	def particleMaxLifeTime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "particleMaxLifeTime", val)
		args = {}
		args["particleMaxLifeTime"] = PropsTypeData.get("particleMaxLifeTime")
		args["particleMaxLifeTime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"particleMaxLifeTime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"particleMaxLifeTime",JsonData)

	@property
	def particleMinLifeTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["particleMinLifeTime"]

	@particleMinLifeTime.setter
	def particleMinLifeTime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "particleMinLifeTime", val)
		args = {}
		args["particleMinLifeTime"] = PropsTypeData.get("particleMinLifeTime")
		args["particleMinLifeTime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"particleMinLifeTime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"particleMinLifeTime",JsonData)

	@property
	def verticalAcceleration(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["verticalAcceleration"]

	@verticalAcceleration.setter
	def verticalAcceleration(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "verticalAcceleration", val)
		args = {}
		args["verticalAcceleration"] = PropsTypeData.get("verticalAcceleration")
		args["verticalAcceleration"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"verticalAcceleration", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"verticalAcceleration",JsonData)

	@property
	def windAcceleration(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["windAcceleration"]

	@windAcceleration.setter
	def windAcceleration(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "windAcceleration", val)
		args = {}
		args["windAcceleration"] = PropsTypeData.get("windAcceleration")
		args["windAcceleration"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"windAcceleration", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"windAcceleration",JsonData)

	@property
	def windDirection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["windDirection"]

	@windDirection.setter
	def windDirection(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "windDirection", val)
		args = {}
		args["windDirection"] = PropsTypeData.get("windDirection")
		args["windDirection"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"windDirection", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"windDirection",JsonData)

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
