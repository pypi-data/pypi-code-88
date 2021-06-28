# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libss', 'libss.separation']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.2,<4.0.0',
 'museval>=0.4.0,<0.5.0',
 'numpy>=1.20.3,<2.0.0',
 'pytest>=6.2.4,<7.0.0']

setup_kwargs = {
    'name': 'libss',
    'version': '0.1.0',
    'description': 'Independent-component-analysis-based Blind audio source separation library.',
    'long_description': '# libss\nIndependent-component-analysis-based blind audio source separation library.\n\n## Installation\n```\npip install libss\n```\n\n## Available algorithms\n- [Auxiliary-function-based independent vector analysis (AuxIVA)](https://doi.org/10.1109/ASPAA.2011.6082320)\n\n### Coming soon...\n- [Online AuxIVA](https://doi.org/10.1109/HSCMA.2014.6843261)\n- [Independent low-rank matrix analysis (ILRMA)](https://doi.org/10.1109/TASLP.2016.2577880)\n- [Fast multichannel nonnegative matrix factorization (FastMNMF)](https://doi.org/10.23919/EUSIPCO.2019.8902557)\n\n## Example\n- [AuxIVA](examples/auxiva.py)\n',
    'author': 'Taishi Nakashima',
    'author_email': 'taishi@ieee.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/taishi-n/bliss',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
