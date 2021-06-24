#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ICurve import ICurve
Props={"pointCount":{"t":"int","v":0,
"F":"g"},"segmentCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICompoundLine","F":"g"}}
class ICompoundLine(ICurve):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._pointCount=args.get("pointCount")
		self._segmentCount=args.get("segmentCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addPointAfter(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"pointValue":{"t": "IPoint","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addPointAfter', 1, state)


	def addPointBefore(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"pointValue":{"t": "IPoint","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addPointBefore', 1, state)


	def addSegmentAfter(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"segment":{"t": "ISegment","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addSegmentAfter', 1, state)


	def addSegmentBefore(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"segment":{"t": "ISegment","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addSegmentBefore', 1, state)


	def appendPoint(self,arg0):  # 先定义函数 
		args = {
				"pointValue":{"t": "IPoint","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'appendPoint', 0, state)


	def appendSegment(self,arg0):  # 先定义函数 
		args = {
				"segment":{"t": "ISegment","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'appendSegment', 1, state)


	def generalize(self,arg0):  # 先定义函数 
		args = {
				"maxAllowOffset":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'generalize', 0, state)


	def getPoint(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPoint', 1, state)


	def getSegment(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSegment', 1, state)


	def removePoints(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"count":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'removePoints', 1, state)


	def removeSegments(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"count":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'removeSegments', 1, state)


	def segmentsChanged(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'segmentsChanged', 0, state)


	def smooth(self,arg0):  # 先定义函数 
		args = {
				"maxAllowOffset":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'smooth', 0, state)


	def smoothLocal(self,arg0):  # 先定义函数 
		args = {
				"vertexIndex":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'smoothLocal', 0, state)


	def updatePoint(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"pointValue":{"t": "IPoint","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'updatePoint', 1, state)


	def updateSegment(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"segment":{"t": "ISegment","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'updateSegment', 1, state)

	@property
	def pointCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["pointCount"]

	@property
	def segmentCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["segmentCount"]

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
