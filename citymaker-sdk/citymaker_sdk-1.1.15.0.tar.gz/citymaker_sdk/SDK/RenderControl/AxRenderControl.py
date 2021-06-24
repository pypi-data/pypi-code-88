#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderControl import IRenderControl
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"AxRenderControl","F":"g"}}
class AxRenderControl(IRenderControl):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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
