# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Utility functions to load the final model and vectorizer during inferencing"""

import logging
import os
import pickle
import torch

from sklearn.feature_extraction.text import CountVectorizer
from typing import Optional

from azureml.automl.dnn.nlp.common.constants import OutputLiterals
from azureml.core.run import Run


_logger = logging.getLogger(__name__)


def load_model(run_object: Run, artifacts_dir: Optional[str] = None) -> torch.nn.Module:
    """Function to load model from the training run

    :param run_object: Run object
    :param artifacts_dir: artifacts directory
    :return: model
    """
    _logger.info("Loading model from artifacts")

    if artifacts_dir is None:
        artifacts_dir = OutputLiterals.OUTPUT_DIR

    run_object.download_file(os.path.join(artifacts_dir, OutputLiterals.MODEL_FILE_NAME),
                             output_file_path=OutputLiterals.MODEL_FILE_NAME)

    _logger.info("Finished loading model from training output")

    model = torch.load(OutputLiterals.MODEL_FILE_NAME)
    return model


def load_vectorizer(run_object: Run, artifacts_dir: Optional[str] = None) -> CountVectorizer:
    """Function to load vectorizer from the training run

    :param run_object: Run object
    :param artifacts_dir: artifacts directory
    :return: vectorizer
    """
    _logger.info("Loading vectorizer from artifacts")

    if artifacts_dir is None:
        artifacts_dir = OutputLiterals.OUTPUT_DIR

    run_object.download_file(os.path.join(artifacts_dir, OutputLiterals.VECTORIZER_FILE_NAME),
                             output_file_path=OutputLiterals.VECTORIZER_FILE_NAME)

    _logger.info("Finished loading vectorizer from training output")

    vectorizer = pickle.load(open(OutputLiterals.VECTORIZER_FILE_NAME, "rb"))
    return vectorizer
