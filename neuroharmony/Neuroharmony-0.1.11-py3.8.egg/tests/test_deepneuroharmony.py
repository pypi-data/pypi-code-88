"""Tests for harmonization with Neuroharmony."""
from unittest.mock import patch, Mock

from pandas.core.generic import NDFrame
import joblib
import pytest
import pandas as pd

from neuroharmony.models.deepharmonization import DeepNeuroharmony
from tests.test_neuroharmony import resources

resources = resources


def something(a, b, cc):
    """Short summary.

    Parameters
    ----------
    a : type
        Description of parameter `a`.
    b : type
        Description of parameter `b`.
    cc : type
        Description of parameter `cc`.

    Returns
    -------
    type
        Description of returned object.

    """
    pass


def test_regressor_class():
    print("ok")


def test_model_with_keras(resources):
    """Teste we can use a DNN on Neuroharmony kernel."""
    x_train = resources.X_train_split
    deepneuroharmony = DeepNeuroharmony(
        resources.features, resources.regression_features, resources.covariates, resources.eliminate_variance,
    )
    # with patch("tensorflow.keras.layers.experimental.preprocessing.Normalization.adapt"):
    #     with patch("neuroharmony.models.deepharmonization.Regressor"):
    #         with patch("kerastuner.RandomSearch"):
    #             with patch("kerastuner.RandomSearch.search"):
    # deepneuroharmony.fit(pd.concat(10 * [x_train]))
    deepneuroharmony.fit(x_train)
    deepneuroharmony.save()
