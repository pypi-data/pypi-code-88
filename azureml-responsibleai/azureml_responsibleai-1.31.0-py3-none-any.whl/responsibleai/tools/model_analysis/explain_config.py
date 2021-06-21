# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Contains the config used for adding explanations to a model analysis.

This can be submitted as a child run of a ModelAnalysisRun
"""
from typing import Any, Optional

from azureml._base_sdk_common._docstring_wrapper import experimental
from azureml._common._error_definition import AzureMLError
from azureml.core import Workspace, Run
from azureml.core import RunConfiguration
from azureml.core._experiment_method import experiment_method
from azureml.exceptions import UserErrorException

from azureml.responsibleai.tools.model_analysis.model_analysis_run import ModelAnalysisRun
from azureml.responsibleai.tools.model_analysis._base_component_config import BaseComponentConfig

from azureml.responsibleai.tools.model_analysis._requests import ExplainRequest
from azureml.responsibleai.common._errors.error_definitions import MismatchedWorkspaceName

from ._requests import RequestDTO


def _explain_submit(config: 'ExplainConfig',
                    workspace: Workspace,
                    experiment_name: str,
                    **kwargs: Any) -> Run:
    """
    Submit a run to add an explanation.

    :param config:
    :param workspace:
    :param experiment_name:
    :param kwargs:
    :return:
    """
    if workspace.name != config._workspace.name:
        raise UserErrorException._with_error(
            AzureMLError.create(
                MismatchedWorkspaceName,
                expected=config._workspace.name,
                actual=workspace.name
            )
        )
    # Create the DTO
    reqs = RequestDTO(
        explanation_requests=config._explain_requests
    )
    return config.compute_requests(experiment_name, reqs, **kwargs)


@experimental
class ExplainConfig(BaseComponentConfig):
    """Class to configure an explanation-generating Run."""

    @experiment_method(submit_function=_explain_submit)
    def __init__(self,
                 model_analysis_run: ModelAnalysisRun,
                 run_configuration: RunConfiguration = None,
                 comment: Optional[str] = None):
        """Instantiate instance of class."""
        super(ExplainConfig, self).__init__(
            model_analysis_run,
            run_configuration
        )
        # Following works around a disagreement between flake8 and mypy
        self._explain_requests = [ExplainRequest(None)]
        del self._explain_requests[0]

    def add_request(self,
                    comment: Optional[str] = None):
        """Add an explanation to the configuration."""
        self._explain_requests.append(ExplainRequest(comment))
