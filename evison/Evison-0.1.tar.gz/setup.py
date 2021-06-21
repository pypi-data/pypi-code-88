# coding: utf-8
import setuptools
from setuptools import setup

setup(
    name='Evison',# 需要打包的名字,即本模块要发布的名字
    version='v0.1',#版本
    description='We provide an easy way for visualizing', # 简要描述
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    author='Jinhong Lin', # 作者名
    author_email='jonneslin@gmail.com',   # 作者邮件
    url='https://github.com/JonnesLin/easy_visualization', # 项目地址,一般是代码托管的网站
    requires=['torchvision', 'numpy', 'matplotlib', 'torch'], # 依赖包,如果没有,可以不要
    license='MIT'
)