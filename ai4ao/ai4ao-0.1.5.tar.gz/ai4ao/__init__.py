"""**AI for Anomaly and Outlier detection (AI4AO)*** is package that can help you to execute any of the sciki-learn supported
anomaly and outlier detection algorithms in batches. AI4AO uses *yaml* style declarative configuration file in which the various 
algorithms and their applicable hyper-parameters are specified. 

Main Features
-------------

Here are just a few of the things that AI4AO does well:

    - template: it helps you declaratively specify the (scikit-learn) algorithm and its hyper-parameters to run.
    - a config in template: it helps you control whether to run a defined configuration or not.
    - batch run: allows you to run multiple models (in sequence) with a single template


Example
-------

::
# configs.yaml
IsolationForest_0.01:
  project_name: iso_anomaly
  run_this_project: True
  multi_variate_model: True
  model: IsolationForest
  data:
    path: 'data/data_train.csv'
    test_data_path: 'data/data_test.csv'
    features_to_avoid: ['feat_to_avoid']
  hyperparams:
    contamination: 0.01
  results:
    path: 'results/iso_anomaly/'
  remote_run: False



>>> import ai4ao
>>> from ai4ao import SKLearnModel
"""

from ai4ao import models

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = '0.1.5'

