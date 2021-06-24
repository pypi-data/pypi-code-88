#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"canRedo":{"t":"bool","v":False,
"F":"g"},"canUndo":{"t":"bool","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICommandManager","F":"g"}}
class ICommandManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

		#CM.AddRenderEventCB(Events)
		#CM.AddRenderEvent(this, Events)

	def initParam(self,args):
		self._canRedo=args.get("canRedo")
		self._canUndo=args.get("canUndo")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def deleteFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectClass":{"t": "IObjectClass","v": arg0},
				"oID":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteFeature', 0, state)


	def deleteFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectClass":{"t": "IObjectClass","v": arg0},
				"ids":{"t": "<N>","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteFeatures', 0, state)


	def insertFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectClass":{"t": "IObjectClass","v": arg0},
				"rowBuffer":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'insertFeature', 0, state)


	def insertFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectClass":{"t": "IObjectClass","v": arg0},
				"rowBuffers":{"t": "IRowBufferCollection","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'insertFeatures', 0, state)


	def redo(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'redo', 0, state)


	def startCommand(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'startCommand', 0, state)


	def undo(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'undo', 0, state)


	def updateFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectClass":{"t": "IObjectClass","v": arg0},
				"rowBuffer":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'updateFeature', 0, state)


	def updateFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"objectClass":{"t": "IObjectClass","v": arg0},
				"rowBuffs":{"t": "IRowBufferCollection","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'updateFeatures', 0, state)

	@property
	def canRedo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["canRedo"]

	@property
	def canUndo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["canUndo"]

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
