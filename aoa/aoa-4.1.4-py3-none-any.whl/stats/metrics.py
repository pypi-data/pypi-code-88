import time
import json
import os
import re

from prometheus_client.metrics import MetricWrapperBase
from prometheus_client import values
from prometheus_client.registry import REGISTRY
from prometheus_client.utils import floatToGoString, INF
from prometheus_client import CollectorRegistry, push_to_gateway

PROMETHEUS_PUSH_GATEWAY_URL = os.getenv('PROMETHEUS_PUSH_GATEWAY_URL', 'localhost:9091')


def publish_data_stats(data_stats, exported_job="aoa_scoring"):
    """
    Publishes the results of record_scoring_stats(..) to prometheus for scoring only.

    This should use the MonitoringHistogram below to record and then push to prometheus the metrics as we do in the
    Java code here https://github.com/ThinkBigAnalytics/AoaCoreService/blob/master/aoa-model-trainer/src/main/java/com/teradata/aoa/trainer/service/monitoring/DataStatisticsPublisher.java#L73

    As we are doing this here in python we may look to remove the same logic from Java and always publish it from here
    for train, eval and scoring.

    Note that we will probably also need to use this for R code later also as R can't publish to prometheus and this will
    allow us to have a single place to publish these metrics.

    :param exported_job:
    :param data_stats:
    :return:
    """

    registry = CollectorRegistry()
    
    # MonitoringHistogram for features and predictors. make sure to take care if categorical or continuous.
    # Just follow logic in Java but it will be much simpler in python :)

    try:
        labels = {
            "model_version": os.environ["MODEL_VERSION"],
            "project_id": os.environ["PROJECT_ID"],
            "model_id": os.environ["MODEL_ID"]
        }
    except Exception as ex:
        raise Exception(f"Missing required environmental variables. Contact system administrator.\nError: {ex}")

    if "features" in data_stats:
        features = data_stats["features"]
        for name, feature in features.items():
            feature_group = feature["group"] if "group" in feature and feature["group"] != "" else "default"
            description = f"Model Feature Statistics {name}"
            name = create_metric_name("model_features", name, feature_group)
            if "type" in feature:
                if feature["type"].lower() == "categorical":
                    record_categorical_histogram(registry, description, name, labels, feature)
                elif feature["type"].lower() == "continuous":
                    record_continuous_histogram(registry, description, name, labels, feature)

    if "predictors" in data_stats:
        predictors = data_stats["predictors"]
        for name, predictor in predictors.items():
            predictor_group = predictor["group"] if "group" in predictor and predictor["group"] != "" else "default"
            description = f"Model Predictor Statistics {name}"
            name = create_metric_name("model_predictors", name, predictor_group)
            if "type" in predictor:
                if predictor["type"].lower() == "categorical":
                    record_categorical_histogram(registry, description, name, labels, predictor)
                elif predictor["type"].lower() == "continuous":
                    record_continuous_histogram(registry, description, name, labels, predictor)

    grouping_key = {
        "model_version": labels['model_version'],
        "job": exported_job
    }
    push_to_gateway(PROMETHEUS_PUSH_GATEWAY_URL, job=exported_job, registry=registry, grouping_key=grouping_key)


def save_evaluation_metrics(metrics):
    with open("artifacts/output/metrics.json", "w+") as f:
        json.dump(metrics, f)


def record_continuous_histogram(registry, documentation, name, labels, data):
    if "statistics" in data and "histogram" in data["statistics"]:
        histogram = data["statistics"]["histogram"]
        edges = histogram["edges"] if "edges" in histogram else None
        edges.sort()
        value_list = histogram["values"] if "values" in histogram else None

        monitor = MonitoringHistogram(name=name,
                                      documentation=documentation,
                                      buckets=edges,
                                      labelnames=["project_id", "model_id", "model_version"],
                                      registry=registry)

        monitor.labels(labels["project_id"], labels["model_id"], labels["model_version"]).record(value_list)


def record_categorical_histogram(registry, documentation, name, labels, data):
    if "statistics" in data and "frequency" in data["statistics"]:
        frequency = data["statistics"]["frequency"]
        categories = [int(x) for x in [*frequency]]
        categories.sort()
        value_list = [*frequency.values()]

        monitor = MonitoringHistogram(name=name,
                                      documentation=documentation,
                                      buckets=categories,
                                      labelnames=["project_id", "model_id", "model_version"],
                                      registry=registry)

        monitor.labels(labels["project_id"], labels["model_id"], labels["model_version"]).record(value_list)


def create_metric_name(metric_prefix, name, group=""):
    return convert_to_valid_name(f"{metric_prefix}_{group}_{name}").lower()


def convert_to_valid_name(name):
    return re.sub('[^a-zA-Z_:][^a-zA-Z0-9_:]*', '', name)


class MonitoringHistogram(MetricWrapperBase):
    """A Custom MonitoringHistogram which we can use to record and publish histograms captured via other systems
    (e.g. Teradata VAL etc) to prometheus for model drift monitoring
    """
    _type = 'histogram'
    _reserved_labelnames = ['le']
    DEFAULT_BUCKETS = (.005, .01, .025, .05, .075, .1, .25, .5, .75, 1.0, 2.5, 5.0, 7.5, 10.0, INF)

    def __init__(self,
                 name,
                 documentation,
                 labelnames=(),
                 namespace='',
                 subsystem='',
                 unit='',
                 registry=REGISTRY,
                 _labelvalues=None,
                 buckets=DEFAULT_BUCKETS
                 ):
        self._prepare_buckets(buckets)
        super(MonitoringHistogram, self).__init__(
            name=name,
            documentation=documentation,
            labelnames=labelnames,
            namespace=namespace,
            subsystem=subsystem,
            unit=unit,
            registry=registry,
            _labelvalues=_labelvalues
        )
        self._kwargs['buckets'] = buckets

    def _prepare_buckets(self, buckets):
        buckets = [float(b) for b in buckets]
        if buckets != sorted(buckets):
            # This is probably an error on the part of the user,
            # so raise rather than sorting for them.
            raise ValueError('Buckets not in sorted order')
        if buckets and buckets[-1] != INF:
            buckets.append(INF)
        if len(buckets) < 2:
            raise ValueError('Must have at least two buckets')
        self._upper_bounds = buckets

    def _metric_init(self):
        self._buckets = []
        self._created = time.time()
        bucket_labelnames = self._labelnames + ('le',)
        self._sum = values.ValueClass(self._type, self._name, self._name + '_sum', self._labelnames, self._labelvalues)
        self._count = values.ValueClass(self._type, self._name, self._name + '_count', self._labelnames, self._labelvalues)
        for b in self._upper_bounds:
            self._buckets.append(values.ValueClass(
                self._type,
                self._name,
                self._name + '_bucket',
                bucket_labelnames,
                self._labelvalues + (floatToGoString(b),))
            )

    def record(self, value_list):
        self._sum.set(0)
        for i, value in enumerate(value_list):
            self._buckets[i].set(value)
            self._count.inc(value)

    def _child_samples(self):
        samples = []
        for i, bound in enumerate(self._upper_bounds):
            acc = self._buckets[i].get()
            samples.append(('_bucket', {'le': floatToGoString(bound)}, acc))
        samples.append(('_count', {}, self._count.get()))
        samples.append(('_sum', {}, self._sum.get()))
        samples.append(('_created', {}, self._created))

        return tuple(samples)
