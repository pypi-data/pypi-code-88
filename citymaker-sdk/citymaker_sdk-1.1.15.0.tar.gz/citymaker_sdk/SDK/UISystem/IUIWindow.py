#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
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
		self._isDisabled=args.get("isDisabled")
		self._isMousePassThroughEnabled=args.get("isMousePassThroughEnabled")
		self._isVisible=args.get("isVisible")
		self._isZOrderingEnabled=args.get("isZOrderingEnabled")
		self._type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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

	@property
	def isDisabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isDisabled"]

	@isDisabled.setter
	def isDisabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isDisabled", val)
		args = {}
		args["isDisabled"] = PropsTypeData.get("isDisabled")
		args["isDisabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isDisabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isDisabled",JsonData)

	@property
	def isMousePassThroughEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isMousePassThroughEnabled"]

	@isMousePassThroughEnabled.setter
	def isMousePassThroughEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isMousePassThroughEnabled", val)
		args = {}
		args["isMousePassThroughEnabled"] = PropsTypeData.get("isMousePassThroughEnabled")
		args["isMousePassThroughEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isMousePassThroughEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isMousePassThroughEnabled",JsonData)

	@property
	def isVisible(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isVisible"]

	@isVisible.setter
	def isVisible(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isVisible", val)
		args = {}
		args["isVisible"] = PropsTypeData.get("isVisible")
		args["isVisible"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isVisible", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isVisible",JsonData)

	@property
	def isZOrderingEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isZOrderingEnabled"]

	@isZOrderingEnabled.setter
	def isZOrderingEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "isZOrderingEnabled", val)
		args = {}
		args["isZOrderingEnabled"] = PropsTypeData.get("isZOrderingEnabled")
		args["isZOrderingEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"isZOrderingEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"isZOrderingEnabled",JsonData)

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

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
