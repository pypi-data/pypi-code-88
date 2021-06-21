# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import logging

from typing import Dict

from azureml._restclient.assets_client import AssetsClient

from azureml.interpret import ExplanationClient

from azureml.responsibleai.tools.model_analysis._constants import (
    AnalysisTypes,
    AzureMLTypes,
    PropertyKeys,
    ExplanationVersion
)

_logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class ModelAnalysisExplanationClient(ExplanationClient):
    def __init__(self,
                 *,
                 service_context,
                 experiment_name,
                 run_id,
                 _run=None,
                 datastore_name=None,
                 analysis_id: str):
        super(ModelAnalysisExplanationClient,
              self).__init__(service_context,
                             experiment_name,
                             run_id,
                             _run,
                             datastore_name)
        self._analysis_id = analysis_id
        self._assets_client = AssetsClient(service_context)

    @property
    def analysis_id(self) -> str:
        return self._analysis_id

    def _get_asset_type(self) -> str:
        """Return the type of Asset to be created."""
        _logger.info("Overriding default asset type for explanation")
        return AzureMLTypes.MODEL_ANALYSIS

    def _update_asset_properties(self, prop_dict: Dict):
        """Modify the properties of the about-to-be-created Asset."""
        _logger.info("Modifying properties for explanation")
        prop_dict[PropertyKeys.ANALYSIS_TYPE] = AnalysisTypes.EXPLANATION_TYPE
        prop_dict[PropertyKeys.ANALYSIS_ID] = self.analysis_id
        prop_dict[PropertyKeys.VERSION] = str(ExplanationVersion.V_0)
