# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ngsderive', 'ngsderive.commands', 'ngsderive.readers']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=4.0.2,<5.0.0',
 'gtfparse>=1.2.1,<2.0.0',
 'pysam>=0.15.3,<0.16.0',
 'pytabix>=0.1,<0.2',
 'rstr>=2.2.6,<3.0.0',
 'sortedcontainers>=2.3.0,<3.0.0']

entry_points = \
{'console_scripts': ['ngsderive = ngsderive.__main__:run']}

setup_kwargs = {
    'name': 'ngsderive',
    'version': '2.2.0',
    'description': 'Forensic analysis tool useful in backwards computing information from next-generation sequencing data.',
    'long_description': '<p align="center">\n  <h1 align="center">\n    ngsderive\n  </h1>\n\n  <p align="center">\n    <a href="https://actions-badge.atrox.dev/stjudecloud/ngsderive/goto" target="_blank">\n      <img alt="Actions: CI Status"\n          src="https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fstjudecloud%2Fngsderive%2Fbadge&style=flat" />\n    </a>\n    <a href="https://pypi.org/project/ngsderive/" target="_blank">\n      <img alt="PyPI"\n          src="https://img.shields.io/pypi/v/ngsderive?color=orange">\n    </a>\n    <a href="https://pypi.python.org/pypi/ngsderive/" target="_blank">\n      <img alt="PyPI: Downloads"\n          src="https://img.shields.io/pypi/dm/ngsderive?color=orange">\n    </a>\n    <a href="https://pypi.python.org/pypi/ngsderive/" target="_blank">\n      <img alt="PyPI: Downloads"\n          src="https://img.shields.io/pypi/pyversions/ngsderive?color=orange">\n    </a>\n    <a href="https://github.com/stjudecloud/ngsderive/blob/master/LICENSE.md" target="_blank">\n    <img alt="License: MIT"\n          src="https://img.shields.io/badge/License-MIT-blue.svg" />\n    </a>\n  </p>\n\n\n  <p align="center">\n    Forensic analysis tool useful in backwards computing information from next-generation sequencing data. \n    <br />\n    <a href="https://stjudecloud.github.io/ngsderive/"><strong>Explore the docs »</strong></a>\n    <br />\n    <br />\n    <a href="https://github.com/stjudecloud/ngsderive/issues/new?assignees=&labels=&template=feature_request.md&title=Descriptive%20Title&labels=enhancement">Request Feature</a>\n    ·\n    <a href="https://github.com/stjudecloud/ngsderive/issues/new?assignees=&labels=&template=bug_report.md&title=Descriptive%20Title&labels=bug">Report Bug</a>\n    ·\n    ⭐ Consider starring the repo! ⭐\n    <br />\n  </p>\n</p>\n\n> Notice: `ngsderive` is a forensic analysis tool useful in backwards computing information \n> from next-generation sequencing data. Notably, results are provided as a \'best guess\' — \n> the tool does not claim 100% accuracy and results should be considered with that understanding.\n\n## 🎨 Features\n\nThe following attributes can be guessed using ngsderive:\n\n* <b>Illumina Instrument.</b> Infer which Illumina instrument was used to generate the data by matching against known instrument and flowcell naming patterns. Each guess comes with a confidence score.\n* <b>RNA-Seq Strandedness.</b> Infer from the data whether RNA-Seq data was generated using a Stranded-Forward, Stranded-Reverse, or Unstranded protocol.\n* <b>Pre-trimmed Read Length.</b> Compute the distribution of read lengths in the file and attempt to guess what the original read length of the experiment was.\n* <b>PHRED Score Encoding.</b> Infers which encoding scheme was used to store PHRED scores as ASCII characters.\n* <b>Junction Annotation.</b> Annotates splice junctions as novel, partial novel, or known in comparison to a reference gene model.\n\n## 📚 Getting Started\n\n### Installation\n\nYou can install ngsderive using the Python Package Index ([PyPI](https://pypi.org/)).\n\n```bash\npip install ngsderive\n```\n\n## 🖥️ Development\n\nIf you are interested in contributing to the code, please first review\nour [CONTRIBUTING.md][contributing-md] document. \n\nTo bootstrap a development environment, please use the following commands.\n\n```bash\n# Clone the repository\ngit clone git@github.com:stjudecloud/ngsderive.git\ncd ngsderive\n\n# Install the project using poetry\npoetry install\n```\n\n## 🚧️ Tests\n\nngsderive provides a (currently patchy) set of tests — both unit and end-to-end.\n\n```bash\npy.test\n```\n\n## 🤝 Contributing\n\nContributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/stjudecloud/ngsderive/issues). You can also take a look at the [contributing guide][contributing-md].\n\n## 📝 License\n\nThis project is licensed as follows:\n\n* All code related to the `instrument` subcommand is licensed under the [AGPL\n  v2.0][agpl-v2]. This is not due any strict requirement, but out of deference\n  to some [code][10x-inspiration] I drew inspiration from (and copied patterns\n  from), the decision was made to license this code consistently.\n* The rest of the project is licensed under the MIT License - see the\n  [LICENSE.md](LICENSE.md) file for details.\n\nCopyright © 2020 [St. Jude Cloud Team](https://github.com/stjudecloud).<br />\n\n[10x-inspiration]: https://github.com/10XGenomics/supernova/blob/master/tenkit/lib/python/tenkit/illumina_instrument.py\n[agpl-v2]: http://www.affero.org/agpl2.html\n[contributing-md]: https://github.com/stjudecloud/ngsderive/blob/master/CONTRIBUTING.md\n[license-md]: https://github.com/stjudecloud/ngsderive/blob/master/LICENSE.md\n',
    'author': 'Clay McLeod',
    'author_email': 'Clay.McLeod@STJUDE.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/claymcleod/ngsderive',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
