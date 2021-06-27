#!/usr/bin/env python
# coding: utf-8

import setuptools

setuptools.setup(
    name="zgtoolkit",
    version="0.0.22",
    author="zg",
    author_email="1480640365@qq.com",
    description=u"张港自用数据处理脚本",
    packages=setuptools.find_packages('.'),
    python_requires=">=3.6",
    install_requires=['matplotlib', 'numpy', 'terminaltables', 'opencv-python',
                      'albumentations',
                      'bbox-visualizer']
)
