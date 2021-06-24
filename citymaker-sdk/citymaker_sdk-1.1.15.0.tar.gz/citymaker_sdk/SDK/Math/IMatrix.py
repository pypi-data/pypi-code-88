#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"hasMirror":{"t":"bool","v":False,
"F":"g"},"hasShear":{"t":"bool","v":False,
"F":"g"},"isIdentity":{"t":"bool","v":False,
"F":"g"},"m11":{"t":"double","v":0,
"F":"gs"},"m12":{"t":"double","v":0,
"F":"gs"},"m13":{"t":"double","v":0,
"F":"gs"},"m14":{"t":"double","v":0,
"F":"gs"},"m21":{"t":"double","v":0,
"F":"gs"},"m22":{"t":"double","v":0,
"F":"gs"},"m23":{"t":"double","v":0,
"F":"gs"},"m24":{"t":"double","v":0,
"F":"gs"},"m31":{"t":"double","v":0,
"F":"gs"},"m32":{"t":"double","v":0,
"F":"gs"},"m33":{"t":"double","v":0,
"F":"gs"},"m34":{"t":"double","v":0,
"F":"gs"},"m41":{"t":"double","v":0,
"F":"gs"},"m42":{"t":"double","v":0,
"F":"gs"},"m43":{"t":"double","v":0,
"F":"gs"},"m44":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IMatrix","F":"g"}}
class IMatrix:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._hasMirror=args.get("hasMirror")
		self._hasShear=args.get("hasShear")
		self._isIdentity=args.get("isIdentity")
		self._m11=args.get("m11")
		self._m12=args.get("m12")
		self._m13=args.get("m13")
		self._m14=args.get("m14")
		self._m21=args.get("m21")
		self._m22=args.get("m22")
		self._m23=args.get("m23")
		self._m24=args.get("m24")
		self._m31=args.get("m31")
		self._m32=args.get("m32")
		self._m33=args.get("m33")
		self._m34=args.get("m34")
		self._m41=args.get("m41")
		self._m42=args.get("m42")
		self._m43=args.get("m43")
		self._m44=args.get("m44")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def compose(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"euler":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'compose', 0, state)


	def compose2(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"rotationAngle":{"t": "N","v": arg2},
				"rotationDir":{"t": "IVector3","v": arg3},
				"shearAngle":{"t": "N","v": arg4},
				"shearDir":{"t": "IVector3","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'compose2', 0, state)


	def decompose(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"euler":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'decompose', 1, state)


	def decompose2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"rotationAngle":{"t": "N","v": arg2},
				"rotationDir":{"t": "IVector3","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'decompose2', 0, state)


	def getRotation(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRotation', 1, state)


	def getScale(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getScale', 1, state)


	def getTranslate(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getTranslate', 1, state)


	def interpolatePosition(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"mat1":{"t": "IMatrix","v": arg0},
				"velocity1":{"t": "N","v": arg1},
				"time1":{"t": "N","v": arg2},
				"mat2":{"t": "IMatrix","v": arg3},
				"velocity2":{"t": "N","v": arg4},
				"time2":{"t": "N","v": arg5},
				"time":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'interpolatePosition', 0, state)


	def inverse(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'inverse', 0, state)


	def makeIdentity(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'makeIdentity', 0, state)


	def multiplyVector(self,arg0,arg1):  # 先定义函数 
		args = {
				"src":{"t": "IVector3","v": arg0},
				"pVal":{"t": "IVector3","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'multiplyVector', 0, state)


	def set(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15):  # 先定义函数 
		args = {
				"a00":{"t": "N","v": arg0},
				"a01":{"t": "N","v": arg1},
				"a02":{"t": "N","v": arg2},
				"a03":{"t": "N","v": arg3},
				"a10":{"t": "N","v": arg4},
				"a11":{"t": "N","v": arg5},
				"a12":{"t": "N","v": arg6},
				"a13":{"t": "N","v": arg7},
				"a20":{"t": "N","v": arg8},
				"a21":{"t": "N","v": arg9},
				"a22":{"t": "N","v": arg10},
				"a23":{"t": "N","v": arg11},
				"a30":{"t": "N","v": arg12},
				"a31":{"t": "N","v": arg13},
				"a32":{"t": "N","v": arg14},
				"a33":{"t": "N","v": arg15}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)


	def setByMatrix(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IMatrix","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setByMatrix', 0, state)


	def setRotation(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IEulerAngle","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRotation', 0, state)


	def setScale(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setScale', 0, state)


	def setTranslate(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setTranslate', 0, state)


	def transpose(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'transpose', 0, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'valid', 1, state)

	@property
	def hasMirror(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasMirror"]

	@property
	def hasShear(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasShear"]

	@property
	def isIdentity(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isIdentity"]

	@property
	def m11(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m11"]

	@m11.setter
	def m11(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m11", val)
		args = {}
		args["m11"] = PropsTypeData.get("m11")
		args["m11"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m11", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m11",JsonData)

	@property
	def m12(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m12"]

	@m12.setter
	def m12(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m12", val)
		args = {}
		args["m12"] = PropsTypeData.get("m12")
		args["m12"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m12", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m12",JsonData)

	@property
	def m13(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m13"]

	@m13.setter
	def m13(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m13", val)
		args = {}
		args["m13"] = PropsTypeData.get("m13")
		args["m13"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m13", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m13",JsonData)

	@property
	def m14(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m14"]

	@m14.setter
	def m14(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m14", val)
		args = {}
		args["m14"] = PropsTypeData.get("m14")
		args["m14"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m14", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m14",JsonData)

	@property
	def m21(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m21"]

	@m21.setter
	def m21(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m21", val)
		args = {}
		args["m21"] = PropsTypeData.get("m21")
		args["m21"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m21", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m21",JsonData)

	@property
	def m22(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m22"]

	@m22.setter
	def m22(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m22", val)
		args = {}
		args["m22"] = PropsTypeData.get("m22")
		args["m22"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m22", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m22",JsonData)

	@property
	def m23(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m23"]

	@m23.setter
	def m23(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m23", val)
		args = {}
		args["m23"] = PropsTypeData.get("m23")
		args["m23"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m23", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m23",JsonData)

	@property
	def m24(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m24"]

	@m24.setter
	def m24(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m24", val)
		args = {}
		args["m24"] = PropsTypeData.get("m24")
		args["m24"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m24", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m24",JsonData)

	@property
	def m31(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m31"]

	@m31.setter
	def m31(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m31", val)
		args = {}
		args["m31"] = PropsTypeData.get("m31")
		args["m31"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m31", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m31",JsonData)

	@property
	def m32(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m32"]

	@m32.setter
	def m32(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m32", val)
		args = {}
		args["m32"] = PropsTypeData.get("m32")
		args["m32"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m32", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m32",JsonData)

	@property
	def m33(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m33"]

	@m33.setter
	def m33(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m33", val)
		args = {}
		args["m33"] = PropsTypeData.get("m33")
		args["m33"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m33", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m33",JsonData)

	@property
	def m34(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m34"]

	@m34.setter
	def m34(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m34", val)
		args = {}
		args["m34"] = PropsTypeData.get("m34")
		args["m34"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m34", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m34",JsonData)

	@property
	def m41(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m41"]

	@m41.setter
	def m41(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m41", val)
		args = {}
		args["m41"] = PropsTypeData.get("m41")
		args["m41"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m41", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m41",JsonData)

	@property
	def m42(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m42"]

	@m42.setter
	def m42(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m42", val)
		args = {}
		args["m42"] = PropsTypeData.get("m42")
		args["m42"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m42", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m42",JsonData)

	@property
	def m43(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m43"]

	@m43.setter
	def m43(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m43", val)
		args = {}
		args["m43"] = PropsTypeData.get("m43")
		args["m43"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m43", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m43",JsonData)

	@property
	def m44(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["m44"]

	@m44.setter
	def m44(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "m44", val)
		args = {}
		args["m44"] = PropsTypeData.get("m44")
		args["m44"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"m44", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"m44",JsonData)

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
