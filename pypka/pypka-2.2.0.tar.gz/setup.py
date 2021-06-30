# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypka',
 'pypka.CHARMM36m',
 'pypka.G54A7',
 'pypka.clean',
 'pypka.clean.pdb2pqr',
 'pypka.clean.pdb2pqr.conf_avg',
 'pypka.clean.pdb2pqr.extensions',
 'pypka.clean.pdb2pqr.src',
 'pypka.delphi4py',
 'pypka.delphi4py.example',
 'pypka.delphi4py.readFiles',
 'pypka.delphi4py.rundelphi',
 'pypka.mc']

package_data = \
{'': ['*'],
 'pypka.CHARMM36m': ['sts/*'],
 'pypka.G54A7': ['sts/*', 'sts_cphmd/*', 'sts_old/*'],
 'pypka.clean.pdb2pqr': ['dat/*', 'tools/*']}

install_requires = \
['numpy', 'psutil']

setup_kwargs = {
    'name': 'pypka',
    'version': '2.2.0',
    'description': 'A python module for flexible Poisson-Boltzmann based pKa calculations with proton tautomerism',
    'long_description': '[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mms-fcul/PypKa/blob/master/pypka/example/notebook/pypka.ipynb) [![CircleCI](https://circleci.com/gh/mms-fcul/PypKa.svg?style=svg)](https://circleci.com/gh/mms-fcul/PypKa) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/59a058e4bf0846f18d9d1f6b16a4a0e5)](https://www.codacy.com/gh/mms-fcul/PypKa/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mms-fcul/PypKa&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/77db3bc226c94625acd3cea0e14c23ad)](https://www.codacy.com/app/pedrishi/PypKa?utm_source=github.com&utm_medium=referral&utm_content=mms-fcul/PypKa&utm_campaign=Badge_Coverage) [![Documentation Status](https://readthedocs.org/projects/pypka/badge/?version=latest)](https://pypka.readthedocs.io/en/latest/?badge=latest)\n\n[![PyPI version](https://badge.fury.io/py/pypKa.svg)](https://badge.fury.io/py/pypKa)  [![PyPI - Downloads](https://img.shields.io/pypi/dm/pypKa)](https://badge.fury.io/py/pypKa)\n\n# PypKa\n\nA python module for flexible Poisson-Boltzmann based pKa calculations with proton tautomerism\nDOI: <a href="https://doi.org/10.1021/acs.jcim.0c00718">10.1021/acs.jcim.0c00718</a>\n\n```bibtex\n@article{reis2020jcim,\nauthor = {Reis, Pedro B. P. S. and Vila-Viçosa, Diogo and Rocchia, Walter and Machuqueiro, Miguel},\ntitle = {PypKa: A Flexible Python Module for Poisson–Boltzmann-Based pKa Calculations},\njournal = {Journal of Chemical Information and Modeling},\nvolume = {60},\nnumber = {10},\npages = {4442-4448},\nyear = {2020},\ndoi = {10.1021/acs.jcim.0c00718}\n}\n```\n\n## Documentation & Basic Usage\n\n  Documentation can be found [here](https://pypka.readthedocs.io/en/latest/)\n\n  Starting templates for the the API and CLI usage can be found [here](https://pypka.readthedocs.io/en/latest/example.html) while a online notebook is hosted at [Google Colab](https://colab.research.google.com/github/mms-fcul/PypKa/blob/master/pypka/example/notebook/pypka.ipynb)\n\n## Installation & Dependencies\n\nPypKa should be installed in a Linux-based system. In Windows please use the [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10).\nA docker image is also [available](https://hub.docker.com/r/pedrishi/pypka).\n\n* python2.6>= & python3.5>=\n* libgfortran4\n* gawk\n* pytest\n* numpy\n\n```bash\n  pip3 install pypka\n  apt install gawk gcc gfortran libgfortran4 python2\n```\n\n## Contributing\n\nContributions are encouraged, and they are greatly appreciated!\n\nYou can contribute in many ways:\n\n* Report Bugs\n* Fix Bugs\n* Implement Features\n* Write Documentation\n* Submit Feedback\n\nFor more info check [CONTRIBUTING](./CONTRIBUTING.rst)\n\n## License\n\n  pypka is distributed under a [LGPL-3.0](./LICENSE), however delphi4py depends on\n  DelPhi which is proprietary. To use DelPhi the user is required to\n  download the DelPhi license\n  [here](https://honiglab.c2b2.columbia.edu/software/cgi-bin/software.pl?input=DelPhi)\n\n## Contacts\n\n  Please submit a github issue to report bugs and to request new features.\n  Alternatively you may find the developer [here](mailto:pdreis@fc.ul.pt). Please visit ou [website](http://mms.rd.ciencias.ulisboa.pt/) for more information.\n',
    'author': 'Pedro Reis',
    'author_email': 'pdreis@fc.ul.pt',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypka.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
