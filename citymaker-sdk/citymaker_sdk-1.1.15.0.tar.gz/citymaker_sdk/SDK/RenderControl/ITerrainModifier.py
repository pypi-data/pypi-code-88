#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"drawOrder":{"t":"int","v":0,
"F":"gs"},"elevationBehavior":{"t":"gviElevationBehaviorMode","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainModifier","F":"g"}}
class ITerrainModifier(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._drawOrder=args.get("drawOrder")
		self._elevationBehavior=args.get("elevationBehavior")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getPolygon(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygon', 1, state)


	def setPolygon(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPolygon', 0, state)

	@property
	def drawOrder(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["drawOrder"]

	@drawOrder.setter
	def drawOrder(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "drawOrder", val)
		args = {}
		args["drawOrder"] = PropsTypeData.get("drawOrder")
		args["drawOrder"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"drawOrder", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"drawOrder",JsonData)

	@property
	def elevationBehavior(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["elevationBehavior"]

	@elevationBehavior.setter
	def elevationBehavior(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "elevationBehavior", val)
		args = {}
		args["elevationBehavior"] = PropsTypeData.get("elevationBehavior")
		args["elevationBehavior"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"elevationBehavior", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"elevationBehavior",JsonData)

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
