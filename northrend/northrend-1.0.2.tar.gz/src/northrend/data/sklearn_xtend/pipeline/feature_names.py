import warnings
import inspect

from sklearn.base import BaseEstimator, TransformerMixin

import sklearn
import pandas as pd
import scipy
import numpy as np


class PersistFeatureNames(BaseEstimator, TransformerMixin):
    def __init__(self, prefix=""):
        self.prefix = prefix

    def fit(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            self.feature_names = X.add_prefix(self.prefix).columns
        else:
            self.feature_names = pd.DataFrame(data=X).add_prefix(self.prefix).columns

    def transform(self, X):
        if isinstance(X, pd.DataFrame):
            return X.add_prefix(self.prefix)
        else:
            return pd.DataFrame(data=X, columns=self.feature_names)

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)

    def get_feature_names(self):
        return self.feature_names


def FeatureNamesAsPandasCols(model, name=None):
    class _AppendFeatureNamesAsPandasCols(BaseEstimator, TransformerMixin):
        def __init__(self, model, name):
            self.model = model
            if name is None:
                self.name = model.__class__.__name__
            else:
                self.name = name
            self.feature_names = None

        def fit(self, X, y=None):
            return self.model.fit(X, y)

        def transform(self, X):
            data = self.model.transform(X)
            self.feature_names = self.extract_feature_names(X)
            return pd.DataFrame(data=data, columns=self.feature_names)

        def fit_transform(self, X, y=None):
            self.fit(X, y)
            return self.transform(X)

        def get_feature_names(self):
            return self.feature_names

        def __repr__(self):
            return self.name

    class FeatureGeneratorWrapper(_AppendFeatureNamesAsPandasCols):
        def transform(self, X):
            data = self.model.transform(X)
            self.feature_names = self.extract_feature_names(X)
            if scipy.sparse.issparse(data):
                df = pd.DataFrame.sparse.from_spmatrix(
                    data=data, columns=self.feature_names
                )
            else:
                df = pd.DataFrame(data=data, columns=self.feature_names)
            return df

        def extract_feature_names(self, X):
            """Extracts the feature names from arbitrary sklearn models

            Args:
            model: The Sklearn model, transformer, clustering algorithm, etc. which we want to get named features for.
            name: The name of the current step in the pipeline we are at.

            Returns:
            The list of feature names.  If the model does not have named features it constructs feature names
            by appending an index to the provided name.
            """
            model = self.model
            name = self.name

            if hasattr(model, "get_feature_names"):
                fn = model.get_feature_names
                if len(inspect.getargspec(fn).args) == 1:
                    feature_names = fn()
                else:
                    feature_names = fn(X.columns)
                self.feature_names = [f"{name}__{feature}" for feature in feature_names]
                return self.feature_names
            elif hasattr(model, "n_clusters"):
                self.feature_names = [f"{name}__{x}" for x in range(model.n_clusters)]
                return self.feature_names
            elif hasattr(model, "n_components"):
                self.feature_names = [f"{name}__{x}" for x in range(model.n_components)]
                return self.feature_names
            elif hasattr(model, "components_"):
                n_components = model.components_.shape[0]
                self.feature_names = [f"{name}__{x}" for x in range(n_components)]
                return self.feature_names
            elif hasattr(model, "classes_"):
                self.feature_names = [f"{name}__{_class}" for _class in model.classes_]
                return self.feature_names
            else:
                self.feature_names = [name]
                return self.feature_names

    class TransformerWrapper(_AppendFeatureNamesAsPandasCols):
        def extract_feature_names(self, X):
            if isinstance(X, pd.DataFrame):
                self.feature_names = X.add_suffix("__" + self.name).columns
            else:
                self.feature_names = (
                    pd.DataFrame(data=X).add_suffix("__" + self.name).columns
                )
            return self.feature_names

    class FeatureSelectorWrapper(_AppendFeatureNamesAsPandasCols):
        def extract_feature_names(self, X):
            # https://stackoverflow.com/questions/35376293/extracting-selected-feature-names-from-scikit-pipeline
            columns = self.model.transform([X.columns]).flatten()
            self.feature_names = [f"{col}__{self.name}" for col in columns]
            return self.feature_names

    if model.__class__.__name__ in ["SelectFromModel"]:
        return FeatureSelectorWrapper(model, name)
    if (
        hasattr(model, "get_feature_names")
        or hasattr(model, "n_clusters")
        or hasattr(model, "n_components")
        or hasattr(model, "kneighbors")  # KNN has attribute classes_ after fit
    ):
        return FeatureGeneratorWrapper(model, name)
    else:
        return TransformerWrapper(model, name)


def get_feature_names(column_transformer):
    """Get feature names from all transformers.
    Source: https://johaupt.github.io/scikit-learn/tutorial/python/data%20processing/ml%20pipeline/model%20interpretation/columnTransformer_feature_names.html

    Returns
    -------
    feature_names : list of strings
        Names of the features produced by transform.
    """
    # Remove the internal helper function
    # check_is_fitted(column_transformer)

    # Turn loopkup into function for better handling with pipeline later
    def get_names(trans):
        # >> Original get_feature_names() method
        if trans == "drop" or (hasattr(column, "__len__") and not len(column)):
            return []
        if trans == "passthrough":
            if hasattr(column_transformer, "_df_columns"):
                if (not isinstance(column, slice)) and all(
                    isinstance(col, str) for col in column
                ):
                    return column
                else:
                    return column_transformer._df_columns[column]
            else:
                indices = np.arange(column_transformer._n_features)
                return ["x%d" % i for i in indices[column]]
        if not hasattr(trans, "get_feature_names"):
            # >>> Change: Return input column names if no method avaiable
            # Turn error into a warning
            warnings.warn(
                "Transformer %s (type %s) does not "
                "provide get_feature_names. "
                "Will return input column names if available"
                % (str(name), type(trans).__name__)
            )
            # For transformers without a get_features_names method, use the input
            # names to the column transformer
            if column is None:
                return []
            else:
                return [name + "__" + f for f in column]

        return [name + "__" + f for f in trans.get_feature_names()]

    ### Start of processing
    feature_names = []

    # Allow transformers to be pipelines. Pipeline steps are named differently, so preprocessing is needed
    if type(column_transformer) == sklearn.pipeline.Pipeline:
        l_transformers = [
            (name, trans, None, None)
            for step, name, trans in column_transformer._iter()
        ]
    else:
        # For column transformers, follow the original method
        l_transformers = list(column_transformer._iter(fitted=True))

    for name, trans, column, _ in l_transformers:
        if type(trans) == sklearn.pipeline.Pipeline:
            # Recursive call on pipeline
            _names = get_feature_names(trans)
            # if pipeline has no transformer that returns names
            if len(_names) == 0:
                _names = [name + "__" + f for f in column]
            feature_names.extend(_names)
        else:
            feature_names.extend(get_names(trans))

    return feature_names


def add_feature_names_from_column_transformer(X, feature_pipe):
    feature_names = get_feature_names(feature_pipe)
    X_t = pd.DataFrame(data=X, columns=feature_names)
    return X_t
