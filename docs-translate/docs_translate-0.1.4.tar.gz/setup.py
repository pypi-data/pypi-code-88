# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docs_translate']

package_data = \
{'': ['*']}

install_requires = \
['google-cloud-translate>=2.0.1,<3.0.0',
 'langdetect>=1.0.8,<2.0.0',
 'loguru>=0.5.3,<0.6.0',
 'requests>=2.24.0,<3.0.0',
 'translators>=4.7.2,<5.0.0']

entry_points = \
{'console_scripts': ['docs-translate = docs_translate.app:run']}

setup_kwargs = {
    'name': 'docs-translate',
    'version': '0.1.4',
    'description': 'CLI tool to translate markdown and reStructuredText files',
    'long_description': '# Docs Translate\n\nCLI tool to translate `.md` and `.rst` files from English to Korea and back.\n\nCan use Yandex Translation API and Google Cloud translation.\n\n## Installation\n\nInstall project:\n\n```bash\n$ pip install docs-translate\n```\n\n## Settings file\n\nYou can store your default settings in `.json` file.\n\nSettings file content example:\n\n```.json\n{\n  "target_dir":"D:\\\\{language_convert_dir}",\n  "source_lang": "ko",\n  "target_lang": "en",\n  "service_name": "Google_v2",\n}\n```\n\nIf you set config file, you should specify it with `-c CONFIG_PATH` argument!\n\n## Usage\n\n```bash\n$ docs-translate [-h] [-c CONFIG_PATH]\n               [-s {Google,Google_v2}] [-S] [-T]\n               [-path {source_path}] [-d {target_dir}]\n```\n\nIf you set config file, you can override any of settings by arguments\n\n### Positional arguments:\n* `path` Path to folder to process. If not set, uses current folder\n* `-d TARGET_DIR, --target_dir TARGET_DIR`, If not set, the target_dir in config.json is set\n\n### Optional arguments:\n* `-h, --help`, show this help message and exit\n* `-c CONFIG_PATH, --config_path CONFIG_PATH`, Path to config_file\n* `-s {Yandex,Google,Bing,Deepl}, --service_name {Yandex,Google,Bing,Deepl}`, Translating service\n* `-S SOURCE_LANG, --source_lang SOURCE_LANG`, Source language code\n* `-T TARGET_LANG, --target_lang TARGET_LANG`, Target language code\n\n### Translation services:\nNow used `Yandex`, `Google`, `Bing`, `Deepl`, `Google_v2`\n\nSome of them can be not working, try it and find the most suitable for you  \n\n`Google --> It\'s free, but the translation isn\'t good.`  \n`Google_v2 --> need to google Cloud Translation API key.` ',
    'author': 'kyeongin kim',
    'author_email': 'kikim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gs-kikim/docs-trans-app',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
