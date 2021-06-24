#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainAnalyse","F":"g"}}
class ITerrainAnalyse:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

		#CM.AddRenderEventCB(Events)
		#CM.AddRenderEvent(this, Events)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def calculateCutFill(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"domain":{"t": "IPolygon","v": arg0},
				"tolerance":{"t": "N","v": arg1},
				"referenceHeight":{"t": "N","v": arg2},
				"cutPolygon":{"t": "IMultiPolygon","v": arg3},
				"fillPolygon":{"t": "IMultiPolygon","v": arg4},
				"cutVolume":{"t": "N","v": arg5},
				"fillVolume":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'calculateCutFill', 0, state)


	def estimateLandslideVolumeEx(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"modelHill":{"t": "IModel","v": arg0},
				"modelSlope":{"t": "IModel","v": arg1},
				"resolution":{"t": "N","v": arg2},
				"volume":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'estimateLandslideVolumeEx', 1, state)


	def findWaterSinkBoundary(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"domain":{"t": "IPolygon","v": arg0},
				"tolerance":{"t": "N","v": arg1},
				"waterDepth":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'findWaterSinkBoundary', 1, state)


	def getSurfaceArea(self,arg0,arg1):  # 先定义函数 
		args = {
				"domain":{"t": "IPolygon","v": arg0},
				"tolerance":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSurfaceArea', 1, state)

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
