#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"angle":{"t":"IEulerAngle","v":None,
"F":"gs"},"aspectRatio":{"t":"double","v":1.36777,
"F":"gs"},"canSeek":{"t":"bool","v":False,
"F":"g"},"displayMode":{"t":"gviTVDisplayMode","v":65535,
"F":"gs"},"farClip":{"t":"double","v":200.0,
"F":"gs"},"fieldOfView":{"t":"double","v":45.0,
"F":"gs"},"playbackRate":{"t":"double","v":1.0,
"F":"gs"},"playLoop":{"t":"bool","v":True,
"F":"gs"},"playStatus":{"t":"int","v":0,
"F":"g"},"playVideoOnStartup":{"t":"bool","v":False,
"F":"gs"},"position":{"t":"IPoint","v":None,
"F":"gs"},"videoLength":{"t":"double","v":0,
"F":"g"},"videoOpacity":{"t":"double","v":1.0,
"F":"gs"},"videoPosition":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainVideo","F":"g"}}
#Events = {icon:{fn:null}videoFileName:{fn:null}}
class ITerrainVideo(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._angle=args.get("angle")
		self._aspectRatio=args.get("aspectRatio")
		self._canSeek=args.get("canSeek")
		self._displayMode=args.get("displayMode")
		self._farClip=args.get("farClip")
		self._fieldOfView=args.get("fieldOfView")
		self._playbackRate=args.get("playbackRate")
		self._playLoop=args.get("playLoop")
		self._playStatus=args.get("playStatus")
		self._playVideoOnStartup=args.get("playVideoOnStartup")
		self._position=args.get("position")
		self._videoLength=args.get("videoLength")
		self._videoOpacity=args.get("videoOpacity")
		self._videoPosition=args.get("videoPosition")
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

	@property
	def angle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"angle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"angle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "angle", res)
		return PropsValueData["angle"]

	@angle.setter
	def angle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "angle", val)
		args = {}
		args["angle"] = PropsTypeData.get("angle")
		args["angle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"angle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"angle",JsonData)

	@property
	def aspectRatio(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["aspectRatio"]

	@aspectRatio.setter
	def aspectRatio(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "aspectRatio", val)
		args = {}
		args["aspectRatio"] = PropsTypeData.get("aspectRatio")
		args["aspectRatio"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"aspectRatio", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"aspectRatio",JsonData)

	@property
	def canSeek(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["canSeek"]

	@property
	def displayMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["displayMode"]

	@displayMode.setter
	def displayMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "displayMode", val)
		args = {}
		args["displayMode"] = PropsTypeData.get("displayMode")
		args["displayMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"displayMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"displayMode",JsonData)

	@property
	def farClip(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["farClip"]

	@farClip.setter
	def farClip(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "farClip", val)
		args = {}
		args["farClip"] = PropsTypeData.get("farClip")
		args["farClip"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"farClip", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"farClip",JsonData)

	@property
	def fieldOfView(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldOfView"]

	@fieldOfView.setter
	def fieldOfView(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fieldOfView", val)
		args = {}
		args["fieldOfView"] = PropsTypeData.get("fieldOfView")
		args["fieldOfView"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fieldOfView", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fieldOfView",JsonData)

	@property
	def playbackRate(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["playbackRate"]

	@playbackRate.setter
	def playbackRate(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "playbackRate", val)
		args = {}
		args["playbackRate"] = PropsTypeData.get("playbackRate")
		args["playbackRate"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"playbackRate", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"playbackRate",JsonData)

	@property
	def playLoop(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["playLoop"]

	@playLoop.setter
	def playLoop(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "playLoop", val)
		args = {}
		args["playLoop"] = PropsTypeData.get("playLoop")
		args["playLoop"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"playLoop", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"playLoop",JsonData)

	@property
	def playStatus(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["playStatus"]

	@property
	def playVideoOnStartup(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["playVideoOnStartup"]

	@playVideoOnStartup.setter
	def playVideoOnStartup(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "playVideoOnStartup", val)
		args = {}
		args["playVideoOnStartup"] = PropsTypeData.get("playVideoOnStartup")
		args["playVideoOnStartup"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"playVideoOnStartup", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"playVideoOnStartup",JsonData)

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
	def videoLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["videoLength"]

	@property
	def videoOpacity(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["videoOpacity"]

	@videoOpacity.setter
	def videoOpacity(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "videoOpacity", val)
		args = {}
		args["videoOpacity"] = PropsTypeData.get("videoOpacity")
		args["videoOpacity"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"videoOpacity", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"videoOpacity",JsonData)

	@property
	def videoPosition(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["videoPosition"]

	@videoPosition.setter
	def videoPosition(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "videoPosition", val)
		args = {}
		args["videoPosition"] = PropsTypeData.get("videoPosition")
		args["videoPosition"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"videoPosition", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"videoPosition",JsonData)

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
