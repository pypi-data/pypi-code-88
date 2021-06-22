# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tsflex',
 'tsflex.chunking',
 'tsflex.features',
 'tsflex.pipeline',
 'tsflex.processing',
 'tsflex.utils']

package_data = \
{'': ['*']}

install_requires = \
['dill>=0.3.3,<0.4.0',
 'fastparquet>=0.6.3,<0.7.0',
 'numpy>=1.19.0,<2.0.0',
 'pandas>=1.2.3,<2.0.0',
 'pathos>=0.2.7,<0.3.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'tqdm>=4.60.0,<5.0.0']

setup_kwargs = {
    'name': 'tsflex',
    'version': '0.1.1.5',
    'description': 'Toolkit for flexible processing & feature extraction on time-series data',
    'long_description': '# <p align="center"> <a href="https://predict-idlab.github.io/tsflex"><img alt="tsflex" src="https://raw.githubusercontent.com/predict-idlab/tsflex/main/docs/_static/logo.png" height="100"></a></p>\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/tsflex.svg)](https://pypi.org/project/tsflex/)\n[![Documentation](https://github.com/predict-idlab/tsflex/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/predict-idlab/tsflex/actions/workflows/deploy-docs.yml)\n[![Testing](https://github.com/predict-idlab/tsflex/actions/workflows/test.yml/badge.svg)](https://github.com/predict-idlab/tsflex/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/predict-idlab/tsflex/branch/main/graph/badge.svg)](https://codecov.io/gh/predict-idlab/tsflex)\n[![Code quality](https://img.shields.io/lgtm/grade/python/g/predict-idlab/tsflex.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/predict-idlab/tsflex/context:python)\n[![Downloads](https://pepy.tech/badge/tsflex)](https://pepy.tech/project/tsflex)\n\n*tsflex* stands for: _**flex**ible **t**ime-**s**eries operations_<br>\n\nIt is a `time-series first` toolkit for **processing & feature extraction**, making few assumptions about input data. \n\n#### Useful links\n\n- [Documentation](https://predict-idlab.github.io/tsflex/)\n- [Example notebooks](https://github.com/predict-idlab/tsflex/tree/main/examples)\n\n## Installation\n\nIf you are using [**pip**](https://pypi.org/project/tsflex/), just execute the following command:\n\n```sh\npip install tsflex\n```\n\n## Usage\n\n_tsflex_ is built to be intuitive, so we encourage you to copy-paste this code and toy with some parameters!\n\n\n### <a href="https://predict-idlab.github.io/tsflex/processing/#getting-started">Series processing</a>\n\n```python\nimport pandas as pd; import scipy.signal as ssig; import numpy as np\nfrom tsflex.processing import SeriesProcessor, SeriesPipeline\n\n# 1. -------- Get your time-indexed data --------\n# Data contains 3 columns; ["ACC_x", "ACC_y", "ACC_z"]\nurl = "https://github.com/predict-idlab/tsflex/raw/main/examples/data/empatica/acc.parquet"\ndata = pd.read_parquet(url).set_index("timestamp")\n\n# 2 -------- Construct your processing pipeline --------\nprocessing_pipe = SeriesPipeline(\n    processors=[\n        SeriesProcessor(function=np.abs, series_names=["ACC_x", "ACC_y", "ACC_z"]),\n        SeriesProcessor(ssig.medfilt, ["ACC_x", "ACC_y", "ACC_z"], kernel_size=5)  # (with kwargs!)\n    ]\n)\n# -- 2.1. Append processing steps to your processing pipeline\nprocessing_pipe.append(SeriesProcessor(ssig.detrend, ["ACC_x", "ACC_y", "ACC_z"]))\n\n# 3 -------- Process the data --------\nprocessing_pipe.process(data=data)\n```\n\n### <a href="https://predict-idlab.github.io/tsflex/features/#getting-started">Feature extraction</a>\n\n```python\nimport pandas as pd; import scipy.stats as ssig; import numpy as np\nfrom tsflex.features import FeatureDescriptor, FeatureCollection, NumpyFuncWrapper\n\n# 1. -------- Get your time-indexed data --------\n# Data contains 1 column; ["TMP"]\nurl = "https://github.com/predict-idlab/tsflex/raw/main/examples/data/empatica/tmp.parquet"\ndata = pd.read_parquet(url).set_index("timestamp")\n\n# 2 -------- Construct your feature collection --------\nfc = FeatureCollection(\n    feature_descriptors=[\n        FeatureDescriptor(\n            function=NumpyFuncWrapper(func=ssig.skew, output_names="skew"),\n            series_name="TMP", \n            window="5min",  # Use 5 minutes \n            stride="2.5min",  # With steps of 2.5 minutes\n        )\n    ]\n)\n# -- 2.1. Add features to your feature collection\nfc.add(FeatureDescriptor(np.min, "TMP", \'2.5min\', \'2.5min\'))\n\n# 3 -------- Calculate features --------\nfc.calculate(data=data)\n```\n\n### Scikit-learn integration\n\n`TODO`\n\n<br>\n\n---\n\n<p align="center">\n👤 <i>Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost</i>\n</p>\n\n\n',
    'author': 'Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/predict-idlab/tsflex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
