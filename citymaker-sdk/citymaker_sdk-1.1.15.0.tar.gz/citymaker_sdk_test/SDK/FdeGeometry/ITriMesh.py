#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.FdeGeometry.ISurface import ISurface
Props={"DirectedEdgeCount":{"t":"int","v":0,
"F":"g"},"FacetCount":{"t":"int","v":0,
"F":"g"},"VertexCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITriMesh","F":"g"}}
class ITriMesh(ISurface):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.DirectedEdgeCount=args.get("DirectedEdgeCount")
		self.FacetCount=args.get("FacetCount")
		self.VertexCount=args.get("VertexCount")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def addPoint(self,arg0):  # 先定义函数 
		args = {
				"point":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'AddPoint', 1, state)


	def addTriangle(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"handlef":{"t": "ITopoNode","v": arg0},
				"handles":{"t": "ITopoNode","v": arg1},
				"handlet":{"t": "ITopoNode","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'AddTriangle', 1, state)


	def batchExport(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'BatchExport', 1, state)


	def beginEdge(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'BeginEdge', 1, state)


	def beginFacet(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'BeginFacet', 1, state)


	def beginVertex(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'BeginVertex', 1, state)


	def endEdge(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'EndEdge', 1, state)


	def endFacet(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'EndFacet', 1, state)


	def endVertex(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'EndVertex', 1, state)


	def eraseConnectedEdge(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoDirectedEdge","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'EraseConnectedEdge', 1, state)


	def eraseConnectedFacet(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoFacet","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'EraseConnectedFacet', 1, state)


	def eraseFacet(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoFacet","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'EraseFacet', 1, state)


	def getPoint(self,arg0):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoNode","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'GetPoint', 1, state)


	def intersectPlane(self,arg0,arg1):  # 先定义函数 
		args = {
				"normal":{"t": "IVector3","v": arg0},
				"constant":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'IntersectPlane', 1, state)


	def lineSegmentIntersect(self,arg0):  # 先定义函数 
		args = {
				"line":{"t": "ILine","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'LineSegmentIntersect', 1, state)


	def locate(self,arg0):  # 先定义函数 
		args = {
				"point":{"t": "IPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Locate', 1, state)


	def rayIntersect(self,arg0,arg1):  # 先定义函数 
		args = {
				"start":{"t": "IPoint","v": arg0},
				"dir":{"t": "IVector3","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'RayIntersect', 1, state)


	def removeUnconnectedVertices(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'RemoveUnconnectedVertices', 1, state)


	def setPoint(self,arg0,arg1):  # 先定义函数 
		args = {
				"handle":{"t": "ITopoNode","v": arg0},
				"point":{"t": "IPoint","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SetPoint', 1, state)

	def __getattr__(self,name):
		if name in Props:
			attrVal=Props[name]
			if name =="_HashCode":
				return CM.dict_get(attrVal, "v", None)
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("g") > -1:
				if CP.ClassFN.get(t) is not None and "PickResult" not in Props["propertyType"]["v"] and name != "propertyType":
					PropsTypeData = CM.getPropsTypeData(self._HashCode)
					PropsValueData = CM.getPropsValueData(self._HashCode)
					jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),name,None)
					res=socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,jsonData)
					CM.addPropsValue(PropsValueData["_HashCode"], name, res)
					return PropsValueData[name]
				else:
					PropsValueData = CM.getPropsValueData(self._HashCode)
					if name == "fullScreen":
						res=CM.isFull()
					CM.addPropsValue(PropsValueData.get("_HashCode"), name, res)
					return PropsValueData[name]

	def __setattr__(self,name,value):
		if name in Props:
			attrVal=Props[name]
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("s") > -1:
				if name =="_HashCode":
					CM.dict_set(attrVal, "F", value)
					return
				PropsTypeData = CM.getPropsTypeData(self._HashCode)
				PropsValueData = CM.getPropsValueData(self._HashCode)
				CM.addPropsValue(PropsValueData.get("_HashCode"), name, value)
				if name == "fullScreen":
					res=CM.isFull()
					return
				args = {}
				args[name] = PropsTypeData.get(name)
				args[name]["v"] = value
				JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),name, args)
				socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,JsonData)
				super(ITriMesh, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
