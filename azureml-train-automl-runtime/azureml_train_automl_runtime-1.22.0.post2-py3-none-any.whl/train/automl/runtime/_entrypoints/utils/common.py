# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Methods for AutoML remote runs."""
import gc
import json
import logging
import os
import re
import sys
import tempfile
import time
from typing import Any, Dict, Optional, Tuple

import numpy as np
import pandas as pd
from azureml._history.utils.constants import LOGS_AZUREML_DIR
from azureml._tracing import get_tracer
from azureml.automl.runtime._ml_engine.validation import common_data_validations

from azureml.automl.core.shared import log_server
from azureml.automl.core.shared import logging_utilities
from azureml.automl.core.shared.constants import TelemetryConstants
from azureml.automl.core.shared.exceptions import AutoMLException, CacheException, UserException
from azureml.automl.core.shared.reference_codes import ReferenceCodes
from azureml.automl.core.shared.telemetry_activity_logger import TelemetryActivityLogger
from azureml.core import Datastore, Experiment, Run
from azureml.data.azure_storage_datastore import AbstractAzureStorageDatastore
from azureml.data.constants import WORKSPACE_BLOB_DATASTORE
from azureml.train.automl.runtime._cachestorefactory import CacheStoreFactory
from azureml.train.automl.runtime._data_preparer import DataPreparer
from azureml.train.automl.runtime.utilities import _load_user_script
from msrest.exceptions import HttpOperationError

from azureml.automl.runtime import short_grain_padding
from azureml.automl.runtime import training_utilities
from azureml.automl.runtime._automl_settings_utilities import rule_based_validation
from azureml.automl.runtime.column_purpose_detection._time_series_column_helper import convert_check_grain_value_types
from azureml.automl.runtime.faults_verifier import VerifierManager
from azureml.automl.runtime.featurizer.transformer.timeseries._validation import check_memory_limit
from azureml.automl.runtime.frequency_fixer import fix_data_set_regularity_may_be, str_to_offset_safe
from azureml.automl.runtime.shared.cache_store import CacheStore
from azureml.automl.runtime.shared.datasets import DatasetBase
from azureml.train.automl import _logging  # type: ignore
from azureml.train.automl._azureautomlsettings import AzureAutoMLSettings
from azureml.train.automl.constants import ComputeTargets
from azureml.train.automl.exceptions import ClientException
from azureml.train.automl.utilities import _get_package_version

CACHE_STORE_KEY_ONNX_CONVERTER_INIT_METADATA = '_CACHE_STORE_KEY_ONNX_CONVERTER_INIT_METADATA_'

# The base dataset object can be cached in the setup iteration (to be later re-used during model training),
# with the following key
DATASET_BASE_CACHE_KEY = 'dataset_cached_object'

logger = logging.getLogger(__name__)
activity_logger = TelemetryActivityLogger()
tracer = get_tracer(__name__)


def init_wrapper(
        current_run: Run,
        automl_settings_str: str,
        script_directory: Optional[str],
        **kwargs: Any
) -> Tuple[Run, AzureAutoMLSettings, CacheStore]:
    """Initialize common variables across remote wrappers."""
    with tracer.start_as_current_span(
            TelemetryConstants.SPAN_FORMATTING.format(
                TelemetryConstants.COMPONENT_NAME, TelemetryConstants.RUN_INITIALIZATION
            ),
            user_facing_name=TelemetryConstants.RUN_INITIALIZATION_USER_FACING
    ):
        pkg_ver = _get_package_version()
        logger.info('Using SDK version {}'.format(pkg_ver))

        _init_directory(directory=script_directory)

        parent_run_id = get_parent_run_id(current_run.id)
        parent_run = Run(current_run.experiment, parent_run_id)

        automl_settings_obj = parse_settings(current_run, automl_settings_str)

        # cache_store_parent_run_id kwarg is only expected to be used in backwards compatibility e2e tests,
        # it is not expected to be used in production scenarios.
        cache_store_parent_run_id = kwargs.pop('cache_store_parent_run_id', parent_run_id)
        cache_store = init_cache_store(parent_run.experiment, parent_run_id=cache_store_parent_run_id)
        cache_store.load()

    return parent_run, automl_settings_obj, cache_store


def prepare_data(data_preparer: Optional[DataPreparer],
                 automl_settings_obj: AzureAutoMLSettings,
                 script_directory: Optional[str],
                 entry_point: Optional[str],
                 verifier: Optional[VerifierManager] = None) -> Dict[str, Any]:
    if data_preparer:
        data_dict = data_preparer.prepare(automl_settings_obj)
    else:
        if script_directory is None:
            script_directory = ""
        if entry_point is None:
            entry_point = ""
        script_path = os.path.join(script_directory, entry_point)
        if script_path is None:
            script_path = '.'
        user_module = _load_user_script(script_path, False)
        data_dict = training_utilities._extract_user_data(user_module)

    # Set min and max y if needed.
    training_utilities.set_task_parameters(y=data_dict.get('y'),
                                           automl_settings=automl_settings_obj)
    if automl_settings_obj.is_timeseries:
        # Reconstruct the pandas data frames if possible.
        if not isinstance(data_dict['X'], pd.DataFrame) and data_dict.get('x_raw_column_names') is not None:
            data_dict['X'] = pd.DataFrame(data_dict['X'], columns=data_dict.get('x_raw_column_names'))
        if data_dict.get('X_valid') is not None and not isinstance(data_dict.get('X_valid'), pd.DataFrame)\
                and data_dict.get('x_raw_column_names') is not None:
            data_dict['X_valid'] = pd.DataFrame(data_dict['X_valid'], columns=data_dict.get('x_raw_column_names'))
        # Check that each grain column contains exactly one data type.
        data_dict['X'], data_dict['X_valid'] = convert_check_grain_value_types(
            data_dict['X'], data_dict.get('X_valid'), automl_settings_obj.grain_column_names,
            automl_settings_obj.featurization, ReferenceCodes._TS_VALIDATION_GRAIN_TYPE_REMOTE)

        # When data were read try to fix the frequency.
        if data_dict.get('X_valid') is None:
            # todo: This should be part of data preparation, which in turn should happen after data validations.
            #       However, currently validations happen after this step. Once we're able to flip the steps, remove
            #       the reference to common_data_validations.check_dimensions, and in general assume the underlying
            #       structures are valid (e.g. X,y have the same number of rows, have the right dimensions etc.)
            common_data_validations.check_dimensions(data_dict['X'], data_dict['y'], None, None, None, None)
            # If X and y are dataflow object, we need to deserialize it here.
            X = data_dict['X']
            y = data_dict['y']
            fixed_freq_obj = fix_data_set_regularity_may_be(
                X,
                y,
                automl_settings_obj.time_column_name,
                automl_settings_obj.grain_column_names,
                str_to_offset_safe(automl_settings_obj.freq,
                                   ReferenceCodes._REMOTE_SCRIPT_WRONG_FREQ))
            X = fixed_freq_obj.data_x
            data_dict['y'] = fixed_freq_obj.data_y
            failed = fixed_freq_obj.is_failed
            corrected = fixed_freq_obj.is_modified
            freq = fixed_freq_obj.freq
            # Do our best to clean up memory.
            del data_dict['X']
            gc.collect()
            # If we do not have enough memory, raise the exception.
            check_memory_limit(X, data_dict['y'])
            # Pad the short grains if needed (the short_series_handing_config_value is
            # checked by pad_short_grains_or_raise).
            X, data_dict['y'] = short_grain_padding.pad_short_grains_or_raise(
                X, data_dict['y'], freq, automl_settings_obj, ReferenceCodes._TS_ONE_VALUE_PER_GRAIN_RSCRIPT,
                verifier)
            # We may have reordered data frame X reorder it back here.
            X = X[data_dict['x_raw_column_names']]
            # and then copy the data to new location.
            data_dict['X'] = X
            if verifier:
                verifier.update_data_verifier_frequency_inference(failed, corrected)

    data_dict['X'], data_dict['y'], data_dict['sample_weight'], data_dict['X_valid'], data_dict['y_valid'], \
        data_dict['sample_weight_valid'] = rule_based_validation(automl_settings_obj,
                                                                 data_dict.get('X'),
                                                                 data_dict.get('y'),
                                                                 data_dict.get('sample_weight'),
                                                                 data_dict.get('X_valid'),
                                                                 data_dict.get('y_valid'),
                                                                 data_dict.get('sample_weight_valid'),
                                                                 data_dict.get('cv_splits_indices'),
                                                                 verifier=verifier)
    return data_dict


def init_cache_store(experiment: Experiment, parent_run_id: str) -> CacheStore:
    cache_data_store = _get_cache_data_store(experiment)
    return _get_cache_store(data_store=cache_data_store, run_id=parent_run_id)


def _get_cache_store(data_store: Optional[AbstractAzureStorageDatastore], run_id: str) -> CacheStore:
    cache_location = '{0}/{1}'.format('_remote_cache_directory_', run_id)

    os.makedirs(cache_location, exist_ok=True)
    return CacheStoreFactory.get_cache_store(temp_location=cache_location,
                                             run_target=ComputeTargets.AMLCOMPUTE,
                                             run_id=run_id,
                                             data_store=data_store)


def _get_cache_data_store(experiment: Experiment) -> Optional[AbstractAzureStorageDatastore]:
    data_store = None  # type: Optional[AbstractAzureStorageDatastore]
    start = time.time()
    try:
        data_store = Datastore.get(experiment.workspace, WORKSPACE_BLOB_DATASTORE)
        logger.info('Successfully got the cache data store, caching enabled.')
    except HttpOperationError as response_exception:
        logging_utilities.log_traceback(response_exception, logger)
        if response_exception.response.status_code >= 500:
            raise
        else:
            raise UserException.from_exception(response_exception).with_generic_msg(
                'Failed to get default datastore from Datastore Service. HTTP Status code: {}'.format(
                    response_exception.response.status_code)
            )
    end = time.time()
    logger.info('Took {} seconds to retrieve cache data store'.format(end - start))
    return data_store


def load_data_from_cache(cache_store: CacheStore) -> DatasetBase:
    with tracer.start_as_current_span(
            TelemetryConstants.SPAN_FORMATTING.format(
                TelemetryConstants.COMPONENT_NAME, TelemetryConstants.LOAD_CACHED_DATA
            ),
            user_facing_name=TelemetryConstants.LOAD_CACHED_DATA_USER_FACING
    ):
        try:
            cache_store.load()
            dataset_dict = cache_store.get([DATASET_BASE_CACHE_KEY])
            if dataset_dict is not None:
                result = dataset_dict.get(DATASET_BASE_CACHE_KEY, None)  # type: Optional[DatasetBase]
                if result:
                    logger.info('Successfully loaded the AutoML Dataset from cache.')
                    return result
            raise CacheException("Failed to find {} in cache_store.".format(DATASET_BASE_CACHE_KEY), has_pii=False)
        except AutoMLException as e:
            logging_utilities.log_traceback(e, logger, is_critical=False)
            logger.warning("Failed to initialize Datasets from the cache")
            raise
        except Exception as e:
            logging_utilities.log_traceback(e, logger, is_critical=False)
            logger.warning('Fatal exception encountered while trying to load data from cache')
            raise


def _init_logger() -> None:
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(fmt="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
                                  datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    log_server.add_handler('stdout', handler)


def parse_settings(
        current_run: Run,
        automl_settings: str,
        parent_run_id: Optional[str] = None
) -> AzureAutoMLSettings:
    if not os.path.exists(LOGS_AZUREML_DIR):
        os.makedirs(LOGS_AZUREML_DIR, exist_ok=True)
    _init_logger()

    # Don't reuse path from user's local machine for remote runs
    automl_settings_obj = AzureAutoMLSettings.from_string_or_dict(automl_settings, overrides={
        'debug_log': os.path.join(LOGS_AZUREML_DIR, "azureml_automl.log"),
        'path': tempfile.mkdtemp()
    })

    # enable traceback logging for remote runs
    os.environ['AUTOML_MANAGED_ENVIRONMENT'] = '1'

    if parent_run_id is None:
        parent_run_id = get_parent_run_id(current_run.id)

    _logging.set_run_custom_dimensions(
        automl_settings=automl_settings_obj,
        parent_run_id=parent_run_id,
        child_run_id=current_run.id)

    return automl_settings_obj


def _init_directory(directory: Optional[str]) -> str:
    if directory is None:
        directory = os.getcwd()
        logger.info('Directory was None, using current working directory.')

    sys.path.append(directory)
    # create the outputs folder
    logger.info('Creating output folder.')
    os.makedirs('./outputs', exist_ok=True)
    return directory


def get_parent_run_id(run_id: str) -> str:
    """
    Code for getting the AutoML parent run-id from the child run-id.
    :param run_id: This is in format AutoML_<GUID>_*
    :type run_id: str
    :return: str
    """
    try:
        return re.match("((?:AutoML_)?[a-zA-Z0-9-]+)_.+", run_id).group(1)  # type: ignore
    except (IndexError, AttributeError) as e:
        raise ClientException.from_exception(e, "Malformed AutoML child run-id passed", has_pii=False)


def modify_settings_for_streaming(
        automl_settings_obj: AzureAutoMLSettings,
        dataprep_json: str
) -> None:
    """called only from training runs"""
    automl_settings_obj.enable_streaming = True
    # check if UX and update the settings appropriately
    dataprep_json_obj = json.loads(dataprep_json)
    if 'activities' not in dataprep_json_obj:
        # for UI we need to set the label_column_name
        if automl_settings_obj.label_column_name is None:
            automl_settings_obj.label_column_name = dataprep_json_obj.get('label', None)
            logger.info('Set label_column_name')

    if automl_settings_obj.enable_stack_ensembling is True or automl_settings_obj.enable_ensembling is True:
        logger.warning('The training data is large. Ensembling is not available for this run.')
        automl_settings_obj.enable_stack_ensembling = False
        automl_settings_obj.enable_ensembling = False
