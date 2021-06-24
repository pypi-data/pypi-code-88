# -*- coding: utf-8 -*-
import setuptools
#env.yaml文件使得直接新建环境并安装，这个文件则是只安装pyqt5-gui-yyj

with open("README.md","r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
  name="pyqt5_gui_yyj",
  install_requires=[
       'pyqt5==5.15.4', 
       'pyqt5-tools==5.15.4.3.2', 
       'pyqtgraph==0.12.1',
       'twine==3.4.1'
  ],
  version="0.0.14",
  author="YangYijian",
  author_email="2715336141@qq.com",
  description="A developing pyqt gui, change __init__.py",
  long_description='long_description',
  long_description_content_type="text/markdown",
  url="https://gitee.com/yangyijian1202/PyQt5_GUI",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)