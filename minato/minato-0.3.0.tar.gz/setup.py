# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minato', 'minato.commands', 'minato.filesystems']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.97,<2.0.0',
 'google-cloud-storage>=1.39.0,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'tqdm>=4.60.0,<5.0.0']

entry_points = \
{'console_scripts': ['minato = minato.__main__:run']}

setup_kwargs = {
    'name': 'minato',
    'version': '0.3.0',
    'description': 'Cache and file system for online resources',
    'long_description': 'Minato\n======\n\n[![Actions Status](https://github.com/altescy/minato/workflows/CI/badge.svg)](https://github.com/altescy/minato/actions/workflows/main.yml)\n[![Python version](https://img.shields.io/pypi/pyversions/minato)](https://github.com/altescy/minato)\n[![License](https://img.shields.io/github/license/altescy/minato)](https://github.com/altescy/minato/blob/master/LICENSE)\n[![pypi version](https://img.shields.io/pypi/v/minato)](https://pypi.org/project/minato/)\n\nCache & file system for online resources in Python\n\n\n## Installation\n\n```\n$ pip install minato\n```\n\n## Usage\n\n### Python\n\n```python\nimport minato\n\n# Read / write files on online storage\nwith minato.open("s3://your_bucket/path/to/file", "w") as f:\n    f.write("Create a new file on AWS S3!")\n\n# Cache & manage online resources in local storage\nlocal_filename = minato.cached_path("http://example.com/path/to/archive.zip!inner/path/to/file")\n```\n\n### CLI\n\n```\n$ minato --help\nusage: minato\n\npositional arguments:\n  {cache,download,list,remove,update,upload}\n    cache               cache remote file and return cached local file path\n    download            download file to local\n    list                show list of cached files\n    remove              remove cached files\n    update              update cached files\n    upload              upload local file to remote\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --version             show program\'s version number and exit\n```\n',
    'author': 'Yasuhiro Yamaguchi',
    'author_email': 'altescy@fastmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/altescy/minato',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
