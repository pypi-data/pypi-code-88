#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"animationCount":{"t":"uint","v":0,
"F":"g"},"animationIndex":{"t":"uint","v":0,
"F":"gs"},"duration":{"t":"double","v":0,
"F":"gs"},"loop":{"t":"bool","v":False,
"F":"gs"},"modelPoint":{"t":"IModelPoint","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISkinnedMesh","F":"g"}}
class ISkinnedMesh(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._animationCount=args.get("animationCount")
		self._animationIndex=args.get("animationIndex")
		self._duration=args.get("duration")
		self._loop=args.get("loop")
		self._modelPoint=args.get("modelPoint")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clampAnimation(self,arg0,arg1):  # 先定义函数 
		args = {
				"startPercentage":{"t": "N","v": arg0},
				"endPercentage":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'clampAnimation', 1, state)


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

	@property
	def animationCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["animationCount"]

	@property
	def animationIndex(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["animationIndex"]

	@animationIndex.setter
	def animationIndex(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "animationIndex", val)
		args = {}
		args["animationIndex"] = PropsTypeData.get("animationIndex")
		args["animationIndex"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"animationIndex", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"animationIndex",JsonData)

	@property
	def duration(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["duration"]

	@duration.setter
	def duration(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "duration", val)
		args = {}
		args["duration"] = PropsTypeData.get("duration")
		args["duration"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"duration", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"duration",JsonData)

	@property
	def loop(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["loop"]

	@loop.setter
	def loop(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "loop", val)
		args = {}
		args["loop"] = PropsTypeData.get("loop")
		args["loop"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"loop", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"loop",JsonData)

	@property
	def modelPoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"modelPoint",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"modelPoint",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "modelPoint", res)
		return PropsValueData["modelPoint"]

	@modelPoint.setter
	def modelPoint(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "modelPoint", val)
		args = {}
		args["modelPoint"] = PropsTypeData.get("modelPoint")
		args["modelPoint"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"modelPoint", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"modelPoint",JsonData)

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
