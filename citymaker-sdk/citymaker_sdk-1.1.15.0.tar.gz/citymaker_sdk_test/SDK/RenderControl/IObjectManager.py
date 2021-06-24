#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IObjectManager","F":"g"}}
class IObjectManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def setSkybox(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"viewIndex":{"t": "N","v": arg0},
				"skyBoxDirPath":{"t": "S","v": arg1},
				"skyBoxImageNumber":{"t": "N","v": arg2}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setSkybox', 0, state)


	def addImage(self,arg0,arg1):  # 先定义函数 
		args = {
				"imageName":{"t": "S","v": arg0},
				"newVal":{"t": "IImage","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'addImage', 0, state)


	def addModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"modelName":{"t": "S","v": arg0},
				"newVal":{"t": "IModel","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'addModel', 0, state)


	def create3DTileLayer(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"layerInfo":{"t": "S","v": arg0},
				"pass":{"t": "S","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'create3DTileLayer', 1, state)


	def createArc(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radiusX":{"t": "N","v": arg1},
				"radiusY":{"t": "N","v": arg2},
				"startAngle":{"t": "N","v": arg3},
				"endAngle":{"t": "N","v": arg4},
				"lineColor":{"t": "S","v": arg5},
				"fillColor":{"t": "S","v": arg6},
				"numOfSegments":{"t": "N","v": arg7},
				"groupID":{"t": "G","v": arg8}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createArc', 1, state)


	def createArrow(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"length":{"t": "N","v": arg1},
				"style":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"groupID":{"t": "G","v": arg5}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createArrow', 1, state)


	def createAttackArrow(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createAttackArrow', 1, state)


	def createCircle(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radius":{"t": "N","v": arg1},
				"lineColor":{"t": "S","v": arg2},
				"fillColor":{"t": "S","v": arg3},
				"groupId":{"t": "G","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCircle', 1, state)


	def createComplexParticleEffect(self,arg0,arg1):  # 先定义函数 
		args={}
		state=""
		if type(arg0) is dict and (type(arg1) in [int,float] or type(arg1) is str):
			args={
				"position":{"t": "IVector3","v": arg0},
				"type":{"t": "gviComplexParticleEffectType","v": arg1}
			}
			state="new"
		elif (type(arg0) in [int,float] or type(arg0) is str) and type(arg1) is str:
			args={
			
				"type":{"t": "gviComplexParticleEffectType","v": arg0},
				"groupID":{"t": "G","v": arg1}
				}
		return CM.AddPrototype(self,args, 'createComplexParticleEffect', 1, state)


	def createDoubleArrow(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createDoubleArrow', 1, state)


	def createEllipse(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radiusX":{"t": "N","v": arg1},
				"radiusY":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"numOfSegments":{"t": "N","v": arg5},
				"groupID":{"t": "G","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createEllipse', 1, state)


	def createFeatureLayer(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"geoField":{"t": "S","v": arg1},
				"textRender":{"t": "ITextRender","v": arg2},
				"geoRender":{"t": "IGeometryRender","v": arg3},
				"groupId":{"t": "G","v": arg4}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFeatureLayer', 1, state)


	def createGatheringPlace(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createGatheringPlace', 1, state)


	def createGeometryRenderFromXML(self,arg0):  # 先定义函数 
		args = {
				"xsv":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createGeometryRenderFromXML', 1, state)


	def createGeometrySymbolFromXML(self,arg0):  # 先定义函数 
		args = {
				"xsv":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createGeometrySymbolFromXML', 1, state)


	def createHeatMap(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"featureClass":{"t": "IFeatureClass","v": arg0},
				"geoFieldName":{"t": "S","v": arg1},
				"heatValueFieldName":{"t": "S","v": arg2},
				"groupID":{"t": "G","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createHeatMap', 1, state)


	def createImageLabel(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args={}
		state=""
		if type(arg0) is dict and (type(arg1) in [int,float] or type(arg1) is str) and type(arg2) is dict and type(arg3) is str:
			args={
				"position":{"t": "IPosition","v": arg0},
				"imageFileName":{"t": "S","v": arg1},
				"style":{"t": "ILabelStyle","v": arg2},
				"groupID":{"t": "G","v": arg3}
			}
		elif type(arg0) is dict and (type(arg1) in [int,float] or type(arg1) is str):
			args={
				"position":{"t": "IVector3","v": arg0},
				"imageFile":{"t": "S","v": arg1}
			}
			state="new"
			return CM.AddPrototype(self,args, 'createImageLabel', 1, state)


	def createImageryLayer(self,arg0,arg1):  # 先定义函数 
		args = {
				"connectionString":{"t": "S","v": arg0},
				"groupId":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createImageryLayer', 1, state)


	def createKmlGroup(self,arg0):  # 先定义函数 
		args = {
				"file":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createKmlGroup', 1, state)


	def createLabel(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args={}
		state=""
		if type(arg0) is dict and (type(arg1) in [int,float] or type(arg1) is str) and (type(arg2) in [int,float] or type(arg2) is str) and type(arg3) in [int,float] and (type(arg4) in [int,float] or type(arg4) is str) and (type(arg5)  is bool or arg5 == 1 or arg5 == 0) and type(arg6) in [int,float]:
			args={
				"position":{"t": "IVector3","v": arg0},
				"text":{"t": "S","v": arg1},
				"textColor":{"t": "S","v": arg2},
				"textSize":{"t": "N","v": arg3},
				"font":{"t": "S","v": arg4},
				"bUnderline":{"t": "B","v": arg5},
				"maxVisibleDistance":{"t": "N","v": arg6}
			}
			state="new"
		elif type(arg0) is str:
			args={
			
				"groupId":{"t": "G","v": arg0}
				}
		return CM.AddPrototype(self,args, 'createLabel', 1, state)


	def createMotionPath(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createMotionPath', 1, state)


	def createOverlayLabel(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createOverlayLabel', 1, state)


	def createOverlayUILabel(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args={}
		state=""
		if (type(arg0) in [int,float] or type(arg0) is str) and (type(arg1) in [int,float] or type(arg1) is str) and type(arg2) is dict and type(arg3) in [int,float] and type(arg4) in [int,float]:
			args={
				"width":{"t": "S","v": arg0},
				"height":{"t": "S","v": arg1},
				"position":{"t": "IVector3","v": arg2},
				"maxVisibleDistance":{"t": "N","v": arg3},
				"minVisibleDistance":{"t": "N","v": arg4}
			}
			state="new"
		elif type(arg0) is str:
			args={
			
				"groupID":{"t": "G","v": arg0}
				}
		return CM.AddPrototype(self,args, 'CreateOverlayUILabel', 1, state)


	def createParticleEffect(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createParticleEffect', 1, state)


	def createParticleEffectFromFDB(self,arg0,arg1):  # 先定义函数 
		args = {
				"featureDataSet":{"t": "IFeatureDataSet","v": arg0},
				"groupId":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createParticleEffectFromFDB', 1, state)


	def createRectangle(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"objectWidth":{"t": "N","v": arg1},
				"objectDepth":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"groupID":{"t": "G","v": arg5}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRectangle', 1, state)


	def createRegularPolygon(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radius":{"t": "N","v": arg1},
				"numOfSegments":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"groupId":{"t": "G","v": arg5}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRegularPolygon', 1, state)


	def createRenderArrow(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderArrow', 1, state)


	def createRenderModelPoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"modelPoint":{"t": "IModelPoint","v": arg0},
				"symbol":{"t": "IModelPointSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderModelPoint', 1, state)


	def createRenderMultiPoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPoint":{"t": "IMultiPoint","v": arg0},
				"symbol":{"t": "IPointSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderMultiPoint', 1, state)


	def createRenderMultiPolygon(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPolygon":{"t": "IMultiPolygon","v": arg0},
				"symbol":{"t": "ISurfaceSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderMultiPolygon', 1, state)


	def createRenderMultiPolyline(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiPolyline":{"t": "IMultiPolyline","v": arg0},
				"symbol":{"t": "ICurveSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderMultiPolyline', 1, state)


	def createRenderMultiTriMesh(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"multiTriMesh":{"t": "IMultiTriMesh","v": arg0},
				"symbol":{"t": "ISurfaceSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderMultiTriMesh', 1, state)


	def createRenderPipeLine(self,arg0,arg1):  # 先定义函数 
		args = {
				"polyline":{"t": "IPolyline","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderPipeLine', 1, state)


	def createRenderPOI(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args={}
		state=""
		if type(arg0) is dict and (type(arg1) in [int,float] or type(arg1) is str) and type(arg2) in [int,float] and (type(arg3) in [int,float] or type(arg3) is str):
			args={
				"position":{"t": "IVector3","v": arg0},
				"imagePath":{"t": "S","v": arg1},
				"size":{"t": "N","v": arg2},
				"name":{"t": "S","v": arg3}
			}
			state="new"
		elif type(arg0) is dict:
			args={
			
				"pOI":{"t": "IPOI","v": arg0}
				}
		return CM.AddPrototype(self,args, 'createRenderPOI', 1, state)


	def createRenderPOIFromFDB(self,arg0,arg1):  # 先定义函数 
		args = {
				"pOI":{"t": "IPOI","v": arg0},
				"featureDataSet":{"t": "IFeatureDataSet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderPOIFromFDB', 1, state)


	def createRenderPoint(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"point":{"t": "IPoint","v": arg0},
				"symbol":{"t": "IPointSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderPoint', 1, state)


	def createRenderPolygon(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"symbol":{"t": "ISurfaceSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderPolygon', 1, state)


	def createRenderPolyline(self,arg0,arg1,arg2):  # 先定义函数 
		args={}
		state=""
		if type(arg0) is dict and (type(arg1) in [int,float] or type(arg1) is str) and type(arg2) in [int,float]:
			args={
				"points":{"t": "<IVector3>","v": arg0},
				"color":{"t": "S","v": arg1},
				"width":{"t": "N","v": arg2}
			}
			state="new"
		elif type(arg0) is dict and type(arg1) is dict and type(arg2) is str:
			args={
			
				"polyline":{"t": "IPolyline","v": arg0},
				"symbol":{"t": "ICurveSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
				}
		return CM.AddPrototype(self,args, 'createRenderPolyline', 1, state)


	def createRenderTriMesh(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"triMesh":{"t": "ITriMesh","v": arg0},
				"symbol":{"t": "ISurfaceSymbol","v": arg1},
				"groupId":{"t": "G","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createRenderTriMesh', 1, state)


	def createSkinnedMesh(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args={}
		state=""
		if (type(arg0) in [int,float] or type(arg0) is str) and type(arg1) is dict and type(arg2) in [int,float] and type(arg3) in [int,float]:
			args={
				"modeName":{"t": "S","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"maxVisibleDistance":{"t": "N","v": arg2},
				"viewingDistance":{"t": "N","v": arg3}
			}
			state="new"
		elif type(arg0) is dict and type(arg1) is str:
			args={
			
				"modelPoint":{"t": "IModelPoint","v": arg0},
				"groupId":{"t": "G","v": arg1}
				}
		return CM.AddPrototype(self,args, 'createSkinnedMesh', 1, state)


	def createSquadCombat(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createSquadCombat', 1, state)


	def createTableLabel(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7):  # 先定义函数 
		args={}
		state=""
		if type(arg0) is dict and type(arg1) in [int,float] and type(arg2) in [int,float] and (type(arg3) in [int,float] or type(arg3) is str) and (type(arg4) in [int,float] or type(arg4) is str) and (type(arg5) in [int,float] or type(arg5) is str) and (type(arg6) in [int,float] or type(arg6) is str) and (type(arg7) in [int,float] or type(arg7) is str):
			args={
				"position":{"t": "IVector3","v": arg0},
				"rowCount":{"t": "N","v": arg1},
				"colCount":{"t": "N","v": arg2},
				"bgImgName":{"t": "S","v": arg3},
				"titleText":{"t": "S","v": arg4},
				"bgColor":{"t": "S","v": arg5},
				"borderColor":{"t": "S","v": arg6},
				"titleBgColor":{"t": "S","v": arg7}
			}
			state="new"
		elif type(arg0) in [int,float] and type(arg1) in [int,float] and type(arg2) is str:
			args={
			
				"rowCount":{"t": "N","v": arg0},
				"columnCount":{"t": "N","v": arg1},
				"groupId":{"t": "G","v": arg2}
				}
		return CM.AddPrototype(self,args, 'createTableLabel', 1, state)


	def createTailedAttackArrow(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTailedAttackArrow', 1, state)


	def createTailedSquadCombat(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTailedSquadCombat', 1, state)


	def createTerrainHole(self,arg0,arg1):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"groupId":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTerrainHole', 1, state)


	def createTerrainModifier(self,arg0,arg1):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"groupId":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTerrainModifier', 1, state)


	def createTerrainVideo(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"groupId":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTerrainVideo', 1, state)


	def createTextRenderFromXML(self,arg0):  # 先定义函数 
		args = {
				"xsv":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTextRenderFromXML', 1, state)


	def createTextSymbolFromXML(self,arg0):  # 先定义函数 
		args = {
				"xsv":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTextSymbolFromXML', 1, state)


	def createTripleArrow(self,arg0,arg1):  # 先定义函数 
		args = {
				"symbol":{"t": "ISurfaceSymbol","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTripleArrow', 1, state)


	def createViewshed(self,arg0,arg1):  # 先定义函数 
		args = {
				"position":{"t": "IPoint","v": arg0},
				"groupId":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createViewshed', 1, state)


	def createVolumeMeasureOperation(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createVolumeMeasureOperation', 1, state)


	def createWalkGround(self,arg0):  # 先定义函数 
		args = {
				"modelPoint":{"t": "IModelPoint","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createWalkGround', 1, state)


	def createWalkGroundFromFDB(self,arg0,arg1):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"geoField":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createWalkGroundFromFDB', 1, state)


	def delayDelete(self,arg0,arg1):  # 先定义函数 
		args = {
				"id":{"t": "G","v": arg0},
				"delayTime":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'delayDelete', 1, state)


	def deleteImage(self,arg0):  # 先定义函数 
		args = {
				"imageName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteImage', 0, state)


	def deleteModel(self,arg0):  # 先定义函数 
		args = {
				"modelName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteModel', 0, state)


	def getFeatureLayer(self,arg0):  # 先定义函数 
		args = {
				"featureLayerGuid":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFeatureLayer', 1, state)


	def getObjectById(self,arg0):  # 先定义函数 
		args = {
				"id":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getObjectById', 1, state)


	def getProjectTree(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getProjectTree', 1, state)


	def getReferencePlane(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getReferencePlane', 1, state)


	def getSkyBox(self,arg0):  # 先定义函数 
		args = {
				"viewIndex":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSkyBox', 1, state)


	def openRasterSourceDialog(self,arg0):  # 先定义函数 
		args = {
				"dataSourceType":{"t": "gviRasterSourceType","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'openRasterSourceDialog', 1, state)


	def createClipPlaneOperation(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createClipPlaneOperation', 1, state)


	def createLocation(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"groupID":{"t": "G","v": arg1},
				"altitudeType":{"t": "gviAltitudeType","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createLocation', 1, state)


	def createCameraTour(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCameraTour', 1, state)


	def createRenderImagePoint(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"imagePath":{"t": "S","v": arg1},
				"imageSize":{"t": "N","v": arg2},
				"toolTipText":{"t": "S","v": arg3}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'CreateRenderImagePoint', 1, state)


	def renderModelPointGlow(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"featureClassId":{"t": "G","v": arg0},
				"featureId":{"t": "N","v": arg1},
				"duration":{"t": "N","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'RenderModelPointGlow', 1, state)


	def createRenderSimplePoint(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"position":{"t": "IVector3","v": arg0},
				"fillColor":{"t": "S","v": arg1},
				"size":{"t": "N","v": arg2},
				"toolTipText":{"t": "S","v": arg3}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'CreateRenderSimplePoint', 1, state)


	def createTerrainRoute(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createTerrainRoute', 1, state)


	def deleteObject(self,arg0):  # 先定义函数 
		args = {
				"id":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'deleteObject', 1, state)


	def createBox(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"objectWidth":{"t": "N","v": arg1},
				"objectDepth":{"t": "N","v": arg2},
				"objectHeight":{"t": "N","v": arg3},
				"lineColor":{"t": "S","v": arg4},
				"fillColor":{"t": "S","v": arg5},
				"groupID":{"t": "G","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createBox', 1, state)


	def createCylinder(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radius":{"t": "N","v": arg1},
				"objectHeight":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"numOfSegments":{"t": "N","v": arg5},
				"groupId":{"t": "G","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCylinder', 1, state)


	def createPyramid(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"objectWidth":{"t": "N","v": arg1},
				"objectDepth":{"t": "N","v": arg2},
				"objectHeight":{"t": "N","v": arg3},
				"lineColor":{"t": "S","v": arg4},
				"fillColor":{"t": "S","v": arg5},
				"groupID":{"t": "G","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createPyramid', 1, state)


	def createSphere(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radius":{"t": "N","v": arg1},
				"style":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"segmentDensity":{"t": "N","v": arg5},
				"groupID":{"t": "G","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'createSphere', 0, state)


	def createCone(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"radius":{"t": "N","v": arg1},
				"objectHeight":{"t": "N","v": arg2},
				"lineColor":{"t": "S","v": arg3},
				"fillColor":{"t": "S","v": arg4},
				"numOfSegments":{"t": "N","v": arg5},
				"groupId":{"t": "G","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCone', 1, state)


	def create3DArrow(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"position":{"t": "IPosition","v": arg0},
				"length":{"t": "N","v": arg1},
				"style":{"t": "N","v": arg2},
				"objectHeight":{"t": "N","v": arg3},
				"lineColor":{"t": "S","v": arg4},
				"fillColor":{"t": "S","v": arg5},
				"groupID":{"t": "G","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'create3DArrow', 1, state)


	def createRenderModelPointFromFile(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fileName":{"t": "S","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"color":{"t": "S","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'CreateRenderModelPointFromFile', 1, state)


	def createRenderModelPointFromFDB(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"modelName":{"t": "S","v": arg0},
				"position":{"t": "IVector3","v": arg1},
				"envelope":{"t": "O","v": arg2},
				"color":{"t": "S","v": arg3}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'CreateRenderModelPointFromFDB', 1, state)


	def createPresentation(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createPresentation', 1, state)


	def createDynamicObject(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createDynamicObject', 1, state)


	def createDynamicObjectFromFile(self,arg0):  # 先定义函数 
		args = {
				"xmlPath":{"t": "S","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'CreateDynamicObjectFromFile', 1, state)

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
				super(IObjectManager, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
