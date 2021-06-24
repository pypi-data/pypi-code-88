#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderable import IRenderable
Props={"arrowType":{"t":"gviArrowType","v":0,
"F":"gs"},"bottomWidth":{"t":"double","v":3.0,
"F":"gs"},"chordHeight":{"t":"double","v":1.0,
"F":"gs"},"dualArrowFollow":{"t":"bool","v":True,
"F":"gs"},"headHeight":{"t":"double","v":1.0,
"F":"gs"},"symbol":{"t":"ISurfaceSymbol","v":None,
"F":"gs"},"tolerance":{"t":"double","v":0.01,
"F":"gs"},"wingAngle":{"t":"double","v":0.7853981633974483,
"F":"gs"},"wingBottomLength":{"t":"double","v":0.5,
"F":"gs"},"wingLength":{"t":"double","v":0.5,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IRenderArrow","F":"g"}}
class IRenderArrow(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._arrowType=args.get("arrowType")
		self._bottomWidth=args.get("bottomWidth")
		self._chordHeight=args.get("chordHeight")
		self._dualArrowFollow=args.get("dualArrowFollow")
		self._headHeight=args.get("headHeight")
		self._symbol=args.get("symbol")
		self._tolerance=args.get("tolerance")
		self._wingAngle=args.get("wingAngle")
		self._wingBottomLength=args.get("wingBottomLength")
		self._wingLength=args.get("wingLength")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addPoint(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IPoint","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addPoint', 0, state)

	@property
	def arrowType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["arrowType"]

	@arrowType.setter
	def arrowType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "arrowType", val)
		args = {}
		args["arrowType"] = PropsTypeData.get("arrowType")
		args["arrowType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"arrowType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"arrowType",JsonData)

	@property
	def bottomWidth(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["bottomWidth"]

	@bottomWidth.setter
	def bottomWidth(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "bottomWidth", val)
		args = {}
		args["bottomWidth"] = PropsTypeData.get("bottomWidth")
		args["bottomWidth"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"bottomWidth", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"bottomWidth",JsonData)

	@property
	def chordHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["chordHeight"]

	@chordHeight.setter
	def chordHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "chordHeight", val)
		args = {}
		args["chordHeight"] = PropsTypeData.get("chordHeight")
		args["chordHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"chordHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"chordHeight",JsonData)

	@property
	def dualArrowFollow(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["dualArrowFollow"]

	@dualArrowFollow.setter
	def dualArrowFollow(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "dualArrowFollow", val)
		args = {}
		args["dualArrowFollow"] = PropsTypeData.get("dualArrowFollow")
		args["dualArrowFollow"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"dualArrowFollow", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"dualArrowFollow",JsonData)

	@property
	def headHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["headHeight"]

	@headHeight.setter
	def headHeight(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "headHeight", val)
		args = {}
		args["headHeight"] = PropsTypeData.get("headHeight")
		args["headHeight"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"headHeight", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"headHeight",JsonData)

	@property
	def symbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"symbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"symbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "symbol", res)
		return PropsValueData["symbol"]

	@symbol.setter
	def symbol(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "symbol", val)
		args = {}
		args["symbol"] = PropsTypeData.get("symbol")
		args["symbol"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"symbol", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"symbol",JsonData)

	@property
	def tolerance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tolerance"]

	@tolerance.setter
	def tolerance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tolerance", val)
		args = {}
		args["tolerance"] = PropsTypeData.get("tolerance")
		args["tolerance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tolerance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tolerance",JsonData)

	@property
	def wingAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["wingAngle"]

	@wingAngle.setter
	def wingAngle(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "wingAngle", val)
		args = {}
		args["wingAngle"] = PropsTypeData.get("wingAngle")
		args["wingAngle"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"wingAngle", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"wingAngle",JsonData)

	@property
	def wingBottomLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["wingBottomLength"]

	@wingBottomLength.setter
	def wingBottomLength(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "wingBottomLength", val)
		args = {}
		args["wingBottomLength"] = PropsTypeData.get("wingBottomLength")
		args["wingBottomLength"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"wingBottomLength", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"wingBottomLength",JsonData)

	@property
	def wingLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["wingLength"]

	@wingLength.setter
	def wingLength(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "wingLength", val)
		args = {}
		args["wingLength"] = PropsTypeData.get("wingLength")
		args["wingLength"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"wingLength", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"wingLength",JsonData)

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
