# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['entropylab_qpudb']

package_data = \
{'': ['*']}

install_requires = \
['ZODB>=5.6.0,<6.0.0', 'entropylab>=0.1.2,<0.2.0', 'pandas>=1.2.4,<2.0.0']

setup_kwargs = {
    'name': 'entropylab-qpudb',
    'version': '0.0.9',
    'description': 'A extension of entropy lab for persistent storage of calibration parameters of a quantum processing unit (QPU).',
    'long_description': '# Entropy QPU DB\n\n## Background\nThe entropy QPU DB is an extension designed to make it easy to calibrate\nand manage experimentation of quantum processing units.\nIt provides two abilites:\n\n1. to run automated calibrations of all parameters\nrelated to the qubits, couplers and readout elements that make up a QPU,\nusing calibration graphs, as inspired by Google\'s [Optimus](https://arxiv.org/abs/1803.03226) method.\n\n2. to store the calibration data in a persistent storage DB, and integrate that DB\ninto the calibration framework.\n   \nOne of the challenges of bringing up a QPU from "scratch" is\nthat it\'s not always straightforward to understand which calibrations\nneed to be, at what order and with which parameters. On the other hand,\nQPUs contain many parameters which require calibration and tracking,\nwhich makes automated tools essential for this task.\n\nThis means that the process of building the calibration graph for a QPU needs to be\nneeds to be both flexible and powerful. The QPU DB is designed to allow to do just that.\n\n## Getting started\n\nThis package requires having entropy installed, which can be obtained from pipy [here](https://pypi.org/project/entropylab/).\n\nTo get started, check out the tutorials under `docs/`.\n\n## Contact info\n\nThe QPU DB was conceived and developed by [Lior Ella](https://github.com/liorella-qm),\n[Gal Winer](https://github.com/galwiner), Ilan Mitnikov and Yonatan Cohen, and is\nmaintained by [Guy Kerem](https://github.com/qguyk). For any questions, suggestions or otherwise - please contact us on\nour [discord server](https://discord.com/channels/806244683403100171/817087420058304532)!',
    'author': 'Lior Ella',
    'author_email': 'lior@quantum-machines.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/entropy-lab/entropy-qpu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
