#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tarfile
import argparse
import numpy as np
import pandas as pd
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
import joblib
import logging
from housing_price_pred.logger import configure_logger

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s"
            + "%(funcName)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

HOUSING_PATH = os.path.join(os.getcwd(),"data", "raw")
PROCESSED_PATH = os.path.join(os.getcwd(),"data", "processed")
PICKLE_PATH = os.path.join(os.getcwd(),'artifacts')

def preprocess_data(input_folder, processed_folder):
    # read train and test sets
    strat_train_set = pd.read_csv(os.path.join(input_folder,'train.csv'))
    strat_test_set = pd.read_csv(os.path.join(input_folder,'test.csv'))

    # prepare train set
    housing = strat_train_set.copy()
    housing = strat_train_set.drop("median_house_value", axis=1)  # drop labels for training set
    housing_labels = strat_train_set["median_house_value"].copy()
    imputer = SimpleImputer(strategy="median")
    housing_num = housing.drop("ocean_proximity", axis=1)
    imputer.fit(housing_num)
    X = imputer.transform(housing_num)
    housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
    housing_tr["rooms_per_household"] = (housing_tr["total_rooms"] / housing_tr["households"])
    housing_tr["bedrooms_per_room"] = (housing_tr["total_bedrooms"] / housing_tr["total_rooms"])
    housing_tr["population_per_household"] = (housing_tr["population"] / housing_tr["households"])
    housing_cat = housing[["ocean_proximity"]]
    housing_prepared = housing_tr.join(pd.get_dummies(housing_cat, drop_first=True))
    housing_prepared.to_csv(os.path.join(processed_folder,'train_processed.csv'),index=False)

    # prepare test set
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set[["median_house_value"]].copy()
    X_test_num = X_test.drop("ocean_proximity", axis=1)
    X_test_prepared = imputer.transform(X_test_num)
    X_test_prepared = pd.DataFrame(X_test_prepared, columns=X_test_num.columns, index=X_test.index)
    X_test_prepared["rooms_per_household"] = (X_test_prepared["total_rooms"] / X_test_prepared["households"])
    X_test_prepared["bedrooms_per_room"] = (X_test_prepared["total_bedrooms"] / X_test_prepared["total_rooms"])
    X_test_prepared["population_per_household"] = (X_test_prepared["population"] / X_test_prepared["households"])
    X_test_cat = X_test[["ocean_proximity"]]
    X_test_prepared = X_test_prepared.join(pd.get_dummies(X_test_cat, drop_first=True))
    X_test_prepared.to_csv(os.path.join(processed_folder,'test_processed.csv'),index=False)
    y_test.to_csv(os.path.join(processed_folder,'test_labels.csv'),index=False)
    return housing_prepared, housing_labels, X_test_prepared, y_test


def lin_reg(X_train, y_train, pickle_path):
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    pred = lin_reg.predict(X_train)
    lin_mse = mean_squared_error(y_train, pred)

    #lin_rmse
    lin_rmse = np.sqrt(lin_mse)
    #lin_mar
    lin_mae = mean_absolute_error(y_train, pred)
    # saving pickle file
    filename_lin_reg = 'lin_reg.pkl'
    joblib.dump(lin_reg, os.path.join(pickle_path,filename_lin_reg))
    return pred, lin_mse, lin_rmse, lin_mae

def tree_reg(X_train, y_train, pickle_path,random_state = 42):
    tree_reg = DecisionTreeRegressor(random_state= random_state)
    tree_reg.fit(X_train, y_train)
    pred = tree_reg.predict(X_train)
    tree_mse = mean_squared_error(y_train, pred)
    tree_rmse = np.sqrt(tree_mse)
    tree_mae = mean_absolute_error(y_train, pred)
    #tree_rmse
    filename_tree_reg = 'tree_reg.pkl'
    joblib.dump(tree_reg, os.path.join(pickle_path,filename_tree_reg))
    return pred, tree_mse, tree_rmse, tree_mae

def rf_hyperparameter_tuner(X_train, y_train, search_type, params, pickle_path, n_iter = 10, cv = 5, random_state = 42):
    forest_reg = RandomForestRegressor(random_state=random_state)
    if search_type == 'Randomized':
        logger.info('Search Type: Randomized')
        rnd_search = RandomizedSearchCV(
            forest_reg,
            param_distributions=params,
            n_iter=n_iter,
            cv=cv,
            scoring="neg_mean_squared_error",
            random_state=random_state,
            )
        rnd_search.fit(X_train, y_train)
        cvres = rnd_search.cv_results_
        for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
            logger.info(np.sqrt(-mean_score), params)
        final_model = rnd_search.best_estimator_
        filename = 'rnd_forest_reg.pkl'
        joblib.dump(final_model, os.path.join(pickle_path,filename))
    elif search_type=='Grid':
        logger.info('Search Type: Grid')
        grid_search = GridSearchCV(
            forest_reg,
            params,
            cv=cv,
            scoring="neg_mean_squared_error",
            return_train_score=True,
            )
        grid_search.fit(X_train, y_train)
        cvres = grid_search.cv_results_
        for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
            logger.info(np.sqrt(-mean_score), params)
        feature_importances = grid_search.best_estimator_.feature_importances_
        sorted(zip(feature_importances, X_train.columns), reverse=True)
        final_model = grid_search.best_estimator_
        filename = 'grd_forest_reg.pkl'
        joblib.dump(final_model, os.path.join(pickle_path,filename))
    else:
        print('Invalid search_type, please choose from {"Randomized","Grid"}')
    return cvres

def train_data(input_folder = HOUSING_PATH, processed_folder = PROCESSED_PATH, pickle_path = PICKLE_PATH, n_iter=10,cv=5,random_state=42):
    
    """Function to train data on various models such as Linear Regression, Decision Tree, Random Forest Tuned (Randomized and Grid Search)
    
    Parameters
    ----------
    input_folder: str, default "current_working_directory/data/raw"
                Path where the train and test data is stored.
                
    processed_folder: str, default "current_working_directory/data/processed"
                Path where preprocessed files (Intermediate) will be stored.
                
    pickle_path: str, default "current_working_directory/artifacts"
                Folder where trained models will be saved/stored.
                
    n_iter: int, default = 10
                Number of parameter settings that are sampled. n_iter trades off runtime vs quality of the solution.
                
    cv: int, default = 5
                cross-validation generator or an iterable.
                
    random_state: int, default = 42
    
    
    Returns
    -------
    None
    Function will pre-process train and test data, train various algorithms on train data and store the trained models in the specified folder.
    """
    os.makedirs(processed_folder, exist_ok=True)
    os.makedirs(pickle_path, exist_ok=True)
    try:
        housing_prepared, housing_labels, X_test_prepared, y_test = preprocess_data(input_folder=input_folder,
                                                                                    processed_folder=processed_folder)
        logger.info('Data processed successfuly')
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
    
    try:
        logger.info('Starting to train data using Linear Regression...')
        pred_lr, lin_mse, lin_rmse, lin_mae = lin_reg(X_train = housing_prepared, y_train = housing_labels,\
                                                        pickle_path = pickle_path)
        logger.info('RMSE - Linear Regression: {}'.format(lin_rmse))
        logger.info('MAE - Linear Regression: {}'.format(lin_mae))
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
    
    try:
        logger.info('Starting to train data using Decision Tree...')
        pred_dt, tree_mse, tree_rmse, tree_mae = tree_reg(X_train = housing_prepared, y_train = housing_labels,\
                                                            pickle_path = pickle_path)
        logger.info('RMSE - Decision Tree: {}'.format(tree_rmse))
        logger.info('MAE - Decision Tree: {}'.format(tree_mae))
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
    try:
        logger.info('Starting Randomized Search for tuning Random Forest model')
        param_distribs = {
            "n_estimators": randint(low=1, high=200),
            "max_features": randint(low=1, high=8)
        }
        cvres_rnd = rf_hyperparameter_tuner(X_train = housing_prepared, y_train = housing_labels, search_type = "Randomized",\
                                            params = param_distribs, n_iter = n_iter, cv = cv, pickle_path = pickle_path,\
                                            random_state = random_state)
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
        
    try:
        logger.info('Starting Grid Search for tuning Random Forest model')
        param_grid = [
            # try 12 (3×4) combinations of hyperparameters
            {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
#             # then try 6 (2×3) combinations with bootstrap set as False
            {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
        ]
        cvres_grid = rf_hyperparameter_tuner(X_train = housing_prepared, y_train = housing_labels, search_type = "Grid",\
                                               params = param_grid, n_iter = n_iter, cv = cv, pickle_path = pickle_path,\
                                               random_state = random_state)
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False

if __name__ == "__main__":
    HOUSING_PATH = os.path.join(os.getcwd(),"data", "raw")
    PROCESSED_PATH = os.path.join(os.getcwd(),"data", "processed")
    PICKLE_PATH = os.path.join(os.getcwd(),'artifacts')
    
    parser = argparse.ArgumentParser()
    log_levels = {
    'critical': 'CRITERIA',
    'error':'ERROR',
    'debug': 'DEBUG',
    'info': 'INFO',
    'warning': 'WARNING',
    }

    parser.add_argument('--input_path', help='Provide path to directory where train and test data is stored',default = HOUSING_PATH)
    parser.add_argument('--processed_path', help = 'Path where processed datasets will be stored',default = PROCESSED_PATH)
    parser.add_argument('--pickle_path', help = 'Directory to save model pkls', default = PICKLE_PATH)
    parser.add_argument('--log-level',dest='log_level',\
                        help="Specify the logging level. Choose from {'DEBUG','INFO','CRITICAL','WARNING','ERROR'},\
                        Default = INFO",default='info')
    parser.add_argument('--log-path',dest='log_path', help = 'Provide a path for logs to be stored', default = False)
    parser.add_argument('--no-console-log', dest = 'console_log',help = 'Whether logs will be printed in console or not', action ='store_false')
    parser.add_argument('--console-log', dest = 'console_log',help = 'Whether logs will be printed in console or not', action ='store_true')
    args = parser.parse_args()
    level = log_levels.get(args.log_level.lower())
    if level is None:
        raise ValueError(
            f"log level given: {args.log_level}"
            f" -- must be one of: {' | '.join(log_levels.keys())}"
            )
    logger = configure_logger(log_file=args.log_path, console=args.console_log, log_level=level)
    train_data(input_folder=args.input_path,processed_folder=args.processed_path,pickle_path=args.pickle_path)

