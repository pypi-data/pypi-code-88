# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drawsbml']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.5.1,<3.0.0',
 'pydot>=1.4.2,<2.0.0',
 'python-libsbml>=5.19.0,<6.0.0']

entry_points = \
{'console_scripts': ['drawsbml = drawsbml.__main__:main']}

setup_kwargs = {
    'name': 'drawsbml',
    'version': '0.1.2',
    'description': 'Draw Signalling Pathways (SBML) using graphviz',
    'long_description': None,
    'author': 'Dilawar Singh',
    'author_email': 'dilawar.s.rajput@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
