#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.RenderControl.IRenderControlEvents import IRenderControlEvents
Props={"cacheManager":{"t":"ICacheManager","v":None,
"F":"g"},"camera":{"t":"ICamera","v":None,
"F":"g"},"clipMode":{"t":"gviClipMode","v":0,
"F":"gs"},"coordSysDialog":{"t":"ICoordSysDialog","v":None,
"H": True,"F":"g"},"crsFactory":{"t":"ICRSFactory","v":None,
"H": True,"F":"g"},"dataSourceFactory":{"t":"IDataSourceFactory","v":None,
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
"F":"g"},"new_ImagePointSymbol":{"t":"IImagePointSymbol","v":None,
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
"H": True,"F":"g"},"dataCopyParam":{"t":"IDataCopyParam","v":None,
"F":"g"},"layerInfoCollection":{"t":"ILayerInfoCollection","v":None,
"F":"g"},"rasterSourceFactory":{"t":"IRasterSourceFactory","v":None,
"F":"g"},"dataInteropFactory":{"t":"IDataInteropFactory","v":None,
"F":"g"},"commandManagerFactory":{"t":"ICommandManagerFactory","v":None,
"F":"g"},"undoRedoResultCollection":{"t":"IUndoRedoResultCollection","v":None,
"F":"g"},"rowBufferFactory":{"t":"IRowBufferFactory","v":None,
"H": True,"F":"g"},"sunConfig":{"t":"ISunConfig","v":None,
"F":"g"},"terrain":{"t":"ITerrain","v":None,
"F":"g"},"terrainAnalyse":{"t":"ITerrainAnalyse","v":None,
"H": True,"F":"g"},"terrainVideoConfig":{"t":"ITerrainVideoConfig","v":None,
"F":"g"},"transformHelper":{"t":"ITransformHelper","v":None,
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
		self._cacheManager=args.get("cacheManager")
		self._camera=args.get("camera")
		self._clipMode=args.get("clipMode")
		self._coordSysDialog=args.get("coordSysDialog")
		self._crsFactory=args.get("crsFactory")
		self._dataSourceFactory=args.get("dataSourceFactory")
		self._exportManager=args.get("exportManager")
		self._featureManager=args.get("featureManager")
		self._fullScreen=args.get("fullScreen")
		self._geometryConvertor=args.get("geometryConvertor")
		self._geometryFactory=args.get("geometryFactory")
		self._geoTransformer=args.get("geoTransformer")
		self._heatMapPlayer=args.get("heatMapPlayer")
		self._highlightHelper=args.get("highlightHelper")
		self._interactMode=args.get("interactMode")
		self._isFocus=args.get("isFocus")
		self._measurementMode=args.get("measurementMode")
		self._mouseSelectMode=args.get("mouseSelectMode")
		self._mouseSelectObjectMask=args.get("mouseSelectObjectMask")
		self._mouseSnapMode=args.get("mouseSnapMode")
		self._msgChainFlags=args.get("msgChainFlags")
		self._new_Attachment=args.get("new_Attachment")
		self._new_BinaryBuffer=args.get("new_BinaryBuffer")
		self._new_ComparedRenderRule=args.get("new_ComparedRenderRule")
		self._new_ConnectionInfo=args.get("new_ConnectionInfo")
		self._new_CurveSymbol=args.get("new_CurveSymbol")
		self._new_DbIndexInfo=args.get("new_DbIndexInfo")
		self._new_DrawGroup=args.get("new_DrawGroup")
		self._new_DrawMaterial=args.get("new_DrawMaterial")
		self._new_DrawPrimitive=args.get("new_DrawPrimitive")
		self._new_EdgeBarrier=args.get("new_EdgeBarrier")
		self._new_EdgeNetworkSource=args.get("new_EdgeNetworkSource")
		self._new_Envelope=args.get("new_Envelope")
		self._new_EulerAngle=args.get("new_EulerAngle")
		self._new_FieldInfo=args.get("new_FieldInfo")
		self._new_FieldInfoCollection=args.get("new_FieldInfoCollection")
		self._new_FillStyle=args.get("new_FillStyle")
		self._new_FloatArray=args.get("new_FloatArray")
		self._new_GeometryDef=args.get("new_GeometryDef")
		self._new_GeometryRenderScheme=args.get("new_GeometryRenderScheme")
		self._new_GridIndexInfo=args.get("new_GridIndexInfo")
		self._new_ImagePointSymbol=args.get("new_ImagePointSymbol")
		self._new_JunctionBarrier=args.get("new_JunctionBarrier")
		self._new_JunctionNetworkSource=args.get("new_JunctionNetworkSource")
		self._new_LabelStyle=args.get("new_LabelStyle")
		self._new_LicenseServer=args.get("new_LicenseServer")
		self._new_LineStyle=args.get("new_LineStyle")
		self._new_Matrix=args.get("new_Matrix")
		self._new_ModelPointSymbol=args.get("new_ModelPointSymbol")
		self._new_NetworkAttribute=args.get("new_NetworkAttribute")
		self._new_NetworkConstantEvaluator=args.get("new_NetworkConstantEvaluator")
		self._new_NetworkEventLocation=args.get("new_NetworkEventLocation")
		self._new_NetworkFieldEvaluator=args.get("new_NetworkFieldEvaluator")
		self._new_NetworkLocation=args.get("new_NetworkLocation")
		self._new_ObjectTexture=args.get("new_ObjectTexture")
		self._new_PointCloudSymbol=args.get("new_PointCloudSymbol")
		self._new_Polygon3DSymbol=args.get("new_Polygon3DSymbol")
		self._new_Position=args.get("new_Position")
		self._new_PropertySet=args.get("new_PropertySet")
		self._new_QueryFilter=args.get("new_QueryFilter")
		self._new_RangeRenderRule=args.get("new_RangeRenderRule")
		self._new_RasterSymbol=args.get("new_RasterSymbol")
		self._new_RenderIndexInfo=args.get("new_RenderIndexInfo")
		self._new_RowBufferCollection=args.get("new_RowBufferCollection")
		self._new_SimpleGeometryRender=args.get("new_SimpleGeometryRender")
		self._new_SimplePointSymbol=args.get("new_SimplePointSymbol")
		self._new_SimpleTextRender=args.get("new_SimpleTextRender")
		self._new_SolidSymbol=args.get("new_SolidSymbol")
		self._new_SpatialFilter=args.get("new_SpatialFilter")
		self._new_SurfaceSymbol=args.get("new_SurfaceSymbol")
		self._new_TemporalFilter=args.get("new_TemporalFilter")
		self._new_TextAttribute=args.get("new_TextAttribute")
		self._new_TextRenderScheme=args.get("new_TextRenderScheme")
		self._new_TextSymbol=args.get("new_TextSymbol")
		self._new_ToolTipTextRender=args.get("new_ToolTipTextRender")
		self._new_UIDim=args.get("new_UIDim")
		self._new_UIRect=args.get("new_UIRect")
		self._new_UniqueValuesRenderRule=args.get("new_UniqueValuesRenderRule")
		self._new_ValueMapGeometryRender=args.get("new_ValueMapGeometryRender")
		self._new_ValueMapTextRender=args.get("new_ValueMapTextRender")
		self._new_Vector3=args.get("new_Vector3")
		self._objectEditor=args.get("objectEditor")
		self._objectManager=args.get("objectManager")
		self._parametricModelling=args.get("parametricModelling")
		self._polynomialTransformer=args.get("polynomialTransformer")
		self._project=args.get("project")
		self._projectTree=args.get("projectTree")
		self._resourceFactory=args.get("resourceFactory")
		self._dataCopyParam=args.get("dataCopyParam")
		self._layerInfoCollection=args.get("layerInfoCollection")
		self._rasterSourceFactory=args.get("rasterSourceFactory")
		self._dataInteropFactory=args.get("dataInteropFactory")
		self._commandManagerFactory=args.get("commandManagerFactory")
		self._undoRedoResultCollection=args.get("undoRedoResultCollection")
		self._rowBufferFactory=args.get("rowBufferFactory")
		self._sunConfig=args.get("sunConfig")
		self._terrain=args.get("terrain")
		self._terrainAnalyse=args.get("terrainAnalyse")
		self._terrainVideoConfig=args.get("terrainVideoConfig")
		self._transformHelper=args.get("transformHelper")
		self._useEarthOrbitManipulator=args.get("useEarthOrbitManipulator")
		self._useInProcHTMLWindow=args.get("useInProcHTMLWindow")
		self._utility=args.get("utility")
		self._viewport=args.get("viewport")
		self._visible=args.get("visible")
		self._visualAnalysis=args.get("visualAnalysis")
		self._guid=args.get("guid")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def tileLayerSelectHelper(self,):  # 先定义函数 
		args = {}
		state = "new"
		CM.AddPrototype(self,args, 'tileLayerSelectHelper', 0, state)


	def tileLayerSelect(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args = {
				"tileLayer":{"t": "I3DTileLayer|TiledFeatureLayer","v": arg0},
				"intersectPoint":{"t": "IPoint","v": arg1},
				"connectionInfo":{"t": "IConnectionInfo","v": arg2},
				"c":{"t": "S","v": arg3},
				"mode":{"t": "N","v": arg4}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'tileLayerSelect', 1, state)


	def tileLayerHighlights(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"queryFilter":{"t": "S","v": arg1},
				"c":{"t": "S","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'tileLayerHighlights', 1, state)


	def getObject(self,arg0):  # 先定义函数 
		args = {
				"_HashCode":{"t": "G","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getObject', 1, state)


	def setTileLayerRenderParams(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"titleLayer":{"t": "I3DTileLayer","v": arg0},
				"type":{"t": "S","v": arg1},
				"value":{"t": "Number","v": arg2}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setTileLayerRenderParams', 0, state)


	def getTileLayerRenderParams(self,arg0,arg1):  # 先定义函数 
		args = {
				"titleLayer":{"t": "I3DTileLayer","v": arg0},
				"type":{"t": "S","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'getTileLayerRenderParams', 1, state)


	def setSelectFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"fL":{"t": "G","v": arg0},
				"selectFID":{"t": "Number","v": arg1}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setSelectFeature', 0, state)


	def setCurFeatureLayer(self,arg0):  # 先定义函数 
		args = {
				"guid":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setCurFeatureLayer', 0, state)


	def getCurGroupID(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'getCurGroupID', 1, state)


	def setCurGroupID(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "S","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setCurGroupID', 0, state)


	def importModelLibraryInfo(self,arg0):  # 先定义函数 
		args = {
				"xmlPath":{"t": "S","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'importModelLibraryInfo', 1, state)


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
		return CM.AddPrototype(self,args, 'loadShpData', 1, state)


	def loadFDBByService(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7):  # 先定义函数
		args = {
				"server":{"t": "S","v": arg0},
				"port":{"t": "Number","v": arg1},
				"database":{"t": "S","v": arg2},
				"pwd":{"t": "S","v": arg3},
				"datasetName":{"t": "S","v": arg4},
				"isFly":{"t": "b","v": arg5},
				"textRender":{"t": "ITextRender","v": arg6},
				"geoRender":{"t": "IGeometryRender","v": arg7}

		}
		state = "new"
		return CM.AddPrototype(self,args, 'loadFDBByService', 1, state)


	def loadFdb(self,arg0,arg1):  # 先定义函数 
		args = {
				"fdbPath":{"t": "S","v": arg0},
				"datasetName":{"t": "S","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'loadFdb', 1, state)


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

	@property
	def cacheManager(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"cacheManager",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"cacheManager",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "cacheManager", res)
		return PropsValueData["cacheManager"]

	@property
	def camera(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"camera",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"camera",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "camera", res)
		return PropsValueData["camera"]

	@property
	def clipMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["clipMode"]

	@clipMode.setter
	def clipMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "clipMode", val)
		args = {}
		args["clipMode"] = PropsTypeData.get("clipMode")
		args["clipMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"clipMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"clipMode",JsonData)

	@property
	def coordSysDialog(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"coordSysDialog",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"coordSysDialog",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "coordSysDialog", res)
		return PropsValueData["coordSysDialog"]

	@property
	def crsFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"crsFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"crsFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "crsFactory", res)
		return PropsValueData["crsFactory"]

	@property
	def dataSourceFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"dataSourceFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"dataSourceFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "dataSourceFactory", res)
		return PropsValueData["dataSourceFactory"]

	@property
	def exportManager(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"exportManager",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"exportManager",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "exportManager", res)
		return PropsValueData["exportManager"]

	@property
	def featureManager(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"featureManager",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"featureManager",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "featureManager", res)
		return PropsValueData["featureManager"]

	@property
	def fullScreen(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		#res=M.isFull()
		#CM.addPropsValue(PropsValueData.get("_HashCode"), "fullScreen", res)
		return PropsValueData["fullScreen"]

	@fullScreen.setter
	def fullScreen(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fullScreen", val)
		wsObj.screenChange()

	@property
	def geometryConvertor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"geometryConvertor",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometryConvertor",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "geometryConvertor", res)
		return PropsValueData["geometryConvertor"]

	@property
	def geometryFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"geometryFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometryFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "geometryFactory", res)
		return PropsValueData["geometryFactory"]

	@property
	def geoTransformer(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"geoTransformer",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geoTransformer",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "geoTransformer", res)
		return PropsValueData["geoTransformer"]

	@property
	def heatMapPlayer(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"heatMapPlayer",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"heatMapPlayer",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "heatMapPlayer", res)
		return PropsValueData["heatMapPlayer"]

	@property
	def highlightHelper(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"highlightHelper",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"highlightHelper",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "highlightHelper", res)
		return PropsValueData["highlightHelper"]

	@property
	def interactMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["interactMode"]

	@interactMode.setter
	def interactMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "interactMode", val)
		args = {}
		args["interactMode"] = PropsTypeData.get("interactMode")
		args["interactMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"interactMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"interactMode",JsonData)
		return JsonData

	def SetInteractMode(self,type,driver,val):
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "interactMode", val)
		args = {}
		args["interactMode"] = PropsTypeData.get("interactMode")
		args["interactMode"]["v"] = val
		JsonData = CM.setJsonData("set_", PropsValueData.get("_HashCode"), "interactMode", args)
		postData = "pyPostMessage('WEBSDK_API'," + str(JsonData) + ")"
		if type==1:
			driver.ExecuteJavascript(postData)
		if type == 2:
			driver.execute_script(postData)

	@property
	def isFocus(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isFocus"]

	@property
	def measurementMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["measurementMode"]

	@measurementMode.setter
	def measurementMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "measurementMode", val)
		args = {}
		args["measurementMode"] = PropsTypeData.get("measurementMode")
		args["measurementMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"measurementMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"measurementMode",JsonData)

	@property
	def mouseSelectMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["mouseSelectMode"]

	@mouseSelectMode.setter
	def mouseSelectMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "mouseSelectMode", val)
		args = {}
		args["mouseSelectMode"] = PropsTypeData.get("mouseSelectMode")
		args["mouseSelectMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"mouseSelectMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"mouseSelectMode",JsonData)

	@property
	def mouseSelectObjectMask(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["mouseSelectObjectMask"]

	@mouseSelectObjectMask.setter
	def mouseSelectObjectMask(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "mouseSelectObjectMask", val)
		args = {}
		args["mouseSelectObjectMask"] = PropsTypeData.get("mouseSelectObjectMask")
		args["mouseSelectObjectMask"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"mouseSelectObjectMask", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"mouseSelectObjectMask",JsonData)

	@property
	def mouseSnapMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["mouseSnapMode"]

	@mouseSnapMode.setter
	def mouseSnapMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "mouseSnapMode", val)
		args = {}
		args["mouseSnapMode"] = PropsTypeData.get("mouseSnapMode")
		args["mouseSnapMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"mouseSnapMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"mouseSnapMode",JsonData)

	@property
	def msgChainFlags(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["msgChainFlags"]

	@msgChainFlags.setter
	def msgChainFlags(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "msgChainFlags", val)
		args = {}
		args["msgChainFlags"] = PropsTypeData.get("msgChainFlags")
		args["msgChainFlags"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"msgChainFlags", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"msgChainFlags",JsonData)

	@property
	def new_Attachment(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_Attachment",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_Attachment",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_Attachment", res)
		return PropsValueData["new_Attachment"]

	@property
	def new_BinaryBuffer(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_BinaryBuffer",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_BinaryBuffer",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_BinaryBuffer", res)
		return PropsValueData["new_BinaryBuffer"]

	@property
	def new_ComparedRenderRule(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ComparedRenderRule",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ComparedRenderRule",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ComparedRenderRule", res)
		return PropsValueData["new_ComparedRenderRule"]

	@property
	def new_ConnectionInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ConnectionInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ConnectionInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ConnectionInfo", res)
		return PropsValueData["new_ConnectionInfo"]

	@property
	def new_CurveSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_CurveSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_CurveSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_CurveSymbol", res)
		return PropsValueData["new_CurveSymbol"]

	@property
	def new_DbIndexInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_DbIndexInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_DbIndexInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_DbIndexInfo", res)
		return PropsValueData["new_DbIndexInfo"]

	@property
	def new_DrawGroup(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_DrawGroup",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_DrawGroup",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_DrawGroup", res)
		return PropsValueData["new_DrawGroup"]

	@property
	def new_DrawMaterial(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_DrawMaterial",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_DrawMaterial",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_DrawMaterial", res)
		return PropsValueData["new_DrawMaterial"]

	@property
	def new_DrawPrimitive(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_DrawPrimitive",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_DrawPrimitive",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_DrawPrimitive", res)
		return PropsValueData["new_DrawPrimitive"]

	@property
	def new_EdgeBarrier(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_EdgeBarrier",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_EdgeBarrier",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_EdgeBarrier", res)
		return PropsValueData["new_EdgeBarrier"]

	@property
	def new_EdgeNetworkSource(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_EdgeNetworkSource",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_EdgeNetworkSource",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_EdgeNetworkSource", res)
		return PropsValueData["new_EdgeNetworkSource"]

	@property
	def new_Envelope(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_Envelope",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_Envelope",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_Envelope", res)
		return PropsValueData["new_Envelope"]

	@property
	def new_EulerAngle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_EulerAngle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_EulerAngle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_EulerAngle", res)
		return PropsValueData["new_EulerAngle"]

	@property
	def new_FieldInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_FieldInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_FieldInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_FieldInfo", res)
		return PropsValueData["new_FieldInfo"]

	@property
	def new_FieldInfoCollection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_FieldInfoCollection",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_FieldInfoCollection",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_FieldInfoCollection", res)
		return PropsValueData["new_FieldInfoCollection"]

	@property
	def new_FillStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_FillStyle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_FillStyle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_FillStyle", res)
		return PropsValueData["new_FillStyle"]

	@property
	def new_FloatArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_FloatArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_FloatArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_FloatArray", res)
		return PropsValueData["new_FloatArray"]

	@property
	def new_GeometryDef(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_GeometryDef",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_GeometryDef",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_GeometryDef", res)
		return PropsValueData["new_GeometryDef"]

	@property
	def new_GeometryRenderScheme(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_GeometryRenderScheme",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_GeometryRenderScheme",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_GeometryRenderScheme", res)
		return PropsValueData["new_GeometryRenderScheme"]

	@property
	def new_GridIndexInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_GridIndexInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_GridIndexInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_GridIndexInfo", res)
		return PropsValueData["new_GridIndexInfo"]

	@property
	def new_ImagePointSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ImagePointSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ImagePointSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ImagePointSymbol", res)
		return PropsValueData["new_ImagePointSymbol"]

	@property
	def new_JunctionBarrier(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_JunctionBarrier",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_JunctionBarrier",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_JunctionBarrier", res)
		return PropsValueData["new_JunctionBarrier"]

	@property
	def new_JunctionNetworkSource(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_JunctionNetworkSource",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_JunctionNetworkSource",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_JunctionNetworkSource", res)
		return PropsValueData["new_JunctionNetworkSource"]

	@property
	def new_LabelStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_LabelStyle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_LabelStyle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_LabelStyle", res)
		return PropsValueData["new_LabelStyle"]

	@property
	def new_LicenseServer(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_LicenseServer",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_LicenseServer",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_LicenseServer", res)
		return PropsValueData["new_LicenseServer"]

	@property
	def new_LineStyle(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_LineStyle",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_LineStyle",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_LineStyle", res)
		return PropsValueData["new_LineStyle"]

	@property
	def new_Matrix(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_Matrix",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_Matrix",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_Matrix", res)
		return PropsValueData["new_Matrix"]

	@property
	def new_ModelPointSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ModelPointSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ModelPointSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ModelPointSymbol", res)
		return PropsValueData["new_ModelPointSymbol"]

	@property
	def new_NetworkAttribute(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_NetworkAttribute",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_NetworkAttribute",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_NetworkAttribute", res)
		return PropsValueData["new_NetworkAttribute"]

	@property
	def new_NetworkConstantEvaluator(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_NetworkConstantEvaluator",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_NetworkConstantEvaluator",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_NetworkConstantEvaluator", res)
		return PropsValueData["new_NetworkConstantEvaluator"]

	@property
	def new_NetworkEventLocation(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_NetworkEventLocation",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_NetworkEventLocation",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_NetworkEventLocation", res)
		return PropsValueData["new_NetworkEventLocation"]

	@property
	def new_NetworkFieldEvaluator(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_NetworkFieldEvaluator",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_NetworkFieldEvaluator",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_NetworkFieldEvaluator", res)
		return PropsValueData["new_NetworkFieldEvaluator"]

	@property
	def new_NetworkLocation(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_NetworkLocation",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_NetworkLocation",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_NetworkLocation", res)
		return PropsValueData["new_NetworkLocation"]

	@property
	def new_ObjectTexture(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ObjectTexture",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ObjectTexture",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ObjectTexture", res)
		return PropsValueData["new_ObjectTexture"]

	@property
	def new_PointCloudSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_PointCloudSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_PointCloudSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_PointCloudSymbol", res)
		return PropsValueData["new_PointCloudSymbol"]

	@property
	def new_Polygon3DSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_Polygon3DSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_Polygon3DSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_Polygon3DSymbol", res)
		return PropsValueData["new_Polygon3DSymbol"]

	@property
	def new_Position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_Position",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_Position",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_Position", res)
		return PropsValueData["new_Position"]

	@property
	def new_PropertySet(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_PropertySet",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_PropertySet",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_PropertySet", res)
		return PropsValueData["new_PropertySet"]

	@property
	def new_QueryFilter(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_QueryFilter",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_QueryFilter",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_QueryFilter", res)
		return PropsValueData["new_QueryFilter"]

	@property
	def new_RangeRenderRule(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_RangeRenderRule",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_RangeRenderRule",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_RangeRenderRule", res)
		return PropsValueData["new_RangeRenderRule"]

	@property
	def new_RasterSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_RasterSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_RasterSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_RasterSymbol", res)
		return PropsValueData["new_RasterSymbol"]

	@property
	def new_RenderIndexInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_RenderIndexInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_RenderIndexInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_RenderIndexInfo", res)
		return PropsValueData["new_RenderIndexInfo"]

	@property
	def new_RowBufferCollection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_RowBufferCollection",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_RowBufferCollection",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_RowBufferCollection", res)
		return PropsValueData["new_RowBufferCollection"]

	@property
	def new_SimpleGeometryRender(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_SimpleGeometryRender",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_SimpleGeometryRender",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_SimpleGeometryRender", res)
		return PropsValueData["new_SimpleGeometryRender"]

	@property
	def new_SimplePointSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_SimplePointSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_SimplePointSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_SimplePointSymbol", res)
		return PropsValueData["new_SimplePointSymbol"]

	@property
	def new_SimpleTextRender(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_SimpleTextRender",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_SimpleTextRender",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_SimpleTextRender", res)
		return PropsValueData["new_SimpleTextRender"]

	@property
	def new_SolidSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_SolidSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_SolidSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_SolidSymbol", res)
		return PropsValueData["new_SolidSymbol"]

	@property
	def new_SpatialFilter(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_SpatialFilter",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_SpatialFilter",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_SpatialFilter", res)
		return PropsValueData["new_SpatialFilter"]

	@property
	def new_SurfaceSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_SurfaceSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_SurfaceSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_SurfaceSymbol", res)
		return PropsValueData["new_SurfaceSymbol"]

	@property
	def new_TemporalFilter(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_TemporalFilter",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_TemporalFilter",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_TemporalFilter", res)
		return PropsValueData["new_TemporalFilter"]

	@property
	def new_TextAttribute(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_TextAttribute",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_TextAttribute",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_TextAttribute", res)
		return PropsValueData["new_TextAttribute"]

	@property
	def new_TextRenderScheme(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_TextRenderScheme",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_TextRenderScheme",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_TextRenderScheme", res)
		return PropsValueData["new_TextRenderScheme"]

	@property
	def new_TextSymbol(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_TextSymbol",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_TextSymbol",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_TextSymbol", res)
		return PropsValueData["new_TextSymbol"]

	@property
	def new_ToolTipTextRender(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ToolTipTextRender",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ToolTipTextRender",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ToolTipTextRender", res)
		return PropsValueData["new_ToolTipTextRender"]

	@property
	def new_UIDim(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_UIDim",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_UIDim",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_UIDim", res)
		return PropsValueData["new_UIDim"]

	@property
	def new_UIRect(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_UIRect",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_UIRect",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_UIRect", res)
		return PropsValueData["new_UIRect"]

	@property
	def new_UniqueValuesRenderRule(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_UniqueValuesRenderRule",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_UniqueValuesRenderRule",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_UniqueValuesRenderRule", res)
		return PropsValueData["new_UniqueValuesRenderRule"]

	@property
	def new_ValueMapGeometryRender(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ValueMapGeometryRender",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ValueMapGeometryRender",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ValueMapGeometryRender", res)
		return PropsValueData["new_ValueMapGeometryRender"]

	@property
	def new_ValueMapTextRender(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_ValueMapTextRender",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_ValueMapTextRender",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_ValueMapTextRender", res)
		return PropsValueData["new_ValueMapTextRender"]

	@property
	def new_Vector3(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"new_Vector3",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"new_Vector3",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "new_Vector3", res)
		return PropsValueData["new_Vector3"]

	@property
	def objectEditor(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"objectEditor",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"objectEditor",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "objectEditor", res)
		return PropsValueData["objectEditor"]

	@property
	def objectManager(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"objectManager",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"objectManager",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "objectManager", res)
		return PropsValueData["objectManager"]

	@property
	def parametricModelling(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"parametricModelling",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"parametricModelling",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "parametricModelling", res)
		return PropsValueData["parametricModelling"]

	@property
	def polynomialTransformer(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"polynomialTransformer",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"polynomialTransformer",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "polynomialTransformer", res)
		return PropsValueData["polynomialTransformer"]

	@property
	def project(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"project",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"project",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "project", res)
		return PropsValueData["project"]

	@property
	def projectTree(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"projectTree",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"projectTree",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "projectTree", res)
		return PropsValueData["projectTree"]

	@property
	def resourceFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"resourceFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"resourceFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "resourceFactory", res)
		return PropsValueData["resourceFactory"]

	@property
	def dataCopyParam(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"dataCopyParam",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"dataCopyParam",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "dataCopyParam", res)
		return PropsValueData["dataCopyParam"]

	@property
	def layerInfoCollection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"layerInfoCollection",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"layerInfoCollection",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "layerInfoCollection", res)
		return PropsValueData["layerInfoCollection"]

	@property
	def rasterSourceFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"rasterSourceFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rasterSourceFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "rasterSourceFactory", res)
		return PropsValueData["rasterSourceFactory"]

	@property
	def dataInteropFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"dataInteropFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"dataInteropFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "dataInteropFactory", res)
		return PropsValueData["dataInteropFactory"]

	@property
	def commandManagerFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"commandManagerFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"commandManagerFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "commandManagerFactory", res)
		return PropsValueData["commandManagerFactory"]

	@property
	def undoRedoResultCollection(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"undoRedoResultCollection",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"undoRedoResultCollection",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "undoRedoResultCollection", res)
		return PropsValueData["undoRedoResultCollection"]

	@property
	def rowBufferFactory(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"rowBufferFactory",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rowBufferFactory",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "rowBufferFactory", res)
		return PropsValueData["rowBufferFactory"]

	@property
	def sunConfig(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"sunConfig",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"sunConfig",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "sunConfig", res)
		return PropsValueData["sunConfig"]

	@property
	def terrain(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"terrain",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"terrain",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "terrain", res)
		return PropsValueData["terrain"]

	@property
	def terrainAnalyse(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"terrainAnalyse",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"terrainAnalyse",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "terrainAnalyse", res)
		return PropsValueData["terrainAnalyse"]

	@property
	def terrainVideoConfig(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"terrainVideoConfig",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"terrainVideoConfig",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "terrainVideoConfig", res)
		return PropsValueData["terrainVideoConfig"]

	@property
	def transformHelper(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"transformHelper",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"transformHelper",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "transformHelper", res)
		return PropsValueData["transformHelper"]

	@property
	def useEarthOrbitManipulator(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["useEarthOrbitManipulator"]

	@useEarthOrbitManipulator.setter
	def useEarthOrbitManipulator(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "useEarthOrbitManipulator", val)
		args = {}
		args["useEarthOrbitManipulator"] = PropsTypeData.get("useEarthOrbitManipulator")
		args["useEarthOrbitManipulator"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"useEarthOrbitManipulator", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"useEarthOrbitManipulator",JsonData)

	@property
	def useInProcHTMLWindow(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["useInProcHTMLWindow"]

	@useInProcHTMLWindow.setter
	def useInProcHTMLWindow(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "useInProcHTMLWindow", val)
		args = {}
		args["useInProcHTMLWindow"] = PropsTypeData.get("useInProcHTMLWindow")
		args["useInProcHTMLWindow"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"useInProcHTMLWindow", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"useInProcHTMLWindow",JsonData)

	@property
	def utility(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"utility",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"utility",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "utility", res)
		return PropsValueData["utility"]

	@property
	def viewport(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"viewport",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"viewport",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "viewport", res)
		return PropsValueData["viewport"]

	@property
	def visible(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["visible"]

	@visible.setter
	def visible(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "visible", val)
		args = {}
		args["visible"] = PropsTypeData.get("visible")
		args["visible"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"visible", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visible",JsonData)

	@property
	def visualAnalysis(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"visualAnalysis",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"visualAnalysis",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "visualAnalysis", res)
		return PropsValueData["visualAnalysis"]

	@property
	def guid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["guid"]

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
