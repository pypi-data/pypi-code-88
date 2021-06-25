#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='joker_test',
    version='0.0.2',
    author='joker',
    author_email='joker.code@qq.com',
    url='http://www.baidu.com',
    description=u'吃枣药丸',
    packages=['joker_test'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'joker=joker_test:jujube',
            'pill=joker_test:pill'
        ]
    }
)