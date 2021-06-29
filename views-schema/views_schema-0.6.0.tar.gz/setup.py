# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['views_schema']
install_requires = \
['pydantic>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'views-schema',
    'version': '0.6.0',
    'description': 'A package containing pydantic models used throughout ViEWS 3 for communication between services',
    'long_description': None,
    'author': 'peder2911',
    'author_email': 'pglandsverk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
