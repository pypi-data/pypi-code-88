#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ICurve import ICurve
Props={"centerPoint":{"t":"IPoint","v":None,
"F":"g"},"centralAngle":{"t":"double","v":0,
"F":"g"},"chordHeight":{"t":"double","v":0,
"F":"g"},"chordLength":{"t":"double","v":0,
"F":"g"},"isLine":{"t":"bool","v":False,
"F":"g"},"isMinor":{"t":"bool","v":False,
"F":"g"},"isPoint":{"t":"bool","v":False,
"F":"g"},"pointOnArc":{"t":"IPoint","v":None,
"F":"gs"},"radius":{"t":"double","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICirculeArc","F":"g"}}
class ICirculeArc(ICurve):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._centerPoint=args.get("centerPoint")
		self._centralAngle=args.get("centralAngle")
		self._chordHeight=args.get("chordHeight")
		self._chordLength=args.get("chordLength")
		self._isLine=args.get("isLine")
		self._isMinor=args.get("isMinor")
		self._isPoint=args.get("isPoint")
		self._pointOnArc=args.get("pointOnArc")
		self._radius=args.get("radius")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def moveModel(self,arg0):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'moveModel', 1, state)


	def rotateModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'rotateModel', 1, state)


	def scaleModel(self,arg0):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'scaleModel', 1, state)


	def moveFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0},
				"mode":{"t": "Number","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'moveFeature', 1, state)


	def rotateFeature(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"mode":{"t": "Number","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'rotateFeature', 1, state)


	def scaleFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0},
				"mode":{"t": "Number","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'scaleFeature', 1, state)


	def move2D(self,arg0,arg1):  # 先定义函数 
		args = {
				"dX":{"t": "N","v": arg0},
				"dY":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'move2D', 0, state)


	def move3D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"dX":{"t": "N","v": arg0},
				"dY":{"t": "N","v": arg1},
				"dZ":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'move3D', 0, state)


	def rotate2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"centerX":{"t": "N","v": arg0},
				"centerY":{"t": "N","v": arg1},
				"angle":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'rotate2D', 0, state)


	def rotate3D(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"axisX":{"t": "N","v": arg0},
				"axisY":{"t": "N","v": arg1},
				"axisZ":{"t": "N","v": arg2},
				"centerX":{"t": "N","v": arg3},
				"centerY":{"t": "N","v": arg4},
				"centerZ":{"t": "N","v": arg5},
				"angle":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'rotate3D', 0, state)


	def scale2D(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"centerX":{"t": "N","v": arg2},
				"centerY":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'scale2D', 0, state)


	def scale3D(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"scaleZ":{"t": "N","v": arg2},
				"centerX":{"t": "N","v": arg3},
				"centerY":{"t": "N","v": arg4},
				"centerZ":{"t": "N","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'scale3D', 0, state)


	def constructThreePoints(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fromPoint":{"t": "IPoint","v": arg0},
				"arcPoint":{"t": "IPoint","v": arg1},
				"toPoint":{"t": "IPoint","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'constructThreePoints', 0, state)

	@property
	def centerPoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"centerPoint",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"centerPoint",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "centerPoint", res)
		return PropsValueData["centerPoint"]

	@property
	def centralAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["centralAngle"]

	@property
	def chordHeight(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["chordHeight"]

	@property
	def chordLength(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["chordLength"]

	@property
	def isLine(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isLine"]

	@property
	def isMinor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isMinor"]

	@property
	def isPoint(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isPoint"]

	@property
	def pointOnArc(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"pointOnArc",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pointOnArc",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "pointOnArc", res)
		return PropsValueData["pointOnArc"]

	@pointOnArc.setter
	def pointOnArc(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "pointOnArc", val)
		args = {}
		args["pointOnArc"] = PropsTypeData.get("pointOnArc")
		args["pointOnArc"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"pointOnArc", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"pointOnArc",JsonData)

	@property
	def radius(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["radius"]

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
