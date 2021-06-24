#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"currentFeatureCount":{"t":"int","v":0,
"F":"g"},"currentOperation":{"t":"gviReplicateOperation","v":0,
"F":"g"},"operationCount":{"t":"int","v":0,
"F":"g"},"operations":{"t":"gviReplicateOperation","v":0,
"F":"g"},"totalFeatureCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureProgress","F":"g"}}
#Events = {featureOwner:{fn:null}}
class IFeatureProgress:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._currentFeatureCount=args.get("currentFeatureCount")
		self._currentOperation=args.get("currentOperation")
		self._operationCount=args.get("operationCount")
		self._operations=args.get("operations")
		self._totalFeatureCount=args.get("totalFeatureCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def cancel(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'cancel', 0, state)

	@property
	def currentFeatureCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["currentFeatureCount"]

	@property
	def currentOperation(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["currentOperation"]

	@property
	def operationCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["operationCount"]

	@property
	def operations(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["operations"]

	@property
	def totalFeatureCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["totalFeatureCount"]

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
