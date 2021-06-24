#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRObject import IRObject
Props={"demAvailable":{"t":"bool","v":True,
"F":"gs"},"enableAtmosphere":{"t":"bool","v":False,
"F":"gs"},"enableOceanEffect":{"t":"bool","v":True,
"F":"gs"},"isPlanarTerrain":{"t":"bool","v":True,
"F":"g"},"isRegistered":{"t":"bool","v":False,
"F":"g"},"oceanWindDirection":{"t":"double","v":0,
"F":"gs"},"oceanWindSpeed":{"t":"double","v":0,
"F":"gs"},"opacity":{"t":"double","v":1,
"F":"gs"},"supportAtmosphere":{"t":"bool","v":False,
"F":"g"},"visibleMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrain","F":"g"}}
#Events = {connectInfo:{fn:null}crsWKT:{fn:null}}
class ITerrain(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._demAvailable=args.get("demAvailable")
		self._enableAtmosphere=args.get("enableAtmosphere")
		self._enableOceanEffect=args.get("enableOceanEffect")
		self._isPlanarTerrain=args.get("isPlanarTerrain")
		self._isRegistered=args.get("isRegistered")
		self._oceanWindDirection=args.get("oceanWindDirection")
		self._oceanWindSpeed=args.get("oceanWindSpeed")
		self._opacity=args.get("opacity")
		self._supportAtmosphere=args.get("supportAtmosphere")
		self._visibleMask=args.get("visibleMask")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def findBestPath(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7):  # 先定义函数 
		args = {
				"startX":{"t": "N","v": arg0},
				"startY":{"t": "N","v": arg1},
				"endX":{"t": "N","v": arg2},
				"endY":{"t": "N","v": arg3},
				"sampleNumber":{"t": "N","v": arg4},
				"searchAreaFactor":{"t": "N","v": arg5},
				"maxClimbSlope":{"t": "N","v": arg6},
				"maxDescentSlope":{"t": "N","v": arg7}
		}
		state = ""
		return CM.AddPrototype(self,args, 'findBestPath', 1, state)


	def flyTo(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "gviTerrainActionCode","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'flyTo', 0, state)


	def getElevation(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1},
				"getAltitudeType":{"t": "gviGetElevationType","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getElevation', 1, state)


	def getInvisibleRegion(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getInvisibleRegion', 1, state)


	def getOceanRegion(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getOceanRegion', 1, state)


	def getSlope(self,arg0,arg1):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSlope', 1, state)


	def registerTerrain(self,arg0,arg1):  # 先定义函数 
		args = {
				"layerInfo":{"t": "S","v": arg0},
				"pass":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'registerTerrain', 1, state)


	def setInvisibleRegion(self,arg0):  # 先定义函数 
		args = {
				"region":{"t": "IMultiPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setInvisibleRegion', 0, state)


	def setOceanRegion(self,arg0):  # 先定义函数 
		args = {
				"region":{"t": "IMultiPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setOceanRegion', 0, state)


	def unregisterTerrain(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'unregisterTerrain', 0, state)

	@property
	def demAvailable(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["demAvailable"]

	@demAvailable.setter
	def demAvailable(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "demAvailable", val)
		args = {}
		args["demAvailable"] = PropsTypeData.get("demAvailable")
		args["demAvailable"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"demAvailable", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"demAvailable",JsonData)

	@property
	def enableAtmosphere(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["enableAtmosphere"]

	@enableAtmosphere.setter
	def enableAtmosphere(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "enableAtmosphere", val)
		args = {}
		args["enableAtmosphere"] = PropsTypeData.get("enableAtmosphere")
		args["enableAtmosphere"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"enableAtmosphere", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"enableAtmosphere",JsonData)

	@property
	def enableOceanEffect(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["enableOceanEffect"]

	@enableOceanEffect.setter
	def enableOceanEffect(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "enableOceanEffect", val)
		args = {}
		args["enableOceanEffect"] = PropsTypeData.get("enableOceanEffect")
		args["enableOceanEffect"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"enableOceanEffect", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"enableOceanEffect",JsonData)

	@property
	def isPlanarTerrain(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isPlanarTerrain"]

	@property
	def isRegistered(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isRegistered"]

	@property
	def oceanWindDirection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["oceanWindDirection"]

	@oceanWindDirection.setter
	def oceanWindDirection(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "oceanWindDirection", val)
		args = {}
		args["oceanWindDirection"] = PropsTypeData.get("oceanWindDirection")
		args["oceanWindDirection"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"oceanWindDirection", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"oceanWindDirection",JsonData)

	@property
	def oceanWindSpeed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["oceanWindSpeed"]

	@oceanWindSpeed.setter
	def oceanWindSpeed(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "oceanWindSpeed", val)
		args = {}
		args["oceanWindSpeed"] = PropsTypeData.get("oceanWindSpeed")
		args["oceanWindSpeed"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"oceanWindSpeed", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"oceanWindSpeed",JsonData)

	@property
	def opacity(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["opacity"]

	@opacity.setter
	def opacity(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "opacity", val)
		args = {}
		args["opacity"] = PropsTypeData.get("opacity")
		args["opacity"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"opacity", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"opacity",JsonData)

	@property
	def supportAtmosphere(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["supportAtmosphere"]

	@property
	def visibleMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["visibleMask"]

	@visibleMask.setter
	def visibleMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "visibleMask", val)
		args = {}
		args["visibleMask"] = PropsTypeData.get("visibleMask")
		args["visibleMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"visibleMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visibleMask",JsonData)

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
