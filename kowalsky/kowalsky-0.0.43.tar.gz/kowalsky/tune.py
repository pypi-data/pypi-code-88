import optuna
from lightgbm import LGBMRegressor
from lightgbm import LGBMClassifier
from xgboost import XGBRegressor
from xgboost import XGBClassifier
from optuna.samplers import TPESampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from catboost import CatBoostRegressor
from sklearn.metrics import get_scorer
from kowalsky.logs.utils import LivePyPlot
from .logs.loggers import get_logger
from .model import EarlyStopping
from .model import EarlyStoppingError
import numpy as np
from .df import read_dataset

family_params = {
    'hgb': {
        'learning_rate': ('uniform', 0.0001, 2),
        'max_iter': ('uniform', 50, 3000),
        'max_depth': ('int', 1, 25),
        'max_bins': ('int', 10, 400),
        'max_leaf_nodes': ('int', 10, 60),
        'min_samples_leaf': ('uniform', 0.00001, 0.5),
        'l2_regularization': ('uniform', 0., 20.)
    },
    'gb': {
        'learning_rate': ('uniform', 0.0001, 2),
        'n_estimators': ('int', 1, 600),
        'max_depth': ('int', 1, 25),
        'min_samples_split': ('uniform', 0.00001, 0.5),
        'min_samples_leaf': ('uniform', 0.00001, 0.5),
        'max_features': ('categorical', ['log2', 'sqrt']),
        'criterion': ('categorical', ['friedman_mse', 'mae']),
        'subsample': ('uniform', 0.3, 1.0)
    },
    'lgb': {
        'learning_rate': ('uniform', 0.0001, 1),
        'n_estimators': ('int', 1, 6200),
        'max_depth': ('int', 1, 25),
        'num_leaves': ('int', 2, 3000),
        'min_child_samples': ('int', 3, 200),
        'max_bin': ('int', 10, 255),
        'lambda_l1': ('uniform', 0, 10),
        'lambda_l2': ('uniform', 0, 10),
        'max_cat_threshold': ('int', 1, 60),
        'min_gain_to_split': ('uniform', 0, 10),
        'min_data_in_leaf': ('int', 5, 60)
    },
    'dt': {
        'max_depth': ('int', 2, 25),
        'min_samples_split': ('int', 2, 20),
        'min_weight_fraction_leaf': ('uniform', 0.0, 0.5),
        'min_samples_leaf': ('int', 1, 15)
    },
    'xgb': {
        'learning_rate': ('uniform', 0.0000001, 1),
        'n_estimators': ('int', 2, 1000),
        'max_depth': ('int', 2, 25),
        'gamma': ('uniform', 0.0000001, 20),
        'alpha': ('uniform', 0, 20),
        'colsample_bytree': ('uniform', 0.3, 1),
        'lambda': ('uniform', 0, 10),
        'max_delta_step': ('uniform', 0, 20),
        'min_child_weight': ('uniform', 0, 20),
        'subsample': ('uniform', 0.2, 1)
    },
    'rf': {
        'min_samples_leaf': ('int', 1, 15),
        'min_samples_split': ('uniform', 0.05, 1.0),
        'n_estimators': ('int', 2, 800),
        'max_depth': ('int', 2, 25),
        'random_state': 666
    },
    'et': {
        'min_samples_leaf': ('int', 1, 15),
        'min_samples_split': ('uniform', 0.05, 1.0),
        'max_depth': ('int', 2, 25),
        'random_state': 666
    },
    'bagg': {
        'n_estimators': ('int', 2, 300),
        'max_samples': ('int', 1, 400),
        'random_state': 666
    },
    'kn': {
        'n_neighbors': ('int', 2, 100)
    },
    'ada': {
        'n_estimators': ('int', 2, 800),
        'learning_rate': ('uniform', 0.0001, 1.0)
    },
    'svm': {
        'kernel': ('categorical', ['linear', 'poly']),
        'tol': ('uniform', 1e-5, 1),
        'C': ('loguniform', 1e-10, 1e10)
    },
    'cb': {
        'learning_rate': ('uniform', 0.0001, 1.0),
        'depth': ('int', 1, 16),
        'iterations': ('int', 100, 2000),
        'l2_leaf_reg': ('uniform', 0, 10),
        'border_count': ('int', 1, 148),
        'subsample': ('uniform', 0.3, 1),
    }
}

models = {

    # Gradient Boosts
    'xgbR': (XGBRegressor, 'xgb'),
    'xgbC': (XGBClassifier, 'xgb'),
    'lgbR': (LGBMRegressor, 'lgb'),
    'lgbC': (LGBMClassifier, 'lgb'),

    # Trees
    'rfR': (RandomForestRegressor, 'rf'),
    'rfC': (RandomForestClassifier, 'rf'),
    'dtR': (DecisionTreeRegressor, 'dt'),
    'dtC': (DecisionTreeClassifier, 'dt'),
    'etR': (ExtraTreeRegressor, 'et'),
    'etC': (ExtraTreeClassifier, 'et'),

    # Ensemble
    'baggC': (BaggingClassifier, 'bagg'),
    'baggR': (BaggingRegressor, 'bagg'),
    'adaR': (AdaBoostRegressor, 'ada'),
    'adaC': (AdaBoostClassifier, 'ada'),
    'cbR': (CatBoostRegressor, 'cb'),
    'cbC': (CatBoostClassifier, 'cb'),

    # KNeighbors
    'knC': (KNeighborsClassifier, 'kn'),
    'knR': (KNeighborsRegressor, 'kn'),

    # SVM
    'svR': (SVR, 'svm'),
    'svC': (SVC, 'svm'),
}


def get_meta_info(model_init, scorer, X_train, y_train, X_val, y_val, callbacks=()):
    def objective(params):
        model = model_init(**params)
        model.fit(X_train, y_train)
        preds = model.predict(X_val)
        error = get_scorer(scorer)._score_func(y_val, preds)
        for callback in callbacks:
            callback(error, params)
        print(error, scorer)
        return error

    return objective


def optimize(model_name, scorer, y_column, trials=30, tuner='optuna', feature_selection_support=None,
             feature_selection_cols=None, ds=None, path=None, sample_size=None, stratify=True,
             custom_params={}, ignore=[], n_jobs=-1, logging=None, logging_params={},
             early_stopping=False, patience=100, threshold=1e-3, show_live=True, X_y_train_val=None):
    if X_y_train_val is None:
        X_ds, y_ds = read_dataset(ds, path, y_column, feature_selection_support, feature_selection_cols, ignore,
                                  sample_size, stratify)

        X_train, X_val, y_train, y_val = train_test_split(X_ds, y_ds)
    else:
        X_train, X_val, y_train, y_val = X_y_train_val

    model_init, family = models[model_name]
    custom_params.update(family_params[family])

    callbacks = []
    logger = get_logger(logging, 'feature_analysis', logging_params)
    callbacks.append(lambda error, params: logger(error, params))
    if show_live:
        live = LivePyPlot('maximize')
        callbacks.append(lambda error, params: live(error))
    if early_stopping:
        stopping = EarlyStopping('maximize', patience, threshold)
        callbacks.append(lambda error, params: stopping(error))

    tuner = get_tuner(tuner, get_meta_info(model_init, scorer, X_train, y_train, X_val, y_val, callbacks),
                      custom_params)
    try:
        tuner.tune(trials, n_jobs)
    except KeyboardInterrupt:
        logger("Stopped with keyboard")
    except EarlyStoppingError:
        logger("Stopped with early stopping")

    logger(tuner.best_score, tuner.best_params)

    return tuner.best_score, tuner.best_params


def get_tuner(tuner, *params):
    if tuner == 'optuna':
        return OptunaTuner(*params)
    else:
        return RandomSearchTuner(*params)


class Tuner():

    def __init__(self, objective, params_setup):
        self.objective = objective
        self.params_setup = params_setup

    def tune(self, trials, n_jobs=-1):
        pass


class OptunaTuner(Tuner):

    def __init__(self, objective, params_setup, sampler=TPESampler(seed=666)):
        super(OptunaTuner, self).__init__(objective, params_setup)
        self.study = optuna.create_study(direction='maximize', sampler=sampler)
        optuna.logging.set_verbosity(optuna.logging.ERROR)

    def _save_result(self):
        self.best_params = self.study.best_params
        self.best_score = self.study.best_value

    def tune(self, trials, n_jobs=-1):
        def optuna_objective(trial):
            params = {col: values[0] if len(values) == 1 else getattr(trial, f'suggest_{values[0]}')(col, *values[1:])
                      for col, values in self.params_setup.items()}
            error = self.objective(params)
            return error

        try:
            self.study.optimize(optuna_objective, n_trials=trials, n_jobs=n_jobs)
        except Exception as e:
            self._save_result()
            raise e
        self._save_result()


class RandomSearchTuner(Tuner):

    def _get_random_attr(self, config):
        type, *params = config
        if type == 'int':
            return np.random.randint(params[0], params[1])
        elif type == 'uniform':
            return np.random.random() * (params[1] - params[0]) + params[0]
        elif type == 'categorical':
            return np.random.choice(params[0])
        return None

    def tune(self, trials, n_jobs=-1):
        self.best_params = {attr: self._get_random_attr(attr_config) for attr, attr_config in self.params_setup.items()}
        self.best_score = -np.inf

        for trial in range(trials):
            params = {attr: self._get_random_attr(attr_config) for attr, attr_config in self.params_setup.items()}
            score = self.objective(params)
            if score > self.best_score:
                self.best_params, self.best_score = params, score
