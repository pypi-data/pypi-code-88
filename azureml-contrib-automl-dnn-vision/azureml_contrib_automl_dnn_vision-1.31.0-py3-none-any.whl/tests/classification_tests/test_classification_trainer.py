import pytest
import torch

from azureml.contrib.automl.dnn.vision.classification.common.constants import ModelNames
from azureml.contrib.automl.dnn.vision.classification.io.read.dataloader import _get_data_loader
from azureml.contrib.automl.dnn.vision.classification.io.read.dataset_wrappers \
    import ImageFolderLabelFileDatasetWrapper
from azureml.contrib.automl.dnn.vision.classification.models.classification_model_wrappers import ModelFactory
from azureml.contrib.automl.dnn.vision.classification.trainer.train import validate, _compute_class_weight
from azureml.contrib.automl.dnn.vision.common.exceptions import AutoMLVisionDataException
from azureml.contrib.automl.dnn.vision.metrics import ClassificationMetrics

from ..common.run_mock import ClassificationDatasetWrapperMock


@pytest.mark.usefixtures('new_clean_dir')
class TestClassificationTrainer:
    def test_validate_with_invalid_dataset(self):
        # All values in the dataset are invalid
        num_classes = 3
        dataset = ClassificationDatasetWrapperMock([None, None, None, None], num_classes)
        dataloader = _get_data_loader(dataset, transform_fn=None, batch_size=10, num_workers=0)
        metrics = ClassificationMetrics(num_classes=num_classes, multilabel=False)
        model_wrapper = ModelFactory().get_model_wrapper(ModelNames.SERESNEXT,
                                                         num_classes=num_classes,
                                                         distributed=False,
                                                         device='cpu',
                                                         rank=0,
                                                         multilabel=False)
        # Should raise exception when all images in validation dataset are invalid
        with pytest.raises(AutoMLVisionDataException):
            validate(model_wrapper, dataloader=dataloader, metrics=metrics)

    def test_compute_class_weight(self):
        # for multi-class
        dataset_wrapper = ImageFolderLabelFileDatasetWrapper(
            'classification_data/images',
            input_file='classification_data/multiclass.csv'
        )
        label_freq_list = list(dataset_wrapper.label_freq_dict.values())
        imbalance_rate, class_weights = _compute_class_weight(dataset_wrapper, sqrt_pow=1)
        assert imbalance_rate == max(label_freq_list) // min(label_freq_list)

        comparision_result = torch.isclose(class_weights, torch.sqrt(1 / torch.tensor(label_freq_list)))
        assert sum(comparision_result) == len(label_freq_list)

        # for multi-label
        dataset_wrapper = ImageFolderLabelFileDatasetWrapper(
            'classification_data/images',
            input_file='classification_data/multilabel.csv',
            multilabel=True
        )
        label_freq_list = list(dataset_wrapper.label_freq_dict.values())
        imbalance_rate, class_weights = _compute_class_weight(dataset_wrapper, sqrt_pow=1)
        assert imbalance_rate == max(label_freq_list) // min(label_freq_list)

        label_freq_tensor = torch.tensor(label_freq_list)
        neg_weights = len(dataset_wrapper) - label_freq_tensor
        calculated_class_weights = neg_weights / label_freq_tensor
        comparision_result = torch.isclose(class_weights, torch.sqrt(calculated_class_weights))
        assert sum(comparision_result) == len(label_freq_list)
