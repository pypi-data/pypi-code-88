# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tiff']

package_data = \
{'': ['*']}

install_requires = \
['geopy>=2.1.0,<3.0.0',
 'numpy>=1.19.5,<2.0.0',
 'pillow>=8.2.0,<9.0.0',
 'pyproj>=3.0.1,<4.0.0',
 'rasterio>=1.2.3,<2.0.0']

setup_kwargs = {
    'name': 'tiff',
    'version': '0.0.10',
    'description': 'GeoTiff utils package',
    'long_description': None,
    'author': 'Moleque',
    'author_email': 'molecada@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
