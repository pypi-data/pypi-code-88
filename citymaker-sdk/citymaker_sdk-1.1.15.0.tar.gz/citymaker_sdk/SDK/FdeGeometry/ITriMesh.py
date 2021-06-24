#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ISurface import ISurface
Props={"directedEdgeCount":{"t":"int","v":0,
"F":"g"},"facetCount":{"t":"int","v":0,
"F":"g"},"vertexCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITriMesh","F":"g"}}
class ITriMesh(ISurface):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._directedEdgeCount=args.get("directedEdgeCount")
		self._facetCount=args.get("facetCount")
		self._vertexCount=args.get("vertexCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addPoint(self,arg0):  # 先定义函数 
		args = {
				"point":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addPoint', 1, state)


	def addTriangle(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"handlef":{"t": "ITopoNode","v": arg0},
				"handles":{"t": "ITopoNode","v": arg1},
				"handlet":{"t": "ITopoNode","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addTriangle', 1, state)


	def batchExport(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'batchExport', 1, state)


	def beginEdge(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'beginEdge', 1, state)


	def beginFacet(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'beginFacet', 1, state)


	def beginVertex(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'beginVertex', 1, state)


	def endEdge(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'endEdge', 1, state)


	def endFacet(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'endFacet', 1, state)


	def endVertex(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'endVertex', 1, state)


	def eraseConnectedEdge(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoDirectedEdge","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'eraseConnectedEdge', 1, state)


	def eraseConnectedFacet(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoFacet","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'eraseConnectedFacet', 1, state)


	def eraseFacet(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoFacet","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'eraseFacet', 1, state)


	def getPoint(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoNode","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPoint', 1, state)


	def intersectPlane(self,arg0,arg1):  # 先定义函数 
		args = {
				"normal":{"t": "IVector3","v": arg0},
				"constant":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'intersectPlane', 1, state)


	def lineSegmentIntersect(self,arg0):  # 先定义函数 
		args = {
				"line":{"t": "ILine","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'lineSegmentIntersect', 1, state)


	def locate(self,arg0):  # 先定义函数 
		args = {
				"point":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'locate', 1, state)


	def rayIntersect(self,arg0,arg1):  # 先定义函数 
		args = {
				"start":{"t": "IPoint","v": arg0},
				"dir":{"t": "IVector3","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'rayIntersect', 1, state)


	def removeUnconnectedVertices(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'removeUnconnectedVertices', 1, state)


	def setPoint(self,arg0,arg1):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoNode","v": arg0},
				"point":{"t": "IPoint","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setPoint', 1, state)

	@property
	def directedEdgeCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["directedEdgeCount"]

	@property
	def facetCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["facetCount"]

	@property
	def vertexCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["vertexCount"]

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
