#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Update	: anyongjin 2021/06/10
# @Link    : https://github.com/anyongjin/pylsd2
# @Version : 0.0.2

from setuptools import setup

setup(
    name='pylid2',
    version='0.0.5',
    description='pylisd is line ',
    author='Gefu Tang, anyongjin',
    author_email='a@163.com',
    license='BSD',
    keywords="LSD",
    packages=['pylid2', 'pylid2.bindings','pylid2.lib'],
    package_dir={'pylid2.lib': 'pylid2/lib'},
    package_data={'pylid2.lib': ['darwin/*.dylib','linux/*.so']},
)
