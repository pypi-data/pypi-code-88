#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.backgroundColor=args.get("backgroundColor")
		self.fogColor=args.get("fogColor")
		self.fogEndDistance=args.get("fogEndDistance")
		self.fogMode=args.get("fogMode")
		self.fogStartDistance=args.get("fogStartDistance")
		self.heading=args.get("heading")
		self.weather=args.get("weather")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
		return CM.AddPrototype(self,args, 'GetImagePath', 1, state)


	def setImagePath(self,arg0,arg1):  # 先定义函数 
		args = {
				"imageIndex":{"t": "gviSkyboxImageIndex","v": arg0},
				"imagePath":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setImagePath', 0, state)

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
				super(ISkyBox, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
