# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Constants for classification tasks."""


class DatasetLiterals:
    """Key columns for Dataset"""
    TEXT_COLUMN = 'text'
    LABEL_COLUMN = 'labels'
    LABEL_CONFIDENCE = 'label_confidence'
    DATAPOINT_ID = 'datapoint_id'


class MultiLabelParameters:
    """Defining key variables that will be used later on in the training"""
    MAX_LEN = 128
    TRAIN_BATCH_SIZE = 16
    VALID_BATCH_SIZE = 8
    EPOCHS = 3
    LEARNING_RATE = 1e-05
    OUTPUT_EPOCHS_COUNT = 5000
    DROPOUT = 0.3


class ModelNames:
    """Currently supported model names."""
    BERT_BASE_UNCASED = "bert-base-uncased"
