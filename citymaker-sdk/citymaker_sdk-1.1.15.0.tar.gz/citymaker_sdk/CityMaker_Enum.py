#!/usr/bin/env Python
# coding=utf-8#
#作者： tony
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from enum import Enum
class gviCompareType(Enum):
	gviCompareGreater=0
	gviCompareLess=1
	gviCompareEqual=2
	gviCompareGreaterOrEqual=3
	gviCompareLessOrEqual=4
	gviCompareNotEqual=5

class gviPolygonCreateMode(Enum):
	gviPolygonCreateProjectedPlane=0
	gviPolygonCreateFirstPointHeight=1
	gviPolygonCreateAverageHorizontalPlane=2
	gviPolygonCreateThreePointPlane=3

class gviRenderPipeLinePlayMode(Enum):
	gviPipeLinePlayShowTrack=0
	gviPipeLinePlayNoTrack=1
	gviPipeLinePlayDrawTrack=2

class gviPIPLocationMode(Enum):
	gviPIPLocationRightBottom=0
	gviPIPLocationRightTop=1
	gviPIPLocationLeftTop=2
	gviPIPLocationLeftBottom=3

class gviModelCheckErrorType(Enum):
	gviModelCheckErrorTooLargeCoord=0
	gviModelCheckErrorIndexOutBound=1

class gviLanguage(Enum):
	gviLanguageChineseSimple=0
	gviLanguageChineseTraditional=1
	gviLanguageEnglish=2

class gviFieldType(Enum):
	gviFieldUnknown=0
	gviFieldInt16=2
	gviFieldInt32=3
	gviFieldInt64=4
	gviFieldFloat=5
	gviFieldDouble=6
	gviFieldString=7
	gviFieldDate=8
	gviFieldBlob=9
	gviFieldFID=10
	gviFieldUUID=11
	gviFieldGeometry=99

class gviDomainType(Enum):
	gviDomainRange=0
	gviDomainCodedValue=1

class gviGeometryColumnType(Enum):
	gviGeometryColumnPoint=0
	gviGeometryColumnModelPoint=1
	gviGeometryColumnPOI=2
	gviGeometryColumnMultiPoint=3
	gviGeometryColumnPolyline=4
	gviGeometryColumnPolygon=5
	gviGeometryColumnTriMesh=7
	gviGeometryColumnPointCloud=8
	gviGeometryColumnCollection=9
	gviGeometryColumnUnknown=-1

class gviIndexType(Enum):
	gviIndexRdbms=0
	gviIndexGrid=3
	gviIndexRender=4

class gviDataSetType(Enum):
	gviDataSetAny=0
	gviDataSetDbmsTable=1
	gviDataSetObjectClassTable=2
	gviDataSetFeatureClassTable=3

class gviFilterType(Enum):
	gviFilterAttributeOnly=1
	gviFilterWithSpatial=2
	gviFilterWithTemporal=3

class gviConnectionType(Enum):
	gviConnectionUnknown=0
	gviConnectionMySql5x=2
	gviConnectionFireBird2x=3
	gviConnectionOCI11=4
	gviConnectionPg9=5
	gviConnectionMSClient=6
	gviConnectionSQLite3=10
	gviConnectionShapeFile=12
	gviConnectionArcGISServer10=13
	gviConnectionArcSDE9x=14
	gviConnectionArcSDE10x=15
	gviConnectionWFS=16
	gviConnectionKingBase7=17
	gviConnectionCms7Http=101
	gviConnectionCms7Https=102
	gviConnectionPlugin=999

class gviLockType(Enum):
	gviLockSharedSchemaReadonly=0
	gviLockSharedSchema=1
	gviLockExclusiveSchema=2

class gviSpatialRel(Enum):
	gviSpatialRelEnvelope=0
	gviSpatialRelEquals=1
	gviSpatialRelIntersects=2
	gviSpatialRelTouches=3
	gviSpatialRelCrosses=4
	gviSpatialRelWithin=5
	gviSpatialRelContains=6
	gviSpatialRelOverlaps=7

class gviRenderIndexRebuildType(Enum):
	gviRenderIndexRebuildFlagOnly=1
	gviRenderIndexRebuildWithData=2

class gviNetworkAttributeUsageType(Enum):
	gviUseAsCost=0
	gviUseAsDescriptor=1
	gviUseAsRestriction=2
	gviUseAsHierarchy=3

class gviNetworkElementType(Enum):
	gviJunction=1
	gviEdge=2

class gviEvaluatorType(Enum):
	gviConstantEvaluator=0
	gviFieldEvaluator=1
	gviScriptEvaluator=2

class gviEdgeDirection(Enum):
	gviNone=0
	gviAlongDigitized=1
	gviAgainstDigitized=2

class gviNetworkType(Enum):
	gviDirectedNetwork=0
	gviUnDirectedNetwork=1

class gviNetworkElevationModel(Enum):
	gviElevationNone=0
	gviElevationFields=1
	gviZCoordinates=2

class gviNetworkBarrierType(Enum):
	gviJunctionBarrier=1
	gviEdgeBarrier=2

class gviConstraintBarrierType(Enum):
	gviRestriction=0
	gviAddedCost=1

class gviNetworkLocationType(Enum):
	gviLocation=1
	gviEventLocation=2

class gviNetworkLocationOrderPolicy(Enum):
	gviSequence=1
	gviFixStart=2
	gviFixStartAndReturn=3
	gviFixStartEnd=4
	gviFree=5

class gviFdbCapability(Enum):
	gviFdbCapReplicationCheckOutMaster=1
	gviFdbCapQueryResultIndexRange=2
	gviFdbCapModifyField=3
	gviFdbCapAddField=4
	gviFdbCapDeleteField=5
	gviFdbCapModifyData=20

class gviResultStoreLocation(Enum):
	gviResultStoreLocationServer=0
	gviResultStoreLocationClient=1

class gviNameType(Enum):
	gviNameDataSource=0
	gviNameFeatureDataSet=1
	gviNameTable=2
	gviNameObjectClass=3
	gviNameFeatureClass=4
	gviNameFieldInfo=5
	gviNameResource=6
	gviNameIndex=7

class gviReplicateOperation(Enum):
	gviReplicateInitialize=0
	gviReplicateFinished=1
	gviReplicateExtractSchema=2
	gviReplicateExtractData=3
	gviReplicateCreateSchema=4
	gviReplicateReplicateData=5
	gviReplicateCreateSpatialIndex=6
	gviReplicateCreateRenderIndex=7
	gviReplicateCommitTransaction=8
	gviReplicateTruncateDelta=9
	gviReplicateReleaseLock=10
	gviCloseFile=11
	gviWriteFile=12
	gviOpenFile=13
	gviWriteImage=14
	gviWriteModel=15

class gviNetworkJunctionConnectivityPolicy(Enum):
	gviHonor=1
	gviOverride=2

class gviNetworkEdgeConnectivityPolicy(Enum):
	gviAnyVertex=1
	gviEndVertex=2

class gviConflictDetectedType(Enum):
	gviConflictDetectedMaster=1
	gviConflictDetectedSlave=2
	gviConflictDetectedManual=3

class gviReplicationType(Enum):
	gviReplicationCheckOut=0
	gviReplicationCheckIn=1

class gviModelLODType(Enum):
	gviSimpleModel=0
	gviFineModel=1

class gviNetworkSide(Enum):
	gviSideNone=0
	gviSideAlongDigitized=1
	gviSideAgainstDigitized=2

class gviDataConnectionType(Enum):
	gviOgrConnectionUnknown=0
	gviOgrConnectionDWG=1
	gviOgrConnectionShp=-2147483647
	gviOgrConnectionSDE=-2147483646
	gviOgrConnectionOCI=-2147483645
	gviOgrConnectionMS=-2147483644
	gviOgrConnectionPG=-2147483643
	gviOgrConnectionPGEO=-2147483642
	gviOgrConnectionWFS=-2147483641
	gviOgrConnectionFileGDB=-2147483640
	gviOgrConnectionSKP=-2147483639
	gviOgrConnectionLAS=-2147483632
	gviOgrConnectionFBX=-2147483631
	gviOgrConnectionIFC=-2147483628

class gviResourceConflictPolicy(Enum):
	gviResourceIgnore=1
	gviResourceUserExists=2
	gviResourceOverWrite=3
	gviResourceRenameToNew=4

class gviDomainCopyPolicy(Enum):
	gviDomainIgnor=1
	gviDomainCopy=2

class gviRebuildRenderIndexPolicy(Enum):
	gviRebuildNone=1
	gviRebuildOnlyFlag=2
	gviRebuildWithData=3

class gviRasterConnectionType(Enum):
	gviRasterConnectionUnknown=0
	gviRasterConnectionFile=1
	gviRasterConnectionWMS=2
	gviRasterConnectionOCI=3
	gviRasterConnectionWMTS=4
	gviRasterConnectionMapServer=5

class gviGeometryType(Enum):
	gviGeometryUnknown=0
	gviGeometryPoint=1
	gviGeometryModelPoint=2
	gviGeometryPOI=4
	gviGeometryCircularArc=6
	gviGeometryLine=10
	gviGeometryCircle=11
	gviGeometryPolyline=30
	gviGeometryRing=31
	gviGeometryCompoundLine=32
	gviGeometryPolygon=50
	gviGeometryTriMesh=51
	gviGeometryCollection=70
	gviGeometryMultiPoint=71
	gviGeometryMultiPolyline=72
	gviGeometryMultiPolygon=73
	gviGeometryMultiTrimesh=74
	gviGeometryClosedTriMesh=77
	gviGeometryPointCloud=100

class gviGeometryDimension(Enum):
	gviGeometry0Dimension=0
	gviGeometry1Dimension=1
	gviGeometry2Dimension=2
	gviGeometry3Dimension=3
	gviGeometryNoDimension=-1

class gviVertexAttribute(Enum):
	gviVertexAttributeNone=0
	gviVertexAttributeZ=1
	gviVertexAttributeM=2
	gviVertexAttributeZM=3
	gviVertexAttributeID=4
	gviVertexAttributeZID=5
	gviVertexAttributeMID=6
	gviVertexAttributeZMID=7

class gviCoordinateReferenceSystemType(Enum):
	gviCrsProject=1
	gviCrsGeographic=2
	gviCrsVertical=3
	gviCrsTemporal=4
	gviCrsUnknown=5
	gviCrsENU=6

class gviCurveInterpolationType(Enum):
	gviCurveInterpolationLinear=0
	gviCurveInterpolationCircle=1

class gviLocateStatus(Enum):
	gviLocateOutside=0
	gviLocateVertex=1
	gviLocateEdge=2
	gviLocateFacet=3

class gviSurfaceInterpolationType(Enum):
	gviSurfaceInterpolationPlanar=0
	gviSurfaceInterpolationSpherical=1
	gviSurfaceInterpolationElliptical=2
	gviSurfaceInterpolationParametricCurve=3

class gviTerrainAnalyseOperation(Enum):
	gviTerrainGetSurfaceArea=0
	gviTerrainFindWaterSinkBoundary=1
	gviTerrainCalculateCutFill=2

class gviBufferStyle(Enum):
	gviBufferCapround=1
	gviBufferCapbutt=2
	gviBufferCapsquare=3

class gviRoofType(Enum):
	gviRoofFlat=0
	gviRoofHip=1
	gviRoofGable=2

class gviCommandType(Enum):
	gviCommandStart=0
	gviCommandInsert=1
	gviCommandDelete=2
	gviCommandUpdate=3

class gviRenderSystem(Enum):
	gviRenderD3D=0
	gviRenderOpenGL=1

class gviObjectType(Enum):
	gviObjectNone=0
	gviObjectReferencePlane=2
	gviObjectFeatureLayer=256
	gviObjectTerrain=257
	gviObjectRenderModelPoint=258
	gviObjectTerrainRoute=260
	gviObjectRenderPolyline=261
	gviObjectRenderPolygon=262
	gviObjectRenderTriMesh=263
	gviObjectRenderMultiPoint=264
	gviObjectRenderPoint=265
	gviObjectCameraTour=266
	gviObjectMotionPath=267
	gviObjectSkyBox=271
	gviObjectParticleEffect=272
	gviObjectLabel=273
	gviObjectTableLabel=274
	gviObjectSkinnedMesh=275
	gviObjectRenderArrow=276
	gviObjectRenderMultiPolyline=277
	gviObjectRenderMultiPolygon=278
	gviObjectImageryLayer=279
	gviObjectRenderMultiTriMesh=280
	gviObjectTerrainHole=281
	gviObject3DTileLayer=282
	gviObjectTerrainVideo=283
	gviObjectOverlayLabel=284
	gviObjectDynamicObject=286
	gviObjectTerrainModifier=287
	gviObjectRenderPointCloud=288
	gviObjectRenderPOI=289
	gviObjectWalkGround=290
	gviObject3DTileHole=291
	gviObjectTerrainRegularPolygon=293
	gviObjectTerrainCylinder=294
	gviObjectTerrainCone=295
	gviObjectTerrainArrow=296
	gviObjectTerrain3DArrow=297
	gviObjectTerrainLocation=298
	gviObjectTerrainRectangle=299
	gviObjectTerrainBox=300
	gviObjectTerrainPyramid=301
	gviObjectTerrainEllipse=302
	gviObjectTerrainArc=303
	gviObjectTerrainSphere=304
	gviObjectPresentation=305
	gviObjectTerrainImageLabel=306
	gviObjectComplexParticleEffect=307
	gviObjectViewshed=308
	gviObjectHeatMap=309
	gviObjectClipPlaneOperation=310

class gviMeasurementMode(Enum):
	gviMeasureAerialDistance=0
	gviMeasureHorizontalDistance=1
	gviMeasureVerticalDistance=2
	gviMeasureCoordinate=3
	gviMeasureGroundDistance=4
	gviMeasureArea=5
	gviMeasureGroundArea=6
	gviMeasureGroupSightLine=7

class gviClipMode(Enum):
	gviClipCustomePlane=0
	gviClipBox=1

class gviClipPlaneOperation(Enum):
	gviSingleClipOperation=0
	gviBoxClipOperation=1

class gviInteractMode(Enum):
	gviInteractNormal=1
	gviInteractSelect=2
	gviInteractMeasurement=3
	gviInteractEdit=4
	gviInteractWalk=9
	gviInteractDisable=6
	gviInteract2DMap=7
	gviInteractSlide=10
	gviInteractClipPlane=11
	gviInteractFocus=12

class gviEditorType(Enum):
	gviEditorNone=0
	gviEditorMove=1
	gviEditorRotate=2
	gviEditorScale=3
	gviEditorZRotate=4
	gviEditorZScale=5
	gviEditorZMove=6
	gviEditorXYMove=7
	gviEditorBoxScale=8

class gviMouseSelectObjectMask(Enum):
	gviSelectNone=0
	gviSelectFeatureLayer=1
	gviSelectTerrain=2
	gviSelectReferencePlane=8
	gviSelectTerrainHole=16
	gviSelectTileLayer=32
	gviSelectLable=64
	gviSelectParticleEffect=128
	gviSelectRenderGeometry=256
	gviSelectSkinnedMesh=512
	gviSelectTileHole=1024
	gviSelectOverlayLabel=2048
	gviSelectTerrainObject=4096
	gviSelectTerrainVideo=16384
	gviSelectAll=65535

class gviMouseSelectMode(Enum):
	gviMouseSelectClick=1
	gviMouseSelectDrag=2
	gviMouseSelectMove=4
	gviMouseSelectHover=8

class gviSetCameraFlags(Enum):
	gviSetCameraNoFlags=0
	gviSetCameraIgnoreX=1
	gviSetCameraIgnoreY=2
	gviSetCameraIgnoreZ=4
	gviSetCameraIgnorePosition=7
	gviSetCameraIgnoreYaw=8
	gviSetCameraIgnorePitch=16
	gviSetCameraIgnoreRoll=32
	gviSetCameraIgnoreOrientation=56

class gviGetElevationType(Enum):
	gviGetElevationFromDatabase=0
	gviGetElevationFromMemory=1

class gviPivotAlignment(Enum):
	gviPivotAlignBottomLeft=0
	gviPivotAlignBottomCenter=1
	gviPivotAlignBottomRight=2
	gviPivotAlignCenterLeft=3
	gviPivotAlignCenterCenter=4
	gviPivotAlignCenterRight=5
	gviPivotAlignTopLeft=6
	gviPivotAlignTopCenter=7
	gviPivotAlignTopRight=8

class gviDashStyle(Enum):
	gviDashTiny=-1717986919
	gviDashDots=-1431655766
	gviDashSmall=-1010580541
	gviDashMedium=-267390961
	gviDashLarge=-16776961
	gviDashDot=-16678657
	gviDashDotDot=-15978241
	gviDashXLarge=-1044481
	gviDashSolid=-1

class gviMultilineJustification(Enum):
	gviMultilineLeft=0
	gviMultilineCenter=1
	gviMultilineRight=2

class gviCameraTourMode(Enum):
	gviCameraTourLinear=0
	gviCameraTourSmooth=1
	gviCameraTourBounce=2

class gviSimplePointStyle(Enum):
	gviSimplePointCircle=0
	gviSimplePointSquare=1
	gviSimplePointCross=2
	gviSimplePointX=3
	gviSimplePointDiamond=4

class gviViewportMode(Enum):
	gviViewportSinglePerspective=1
	gviViewportStereoAnaglyph=2
	gviViewportStereoQuadbuffer=3
	gviViewportL1R1=4
	gviViewportT1B1=6
	gviViewportL1M1R1=7
	gviViewportT1M1B1=8
	gviViewportL2R1=9
	gviViewportL1R2=10
	gviViewportQuad=11
	gviViewportPIP=12
	gviViewportQuadH=13
	gviViewportStereoDualView=14
	gviViewportL1R1SingleFrustum=15
	gviViewportT1B1SingleFrustum=16

class gviSkyboxImageIndex(Enum):
	gviSkyboxImageFront=0
	gviSkyboxImageBack=1
	gviSkyboxImageLeft=2
	gviSkyboxImageRight=3
	gviSkyboxImageTop=4
	gviSkyboxImageBottom=5

class gviGeoEditType(Enum):
	gviGeoEditCreator=0
	gviGeoEdit3DMove=1
	gviGeoEdit3DRotate=2
	gviGeoEdit3DScale=3
	gviGeoEdit2DMove=4
	gviGeoEditZRotate=5
	gviGeoEditZScale=6
	gviGeoEditVertex=7
	gviGeoEditBoxScale=8

class gviParticleBillboardType(Enum):
	gviParticleBillboardOrientedCamera=0
	gviParticleBillboardOrientedMoveDirection=1

class gviEmitterType(Enum):
	gviEmitterNone=0
	gviEmitterPoint=1
	gviEmitterBox=2
	gviEmitterCircle=3

class gviWeatherType(Enum):
	gviWeatherSunShine=0
	gviWeatherLightRain=1
	gviWeatherModerateRain=2
	gviWeatherHeavyRain=3
	gviWeatherLightSnow=4
	gviWeatherModerateSnow=5
	gviWeatherHeavySnow=6

class gviModKeyMask(Enum):
	gviModKeyShift=3
	gviModKeyCtrl=12
	gviModKeyDblClk=16384

class gviViewportMask(Enum):
	gviViewNone=0
	gviView0=1
	gviView1=2
	gviView2=4
	gviView3=8
	gviViewAllNormalView=15
	gviViewPIP=16

class gviRenderRuleType(Enum):
	gviRenderRuleRange=0
	gviRenderRuleUniqueValues=1

class gviHeightStyle(Enum):
	gviHeightOnTerrain=0
	gviHeightAbsolute=1
	gviHeightRelative=2
	gviHeightOnEverything=3

class gviFogMode(Enum):
	gviFogNone=0
	gviFogExp=1
	gviFogExp2=2
	gviFogLinear=3

class gviRenderType(Enum):
	gviRenderSimple=0
	gviRenderValueMap=1
	gviRenderToolTip=2

class gviRasterSourceType(Enum):
	gviRasterUnknown=0
	gviRasterSourceFile=1
	gviRasterSourceGeoRaster=2
	gviRasterSourceWMS=3
	gviRasterSourceWMTS=4
	gviRasterSourceMapServer=5

class gviGeometrySymbolType(Enum):
	gviGeoSymbolPoint=0
	gviGeoSymbolImagePoint=1
	gviGeoSymbolModelPoint=2
	gviGeoSymbolCurve=3
	gviGeoSymbolSurface=4
	gviGeoSymbol3DPolygon=5
	gviGeoSymbolSolid=6
	gviGeoSymbolPointCloud=7

class gviFlyMode(Enum):
	gviFlyArc=0
	gviFlyLinear=1

class gviActionCode(Enum):
	gviActionFlyTo=0
	gviActionJump=1
	gviActionFollowBehind=2
	gviActionFollowAbove=3
	gviActionFollowBelow=4
	gviActionFollowLeft=5
	gviActionFollowRight=6
	gviActionFollowBehindAndAbove=7
	gviActionFollowCockpit=8

class gviHTMLWindowPosition(Enum):
	gviWinPosUserDefined=0
	gviWinPosCenterParent=1
	gviWinPosCenterDesktop=2
	gviWinPosMousePosition=3
	gviWinPosParentSize=4
	gviWinPosParentRightTop=5

class gviSunCalculateMode(Enum):
	gviSunModeFollowCamera=1
	gviSunModeAccordingToGMT=2
	gviSunModeUserDefined=3

class gviMouseSnapMode(Enum):
	gviMouseSnapDisable=0
	gviMouseSnapVertex=1

class gviArrowType(Enum):
	gviArrowSingle=0
	gviArrowDual=1

class gviCollisionDetectionMode(Enum):
	gviCollisionDisable=0
	gviCollisionOnlyKeyboard=1
	gviCollisionEnable=3

class gviAttributeMask(Enum):
	all=7
	gviAttributeHighlight=1
	gviAttributeCollision=2
	gviAttributeClipPlane=4

class gviRenderControlParameters(Enum):
	gviRenderParamMeasurementLengthUnit=0
	gviRenderParamMeasurementAreaUnit=1
	gviRenderParamLanguage=2
	gviRenderParamLight0Ambient=3
	gviRenderParamLight0Diffuse=4
	gviRenderParamLightModelAmbient=5
	gviRenderParamStereoFusionDistance=6
	gviRenderParamStereoEyeSeparation=7
	gviRenderParamStereoScreenDistance=8
	gviRenderParam3DWindowHeight=9
	gviRenderParam3DWindowWidth=10
	gviRenderParamOcclusionQuery=11
	gviRenderParamOutlineColor=12
	gviRenderParamAlphaTestValue=13
	gviRenderParamClipPlaneLineColor=14

class gviManipulatorMode(Enum):
	gviCityMakerManipulator=0
	gviGoogleEarthManipulator=1

class gviLengthUnit(Enum):
	gviLengthUnitMeter=0
	gviLengthUnitKilometer=1
	gviLengthUnitFoot=2
	gviLengthUnitMile=3
	gviLengthUnitSeaMile=4

class gviAreaUnit(Enum):
	gviAreaUnitSquareMeter=0
	gviAreaUnitSquareKilometer=1
	gviAreaUnitHectare=2
	gviAreaUnitMu=3
	gviAreaUnitQing=4
	gviAreaUnitAcre=5
	gviAreaUnitSquareMile=6

class gviLockMode(Enum):
	gviLockDecal=0
	gviLockAxis=1
	gviLockAxisTextUp=2
	gviAxisAutoPitch=3
	gviAxisAutoPitchTextup=4

class gviDynamicMotionStyle(Enum):
	gviDynamicMotionGroundVehicle=0
	gviDynamicMotionAirplane=1
	gviDynamicMotionHelicopter=2
	gviDynamicMotionHover=3

class gviElevationBehaviorMode(Enum):
	gviElevationBehaviorReplace=0
	gviElevationBehaviorBelow=1
	gviElevationBehaviorAbove=2

class gviDepthTestMode(Enum):
	gviDepthTestEnable=0
	gviDepthTestDisable=1
	gviDepthTestAdvance=2
	gviDepthTestGreaterEqual=3
	gviDepthTestGreater=4
	gviDepthTestLessEqual=5
	gviDepthTestEqual=6
	gviDepthTestNotEqual=7
	gviDepthTestAlways=8
	gviDepthTestAdvanceSecondDrawMaxDepth=1000

class gviWalkMode(Enum):
	gviWalkDisable=0
	gviWalkOnWalkGround=1
	gviWalkOnAll=-1

class gviTerrainActionCode(Enum):
	gviFlyToTerrain=0
	gviJumpToTerrain=1

class gviAltitudeType(Enum):
	gviAltitudeTerrainRelative=0
	gviAltitudePivotRelative=1
	gviAltitudeOnTerrain=2
	gviAltitudeTerrainAbsolute=3

class gviLineToGroundType(Enum):
	gviLineTypeNone=0
	gviLineTypeToGround=1
	gviLineTypeCustom=2

class gviShowTextOptions(Enum):
	gviShowTextAlways=0
	gviShowTextOnHover=1

class gviPresentationPlayMode(Enum):
	gviPresentationPlayAutomatic=0
	gviPresentationPlayManual=1

class gviPresentationPlaySpeed(Enum):
	gviPresentationPlayVerySlow=0
	gviPresentationPlaySlow=1
	gviPresentationPlayNormal=2
	gviPresentationPlayFast=3
	gviPresentationPlayVeryFast=4

class gviPresentationStatus(Enum):
	gviPresentationPlaying=0
	gviPresentationNotPlaying=1
	gviPresentationPaused=2
	gviPresentationWaitingTime=3
	gviPresentationWaitingClick=4
	gviPresentationBeforeSwitchingToAnotherPresentation=5
	gviPresentationAfterSwitchingFromAnotherPresentation=6

class gviPresentationStepContinue(Enum):
	gviPresentationStepContinueMouseClick=0
	gviPresentationStepContinueWait=1

class gviPresentationStepFlightSpeed(Enum):
	gviPresentationStepFlightVerySlow=0
	gviPresentationStepFlightSlow=1
	gviPresentationStepFlightNormal=2
	gviPresentationStepFlightFast=3
	gviPresentationStepFlightVeryFast=4

class gviPresentationSplineSpeedBehavior(Enum):
	gviPresentationSplineSpeedAutomatic=0
	gviPresentationSplineSpeedManualIgnoreSpeedFactor=1
	gviPresentationSplineSpeedManualWithSpeedFactor=2

class gviPresentationStepType(Enum):
	gviPresentationStepTypeLocation=0
	gviPresentationStepTypeDynamicObject=1
	gviPresentationStepTypeGroupOrObject=2
	gviPresentationStepTypeUnderGroundMode=3
	gviPresentationStepTypeTimeSlider=4
	gviPresentationStepTypeSetTime=5
	gviPresentationStepTypeMessage=6
	gviPresentationStepTypeTool=7
	gviPresentationStepTypeCaption=8
	gviPresentationStepTypeRestartDynamicObject=9
	gviPresentationStepTypeFlightSpeedFactor=10
	gviPresentationStepTypePlayTimeAnimation=11
	gviPresentationStepTypePlayAnotherPresentation=12
	gviPresentationStepTypeObjectControl=13
	gviPresentationStepTypeEnvironmentSetting=14
	gviPresentationStepTypeClearCaption=-1

class gviPresentationCaptionPosition(Enum):
	gviPresentationCaptionPositionTopLeft=0
	gviPresentationCaptionPositionTopCenter=1
	gviPresentationCaptionPositionTopRight=2
	gviPresentationCaptionPositionBottomLeft=3
	gviPresentationCaptionPositionBottomCenter=4
	gviPresentationCaptionPositionBottomRight=5

class gviPresentationCaptionSizeType(Enum):
	gviPresentationCaptionSizeTypeFixed=0
	gviPresentationCaptionSizeTypeAutomaticallyAdjust=1

class gviPresentationPlayAlgorithm(Enum):
	gviPresentationPlayAlgorithmFlyTo=0
	gviPresentationPlayAlgorithmSpline=1

class gviComplexParticleEffectType(Enum):
	gviComplexParticleEffectUnknown=0
	gviComplexParticleEffectFire_0=1000
	gviComplexParticleEffectFire_1=1001
	gviComplexParticleEffectFire_2=1002
	gviComplexParticleEffectFire_3=1003
	gviComplexParticleEffectFire_4=1004
	gviComplexParticleEffectSmoke_0=2000
	gviComplexParticleEffectSmoke_1=2001
	gviComplexParticleEffectSmoke_2=2002
	gviComplexParticleEffectExplosion_0=3000
	gviComplexParticleEffectExplosion_1=3001
	gviComplexParticleEffectExplosion_2=3002
	gviComplexParticleEffectExplosion_3=3003
	gviComplexParticleEffectExplosion_4=3004
	gviComplexParticleEffectExplosion_5=3005
	gviComplexParticleEffectExplosion_6=3006
	gviComplexParticleEffectExplosion_7=3007
	gviComplexParticleEffectExplosion_8=3008
	gviComplexParticleEffectRocketTailFlame=9000

class gviMsgChainFlags(Enum):
	gviMsgChainLButtonDown=1
	gviMsgChainLButtonUp=2
	gviMsgChainLButtonDblClk=4
	gviMsgChainMButtonDown=8
	gviMsgChainMButtonUp=16
	gviMsgChainMButtonDblClk=32
	gviMsgChainRButtonDown=64
	gviMsgChainRButtonUp=128
	gviMsgChainRButtonDblClk=256
	gviMsgChainMouseMove=512
	gviMsgChainMouseHover=1024
	gviMsgChainMouseWheel=2048
	gviMsgChainKeyDown=4096
	gviMsgChainKeyUp=8192

class gviUIWindowType(Enum):
	gviUIUnknown=0
	gviUIImageButton=1
	gviUIButton=2

class gviUIEventType(Enum):
	gviUIMouseMove=-17
	gviUIMouseButtonDoubleClick=-16
	gviUIMouseButtonUp=-15
	gviUIMouseButtonDown=-14
	gviUIMouseLeavesArea=-13
	gviUIMouseEntersArea=-12
	gviUIMouseClick=-11
	gviUINone=-1

class gviUIMouseButtonType(Enum):
	gviUILeftButton=0
	gviUIRightButton=1
	gviUIMiddleButton=2
	gviUIX1Button=3
	gviUIX2Button=4
	gviUIMouseButtonCount=5
	gviUINoButton=6

class gviTVDisplayMode(Enum):
	gviTVShowPicture=2
	gviTVShowIcon=4
	gviTVShowEnvelopLines=32
	gviTVShowLinesAndPicture=34
	gviTVShowEnvelopFaces=64
	gviTVShowLinesFacesAndIcon=100
	gviTVShowAll=65535

class gviImageType(Enum):
	gviImageStatic=0
	gviImageDynamic=1
	gviImageCube=2

class gviImageFormat(Enum):
	gviImageUnknown=0
	gviImageDDS=1
	gviImagePNG=2
	gviImageJPG=3
	gviImagePVR=4

class gviTextureWrapMode(Enum):
	gviTextureWrapRepeat=0
	gviTextureWrapClampToEdge=1

class gviCullFaceMode(Enum):
	gviCullNone=0
	gviCullBack=1
	gviCullFront=2

class gviPrimitiveType(Enum):
	gviPrimitiveNormal=0
	gviPrimitiveBillboardZ=1
	gviPrimitiveWater=2
	gviPrimitiveGlass=3
	gviPrimitive3DTree=4
	gviPrimitiveNone=5

class gviPrimitiveMode(Enum):
	gviPrimitiveModeTriangleList=0
	gviPrimitiveModeLineList=1
	gviPrimitiveModePointList=2
	gviPrimitiveModeNone=3

class gviModelType(Enum):
	gviModelStatic=1
	gviModelSkinning=2

class gviPixelFormat(Enum):
	gviPixelUNKNOWN=0
	gviPixelB8G8R8=1
	gviPixelA8R8G8B8=2
	gviPixelDXT1=3
	gviPixelDXT1a=4
	gviPixelDXT3=5
	gviPixelDXT5=6
	gviPixelBGR_PVR2=7
	gviPixelBGR_PVR4=8
	gviPixelARGB_PVR2=9
	gviPixelARGB_PVR4=10
	gviPixelBGR_ATC=11
	gviPixelARGB_ATC_EXPLICIT=12
	gviPixelARGB_ATC_INTERPOLATED=13
	gviPixelBGR8_ETC=14

class gviSetTileLayerRenderParams(Enum):
	GrayShowEnable=0
	GrayShowScalar=1
	IgnoreHole=2
	BrightnessScalar=3
	ContrastScalar=4
	SaturationScalar=5
	DetailScalar=6

class gviConflictResType(Enum):
	gviConflictModelResource=0
	gviConflictImageResource=1

