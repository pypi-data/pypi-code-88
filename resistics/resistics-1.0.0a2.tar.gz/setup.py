# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resistics']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'attotime==0.2.3',
 'loguru>=0.5.3,<0.6.0',
 'lttbc>=0.2.0,<0.3.0',
 'numpy>=1.20.2,<2.0.0',
 'pandas>=1.2.3,<2.0.0',
 'plotly>=4.14.3,<5.0.0',
 'prettyprinter>=0.18.0,<0.19.0',
 'pydantic>=1.8.1,<2.0.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'scipy>=1.6.2,<2.0.0',
 'tqdm>=4.61.0,<5.0.0']

setup_kwargs = {
    'name': 'resistics',
    'version': '1.0.0a2',
    'description': 'Python package for processing magnetotelluric data',
    'long_description': '## Welcome\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/resistics.svg)](https://pypi.org/project/resistics/)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/resistics)](https://pypi.org/project/resistics/)\n[![Documentation Status](https://readthedocs.org/projects/resistics/badge/?version=latest)](https://resistics.readthedocs.io/en/latest/?badge=latest)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/resistics/resistics.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/resistics/resistics/context:python)\n[![codecov](https://codecov.io/gh/resistics/resistics/branch/master/graph/badge.svg?token=CXLJC9J7AW)](https://codecov.io/gh/resistics/resistics)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nResistics is a native Python 3.8+ package for the processing of magnetotelluric\n(MT) data. It incorporates robust processing methods and adopts a modular\napproach to processing which allows for customisation and future improvements\nto be quickly adopted.\n\n## Latest news\n\nResistics is moving to version 1.0.0 which will be a breaking change versus\nthe current stable version of 0.0.6. Currently, version 1.0.0 is available as a\npre-release on PYPI.\n\n- Documentation for 1.0.0: https://resistics.readthedocs.io/\n- Documentation for 0.0.6: https://resistics.io/\n\nWhen version 1.0.0 reaches a stable releases the documentation will move to the\nmain resistics.io site.\n\n## Audience\n\nResistics is intended for people who use magnetotelluric methods to estimate the\nsubsurface resistivity. This may be for furthering geological understanding, for\ngeothermal prospecting or for other purposes.\n\nThe package may have utility for the wider electromagnetic geophysics community.\n\n## Getting started\n\nTo install the pre-release of version 1.0.0\n\npython -m pip install resistics==1.0.0a0\n\nFor the stable 0.0.6 version\n\npython -m pip install resistics\n\n## Support and feature requests\n\nFeel free to submit issues, feature requests or ideas for improvements in the\nGithub issues section.\n',
    'author': 'Neeraj Shah',
    'author_email': 'resistics@outlook.com',
    'maintainer': 'Neeraj Shah',
    'maintainer_email': 'resistics@outlook.com',
    'url': 'https://www.resistics.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.10',
}


setup(**setup_kwargs)
