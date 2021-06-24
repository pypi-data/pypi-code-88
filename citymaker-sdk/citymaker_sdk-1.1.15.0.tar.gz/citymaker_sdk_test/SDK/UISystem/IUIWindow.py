#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"isDisabled":{"t":"bool","v":False,
"F":"gs"},"isMousePassThroughEnabled":{"t":"bool","v":True,
"F":"gs"},"isVisible":{"t":"bool","v":False,
"F":"gs"},"isZOrderingEnabled":{"t":"bool","v":False,
"F":"gs"},"type":{"t":"gviUIWindowType","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IUIWindow","F":"g"}}
#Events = {name:{fn:null}text:{fn:null}toolTipText:{fn:null}}
class IUIWindow:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.isDisabled=args.get("isDisabled")
		self.isMousePassThroughEnabled=args.get("isMousePassThroughEnabled")
		self.isVisible=args.get("isVisible")
		self.isZOrderingEnabled=args.get("isZOrderingEnabled")
		self.type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def fillOverlayUILabel(self,arg0,arg1):  # 先定义函数 
		args = {
				"uiLabelGuid":{"t": "S","v": arg0},
				"childNames":{"t": "S","v": arg1}
		}
		state = "new"
		CM.AddPrototype(self,args, 'fillOverlayUILabel', 0, state)


	def addChild(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IUIWindow","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addChild', 0, state)


	def getArea(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getArea', 1, state)


	def getPixelSize(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getPixelSize', 1, state)


	def getUserString(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getUserString', 1, state)


	def removeChild(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'removeChild', 0, state)


	def setArea(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IUIRect","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setArea', 0, state)


	def setUserString(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"value":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setUserString', 0, state)


	def subscribeEvent(self,arg0):  # 先定义函数 
		args = {
				"eventType":{"t": "gviUIEventType","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'subscribeEvent', 0, state)


	def unsubscribeEvent(self,arg0):  # 先定义函数 
		args = {
				"eventType":{"t": "gviUIEventType","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'unsubscribeEvent', 0, state)

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
				super(IUIWindow, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
