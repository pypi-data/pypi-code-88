#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IResourceFactory","F":"g"}}
class IResourceFactory:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def createImageFromBinary(self,arg0):  # 先定义函数 
		args = {
				"binaryBuffer":{"t": "IBinaryBuffer","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createImageFromBinary', 1, state)


	def createImageFromFile(self,arg0):  # 先定义函数 
		args = {
				"imageFile":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createImageFromFile', 1, state)


	def createModel(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createModel', 1, state)


	def createModelAndImageFromFile(self,arg0):  # 先定义函数 
		args = {
				"modelFile":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createModelAndImageFromFile', 1, state)


	def createModelAndImageFromFileEx(self,arg0):  # 先定义函数 
		args = {
				"modelFile":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createModelAndImageFromFileEx', 1, state)


	def createModelFromBinary(self,arg0):  # 先定义函数 
		args = {
				"binaryBuffer":{"t": "IBinaryBuffer","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createModelFromBinary', 1, state)

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
