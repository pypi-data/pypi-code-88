# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sfu_ml_lib',
 'sfu_ml_lib.base',
 'sfu_ml_lib.common',
 'sfu_ml_lib.dataset',
 'sfu_ml_lib.metrics',
 'sfu_ml_lib.metrics.aggregation',
 'sfu_ml_lib.models',
 'sfu_ml_lib.modules',
 'sfu_ml_lib.trackers']

package_data = \
{'': ['*']}

install_requires = \
['mlflow>=1.8,<2.0',
 'numba>=0.51,<1',
 'numpy',
 'scikit-learn>=0.24,<1',
 'scipy>=1.4,<2.0',
 'sfu-data-io>=0.0,<0.1',
 'tensorflow>=2.2,<3.0']

setup_kwargs = {
    'name': 'sfu-ml-lib',
    'version': '0.0.9',
    'description': 'Libraries that support the development of machine learning models in TensorFlow.',
    'long_description': None,
    'author': 'Anderson de Andrade',
    'author_email': 'adeandrade@ensc.sfu.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
