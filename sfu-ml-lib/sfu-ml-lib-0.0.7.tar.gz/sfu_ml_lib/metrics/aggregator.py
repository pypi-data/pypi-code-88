from typing import Optional, Collection, Mapping

import tensorflow as tf
from tensorflow.keras.metrics import Metric

import sfu_ml_lib.base.metrics as metric_helpers
from sfu_ml_lib.base.metrics import NumericType
from sfu_ml_lib.metrics.aggregation.aggregator import Aggregation, MetricAggregator, Statistic


class KerasMetric(Metric):
    def __init__(
            self,
            aggregations: Collection[Aggregation],
            session: tf.compat.v1.Session,
            name: str = 'custom_metric',
            **kwargs,
    ) -> None:

        super().__init__(name, **kwargs)

        self.metric_aggregator = MetricAggregator(aggregations)
        self.session = session

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        self.metric_aggregator.add_statistics({
            Statistic.TARGET: y_true.eval(session=self.session),
            Statistic.LOGITS: y_pred.eval(session=self.session),
        })

        if sample_weight:
            self.metric_aggregator.add_statistic(Statistic.WEIGHTS, sample_weight.numpy())

    def reset_state(self) -> None:
        self.metric_aggregator.clear()

    def result(self) -> NumericType:
        return next(iter(self.metric_aggregator.get_metrics().values()))

    def get_metrics(self) -> Mapping[str, tf.Tensor]:
        return {
            metric_helpers.to_string(label): tf.convert_to_tensor(value)
            for label, value
            in self.metric_aggregator.get_metrics().items()
        }
