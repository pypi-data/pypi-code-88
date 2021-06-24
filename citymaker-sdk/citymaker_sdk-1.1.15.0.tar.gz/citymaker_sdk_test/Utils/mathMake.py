#!/usr/bin/env Python
# coding=utf-8
#作者： tony
#* 所有类中能通过自身方法改变自身属性的方法名
# * 以下方法名调用时同时调用getObject方法获取自身属性值并更新
needGetObject=[
  "expandByEnvelope",
  "expandByVector",
  "setByEnvelope",
  "set",
  "setByEulerAngle",
  "normalize",
  "setByVector",
  "multiplyByScalar",
  "setCoords",
  "compose",
  "compose2",
  "decompose2",
  "interpolatePosition",
  "inverse",
  "makeIdentity",
  "multiplyVector",
  "setByMatrix",
  "setRotation",
  "setScale",
  "setTranslate",
  "addPointAfter",
  "addPointBefore",
  "addSegmentAfter",
  "addSegmentBefore",
  "addWaypoint",
  "appendPoint",
  "appendSegment",
  "removePoints",
  "removeSegments",
  "updatePoint",
  "updateSegment",
  "addGeometry"
]
