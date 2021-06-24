#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.IReplication import IReplication
Props={"masterConnectionInfo":{"t":"IConnectionInfo","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICheckIn","F":"g"}}
class ICheckIn(IReplication):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._masterConnectionInfo=args.get("masterConnectionInfo")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def checkIn(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'checkIn', 0, state)


	def commit(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'commit', 0, state)


	def undoCheckOut(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'undoCheckOut', 0, state)


	def validate(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'validate', 0, state)

	@property
	def masterConnectionInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"masterConnectionInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"masterConnectionInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "masterConnectionInfo", res)
		return PropsValueData["masterConnectionInfo"]

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
