#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit as socketApi 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGlobal","F":"g"}}
class IGlobal:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def setSelectFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"fL":{"t": "G","v": arg0},
				"selectFID":{"t": "N","v": arg1}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setSelectFeature', 0, state)


	def setCurFeatureLayer(self,arg0):  # 先定义函数 
		args = {
				"guid":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setCurFeatureLayer', 0, state)


	def getCurGroupID(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'GetCurGroupID', 1, state)


	def setCurGroupID(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setCurGroupID', 0, state)


	def importModelLibraryInfo(self,arg0):  # 先定义函数 
		args = {
				"xmlPath":{"t": "S","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'ImportModelLibraryInfo', 1, state)

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
