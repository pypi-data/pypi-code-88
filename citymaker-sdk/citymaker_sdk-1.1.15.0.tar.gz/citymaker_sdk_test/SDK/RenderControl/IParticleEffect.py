#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.damping=args.get("damping")
		self.emissionDirectionEulerAngle=args.get("emissionDirectionEulerAngle")
		self.emissionMaxAngle=args.get("emissionMaxAngle")
		self.emissionMaxMoveSpeed=args.get("emissionMaxMoveSpeed")
		self.emissionMaxParticleSize=args.get("emissionMaxParticleSize")
		self.emissionMaxRate=args.get("emissionMaxRate")
		self.emissionMaxRotationSpeed=args.get("emissionMaxRotationSpeed")
		self.emissionMaxScaleSpeed=args.get("emissionMaxScaleSpeed")
		self.emissionMinAngle=args.get("emissionMinAngle")
		self.emissionMinMoveSpeed=args.get("emissionMinMoveSpeed")
		self.emissionMinParticleSize=args.get("emissionMinParticleSize")
		self.emissionMinRate=args.get("emissionMinRate")
		self.emissionMinRotationSpeed=args.get("emissionMinRotationSpeed")
		self.emissionMinScaleSpeed=args.get("emissionMinScaleSpeed")
		self.emitterType=args.get("emitterType")
		self.particleAspectRatio=args.get("particleAspectRatio")
		self.particleBillboardType=args.get("particleBillboardType")
		self.particleBirthColor=args.get("particleBirthColor")
		self.particleDeathColor=args.get("particleDeathColor")
		self.particleMaxLifeTime=args.get("particleMaxLifeTime")
		self.particleMinLifeTime=args.get("particleMinLifeTime")
		self.verticalAcceleration=args.get("verticalAcceleration")
		self.windAcceleration=args.get("windAcceleration")
		self.windDirection=args.get("windDirection")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				super(IParticleEffect, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
