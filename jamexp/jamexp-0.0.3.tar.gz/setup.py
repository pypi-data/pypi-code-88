# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jexp', 'jexp.cli', 'jexp.hyd', 'jexp.utils', 'jexp.wandb_clean']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.17,<4.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'black>=21.5b1,<22.0',
 'hydra-core>=1.0.6,<2.0.0',
 'isort>=5.8.0,<6.0.0',
 'loguru>=0.5.3,<0.6.0',
 'numpy>=1.20.3,<2.0.0',
 'pre-commit>=2.13.0,<3.0.0',
 'pyfzf>=0.2.2,<0.3.0',
 'pylint>=2.8.3,<3.0.0',
 'scipy>=1.6.3,<2.0.0',
 'typer>=0.3.2,<0.4.0',
 'wandb>=0.10.30,<0.11.0']

entry_points = \
{'console_scripts': ['jhydc = jexp.cli.jhyd_clean:main',
                     'jpin = jexp.cli.jpin:main',
                     'jstar = jexp.cli.star_file:main',
                     'jwdc = jexp.cli.jwb_clean:main']}

setup_kwargs = {
    'name': 'jamexp',
    'version': '0.0.3',
    'description': 'Jam Experiment helper',
    'long_description': None,
    'author': 'Qinsheng',
    'author_email': 'qsh.zh27@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
