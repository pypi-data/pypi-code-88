import json
import os
from abc import ABC
from typing import List, Dict, Mapping, Tuple, Optional, TypeVar, Union, Sequence, Any

import sfu_data_io.helpers as io
import tensorflow as tf
from tensorflow import Tensor
from tensorflow.data import Dataset
from tensorflow.keras import Model
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.losses import Loss
from tensorflow.keras.metrics import Metric
from tensorflow.keras.optimizers import Optimizer

import sfu_ml_lib.base.metrics as metric_helpers
from sfu_ml_lib.base.dataset import TensorTuple
from sfu_ml_lib.base.metrics import MetricKeyType, NumericType
from sfu_ml_lib.metrics.aggregator import KerasMetric


T = TypeVar('T')
W = TypeVar('W')
Z = TypeVar('Z')


class KerasModel(Model, ABC):
    @classmethod
    def deconstruct_inputs(
            cls,
            features: T,
            targets: Optional[W] = None,
            weights: Optional[Z] = None,
    ) -> Tuple[T, Optional[W], Optional[Z]]:
        """
        Converts the outputs of a tf.Dataset into features, optional targets and optional weights.
        Used in combination with `deconstruct_inputs(*args)`.
        """
        return features, targets, weights

    @classmethod
    def from_config_path(cls, path: str, **kwargs) -> 'KerasModel':
        with io.open(os.path.join(path, 'config.json'), mode='r') as json_file:
            config = json.load(json_file)

        config.update(kwargs)

        return cls.from_config(config)

    @classmethod
    def from_config(cls, config: Mapping[str, Any], custom_objects=None) -> 'KerasModel':
        return cls(**config)

    def save_config(self, path: str) -> None:
        with io.open(os.path.join(path, 'config.json'), mode='w') as json_file:
            json.dump(self.get_config(), json_file)

    @classmethod
    def convert_metrics(cls, metrics: Mapping[str, Tensor]) -> Mapping[MetricKeyType, NumericType]:
        return {label: value.numpy() for label, value in metrics.items()}

    @staticmethod
    def get_metrics(metrics: Sequence[Metric]) -> Mapping[str, Tensor]:
        metric_map: Dict[str, Tensor] = {}

        for metric in metrics:
            if isinstance(metric, KerasMetric):
                metric_map.update(metric.get_metrics())
            else:
                metric_map[metric.name] = metric.result()

        return metric_map

    def train_batch(
            self,
            features: T,
            targets: Optional[W],
            weights: Optional[Z],
            loss: Union[Loss, Mapping[str, Loss]],
            optimizer: Union[Optimizer, Mapping[str, Optimizer]],
    ) -> TensorTuple:

        assert isinstance(loss, Loss)
        assert isinstance(optimizer, Optimizer)

        with tf.GradientTape() as tape:
            predictions = self(features, training=True)

            loss_result = loss(targets, predictions, weights)
            if len(self.losses) > 0:
                loss_result += tf.add_n(self.losses)

        optimizer.minimize(loss_result, self.trainable_weights, tape=tape)

        return predictions

    def train_dataset(
            self,
            dataset: tf.data.Dataset,
            loss: Union[Loss, Mapping[str, Loss]],
            optimizer: Union[Optimizer, Mapping[str, Optimizer]],
            metrics: Sequence[Metric],
    ) -> Mapping[str, Tensor]:

        for metric in metrics:
            metric.reset_state()

        for arguments in dataset:
            features, targets, weights = self.deconstruct_inputs(*arguments)

            predictions = self.train_batch(features, targets, weights, loss, optimizer)

            for metric in metrics:
                metric.update_state(targets, predictions, weights)

        metric_results = self.get_metrics(metrics)

        return metric_results

    def test_batch(self, features: T) -> TensorTuple:
        return self(features, training=False)

    def test_dataset(self, dataset: Dataset, metrics: Sequence[Metric]) -> Mapping[str, Tensor]:
        for metric in metrics:
            metric.reset_state()

        for arguments in dataset:
            features, targets, weights = self.deconstruct_inputs(*arguments)

            predictions = self.test_batch(features)

            for metric in metrics:
                metric.update_state(targets, predictions, weights)

        metric_results = self.get_metrics(metrics)

        return metric_results

    def fit_dataset(
            self,
            train_batches: Dataset,
            max_num_epochs: int = 1,
            validation_batches: Optional[Dataset] = None,
            test_batches: Optional[Dataset] = None,
            callbacks: Optional[List[Callback]] = None,
    ) -> None:
        """
        Please look at `train_dataset` for details on how to construct `batches`.
        """
        callbacks = callbacks if callbacks else []
        metrics = self.compiled_metrics._metrics
        train_dataset = tf.function(self.train_dataset)
        test_dataset = tf.function(self.test_dataset)

        self.stop_training = False

        for callback in callbacks:
            callback.set_model(self)
            callback.on_train_begin()

        for epoch in range(max_num_epochs):
            for callback in callbacks:
                callback.on_epoch_begin(epoch)

            train_metrics = self.convert_metrics(train_dataset(train_batches, self.loss, self.optimizer, metrics))
            metric_results = metric_helpers.prefix_metrics_train(train_metrics)

            if validation_batches is not None:
                validation_metrics = self.convert_metrics(test_dataset(validation_batches, metrics))
                metric_results.update(metric_helpers.prefix_metrics_validation(validation_metrics))

            for callback in callbacks:
                callback.on_epoch_end(epoch, metric_results)

            if self.stop_training:
                break

        results = None

        if test_batches is not None:
            test_metrics = self.convert_metrics(test_dataset(test_batches, metrics))
            results = metric_helpers.prefix_metrics_test(test_metrics)

        for callback in callbacks:
            callback.on_train_end(results)
