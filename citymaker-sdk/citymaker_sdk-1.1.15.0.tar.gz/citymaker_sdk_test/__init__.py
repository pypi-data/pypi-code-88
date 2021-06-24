#!/usr/bin/env Python
# coding=utf-8#
#!/usr/bin/env Python
# coding=utf-8#
#作者： tony
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from citymaker_sdk.SDK.Common.IBinaryBuffer import IBinaryBuffer
IBinaryBuffer=IBinaryBuffer
from citymaker_sdk.SDK.Common.ICoordSysDialog import ICoordSysDialog
ICoordSysDialog=ICoordSysDialog
from citymaker_sdk.SDK.Common.IDoubleArray import IDoubleArray
IDoubleArray=IDoubleArray
from citymaker_sdk.SDK.Common.IFloatArray import IFloatArray
IFloatArray=IFloatArray
from citymaker_sdk.SDK.Common.ILicenseServer import ILicenseServer
ILicenseServer=ILicenseServer
from citymaker_sdk.SDK.Common.IPropertySet import IPropertySet
IPropertySet=IPropertySet
from citymaker_sdk.SDK.Common.IRuntimeInfo import IRuntimeInfo
IRuntimeInfo=IRuntimeInfo
from citymaker_sdk.SDK.Common.IUInt16Array import IUInt16Array
IUInt16Array=IUInt16Array
from citymaker_sdk.SDK.Common.IUInt32Array import IUInt32Array
IUInt32Array=IUInt32Array
from citymaker_sdk.SDK.FdeCore.FeatureDataSet import FeatureDataSet
FeatureDataSet=FeatureDataSet
from citymaker_sdk.SDK.FdeCore.IAttachment import IAttachment
IAttachment=IAttachment
from citymaker_sdk.SDK.FdeCore.IAttachmentCollection import IAttachmentCollection
IAttachmentCollection=IAttachmentCollection
from citymaker_sdk.SDK.FdeCore.IAttachmentManager import IAttachmentManager
IAttachmentManager=IAttachmentManager
from citymaker_sdk.SDK.FdeCore.ICheckIn import ICheckIn
ICheckIn=ICheckIn
from citymaker_sdk.SDK.FdeCore.ICheckOut import ICheckOut
ICheckOut=ICheckOut
from citymaker_sdk.SDK.FdeCore.ICodedValueDomain import ICodedValueDomain
ICodedValueDomain=ICodedValueDomain
from citymaker_sdk.SDK.FdeCore.IConflict import IConflict
IConflict=IConflict
from citymaker_sdk.SDK.FdeCore.IConnectionInfo import IConnectionInfo
IConnectionInfo=IConnectionInfo
from citymaker_sdk.SDK.FdeCore.IDataSource import IDataSource
IDataSource=IDataSource
from citymaker_sdk.SDK.FdeCore.IDataSourceFactory import IDataSourceFactory
IDataSourceFactory=IDataSourceFactory
from citymaker_sdk.SDK.FdeCore.IDataSourcePluginManager import IDataSourcePluginManager
IDataSourcePluginManager=IDataSourcePluginManager
from citymaker_sdk.SDK.FdeCore.IDbIndexInfo import IDbIndexInfo
IDbIndexInfo=IDbIndexInfo
from citymaker_sdk.SDK.FdeCore.IDbIndexInfoCollection import IDbIndexInfoCollection
IDbIndexInfoCollection=IDbIndexInfoCollection
from citymaker_sdk.SDK.FdeCore.IDomain import IDomain
IDomain=IDomain
from citymaker_sdk.SDK.FdeCore.IDomainFactory import IDomainFactory
IDomainFactory=IDomainFactory
from citymaker_sdk.SDK.FdeCore.IEnumResName import IEnumResName
IEnumResName=IEnumResName
from citymaker_sdk.SDK.FdeCore.IFdeCursor import IFdeCursor
IFdeCursor=IFdeCursor
from citymaker_sdk.SDK.FdeCore.IFeatureClass import IFeatureClass
IFeatureClass=IFeatureClass
from citymaker_sdk.SDK.FdeCore.IFeatureClassQuery import IFeatureClassQuery
IFeatureClassQuery=IFeatureClassQuery
from citymaker_sdk.SDK.FdeCore.IFeatureDataSet import IFeatureDataSet
IFeatureDataSet=IFeatureDataSet
from citymaker_sdk.SDK.FdeCore.IFeatureProgress import IFeatureProgress
IFeatureProgress=IFeatureProgress
from citymaker_sdk.SDK.FdeCore.IFieldDomainInfo import IFieldDomainInfo
IFieldDomainInfo=IFieldDomainInfo
from citymaker_sdk.SDK.FdeCore.IFieldInfo import IFieldInfo
IFieldInfo=IFieldInfo
from citymaker_sdk.SDK.FdeCore.IFieldInfoCollection import IFieldInfoCollection
IFieldInfoCollection=IFieldInfoCollection
from citymaker_sdk.SDK.FdeCore.IGeometryDef import IGeometryDef
IGeometryDef=IGeometryDef
from citymaker_sdk.SDK.FdeCore.IGridIndexInfo import IGridIndexInfo
IGridIndexInfo=IGridIndexInfo
from citymaker_sdk.SDK.FdeCore.IIndexInfo import IIndexInfo
IIndexInfo=IIndexInfo
from citymaker_sdk.SDK.FdeCore.IIndexInfoCollection import IIndexInfoCollection
IIndexInfoCollection=IIndexInfoCollection
from citymaker_sdk.SDK.FdeCore.IObjectClass import IObjectClass
IObjectClass=IObjectClass
from citymaker_sdk.SDK.FdeCore.IQueryDef import IQueryDef
IQueryDef=IQueryDef
from citymaker_sdk.SDK.FdeCore.IQueryFilter import IQueryFilter
IQueryFilter=IQueryFilter
from citymaker_sdk.SDK.FdeCore.IRangeDomain import IRangeDomain
IRangeDomain=IRangeDomain
from citymaker_sdk.SDK.FdeCore.IRenderIndexInfo import IRenderIndexInfo
IRenderIndexInfo=IRenderIndexInfo
from citymaker_sdk.SDK.FdeCore.IReplication import IReplication
IReplication=IReplication
from citymaker_sdk.SDK.FdeCore.IReplicationFactory import IReplicationFactory
IReplicationFactory=IReplicationFactory
from citymaker_sdk.SDK.FdeCore.IResourceManager import IResourceManager
IResourceManager=IResourceManager
from citymaker_sdk.SDK.FdeCore.IRowBuffer import IRowBuffer
IRowBuffer=IRowBuffer
from citymaker_sdk.SDK.FdeCore.IRowBufferCollection import IRowBufferCollection
IRowBufferCollection=IRowBufferCollection
from citymaker_sdk.SDK.FdeCore.IRowBufferFactory import IRowBufferFactory
IRowBufferFactory=IRowBufferFactory
from citymaker_sdk.SDK.FdeCore.ISpatialFilter import ISpatialFilter
ISpatialFilter=ISpatialFilter
from citymaker_sdk.SDK.FdeCore.ISQLCheck import ISQLCheck
ISQLCheck=ISQLCheck
from citymaker_sdk.SDK.FdeCore.ISubTypeInfo import ISubTypeInfo
ISubTypeInfo=ISubTypeInfo
from citymaker_sdk.SDK.FdeCore.ITable import ITable
ITable=ITable
from citymaker_sdk.SDK.FdeCore.ITemporalCursor import ITemporalCursor
ITemporalCursor=ITemporalCursor
from citymaker_sdk.SDK.FdeCore.ITemporalFilter import ITemporalFilter
ITemporalFilter=ITemporalFilter
from citymaker_sdk.SDK.FdeCore.ITemporalInstance import ITemporalInstance
ITemporalInstance=ITemporalInstance
from citymaker_sdk.SDK.FdeCore.ITemporalInstanceCursor import ITemporalInstanceCursor
ITemporalInstanceCursor=ITemporalInstanceCursor
from citymaker_sdk.SDK.FdeCore.ITemporalManager import ITemporalManager
ITemporalManager=ITemporalManager
from citymaker_sdk.SDK.FdeCore.ITools import ITools
ITools=ITools
from citymaker_sdk.SDK.FdeGeometry.CirculeArc import CirculeArc
CirculeArc=CirculeArc
from citymaker_sdk.SDK.FdeGeometry.ClosedTriMesh import ClosedTriMesh
ClosedTriMesh=ClosedTriMesh
from citymaker_sdk.SDK.FdeGeometry.ICircle import ICircle
ICircle=ICircle
from citymaker_sdk.SDK.FdeGeometry.ICirculeArc import ICirculeArc
ICirculeArc=ICirculeArc
from citymaker_sdk.SDK.FdeGeometry.IClosedTriMesh import IClosedTriMesh
IClosedTriMesh=IClosedTriMesh
from citymaker_sdk.SDK.FdeGeometry.ICompoundLine import ICompoundLine
ICompoundLine=ICompoundLine
from citymaker_sdk.SDK.FdeGeometry.ICoordinateReferenceSystem import ICoordinateReferenceSystem
ICoordinateReferenceSystem=ICoordinateReferenceSystem
from citymaker_sdk.SDK.FdeGeometry.ICoordinateTransformer import ICoordinateTransformer
ICoordinateTransformer=ICoordinateTransformer
from citymaker_sdk.SDK.FdeGeometry.ICRSFactory import ICRSFactory
ICRSFactory=ICRSFactory
from citymaker_sdk.SDK.FdeGeometry.ICurve import ICurve
ICurve=ICurve
from citymaker_sdk.SDK.FdeGeometry.IEastNorthUpCRS import IEastNorthUpCRS
IEastNorthUpCRS=IEastNorthUpCRS
from citymaker_sdk.SDK.FdeGeometry.IGeographicCRS import IGeographicCRS
IGeographicCRS=IGeographicCRS
from citymaker_sdk.SDK.FdeGeometry.IGeometry import IGeometry
IGeometry=IGeometry
from citymaker_sdk.SDK.FdeGeometry.IGeometryCollection import IGeometryCollection
IGeometryCollection=IGeometryCollection
from citymaker_sdk.SDK.FdeGeometry.IGeometryConvertor import IGeometryConvertor
IGeometryConvertor=IGeometryConvertor
from citymaker_sdk.SDK.FdeGeometry.IGeometryFactory import IGeometryFactory
IGeometryFactory=IGeometryFactory
from citymaker_sdk.SDK.FdeGeometry.IGeoTransformer import IGeoTransformer
IGeoTransformer=IGeoTransformer
from citymaker_sdk.SDK.FdeGeometry.ILine import ILine
ILine=ILine
from citymaker_sdk.SDK.FdeGeometry.IModelPoint import IModelPoint
IModelPoint=IModelPoint
from citymaker_sdk.SDK.FdeGeometry.IMultiCurve import IMultiCurve
IMultiCurve=IMultiCurve
from citymaker_sdk.SDK.FdeGeometry.IMultiPoint import IMultiPoint
IMultiPoint=IMultiPoint
from citymaker_sdk.SDK.FdeGeometry.IMultiPolygon import IMultiPolygon
IMultiPolygon=IMultiPolygon
from citymaker_sdk.SDK.FdeGeometry.IMultiPolyline import IMultiPolyline
IMultiPolyline=IMultiPolyline
from citymaker_sdk.SDK.FdeGeometry.IMultiSurface import IMultiSurface
IMultiSurface=IMultiSurface
from citymaker_sdk.SDK.FdeGeometry.IMultiTriMesh import IMultiTriMesh
IMultiTriMesh=IMultiTriMesh
from citymaker_sdk.SDK.FdeGeometry.IParametricModelling import IParametricModelling
IParametricModelling=IParametricModelling
from citymaker_sdk.SDK.FdeGeometry.IPOI import IPOI
IPOI=IPOI
from citymaker_sdk.SDK.FdeGeometry.IPoint import IPoint
IPoint=IPoint
from citymaker_sdk.SDK.FdeGeometry.IPointCloud import IPointCloud
IPointCloud=IPointCloud
from citymaker_sdk.SDK.FdeGeometry.IPolygon import IPolygon
IPolygon=IPolygon
from citymaker_sdk.SDK.FdeGeometry.IPolyline import IPolyline
IPolyline=IPolyline
from citymaker_sdk.SDK.FdeGeometry.IPolynomialTransformer import IPolynomialTransformer
IPolynomialTransformer=IPolynomialTransformer
from citymaker_sdk.SDK.FdeGeometry.IProjectedCRS import IProjectedCRS
IProjectedCRS=IProjectedCRS
from citymaker_sdk.SDK.FdeGeometry.IProximityOperator import IProximityOperator
IProximityOperator=IProximityOperator
from citymaker_sdk.SDK.FdeGeometry.IRelationalOperator2D import IRelationalOperator2D
IRelationalOperator2D=IRelationalOperator2D
from citymaker_sdk.SDK.FdeGeometry.IRelationalOperator3D import IRelationalOperator3D
IRelationalOperator3D=IRelationalOperator3D
from citymaker_sdk.SDK.FdeGeometry.IRing import IRing
IRing=IRing
from citymaker_sdk.SDK.FdeGeometry.ISegment import ISegment
ISegment=ISegment
from citymaker_sdk.SDK.FdeGeometry.ISpatialCRS import ISpatialCRS
ISpatialCRS=ISpatialCRS
from citymaker_sdk.SDK.FdeGeometry.ISurface import ISurface
ISurface=ISurface
from citymaker_sdk.SDK.FdeGeometry.ISurfacePatch import ISurfacePatch
ISurfacePatch=ISurfacePatch
from citymaker_sdk.SDK.FdeGeometry.ITerrainAnalyse import ITerrainAnalyse
ITerrainAnalyse=ITerrainAnalyse
from citymaker_sdk.SDK.FdeGeometry.ITopoDirectedEdge import ITopoDirectedEdge
ITopoDirectedEdge=ITopoDirectedEdge
from citymaker_sdk.SDK.FdeGeometry.ITopoFacet import ITopoFacet
ITopoFacet=ITopoFacet
from citymaker_sdk.SDK.FdeGeometry.ITopologicalOperator2D import ITopologicalOperator2D
ITopologicalOperator2D=ITopologicalOperator2D
from citymaker_sdk.SDK.FdeGeometry.ITopologicalOperator3D import ITopologicalOperator3D
ITopologicalOperator3D=ITopologicalOperator3D
from citymaker_sdk.SDK.FdeGeometry.ITopoNode import ITopoNode
ITopoNode=ITopoNode
from citymaker_sdk.SDK.FdeGeometry.ITransform import ITransform
ITransform=ITransform
from citymaker_sdk.SDK.FdeGeometry.ITriMesh import ITriMesh
ITriMesh=ITriMesh
from citymaker_sdk.SDK.FdeGeometry.IUnknownCRS import IUnknownCRS
IUnknownCRS=IUnknownCRS
from citymaker_sdk.SDK.FdeGeometry.Line import Line
Line=Line
from citymaker_sdk.SDK.FdeGeometry.MultiPoint import MultiPoint
MultiPoint=MultiPoint
from citymaker_sdk.SDK.FdeGeometry.Point import Point
Point=Point
from citymaker_sdk.SDK.FdeGeometry.Polygon import Polygon
Polygon=Polygon
from citymaker_sdk.SDK.FdeGeometry.Polyline import Polyline
Polyline=Polyline
from citymaker_sdk.SDK.Global.IGlobal import IGlobal
IGlobal=IGlobal
from citymaker_sdk.SDK.Math.IEnvelope import IEnvelope
IEnvelope=IEnvelope
from citymaker_sdk.SDK.Math.IEulerAngle import IEulerAngle
IEulerAngle=IEulerAngle
from citymaker_sdk.SDK.Math.IMatrix import IMatrix
IMatrix=IMatrix
from citymaker_sdk.SDK.Math.IVector3 import IVector3
IVector3=IVector3
from citymaker_sdk.SDK.Network.IEdgeBarrier import IEdgeBarrier
IEdgeBarrier=IEdgeBarrier
from citymaker_sdk.SDK.Network.IEdgeNetworkSource import IEdgeNetworkSource
IEdgeNetworkSource=IEdgeNetworkSource
from citymaker_sdk.SDK.Network.IJunctionBarrier import IJunctionBarrier
IJunctionBarrier=IJunctionBarrier
from citymaker_sdk.SDK.Network.IJunctionNetworkSource import IJunctionNetworkSource
IJunctionNetworkSource=IJunctionNetworkSource
from citymaker_sdk.SDK.Network.ILogicalNetwork import ILogicalNetwork
ILogicalNetwork=ILogicalNetwork
from citymaker_sdk.SDK.Network.INetwork import INetwork
INetwork=INetwork
from citymaker_sdk.SDK.Network.INetworkAttribute import INetworkAttribute
INetworkAttribute=INetworkAttribute
from citymaker_sdk.SDK.Network.INetworkBarrier import INetworkBarrier
INetworkBarrier=INetworkBarrier
from citymaker_sdk.SDK.Network.INetworkClosestFacilitySolver import INetworkClosestFacilitySolver
INetworkClosestFacilitySolver=INetworkClosestFacilitySolver
from citymaker_sdk.SDK.Network.INetworkConstantEvaluator import INetworkConstantEvaluator
INetworkConstantEvaluator=INetworkConstantEvaluator
from citymaker_sdk.SDK.Network.INetworkEdge import INetworkEdge
INetworkEdge=INetworkEdge
from citymaker_sdk.SDK.Network.INetworkEdgeCollection import INetworkEdgeCollection
INetworkEdgeCollection=INetworkEdgeCollection
from citymaker_sdk.SDK.Network.INetworkElement import INetworkElement
INetworkElement=INetworkElement
from citymaker_sdk.SDK.Network.INetworkElementCollection import INetworkElementCollection
INetworkElementCollection=INetworkElementCollection
from citymaker_sdk.SDK.Network.INetworkEvaluator import INetworkEvaluator
INetworkEvaluator=INetworkEvaluator
from citymaker_sdk.SDK.Network.INetworkEventLocation import INetworkEventLocation
INetworkEventLocation=INetworkEventLocation
from citymaker_sdk.SDK.Network.INetworkFieldEvaluator import INetworkFieldEvaluator
INetworkFieldEvaluator=INetworkFieldEvaluator
from citymaker_sdk.SDK.Network.INetworkFindAncestorsSolver import INetworkFindAncestorsSolver
INetworkFindAncestorsSolver=INetworkFindAncestorsSolver
from citymaker_sdk.SDK.Network.INetworkFindConnectedSolver import INetworkFindConnectedSolver
INetworkFindConnectedSolver=INetworkFindConnectedSolver
from citymaker_sdk.SDK.Network.INetworkFindDisconnectedSolver import INetworkFindDisconnectedSolver
INetworkFindDisconnectedSolver=INetworkFindDisconnectedSolver
from citymaker_sdk.SDK.Network.INetworkFindLoopsSolver import INetworkFindLoopsSolver
INetworkFindLoopsSolver=INetworkFindLoopsSolver
from citymaker_sdk.SDK.Network.INetworkJunction import INetworkJunction
INetworkJunction=INetworkJunction
from citymaker_sdk.SDK.Network.INetworkLoader import INetworkLoader
INetworkLoader=INetworkLoader
from citymaker_sdk.SDK.Network.INetworkLocation import INetworkLocation
INetworkLocation=INetworkLocation
from citymaker_sdk.SDK.Network.INetworkManager import INetworkManager
INetworkManager=INetworkManager
from citymaker_sdk.SDK.Network.INetworkRoute import INetworkRoute
INetworkRoute=INetworkRoute
from citymaker_sdk.SDK.Network.INetworkRouteSegment import INetworkRouteSegment
INetworkRouteSegment=INetworkRouteSegment
from citymaker_sdk.SDK.Network.INetworkRouteSolver import INetworkRouteSolver
INetworkRouteSolver=INetworkRouteSolver
from citymaker_sdk.SDK.Network.INetworkScriptEvaluator import INetworkScriptEvaluator
INetworkScriptEvaluator=INetworkScriptEvaluator
from citymaker_sdk.SDK.Network.INetworkSolver import INetworkSolver
INetworkSolver=INetworkSolver
from citymaker_sdk.SDK.Network.INetworkSource import INetworkSource
INetworkSource=INetworkSource
from citymaker_sdk.SDK.Network.INetworkTraceDownstreamSolver import INetworkTraceDownstreamSolver
INetworkTraceDownstreamSolver=INetworkTraceDownstreamSolver
from citymaker_sdk.SDK.Network.INetworkTraceResult import INetworkTraceResult
INetworkTraceResult=INetworkTraceResult
from citymaker_sdk.SDK.Network.INetworkTraceUpstreamSolver import INetworkTraceUpstreamSolver
INetworkTraceUpstreamSolver=INetworkTraceUpstreamSolver
from citymaker_sdk.SDK.RenderControl.AxRenderControl import AxRenderControl
AxRenderControl=AxRenderControl
from citymaker_sdk.SDK.RenderControl.ComplexParticleEffect import ComplexParticleEffect
ComplexParticleEffect=ComplexParticleEffect
from citymaker_sdk.SDK.RenderControl.I3DTileLayer import I3DTileLayer
I3DTileLayer=I3DTileLayer
from citymaker_sdk.SDK.RenderControl.I3DTileLayerPickResult import I3DTileLayerPickResult
I3DTileLayerPickResult=I3DTileLayerPickResult
from citymaker_sdk.SDK.RenderControl.IAttackArrow import IAttackArrow
IAttackArrow=IAttackArrow
from citymaker_sdk.SDK.RenderControl.IAttackArrowPickResult import IAttackArrowPickResult
IAttackArrowPickResult=IAttackArrowPickResult
from citymaker_sdk.SDK.RenderControl.ICacheManager import ICacheManager
ICacheManager=ICacheManager
from citymaker_sdk.SDK.RenderControl.ICamera import ICamera
ICamera=ICamera
from citymaker_sdk.SDK.RenderControl.ICameraTour import ICameraTour
ICameraTour=ICameraTour
from citymaker_sdk.SDK.RenderControl.IClipPlaneOperation import IClipPlaneOperation
IClipPlaneOperation=IClipPlaneOperation
from citymaker_sdk.SDK.RenderControl.IComparedRenderRule import IComparedRenderRule
IComparedRenderRule=IComparedRenderRule
from citymaker_sdk.SDK.RenderControl.IComplexParticleEffect import IComplexParticleEffect
IComplexParticleEffect=IComplexParticleEffect
from citymaker_sdk.SDK.RenderControl.IComplexParticleEffectPickResult import IComplexParticleEffectPickResult
IComplexParticleEffectPickResult=IComplexParticleEffectPickResult
from citymaker_sdk.SDK.RenderControl.ICurveSymbol import ICurveSymbol
ICurveSymbol=ICurveSymbol
from citymaker_sdk.SDK.RenderControl.IDoubleArrow import IDoubleArrow
IDoubleArrow=IDoubleArrow
from citymaker_sdk.SDK.RenderControl.IDoubleArrowPickResult import IDoubleArrowPickResult
IDoubleArrowPickResult=IDoubleArrowPickResult
from citymaker_sdk.SDK.RenderControl.IDynamicObject import IDynamicObject
IDynamicObject=IDynamicObject
from citymaker_sdk.SDK.RenderControl.IExportManager import IExportManager
IExportManager=IExportManager
from citymaker_sdk.SDK.RenderControl.IFeatureClassInfo import IFeatureClassInfo
IFeatureClassInfo=IFeatureClassInfo
from citymaker_sdk.SDK.RenderControl.IFeatureLayer import IFeatureLayer
IFeatureLayer=IFeatureLayer
from citymaker_sdk.SDK.RenderControl.IFeatureLayerPickResult import IFeatureLayerPickResult
IFeatureLayerPickResult=IFeatureLayerPickResult
from citymaker_sdk.SDK.RenderControl.IFeatureManager import IFeatureManager
IFeatureManager=IFeatureManager
from citymaker_sdk.SDK.RenderControl.IFillStyle import IFillStyle
IFillStyle=IFillStyle
from citymaker_sdk.SDK.RenderControl.IGatheringPlace import IGatheringPlace
IGatheringPlace=IGatheringPlace
from citymaker_sdk.SDK.RenderControl.IGatheringPlacePickResult import IGatheringPlacePickResult
IGatheringPlacePickResult=IGatheringPlacePickResult
from citymaker_sdk.SDK.RenderControl.IGeometryRender import IGeometryRender
IGeometryRender=IGeometryRender
from citymaker_sdk.SDK.RenderControl.IGeometryRenderScheme import IGeometryRenderScheme
IGeometryRenderScheme=IGeometryRenderScheme
from citymaker_sdk.SDK.RenderControl.IGeometrySymbol import IGeometrySymbol
IGeometrySymbol=IGeometrySymbol
from citymaker_sdk.SDK.RenderControl.IHeatMap import IHeatMap
IHeatMap=IHeatMap
from citymaker_sdk.SDK.RenderControl.IHeatMapPlayer import IHeatMapPlayer
IHeatMapPlayer=IHeatMapPlayer
from citymaker_sdk.SDK.RenderControl.IHighlightHelper import IHighlightHelper
IHighlightHelper=IHighlightHelper
from citymaker_sdk.SDK.RenderControl.IHTMLWindow import IHTMLWindow
IHTMLWindow=IHTMLWindow
from citymaker_sdk.SDK.RenderControl.IImagePointSymbol import IImagePointSymbol
IImagePointSymbol=IImagePointSymbol
from citymaker_sdk.SDK.RenderControl.IImageryLayer import IImageryLayer
IImageryLayer=IImageryLayer
from citymaker_sdk.SDK.RenderControl.IKmlGroup import IKmlGroup
IKmlGroup=IKmlGroup
from citymaker_sdk.SDK.RenderControl.ILabel import ILabel
ILabel=ILabel
from citymaker_sdk.SDK.RenderControl.ILabelPickResult import ILabelPickResult
ILabelPickResult=ILabelPickResult
from citymaker_sdk.SDK.RenderControl.ILabelStyle import ILabelStyle
ILabelStyle=ILabelStyle
from citymaker_sdk.SDK.RenderControl.ILineStyle import ILineStyle
ILineStyle=ILineStyle
from citymaker_sdk.SDK.RenderControl.IModelPointSymbol import IModelPointSymbol
IModelPointSymbol=IModelPointSymbol
from citymaker_sdk.SDK.RenderControl.IMotionable import IMotionable
IMotionable=IMotionable
from citymaker_sdk.SDK.RenderControl.IMotionPath import IMotionPath
IMotionPath=IMotionPath
from citymaker_sdk.SDK.RenderControl.IObjectEditor import IObjectEditor
IObjectEditor=IObjectEditor
from citymaker_sdk.SDK.RenderControl.IObjectManager import IObjectManager
IObjectManager=IObjectManager
from citymaker_sdk.SDK.RenderControl.IObjectTexture import IObjectTexture
IObjectTexture=IObjectTexture
from citymaker_sdk.SDK.RenderControl.IOperation import IOperation
IOperation=IOperation
from citymaker_sdk.SDK.RenderControl.IOverlayLabel import IOverlayLabel
IOverlayLabel=IOverlayLabel
from citymaker_sdk.SDK.RenderControl.IOverlayLabelPickResult import IOverlayLabelPickResult
IOverlayLabelPickResult=IOverlayLabelPickResult
from citymaker_sdk.SDK.RenderControl.IOverlayUILabel import IOverlayUILabel
IOverlayUILabel=IOverlayUILabel
from citymaker_sdk.SDK.RenderControl.IParticleEffect import IParticleEffect
IParticleEffect=IParticleEffect
from citymaker_sdk.SDK.RenderControl.IParticleEffectPickResult import IParticleEffectPickResult
IParticleEffectPickResult=IParticleEffectPickResult
from citymaker_sdk.SDK.RenderControl.IPickResult import IPickResult
IPickResult=IPickResult
from citymaker_sdk.SDK.RenderControl.IPickResultCollection import IPickResultCollection
IPickResultCollection=IPickResultCollection
from citymaker_sdk.SDK.RenderControl.IPlot import IPlot
IPlot=IPlot
from citymaker_sdk.SDK.RenderControl.IPointCloudSymbol import IPointCloudSymbol
IPointCloudSymbol=IPointCloudSymbol
from citymaker_sdk.SDK.RenderControl.IPointSymbol import IPointSymbol
IPointSymbol=IPointSymbol
from citymaker_sdk.SDK.RenderControl.IPolygon3DSymbol import IPolygon3DSymbol
IPolygon3DSymbol=IPolygon3DSymbol
from citymaker_sdk.SDK.RenderControl.IPosition import IPosition
IPosition=IPosition
from citymaker_sdk.SDK.RenderControl.IPresentation import IPresentation
IPresentation=IPresentation
from citymaker_sdk.SDK.RenderControl.IPresentationStep import IPresentationStep
IPresentationStep=IPresentationStep
from citymaker_sdk.SDK.RenderControl.IPresentationSteps import IPresentationSteps
IPresentationSteps=IPresentationSteps
from citymaker_sdk.SDK.RenderControl.IProject import IProject
IProject=IProject
from citymaker_sdk.SDK.RenderControl.IProjectTree import IProjectTree
IProjectTree=IProjectTree
from citymaker_sdk.SDK.RenderControl.IProjectTreeNode import IProjectTreeNode
IProjectTreeNode=IProjectTreeNode
from citymaker_sdk.SDK.RenderControl.IRangeRenderRule import IRangeRenderRule
IRangeRenderRule=IRangeRenderRule
from citymaker_sdk.SDK.RenderControl.IRasterSymbol import IRasterSymbol
IRasterSymbol=IRasterSymbol
from citymaker_sdk.SDK.RenderControl.IReferencePlane import IReferencePlane
IReferencePlane=IReferencePlane
from citymaker_sdk.SDK.RenderControl.IReferencePlanePickResult import IReferencePlanePickResult
IReferencePlanePickResult=IReferencePlanePickResult
from citymaker_sdk.SDK.RenderControl.IRenderable import IRenderable
IRenderable=IRenderable
from citymaker_sdk.SDK.RenderControl.IRenderArrow import IRenderArrow
IRenderArrow=IRenderArrow
from citymaker_sdk.SDK.RenderControl.IRenderArrowPickResult import IRenderArrowPickResult
IRenderArrowPickResult=IRenderArrowPickResult
from citymaker_sdk.SDK.RenderControl.IRenderControl import IRenderControl
IRenderControl=IRenderControl
from citymaker_sdk.SDK.RenderControl.IRenderControlEvents import IRenderControlEvents
IRenderControlEvents=IRenderControlEvents
from citymaker_sdk.SDK.RenderControl.IRenderGeometry import IRenderGeometry
IRenderGeometry=IRenderGeometry
from citymaker_sdk.SDK.RenderControl.IRenderModelPoint import IRenderModelPoint
IRenderModelPoint=IRenderModelPoint
from citymaker_sdk.SDK.RenderControl.IRenderModelPointPickResult import IRenderModelPointPickResult
IRenderModelPointPickResult=IRenderModelPointPickResult
from citymaker_sdk.SDK.RenderControl.IRenderMultiPoint import IRenderMultiPoint
IRenderMultiPoint=IRenderMultiPoint
from citymaker_sdk.SDK.RenderControl.IRenderMultiPointPickResult import IRenderMultiPointPickResult
IRenderMultiPointPickResult=IRenderMultiPointPickResult
from citymaker_sdk.SDK.RenderControl.IRenderMultiPolygon import IRenderMultiPolygon
IRenderMultiPolygon=IRenderMultiPolygon
from citymaker_sdk.SDK.RenderControl.IRenderMultiPolygonPickResult import IRenderMultiPolygonPickResult
IRenderMultiPolygonPickResult=IRenderMultiPolygonPickResult
from citymaker_sdk.SDK.RenderControl.IRenderMultiPolyline import IRenderMultiPolyline
IRenderMultiPolyline=IRenderMultiPolyline
from citymaker_sdk.SDK.RenderControl.IRenderMultiPolylinePickResult import IRenderMultiPolylinePickResult
IRenderMultiPolylinePickResult=IRenderMultiPolylinePickResult
from citymaker_sdk.SDK.RenderControl.IRenderMultiTriMesh import IRenderMultiTriMesh
IRenderMultiTriMesh=IRenderMultiTriMesh
from citymaker_sdk.SDK.RenderControl.IRenderMultiTriMeshPickResult import IRenderMultiTriMeshPickResult
IRenderMultiTriMeshPickResult=IRenderMultiTriMeshPickResult
from citymaker_sdk.SDK.RenderControl.IRenderPipeLine import IRenderPipeLine
IRenderPipeLine=IRenderPipeLine
from citymaker_sdk.SDK.RenderControl.IRenderPOI import IRenderPOI
IRenderPOI=IRenderPOI
from citymaker_sdk.SDK.RenderControl.IRenderPoint import IRenderPoint
IRenderPoint=IRenderPoint
from citymaker_sdk.SDK.RenderControl.IRenderPointPickResult import IRenderPointPickResult
IRenderPointPickResult=IRenderPointPickResult
from citymaker_sdk.SDK.RenderControl.IRenderPOIPickResult import IRenderPOIPickResult
IRenderPOIPickResult=IRenderPOIPickResult
from citymaker_sdk.SDK.RenderControl.IRenderPolygon import IRenderPolygon
IRenderPolygon=IRenderPolygon
from citymaker_sdk.SDK.RenderControl.IRenderPolygonPickResult import IRenderPolygonPickResult
IRenderPolygonPickResult=IRenderPolygonPickResult
from citymaker_sdk.SDK.RenderControl.IRenderPolyline import IRenderPolyline
IRenderPolyline=IRenderPolyline
from citymaker_sdk.SDK.RenderControl.IRenderPolylinePickResult import IRenderPolylinePickResult
IRenderPolylinePickResult=IRenderPolylinePickResult
from citymaker_sdk.SDK.RenderControl.IRenderRule import IRenderRule
IRenderRule=IRenderRule
from citymaker_sdk.SDK.RenderControl.IRenderTriMesh import IRenderTriMesh
IRenderTriMesh=IRenderTriMesh
from citymaker_sdk.SDK.RenderControl.IRenderTriMeshPickResult import IRenderTriMeshPickResult
IRenderTriMeshPickResult=IRenderTriMeshPickResult
from citymaker_sdk.SDK.RenderControl.IRObject import IRObject
IRObject=IRObject
from citymaker_sdk.SDK.RenderControl.ISimpleGeometryRender import ISimpleGeometryRender
ISimpleGeometryRender=ISimpleGeometryRender
from citymaker_sdk.SDK.RenderControl.ISimplePointSymbol import ISimplePointSymbol
ISimplePointSymbol=ISimplePointSymbol
from citymaker_sdk.SDK.RenderControl.ISimpleTextRender import ISimpleTextRender
ISimpleTextRender=ISimpleTextRender
from citymaker_sdk.SDK.RenderControl.ISkinnedMesh import ISkinnedMesh
ISkinnedMesh=ISkinnedMesh
from citymaker_sdk.SDK.RenderControl.ISkinnedMeshPickResult import ISkinnedMeshPickResult
ISkinnedMeshPickResult=ISkinnedMeshPickResult
from citymaker_sdk.SDK.RenderControl.ISkyBox import ISkyBox
ISkyBox=ISkyBox
from citymaker_sdk.SDK.RenderControl.ISolidSymbol import ISolidSymbol
ISolidSymbol=ISolidSymbol
from citymaker_sdk.SDK.RenderControl.ISquadCombat import ISquadCombat
ISquadCombat=ISquadCombat
from citymaker_sdk.SDK.RenderControl.ISquadCombatPickResult import ISquadCombatPickResult
ISquadCombatPickResult=ISquadCombatPickResult
from citymaker_sdk.SDK.RenderControl.ISunConfig import ISunConfig
ISunConfig=ISunConfig
from citymaker_sdk.SDK.RenderControl.ISurfaceSymbol import ISurfaceSymbol
ISurfaceSymbol=ISurfaceSymbol
from citymaker_sdk.SDK.RenderControl.ITableLabel import ITableLabel
ITableLabel=ITableLabel
from citymaker_sdk.SDK.RenderControl.ITableLabelPickResult import ITableLabelPickResult
ITableLabelPickResult=ITableLabelPickResult
from citymaker_sdk.SDK.RenderControl.ITailedAttackArrow import ITailedAttackArrow
ITailedAttackArrow=ITailedAttackArrow
from citymaker_sdk.SDK.RenderControl.ITailedAttackArrowPickResult import ITailedAttackArrowPickResult
ITailedAttackArrowPickResult=ITailedAttackArrowPickResult
from citymaker_sdk.SDK.RenderControl.ITailedSquadCombat import ITailedSquadCombat
ITailedSquadCombat=ITailedSquadCombat
from citymaker_sdk.SDK.RenderControl.ITailedSquadCombatPickResult import ITailedSquadCombatPickResult
ITailedSquadCombatPickResult=ITailedSquadCombatPickResult
from citymaker_sdk.SDK.RenderControl.ITerrain import ITerrain
ITerrain=ITerrain
from citymaker_sdk.SDK.RenderControl.ITerrain3DArrow import ITerrain3DArrow
ITerrain3DArrow=ITerrain3DArrow
from citymaker_sdk.SDK.RenderControl.ITerrain3DArrowPickResult import ITerrain3DArrowPickResult
ITerrain3DArrowPickResult=ITerrain3DArrowPickResult
from citymaker_sdk.SDK.RenderControl.ITerrain3DRectBase import ITerrain3DRectBase
ITerrain3DRectBase=ITerrain3DRectBase
from citymaker_sdk.SDK.RenderControl.ITerrain3DRegBase import ITerrain3DRegBase
ITerrain3DRegBase=ITerrain3DRegBase
from citymaker_sdk.SDK.RenderControl.ITerrainArc import ITerrainArc
ITerrainArc=ITerrainArc
from citymaker_sdk.SDK.RenderControl.ITerrainArcPickResult import ITerrainArcPickResult
ITerrainArcPickResult=ITerrainArcPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainArrow import ITerrainArrow
ITerrainArrow=ITerrainArrow
from citymaker_sdk.SDK.RenderControl.ITerrainArrowPickResult import ITerrainArrowPickResult
ITerrainArrowPickResult=ITerrainArrowPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainBoxPickResult import ITerrainBoxPickResult
ITerrainBoxPickResult=ITerrainBoxPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainConePickResult import ITerrainConePickResult
ITerrainConePickResult=ITerrainConePickResult
from citymaker_sdk.SDK.RenderControl.ITerrainCylinderPickResult import ITerrainCylinderPickResult
ITerrainCylinderPickResult=ITerrainCylinderPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainEllipse import ITerrainEllipse
ITerrainEllipse=ITerrainEllipse
from citymaker_sdk.SDK.RenderControl.ITerrainEllipsePickResult import ITerrainEllipsePickResult
ITerrainEllipsePickResult=ITerrainEllipsePickResult
from citymaker_sdk.SDK.RenderControl.ITerrainHole import ITerrainHole
ITerrainHole=ITerrainHole
from citymaker_sdk.SDK.RenderControl.ITerrainHolePickResult import ITerrainHolePickResult
ITerrainHolePickResult=ITerrainHolePickResult
from citymaker_sdk.SDK.RenderControl.ITerrainImageLabel import ITerrainImageLabel
ITerrainImageLabel=ITerrainImageLabel
from citymaker_sdk.SDK.RenderControl.ITerrainImageLabelPickResult import ITerrainImageLabelPickResult
ITerrainImageLabelPickResult=ITerrainImageLabelPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainLocation import ITerrainLocation
ITerrainLocation=ITerrainLocation
from citymaker_sdk.SDK.RenderControl.ITerrainModifier import ITerrainModifier
ITerrainModifier=ITerrainModifier
from citymaker_sdk.SDK.RenderControl.ITerrainModifierPickResult import ITerrainModifierPickResult
ITerrainModifierPickResult=ITerrainModifierPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainPickResult import ITerrainPickResult
ITerrainPickResult=ITerrainPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainPyramidPickResult import ITerrainPyramidPickResult
ITerrainPyramidPickResult=ITerrainPyramidPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainRectangle import ITerrainRectangle
ITerrainRectangle=ITerrainRectangle
from citymaker_sdk.SDK.RenderControl.ITerrainRectanglePickResult import ITerrainRectanglePickResult
ITerrainRectanglePickResult=ITerrainRectanglePickResult
from citymaker_sdk.SDK.RenderControl.ITerrainRegularPolygon import ITerrainRegularPolygon
ITerrainRegularPolygon=ITerrainRegularPolygon
from citymaker_sdk.SDK.RenderControl.ITerrainRegularPolygonPickResult import ITerrainRegularPolygonPickResult
ITerrainRegularPolygonPickResult=ITerrainRegularPolygonPickResult
from citymaker_sdk.SDK.RenderControl.ITerrainRoute import ITerrainRoute
ITerrainRoute=ITerrainRoute
from citymaker_sdk.SDK.RenderControl.ITerrainSphere import ITerrainSphere
ITerrainSphere=ITerrainSphere
from citymaker_sdk.SDK.RenderControl.ITerrainSpherePickResult import ITerrainSpherePickResult
ITerrainSpherePickResult=ITerrainSpherePickResult
from citymaker_sdk.SDK.RenderControl.ITerrainVideo import ITerrainVideo
ITerrainVideo=ITerrainVideo
from citymaker_sdk.SDK.RenderControl.ITerrainVideoConfig import ITerrainVideoConfig
ITerrainVideoConfig=ITerrainVideoConfig
from citymaker_sdk.SDK.RenderControl.ITextAttribute import ITextAttribute
ITextAttribute=ITextAttribute
from citymaker_sdk.SDK.RenderControl.ITextRender import ITextRender
ITextRender=ITextRender
from citymaker_sdk.SDK.RenderControl.ITextRenderScheme import ITextRenderScheme
ITextRenderScheme=ITextRenderScheme
from citymaker_sdk.SDK.RenderControl.ITextSymbol import ITextSymbol
ITextSymbol=ITextSymbol
from citymaker_sdk.SDK.RenderControl.IToolTipTextRender import IToolTipTextRender
IToolTipTextRender=IToolTipTextRender
from citymaker_sdk.SDK.RenderControl.ITransformHelper import ITransformHelper
ITransformHelper=ITransformHelper
from citymaker_sdk.SDK.RenderControl.ITripleArrow import ITripleArrow
ITripleArrow=ITripleArrow
from citymaker_sdk.SDK.RenderControl.ITripleArrowPickResult import ITripleArrowPickResult
ITripleArrowPickResult=ITripleArrowPickResult
from citymaker_sdk.SDK.RenderControl.IUniqueValuesRenderRule import IUniqueValuesRenderRule
IUniqueValuesRenderRule=IUniqueValuesRenderRule
from citymaker_sdk.SDK.RenderControl.IUtility import IUtility
IUtility=IUtility
from citymaker_sdk.SDK.RenderControl.IValueMapGeometryRender import IValueMapGeometryRender
IValueMapGeometryRender=IValueMapGeometryRender
from citymaker_sdk.SDK.RenderControl.IValueMapTextRender import IValueMapTextRender
IValueMapTextRender=IValueMapTextRender
from citymaker_sdk.SDK.RenderControl.IViewport import IViewport
IViewport=IViewport
from citymaker_sdk.SDK.RenderControl.IViewshed import IViewshed
IViewshed=IViewshed
from citymaker_sdk.SDK.RenderControl.IVisualAnalysis import IVisualAnalysis
IVisualAnalysis=IVisualAnalysis
from citymaker_sdk.SDK.RenderControl.IVolumeMeasureOperation import IVolumeMeasureOperation
IVolumeMeasureOperation=IVolumeMeasureOperation
from citymaker_sdk.SDK.RenderControl.IWalkGround import IWalkGround
IWalkGround=IWalkGround
from citymaker_sdk.SDK.RenderControl.IWindowParam import IWindowParam
IWindowParam=IWindowParam
from citymaker_sdk.SDK.RenderControl.Label import Label
Label=Label
from citymaker_sdk.SDK.RenderControl.ParticleEffect import ParticleEffect
ParticleEffect=ParticleEffect
from citymaker_sdk.SDK.RenderControl.RenderGeometry import RenderGeometry
RenderGeometry=RenderGeometry
from citymaker_sdk.SDK.RenderControl.SkinnedMesh import SkinnedMesh
SkinnedMesh=SkinnedMesh
from citymaker_sdk.SDK.RenderControl.TableLabel import TableLabel
TableLabel=TableLabel
from citymaker_sdk.SDK.RenderControl.TerrainVideo import TerrainVideo
TerrainVideo=TerrainVideo
from citymaker_sdk.SDK.RenderControl.TiledFeatureLayer import TiledFeatureLayer
TiledFeatureLayer=TiledFeatureLayer
from citymaker_sdk.SDK.RenderControl.Viewshed import Viewshed
Viewshed=Viewshed
from citymaker_sdk.SDK.Resource.IDrawGroup import IDrawGroup
IDrawGroup=IDrawGroup
from citymaker_sdk.SDK.Resource.IDrawMaterial import IDrawMaterial
IDrawMaterial=IDrawMaterial
from citymaker_sdk.SDK.Resource.IDrawPrimitive import IDrawPrimitive
IDrawPrimitive=IDrawPrimitive
from citymaker_sdk.SDK.Resource.IImage import IImage
IImage=IImage
from citymaker_sdk.SDK.Resource.IModel import IModel
IModel=IModel
from citymaker_sdk.SDK.Resource.IModelTools import IModelTools
IModelTools=IModelTools
from citymaker_sdk.SDK.Resource.IResourceFactory import IResourceFactory
IResourceFactory=IResourceFactory
from citymaker_sdk.SDK.Resource.ISkinnedModel import ISkinnedModel
ISkinnedModel=ISkinnedModel
from citymaker_sdk.SDK.UISystem.IUIDim import IUIDim
IUIDim=IUIDim
from citymaker_sdk.SDK.UISystem.IUIEventArgs import IUIEventArgs
IUIEventArgs=IUIEventArgs
from citymaker_sdk.SDK.UISystem.IUIImageButton import IUIImageButton
IUIImageButton=IUIImageButton
from citymaker_sdk.SDK.UISystem.IUIMouseEventArgs import IUIMouseEventArgs
IUIMouseEventArgs=IUIMouseEventArgs
from citymaker_sdk.SDK.UISystem.IUIRect import IUIRect
IUIRect=IUIRect
from citymaker_sdk.SDK.UISystem.IUIStaticImage import IUIStaticImage
IUIStaticImage=IUIStaticImage
from citymaker_sdk.SDK.UISystem.IUIStaticLabel import IUIStaticLabel
IUIStaticLabel=IUIStaticLabel
from citymaker_sdk.SDK.UISystem.IUITextButton import IUITextButton
IUITextButton=IUITextButton
from citymaker_sdk.SDK.UISystem.IUIWindow import IUIWindow
IUIWindow=IUIWindow
from citymaker_sdk.SDK.UISystem.IUIWindowEventArgs import IUIWindowEventArgs
IUIWindowEventArgs=IUIWindowEventArgs
from citymaker_sdk.SDK.UISystem.IUIWindowManager import IUIWindowManager
IUIWindowManager=IUIWindowManager
from citymaker_sdk.Utils.Config import Config 
Config=Config
from citymaker_sdk.Utils.RenderViewer3D import RenderViewer3D
RenderViewer3D=RenderViewer3D