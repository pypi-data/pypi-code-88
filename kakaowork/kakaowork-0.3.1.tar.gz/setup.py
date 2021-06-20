# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kakaowork']

package_data = \
{'': ['*']}

install_requires = \
['aiosonic>=0.10.0,<0.11.0', 'pytz>=2015.7', 'urllib3>=1.14.0,<2.0.0']

extras_require = \
{'cli': ['click>=7,<9']}

entry_points = \
{'console_scripts': ['kakaowork = kakaowork.__main__:main']}

setup_kwargs = {
    'name': 'kakaowork',
    'version': '0.3.1',
    'description': 'Kakaowork Python client',
    'long_description': '# kakaowork-py\n\n(Unofficial) Kakaowork Python client\n\n[![PyPI](https://img.shields.io/pypi/v/kakaowork)](https://pypi.org/project/kakaowork)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kakaowork)](https://pypi.org/project/kakaowork)\n[![Downloads](https://pepy.tech/badge/kakaowork)](https://pepy.tech/project/kakaowork)\n[![GitHub](https://img.shields.io/github/license/skyoo2003/kakaowork-py)](LICENSE)\n[![Documentation Status](https://readthedocs.org/projects/kakaowork-py/badge/?version=latest)](https://kakaowork-py.readthedocs.io/en/latest)\n[![CI](https://github.com/skyoo2003/kakaowork-py/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/skyoo2003/kakaowork-py/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/skyoo2003/kakaowork-py/branch/master/graph/badge.svg?token=J6NQHDJEMZ)](https://codecov.io/gh/skyoo2003/kakaowork-py)\n\n__Table of Contents__\n\n- [Prerequisites](#prerequisites)\n- [Installation](#installation)\n- [Usages](#usages)\n- [Contributing](#contributing)\n- [License](#license)\n\n## Prerequisites\n\n- Python >= 3.6.1\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install kakaowork-py\n\n```bash\npip install kakaowork\n```\n\nIf you want to use CLI, install with the extras \'cli\'\n\n```bash\npip install kakaowork[cli]\n```\n\n## Usages\n\n```python\nfrom kakaowork import Kakaowork\n\n\ndef main():\n  client = Kakaowork(app_key="your_app_key")\n  r = client.users.list(limit=10)  # get a response of users using limit\n  print(r.users)\n  while r.cursor:  # loop until it does not to exist\n    print(r.users)\n    r = client.users.list(cursor=r.cursor)  # get a response of users using cursor\n\nif __name__ == \'__main__\':\n  main()\n```\n\n```python\nimport asyncio\n\nfrom kakaowork import AsyncKakaowork\n\n\nasync def main():\n    client = AsyncKakaowork(app_key="your_app_key")\n    r = await client.users.list(limit=10)  # get a response of users using limit\n    print(r.users)\n    while r.cursor:  # loop until it does not to exist\n        print(r.users)\n        r = await client.users.list(cursor=r.cursor)  # get a response of users using cursor\n\nif __name__ == \'__main__\':\n    loop = asyncio.get_event_loop()\n    loop.run_until_complete(main())\n```\n\nIf you have installed it with the extras \'cli\', you can use the command line below in your shell.\n\n```sh\n$ kakaowork --help\nUsage: kakaowork [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -k, --app-key TEXT\n  --help              Show this message and exit.\n\nCommands:\n  bots\n  conversations\n  departments\n  messages\n  spaces\n  users\n\n$ kakaowork -k <your_app_key> bots info\nID:     1\nName:   Test\nStatus: activated\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## [License](LICENSE)\n\nCopyright (c) 2021 Sung-Kyu Yoo.\n\nThis project is MIT license.\n',
    'author': 'Sung-Kyu Yoo',
    'author_email': 'skyoo2003@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/skyoo2003/kakaowork-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
