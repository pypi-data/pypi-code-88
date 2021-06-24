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
    global renderControl
    config=Config()
    config.renderAddress = 'http://192.168.3.97:8089/'
    # config.renderAddress = 'http://192.168.1.68:8888/'
    config.serverAddress = "ws://127.0.0.1:8181"
    # config.serverAddress = "ws://192.168.1.68:18900?mode=0"
    # config.serverAddress1 = "ws://192.168.1.68:18900?mode=2"
    config.token='mnMuElXrCdaMkqkVZsiNZUiTqtjNuzWh'
    root = "renderControl"
    renderViewer3D=RenderViewer3D()
    renderViewer3D.setConfig(root,config)
    renderControl= renderViewer3D.getRenderControl()
    return renderControl



def loadSkyBox():
    skyboxPath = "D://bin//skybox"
    renderControl.objectManager.setSkybox(0,skyboxPath,1)

def initCamera():
    camera =renderControl.camera
    pos =renderControl.new_Vector3
    ang =renderControl.new_EulerAngle
    pos.set(15215.2, 35411.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos,50, ang)

def loadFDB():
    server = "192.168.1.68"
    port = 8040
    database = "SDKDEMO"
    renderControl.loadFDBByService(server, port, database, "", "")

def loadCep():#---------------------------------------------加载CEP
    cepPath = "D:/cep/Package_乾隆花园/乾隆花园.cep"
    project =renderControl.project
    project.open(cepPath, False, "")
    camera =renderControl.camera
    camera.flyTime = 1

# @eventfun
def fnMouseClickSelect(pickResult,intersectPoint,mask,eventSender):
    position = intersectPoint.position

    # g1= glovar.getRenderControl()
    label =renderControl.objectManager.createLabel(
        {"x": position.x, "y": position.y,"z": position.z },
        "标签123",
        "#000000",
        15,
        "宋体",
        1,
        1000
        )
    # g.onMouseClickSelect =None

if __name__ == '__main__':
    # aa=c.check_exsit("WebSocket3Dserver.exe")
    # print(aa)
    init()
    loadSkyBox()
    loadFDB()
    initCamera()
    renderControl.interactMode = 2
    renderControl.onMouseClickSelect = fnMouseClickSelect
    print("end")
    # loadFDB(g)
    # initCamera(g)
    # g.interactMode = 3
    # time.sleep(4)
    # loadCep(g)
    # g.interactMode = 2