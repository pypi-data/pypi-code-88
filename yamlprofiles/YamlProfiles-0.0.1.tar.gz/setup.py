# coding=utf8
# @Created : 2021/6/24 1:35 下午
# @Author  : yunfound@outlook.com

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='YamlProfiles',
    version='0.0.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['yamlprofiles'],
    author='liuyunfeng',
    author_email='yunfound@outlook.com',
    install_requires=['PyYAML==5.4.1'],
    python_requires='>3.6',
    url='https://www.obatu.com',
    project_urls={
        'Source Code': 'https://github.com/yunfong/yaml.profiles'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
