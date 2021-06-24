#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRObject import IRObject
Props={"backgroundColor":{"t":"Color","v":"",
"F":"gs"},"fogColor":{"t":"Color","v":"",
"F":"gs"},"fogEndDistance":{"t":"float","v":0,
"F":"gs"},"fogMode":{"t":"gviFogMode","v":0,
"F":"gs"},"fogStartDistance":{"t":"float","v":0,
"F":"gs"},"heading":{"t":"double","v":0,
"F":"gs"},"weather":{"t":"gviWeatherType","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISkyBox","F":"g"}}
class ISkyBox(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._backgroundColor=args.get("backgroundColor")
		self._fogColor=args.get("fogColor")
		self._fogEndDistance=args.get("fogEndDistance")
		self._fogMode=args.get("fogMode")
		self._fogStartDistance=args.get("fogStartDistance")
		self._heading=args.get("heading")
		self._weather=args.get("weather")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def setSkybox(self,arg0,arg1):  # 先定义函数 
		args = {
				"skyboxDirPath":{"t": "S","v": arg0},
				"skyboxImageFileName":{"t": "S","v": arg1}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setSkybox', 0, state)


	def setWeather(self,arg0):  # 先定义函数 
		args = {
				"weatherType":{"t": "gviWeatherType","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setWeather', 0, state)


	def setFogMode(self,arg0):  # 先定义函数 
		args = {
				"fogMode":{"t": "gviFogMode","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setFogMode', 0, state)


	def getImagePath(self,arg0):  # 先定义函数 
		args = {
				"imageIndex":{"t": "gviSkyboxImageIndex","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getImagePath', 1, state)


	def setImagePath(self,arg0,arg1):  # 先定义函数 
		args = {
				"imageIndex":{"t": "gviSkyboxImageIndex","v": arg0},
				"imagePath":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setImagePath', 0, state)

	@property
	def backgroundColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["backgroundColor"]

	@backgroundColor.setter
	def backgroundColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "backgroundColor", val)
		args = {}
		args["backgroundColor"] = PropsTypeData.get("backgroundColor")
		args["backgroundColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"backgroundColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"backgroundColor",JsonData)

	@property
	def fogColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fogColor"]

	@fogColor.setter
	def fogColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fogColor", val)
		args = {}
		args["fogColor"] = PropsTypeData.get("fogColor")
		args["fogColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fogColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fogColor",JsonData)

	@property
	def fogEndDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fogEndDistance"]

	@fogEndDistance.setter
	def fogEndDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fogEndDistance", val)
		args = {}
		args["fogEndDistance"] = PropsTypeData.get("fogEndDistance")
		args["fogEndDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fogEndDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fogEndDistance",JsonData)

	@property
	def fogMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fogMode"]

	@fogMode.setter
	def fogMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fogMode", val)
		args = {}
		args["fogMode"] = PropsTypeData.get("fogMode")
		args["fogMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fogMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fogMode",JsonData)

	@property
	def fogStartDistance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fogStartDistance"]

	@fogStartDistance.setter
	def fogStartDistance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fogStartDistance", val)
		args = {}
		args["fogStartDistance"] = PropsTypeData.get("fogStartDistance")
		args["fogStartDistance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fogStartDistance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fogStartDistance",JsonData)

	@property
	def heading(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["heading"]

	@heading.setter
	def heading(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "heading", val)
		args = {}
		args["heading"] = PropsTypeData.get("heading")
		args["heading"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"heading", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"heading",JsonData)

	@property
	def weather(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["weather"]

	@weather.setter
	def weather(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "weather", val)
		args = {}
		args["weather"] = PropsTypeData.get("weather")
		args["weather"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"weather", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"weather",JsonData)

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
