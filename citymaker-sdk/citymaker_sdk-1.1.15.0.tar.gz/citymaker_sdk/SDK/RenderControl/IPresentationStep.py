#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"captionTimeout":{"t":"int","v":0,
"F":"gs"},"continue":{"t":"gviPresentationStepContinue","v":1,
"F":"gs"},"flightSpeedFactor":{"t":"gviPresentationStepFlightSpeed","v":2,
"F":"gs"},"id":{"t":"Guid","v":"",
"F":"g"},"index":{"t":"int","v":0,
"F":"gs"},"keyStep":{"t":"bool","v":True,
"F":"gs"},"locationSplineSpeed":{"t":"double","v":0,
"F":"gs"},"locationSplineSpeedBehavior":{"t":"gviPresentationSplineSpeedBehavior","v":0,
"F":"gs"},"showHideValue":{"t":"bool","v":True,
"F":"gs"},"type":{"t":"gviPresentationStepType","v":0,
"F":"gs"},"waitTime":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPresentationStep","F":"g"}}
#Events = {captionText:{fn:null}description:{fn:null}}
class IPresentationStep:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._captionTimeout=args.get("captionTimeout")
		self._continue=args.get("continue")
		self._flightSpeedFactor=args.get("flightSpeedFactor")
		self._id=args.get("id")
		self._index=args.get("index")
		self._keyStep=args.get("keyStep")
		self._locationSplineSpeed=args.get("locationSplineSpeed")
		self._locationSplineSpeedBehavior=args.get("locationSplineSpeedBehavior")
		self._showHideValue=args.get("showHideValue")
		self._type=args.get("type")
		self._waitTime=args.get("waitTime")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def containsOperation(self,arg0):  # 先定义函数 
		args = {
				"operationName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'containsOperation', 1, state)


	def getOperationValue(self,arg0):  # 先定义函数 
		args = {
				"operationName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getOperationValue', 1, state)

	@property
	def captionTimeout(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["captionTimeout"]

	@captionTimeout.setter
	def captionTimeout(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "captionTimeout", val)
		args = {}
		args["captionTimeout"] = PropsTypeData.get("captionTimeout")
		args["captionTimeout"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"captionTimeout", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"captionTimeout",JsonData)

	@property
	def _continue(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["_continue"]

	@_continue.setter
	def _continue(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "_continue", val)
		args = {}
		args["_continue"] = PropsTypeData.get("_continue")
		args["_continue"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"_continue", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"_continue",JsonData)

	@property
	def flightSpeedFactor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["flightSpeedFactor"]

	@flightSpeedFactor.setter
	def flightSpeedFactor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "flightSpeedFactor", val)
		args = {}
		args["flightSpeedFactor"] = PropsTypeData.get("flightSpeedFactor")
		args["flightSpeedFactor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"flightSpeedFactor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"flightSpeedFactor",JsonData)

	@property
	def id(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["id"]

	@property
	def index(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["index"]

	@index.setter
	def index(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "index", val)
		args = {}
		args["index"] = PropsTypeData.get("index")
		args["index"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"index", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"index",JsonData)

	@property
	def keyStep(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["keyStep"]

	@keyStep.setter
	def keyStep(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "keyStep", val)
		args = {}
		args["keyStep"] = PropsTypeData.get("keyStep")
		args["keyStep"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"keyStep", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"keyStep",JsonData)

	@property
	def locationSplineSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["locationSplineSpeed"]

	@locationSplineSpeed.setter
	def locationSplineSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "locationSplineSpeed", val)
		args = {}
		args["locationSplineSpeed"] = PropsTypeData.get("locationSplineSpeed")
		args["locationSplineSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"locationSplineSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"locationSplineSpeed",JsonData)

	@property
	def locationSplineSpeedBehavior(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["locationSplineSpeedBehavior"]

	@locationSplineSpeedBehavior.setter
	def locationSplineSpeedBehavior(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "locationSplineSpeedBehavior", val)
		args = {}
		args["locationSplineSpeedBehavior"] = PropsTypeData.get("locationSplineSpeedBehavior")
		args["locationSplineSpeedBehavior"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"locationSplineSpeedBehavior", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"locationSplineSpeedBehavior",JsonData)

	@property
	def showHideValue(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["showHideValue"]

	@showHideValue.setter
	def showHideValue(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "showHideValue", val)
		args = {}
		args["showHideValue"] = PropsTypeData.get("showHideValue")
		args["showHideValue"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"showHideValue", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"showHideValue",JsonData)

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

	@type.setter
	def type(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "type", val)
		args = {}
		args["type"] = PropsTypeData.get("type")
		args["type"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"type", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"type",JsonData)

	@property
	def waitTime(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["waitTime"]

	@waitTime.setter
	def waitTime(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "waitTime", val)
		args = {}
		args["waitTime"] = PropsTypeData.get("waitTime")
		args["waitTime"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"waitTime", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"waitTime",JsonData)

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
