#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
import tarfile
import argparse
import numpy as np
import pandas as pd
import sys
import traceback
from scipy.stats import randint
from six.moves import urllib
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    StratifiedShuffleSplit,
    train_test_split,
)
from sklearn.tree import DecisionTreeRegressor
import logging
from housing_price_pred.logger import configure_logger

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s"
            + "%(funcName)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
HOUSING_PATH = os.path.join(os.getcwd(),"data", "raw")



def fetch_housing_data(housing_url, housing_path):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

# In[ ]:


def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)



# In[3]:
def create_train_test(housing,housing_path):
    housing["income_cat"] = pd.cut(
    housing["median_income"],
    bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
    labels=[1, 2, 3, 4, 5],
    )
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)
    strat_train_set.to_csv(os.path.join(housing_path,'train.csv'),index=False)
    strat_test_set.to_csv(os.path.join(housing_path,'test.csv'),index=False)
    return strat_train_set, strat_test_set


def download_data(housing_url=HOUSING_URL,housing_path=HOUSING_PATH):
    """Function to Download raw data, Create Train and Test sets
    
    Parameters
    ----------
    housing_url: str, default "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz"
                specifies the url for data download 

    housing_path: str, default "current_working_directory/data/raw"
                Folder/Path where downloaded data is stored
                
    Returns
    -------
    Downloaded data in pandas dataframe format
    Train Dataset
    Test Dataset
    
    Function will also write the returned dataframes into the folder specified under argument housing_path
    """
    
    try:
        fetch_housing_data(housing_url=housing_url, housing_path=housing_path)
        logger.info('Data will be stored at:'+args.outpath)
        logger.info('Data downloaded successfully!')
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
    try:
        housing = load_housing_data(housing_path=housing_path)
        logger.info('Data has {} rows and {} fields'.format(housing.shape[0],housing.shape[1]))
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
        
    try:
        strat_train_set, strat_test_set = create_train_test(housing=housing,housing_path=housing_path) 
        logger.info('Train and Test set created successfully!')
        logger.info('Train Data has {} rows'.format(strat_train_set.shape[0]))
        logger.info('Test Data has {} rows'.format(strat_test_set.shape[0]))
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
    return housing, strat_train_set, strat_test_set


if __name__ == "__main__":
    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
    HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
    HOUSING_PATH = os.path.join(os.getcwd(),"data", "raw")

    parser = argparse.ArgumentParser()
    log_levels = {
    'critical': 'CRITERIA',
    'error':'ERROR',
    'debug': 'DEBUG',
    'info': 'INFO',
    'warning': 'WARNING',
    }

    parser.add_argument('--outpath', help='Provide Output Directory',default = HOUSING_PATH)
    parser.add_argument('--log-level',dest='log_level',\
                        help="Specify the logging level. Choose from {'DEBUG','INFO','CRITICAL','WARNING','ERROR'},\
                        Default = INFO",default='info')
    parser.add_argument('--log-path',dest='log_path', help = 'Provide a path for logs to be stored', default = False)
    parser.add_argument('--no-console-log', dest = 'console_log',help = 'Logs will not be printed on Console', action ='store_false')
    parser.add_argument('--console-log', dest = 'console_log',help = 'Logs will be printed on Console', action ='store_true')
    args = parser.parse_args()
    level = log_levels.get(args.log_level.lower())
    if level is None:
        raise ValueError(
            f"log level given: {args.log_level}"
            f" -- must be one of: {' | '.join(log_levels.keys())}"
            )
    logger = configure_logger(log_file=args.log_path, console=args.console_log, log_level=level)
    housing, strat_train_set, strat_test_set = download_data(housing_url = HOUSING_URL, housing_path = args.outpath)




