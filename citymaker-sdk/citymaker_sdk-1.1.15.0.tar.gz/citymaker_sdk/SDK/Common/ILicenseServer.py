#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"hasRuntimeLicense":{"t":"bool","v":False,
"F":"g"},"remainingLicenses":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ILicenseServer","F":"g"}}
class ILicenseServer:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._hasRuntimeLicense=args.get("hasRuntimeLicense")
		self._remainingLicenses=args.get("remainingLicenses")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def enableTrial(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'enableTrial', 0, state)


	def getSignatureCode(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getSignatureCode', 1, state)


	def setHost(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"server":{"t": "S","v": arg0},
				"port":{"t": "N","v": arg1},
				"password":{"t": "S","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setHost', 0, state)

	@property
	def hasRuntimeLicense(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasRuntimeLicense"]

	@property
	def remainingLicenses(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["remainingLicenses"]

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
