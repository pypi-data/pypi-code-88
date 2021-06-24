#!/usr/bin/env Python
# coding=utf-8
# 作者： tony
from cefpython3 import cefpython as cef

from tkinter import *
import threading
import sys
import requests
import json
import time
import requests
import json
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from getpass import getuser
import datetime
import os, sys,types,json
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.Config import Config
from Utils.RenderViewer3D import RenderViewer3D
from CityMaker_Enum import *

def load(browser):
    init()
    loadSkyBox()
    loadFDB()
    initCamera()
    renderControl.interactMode = 2
    # postData = "pyPostMessage('WEBSDK_INIT_CONF',{param:'',log:true,widgets:{netWorkerShow:true,logShow:true}})"
    # aa = browser.ExecuteJavascript(postData)
    renderControl.SetInteractMode(1,browser,2)
    renderControl.onMouseClickSelect = fnMouseClickSelect
    print("end")

class LifespanHandler(object):
    def __init__(self, para):  # name就是实例变量
        self.para = para
    def OnLoadEnd(self, browser, **_):
        # Execute function with a delay of 1 second after page
        # has completed loading.
        print("Page loading is complete")
        cef.PostDelayedTask(cef.TID_UI, 1000, load, browser)

        postData = "pyPostMessage('WEBSDK_INIT_CONF',{param:" + str(
            self.para) + ",log:true,widgets:{netWorkerShow:true,logShow:true}})"
        aa=browser.ExecuteJavascript(postData)
        print(str(self.para))
        print(time.time())

browser_url = 'http://192.168.1.68:8888/'
# browser_url ='http://192.168.3.97:8089/'


# cefpython3 目前只支持python3.7，高版本Python不兼容
def embed_browser_thread(frame, _rect,msg):
    sys.excepthook = cef.ExceptHook
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), _rect)
    cef.Initialize()
    browser = cef.CreateBrowserSync(window_info, url=browser_url)
    browser.SetClientHandler(LifespanHandler(msg))
    cef.MessageLoop()

def initUI():
    global  TokenDate,root
    r = requests.get("http://192.168.1.68:9000/api/connection/Get/" + str(time.time()))
    TokenDate = json.loads(r.text)
    print(str(TokenDate["Server"]) + ":" + str(TokenDate["ControlPort"]) + ":" + str(TokenDate["ViewPort"]) + ":" + str(TokenDate["Token"]))
    root = Tk()
    root.geometry("1024x900")

    frame1 = Frame(root, bg='white', height=700)
    frame1.pack(side=TOP, fill=X)

    frame2 = Frame(root, bg='white', height=200)
    frame2.pack(side=TOP, fill=X)

    rect = [0, 0, 1024, 700]
    thread = threading.Thread(target=embed_browser_thread, args=(frame1, rect, TokenDate))
    thread.start()
    root.mainloop()


def init():
    global  renderControl
    config=Config()
    config.renderAddress = browser_url
    # config.renderAddress = 'http://192.168.1.68:8888/'
    # config.serverAddress = "ws://127.0.0.1:8181"
    # config.serverAddress1 ="ws://127.0.0.1:8181"
    config.serverAddress = "ws://"+str(TokenDate["Server"])+":"+str(TokenDate["ControlPort"])+"?mode=0"
    config.token=str(TokenDate["Token"])
    root = "renderControl"
    renderViewer3D=RenderViewer3D()
    renderViewer3D.setConfig(root,config)
    renderControl= renderViewer3D.getRenderControl()
    return renderControl



def loadSkyBox( ):
    skyboxPath ="E://server//media//skybox"
    renderControl.objectManager.setSkybox(0,skyboxPath,1)

def initCamera( ):
    camera =renderControl.camera
    pos =renderControl.new_Vector3
    ang =renderControl.new_EulerAngle
    pos.set(15215.2, 35411.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos,50, ang)

def loadFDB( ):
    server = "192.168.1.68"
    port = 8040
    database = "SDKDEMO"
    renderControl.loadFDBByService(server, port, database, "", "",True,None,None)
    # renderControl.loadFDBByService(server, port, database, "", "")

def loadCep( ):#---------------------------------------------加载CEP
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


if __name__ == '__main__':
    initUI()

    print("end")
