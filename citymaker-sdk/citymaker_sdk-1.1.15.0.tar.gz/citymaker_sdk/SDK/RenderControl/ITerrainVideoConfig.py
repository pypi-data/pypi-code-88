#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"maxRealtimeTVNum":{"t":"int","v":0,
"F":"gs"},"maxVisualFieldTVNum":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainVideoConfig","F":"g"}}
class ITerrainVideoConfig:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._maxRealtimeTVNum=args.get("maxRealtimeTVNum")
		self._maxVisualFieldTVNum=args.get("maxVisualFieldTVNum")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def setPriorityDisplay(self,arg0):  # 先定义函数 
		args = {
				"video":{"t": "ITerrainVideo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPriorityDisplay', 0, state)

	@property
	def maxRealtimeTVNum(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxRealtimeTVNum"]

	@maxRealtimeTVNum.setter
	def maxRealtimeTVNum(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxRealtimeTVNum", val)
		args = {}
		args["maxRealtimeTVNum"] = PropsTypeData.get("maxRealtimeTVNum")
		args["maxRealtimeTVNum"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxRealtimeTVNum", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxRealtimeTVNum",JsonData)

	@property
	def maxVisualFieldTVNum(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxVisualFieldTVNum"]

	@maxVisualFieldTVNum.setter
	def maxVisualFieldTVNum(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxVisualFieldTVNum", val)
		args = {}
		args["maxVisualFieldTVNum"] = PropsTypeData.get("maxVisualFieldTVNum")
		args["maxVisualFieldTVNum"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxVisualFieldTVNum", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxVisualFieldTVNum",JsonData)

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
