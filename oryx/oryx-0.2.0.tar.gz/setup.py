# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oryx',
 'oryx.bijectors',
 'oryx.core',
 'oryx.core.interpreters',
 'oryx.core.interpreters.inverse',
 'oryx.core.ppl',
 'oryx.core.state',
 'oryx.distributions',
 'oryx.experimental',
 'oryx.experimental.matching',
 'oryx.experimental.mcmc',
 'oryx.experimental.nn',
 'oryx.experimental.optimizers',
 'oryx.internal',
 'oryx.tools',
 'oryx.util']

package_data = \
{'': ['*']}

install_requires = \
['jax==0.2.16', 'jaxlib==0.1.68', 'tfp-nightly[jax]==0.14.0-alpha.20210623']

extras_require = \
{':python_version < "3.7"': ['dataclasses']}

setup_kwargs = {
    'name': 'oryx',
    'version': '0.2.0',
    'description': 'Probabilistic programming and deep learning in JAX',
    'long_description': None,
    'author': 'Google LLC',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
