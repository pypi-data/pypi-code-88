#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import os, sys,types,json
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils.Config import Config
from Utils.RenderViewer3D import RenderViewer3D

import asyncio

renderControl =None
objectManager=None
async def initAxControl():
    config =Config()
    config.renderAddress = "http://124.193.151.47:8081"
    root ="renderControl"
    renderViewer3D=RenderViewer3D()
    confi=await renderViewer3D.setConfig(root, config)
    renderControl =renderViewer3D.getRenderControl()
    renderControl.interactMode = 1
    objectManager = await renderControl.objectManager
    return renderControl

async def loadSkyBox(renderControl):
    skyboxPath = "D://skybox"
    await objectManager.setSkybox(0,skyboxPath,1)


async def initCamera(renderControl):
    camera =await renderControl.camera
    pos =await renderControl.new_Vector3
    ang =await renderControl.new_EulerAngle
    pos.set(15415.2, 35211.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos, 600, ang)

async def loadFDB(renderControl):
    server = "124.193.151.44"
    port = 8040
    database = "SDKDEMO"
    await renderControl.loadFDBByService(server, port, database, "", "")

async def loadCep(renderControl):#---------------------------------------------加载CEP
    cepPath = "D:/cep/Package_乾隆花园/乾隆花园.cep"
    project = renderControl.project
    project.open(cepPath, False, "")
    camera = renderControl.camera
    camera.flyTime = 1

async def fnMouseClickSelect(pickResult,intersectPoint,mask,eventSender):
    position =await intersectPoint.position
        # if (!renderControl) {
        #   alert("renderControl未初始化完成!");
        #   return;
        # }
    label =await objectManager.createLabel(
        {"x": position.x, "y": position.y,"z": position.z },
        "标签123",
        "#000000",
        15,
        "宋体",
        1,
        1000
        )


async def main():
    g=await initAxControl()
    await loadSkyBox(g)
    await initCamera(g)
    await loadFDB(g)
    g.interactMode = 2
    g.onMouseClickSelect = fnMouseClickSelect
    # time.sleep(4)
    # loadCep(g)

asyncio.get_event_loop().run_until_complete(main())