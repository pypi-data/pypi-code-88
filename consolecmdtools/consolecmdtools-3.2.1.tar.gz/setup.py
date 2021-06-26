# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['consolecmdtools']
install_requires = \
['Pillow', 'consoleiotools']

setup_kwargs = {
    'name': 'consolecmdtools',
    'version': '3.2.1',
    'description': 'Some console tools for console command uses',
    'long_description': None,
    'author': 'Kyan',
    'author_email': 'kai@kyan001.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
