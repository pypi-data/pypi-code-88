# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['earworm']

package_data = \
{'': ['*'], 'earworm': ['static/*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'tinytag>=1.5.0,<2.0.0',
 'webassets>=2.0,<3.0']

entry_points = \
{'console_scripts': ['earworm = earworm.generate:main']}

setup_kwargs = {
    'name': 'earworm',
    'version': '0.1.1',
    'description': 'Create a simple web page to listen to audio files in a directory',
    'long_description': '# earworm\nCreate a simple web page to listen to audio files in a directory\n\n## Setup\n\nThe package is available on PyPI and you can install it using pip/conda.\n\n```sh\npip install earworm\n```\n## Usage\n\nThis tool can generate a simple HTML page from a directory of music files. The\ntool can read metadata from files directly (currently only supports MP3 files\nand ID3 tags). But, if you have files which are not MP3, you can use a CSV file\nwith the metadata.\n\nThe CSV file **must** have the following columns `filename` and `title`, and\nany additional ones you may want. A template can be generated using the tool --\nsee step 3 below.\n\n1. To get started create a copy of the example config file:\n\n\n   ```sh\n   cp config.yml.example config.yml\n   ```\n\n1. Change the value of `music_dir` to the directory where you have your music\n   files. If you wish to use a CSV file for the metadata, add a `metadata_csv`\n   entry to the config.\n\n   ```yaml\n   metadata_csv: "/path/to/metadata.csv"\n   ```\n\n1. You can generate a template for the `metadata.csv` from your `music_dir` by\n   running `earworm` with the `--update-csv` flag. Once the CSV file is\n   generated, add a `metadata_csv` entry pointing to this file to your config.\n\n1. Run `earworm` to generate a directory called `output` with an\n   `index.html`, `music/` directory with all the music files that have "valid\n   metadata", and a `covers/` directory with the cover images for the albums.\n\n2. You can specify the `<title>` of the page by using the `title` config var\n\n3. If the `base_url` parameter is specified, an `og:image` tag is added to the\n   page, using the latest song\'s cover image.\n\n2. Open the `index.html` in your browser to view the playlist locally.\n\n4. If you have access to a webserver, you can just sync the output directory to\n   your webserver. You can modify `deploy.sh` for your purposes, if you like.\n\n5. If you don\'t have access to a webserver you can use something like [Google\n   Drive](https://web.archive.org/web/20201127203126/https://www.ampercent.com/host-static-websites-google-driv/11070/)\n   or\n   [Dropbox](https://web.archive.org/web/20210117032036/https://www.ampercent.com/host-static-website-dropbox-free-webhosting/6426/)\n   to host this as a static website.\n\n## Dev Setup\n\nWhen working on the source (py/html/CSS/JS) of the site, you can automatically\ngenerate the html each time you make any changes to the input files using\n`entr`.\n\n```sh\nls /path/to/config $(git ls-files) | entr earworm --config /path/to/config-file\n```\n\n### JS toolchain\n\nTo change the JS files, you need to have `rollup` installed and you can run the\nrollup watcher (`rollup -w -c rollup.config.js`) to build the `bundle.js`.\n',
    'author': 'Puneeth Chaganti',
    'author_email': 'punchagan@muse-amuse.in',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/punchagan/earworm/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
