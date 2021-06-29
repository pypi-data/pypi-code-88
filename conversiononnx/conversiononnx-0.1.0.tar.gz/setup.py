#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="conversiononnx",
    version="0.1.0",
    description="library ",
    long_description="library ",
    author="wangyp",
    author_email="562584614@qq.com",
    url="",
    license="MIT Licence",
    keywords="pytorch onnx util",
    platforms="any",
    python_requires=">=3.6.*",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "numpy>=1.16,<2.0",
        "torch>=1.6.0",
        "onnxruntime",
    ],
)
