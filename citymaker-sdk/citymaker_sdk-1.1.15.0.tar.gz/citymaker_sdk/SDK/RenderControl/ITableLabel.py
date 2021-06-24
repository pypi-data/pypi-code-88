#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"borderColor":{"t":"Color","v":"",
"F":"gs"},"borderWidth":{"t":"float","v":0,
"F":"gs"},"columnCount":{"t":"int","v":0,
"F":"g"},"position":{"t":"IPoint","v":None,
"F":"gs"},"rowCount":{"t":"int","v":0,
"F":"g"},"tableBackgroundColor":{"t":"Color","v":"",
"F":"gs"},"titleBackgroundColor":{"t":"Color","v":"",
"F":"gs"},"titleTextAttribute":{"t":"ITextAttribute","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITableLabel","F":"g"}}
#Events = {backgroundImageName:{fn:null}titleText:{fn:null}}
class ITableLabel(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._borderColor=args.get("borderColor")
		self._borderWidth=args.get("borderWidth")
		self._columnCount=args.get("columnCount")
		self._position=args.get("position")
		self._rowCount=args.get("rowCount")
		self._tableBackgroundColor=args.get("tableBackgroundColor")
		self._titleBackgroundColor=args.get("titleBackgroundColor")
		self._titleTextAttribute=args.get("titleTextAttribute")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def bind(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"path":{"t": "IMotionPath","v": arg0},
				"posOffset":{"t": "IVector3","v": arg1},
				"headingOffset":{"t": "N","v": arg2},
				"pitchOffset":{"t": "N","v": arg3},
				"rollOffset":{"t": "N","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'bind', 0, state)


	def bind2(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"path":{"t": "IDynamicObject","v": arg0},
				"posOffset":{"t": "IVector3","v": arg1},
				"headingOffset":{"t": "N","v": arg2},
				"pitchOffset":{"t": "N","v": arg3},
				"rollOffset":{"t": "N","v": arg4}
		}
		state = ""
		CM.AddPrototype(self,args, 'bind2', 0, state)


	def getMotionPathId(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getMotionPathId', 1, state)


	def unbind(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'unbind', 0, state)


	def motionableBindDynamicObject(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"modelGuid":{"t": "S","v": arg0},
				"dynamicGuid":{"t": "S","v": arg1},
				"posOffset":{"t": "IVector3","v": arg2},
				"angleOffset":{"t": "IEulerAngle","v": arg3}
		}
		state = "new"
		CM.AddPrototype(self,args, 'motionableBindDynamicObject', 0, state)


	def getColumnWidth(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getColumnWidth', 1, state)


	def getRecord(self,arg0,arg1):  # 先定义函数 
		args = {
				"row":{"t": "N","v": arg0},
				"col":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRecord', 1, state)


	def getColumnTextAttribute(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getColumnTextAttribute', 1, state)


	def setRecord(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"row":{"t": "N","v": arg0},
				"col":{"t": "N","v": arg1},
				"record":{"t": "S","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRecord', 0, state)


	def setColumnTextAttribute(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"newVal":{"t": "ITextAttribute","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setColumnTextAttribute', 0, state)


	def setColumnWidth(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"width":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setColumnWidth', 0, state)

	@property
	def borderColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["borderColor"]

	@borderColor.setter
	def borderColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "borderColor", val)
		args = {}
		args["borderColor"] = PropsTypeData.get("borderColor")
		args["borderColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"borderColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"borderColor",JsonData)

	@property
	def borderWidth(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["borderWidth"]

	@borderWidth.setter
	def borderWidth(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "borderWidth", val)
		args = {}
		args["borderWidth"] = PropsTypeData.get("borderWidth")
		args["borderWidth"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"borderWidth", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"borderWidth",JsonData)

	@property
	def columnCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["columnCount"]

	@property
	def position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"position",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "position", res)
		return PropsValueData["position"]

	@position.setter
	def position(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "position", val)
		args = {}
		args["position"] = PropsTypeData.get("position")
		args["position"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"position", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",JsonData)

	@property
	def rowCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["rowCount"]

	@property
	def tableBackgroundColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tableBackgroundColor"]

	@tableBackgroundColor.setter
	def tableBackgroundColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tableBackgroundColor", val)
		args = {}
		args["tableBackgroundColor"] = PropsTypeData.get("tableBackgroundColor")
		args["tableBackgroundColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tableBackgroundColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tableBackgroundColor",JsonData)

	@property
	def titleBackgroundColor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["titleBackgroundColor"]

	@titleBackgroundColor.setter
	def titleBackgroundColor(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "titleBackgroundColor", val)
		args = {}
		args["titleBackgroundColor"] = PropsTypeData.get("titleBackgroundColor")
		args["titleBackgroundColor"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"titleBackgroundColor", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"titleBackgroundColor",JsonData)

	@property
	def titleTextAttribute(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"titleTextAttribute",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"titleTextAttribute",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "titleTextAttribute", res)
		return PropsValueData["titleTextAttribute"]

	@titleTextAttribute.setter
	def titleTextAttribute(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "titleTextAttribute", val)
		args = {}
		args["titleTextAttribute"] = PropsTypeData.get("titleTextAttribute")
		args["titleTextAttribute"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"titleTextAttribute", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"titleTextAttribute",JsonData)

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
