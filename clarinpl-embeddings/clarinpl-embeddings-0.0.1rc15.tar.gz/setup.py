# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['embeddings',
 'embeddings.data',
 'embeddings.embedding',
 'embeddings.evaluator',
 'embeddings.metric',
 'embeddings.model',
 'embeddings.pipeline',
 'embeddings.task',
 'embeddings.task.flair_task',
 'embeddings.transformation',
 'embeddings.transformation.flair_transformation',
 'embeddings.utils',
 'experimental',
 'experimental.datasets',
 'experimental.datasets.utils',
 'experimental.embeddings',
 'experimental.embeddings.language_models',
 'experimental.embeddings.scripts']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0',
 'datasets==1.6.1',
 'flair>=0.8.0,<0.9.0',
 'requests>=2.25.1,<3.0.0',
 'scikit-learn>=0.24.1,<0.25.0',
 'seqeval>=1.2.2,<2.0.0',
 'spacy>=3.0.0,<4.0.0',
 'srsly>=2.4.0,<3.0.0',
 'tensorboard>=2.4.1,<3.0.0',
 'torch>=1.8.0,<2.0.0',
 'transformers>=4.4.2,<5.0.0',
 'typer>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'clarinpl-embeddings',
    'version': '0.0.1rc15',
    'description': '',
    'long_description': None,
    'author': 'Roman Bartusiak',
    'author_email': 'riomus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CLARIN-PL/embeddings',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
