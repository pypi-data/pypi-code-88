# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyfactcast',
 'pyfactcast.app',
 'pyfactcast.app.business',
 'pyfactcast.app.ui',
 'pyfactcast.client',
 'pyfactcast.client.auth',
 'pyfactcast.grpc',
 'pyfactcast.grpc.generated']

package_data = \
{'': ['*'], 'pyfactcast.grpc': ['proto/*']}

install_requires = \
['grpcio-tools>=1.37.1,<2.0.0',
 'grpcio>=1.37.1,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'rich>=10.2.0,<11.0.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{'docs': ['sphinx<4',
          'sphinx-click>=2.7.1,<3.0.0',
          'sphinx-rtd-theme>=0.5.2,<0.6.0',
          'sphinx-autodoc-typehints>=1.12.0,<2.0.0']}

entry_points = \
{'console_scripts': ['factcast = pyfactcast.app.ui.cli:app']}

setup_kwargs = {
    'name': 'pyfactcast',
    'version': '0.0.9',
    'description': 'A python client library for FactCast',
    'long_description': '# PyFactCast\n\nWelcome to pyfactcast. You can find more extensive documentation over at [readthedocs](https://pyfactcast.readthedocs.io/en/latest/).\n\nThis project arose manly out of frustration with the excessive wait times for a spring boot\nbased CLI like the one offered by the original [FactCast](https://docs.factcast.org/).\nBut on the way grew a bit. It will likely grow even more as I would like to actually use this\ntooling to bring the ability for rapid prototyping and production grade python applications\nto the FactCast community.\n\nContributions are welcome. Just get in touch.\n\n## Quickstart\n\nSimply `pip install pyfactcast` and get going. The cli is available as `factcast` and\nyou can run `factcast --help` to get up to speed on what you can do.\n\n## Development\n\nThis project uses `poetry` for dependency management and `pre-commit` for local checks.\n',
    'author': 'Eduard Thamm',
    'author_email': 'eduard.thamm@thammit.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/edthamm/pyfactcast',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
