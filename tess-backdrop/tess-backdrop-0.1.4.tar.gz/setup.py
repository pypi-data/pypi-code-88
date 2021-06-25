# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tess_backdrop']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.2.1,<5.0.0',
 'fbpca>=1.0,<2.0',
 'fitsio>=1.1.4,<2.0.0',
 'lightkurve>=2.0.9,<3.0.0',
 'matplotlib>=3.4.1,<4.0.0',
 'mkdocs-jupyter>=0.17.3,<0.18.0',
 'mkdocs-material>=7.1.3,<8.0.0',
 'mkdocs>=1.1.2,<2.0.0',
 'mkdocstrings>=0.15.0,<0.16.0',
 'scipy>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'tess-backdrop',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'Christina Hedges',
    'author_email': 'christina.l.hedges@nasa.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
