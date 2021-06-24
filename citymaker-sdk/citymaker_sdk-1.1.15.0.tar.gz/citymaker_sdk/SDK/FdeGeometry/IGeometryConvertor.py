#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometryConvertor","F":"g"}}
class IGeometryConvertor:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def cutModelPointByPolygon2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'cutModelPointByPolygon2D', 1, state)


	def cutModelPointByPolygon2DWithZ(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2},
				"minZ":{"t": "N","v": arg3},
				"maxZ":{"t": "N","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'cutModelPointByPolygon2DWithZ', 1, state)


	def cutTriMeshToPolygon(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0},
				"heightSpec":{"t": "N","v": arg1},
				"tol":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'cutTriMeshToPolygon', 1, state)


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
		return CM.AddPrototype(self,args, 'extrudePolygonToModel', 1, state)


	def extrudePolygonToTriMesh(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"height":{"t": "N","v": arg1},
				"closed":{"t": "B","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'extrudePolygonToTriMesh', 1, state)


	def getSolidProfile(self,arg0,arg1):  # 先定义函数 
		args = {
				"closedTriMesh":{"t": "ITriMesh","v": arg0},
				"polygon":{"t": "IPolygon","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSolidProfile', 1, state)


	def getSolidProfile2(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"modelSrc":{"t": "IModel","v": arg0},
				"modelPointSrc":{"t": "IModelPoint","v": arg1},
				"polygon":{"t": "IPolygon","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSolidProfile2', 1, state)


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
		return CM.AddPrototype(self,args, 'multiTriMeshToMultiPoint', 1, state)


	def polygonToModelPoint(self,arg0):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'polygonToModelPoint', 1, state)


	def polygonToTriMesh(self,arg0):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'polygonToTriMesh', 1, state)


	def projectModelPointToPolygon(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"modelPoint":{"t": "IModelPoint","v": arg0},
				"model":{"t": "IModel","v": arg1},
				"tol":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'projectModelPointToPolygon', 1, state)


	def projectModelPointToXYPlane(self,arg0,arg1):  # 先定义函数 
		args = {
				"modelPoint":{"t": "IModelPoint","v": arg0},
				"model":{"t": "IModel","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'projectModelPointToXYPlane', 1, state)


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
		return CM.AddPrototype(self,args, 'projectTrimeshToXYPlane', 1, state)


	def simplifyModel(self,arg0):  # 先定义函数 
		args = {
				"tol":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'simplifyModel', 1, state)


	def simplifyModel2(self,arg0):  # 先定义函数 
		args = {
				"tol":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'simplifyModel2', 1, state)


	def splitModelPointByPolygon2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'splitModelPointByPolygon2D', 1, state)


	def splitModelPointByPolygon2DWithZ(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"modelSrc":{"t": "IModel","v": arg1},
				"modelPointSrc":{"t": "IModelPoint","v": arg2},
				"minZ":{"t": "N","v": arg3},
				"maxZ":{"t": "N","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'splitModelPointByPolygon2DWithZ', 1, state)


	def triMeshToModelPoint(self,arg0):  # 先定义函数 
		args = {
				"multiMesh":{"t": "IMultiTriMesh","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'triMeshToModelPoint', 1, state)

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
