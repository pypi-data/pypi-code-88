# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['schism']
setup_kwargs = {
    'name': 'schism',
    'version': '0.1.0',
    'description': 'Schism will be a microservices framework designed to keep everything dead simple.',
    'long_description': '## Schism\n\n**COMING SOON!!!**\n',
    'author': 'Zech Zimmerman',
    'author_email': 'hi@zech.codes',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
