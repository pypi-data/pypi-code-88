#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IPoint import IPoint
Props={"matrix33":{"t":"IFloatArray","v":"",
"F":"gs"},"modelEnvelope":{"t":"IEnvelope","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IModelPoint","F":"g"}}
#Events = {modelName:{fn:null}}
class IModelPoint(IPoint):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._matrix33=args.get("matrix33")
		self._modelEnvelope=args.get("modelEnvelope")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asMatrix(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asMatrix', 1, state)


	def fromMatrix(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IMatrix","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'fromMatrix', 0, state)


	def rayIntersect(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"model":{"t": "IModel","v": arg0},
				"start":{"t": "IPoint","v": arg1},
				"dir":{"t": "IVector3","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'rayIntersect', 1, state)


	def resetPose(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'resetPose', 0, state)


	def selfRotate(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"axisX":{"t": "N","v": arg0},
				"axisY":{"t": "N","v": arg1},
				"axisZ":{"t": "N","v": arg2},
				"rotationAngle":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'selfRotate', 0, state)


	def selfScale(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"scaleZ":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'selfScale', 0, state)

	@property
	def matrix33(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"matrix33",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"matrix33",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "matrix33", res)
		return PropsValueData["matrix33"]

	@matrix33.setter
	def matrix33(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "matrix33", val)
		args = {}
		args["matrix33"] = PropsTypeData.get("matrix33")
		args["matrix33"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"matrix33", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"matrix33",JsonData)

	@property
	def modelEnvelope(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"modelEnvelope",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"modelEnvelope",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "modelEnvelope", res)
		return PropsValueData["modelEnvelope"]

	@modelEnvelope.setter
	def modelEnvelope(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "modelEnvelope", val)
		args = {}
		args["modelEnvelope"] = PropsTypeData.get("modelEnvelope")
		args["modelEnvelope"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"modelEnvelope", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"modelEnvelope",JsonData)

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
