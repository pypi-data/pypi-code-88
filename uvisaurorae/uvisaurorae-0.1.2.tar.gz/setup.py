# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uvisaurorae', 'uvisaurorae.resources']

package_data = \
{'': ['*'],
 'uvisaurorae.resources': ['calibration_files/*',
                           'calibration_files/UVIS_flat-field_modifiers_2016-01-13/*']}

install_requires = \
['Shapely>=1.7.1,<2.0.0',
 'astropy>=4.2.1,<5.0.0',
 'importlib-resources>=5.1.2,<6.0.0',
 'matplotlib>=3.4.1,<4.0.0',
 'numpy>=1.20.2,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'scipy>=1.6.3,<2.0.0',
 'spiceypy>=4.0.0,<5.0.0',
 'tqdm>=4.60.0,<5.0.0']

setup_kwargs = {
    'name': 'uvisaurorae',
    'version': '0.1.2',
    'description': 'A library for projecting Cassini-UVIS auroral imagery',
    'long_description': None,
    'author': 'Alexander Bader',
    'author_email': 'lxbader@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
