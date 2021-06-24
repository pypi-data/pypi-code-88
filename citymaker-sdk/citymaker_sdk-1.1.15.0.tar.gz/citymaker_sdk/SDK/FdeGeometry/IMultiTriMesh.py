#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.IGeometryCollection import IGeometryCollection
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IMultiTriMesh","F":"g"}}
class IMultiTriMesh(IGeometryCollection):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addSurface(self,arg0):  # 先定义函数 
		args = {
				"surface":{"t": "ISurface","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addSurface', 1, state)


	def generalize(self,arg0):  # 先定义函数 
		args = {
				"maxAllowOffset":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'generalize', 1, state)


	def getArea(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getArea', 1, state)


	def addTriMesh(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "ITriMesh","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addTriMesh', 1, state)


	def getTriMesh(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getTriMesh', 1, state)


	def lineSegmentIntersect(self,arg0):  # 先定义函数 
		args = {
				"line":{"t": "ILine","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'lineSegmentIntersect', 1, state)


	def rayIntersect(self,arg0,arg1):  # 先定义函数 
		args = {
				"start":{"t": "IPoint","v": arg0},
				"dir":{"t": "IVector3","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'rayIntersect', 1, state)

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
