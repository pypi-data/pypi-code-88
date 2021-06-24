#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IAttachmentManager","F":"g"}}
class IAttachmentManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addAttachment(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IAttachment","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addAttachment', 1, state)


	def close(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'close', 0, state)


	def deleteAllAttachments(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'deleteAllAttachments', 1, state)


	def deleteAttachment(self,arg0):  # 先定义函数 
		args = {
				"attachmentId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteAttachment', 1, state)


	def deleteAttachmentsByFeatureId(self,arg0):  # 先定义函数 
		args = {
				"featureId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteAttachmentsByFeatureId', 1, state)


	def getAllAttachments(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getAllAttachments', 1, state)


	def getAttachment(self,arg0):  # 先定义函数 
		args = {
				"attachmentId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAttachment', 1, state)


	def getAttachmentsByFeatureId(self,arg0):  # 先定义函数 
		args = {
				"featureId":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAttachmentsByFeatureId', 1, state)


	def getAttachmentsByFeatureIds(self,arg0):  # 先定义函数 
		args = {
				"featureIds":{"t": "<N>","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAttachmentsByFeatureIds', 1, state)


	def getAttachmentsByIds(self,arg0):  # 先定义函数 
		args = {
				"ids":{"t": "<N>","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getAttachmentsByIds', 1, state)


	def isClosed(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'isClosed', 1, state)


	def updateAttachment(self,arg0):  # 先定义函数 
		args = {
				"attachment":{"t": "IAttachment","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'updateAttachment', 1, state)

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
