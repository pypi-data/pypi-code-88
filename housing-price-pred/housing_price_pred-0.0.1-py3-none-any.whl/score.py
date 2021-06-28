#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

PROCESSED_PATH = os.path.join(os.getcwd(),"data", "processed")
PICKLE_PATH = os.path.join(os.getcwd(),'artifacts')
PRED_PATH = os.path.join(os.getcwd(),'Predictions')

def score_models(processed_folder = PROCESSED_PATH, pickle_path = PICKLE_PATH, output_path = PRED_PATH):
    """Function to score the trained models on Test Data
    
    Parameters
    ----------
    processed_folder: str, default "current_working_directory/data/processed"
                Path where preprocessed files (Intermediate) are stored.
                
    pickle_path: str, default "current_working_directory/artifacts"
                Path where trained models are saved/stored.
                
    output_path: str, default "current_working_directory/Predictions"
                Path where prediction is stored.
            
                
    Returns
    -------
    Predictions on test set from Trained Models.
    
    Function will load trained models, and score the models on test data.
    """
    os.makedirs(output_path, exist_ok=True)

    try:
        X_test_prepared = pd.read_csv(os.path.join(processed_folder,'test_processed.csv'))
        y_test_df = pd.read_csv(os.path.join(processed_folder,'test_labels.csv'))
        y_test = y_test_df["median_house_value"].copy()
        
        logger.info('Loading Models')
        lin_reg = joblib.load(os.path.join(pickle_path,'lin_reg.pkl'))
        tree_reg = joblib.load(os.path.join(pickle_path,'tree_reg.pkl'))
        rnd_forest_reg = joblib.load(os.path.join(pickle_path,'rnd_forest_reg.pkl'))
        grd_forest_reg = joblib.load(os.path.join(pickle_path,'grd_forest_reg.pkl'))

        lin_reg_predictions = lin_reg.predict(X_test_prepared)
        lin_reg_mse = mean_squared_error(y_test, lin_reg_predictions)
        lin_reg_rmse = np.sqrt(lin_reg_mse)

        logger.info('Linear Regression RMSE (Test Set): {}'.format(lin_reg_rmse))
        df_lin_reg = pd.DataFrame(lin_reg_predictions,columns=['Lin_Reg_Pred'])
        df_lin_reg.to_csv(os.path.join(output_path,'df_lin_reg.csv'),index=False)

        tree_reg_predictions = tree_reg.predict(X_test_prepared)
        tree_reg_mse = mean_squared_error(y_test, tree_reg_predictions)
        tree_reg_rmse = np.sqrt(tree_reg_mse)

        logger.info('Decision Tree Regression RMSE (Test Set): {}'.format(tree_reg_rmse))
        df_tree_reg = pd.DataFrame(tree_reg_predictions,columns=['DTree_Reg_Pred'])
        df_tree_reg.to_csv(os.path.join(output_path,'df_tree_reg.csv'),index=False)
        # In[ ]:


        rnd_forest_reg_predictions = rnd_forest_reg.predict(X_test_prepared)
        rnd_forest_reg_mse = mean_squared_error(y_test, rnd_forest_reg_predictions)
        rnd_forest_reg_rmse = np.sqrt(rnd_forest_reg_mse)

        logger.info('Random Forest Randomized Search RMSE (Test Set): {}'.format(rnd_forest_reg_rmse))
        df_rnd_forest_reg = pd.DataFrame(rnd_forest_reg_predictions,columns=['Randomized_RF_Reg_Pred'])
        df_rnd_forest_reg.to_csv(os.path.join(output_path,'df_rnd_forest_reg.csv'),index=False)
        # In[ ]:


        grd_forest_reg_predictions = grd_forest_reg.predict(X_test_prepared)
        grd_forest_reg_mse = mean_squared_error(y_test, grd_forest_reg_predictions)
        grd_forest_reg_rmse = np.sqrt(grd_forest_reg_mse)

        logger.info('Random Forest Grid Search RMSE (Test Set): {}'.format(grd_forest_reg_rmse))
        df_grd_forest_reg = pd.DataFrame(grd_forest_reg_predictions,columns=['Grid_RF_Reg_Pred'])
        df_grd_forest_reg.to_csv(os.path.join(output_path,'df_grd_forest_reg.csv'),index=False)
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False
    
    return lin_reg_predictions, tree_reg_predictions, rnd_forest_reg_predictions, grd_forest_reg_predictions


if __name__ == "__main__":
    PROCESSED_PATH = os.path.join(os.getcwd(),"data", "processed")
    PICKLE_PATH = os.path.join(os.getcwd(),'artifacts')
    PRED_PATH = os.path.join(os.getcwd(),'Predictions')
    parser = argparse.ArgumentParser()
    log_levels = {
    'critical': 'CRITERIA',
    'error':'ERROR',
    'debug': 'DEBUG',
    'info': 'INFO',
    'warning': 'WARNING',
    }

    parser.add_argument('--processed_path', help = 'Path where processed datasets will be stored',default = PROCESSED_PATH)
    parser.add_argument('--pickle_path', help = 'Directory to save model pkls', default = PICKLE_PATH)
    parser.add_argument('--pred_path', help = 'Saved Model Predictions', default = PRED_PATH)
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
    lr_predictions, tr_predictions, rnd_forest_predictions, grd_forest_predictions = score_models(processed_folder=\
                                                                                                  args.processed_path,\
                                                                                                  pickle_path=args.pickle_path,\
                                                                                                  output_path=args.pred_path
                                                                                                  )
