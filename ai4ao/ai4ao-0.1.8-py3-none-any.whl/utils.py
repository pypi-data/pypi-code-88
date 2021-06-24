import os
import copy
import yaml
import logging

import numpy as np
from numpy.random import randint

import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import filters
from scipy.signal import savgol_filter, wiener, filtfilt, butter, gaussian, freqz


def read_config_file(path_config):
    """This functions reads the configurations from the **configuration yaml** file 
    and seggregates the configuration marked as **run**.
    
    Parameters
    ----------
    path_config: str

    Returns:
    -------
    configs: dict
    a_list: list
    """

    with open(path_config) as file_config:
        configs = yaml.load(file_config, Loader=yaml.FullLoader)
    return configs, [key for key, val in configs.items() if val['run_this_project']]


def get_data(config, data_type='train'):
    """This function reads both the training and the testing data
    
    Parameters
    ----------
    config: dict
    data_type: str, default=train

    Returns:
    -------
    raw_data: pd.DataFrame
    """

    if data_type == 'train':
        raw_data = pd.read_csv(config['data']['path'], delimiter=";")
    else:
        raw_data = pd.read_csv(config['data']['test_data_path'], delimiter=";")
    feats_to_avoid = config['data']['features_to_avoid']

    if len(feats_to_avoid) is not None:
        for feat_name in feats_to_avoid:
            try:
                raw_data.drop([feat_name], axis=1, inplace=True)
            except KeyError as e:
                logging.warning(" Column {} (which is to be dropped) doesn't exist in {}".format(
                    feat_name, config['data']['test_data_path']))
    return raw_data
    




