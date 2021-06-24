#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureManager","F":"g"}}
class IFeatureManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def stopFeatureLayerTime(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'stopFeatureLayerTime', 1, state)


	def setFeatureLayerTime(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"startTime":{"t": "S","v": arg0},
				"endTime":{"t": "S","v": arg1},
				"playSpeed":{"t": "Number","v": arg2},
				"interval":{"t": "Number","v": arg3},
				"intervalType":{"t": "S","v": arg4}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'setFeatureLayerTime', 1, state)


	def getFeaturesFromBaseLyr(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc_name":{"t": "S","v": arg0},
				"spatialRel":{"t": "gviSpatialRel","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getFeaturesFromBaseLyr', 1, state)


	def getFeaturesFromBaseLyr2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"fc_name":{"t": "S","v": arg0},
				"geoType":{"t": "gviGeometryType","v": arg1},
				"spatialRel":{"t": "gviSpatialRel","v": arg2},
				"position":{"t": "<IVector3>","v": arg3}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getFeaturesFromBaseLyr2', 1, state)


	def getFeatureQuery(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc_name":{"t": "S","v": arg0},
				"queryFilter":{"t": "S","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getFeatureQuery', 1, state)


	def createFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"rb":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFeature', 1, state)


	def createFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"rbs":{"t": "IRowBufferCollection","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFeatures', 1, state)


	def deleteFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"ids":{"t": "<N>","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteFeatures', 1, state)


	def editFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"rb":{"t": "IRowBuffer","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'editFeature', 1, state)


	def editFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"rbs":{"t": "IRowBufferCollection","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'editFeatures', 1, state)


	def highlightFeature(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"featureId":{"t": "N","v": arg1},
				"cv":{"t": "S","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'highlightFeature', 1, state)


	def highlightFeatures(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"fids":{"t": "<N>","v": arg1},
				"cv":{"t": "S","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'highlightFeatures', 1, state)


	def refreshAll(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'refreshAll', 0, state)


	def refreshFeatureClass(self,arg0):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'refreshFeatureClass', 0, state)


	def resetAllVisibleMask(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'resetAllVisibleMask', 1, state)


	def resetFeatureClassVisibleMask(self,arg0):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'resetFeatureClassVisibleMask', 1, state)


	def resetFeatureVisibleMask(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"featureId":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'resetFeatureVisibleMask', 1, state)


	def setFeaturesVisibleMask(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"fids":{"t": "<N>","v": arg1},
				"visibleMask":{"t": "gviViewportMask","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setFeaturesVisibleMask', 1, state)


	def setFeatureVisibleMask(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"featureId":{"t": "N","v": arg1},
				"visibleMask":{"t": "gviViewportMask","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setFeatureVisibleMask', 1, state)


	def unhighlightAll(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightAll', 1, state)


	def unhighlightFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"featureId":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightFeature', 1, state)


	def unhighlightFeatureClass(self,arg0):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightFeatureClass', 1, state)


	def unhighlightFeatures(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"fids":{"t": "<N>","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'unhighlightFeatures', 1, state)


	def deleteFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"fid":{"t": "Number","v": arg0},
				"mode":{"t": "Number","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'deleteFeature', 1, state)

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
