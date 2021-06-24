# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ds_toolbox', 'ds_toolbox.econometrics', 'ds_toolbox.ml']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.5,<2.0.0',
 'pandas>=1.2.3,<2.0.0',
 'pyspark>=3.0.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'scikit-posthocs>=0.6.7,<0.7.0',
 'scipy==1.5.4',
 'statsmodels>=0.12.2,<0.13.0',
 'typeguard>=2.12.0,<3.0.0']

setup_kwargs = {
    'name': 'ds-toolbox',
    'version': '0.2.0',
    'description': 'A ToolBox with daily helpers for the analytical part of a Data Scientist.',
    'long_description': None,
    'author': 'viniciusmsousa',
    'author_email': 'vinisousa04@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/viniciusmsousa/ds-toolbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
