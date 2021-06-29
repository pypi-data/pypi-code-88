# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aioswitcher', 'aioswitcher.api', 'aioswitcher.device', 'aioswitcher.schedule']

package_data = \
{'': ['*']}

extras_require = \
{'docs': ['insegel==1.1.0',
          'sphinx==4.0.2',
          'sphinxcontrib-autoprogram==0.1.7',
          'sphinxcontrib-spelling==7.2.1',
          'toml==0.10.1']}

setup_kwargs = {
    'name': 'aioswitcher',
    'version': '2.0.0',
    'description': 'Switcher Unofficial Integration.',
    'long_description': '<!-- markdownlint-disable MD013 -->\n# Switcher Unofficial Integration</br>[![pypi-version]][11] [![pypi-downloads]][11] [![license-badge]][4]\n<!-- markdownlint-enable MD013 -->\n\n[![gh-build-status]][7] [![read-the-docs]][8] [![codecov]][3]\n\nPyPi module named [aioswitcher][11] for integrating with the [Switcher Devices](https://www.switcher.co.il/).</br>\nPlease check out the [documentation][8].\n\n## Install\n\n```shell\npip install aioswitcher\n```\n\n## Usage Example\n\nPlease check out the [documentation][8] for the full usage section.\n\n```python\nasync with SwitcherApi(device_ip, device_id) as api:\n    # get the device state\n    state_response = await swapi.get_state()\n\n    # control the device on for 15 minutes and then turn it off\n    await api.control_device(Command.ON, 15)\n    await api.control_device(Command.OFF)\n```\n\n## Command Line Helper Scripts\n\n- [discover_devices.py](scripts/discover_devices.py) can be used to discover devices\n  and their states.\n- [control_device.py](scripts/control_device.py) can be used to control a device.\n\n## Contributing\n\nThe contributing guidelines are [here](.github/CONTRIBUTING.md)\n\n## Code of Conduct\n\nThe code of conduct is [here](.github/CODE_OF_CONDUCT.md)\n\n<!-- Real Links -->\n[2]: https://github.com/TomerFi/aioswitcher/releases\n[3]: https://codecov.io/gh/TomerFi/aioswitcher\n[4]: https://github.com/TomerFi/aioswitcher\n[7]: https://github.com/TomerFi/aioswitcher/actions/workflows/pre_release.yml\n[8]: https://aioswitcher.tomfi.info/\n[11]: https://pypi.org/project/aioswitcher\n<!-- Badges Links -->\n[codecov]: https://codecov.io/gh/TomerFi/aioswitcher/graph/badge.svg\n[gh-build-status]: https://github.com/TomerFi/aioswitcher/actions/workflows/pre_release.yml/badge.svg\n[license-badge]: https://img.shields.io/github/license/tomerfi/aioswitcher\n[pypi-downloads]: https://img.shields.io/pypi/dm/aioswitcher.svg?logo=pypi&color=1082C2\n[pypi-version]: https://img.shields.io/pypi/v/aioswitcher?logo=pypi\n[read-the-docs]: https://readthedocs.org/projects/aioswitcher/badge/?version=stable\n',
    'author': 'Tomer Figenblat',
    'author_email': 'tomer.figenblat@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/aioswitcher/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
