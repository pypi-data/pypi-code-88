# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysigmap']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysigmap',
    'version': '0.1.8',
    'description': 'Application software for calculating the preconsolidation pressure from the incremental loading oedometer testing',
    'long_description': None,
    'author': 'E. A. Montoya-Araque, A. J. Aparicio-Ortube, D. G. Zapata-Medina and L. G. Arboleda-Monsalve',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
