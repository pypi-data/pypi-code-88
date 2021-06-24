#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.RenderControl.IRenderControlEvents import IRenderControlEvents
Props={"cacheManager":{"t":"ICacheManager","v":None,
"F":"g"},"camera":{"t":"ICamera","v":None,
"F":"g"},"clipMode":{"t":"gviClipMode","v":0,
"F":"gs"},"coordSysDialog":{"t":"ICoordSysDialog","v":None,
"H": True,"F":"g"},"crsFactory":{"t":"ICRSFactory","v":None,
"H": True,"F":"g"},"DataSourceFactory":{"t":"IDataSourceFactory","v":None,
"H": True,"F":"g"},"exportManager":{"t":"IExportManager","v":None,
"F":"g"},"featureManager":{"t":"IFeatureManager","v":None,
"F":"g"},"fullScreen":{"t":"bool","v":False,
"F":"gs"},"geometryConvertor":{"t":"IGeometryConvertor","v":None,
"H": True,"F":"g"},"geometryFactory":{"t":"IGeometryFactory","v":None,
"H": True,"F":"g"},"geoTransformer":{"t":"IGeoTransformer","v":None,
"H": True,"F":"g"},"heatMapPlayer":{"t":"IHeatMapPlayer","v":None,
"F":"g"},"highlightHelper":{"t":"IHighlightHelper","v":None,
"F":"g"},"interactMode":{"t":"gviInteractMode","v":1,
"F":"gs"},"isFocus":{"t":"bool","v":False,
"F":"g"},"measurementMode":{"t":"gviMeasurementMode","v":0,
"F":"gs"},"mouseSelectMode":{"t":"gviMouseSelectMode","v":1,
"F":"gs"},"mouseSelectObjectMask":{"t":"gviMouseSelectObjectMask","v":0,
"F":"gs"},"mouseSnapMode":{"t":"gviMouseSnapMode","v":0,
"F":"gs"},"msgChainFlags":{"t":"gviMsgChainFlags","v":1,
"F":"gs"},"new_Attachment":{"t":"IAttachment","v":None,
"F":"g"},"new_BinaryBuffer":{"t":"IBinaryBuffer","v":None,
"F":"g"},"new_ComparedRenderRule":{"t":"IComparedRenderRule","v":None,
"F":"g"},"new_ConnectionInfo":{"t":"IConnectionInfo","v":None,
"F":"g"},"new_CurveSymbol":{"t":"ICurveSymbol","v":None,
"F":"g"},"new_DbIndexInfo":{"t":"IDbIndexInfo","v":None,
"F":"g"},"new_DrawGroup":{"t":"IDrawGroup","v":None,
"F":"g"},"new_DrawMaterial":{"t":"IDrawMaterial","v":None,
"F":"g"},"new_DrawPrimitive":{"t":"IDrawPrimitive","v":None,
"F":"g"},"new_EdgeBarrier":{"t":"IEdgeBarrier","v":None,
"F":"g"},"new_EdgeNetworkSource":{"t":"IEdgeNetworkSource","v":None,
"F":"g"},"new_Envelope":{"t":"IEnvelope","v":None,
"F":"g"},"new_EulerAngle":{"t":"IEulerAngle","v":None,
"F":"g"},"new_FieldInfo":{"t":"IFieldInfo","v":None,
"F":"g"},"new_FieldInfoCollection":{"t":"IFieldInfoCollection","v":None,
"F":"g"},"new_FillStyle":{"t":"IFillStyle","v":None,
"F":"g"},"new_FloatArray":{"t":"IFloatArray","v":None,
"F":"g"},"new_GeometryDef":{"t":"IGeometryDef","v":None,
"F":"g"},"new_GeometryRenderScheme":{"t":"IGeometryRenderScheme","v":None,
"F":"g"},"new_GridIndexInfo":{"t":"IGridIndexInfo","v":None,
"F":"g"},"new_ImagePointSymbol":{"t":"ImagePointSymbol","v":None,
"F":"g"},"new_JunctionBarrier":{"t":"IJunctionBarrier","v":None,
"F":"g"},"new_JunctionNetworkSource":{"t":"IJunctionNetworkSource","v":None,
"F":"g"},"new_LabelStyle":{"t":"ILabelStyle","v":None,
"F":"g"},"new_LicenseServer":{"t":"ILicenseServer","v":None,
"F":"g"},"new_LineStyle":{"t":"ILineStyle","v":None,
"F":"g"},"new_Matrix":{"t":"IMatrix","v":None,
"F":"g"},"new_ModelPointSymbol":{"t":"IModelPointSymbol","v":None,
"F":"g"},"new_NetworkAttribute":{"t":"INetworkAttribute","v":None,
"F":"g"},"new_NetworkConstantEvaluator":{"t":"INetworkConstantEvaluator","v":None,
"F":"g"},"new_NetworkEventLocation":{"t":"INetworkEventLocation","v":None,
"F":"g"},"new_NetworkFieldEvaluator":{"t":"INetworkFieldEvaluator","v":None,
"F":"g"},"new_NetworkLocation":{"t":"INetworkLocation","v":None,
"F":"g"},"new_ObjectTexture":{"t":"IObjectTexture","v":None,
"F":"g"},"new_PointCloudSymbol":{"t":"IPointCloudSymbol","v":None,
"F":"g"},"new_Polygon3DSymbol":{"t":"IPolygon3DSymbol","v":None,
"F":"g"},"new_Position":{"t":"IPosition","v":None,
"F":"g"},"new_PropertySet":{"t":"IPropertySet","v":None,
"F":"g"},"new_QueryFilter":{"t":"IQueryFilter","v":None,
"F":"g"},"new_RangeRenderRule":{"t":"IRangeRenderRule","v":None,
"F":"g"},"new_RasterSymbol":{"t":"IRasterSymbol","v":None,
"F":"g"},"new_RenderIndexInfo":{"t":"IRenderIndexInfo","v":None,
"F":"g"},"new_RowBufferCollection":{"t":"IRowBufferCollection","v":None,
"F":"g"},"new_SimpleGeometryRender":{"t":"ISimpleGeometryRender","v":None,
"F":"g"},"new_SimplePointSymbol":{"t":"ISimplePointSymbol","v":None,
"F":"g"},"new_SimpleTextRender":{"t":"ISimpleTextRender","v":None,
"F":"g"},"new_SolidSymbol":{"t":"ISolidSymbol","v":None,
"F":"g"},"new_SpatialFilter":{"t":"ISpatialFilter","v":None,
"F":"g"},"new_SurfaceSymbol":{"t":"ISurfaceSymbol","v":None,
"F":"g"},"new_TemporalFilter":{"t":"ITemporalFilter","v":None,
"F":"g"},"new_TextAttribute":{"t":"ITextAttribute","v":None,
"F":"g"},"new_TextRenderScheme":{"t":"ITextRenderScheme","v":None,
"F":"g"},"new_TextSymbol":{"t":"ITextSymbol","v":None,
"F":"g"},"new_ToolTipTextRender":{"t":"IToolTipTextRender","v":None,
"F":"g"},"new_UIDim":{"t":"IUIDim","v":None,
"F":"g"},"new_UIRect":{"t":"IUIRect","v":None,
"F":"g"},"new_UniqueValuesRenderRule":{"t":"IUniqueValuesRenderRule","v":None,
"F":"g"},"new_ValueMapGeometryRender":{"t":"IValueMapGeometryRender","v":None,
"F":"g"},"new_ValueMapTextRender":{"t":"IValueMapTextRender","v":None,
"F":"g"},"new_Vector3":{"t":"IVector3","v":None,
"F":"g"},"objectEditor":{"t":"IObjectEditor","v":None,
"F":"g"},"objectManager":{"t":"IObjectManager","v":None,
"F":"g"},"parametricModelling":{"t":"IParametricModelling","v":None,
"H": True,"F":"g"},"polynomialTransformer":{"t":"IPolynomialTransformer","v":None,
"H": True,"F":"g"},"project":{"t":"IProject","v":None,
"F":"g"},"projectTree":{"t":"IProjectTree","v":None,
"F":"g"},"resourceFactory":{"t":"IResourceFactory","v":None,
"H": True,"F":"g"},"rowBufferFactory":{"t":"IRowBufferFactory","v":None,
"H": True,"F":"g"},"sunConfig":{"t":"ISunConfig","v":None,
"F":"g"},"terrain":{"t":"ITerrain","v":None,
"F":"g"},"terrainAnalyse":{"t":"ITerrainAnalyse","v":None,
"H": True,"F":"g"},"terrainVideoConfig":{"t":"ITerrainVideoConfig","v":None,
"F":"g"},"transformHelper":{"t":"ITransformHelper","v":None,
"F":"g"},"uiWindowManager":{"t":"IUIWindowManager","v":None,
"F":"g"},"useEarthOrbitManipulator":{"t":"gviManipulatorMode","v":0,
"F":"gs"},"useInProcHTMLWindow":{"t":"bool","v":False,
"F":"gs"},"utility":{"t":"IUtility","v":None,
"F":"g"},"viewport":{"t":"IViewport","v":None,
"F":"g"},"visible":{"t":"bool","v":False,
"F":"gs"},"visualAnalysis":{"t":"IVisualAnalysis","v":None,
"F":"g"},"guid":{"t":"S","v":"11111111-1111-1111-1111-111111111111","F":"g"},
"_HashCode":{"t":"S","v":"11111111-1111-1111-1111-111111111111","F":"g"},
"propertyType":{"t":"S","v":"IRenderControl","F":"g"}}
#Events = {mouseCursor:{fn:null}}
class IRenderControl(IRenderControlEvents):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.cacheManager=args.get("cacheManager")
		self.camera=args.get("camera")
		self.clipMode=args.get("clipMode")
		self.coordSysDialog=args.get("coordSysDialog")
		self.crsFactory=args.get("crsFactory")
		self.DataSourceFactory=args.get("DataSourceFactory")
		self.exportManager=args.get("exportManager")
		self.featureManager=args.get("featureManager")
		self.fullScreen=args.get("fullScreen")
		self.geometryConvertor=args.get("geometryConvertor")
		self.geometryFactory=args.get("geometryFactory")
		self.geoTransformer=args.get("geoTransformer")
		self.heatMapPlayer=args.get("heatMapPlayer")
		self.highlightHelper=args.get("highlightHelper")
		self.interactMode=args.get("interactMode")
		self.isFocus=args.get("isFocus")
		self.measurementMode=args.get("measurementMode")
		self.mouseSelectMode=args.get("mouseSelectMode")
		self.mouseSelectObjectMask=args.get("mouseSelectObjectMask")
		self.mouseSnapMode=args.get("mouseSnapMode")
		self.msgChainFlags=args.get("msgChainFlags")
		self.new_Attachment=args.get("new_Attachment")
		self.new_BinaryBuffer=args.get("new_BinaryBuffer")
		self.new_ComparedRenderRule=args.get("new_ComparedRenderRule")
		self.new_ConnectionInfo=args.get("new_ConnectionInfo")
		self.new_CurveSymbol=args.get("new_CurveSymbol")
		self.new_DbIndexInfo=args.get("new_DbIndexInfo")
		self.new_DrawGroup=args.get("new_DrawGroup")
		self.new_DrawMaterial=args.get("new_DrawMaterial")
		self.new_DrawPrimitive=args.get("new_DrawPrimitive")
		self.new_EdgeBarrier=args.get("new_EdgeBarrier")
		self.new_EdgeNetworkSource=args.get("new_EdgeNetworkSource")
		self.new_Envelope=args.get("new_Envelope")
		self.new_EulerAngle=args.get("new_EulerAngle")
		self.new_FieldInfo=args.get("new_FieldInfo")
		self.new_FieldInfoCollection=args.get("new_FieldInfoCollection")
		self.new_FillStyle=args.get("new_FillStyle")
		self.new_FloatArray=args.get("new_FloatArray")
		self.new_GeometryDef=args.get("new_GeometryDef")
		self.new_GeometryRenderScheme=args.get("new_GeometryRenderScheme")
		self.new_GridIndexInfo=args.get("new_GridIndexInfo")
		self.new_ImagePointSymbol=args.get("new_ImagePointSymbol")
		self.new_JunctionBarrier=args.get("new_JunctionBarrier")
		self.new_JunctionNetworkSource=args.get("new_JunctionNetworkSource")
		self.new_LabelStyle=args.get("new_LabelStyle")
		self.new_LicenseServer=args.get("new_LicenseServer")
		self.new_LineStyle=args.get("new_LineStyle")
		self.new_Matrix=args.get("new_Matrix")
		self.new_ModelPointSymbol=args.get("new_ModelPointSymbol")
		self.new_NetworkAttribute=args.get("new_NetworkAttribute")
		self.new_NetworkConstantEvaluator=args.get("new_NetworkConstantEvaluator")
		self.new_NetworkEventLocation=args.get("new_NetworkEventLocation")
		self.new_NetworkFieldEvaluator=args.get("new_NetworkFieldEvaluator")
		self.new_NetworkLocation=args.get("new_NetworkLocation")
		self.new_ObjectTexture=args.get("new_ObjectTexture")
		self.new_PointCloudSymbol=args.get("new_PointCloudSymbol")
		self.new_Polygon3DSymbol=args.get("new_Polygon3DSymbol")
		self.new_Position=args.get("new_Position")
		self.new_PropertySet=args.get("new_PropertySet")
		self.new_QueryFilter=args.get("new_QueryFilter")
		self.new_RangeRenderRule=args.get("new_RangeRenderRule")
		self.new_RasterSymbol=args.get("new_RasterSymbol")
		self.new_RenderIndexInfo=args.get("new_RenderIndexInfo")
		self.new_RowBufferCollection=args.get("new_RowBufferCollection")
		self.new_SimpleGeometryRender=args.get("new_SimpleGeometryRender")
		self.new_SimplePointSymbol=args.get("new_SimplePointSymbol")
		self.new_SimpleTextRender=args.get("new_SimpleTextRender")
		self.new_SolidSymbol=args.get("new_SolidSymbol")
		self.new_SpatialFilter=args.get("new_SpatialFilter")
		self.new_SurfaceSymbol=args.get("new_SurfaceSymbol")
		self.new_TemporalFilter=args.get("new_TemporalFilter")
		self.new_TextAttribute=args.get("new_TextAttribute")
		self.new_TextRenderScheme=args.get("new_TextRenderScheme")
		self.new_TextSymbol=args.get("new_TextSymbol")
		self.new_ToolTipTextRender=args.get("new_ToolTipTextRender")
		self.new_UIDim=args.get("new_UIDim")
		self.new_UIRect=args.get("new_UIRect")
		self.new_UniqueValuesRenderRule=args.get("new_UniqueValuesRenderRule")
		self.new_ValueMapGeometryRender=args.get("new_ValueMapGeometryRender")
		self.new_ValueMapTextRender=args.get("new_ValueMapTextRender")
		self.new_Vector3=args.get("new_Vector3")
		self.objectEditor=args.get("objectEditor")
		self.objectManager=args.get("objectManager")
		self.parametricModelling=args.get("parametricModelling")
		self.polynomialTransformer=args.get("polynomialTransformer")
		self.project=args.get("project")
		self.projectTree=args.get("projectTree")
		self.resourceFactory=args.get("resourceFactory")
		self.rowBufferFactory=args.get("rowBufferFactory")
		self.sunConfig=args.get("sunConfig")
		self.terrain=args.get("terrain")
		self.terrainAnalyse=args.get("terrainAnalyse")
		self.terrainVideoConfig=args.get("terrainVideoConfig")
		self.transformHelper=args.get("transformHelper")
		self.uiWindowManager=args.get("uiWindowManager")
		self.useEarthOrbitManipulator=args.get("useEarthOrbitManipulator")
		self.useInProcHTMLWindow=args.get("useInProcHTMLWindow")
		self.utility=args.get("utility")
		self.viewport=args.get("viewport")
		self.visible=args.get("visible")
		self.visualAnalysis=args.get("visualAnalysis")
		self.guid=args.get("guid")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def setPlanarGlobe(self,arg0):  # 先定义函数 
		args = {
				"isPlanarTerrain":{"t": "B","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setPlanarGlobe', 0, state)


	def loadShpData(self,arg0):  # 先定义函数 
		args = {
				"shpPath":{"t": "S","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'LoadShpData', 1, state)


	def loadFDBByService(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"server":{"t": "S","v": arg0},
				"port":{"t": "N","v": arg1},
				"database":{"t": "S","v": arg2},
				"pwd":{"t": "S","v": arg3},
				"datasetName":{"t": "S","v": arg4}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'LoadFDBByService', 1, state)


	def loadFdb(self,arg0,arg1):  # 先定义函数 
		args = {
				"fdbPath":{"t": "S","v": arg0},
				"datasetName":{"t": "S","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'LoadFdb', 1, state)


	def getCurrentCrsWKT(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getCurrentCrsWKT', 1, state)


	def getLastError(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getLastError', 1, state)


	def getRenderParam(self,arg0):  # 先定义函数 
		args = {
				"param":{"t": "gviRenderControlParameters","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRenderParam', 1, state)


	def getTerrainCrsWKT(self,arg0,arg1):  # 先定义函数 
		args = {
				"layerInfo":{"t": "S","v": arg0},
				"password":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getTerrainCrsWKT', 1, state)


	def initialize(self,arg0,arg1):  # 先定义函数 
		args = {
				"isPlanarTerrain":{"t": "B","v": arg0},
				"params":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'initialize', 1, state)


	def initialize2(self,arg0,arg1):  # 先定义函数 
		args = {
				"crsWKT":{"t": "S","v": arg0},
				"params":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'initialize2', 1, state)


	def pauseRendering(self,arg0):  # 先定义函数 
		args = {
				"dumpMemory":{"t": "B","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'pauseRendering', 0, state)


	def reconnect(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'reconnect', 0, state)


	def refreshImage(self,arg0,arg1):  # 先定义函数 
		args = {
				"dataSet":{"t": "IFeatureDataSet","v": arg0},
				"imageName":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'refreshImage', 0, state)


	def refreshModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"dataSet":{"t": "IFeatureDataSet","v": arg0},
				"modelName":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'refreshModel', 0, state)


	def reset(self,arg0):  # 先定义函数 
		args = {
				"isPlanar":{"t": "B","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'reset', 0, state)


	def reset2(self,arg0):  # 先定义函数 
		args = {
				"crsWKT":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'reset2', 0, state)


	def resumeRendering(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'resumeRendering', 0, state)


	def setMenuData(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setMenuData', 1, state)


	def setMenuEnabled(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "B","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setMenuEnabled', 0, state)


	def setRenderParam(self,arg0,arg1):  # 先定义函数 
		args = {
				"param":{"t": "gviRenderControlParameters","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRenderParam', 0, state)


	def terminate(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'terminate', 0, state)


	def trackPopupMenu(self,arg0,arg1):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'trackPopupMenu', 1, state)

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
				super(IRenderControl, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
