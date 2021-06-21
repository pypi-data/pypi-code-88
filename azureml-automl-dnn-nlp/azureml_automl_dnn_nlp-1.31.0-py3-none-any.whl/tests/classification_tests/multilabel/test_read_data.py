import pytest
import unittest

from azureml.automl.dnn.nlp.classification.common.constants import DatasetLiterals
from azureml.automl.dnn.nlp.classification.io.read.pytorch_dataset_wrapper import PyTorchDatasetWrapper
from azureml.automl.dnn.nlp.classification.io.read.dataloader import convert_dataset_format, get_vectorizer

try:
    import torch
    has_torch = True
except ImportError:
    has_torch = False


@pytest.mark.usefixtures('MultilabelDatasetTester')
@pytest.mark.parametrize('multiple_text_column', [False])
class TestPyTorchDatasetWrappert:
    @unittest.skipIf(not has_torch, "torch not installed")
    def test_pytorch_dataset_wrapper(self, MultilabelDatasetTester):
        input_df = MultilabelDatasetTester.get_data().copy()
        vectorizer = get_vectorizer(input_df, input_df)
        num_label_cols = len(vectorizer.get_feature_names())
        assert num_label_cols == 6
        training_df = convert_dataset_format(input_df, vectorizer)
        training_df['list'] = training_df[training_df.columns[1:]].values.tolist()
        training_df = training_df[[DatasetLiterals.TEXT_COLUMN, 'list']].copy()
        training_set = PyTorchDatasetWrapper(training_df)
        assert len(training_set) == 5
        assert all(item in ['ids', 'mask', 'token_type_ids', 'targets'] for item in training_set[1])
        assert all(torch.is_tensor(value) for key, value in training_set[1].items())

    @unittest.skipIf(not has_torch, "torch not installed")
    def test_convert_dataset_format(self, MultilabelDatasetTester):
        input_df = MultilabelDatasetTester.get_data().copy()
        pre_conv_col_list = [DatasetLiterals.TEXT_COLUMN, DatasetLiterals.LABEL_COLUMN]
        assert input_df.columns.to_list() == pre_conv_col_list
        vectorizer = get_vectorizer(input_df, input_df)
        num_label_cols = len(vectorizer.get_feature_names())
        training_df = convert_dataset_format(input_df, vectorizer)
        assert num_label_cols == 6
        post_conv_col_list = [DatasetLiterals.TEXT_COLUMN, 'list']
        assert training_df.columns.to_list() == post_conv_col_list

    @unittest.skipIf(not has_torch, "torch not installed")
    def test_get_vectorizer(self, MultilabelDatasetTester):
        input_df = MultilabelDatasetTester.get_data().copy()
        vectorizer = get_vectorizer(input_df, input_df)
        num_label_cols = len(vectorizer.get_feature_names())
        assert num_label_cols == 6
        assert set(vectorizer.get_feature_names()) == set(['A', 'a', '1', '2', 'label5', 'label6'])


@pytest.mark.usefixtures('MultilabelDatasetTester')
@pytest.mark.parametrize('multiple_text_column', [True])
class TestPyTorchDatasetWrapperMultipleColumnst:
    @unittest.skipIf(not has_torch, "torch not installed")
    def test_pytorch_dataset_wrapper(self, MultilabelDatasetTester):
        input_df = MultilabelDatasetTester.get_data().copy()
        vectorizer = get_vectorizer(input_df, input_df)
        num_label_cols = len(vectorizer.get_feature_names())
        assert num_label_cols == 6
        training_df = convert_dataset_format(input_df, vectorizer)
        training_df['list'] = training_df[training_df.columns[1:]].values.tolist()
        training_df = training_df[[DatasetLiterals.TEXT_COLUMN, 'list']].copy()
        training_set = PyTorchDatasetWrapper(training_df)
        assert len(training_set) == 5
        assert all(item in ['ids', 'mask', 'token_type_ids', 'targets'] for item in training_set[1])
        assert all(torch.is_tensor(value) for key, value in training_set[1].items())

    @unittest.skipIf(not has_torch, "torch not installed")
    def test_convert_dataset_format(self, MultilabelDatasetTester):
        input_df = MultilabelDatasetTester.get_data().copy()
        vectorizer = get_vectorizer(input_df, input_df)
        num_label_cols = len(vectorizer.get_feature_names())
        training_df = convert_dataset_format(input_df, vectorizer)
        assert num_label_cols == 6
        post_conv_col_list = [DatasetLiterals.TEXT_COLUMN, 'list']
        assert training_df.columns.to_list() == post_conv_col_list

    @unittest.skipIf(not has_torch, "torch not installed")
    def test_get_vectorizer(self, MultilabelDatasetTester):
        input_df = MultilabelDatasetTester.get_data().copy()
        vectorizer = get_vectorizer(input_df, input_df)
        num_label_cols = len(vectorizer.get_feature_names())
        assert num_label_cols == 6
        assert set(vectorizer.get_feature_names()) == set(['A', 'a', '1', '2', 'label5', 'label6'])
