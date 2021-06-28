# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['legistream_backend', 'legistream_backend.util']

package_data = \
{'': ['*']}

install_requires = \
['ImageHash>=4.2.0,<5.0.0',
 'bs4>=0.0.1,<0.0.2',
 'lxml>=4.6.3,<5.0.0',
 'm3u8>=0.9.0,<0.10.0',
 'pytest>=6.2.4,<7.0.0',
 'requests>=2.25.1,<3.0.0',
 'websocket-client>=1.1.0,<2.0.0',
 'websocket>=0.2.1,<0.3.0']

setup_kwargs = {
    'name': 'legistream-backend',
    'version': '1.4.17',
    'description': 'Get live stream metadata from the various Australian parliaments.',
    'long_description': "# legistream_backend\n\nThis is the Python backend for legistream.\n\n---\n\nInstall with **pip**:\n\n`pip install legistream-backend`\n\nView project on PyPI: [https://pypi.org/project/legistream-backend/](https://pypi.org/project/legistream-backend/).\n\n## Usage\n\nThis package uses different modules to get live stream data from the various Australian parliaments.\n\n**Currently supported parliaments:**\n\n- Australian Capital Territory\n- Federal\n- New South Wales\n- Northern Territory\n- Queensland\n- South Australia\n- Tasmania\n- Victoria\n- Western Australia\n\n### Setup\n\n1. Install `poetry`:\n\n    ```sh\n    pip3 install poetry\n    ```\n\n2. Install/update dependencies with `poetry`:\n\n    ```sh\n    poetry update\n    ```\n\nInstall **ffmpeg**:\n\n#### Linux\n\n`sudo apt install ffmpeg`\n\n#### Mac\n\nInstall with **brew**:\n\n`brew install ffmpeg`\n\n#### Windows\n\nOfficial Windows builds of **ffmpeg** can be found [here](https://ffmpeg.org/download.html#build-windows)\n\n### Print out stream URLs:\n\nEvery parliament module returns data the same way, Victoria is used here only for example purposes.\n\nThe `stream_urls` property can be used to return streams as a **dict**:\n\n```python\nfrom legistream_backend.vic import Stream\n\nprint(Stream().stream_urls)\n```\n\nEach URL can be returned individually by using the `[house]_stream_url` property (e.g `lower_stream_url`)\n\n```python\nprint(Stream().lower_stream_url)\n```\n\n### Check if a parliament's house is live:\n\nSimilarly, you can check the status of a live stream with the `[house]_is_live` boolean property.\n\n```python\nif(Stream().lower_is_live):\n    print('The lower house of Victoria is currently live.')\nelse:\n    print('The lower house of Victoria is not currently live.')\n```\n\n## Notes\n\n1. Run all scripts using `poetry`:\n\n    ```sh\n    poetry run python3 [file].py\n    ```\n\n1. The South Australia stream extractor uses code adapted from the [streamlink ustreamtv implementation](https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/ustreamtv.py).",
    'author': 'king-millez',
    'author_email': 'millez.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://legistream.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
