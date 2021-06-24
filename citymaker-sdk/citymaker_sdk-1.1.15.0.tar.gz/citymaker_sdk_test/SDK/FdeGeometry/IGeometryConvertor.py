#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometryConvertor","F":"g"}}
class IGeometryConvertor:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def cutModelPointByPolygon2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'CutModelPointByPolygon2D', 1, state)


	def cutModelPointByPolygon2DWithZ(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2},
				"minZ":{"t": "N","v": arg3},
				"maxZ":{"t": "N","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'CutModelPointByPolygon2DWithZ', 1, state)


	def cutTriMeshToPolygon(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0},
				"heightSpec":{"t": "N","v": arg1},
				"tol":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'CutTriMeshToPolygon', 1, state)


	def extrudePolygonToModel(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"floorNumber":{"t": "N","v": arg1},
				"floorHeight":{"t": "N","v": arg2},
				"slopeAngle":{"t": "N","v": arg3},
				"roofType":{"t": "gviRoofType","v": arg4},
				"facadeTextureName":{"t": "S","v": arg5},
				"roofTextureName":{"t": "S","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'ExtrudePolygonToModel', 1, state)


	def extrudePolygonToTriMesh(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"height":{"t": "N","v": arg1},
				"closed":{"t": "B","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'ExtrudePolygonToTriMesh', 1, state)


	def getSolidProfile(self,arg0,arg1):  # 先定义函数 
		args = {
				"closedTriMesh":{"t": "ITriMesh","v": arg0},
				"polygon":{"t": "IPolygon","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'GetSolidProfile', 1, state)


	def getSolidProfile2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"modelSrc":{"t": "IModel","v": arg0},
				"modelPointSrc":{"t": "IModelPoint","v": arg1},
				"polygon":{"t": "IPolygon","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'GetSolidProfile2', 1, state)


	def modelPointToTriMesh(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"model":{"t": "IModel","v": arg0},
				"modelPoint":{"t": "IModelPoint","v": arg1},
				"useTexture":{"t": "B","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'modelPointToTriMesh', 0, state)


	def multiTriMeshToMultiPoint(self,arg0,arg1):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0},
				"tol":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'MultiTriMeshToMultiPoint', 1, state)


	def polygonToModelPoint(self,arg0):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'PolygonToModelPoint', 1, state)


	def polygonToTriMesh(self,arg0):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'PolygonToTriMesh', 1, state)


	def projectModelPointToPolygon(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"modelPoint":{"t": "IModelPoint","v": arg0},
				"model":{"t": "IModel","v": arg1},
				"tol":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'ProjectModelPointToPolygon', 1, state)


	def projectModelPointToXYPlane(self,arg0,arg1):  # 先定义函数 
		args = {
				"modelPoint":{"t": "IModelPoint","v": arg0},
				"model":{"t": "IModel","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'ProjectModelPointToXYPlane', 1, state)


	def projectTriMeshToPolygon(self,arg0,arg1):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0},
				"tol":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'projectTriMeshToPolygon', 0, state)


	def projectTrimeshToXYPlane(self,arg0):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'ProjectTrimeshToXYPlane', 1, state)


	def simplifyModel(self,arg0):  # 先定义函数 
		args = {
				"tol":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SimplifyModel', 1, state)


	def simplifyModel2(self,arg0):  # 先定义函数 
		args = {
				"tol":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SimplifyModel2', 1, state)


	def splitModelPointByPolygon2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SplitModelPointByPolygon2D', 1, state)


	def splitModelPointByPolygon2DWithZ(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2},
				"minZ":{"t": "N","v": arg3},
				"maxZ":{"t": "N","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'SplitModelPointByPolygon2DWithZ', 1, state)


	def triMeshToModelPoint(self,arg0):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'TriMeshToModelPoint', 1, state)

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
				super(IGeometryConvertor, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
