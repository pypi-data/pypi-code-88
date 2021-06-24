#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.RenderControl.IRenderable import IRenderable
Props={"alignment":{"t":"gviPivotAlignment","v":0,
"F":"gs"},"depth":{"t":"float","v":0,
"F":"gs"},"rotation":{"t":"float","v":0,
"F":"gs"},"textStyle":{"t":"ITextAttribute","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IOverlayLabel","F":"g"}}
#Events = {imageName:{fn:null}text:{fn:null}}
class IOverlayLabel(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.alignment=args.get("alignment")
		self.depth=args.get("depth")
		self.rotation=args.get("rotation")
		self.textStyle=args.get("textStyle")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def getHeight(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getHeight', 1, state)


	def getWidth(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getWidth', 1, state)


	def getX(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getX', 1, state)


	def getY(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getY', 1, state)


	def setHeight(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setHeight', 0, state)


	def setWidth(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setWidth', 0, state)


	def setX(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setX', 0, state)


	def setY(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"offset":{"t": "N","v": arg0},
				"windowWidthRatio":{"t": "N","v": arg1},
				"windowHeightRatio":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setY', 0, state)

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
				super(IOverlayLabel, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
