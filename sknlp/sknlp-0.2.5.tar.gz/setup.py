# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sknlp',
 'sknlp.callbacks',
 'sknlp.data',
 'sknlp.data.text_segmenter',
 'sknlp.layers',
 'sknlp.layers.utils',
 'sknlp.losses',
 'sknlp.metrics',
 'sknlp.module',
 'sknlp.module.classifiers',
 'sknlp.module.discriminators',
 'sknlp.module.taggers',
 'sknlp.module.text2vec',
 'sknlp.typing',
 'sknlp.utils',
 'sknlp.vocab']

package_data = \
{'': ['*']}

install_requires = \
['jieba>=0.42.1,<0.43.0',
 'keras-tuner>=1.0.2,<2.0.0',
 'numpy<1.20.0',
 'pandas==1.0.4',
 'scikit-learn>=0.24.2,<0.25.0',
 'tabulate>=0.8.6,<0.9.0',
 'tensorflow-addons==0.13.0',
 'tensorflow-text==2.5.0',
 'tensorflow==2.5.0',
 'tf-models-official==2.5.0']

setup_kwargs = {
    'name': 'sknlp',
    'version': '0.2.5',
    'description': '',
    'long_description': None,
    'author': 'nanaya',
    'author_email': 'nanaya100@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
