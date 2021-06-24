#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"color":{"t":"Color","v":"",
"F":"gs"},"flowLineLength":{"t":"double","v":10,
"F":"gs"},"radius":{"t":"float","v":2,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRenderPipeLine","F":"g"}}
class IRenderPipeLine(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._color=args.get("color")
		self._flowLineLength=args.get("flowLineLength")
		self._radius=args.get("radius")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getFdeGeometry(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFdeGeometry', 1, state)


	def play(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"playMode":{"t": "gviRenderPipeLinePlayMode","v": arg0},
				"duration":{"t": "N","v": arg1},
				"needLoop":{"t": "B","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'play', 0, state)


	def setFdeGeometry(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IGeometry","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setFdeGeometry', 0, state)


	def stop(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stop', 0, state)

	@property
	def color(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["color"]

	@color.setter
	def color(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "color", val)
		args = {}
		args["color"] = PropsTypeData.get("color")
		args["color"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"color", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"color",JsonData)

	@property
	def flowLineLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["flowLineLength"]

	@flowLineLength.setter
	def flowLineLength(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "flowLineLength", val)
		args = {}
		args["flowLineLength"] = PropsTypeData.get("flowLineLength")
		args["flowLineLength"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"flowLineLength", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"flowLineLength",JsonData)

	@property
	def radius(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["radius"]

	@radius.setter
	def radius(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "radius", val)
		args = {}
		args["radius"] = PropsTypeData.get("radius")
		args["radius"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"radius", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"radius",JsonData)

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
