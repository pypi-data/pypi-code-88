#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IOperation import IOperation
Props={"polygonFixedHeight":{"t":"double","v":0,
"F":"gs"},"polygonFixedHeightEnabled":{"t":"bool","v":False,
"F":"gs"},"sampleGridLength":{"t":"double","v":5.0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IVolumeMeasureOperation","F":"g"}}
class IVolumeMeasureOperation(IOperation):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._polygonFixedHeight=args.get("polygonFixedHeight")
		self._polygonFixedHeightEnabled=args.get("polygonFixedHeightEnabled")
		self._sampleGridLength=args.get("sampleGridLength")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getPolygon(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygon', 1, state)


	def getVolume(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getVolume', 1, state)


	def setPolygon(self,arg0):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPolygon', 0, state)

	@property
	def polygonFixedHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["polygonFixedHeight"]

	@polygonFixedHeight.setter
	def polygonFixedHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "polygonFixedHeight", val)
		args = {}
		args["polygonFixedHeight"] = PropsTypeData.get("polygonFixedHeight")
		args["polygonFixedHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"polygonFixedHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"polygonFixedHeight",JsonData)

	@property
	def polygonFixedHeightEnabled(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["polygonFixedHeightEnabled"]

	@polygonFixedHeightEnabled.setter
	def polygonFixedHeightEnabled(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "polygonFixedHeightEnabled", val)
		args = {}
		args["polygonFixedHeightEnabled"] = PropsTypeData.get("polygonFixedHeightEnabled")
		args["polygonFixedHeightEnabled"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"polygonFixedHeightEnabled", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"polygonFixedHeightEnabled",JsonData)

	@property
	def sampleGridLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["sampleGridLength"]

	@sampleGridLength.setter
	def sampleGridLength(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "sampleGridLength", val)
		args = {}
		args["sampleGridLength"] = PropsTypeData.get("sampleGridLength")
		args["sampleGridLength"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"sampleGridLength", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"sampleGridLength",JsonData)

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
