#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import os, sys,types,json
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.Config import Config
from Utils.RenderViewer3D import RenderViewer3D
from CityMaker_Enum import *
# import Utils.globalvar as glovar

def init():
    global objectManager,renderControl,geometryFactory,currentGeometry
    config=Config()
    config.renderAddress = "http://124.193.151.47:8081"
    config.serverAddress = "ws://127.0.0.1:8181/"
    config.clientdir = "D:\\bin\\WebSocket3Server.bat"
    root = "renderControl"
    renderViewer3D=RenderViewer3D()
    renderViewer3D.setConfig(root,config)
    renderControl= renderViewer3D.getRenderControl()

    objectManager = renderControl.objectManager
    objectManager = renderControl.objectManager
    geometryFactory = renderControl.geometryFactory

    return renderControl




def loadSkyBox(g):
    skyboxPath = "D://bin//skybox"
    g.objectManager.setSkybox(0,skyboxPath,1)

def initCamera(g):
    camera =g.camera
    pos =g.new_Vector3
    ang =g.new_EulerAngle
    pos.set(15415.2, 35211.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos, 600, ang)

def loadFDB(g):
    server = "124.193.151.44"
    port = 8040
    database = "SDKDEMO"
    g.loadFDBByService(server, port, database, "", "")

def loadCep(g):#---------------------------------------------加载CEP
    cepPath = "D:/cep/Package_乾隆花园/乾隆花园.cep"
    project =g.project
    project.open(cepPath, False, "")
    camera =g.camera
    camera.flyTime = 1

# @eventfun
def fnMouseClickSelect(pickResult,intersectPoint,mask,eventSender):
    position = intersectPoint.position

    # g1= glovar.getRenderControl()
    label =g.objectManager.createLabel(
        {"x": position.x, "y": position.y,"z": position.z },
        "标签123",
        "#000000",
        15,
        "宋体",
        1,
        1000
        )
    g.onMouseClickSelect =None

def onObjectEditing(geometry):
    currentGeometry = geometry
    # print("this is onObjectEditing")

def onObjectEditFinish():
    print("onObjectEditFinish")
    multipolygon =g.geometryFactory.createGeometry(gviGeometryType.gviGeometryMultiPolygon,
                                                        gviVertexAttribute.gviVertexAttributeZ)
    b = multipolygon.addGeometry(currentGeometry)
    # console.log("addGeometry", b);
    # console.log("mu", multipolygon);
    # tilePath = "D:\\Media\\sdk.tdbx"
    tilePath = "http:123@192.168.1.66:8040"
    test3DTileLayer = g.objectManager.create3DTileLayer(tilePath, "", g.guid)
    test3DTileLayer.setHoles(multipolygon)
    print("onObjectEditFinish------------")


if __name__ == '__main__':
    # aa=c.check_exsit("WebSocket3Dserver.exe")
    # print(aa)
    g=init()
    loadSkyBox(g)
    loadFDB(g)
    initCamera(g)
    g.interactMode = 2
    # g.onMouseClickSelect = fnMouseClickSelect
    print("event onObjectEditing")
    g.onObjectEditing = onObjectEditing
    print("event onObjectEditFinish")
    g.onObjectEditFinish = onObjectEditFinish
    print("event edn")
    g.interactMode = 4
    objectEditor =g.objectEditor
    surfaceSymbol = g.new_SurfaceSymbol
    surfaceSymbol.color = 0x770000FF
    currentGeometry = g.geometryFactory.createGeometry(gviGeometryType.gviGeometryPolygon,gviVertexAttribute.gviVertexAttributeZ)
    currentRenderGeometry = g.objectManager.createRenderPolygon(currentGeometry, surfaceSymbol,g.guid)
    currentRenderGeometry.heightStyle = gviHeightStyle.gviHeightOnEverything
    objectEditor.startEditRenderGeometry(currentRenderGeometry, gviGeoEditType.gviGeoEditCreator)
    print("end")
    # loadFDB(g)
    # initCamera(g)
    # g.interactMode = 3
    # time.sleep(4)
    # loadCep(g)
    # g.interactMode = 2