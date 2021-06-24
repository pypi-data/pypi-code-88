#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"needSave":{"t":"bool","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IProject","F":"g"}}
#Events = {name:{fn:null}}
class IProject:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._needSave=args.get("needSave")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addExternalFile(self,arg0,arg1):  # 先定义函数 
		args = {
				"key":{"t": "S","v": arg0},
				"originalFilePath":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addExternalFile', 1, state)


	def close(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'close', 1, state)


	def deleteExternalFile(self,arg0):  # 先定义函数 
		args = {
				"key":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteExternalFile', 1, state)


	def getExternalFileRealPath(self,arg0):  # 先定义函数 
		args = {
				"key":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getExternalFileRealPath', 1, state)


	def packReplaceConnectionString(self,arg0,arg1):  # 先定义函数 
		args = {
				"oldString":{"t": "S","v": arg0},
				"newString":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'packReplaceConnectionString', 0, state)


	def save(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'save', 0, state)


	def open(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"projectPath":{"t": "S","v": arg0},
				"showProgress":{"t": "B","v": arg1},
				"password":{"t": "S","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'open', 1, state)


	def saveAs(self,arg0):  # 先定义函数 
		args = {
				"projectFileName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'saveAs', 1, state)

	@property
	def needSave(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["needSave"]

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
