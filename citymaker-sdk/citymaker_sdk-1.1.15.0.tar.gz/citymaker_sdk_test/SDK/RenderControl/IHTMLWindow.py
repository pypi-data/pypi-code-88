#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IHTMLWindow","F":"g"}}
class IHTMLWindow:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def createWindowParam(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createWindowParam', 1, state)


	def deletePopupWindow(self,arg0):  # 先定义函数 
		args = {
				"winId":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deletePopupWindow', 0, state)


	def getWindowParam(self,arg0):  # 先定义函数 
		args = {
				"winId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getWindowParam', 1, state)


	def hideWindow(self,arg0):  # 先定义函数 
		args = {
				"winId":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'hideWindow', 0, state)


	def setWindowParam(self,arg0):  # 先定义函数 
		args = {
				"param":{"t": "IWindowParam","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setWindowParam', 0, state)


	def setWindowSize(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"width":{"t": "N","v": arg0},
				"height":{"t": "N","v": arg1},
				"winId":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setWindowSize', 0, state)


	def showPopupWindow(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"uRL":{"t": "S","v": arg0},
				"sizeX":{"t": "N","v": arg1},
				"sizeY":{"t": "N","v": arg2},
				"hasTitle":{"t": "B","v": arg3},
				"position":{"t": "gviHTMLWindowPosition","v": arg4},
				"round":{"t": "N","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'showPopupWindow', 0, state)


	def showPopupWindowEx(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"param":{"t": "IWindowParam","v": arg1},
				"autoComputePos":{"t": "B","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'showPopupWindowEx', 0, state)

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
				super(IHTMLWindow, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
