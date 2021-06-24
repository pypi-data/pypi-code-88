#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureClassQuery","F":"g"}}
class IFeatureClassQuery:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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
