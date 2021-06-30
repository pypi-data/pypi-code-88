# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rrunner',
 'rrunner.builtin',
 'rrunner.common',
 'rrunner.ext',
 'rrunner.ext.har2case',
 'rrunner.ext.locust',
 'rrunner.ext.uploader']

package_data = \
{'': ['*'], 'rrunner': ['config/*']}

install_requires = \
['black>=19.10b0,<20.0',
 'jinja2>=2.10.3,<3.0.0',
 'jmespath>=0.9.5,<0.10.0',
 'loguru>=0.4.1,<0.5.0',
 'pydantic>=1.4,<2.0',
 'pytest-html>=2.1.1,<3.0.0',
 'pytest>=5.4.2,<6.0.0',
 'pyyaml>=5.1.2,<6.0.0',
 'requests>=2.22.0,<3.0.0',
 'sentry-sdk>=0.14.4,<0.15.0']

extras_require = \
{'allure': ['allure-pytest>=2.8.16,<3.0.0'],
 'locust': ['locust>=1.0.3,<2.0.0'],
 'upload': ['requests-toolbelt>=0.9.1,<0.10.0', 'filetype>=1.0.7,<2.0.0']}

entry_points = \
{'console_scripts': ['locusts = rrunner.ext.locust:main_locusts',
                     'rmake = rrunner.cli:main_make_alias',
                     'rrun = rrunner.cli:main_hrun_alias',
                     'rrunner = rrunner.cli:main']}

setup_kwargs = {
    'name': 'rrunner',
    'version': '0.0.1',
    'description': 'One-stop solution for HTTP(S) testing.',
    'long_description': '\n# Rrunner\n\n\n\n\n',
    'author': 'jgang.c',
    'author_email': 'jgang.c@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jigangc/rrunner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
