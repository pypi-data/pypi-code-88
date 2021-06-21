# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['grammar']
install_requires = \
['colorama>=0.4.4,<0.5.0',
 'httpx>=0.18.1,<0.19.0',
 'pydantic>=1.8.2,<2.0.0',
 'pytz>=2021.1,<2022.0',
 'structlog>=21.1.0,<22.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['communauto = communauto:main']}

setup_kwargs = {
    'name': 'communauto',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Hadrien David',
    'author_email': 'hadrien@ectobal.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
