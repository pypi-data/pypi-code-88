#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"beginCirculatorVertexAround":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITopoNode","F":"g"}}
class ITopoNode:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._beginCirculatorVertexAround=args.get("beginCirculatorVertexAround")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def circulatorNext(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'circulatorNext', 1, state)


	def equal(self,arg0):  # 先定义函数 
		args = {
				"x":{"t": "ITopoNode","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'equal', 1, state)


	def getEdge(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getEdge', 1, state)


	def getLocation(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getLocation', 1, state)


	def next(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'next', 1, state)


	def notEqual(self,arg0):  # 先定义函数 
		args = {
				"x":{"t": "ITopoNode","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'notEqual', 1, state)


	def setLocation(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IPoint","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setLocation', 0, state)

	@property
	def beginCirculatorVertexAround(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["beginCirculatorVertexAround"]

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
