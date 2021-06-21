# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains dataloader functions for the classification tasks."""

import logging
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from typing import Tuple

from azureml.automl.dnn.nlp.classification.io.read.pytorch_dataset_wrapper import PyTorchDatasetWrapper
from azureml.automl.dnn.nlp.classification.common.constants import DatasetLiterals
from azureml.automl.dnn.nlp.classification.io.write.save_utils import save_vectorizer
from azureml.core import Dataset as AmlDataset
from azureml.core.workspace import Workspace


_logger = logging.getLogger(__name__)


def get_vectorizer(train_df: pd.DataFrame, val_df: pd.DataFrame) -> CountVectorizer:
    """Obtain labels vectorizer

    :param train_df: Training DataFrame
    :param val_df: Validation DataFrame
    :return: vectorizer
    """
    # Combine both dataframes
    combined_df = pd.concat([train_df, val_df])

    # Get combined label column
    combined_label_col = np.array(combined_df[DatasetLiterals.LABEL_COLUMN].astype(str))

    # TODO: CountVectorizer could run into memory issues for large datasets
    vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b", lowercase=False)
    vectorizer.fit(combined_label_col)
    save_vectorizer(vectorizer)

    return vectorizer


def concat_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Concatenating text (feature) columns present in the dataframe.

    :param df: Dataframe with all columns
    :return: Combined text columns Dataframe
    """
    df_copy = df.copy()
    # Obtain the list of all columns
    df_columns = df_copy.columns

    if DatasetLiterals.LABEL_COLUMN in df_columns:
        df_copy.drop(columns=[DatasetLiterals.LABEL_COLUMN], inplace=True)

    text_columns = df_copy.columns

    text_df = pd.DataFrame()
    text_df[DatasetLiterals.TEXT_COLUMN] = df_copy[text_columns[0]].map(str)

    # Iterate through other text columns and concatenate them
    for column_name in text_columns[1:]:
        text_df[DatasetLiterals.TEXT_COLUMN] += ". " + df_copy[column_name].map(str)

    return text_df


def convert_dataset_format(df: pd.DataFrame, vectorizer: CountVectorizer) -> pd.DataFrame:
    """Converting dataset format for consumption during model training.
    The input dataframe contains a single labels columns with comma separated labels per datapoint.
    The vectorizer is used to generate multiple label columns from the combined labels column.

    :param df: Dataframe to be converted into required format
    :param vectorizer: labels vectorizer
    :return: Dataframe in required format
    """
    label_col = np.array(df[DatasetLiterals.LABEL_COLUMN].astype(str))

    # Create dataframes with label columns
    count_array = vectorizer.transform(label_col)
    labels_df = pd.DataFrame(count_array.toarray().astype(float))
    labels_df.columns = vectorizer.get_feature_names()

    text_df = concat_text_columns(df)

    # Create final dataframe by concatenating text with label dataframe
    final_df = pd.concat([text_df, labels_df], join='outer', axis=1)

    final_df['list'] = final_df[final_df.columns[1:]].values.tolist()
    final_df = final_df[[DatasetLiterals.TEXT_COLUMN, 'list']].copy()

    return final_df


def dataset_loader(dataset_id: str,
                   validation_dataset_id: str,
                   workspace: Workspace) -> Tuple[PyTorchDatasetWrapper, PyTorchDatasetWrapper, int]:
    """Save checkpoint to outputs directory.

    :param dataset_id: Unique identifier to fetch dataset from datastore
    :param validation_dataset_id: Unique identifier to fetch validation dataset from datastore
    :param workspace: workspace where dataset is stored in blob
    :return: training dataset, test datasets, number of label columns
    """

    # Get Training Dataset object
    train_ds = AmlDataset.get_by_id(workspace, dataset_id)
    _logger.info("Type of Dataset is: {}".format(type(train_ds)))

    # Get Validation Dataset object
    validation_ds = AmlDataset.get_by_id(workspace, validation_dataset_id)
    _logger.info("Type of Validation Dataset is: {}".format(type(validation_ds)))

    # Convert Dataset to Dataframe
    train_df = train_ds.to_pandas_dataframe()
    validation_df = validation_ds.to_pandas_dataframe()

    # Fit a vectorizer on the label column so that we can transform labels column
    vectorizer = get_vectorizer(train_df, validation_df)
    num_label_cols = len(vectorizer.get_feature_names())

    # Convert dataset into the format ingestible be model
    t_df = convert_dataset_format(train_df, vectorizer)
    v_df = convert_dataset_format(validation_df, vectorizer)

    _logger.info("TRAIN Dataset: {}".format(t_df.shape))
    _logger.info("VALIDATION Dataset: {}".format(v_df.shape))

    training_set = PyTorchDatasetWrapper(t_df)
    validation_set = PyTorchDatasetWrapper(v_df)

    return training_set, validation_set, num_label_cols
