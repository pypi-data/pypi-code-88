#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"duration":{"t":"double","v":0,
"F":"g"},"emissionRate":{"t":"double","v":0,
"F":"gs"},"isAlive":{"t":"bool","v":False,
"F":"g"},"position":{"t":"IPoint","v":None,
"F":"gs"},"rotateAngle":{"t":"IEulerAngle","v":None,
"F":"gs"},"scalingFactor":{"t":"double","v":0,
"F":"gs"},"windAcceleration":{"t":"double","v":0,
"F":"gs"},"windDirection":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IComplexParticleEffect","F":"g"}}
class IComplexParticleEffect(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._duration=args.get("duration")
		self._emissionRate=args.get("emissionRate")
		self._isAlive=args.get("isAlive")
		self._position=args.get("position")
		self._rotateAngle=args.get("rotateAngle")
		self._scalingFactor=args.get("scalingFactor")
		self._windAcceleration=args.get("windAcceleration")
		self._windDirection=args.get("windDirection")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def bind(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"path":{"t": "IMotionPath","v": arg0},
				"posOffset":{"t": "IVector3","v": arg1},
				"headingOffset":{"t": "N","v": arg2},
				"pitchOffset":{"t": "N","v": arg3},
				"rollOffset":{"t": "N","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'bind', 0, state)


	def bind2(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"path":{"t": "IDynamicObject","v": arg0},
				"posOffset":{"t": "IVector3","v": arg1},
				"headingOffset":{"t": "N","v": arg2},
				"pitchOffset":{"t": "N","v": arg3},
				"rollOffset":{"t": "N","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'bind2', 0, state)


	def getMotionPathId(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getMotionPathId', 1, state)


	def unbind(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'unbind', 0, state)


	def motionableBindDynamicObject(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"modelGuid":{"t": "S","v": arg0},
				"dynamicGuid":{"t": "S","v": arg1},
				"posOffset":{"t": "IVector3","v": arg2},
				"angleOffset":{"t": "IEulerAngle","v": arg3}
		}
		state = "new"
		CM.AddPrototype(self,args, 'motionableBindDynamicObject', 0, state)


	def getComplexParticleEffectType(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getComplexParticleEffectType', 1, state)


	def play(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'play', 0, state)


	def stop(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stop', 0, state)

	@property
	def duration(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["duration"]

	@property
	def emissionRate(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["emissionRate"]

	@emissionRate.setter
	def emissionRate(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "emissionRate", val)
		args = {}
		args["emissionRate"] = PropsTypeData.get("emissionRate")
		args["emissionRate"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"emissionRate", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"emissionRate",JsonData)

	@property
	def isAlive(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isAlive"]

	@property
	def position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"position",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "position", res)
		return PropsValueData["position"]

	@position.setter
	def position(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "position", val)
		args = {}
		args["position"] = PropsTypeData.get("position")
		args["position"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"position", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",JsonData)

	@property
	def rotateAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"rotateAngle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rotateAngle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "rotateAngle", res)
		return PropsValueData["rotateAngle"]

	@rotateAngle.setter
	def rotateAngle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "rotateAngle", val)
		args = {}
		args["rotateAngle"] = PropsTypeData.get("rotateAngle")
		args["rotateAngle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"rotateAngle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rotateAngle",JsonData)

	@property
	def scalingFactor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["scalingFactor"]

	@scalingFactor.setter
	def scalingFactor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "scalingFactor", val)
		args = {}
		args["scalingFactor"] = PropsTypeData.get("scalingFactor")
		args["scalingFactor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"scalingFactor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"scalingFactor",JsonData)

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
