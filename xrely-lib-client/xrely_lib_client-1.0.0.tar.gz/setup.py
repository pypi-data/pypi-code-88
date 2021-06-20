# coding: utf-8

"""
    xrely

    API Documentation for xrely platform. For more information please visit https://www.xrely.com.

    OpenAPI spec version: 1.0.0
    Contact: info@xrely.com
    
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "xrely_lib_client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="client library for xrely platform.",
    author_email="info@xrely.com",
    url="https://www.xrely.com",
    keywords=["Web search intelligence","Autocrawl search","Intelligent search engine","install site search","Autocomplete search solution","Autocrawl Search","Search discovery"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    client library for xrely platform. For more information please visit https://www.xrely.com
    """
)
