# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resistics_readers',
 'resistics_readers.lemi',
 'resistics_readers.metronix',
 'resistics_readers.miniseed',
 'resistics_readers.phoenix',
 'resistics_readers.spam']

package_data = \
{'': ['*']}

install_requires = \
['defusedxml>=0.7.1,<0.8.0',
 'loguru>=0.5.3,<0.6.0',
 'numpy>=1.20.3,<2.0.0',
 'obspy>=1.2.2,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'resistics==1.0.0a3']

setup_kwargs = {
    'name': 'resistics-readers',
    'version': '0.1.3',
    'description': 'Package with various instrument data format readers for resistics',
    'long_description': '## Welcome\n\n[![PyPI](https://img.shields.io/pypi/v/resistics-readers)](https://pypi.org/project/resistics-readers/)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/resistics-readers)](https://pypi.org/project/resistics-readers/)\n[![Documentation Status](https://readthedocs.org/projects/resistics-readers/badge/?version=latest)](https://resistics-readers.readthedocs.io/en/latest/?badge=latest)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/resistics/resistics-readers.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/resistics/resistics-readers/context:python)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nResistics readers is an extension to resistics adding support for various\ninstrument data formats.\n\nMore coming soon...\n',
    'author': 'Neeraj Shah',
    'author_email': 'resistics@outlook.com',
    'maintainer': 'Neeraj Shah',
    'maintainer_email': 'resistics@outlook.com',
    'url': 'https://github.com/resistics/resistics-readers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.10',
}


setup(**setup_kwargs)
