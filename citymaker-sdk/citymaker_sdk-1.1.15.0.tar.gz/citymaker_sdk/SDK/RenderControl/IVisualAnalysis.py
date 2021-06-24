#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IVisualAnalysis","F":"g"}}
class IVisualAnalysis:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addOccluder(self,arg0,arg1):  # 先定义函数 
		args = {
				"fL":{"t": "IFeatureLayer","v": arg0},
				"geo":{"t": "IGeometry","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'addOccluder', 0, state)


	def clearOccluders(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearOccluders', 0, state)


	def startShadowAnalyse(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'startShadowAnalyse', 0, state)


	def startViewshedAnalyse(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"start":{"t": "IPoint","v": arg0},
				"end":{"t": "IPoint","v": arg1},
				"horizontalAngle":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'startViewshedAnalyse', 0, state)


	def stopAnalyse(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stopAnalyse', 0, state)

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
