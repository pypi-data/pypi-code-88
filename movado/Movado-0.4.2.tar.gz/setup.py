# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['movado']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19,<2.0',
 'plotly>=4.14.3,<5.0.0',
 'pygmo>=2.16.1,<3.0.0',
 'river>=0.7.0,<0.8.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'scipy>=1.5.4,<2.0.0',
 'vowpalwabbit>=8.9.0,<9.0.0']

setup_kwargs = {
    'name': 'movado',
    'version': '0.4.2',
    'description': 'Approximation utility for expensive fitness functions',
    'long_description': None,
    'author': 'Daniele Paletti',
    'author_email': 'danielepaletti98@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
