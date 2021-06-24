#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeCore.IObjectClass import IObjectClass
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureClass","F":"g"}}
class IFeatureClass(IObjectClass):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def spatialIntersects(self,arg0):  # 先定义函数 
		args = {
				"fid":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'spatialIntersects', 1, state)


	def getfieldNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getfieldNames', 1, state)


	def getRowBuffers(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRowBuffers', 1, state)


	def getDataTable(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getDataTable', 1, state)


	def addRenderIndex(self,arg0):  # 先定义函数 
		args = {
				"indexInfo":{"t": "IRenderIndexInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addRenderIndex', 0, state)


	def addSpatialIndex(self,arg0):  # 先定义函数 
		args = {
				"indexInfo":{"t": "IIndexInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addSpatialIndex', 0, state)


	def calculateDefaultGridIndex(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'calculateDefaultGridIndex', 1, state)


	def calculateDefaultRenderIndex(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'calculateDefaultRenderIndex', 1, state)


	def calculateExtent(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'calculateExtent', 1, state)


	def deleteRenderIndex(self,arg0):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteRenderIndex', 0, state)


	def deleteSpatialIndex(self,arg0):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteSpatialIndex', 0, state)


	def getFeaturesEnvelope(self,arg0,arg1):  # 先定义函数 
		args = {
				"fidArray":{"t": "<N>","v": arg0},
				"geoField":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFeaturesEnvelope', 1, state)


	def getRenderIndexInfos(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRenderIndexInfos', 1, state)


	def getSpatialIndexInfos(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getSpatialIndexInfos', 1, state)


	def purgeGeometry(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'purgeGeometry', 0, state)


	def rebuildRenderIndex(self,arg0,arg1):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0},
				"rebuildType":{"t": "gviRenderIndexRebuildType","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'rebuildRenderIndex', 0, state)


	def rebuildSpatialIndex(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'rebuildSpatialIndex', 0, state)


	def setRenderIndexEnabled(self,arg0,arg1):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0},
				"enabled":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRenderIndexEnabled', 0, state)


	def updateExtent(self,arg0):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'updateExtent', 0, state)

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
