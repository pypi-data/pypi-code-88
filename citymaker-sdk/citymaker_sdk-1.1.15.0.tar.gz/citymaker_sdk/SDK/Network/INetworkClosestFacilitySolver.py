#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.Network.INetworkSolver import INetworkSolver
Props={"eventLocationCount":{"t":"int","v":0,
"F":"g"},"facilityLocationCount":{"t":"int","v":0,
"F":"g"},"routeCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkClosestFacilitySolver","F":"g"}}
class INetworkClosestFacilitySolver(INetworkSolver):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._eventLocationCount=args.get("eventLocationCount")
		self._facilityLocationCount=args.get("facilityLocationCount")
		self._routeCount=args.get("routeCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addEventLocation(self,arg0):  # 先定义函数 
		args = {
				"nel":{"t": "INetworkEventLocation","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addEventLocation', 0, state)


	def addFacilityLocation(self,arg0):  # 先定义函数 
		args = {
				"nl":{"t": "INetworkLocation","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addFacilityLocation', 0, state)


	def clearEventLocations(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearEventLocations', 0, state)


	def clearFacilityLocations(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearFacilityLocations', 0, state)


	def getEventLocation(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEventLocation', 1, state)


	def getFacilityLocation(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFacilityLocation', 1, state)


	def getRoute(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRoute', 1, state)


	def loadFacilityLocationFromFeatureClass(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"queryFilter":{"t": "IQueryFilter","v": arg1},
				"geoColumnName":{"t": "S","v": arg2},
				"facilityNameColumn":{"t": "S","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'loadFacilityLocationFromFeatureClass', 0, state)

	@property
	def eventLocationCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["eventLocationCount"]

	@property
	def facilityLocationCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["facilityLocationCount"]

	@property
	def routeCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["routeCount"]

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
