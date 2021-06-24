# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['conversortemperatura']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'conversortemperatura',
    'version': '1.0',
    'description': 'Paquete que convierte temperatura de Celcius a Farenheit y Rankine  y De Farenheit a Rankine',
    'long_description': None,
    'author': 'Ramiro Israel Vivanco Gualan',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
