#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ICoordinateReferenceSystem import ICoordinateReferenceSystem
Props={"highPrecision":{"t":"bool","v":False,
"F":"gs"},"mResolution":{"t":"double","v":0,
"F":"gs"},"mTolerance":{"t":"double","v":0,
"F":"gs"},"xYResolution":{"t":"double","v":0,
"F":"gs"},"xYTolerance":{"t":"double","v":0,
"F":"gs"},"zResolution":{"t":"double","v":0,
"F":"gs"},"zTolerance":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISpatialCRS","F":"g"}}
class ISpatialCRS(ICoordinateReferenceSystem):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._highPrecision=args.get("highPrecision")
		self._mResolution=args.get("mResolution")
		self._mTolerance=args.get("mTolerance")
		self._xYResolution=args.get("xYResolution")
		self._xYTolerance=args.get("xYTolerance")
		self._zResolution=args.get("zResolution")
		self._zTolerance=args.get("zTolerance")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def constructFromHorizon(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'constructFromHorizon', 0, state)


	def isPrecisionEqual(self,arg0):  # 先定义函数 
		args = {
				"src":{"t": "ISpatialCRS","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isPrecisionEqual', 1, state)


	def setDefaultMResolution(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultMResolution', 0, state)


	def setDefaultMTolerance(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultMTolerance', 0, state)


	def setDefaultXYResolution(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultXYResolution', 0, state)


	def setDefaultXYTolerance(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultXYTolerance', 0, state)


	def setDefaultZResolution(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultZResolution', 0, state)


	def setDefaultZTolerance(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'setDefaultZTolerance', 0, state)

	@property
	def highPrecision(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["highPrecision"]

	@highPrecision.setter
	def highPrecision(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "highPrecision", val)
		args = {}
		args["highPrecision"] = PropsTypeData.get("highPrecision")
		args["highPrecision"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"highPrecision", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"highPrecision",JsonData)

	@property
	def mResolution(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["mResolution"]

	@mResolution.setter
	def mResolution(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "mResolution", val)
		args = {}
		args["mResolution"] = PropsTypeData.get("mResolution")
		args["mResolution"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"mResolution", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"mResolution",JsonData)

	@property
	def mTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["mTolerance"]

	@mTolerance.setter
	def mTolerance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "mTolerance", val)
		args = {}
		args["mTolerance"] = PropsTypeData.get("mTolerance")
		args["mTolerance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"mTolerance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"mTolerance",JsonData)

	@property
	def xYResolution(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["xYResolution"]

	@xYResolution.setter
	def xYResolution(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "xYResolution", val)
		args = {}
		args["xYResolution"] = PropsTypeData.get("xYResolution")
		args["xYResolution"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"xYResolution", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"xYResolution",JsonData)

	@property
	def xYTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["xYTolerance"]

	@xYTolerance.setter
	def xYTolerance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "xYTolerance", val)
		args = {}
		args["xYTolerance"] = PropsTypeData.get("xYTolerance")
		args["xYTolerance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"xYTolerance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"xYTolerance",JsonData)

	@property
	def zResolution(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["zResolution"]

	@zResolution.setter
	def zResolution(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "zResolution", val)
		args = {}
		args["zResolution"] = PropsTypeData.get("zResolution")
		args["zResolution"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"zResolution", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"zResolution",JsonData)

	@property
	def zTolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["zTolerance"]

	@zTolerance.setter
	def zTolerance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "zTolerance", val)
		args = {}
		args["zTolerance"] = PropsTypeData.get("zTolerance")
		args["zTolerance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"zTolerance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"zTolerance",JsonData)

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
