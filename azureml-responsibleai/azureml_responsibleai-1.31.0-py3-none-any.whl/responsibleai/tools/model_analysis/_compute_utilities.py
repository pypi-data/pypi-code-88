# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import argparse
import joblib
import logging

from azureml._common._error_definition import AzureMLError
from azureml.core import Run
from azureml.exceptions import AzureMLException, UserErrorException

from responsibleai import ModelAnalysis

from azureml.responsibleai.common._errors.error_definitions import (
    MismatchedExperimentName,
    UnexpectedObjectType
)

from azureml.responsibleai.tools.model_analysis._model_analysis_explanation_client import (
    ModelAnalysisExplanationClient)

from azureml.responsibleai.tools.model_analysis.model_analysis_run import ModelAnalysisRun
from azureml.responsibleai.tools.model_analysis._compute_dto import ComputeDTO
from azureml.responsibleai.tools.model_analysis._constants import PropertyKeys


_logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


def _parse_command_line():
    parser = argparse.ArgumentParser()

    parser.add_argument('--settings_filepath', type=str, required=True,
                        help="Path to the pickled settings")

    return parser.parse_args()


def _run_all_and_upload(settings: ComputeDTO,
                        current_run: Run):
    _logger.info("Found {0} explanation requests".format(
        len(settings.requests.explanation_requests)))

    _logger.info("Getting the parent run")
    ma_run = ModelAnalysisRun(
        current_run.experiment,
        settings.model_analysis_run_id)

    _logger.info("Loading the data")
    train_df = ma_run.get_train_data()
    test_df = ma_run.get_test_data()
    # train_y_pred = ma_run.get_train_labels()
    # test_y_pred = ma_run.get_test_labels()

    _logger.info("Loading the estimator")
    estimator = ma_run.settings.model_loader.load_by_model_id(
        current_run.experiment.workspace,
        ma_run.settings.model_id)

    _logger.info("Creating the local model analysis")
    rai_a = ModelAnalysis(
        estimator,
        train_df,
        test_df,
        target_column=ma_run.settings.target_column_name,
        task_type=ma_run.settings.model_type
    )

    _logger.info("Queueing up requests")
    for _ in settings.requests.explanation_requests:
        rai_a.explainer.add()

    _logger.info("Running computations")
    rai_a.compute()

    _store_explanations(rai_a, ma_run, settings, current_run)


def _store_explanations(rai_analyzer: ModelAnalysis,
                        parent_ma_run: Run,
                        settings: ComputeDTO,
                        current_run: Run):
    _logger.info("Storing explanations")
    client = ModelAnalysisExplanationClient(
        service_context=current_run.experiment.workspace.service_context,
        experiment_name=current_run.experiment,
        run_id=current_run.id,
        _run=current_run,
        datastore_name=parent_ma_run.settings.confidential_datastore_name,
        analysis_id=parent_ma_run.settings.analysis_id
    )

    all_explanations = rai_analyzer.explainer.get()
    for i in range(len(all_explanations)):
        explanation = all_explanations[i]
        comment = settings.requests.explanation_requests[i].comment
        explanation_asset_id = client._upload_model_explanation_internal(explanation,
                                                                         comment=comment)
        props = {
            PropertyKeys.EXPLANATION_POINTER_FORMAT.format(explanation.id): explanation_asset_id
        }
        parent_ma_run.add_properties(props)
    _logger.info("Explanations stored")


def _compute_wrapper():
    args = _parse_command_line()

    settings: ComputeDTO = joblib.load(args.settings_filepath)
    if not isinstance(settings, ComputeDTO):
        raise AzureMLException._with_error(
            AzureMLError.create(
                UnexpectedObjectType,
                expected='ComputeDTO',
                actual=str(type(settings))
            )
        )

    my_run = Run.get_context()
    if my_run.experiment.name != settings.experiment_name:
        raise UserErrorException._with_error(
            AzureMLError.create(
                MismatchedExperimentName,
                expected=settings.experiment_name,
                actual=my_run.experiment.name
            )
        )

    _run_all_and_upload(settings, my_run)
