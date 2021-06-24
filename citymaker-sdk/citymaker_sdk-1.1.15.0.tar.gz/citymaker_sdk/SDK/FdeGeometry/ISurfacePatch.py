#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ISurface import ISurface
Props={"surfaceInterpolationType":{"t":"gviSurfaceInterpolationType","v":3,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ISurfacePatch","F":"g"}}
class ISurfacePatch(ISurface):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._surfaceInterpolationType=args.get("surfaceInterpolationType")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def convert2Mesh(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'convert2Mesh', 1, state)

	@property
	def surfaceInterpolationType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["surfaceInterpolationType"]

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
