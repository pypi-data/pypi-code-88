# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mira',
 'mira.core',
 'mira.datasets',
 'mira.detectors',
 'mira.thirdparty',
 'mira.thirdparty.automl',
 'mira.thirdparty.automl.efficientdet',
 'mira.thirdparty.automl.efficientdet.aug',
 'mira.thirdparty.automl.efficientdet.backbone',
 'mira.thirdparty.automl.efficientdet.dataset',
 'mira.thirdparty.automl.efficientdet.keras',
 'mira.thirdparty.automl.efficientdet.object_detection',
 'mira.thirdparty.automl.efficientdet.visualize',
 'mira.thirdparty.automl.efficientnetv2']

package_data = \
{'': ['*'],
 'mira.datasets': ['assets/*'],
 'mira.thirdparty.automl': ['.github/workflows/*'],
 'mira.thirdparty.automl.efficientdet': ['g3doc/*', 'testdata/*'],
 'mira.thirdparty.automl.efficientnetv2': ['g3doc/*']}

install_requires = \
['albumentations',
 'numpy',
 'pandas',
 'scikit-learn',
 'tensorflow_addons',
 'tqdm',
 'validators']

setup_kwargs = {
    'name': 'mira',
    'version': '0.5.0rc1',
    'description': 'A package for simplifying object detection',
    'long_description': '# mira [![CircleCI](https://circleci.com/gh/faustomorales/mira.svg?style=shield)](https://circleci.com/gh/faustomorales/mira) [![Documentation Status](https://readthedocs.org/projects/mira-python/badge/?version=latest)](https://mira-python.readthedocs.io/en/latest/?badge=latest)\n\nmira provides tooling for simple object detection projects. The package spans three areas of focus.\n\n- **Core** object detection abstractions for images and annotations\n- Access to **datasets** from common formats (e.g., VOC, COCO) and image sets (e.g., VOC 2012)\n- A common API to for **well-known models** (e.g., RetinaNet and YOLO)\n\nCheck out [the docs](https://mira-python.readthedocs.io/en/latest/).\n\n## Installation\n\n```shell\npip install mira\n```\n',
    'author': 'Fausto Morales',
    'author_email': 'faustomorales@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/faustomorales/mira',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
