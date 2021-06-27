from enum import Enum
from typing import Mapping, Union, MutableMapping, Collection, Tuple, List, Optional, NamedTuple

import numpy as np

from sfu_ml_lib.base.metrics import NumericType, AggregatorType, MetricKeyType


class Statistic(Enum):
    TARGET = 'Target'
    PREDICTION = 'Prediction'
    PROBABILITY = 'Probability'
    COST = 'Cost'
    BETA = 'Beta'
    LOGITS = 'Logits'
    WEIGHTS = 'Weights'


StatisticKey = Union[str, Statistic]
StatisticValue = Union[List[NumericType], NumericType, np.ndarray]


class Aggregation(NamedTuple):
    metric: MetricKeyType
    statistics: Collection[StatisticKey]
    function: AggregatorType


class MetricAggregator:
    def __init__(self, aggregators: Optional[Collection[Aggregation]] = None):
        self.aggregators: MutableMapping[MetricKeyType, Tuple[Collection[StatisticKey], AggregatorType]] = {}
        self.state: MutableMapping[StatisticKey, List[NumericType]] = {}

        if aggregators:
            self.register_aggregators(aggregators)

    @staticmethod
    def to_numeric_list(value: StatisticValue) -> List[NumericType]:
        if isinstance(value, np.ndarray):
            return value.tolist()
        elif isinstance(value, List):
            return value
        else:
            return [value]

    @staticmethod
    def to_str(value: Union[Enum, str]) -> str:
        return str(value.value) if isinstance(value, Enum) else value

    def register_aggregator(
            self,
            metric: MetricKeyType,
            statistics: Collection[StatisticKey],
            function: AggregatorType,
    ) -> None:

        self.aggregators[metric] = (statistics, function)

        for statistic in statistics:
            if statistic not in self.state:
                self.state[statistic] = []

    def register_aggregators(self, aggregators: Collection[Aggregation]):
        for aggregator in aggregators:
            self.register_aggregator(aggregator.metric, aggregator.statistics, aggregator.function)

    def add_statistic(self, key: StatisticKey, value: StatisticValue) -> None:
        self.state[key].extend(self.to_numeric_list(value))

    def add_statistics(self, statistics: Mapping[StatisticKey, StatisticValue]) -> None:
        for key, value in statistics.items():
            self.add_statistic(key, value)

    def compute_metric(self, key: MetricKeyType) -> Optional[NumericType]:
        statistics, function = self.aggregators[key]

        if not any(len(self.state[statistic]) != 0 for statistic in statistics):
            return None

        return function(*(np.array(self.state[statistic]) for statistic in statistics))

    def compute_metrics(self, keys: Collection[MetricKeyType]) -> Mapping[MetricKeyType, NumericType]:
        return {
            key: value
            for key, value
            in ((key, self.compute_metric(key)) for key in keys)
            if value is not None
        }

    def get_metrics(self) -> Mapping[MetricKeyType, NumericType]:
        return self.compute_metrics(self.aggregators.keys())

    def clear(self) -> None:
        for sequence in self.state.values():
            sequence.clear()

    def flush(self) -> Mapping[MetricKeyType, NumericType]:
        metrics = self.compute_metrics(self.aggregators.keys())

        self.clear()

        return metrics
