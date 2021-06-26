# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['allennlp_shiba',
 'allennlp_shiba.common',
 'allennlp_shiba.common.testing',
 'allennlp_shiba.data',
 'allennlp_shiba.data.token_indexers',
 'allennlp_shiba.data.tokenizers',
 'allennlp_shiba.modules',
 'allennlp_shiba.modules.token_embedders']

package_data = \
{'': ['*']}

install_requires = \
['allennlp>=2.5.0,<3.0.0', 'shiba-model>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'allennlp-shiba',
    'version': '0.0.1',
    'description': 'AllenNLP integration for Shiba: Japanese CANINE model',
    'long_description': '# Allennlp Integration for [Shiba](https://github.com/octanove/shiba)\n\n[![CI](https://github.com/shunk031/allennlp-shiba-model/actions/workflows/ci.yml/badge.svg)](https://github.com/shunk031/allennlp-shiba-model/actions/workflows/ci.yml)\n\n`allennlp-shiab-model` is a Python library that provides AllenNLP integration for [shiba-model](https://pypi.org/project/shiba-model/).\n\n> SHIBA is an approximate reimplementation of CANINE [[1]](https://github.com/octanove/shiba#1) in raw Pytorch, pretrained on the Japanese wikipedia corpus using random span masking. If you are unfamiliar with CANINE, you can think of it as a very efficient (approximately 4x as efficient) character-level BERT model. Of course, the name SHIBA comes from the identically named Japanese canine.\n\n## Example\n\nThis library enables users to specify the in a jsonnet config file. Here is an example of the model in jsonnet config file:\n\n```json\n{\n    "dataset_reader": {\n        "tokenizer": {\n            "type": "shiba",\n        },\n        "token_indexers": {\n            "tokens": {\n                "type": "shiba",\n            }\n        },\n    },\n    "model": {\n        "shiba_embedder": {\n            "type": "basic",\n            "token_embedders": {\n                "shiba": {\n                    "type": "shiba",\n                    "eval_model": true,\n                }\n            }\n\n        }\n    }\n}\n```\n\n\n## Reference\n\n- Joshua Tanner and Masato Hagiwara (2021). [SHIBA: Japanese CANINE model](https://github.com/octanove/shiba). GitHub repository, GitHub.\n\n',
    'author': 'Shunsuke KITADA',
    'author_email': 'shunsuke.kitada.0831@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shunk031/allennlp-shiba-model',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
