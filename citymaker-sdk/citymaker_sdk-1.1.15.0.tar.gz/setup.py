#!/usr/bin/env Python
# coding=utf-8
#作者： tony
from setuptools import setup,find_packages

setup(
    name="citymaker_sdk",
    version="1.1.15.0",
    #package_dir = {'':'citymaker_sdk'},
    #packages=find_packages("citymaker_sdk"),
    packages=find_packages(),
    description="this is CityMaker_SDK for python",
    long_description="",
    author="Gvitech",
    author_email="zhoutongit@163.com",
    platforms="windows",#程序适用的团建平台列表
    classifiers="",#程序的所属分类列表
    keywords="3D 三维 伟景行 Citymaker",#程序的关键字
    py_modules="",#需要打包的目录列表
    download_url="",#程序的下载地址
    scripts=[],#安装时需要执行的脚本列表
    install_requires = ['websockets>=8.1','websocket-client>=0.15.0'],#依赖包及版本号
    license="""Copyright (c) 2020 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""",
    python_requires='>=3.7',
    url="https://gitee.com/zhoutongit/CityMaker_PySDK"#程序的官网地址


)