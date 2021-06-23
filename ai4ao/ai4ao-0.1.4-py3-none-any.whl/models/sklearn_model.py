import os
import copy
import yaml
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor

from ai4ao.models.models import BaseModel
from ai4ao.utils import read_config_file, get_data

from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import accuracy_score as ascore
from sklearn.metrics import f1_score as fscore
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

"""This is a wrapper for using scikit-learn based
    models! One can extend this to any relevant scikit-learn
    model by simply importing the algorithm from sklearn!"""

class SKLearnModel(BaseModel):
    """This is the class which is used to build **scikit-learn models**. 

    Attributes
    ----------
    plot_results: bool, default=True

    Methods
    -------
    fit:
    predict:
    batch_fit:
    metrics:
    """
    def __init__(self, plot_results=False):
        """This is the constructor of the **SKLearnModel**.

        Parameters
        ----------
        plot_results: bool, default=True
        """
        super(SKLearnModel, self).__init__(plot_results)
        self.models = None
        self.configs = None
        self.configs_ran = None
        self.model_errs = {'train': dict(),'test': pd.DataFrame}

    def fit(self):
        """This is the SKLearnModel **single model fit**. This is to be implemented"""
        pass

    def predict(self):
        """This is the SKLearnModel **single model predict**. This is to be implemented"""
        pass

    def metrics(self):
        """This returns the **metrics** of all the models"""
        return self.model_errs

    def batch_fit(self, path_config):
        """This function allows one to build many models in one go"""
        configs, configs_to_run = read_config_file(path_config)
        self.configs = configs
        self.configs_ran = configs_to_run

        logging.debug("======================================")
        logging.debug("[Model]: Projects to be run: \n {}".format(configs_to_run))
        logging.debug("[Model]: Corresponding Configurations: \n {}".format(configs))
        logging.debug("======================================")

        self.models = self.__run_configs(configs, configs_to_run)

        if self.plot_results:
            self.__plot_in_out_liers(configs, configs_to_run, self.models)

    def __run_configs(self, configs, configs_to_run):
        """This function actually loops over each configuration to fit the corresponding model"""
        models_trained = dict()
        for config_name in configs_to_run:
            data_raw = get_data(configs[config_name], data_type='train')

            if configs[config_name]['multi_variate_model']:
                models_trained[config_name], model_err = self.__fit_model(configs[config_name], data_raw.values)
                # self.model_errs['train'][config_name] = {'all_feats': model_err}
            else:
                model_errs = dict()
                models_univar_trained = dict()
                for feat_name in data_raw.columns:
                    models_univar_trained[feat_name], model_errs[feat_name] = self.__fit_model(configs[config_name], data_raw[feat_name].values)
                models_trained[config_name] = models_univar_trained
                # self.model_errs['train'][config_name] = model_errs
        return models_trained

    def __fit_model(self, metadata, data_train):
        """This function is actually responsible fot **fitting** the model"""
        eval_string = str(metadata['model']) + '('
        if metadata['hyperparams'] is not None:
            for param in metadata['hyperparams']:
                eval_string += str(param) + "=" + str(metadata['hyperparams'][param])
                if len(metadata['hyperparams']) > 1:
                    eval_string += ","
        eval_string += ')'

        model = eval(eval_string)
        if len(data_train.shape) <= 1:
            data_train = data_train.reshape(-1, 1)
        model.fit(data_train)
        return model, 0
        # , mse(data_train, model.predict(copy.deepcopy(data_train)))

    def __plot_in_out_liers(self, configs, configs_ran, models_trained):
        """This function **plots the inlier and outlier** data resulting from anomaly/outlier detection"""
        for config_name in configs_ran:
            data_train = get_data(configs[config_name], data_type='train')
            data_test = get_data(configs[config_name], data_type='test')

            plots_path = os.path.join(configs[config_name]['results']['path'], 'plots')
            os.makedirs(plots_path, exist_ok=True)

            legend = ['train:inliers', 'train:outliers', 'test:inliers', 'test:outliers']
            for feat_name in data_train.columns:
                model_retrieved = models_trained[config_name]

                data_to_infer_train = copy.deepcopy(data_train.values)
                data_to_infer_test = copy.deepcopy(data_test.values)

                if type(model_retrieved) == dict:
                    model_retrieved = models_trained[config_name][feat_name]
                    data_to_infer_train = copy.deepcopy(data_train[feat_name].values)
                    data_to_infer_test = copy.deepcopy(data_test[feat_name].values)

                if len(data_to_infer_train.shape) <= 1:
                    data_to_infer_train = data_to_infer_train.reshape(-1, 1)

                if len(data_to_infer_test.shape) <= 1:
                    data_to_infer_test = data_to_infer_test.reshape(-1, 1)

                infers_train_data = model_retrieved.predict(data_to_infer_train)
                infers_test_data = model_retrieved.predict(data_to_infer_test)
                inliers_train_data = data_train[feat_name].loc[infers_train_data == 1]
                outliers_train_data = data_train[feat_name].loc[infers_train_data == -1]
                inliers_test_data = data_test[feat_name].loc[infers_test_data == 1]
                outliers_test_data = data_test[feat_name].loc[infers_test_data == -1]

                fig, ax = plt.subplots(figsize=(10, 7))
                plt.plot(inliers_train_data.index, inliers_train_data, 'o')
                plt.plot(outliers_train_data.index, outliers_train_data, '+')
                plt.plot(inliers_test_data.index, inliers_test_data, '^')
                plt.plot(outliers_test_data.index, outliers_test_data, '*')
                plt.grid(which="both")
                plt.ticklabel_format(axis='y', style='plain')
                plt.legend(legend, loc="upper left")
                plt.xlabel('Sample')
                plt.ylabel(feat_name)
                plt.savefig(os.path.join(plots_path, config_name + '_' + feat_name + ".png"))
                plt.close()
