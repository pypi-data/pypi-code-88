#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"isImageEncrypted":{"t":"bool","v":False,
"F":"g"},"isModelEncrypted":{"t":"bool","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IResourceManager","F":"g"}}
class IResourceManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._isImageEncrypted=args.get("isImageEncrypted")
		self._isModelEncrypted=args.get("isModelEncrypted")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addImage(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"image":{"t": "IImage","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addImage', 1, state)


	def addModel(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"model":{"t": "IModel","v": arg1},
				"simplifiedModel":{"t": "IModel","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addModel', 1, state)


	def checkResourceName(self,arg0):  # 先定义函数 
		args = {
				"resourceName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'checkResourceName', 1, state)


	def deleteImage(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteImage', 1, state)


	def deleteModel(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteModel', 1, state)


	def encryptImage(self,arg0):  # 先定义函数 
		args = {
				"password":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'encryptImage', 1, state)


	def encryptModel(self,arg0):  # 先定义函数 
		args = {
				"password":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'encryptModel', 1, state)


	def getImage(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getImage', 1, state)


	def getImageCount(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getImageCount', 1, state)


	def getImageLastUpdateTime(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getImageLastUpdateTime', 1, state)


	def getImageNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getImageNames', 1, state)


	def getModel(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getModel', 1, state)


	def getModelCount(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getModelCount', 1, state)


	def getModelLastUpdateTime(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getModelLastUpdateTime', 1, state)


	def getModelNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getModelNames', 1, state)


	def getSimplifiedModel(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSimplifiedModel', 1, state)


	def imageExist(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'imageExist', 1, state)


	def modelExist(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'modelExist', 1, state)


	def rebuildSimplifiedModel(self,arg0):  # 先定义函数 
		args = {
				"modelName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'rebuildSimplifiedModel', 1, state)


	def updateImage(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"image":{"t": "IImage","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'updateImage', 1, state)


	def updateModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"model":{"t": "IModel","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'updateModel', 1, state)


	def updateSimplifiedModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0},
				"model":{"t": "IModel","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'updateSimplifiedModel', 1, state)


	def writeModelAndImageToFile(self,arg0,arg1):  # 先定义函数 
		args = {
				"modelName":{"t": "S","v": arg0},
				"fileName":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'writeModelAndImageToFile', 1, state)

	@property
	def isImageEncrypted(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isImageEncrypted"]

	@property
	def isModelEncrypted(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isModelEncrypted"]

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
