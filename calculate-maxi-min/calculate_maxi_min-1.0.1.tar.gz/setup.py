# -*- encoding: utf-8 -*-
# @created_at: 2021/6/23 10:55
from setuptools import setup
import setuptools
setup(
    name='calculate_maxi_min',# 需要打包的名字,即本模块要发布的名字
    version='v1.0.1',#版本
    description='计算最大最小值', # 简要描述
    py_modules=['rongjilv'],   #  需要打包的模块
    author='jkp', # 作者名
    author_email='1543889217@qq.com',   # 作者邮件
    url='https://gitee.com/jia_kai_peng/calcalute', # 项目地址,一般是代码托管的网站
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)