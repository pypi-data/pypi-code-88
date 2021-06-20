"""A module for pre/postprocessing dates
"""

import numpy as np
import pandas as pd
import datetime
from pyhere import here
from pathlib import Path


from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import check_random_state
from sklearn.utils.validation import check_array, check_is_fitted, FLOAT_DTYPES
from sklearn.preprocessing import KBinsDiscretizer

class GeneralizeContinuous(KBinsDiscretizer):

    def __init__(self, n_bins=10, strategy='uniform', labeled_missing=None):
        super().__init__(n_bins=n_bins, strategy=strategy, encode='ordinal')
        self.labeled_missing = labeled_missing

    def fit(self, X, y=None):
        self._infer_numerical_type(X)
        self.feature_names = X.columns
        self.missing_indeces =
        super().fit(X, y)
        return self

    def transform(self, X):

        super().transform(X)

    def _infer_numerical_type(self, X):
        """Determine if numerical column is an integer of float for inverse transform"""
        assert X.select_dtypes(exclude=['int', 'float']).shape[1] == 0, "input X contains non-numeric columns"
        self.integer_columns = []
        self.float_columns = []

        for c in X.columns:
            if np.array_equal(X[c].dropna(), X[c].dropna().astype(int)):
                self.integer_columns.append(c)
            else:
                self.float_columns.append(c)

    def _get_missing_idx(self, column):

        missing_idx = np.isnan(column) | np.isin(column, self.labeled_missing)


    def inverse_transform(self, Xt):
        # check_is_fitted(self)

        if 'onehot' in self.encode:
            Xt = self._encoder.inverse_transform(Xt)

        # Xinv = check_array(Xt, copy=True, dtype=FLOAT_DTYPES)
        Xinv = Xt.copy()
        n_features = self.n_bins_.shape[0]
        if Xinv.shape[1] != n_features:
            raise ValueError("Incorrect number of features. Expecting {}, "
                             "received {}.".format(n_features, Xinv.shape[1]))

        for jj in range(n_features):
            bin_edges = self.bin_edges_[jj]
            lower_bounds = bin_edges[np.int_(Xinv[:, jj])]
            upper_bounds = bin_edges[np.int_(Xinv[:, jj]) + 1]
            Xinv[:, jj] = np.random.uniform(lower_bounds, upper_bounds)

            # todo transfer to numpy
            if self.feature_names[jj] in self.integer_columns:
                Xinv[:, jj] = np.round(Xinv[:, jj])

        return Xinv


if __name__ == '__main__':
    data_path = Path("c:/data/1_iknl/processed/bente/cc_9col.csv")
    X = pd.read_csv(data_path)
    columns = ['tum_topo_sublokalisatie_code', 'tum_differentiatiegraad_code', 'tum_lymfklieren_positief_atl']
    columns = ['tum_lymfklieren_positief_atl']
    X = X.loc[:, columns]
    print(X.head(20))

    gen_cont = GeneralizeContinuous(n_bins=10, strategy='quantile')
    X = X.dropna()

    gen_cont.fit(X)
    X_cat = gen_cont.transform(X)
    print(X_cat)

    X_inv = gen_cont.inverse_transform(X_cat)
    print(X_inv)
    print(gen_cont.bin_edges_)