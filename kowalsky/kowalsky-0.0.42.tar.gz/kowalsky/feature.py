import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score
from kowalsky.logs.utils import LivePyPlot
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
from sklearn.metrics import get_scorer
from sklearn.base import clone
from .logs.loggers import get_logger
import numpy as np
import math


def calc_score(model, X, y, type='cv', scoring=None, cv=5):
    if type == 'cv':
        return abs(cross_val_score(model, X, y, scoring=scoring, cv=cv, n_jobs=-1, verbose=10).mean())
    elif type == 'test':
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        return abs(get_scorer(scoring)._score_func(y_test, preds))
    else:
        raise Exception(f'Wrong type: {type} (use cv/test)')


class XRFE(RFE):

    def __init__(self, estimator, n_features_to_select=None, step=1, logging=None, logging_params={}):
        self.estimator = estimator
        self.n_features_to_select = n_features_to_select
        self.step = step
        self.logger = get_logger(logging, 'XRFE', logging_params)

    def fit(self, X, y):
        n_features = X.shape[1]
        all_features = X.columns
        support_ = np.ones(n_features, dtype=bool)
        ranking_ = np.ones(n_features, dtype=int)

        while np.sum(support_) > self.n_features_to_select:
            features = np.arange(n_features)[support_]
            estimator = clone(self.estimator)

            self.logger("Training %d cols" % np.sum(support_))
            estimator.fit(X.iloc[:, features], y)
            importances = estimator.feature_importances_
            ranks = np.argsort(importances)
            ranks = np.ravel(ranks)

            # Eliminate the worse features
            threshold = min(self.step, np.sum(support_) - self.n_features_to_select)

            support_[features[ranks][:threshold]] = False
            ranking_[np.logical_not(support_)] += 1

        features = np.arange(n_features)[support_]
        self.estimator_ = clone(self.estimator)
        self.estimator_.fit(X.loc[:, all_features[features]], y)
        self.n_features_ = support_.sum()
        self.support_ = support_
        self.ranking_ = ranking_

        self.logger('Support: ', support_)
        self.logger('Ranking: ', ranking_)
        return self


class XRFECV(RFE):

    def __init__(self, estimator, n_features_to_select=None, step=1, scorer=None, logging=None, logging_params={}):
        self.estimator = estimator
        self.n_features_to_select = n_features_to_select
        self.step = step
        self.scorer = scorer
        self.logger = get_logger(logging, 'XRFECV', logging_params)

    def fit(self, X, y):
        n_features = X.shape[1]
        all_features = X.columns
        support_ = np.ones(n_features, dtype=bool)
        ranking_ = np.ones(n_features, dtype=int)
        self.scores = []

        while np.sum(support_) > self.n_features_to_select:
            features = np.arange(n_features)[support_]
            estimator = clone(self.estimator)

            self.logger("Training %d cols" % np.sum(support_))
            estimator.fit(X.iloc[:, features], y)
            importances = estimator.feature_importances_
            ranks = np.argsort(importances)
            ranks = np.ravel(ranks)

            # Eliminate the worse features
            threshold = min(self.step, np.sum(support_) - self.n_features_to_select)

            support_[features[ranks][:threshold]] = False
            ranking_[np.logical_not(support_)] += 1

            if self.scorer is not None:
                res = cross_val_score(estimator, X.iloc[:, features], y, n_jobs=-1)
                self.scores.append(res)
                self.logger(f"Scores: {np.mean(res)}")

        features = np.arange(n_features)[support_]
        self.estimator_ = clone(self.estimator)
        self.estimator_.fit(X.loc[:, all_features[features]], y)
        self.n_features_ = support_.sum()
        self.support_ = support_
        self.ranking_ = ranking_

        self.logger('Support: ', support_)
        self.logger('Ranking: ', ranking_)
        return self


def rfe_analysis(model, y_column, scoring, direction, cv=3, ranking=None, path=None, ds=None,
                 sample_size=None, n_features_to_select=5, precision=1e-3, stratify=False, eval_type='cv',
                 logging=None, logging_params={}):

    logger = get_logger(logging, 'feature_analysis', logging_params)

    if ds is None:
        ds = pd.read_csv(path)

    if sample_size is not None:
        ds, _ = train_test_split(ds, train_size=sample_size, stratify=ds[y_column] if stratify else None)

    X, y = ds.drop(y_column, axis=1), ds[y_column]

    if ranking is None:
        rfe = RFE(model, step=1, verbose=10, n_features_to_select=n_features_to_select)
        try:
            rfe.fit(X, y)
        except KeyboardInterrupt:
            logger("Stopped with keyboard")
            return
        ranking = rfe.ranking_
    else:
        ranking = np.array(ranking)

    logger(pd.DataFrame({
        'column': X.columns,
        'ranking': ranking
    }).sort_values(by='ranking').values)

    live = LivePyPlot(direction=direction, show_true_value=True)

    best_score = -math.inf if direction == 'maximize' else math.inf
    best_columns = None

    try:
        for rank in range(1, np.max(ranking) + 1):
            rank_columns = X.columns[ranking <= rank]
            score = calc_score(model, X[rank_columns], y, type=eval_type, cv=cv, scoring=scoring)
            live(score, sum(ranking <= rank))
            logger(score, sum(ranking <= rank))

            is_better_score = score > best_score + precision if direction == 'maximize' else score < best_score - precision
            if is_better_score:
                best_score = score
                best_columns = ranking <= rank
    except KeyboardInterrupt:
        logger("Stopped with keyboard")

    live.clear()

    logger('Best score', best_score)
    logger('Best columns', best_columns)
    logger('Ranking', ranking)
    return best_columns, ranking


def sfs_analysis(model, y_label, scoring, k_features, cv=3, forward=True, floating=False, path=None,
                 sample_size=None, stratify=False, ds=None, logging=None, logging_params={}):

    logger = get_logger(logging, 'sfs_feature_analysis', logging_params)

    if ds is None:
        ds = pd.read_csv(path)

    if sample_size is not None:
        ds, _ = train_test_split(ds, train_size=sample_size, stratify=ds[y_label] if stratify else None)

    X, y = ds.drop(y_label, axis=1), ds[y_label]

    selector = SFS(model, forward=forward, floating=floating, verbose=10,
                   scoring=scoring, cv=cv, n_jobs=-1, k_features=k_features)
    try:
        selector.fit(X, y)
    except KeyboardInterrupt:
        print("Stopped with keyboard")

    plot_sfs(selector.get_metric_dict(), kind='std_dev')

    plt.grid()
    plt.show()

    logger(selector.get_metric_dict())

    return selector.get_metric_dict()
