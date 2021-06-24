#!/usr/bin/env Python
# coding=utf-8
#作者： tony
# encoding = utf-8

import time
from time import sleep

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


'''
打开浏览器
访问URL
等待5s
退出浏览器
'''
browser_url = 'http://192.168.1.68:8888/'
# browser_url ='http://192.168.3.97:8089/'
# browser_url = 'http://192.168.7.105:8089/'
def initUI():
    global driver
    # 谷歌浏览启动配置
    option = webdriver.ChromeOptions()
    # 配置参数 禁止 Chrome 正在受到自动化软件控制
    option.add_argument('disable-infobars')
    # 配置参数禁止data;的出现
    current_user = getuser()
    option.add_argument(r'user-data-dir=C:\python\{}'.format(current_user))
    # option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe' # 手动指定使用的浏览器位置
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=option, executable_path=chrome_path)

    driver.get(browser_url)
    print("start")
    loadfinished = WebDriverWait(driver, 10, poll_frequency=0.5)
    print("loadfinished")
    r = requests.get("http://192.168.1.68:9000/api/connection/Get/" + str(time.time()))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    TokenDate = json.loads(r.text)
    print(str(TokenDate["Server"]) + ":" + str(TokenDate["ControlPort"]) + ":" + str(TokenDate["ViewPort"]) + ":" + str(
        TokenDate["Token"]))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    postData = "pyPostMessage('WEBSDK_INIT_CONF',{param:" + str(
        TokenDate) + ",log:true,widgets:{netWorkerShow:true,logShow:true}})"
    driver.execute_script(postData)
    time.sleep(2)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("finished")
    return TokenDate


   # time.sleep(5)
   # driver.quit()


def init(TokenDate):
    global renderControl
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



def loadSkyBox(g):
    skyboxPath = "E://server//media//skybox"
    g.objectManager.setSkybox(0,skyboxPath,1)

def initCamera(g):
    camera =g.camera
    pos =g.new_Vector3
    ang =g.new_EulerAngle
    pos.set(15215.2, 35411.31, 200)
    ang.heading = 0
    ang.tilt = -20
    camera.lookAt(pos,50, ang)

def loadFDB(g):
    server = "192.168.1.68"
    port = 8040
    database = "SDKDEMO"
    g.loadFDBByService(server, port, database, "", "",True,None,None)

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
        "这是一个什么东西？",
        "#000000",
        15,
        "宋体",
        1,
        1000
        )

def pauseRendering():
    renderControl.pauseRendering(True)# 停止渲染

def resumeRendering():
    renderControl.resumeRendering()# 恢复渲染

def fullScreen():
    fullScreen = await renderControl.fullScreen# 获取全屏状态
    renderControl.fullScreen = fullScreen# 设置全屏状态

def captureScreen():
    exportManager = renderControl.exportManager# 获取出图管理器接口
    exportManager.exportImage('test.png', 2048, 2048, False)#设置出图参数


if __name__ == '__main__':

   TokenDate=initUI()
   # TokenDate = {"Server": "127.0.0.1", "ControlPort": "8181", "Token": ""}
   print("start")
   g = init(TokenDate)
   loadSkyBox(g)
   loadFDB(g)
   initCamera(g)
   g.interactMode = 2
   g.SetInteractMode(2,driver,2)
   g.onMouseClickSelect = fnMouseClickSelect
   print("end")

