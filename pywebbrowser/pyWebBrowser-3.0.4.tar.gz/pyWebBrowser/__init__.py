# -*- coding: utf-8 -*-

'''
项目介绍:
开发者  : Yogurt_cry
更新说明: 1. 新增 F12 终止程序
　　　　  2. 整合模块, 调整框架结构, 完善大量的模块及函数使用说明
　　　　  3. 根据 Python 数据类型返回输出结果
　　　　  4. 调整 dll 模块仅支持 x64 位 windows 操作系统
　　　　  5. 修改浏览器默认初始尺寸为 1360 x 768
　　　　  6. 浏览器模块新增刷新 (Refresh)、获取当前网页链接 (Url) 等功能
　　　　  7. 新增浏览器获取页面框架数量、源代码功能
　　　　  8. 修复多处返回值适配 python 数据类型
　　　　  9. 新增元素加载等待
　　　　  10.新增平滑移动可默认初始位置为当前鼠标位置
　　　　  11.新增鼠标相对移动
　　　　  12.新增获取浏览器窗口坐标
　　　　  13.新增主页面鼠标跟随 xpath
　　　　  14.新增主页面输入跟随 xpath
模块说明: 1. Win64Browser.Browser()        浏览器控制
　　　　  2. Win64Browser.Hook()           键盘钩子, MKListen() 启动后检测是否按下 F12, 按下则终止程序
　　　　  3. Win64Browser.MKC()            键盘、鼠标、剪切板、屏幕截图控制合集
'''

from clr import AddReference
from os import path

win64BrowserPath = r'pyWebBrowser/Win64Browser/Win64Browser' # 部署环境
AddReference(win64BrowserPath)

from datetime import datetime
from time import sleep
from json import loads
from lxml import etree
from base64 import b64decode
import math

import Win64Browser
from pyWebBrowser.Browser import Browser
from pyWebBrowser.MKC import MKC

__title__ = 'pyWebBrowser'
__description__ = '基于 C# 开发的浏览器控制工具。整合提供了浏览器控制、键鼠控制、屏幕截图、剪切板控制等常用 API'
__url__ = 'https://gitee.com/Yogurt_cry/pyWebBrowser'
__version__ = '3.0.4'
__build__ = ''
__author__ = 'Yogurt_cry'
__author_email__ = 'ben.2001@foxmail.com'
__license__ = 'MIT License'
__copyright__ = 'CCSDESIGN'