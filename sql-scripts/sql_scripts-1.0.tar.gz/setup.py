# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 5:07 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : setup.py.py


# https://www.cnblogs.com/sting2me/p/6550897.html

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sql_scripts",  # 模块名称
    version="1.0",  # 当前版本
    author="lipanpan",  # 作者
    author_email="1299793997@qq.com",  # 作者邮箱
    description="脚本规范",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/wupeiqi/fucker",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        'PyMySQL',
    ],
    python_requires='>=3',
)
