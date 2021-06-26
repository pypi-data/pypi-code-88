from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='CodetagCrawler',
    version='1.0.17',
    packages=[
        'CodetagCrawler'
    ],
    package_data={
        'CodetagCrawler': ['config.yml'],
    },
    include_package_data=True,
    author='Jon Oddvar Rambjør',
    author_email='jonoddram@gmail.com',
    description='''This package provides a click interface to a (Python) codetag crawler, which
    searches through a target directory for codetags, and formats them to a .csv format
    that can be imported to Azure DevOps or other services using equivalent .csv formats.
    A config file is provided to define which codetags to search for. Possible codetags are
    as of now limited by the .yml format, so codetags like !!! or ??? are not supported as is.''',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/jonoddram/CodetagCrawler',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'pyyaml',
        'click'
    ],
    python_requires='>=3.7'
)

