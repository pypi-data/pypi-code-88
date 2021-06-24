#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"shadowColor":{"t":"Color","v":"",
"F":"gs"},"sunCalculateMode":{"t":"gviSunCalculateMode","v":1,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISunConfig","F":"g"}}
class ISunConfig:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._shadowColor=args.get("shadowColor")
		self._sunCalculateMode=args.get("sunCalculateMode")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def enableShadow(self,arg0,arg1):  # 先定义函数 
		args = {
				"viewID":{"t": "N","v": arg0},
				"isEnable":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'enableShadow', 0, state)


	def getSunEuler(self,arg0):  # 先定义函数 
		args = {
				"pos":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSunEuler', 1, state)


	def isShadowEnabled(self,arg0):  # 先定义函数 
		args = {
				"viewID":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isShadowEnabled', 1, state)


	def setGMT(self,arg0):  # 先定义函数 
		args = {
				"time":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setGMT', 0, state)


	def setSunEuler(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IEulerAngle","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setSunEuler', 0, state)

	@property
	def shadowColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["shadowColor"]

	@shadowColor.setter
	def shadowColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "shadowColor", val)
		args = {}
		args["shadowColor"] = PropsTypeData.get("shadowColor")
		args["shadowColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"shadowColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"shadowColor",JsonData)

	@property
	def sunCalculateMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["sunCalculateMode"]

	@sunCalculateMode.setter
	def sunCalculateMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "sunCalculateMode", val)
		args = {}
		args["sunCalculateMode"] = PropsTypeData.get("sunCalculateMode")
		args["sunCalculateMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"sunCalculateMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"sunCalculateMode",JsonData)

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
