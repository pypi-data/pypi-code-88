#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IOperation import IOperation
Props={"boxLineColor":{"t":"Color","v":"",
"F":"gs"},"boxSurfaceColor":{"t":"Color","v":"",
"F":"gs"},"clipPlaneOperationType":{"t":"gviClipPlaneOperation","v":0,
"F":"g"},"visibleMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IClipPlaneOperation","F":"g"}}
class IClipPlaneOperation(IOperation):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._boxLineColor=args.get("boxLineColor")
		self._boxSurfaceColor=args.get("boxSurfaceColor")
		self._clipPlaneOperationType=args.get("clipPlaneOperationType")
		self._visibleMask=args.get("visibleMask")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getBoxClip(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getBoxClip', 1, state)


	def getSingleClip(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getSingleClip', 1, state)


	def setBoxClip(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"boxCenter":{"t": "IVector3","v": arg0},
				"boxSize":{"t": "IVector3","v": arg1},
				"angle":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setBoxClip', 0, state)


	def setSingleClip(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setSingleClip', 0, state)

	@property
	def boxLineColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["boxLineColor"]

	@boxLineColor.setter
	def boxLineColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "boxLineColor", val)
		args = {}
		args["boxLineColor"] = PropsTypeData.get("boxLineColor")
		args["boxLineColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"boxLineColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"boxLineColor",JsonData)

	@property
	def boxSurfaceColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["boxSurfaceColor"]

	@boxSurfaceColor.setter
	def boxSurfaceColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "boxSurfaceColor", val)
		args = {}
		args["boxSurfaceColor"] = PropsTypeData.get("boxSurfaceColor")
		args["boxSurfaceColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"boxSurfaceColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"boxSurfaceColor",JsonData)

	@property
	def clipPlaneOperationType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["clipPlaneOperationType"]

	@property
	def visibleMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["visibleMask"]

	@visibleMask.setter
	def visibleMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "visibleMask", val)
		args = {}
		args["visibleMask"] = PropsTypeData.get("visibleMask")
		args["visibleMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"visibleMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visibleMask",JsonData)

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
