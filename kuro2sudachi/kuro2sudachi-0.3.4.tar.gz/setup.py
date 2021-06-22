# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kuro2sudachi']

package_data = \
{'': ['*']}

install_requires = \
['SudachiDict-core>=20210608,<20210609',
 'importlib-metadata>=3.7.3,<4.0.0',
 'jaconv>=0.2.4,<0.3.0',
 'sudachidict_full>=20210608,<20210609',
 'sudachipy>=0.5.2,<0.6.0']

entry_points = \
{'console_scripts': ['kuro2sudachi = kuro2sudachi.core:cli']}

setup_kwargs = {
    'name': 'kuro2sudachi',
    'version': '0.3.4',
    'description': '',
    'long_description': '# kuro2sudachi\n\n[![PyPi version](https://img.shields.io/pypi/v/kuro2sudachi.svg)](https://pypi.python.org/pypi/kuro2sudachi/)\n![PyTest](https://github.com/po3rin/kuro2sudachi/workflows/PyTest/badge.svg)\n[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-390/)\n\nkuro2sudachi lets you to convert kuromoji user dict to sudachi user dict.\n\n## Usage\n\n```sh\n$ pip install kuro2sudachi\n$ kuro2sudachi kuromoji_dict.txt -o sudachi_user_dict.txt\n```\n\n## Custom pos convert dict\n\nyou can overwrite convert config with setting json file.\n\n```json\n{\n    "固有名詞": {\n        "sudachi_pos": "名詞,固有名詞,一般,*,*,*",\n        "left_id": 4786,\n        "right_id": 4786,\n        "cost": 5000\n    },\n    "名詞": {\n        "sudachi_pos": "名詞,普通名詞,一般,*,*,*",\n        "left_id": 5146,\n        "right_id": 5146,\n        "cost": 5000\n    }\n}\n\n```\n\n```$\n$ kuro2sudachi kuromoji_dict.txt -o sudachi_user_dict.txt -c convert_config.json\n```\n\nif you want to ignore unsupported pos error & invalid format, use `--ignore` flag.\n\n## Dictionary type\n\nYou can specify the dictionary with the tokenize option -s (default: core).\n\n```sh\n$ pip install sudachidict_full\n$ kuro2sudachi kuromoji_dict.txt -o sudachi_user_dict.txt -s full\n```\n\n## Auto Splitting\n\nkuro2sudachi supports suto splitting.\n\n```json\n{\n    "名詞": {\n        "sudachi_pos": "名詞,普通名詞,一般,*,*,*",\n        "left_id": 5146,\n        "right_id": 5146,\n        "cost": 5000,\n        "split_mode": "C",\n        "unit_div_mode": [\n            "A", "B"\n        ]\n    }\n}\n```\n\noutput includes unit devision info.\n\n```sh\n$ cat kuromoji_dict.txt\n融合たんぱく質,融合たんぱく質,融合たんぱく質,名詞\n発作性心房細動,発作性心房細動,発作性心房細動,名詞\n\n$ kuro2sudachi kuromoji_dict.txt -o sudachi_user_dict.txt -c convert_config.json --ignore\n\n$ cat sudachi_user_dict.txt\n融合たんぱく質,4786,4786,5000,融合たんぱく質,名詞,普通名詞,一般,*,*,*,,融合たんぱく質,*,C,"融合,名詞,普通名詞,サ変可能,*,*,*,ユウゴウ/たんぱく,名詞,普通名詞,一般,*,*,*,タンパク/質,接尾辞,名詞的,一般,*,*,*,シツ","融合,名詞,普通名詞,サ変可能,*,*,*,ユウゴウ/たんぱく質,名詞,普通名詞,一般,*,*,*,タンパクシツ",*\n発作性心房細動,4786,4786,5000,発作性心房細動,名詞,普通名詞,一般,*,*,*,,発作性心房細動,*,C,"発作,名詞,普通名詞,一般,*,*,*,ホッサ/性,接尾辞,名詞的,一般,*,*,*,セイ/心房,名詞,普通名詞,一般,*,*,*,シンボウ/細動,名詞,普通名詞,一般,*,*,*,サイドウ","発作,名詞,普通名詞,一般,*,*,*,ホッサ/性,接尾辞,名詞的,一般,*,*,*,セイ/心房,名詞,普通名詞,一般,*,*,*,シンボウ/細動,名詞,普通名詞,一般,*,*,*,サイドウ",*\n```\n\n## Splitting Words defined by kuromoji\n\nCurrently, the CLI does not support word splitting defined by kuromoji. Therefore, the split representation of kuromoji is ignored.\n\n```\n中咽頭ガン,中咽頭 ガン,チュウイントウ ガン,カスタム名詞\n↓\n中咽頭ガン,4786,4786,7000,中咽頭ガン,名詞,固有名詞,一般,*,*,*,チュウイントウガン,中咽頭ガン,*,*,*,*,*\n```\n\n# For Developer\n\ntest kuro2sudachi\n\n```sh\n$ poetry install\n$ poetry run pytest\n```\n\nexec kuro2sudachi command\n\n```sh\n$ poetry run kuro2sudachi tests/kuromoji_dict_test.txt -o sudachi_user_dict.txt\n```\n\n## TODO\n\n- [ ] split mode\n- [ ] default rewrite\n',
    'author': 'po3rin',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/po3rin/kuro2sudachi',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
