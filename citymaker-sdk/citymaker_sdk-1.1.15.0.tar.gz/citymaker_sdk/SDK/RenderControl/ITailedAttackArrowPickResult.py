#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IPickResult import IPickResult
Props={"tailedAttackArrow":{"t":"ITailedAttackArrow","v":"",
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITailedAttackArrowPickResult","F":"g"}}
class ITailedAttackArrowPickResult(IPickResult):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._tailedAttackArrow=args.get("tailedAttackArrow")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")
	@property
	def tailedAttackArrow(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tailedAttackArrow"]

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
