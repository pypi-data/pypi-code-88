# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dotify', 'dotify.models']

package_data = \
{'': ['*'], 'dotify.models': ['schema/*']}

install_requires = \
['cached-property>=1.5.2,<2.0.0',
 'moviepy',
 'mutagen',
 'python-jsonschema-objects',
 'pytube',
 'requests',
 'spotipy',
 'youtube-search-python']

setup_kwargs = {
    'name': 'dotify',
    'version': '2.0.0',
    'description': '🐍🎶 Yet another Spotify Web API Python library',
    'long_description': '![Dotify](https://raw.githubusercontent.com/the-dotify-project/dotify/master/docs/img/logo.png)\n\n<p align="center">\n  <a href="https://www.python.org/">\n    <img\n      src="https://img.shields.io/pypi/pyversions/dotify"\n      alt="PyPI - Python Version"\n    />\n  </a>\n  <a href="https://pypi.org/project/dotify/">\n    <img\n      src="https://img.shields.io/pypi/v/dotify"\n      alt="PyPI"\n    />\n  </a>\n  <a href="https://github.com/the-dotify-project/dotify/actions/workflows/ci.yml">\n    <img\n      src="https://github.com/the-dotify-project/dotify/actions/workflows/ci.yml/badge.svg"\n      alt="CI"\n    />\n  </a>\n  <a href="https://the-dotify-project.github.io/dotify/">\n    <img\n      src="https://github.com/the-dotify-project/dotify/actions/workflows/docs.yml/badge.svg"\n      alt="docs"\n    />\n  </a>\n  <a href="https://results.pre-commit.ci/latest/github/the-dotify-project/dotify/master">\n    <img\n      src="https://results.pre-commit.ci/badge/github/the-dotify-project/dotify/master.svg"\n      alt="pre-commit.ci status"\n    />\n  </a>\n  <a href="https://codeclimate.com/github/billsioros/dotify/maintainability">\n    <img\n      src="https://api.codeclimate.com/v1/badges/573685a448c6422d49de/maintainability"\n      alt="Maintainability"\n    />\n  </a>\n  <a href="https://codeclimate.com/github/billsioros/dotify/test_coverage">\n    <img\n      src="https://api.codeclimate.com/v1/badges/573685a448c6422d49de/test_coverage"\n      alt="Test Coverage"\n    />\n  </a>\n  <a href="https://opensource.org/licenses/MIT">\n    <img\n      src="https://img.shields.io/pypi/l/dotify"\n      alt="PyPI - License"\n    />\n  </a>\n  <a href="https://github.com/the-dotify-project/dotify/commits">\n    <img\n      src="https://img.shields.io/github/commits-since/the-dotify-project/dotify/latest?style=flat-square"\n      alt="GitHub commits since latest release (by SemVer)"\n    />\n  </a>\n</p>\n\n> _🚧 The project is currently under heavy development 🚧_\n\n## Example Usage\n\n```python\n>>> from dotify import Dotify, Track\n>>> with Dotify(SPOTIFY_ID, SPOTIFY_SECRET):\n>>>     result = next(Track.search("SAINt JHN 5 Thousand Singles", limit=1))\n>>> result\n<Track "SAINt JHN - 5 Thousand Singles">\n>>> result.url\n\'https://open.spotify.com/track/0fFWxRZGKR7HDW2xBMOZgW\'\n>>> result.download("SAINt JHN - 5 Thousand Singles.mp3")\nPosixPath(\'SAINt JHN - 5 Thousand Singles.mp3\')\n```\n\nFeel free to check the [examples](https://github.com/the-dotify-project/dotify/tree/master/examples) folder for more use cases!\n\n## Features\n\n- Searching for\n  - Tracks\n  - Playlists\n  - Albums\n- Downloading\n  - Tracks\n  - Playlists\n  - Albums\n\n## Documentation\n\nThe project\'s documentation can be found [here](https://the-dotify-project.github.io/dotify/).\n\n## Installation\n\n```bash\npip install dotify\n```\n\n## Contributing\n\nIf you would like to contribute to the project, please go through the [Contributing Guidelines](https://the-dotify-project.github.io/dotify/latest/CONTRIBUTING/) first.\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tr>\n    <td align="center"><a href="https://www.linkedin.com/in/vasileios-sioros/"><img src="https://avatars.githubusercontent.com/u/33862937?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vasilis Sioros</b></sub></a><br /><a href="#maintenance-billsioros" title="Maintenance">🚧</a> <a href="#projectManagement-billsioros" title="Project Management">📆</a> <a href="https://github.com/billsioros/dotify/commits?author=billsioros" title="Documentation">📖</a></td>\n  </tr>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n',
    'author': 'billsioros',
    'author_email': 'billsioros97@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://the-dotify-project.github.io/dotify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
