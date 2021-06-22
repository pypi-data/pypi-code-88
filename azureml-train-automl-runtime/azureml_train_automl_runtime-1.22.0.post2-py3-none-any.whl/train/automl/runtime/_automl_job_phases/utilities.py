# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
from typing import Any, Dict, Optional, Tuple, Union

from azureml.automl.core.onnx_convert import OnnxConvertConstants
from azureml.automl.runtime.data_context import RawDataContext
from azureml.automl.runtime.onnx_convert import OnnxConverter
from azureml.automl.runtime.shared.cache_store import CacheStore
from azureml.train.automl._azureautomlsettings import AzureAutoMLSettings
from azureml.train.automl.utilities import _get_package_version

logger = logging.getLogger(__name__)


class PhaseUtil:
    """Utils leveraged by AutoML job phases."""

    @staticmethod
    def build_onnx_converter(
        automl_settings: AzureAutoMLSettings
    ) -> Optional[OnnxConverter]:
        """Build the ONNX converter for the run."""
        if not automl_settings.enable_onnx_compatible_models:
            return None
        pkg_ver = _get_package_version()
        enable_split_onnx_models = automl_settings.enable_split_onnx_featurizer_estimator_models
        return OnnxConverter(
            version=pkg_ver,
            is_onnx_compatible=automl_settings.enable_onnx_compatible_models,
            enable_split_onnx_featurizer_estimator_models=enable_split_onnx_models)

    @staticmethod
    def build_raw_data_context(
        fit_iteration_parameters_dict: Dict[str, Any],
        automl_settings: AzureAutoMLSettings
    ) -> RawDataContext:
        return RawDataContext(
            automl_settings_obj=automl_settings,
            X=fit_iteration_parameters_dict.get('X'),
            y=fit_iteration_parameters_dict.get('y'),
            X_valid=fit_iteration_parameters_dict.get('X_valid'),
            y_valid=fit_iteration_parameters_dict.get('y_valid'),
            sample_weight=fit_iteration_parameters_dict.get('sample_weight'),
            sample_weight_valid=fit_iteration_parameters_dict.get('sample_weight_valid'),
            x_raw_column_names=fit_iteration_parameters_dict.get('x_raw_column_names'),
            cv_splits_indices=fit_iteration_parameters_dict.get('cv_splits_indices'),
            training_data=fit_iteration_parameters_dict.get('training_data'),
            validation_data=fit_iteration_parameters_dict.get('validation_data'))

    @staticmethod
    def get_onnx_model_desc(parent_run_id: str) -> Dict[str, str]:
        """Get the description for the ONNX model."""
        return {'ParentRunId': parent_run_id}

    @staticmethod
    def get_onnx_model_name(parent_run_id: str) -> str:
        """Get the name for the ONNX model."""
        return '{}[{}]'.format(OnnxConvertConstants.OnnxModelNamePrefix, parent_run_id)
