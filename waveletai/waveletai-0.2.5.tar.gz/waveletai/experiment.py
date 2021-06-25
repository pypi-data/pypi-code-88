#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2021/6/4 13:36
@Author  : WaveletAI-Product-Team Janus
@license : (C) Copyright 2019-2022, Visionet(Tianjin)Information Technology Co.,Ltd.
@Site    : plus.xiaobodata.com
@File    : experiment.py
@Desc    : 实验训练实体类
"""

import logging
import os

import mlflow
from mlflow.entities import (Experiment as MlExperiment,
                             RunTag, Metric, Param,
                             RunData, RunInfo, Run, ExperimentTag)

_logger = logging.getLogger(__name__)


class Experiment(object):

    def __init__(self, backend, id, name, desc, param_json, host_id, model_id, dataset_id, start_time, end_time, state,
                 best_run_id, create_time, create_user_id, mlflow_experiments_id, ml_experiment=None):
        self._backend = backend
        self.id = id
        self.name = name
        self.desc = desc
        self.param_json = param_json
        self.host_id = host_id
        self.model_id = model_id
        self.dataset_id = dataset_id
        self.start_time = start_time
        self.end_time = end_time
        self.state = state
        self.best_run_id = best_run_id
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.mlflow_experiments_id = mlflow_experiments_id
        if ml_experiment \
                and mlflow_experiments_id \
                and mlflow_experiments_id == str(ml_experiment['experiment_id']):
            self._mlflow_experiment = MLFlowExperiment(self._backend, ml_experiment['experiment_id'],
                                                       ml_experiment['name'],
                                                       ml_experiment['artifact_location'],
                                                       ml_experiment['lifecycle_stage'])

    def update(self):
        pass

    def delete(self):
        pass

    def run(self, uri='./'):
        mlflow.set_tracking_uri('waveletai-store://')
        mlflow.run(uri, experiment_id=self.mlflow_experiments_id, use_conda=False)

    @property
    def mlflow_experiment(self):
        return self._mlflow_experiment if self._mlflow_experiment else None

    def create_mlflow_run(self, name, artifact_uri, run_uuid, experiment_id, source_type, source_name, entry_point_name,
                          user_id, status, start_time, end_time, source_version, lifecycle_stage):
        return self._backend.create_mlflow_run(name, artifact_uri, run_uuid, experiment_id, source_type,
                                               source_name, entry_point_name, user_id, status, start_time, end_time,
                                               source_version, lifecycle_stage)

    def update_run_info(self, run):
        return self._backend.update_run_info(run.run_uuid, run.status, run.end_time)

    def get_mlflow_run(self, run_id):
        return self._backend.get_mlflow_run(run_id)

    def log_param(self, run_id, params):
        return self._backend.log_param(run_id, params)

    def log_metric(self, run_id, metrics, value, is_nan):
        return self._backend.log_metric(run_id, metrics, value, is_nan)

    def set_tag(self, run_id, tag):
        return self._backend.set_tag(run_id, tag)


class MLFlowExperiment:
    def __init__(self, backend, experiment_id, name, artifact_location, lifecycle_stage):
        self._backend = backend
        self.experiment_id = experiment_id
        self.name = name
        self.artifact_location = artifact_location
        self.lifecycle_stage = lifecycle_stage
        # todo 这种方式在客户端多线程运行多个实验时会存在问题
        os.environ.update({'MLFLOW_EXPERIMENT_ID': str(self.experiment_id)})

    def to_mlflow_entity(self) -> MlExperiment:
        return MlExperiment(
            experiment_id=str(self.experiment_id),
            name=self.name,
            artifact_location=self.artifact_location,
            lifecycle_stage=self.lifecycle_stage)
        # tags=[t.to_mlflow_entity() for t in self.tags])


class MLFlowRun:
    def __init__(self, backend, name, artifact_uri, run_uuid, experiment_id, source_type, source_name, entry_point_name,
                 user_id, status, start_time, end_time, source_version, lifecycle_stage):
        self._backend = backend
        self.name = name
        self.artifact_uri = artifact_uri
        self.run_uuid = run_uuid
        self.experiment_id = experiment_id
        self.source_type = source_type
        self.source_name = source_name
        self.entry_point_name = entry_point_name
        self.user_id = user_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.source_version = source_version
        self.lifecycle_stage = lifecycle_stage

    @property
    def latest_metrics(self):
        return []

    @property
    def params(self):
        return []

    @property
    def tags(self):
        return []

    def to_mlflow_entity(self):
        run_info = RunInfo(
            run_uuid=self.run_uuid,
            run_id=self.run_uuid,
            experiment_id=str(self.experiment_id),
            user_id=self.user_id,
            status=self.status,
            start_time=self.start_time,
            end_time=self.end_time,
            lifecycle_stage=self.lifecycle_stage,
            artifact_uri=self.artifact_uri)

        run_data = RunData(
            metrics=[m.to_mlflow_entity() for m in self.latest_metrics],
            params=[p.to_mlflow_entity() for p in self.params],
            tags=[t.to_mlflow_entity() for t in self.tags])

        return Run(run_info=run_info, run_data=run_data)


class MLflowLatersMetric:
    def __init__(self, key, value, timestamp, step, is_nan, run_uuid):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.step = step
        self.is_nan = is_nan
        self.run_uuid = run_uuid

    def to_mlflow_entity(self):
        """
        Convert DB model to corresponding MLflow entity.

        :return: :py:class:`mlflow.entities.Metric`.
        """
        return Metric(
            key=self.key,
            value=self.value if not self.is_nan else float("nan"),
            timestamp=self.timestamp,
            step=self.step)


class MLFlowParam:
    def __init__(self, key, value, run_uuid):
        self.key = key
        self.value = value
        self.run_uuid = run_uuid

    def to_mlflow_entity(self):
        """
        Convert DB model to corresponding MLflow entity.

        :return: :py:class:`mlflow.entities.Param`.
        """
        return Param(
            key=self.key,
            value=self.value)


class MLFlowTag:
    def __init__(self, key, value, run_uuid):
        self.key = key
        self.value = value
        self.run_uuid = run_uuid

    def to_mlflow_entity(self):
        """
        Convert DB model to corresponding MLflow entity.

        :return: :py:class:`mlflow.entities.RunTag`.
        """
        return RunTag(
            key=self.key,
            value=self.value)
