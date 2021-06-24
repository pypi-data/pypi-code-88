#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"altitude":{"t":"double","v":0,
"F":"gs"},"altitudeType":{"t":"gviAltitudeType","v":0,
"F":"gs"},"cartesian":{"t":"bool","v":False,
"F":"gs"},"distance":{"t":"double","v":0,
"F":"gs"},"heading":{"t":"double","v":0,
"F":"gs"},"roll":{"t":"double","v":0,
"F":"gs"},"tilt":{"t":"double","v":0,
"F":"gs"},"x":{"t":"double","v":0,
"F":"gs"},"y":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPosition","F":"g"}}
class IPosition:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._altitude=args.get("altitude")
		self._altitudeType=args.get("altitudeType")
		self._cartesian=args.get("cartesian")
		self._distance=args.get("distance")
		self._heading=args.get("heading")
		self._roll=args.get("roll")
		self._tilt=args.get("tilt")
		self._x=args.get("x")
		self._y=args.get("y")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def init(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1},
				"altitude":{"t": "N","v": arg2},
				"heading":{"t": "N","v": arg3},
				"tilt":{"t": "N","v": arg4},
				"roll":{"t": "N","v": arg5},
				"altitudeType":{"t": "gviAltitudeType","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'init', 0, state)

	@property
	def altitude(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["altitude"]

	@altitude.setter
	def altitude(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "altitude", val)
		args = {}
		args["altitude"] = PropsTypeData.get("altitude")
		args["altitude"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"altitude", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"altitude",JsonData)

	@property
	def altitudeType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["altitudeType"]

	@altitudeType.setter
	def altitudeType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "altitudeType", val)
		args = {}
		args["altitudeType"] = PropsTypeData.get("altitudeType")
		args["altitudeType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"altitudeType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"altitudeType",JsonData)

	@property
	def cartesian(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["cartesian"]

	@cartesian.setter
	def cartesian(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "cartesian", val)
		args = {}
		args["cartesian"] = PropsTypeData.get("cartesian")
		args["cartesian"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"cartesian", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"cartesian",JsonData)

	@property
	def distance(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["distance"]

	@distance.setter
	def distance(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "distance", val)
		args = {}
		args["distance"] = PropsTypeData.get("distance")
		args["distance"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"distance", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"distance",JsonData)

	@property
	def heading(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["heading"]

	@heading.setter
	def heading(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "heading", val)
		args = {}
		args["heading"] = PropsTypeData.get("heading")
		args["heading"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"heading", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"heading",JsonData)

	@property
	def roll(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["roll"]

	@roll.setter
	def roll(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "roll", val)
		args = {}
		args["roll"] = PropsTypeData.get("roll")
		args["roll"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"roll", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"roll",JsonData)

	@property
	def tilt(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tilt"]

	@tilt.setter
	def tilt(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tilt", val)
		args = {}
		args["tilt"] = PropsTypeData.get("tilt")
		args["tilt"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tilt", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tilt",JsonData)

	@property
	def x(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["x"]

	@x.setter
	def x(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "x", val)
		args = {}
		args["x"] = PropsTypeData.get("x")
		args["x"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"x", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"x",JsonData)

	@property
	def y(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["y"]

	@y.setter
	def y(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "y", val)
		args = {}
		args["y"] = PropsTypeData.get("y")
		args["y"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"y", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"y",JsonData)

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
