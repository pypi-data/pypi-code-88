# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))

setup(
    name='zbzdata',      # 包的名字
    author='ysteq',       # 作者
    version='1.0.0',      # 版本号
    license='MIT',

    description='project describe',     # 描述
    long_description='''long description''',
    author_email='xing.lu@ysteq.com',  # 你的邮箱**
    url='http://www.ysteq.com/',       # 可以写github上的地址，或者其他地址
    packages=["zbzdata"],
    # 依赖包
    install_requires=[
        'requests >= 2.19.1',
        "lxml >= 3.7.1",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',       # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)