# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trattoria']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16', 'scipy>=1.5', 'trattoria-core==0.4.2']

setup_kwargs = {
    'name': 'trattoria',
    'version': '0.3.3',
    'description': 'The fastest streaming algorithms for your TTTR data',
    'long_description': '# 🍕 Trattoria 🍕\nTrattoria delivers you the fastest streaming algorithms to analyze your TTTR data. We\ncurrenlty support the following algorithms:\n- __Second order autocorrelations__: Calculate the autocorrelation between two channels of\n  your TCSPC.\n- __Third Order autocorrelations__: Calculate the coincidences between 3 channels. A sync\nversion is provided were it uses the fact that the sync channel is periodic and known.\n- __Intensity time trace__: Calculate the intensity on each (or all) channels versus time.\n- __Zero finder__: Given two uncorrelated channels (e.g. a laser behind a 50/50 splitter)\n  compute the delay between the input channels.\n- __Lifetime__: Compute the lifetime histogram from a pulsed excitation experiment.\n\n## Supported file formats\nCurrently Trattoria can only read PTU files from PicoQuant. If you want support for more\nor want to help providing it please put a ticket on the tttr-toolbox project.\n\n## Installing\n```\npip install trattoria\n```\n\n## Examples\nThe entry point to Trattoria is the PTUFile class. This class has methods\nthat give us access to the algorithms. Each of the algorithms takes as input a\nparameter object and returns a results object. For a complete list of the functionality\nsee the `examples` folder.\n\n```python\nimport trattoria\n\nimport matplotlib.pyplot as plt\n\nptu_filepath = Path("/path/to/some.ptu")\nptu = trattoria.PTUFile(ptu_filepath)\n\ntimetrace_params = trattoria.TimeTraceParameters(\n    resolution=10.0,\n    channel=None,\n)\ntt_res = ptu.timetrace(timetrace_params)\n\nplt.plot(tt_res.t, tt_res.tt / timetrace_params.resolution)\nplt.xlabel("Time (s)")\nplt.ylabel("Intensity (Hz)")\nplt.show()\n```\n\nThe examples folders contains examples of all the functionality available in Trattoria.\nFor more details check the docstrings in `core.py`.\n\n## Design\nTrattoria is just a very thin wrapper around the\n[trattoria-core](https://github.com/GCBallesteros/trattoria-core) library which\nitselfs provides a lower level interface to the the\n[tttr-toolbox](https://github.com/GCBallesteros/tttr-toolbox/tree/master/tttr-toolbox)\nlibrary. A Rust project that provides the compiled components that allows us to\ngo fast.\n\n## Citing\n\n',
    'author': 'Guillem Ballesteros',
    'author_email': 'dev+pypi@maxwellrules.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GCBallesteros/trattoria',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
