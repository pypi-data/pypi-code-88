#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="conversionwangyp",
    version="0.0.3",
    description="library ",
    long_description="library ",
    author="wangyp",
    author_email="562584614@qq.com",
    url="",
    license="MIT Licence",
    keywords="pytorch onnx util",
    platforms="any",
    python_requires=">=3.6.*",
    package_dir={"": "modelhub"},
    packages=find_packages("modelhub"),
    install_requires=[
        "numpy>=1.16,<2.0",
        "torch>=1.6.0",
        "onnxruntime",
    ],
)
