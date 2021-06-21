# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""The module handles the upload and download of the causal insights to run history."""
import json
import os
from typing import Callable, Dict, List, Optional, Any
import uuid

from azureml.core.run import Run

from azureml._base_sdk_common._docstring_wrapper import experimental
from azureml._common._error_definition import AzureMLError
from azureml._restclient.assets_client import AssetsClient
from azureml.exceptions import UserErrorException

from azureml.responsibleai.common._constants import RAITool, AssetProperties
from azureml.responsibleai.common._errors.error_definitions import ArgumentInvalidTypeError
from azureml.responsibleai.common._search_assets import (
    list_rai_tool, search_rai_assets, get_asset_name_rai_tool,
    get_asset_type_rai_tool)
from azureml.responsibleai.common.rai_artifact_client import RAIArtifactClient
from azureml.responsibleai.common.rai_validations import (
    _check_serialization_size, _check_against_json_schema)


class _CausalEffectsConstants:
    RawFeatureNameKey = 'raw_name'
    EngineeredNameKey = 'name'
    CategoricalColumnKey = 'cat'
    TypeKey = 'type'
    PointKey = 'point'
    ZStatKey = 'zstat'
    StdErrKey = 'stderr'
    ConfidenceIntervalLowerKey = 'ci_lower'
    ConfidenceIntervalUpperKey = 'ci_upper'
    PValueKey = 'p_value'
    VersionKey = 'version'
    CausalComputationTypeKey = 'causal_computation_type'
    ConfoundingIntervalKey = 'confounding_interval'
    ViewKey = 'view'

    ALL = [RawFeatureNameKey,
           EngineeredNameKey,
           CategoricalColumnKey,
           TypeKey,
           PointKey,
           ZStatKey,
           StdErrKey,
           ConfidenceIntervalLowerKey,
           ConfidenceIntervalUpperKey,
           PValueKey,
           VersionKey,
           CausalComputationTypeKey,
           ConfoundingIntervalKey,
           ViewKey]

    NON_LIST_TYPE_KEYS = [VersionKey,
                          CausalComputationTypeKey,
                          ConfoundingIntervalKey,
                          ViewKey]


CAUSAL_EFFECTS_UPLOAD_BYTES_LIMIT = 20 * 1024 * 1024


def _check_causal_effect_output_against_json_schema(causal_effects_dict):
    """
    Validate the dictionary version of the causal effects.

    :param causal_effects_dict: Serialized version of the causal effects.
    :type causal_effects_dict: Dict
    """
    schema_path = os.path.join(os.path.dirname(__file__),
                               'causal_effects_output_v0.0.json')
    with open(schema_path, 'r') as schema_file:
        schema_json = json.load(schema_file)

    _check_against_json_schema(schema_json, causal_effects_dict)


def _validate_causal_effects_dict(causal_effects: Dict) -> None:
    """
    Validate the serialized version of the causal effects.

    :param causal_effects: Serialized version of the causal effects.
    :type causal_effects: Dict
    """
    if not isinstance(causal_effects, dict):
        raise UserErrorException._with_error(
            AzureMLError.create(
                ArgumentInvalidTypeError,
                arg_name='causal_effects',
                type=type(causal_effects),
                type_list=['dict'],
            )
        )

    _check_serialization_size(json.dumps(causal_effects),
                              CAUSAL_EFFECTS_UPLOAD_BYTES_LIMIT)

    # Verify the outputs against json schema
    _check_causal_effect_output_against_json_schema(causal_effects)

    # TODO: Verify if the lengths of all values is same


@experimental
def upload_causal_effects(run: Run,
                          causal_effects: Dict,
                          comment: Optional[str] = None,
                          datastore_name: Optional[str] = None) -> None:
    """Upload the causal effects to the run.

    :param run: A Run object into which the causal effects need to be uploaded.
    :type run: azureml.core.Run
    :param causal_effects: The dictionary containing the causal effects.
    :type causal_effects: Dict
    :param datastore_name: The datastore to which the causal_effects should be uploaded
    :type datastore_name: str
    :param comment: An optional string to identify the causal effects.
                    The string is displayed when listing causal effects,
                    which allows identification of uploaded causal effects.
    :type comment: str
    """
    def no_updates(props: Dict[str, str]) -> None:
        pass

    _upload_causal_effects_internal(run,
                                    causal_effects,
                                    get_asset_type_rai_tool(RAITool.CAUSAL),
                                    no_updates,
                                    comment,
                                    datastore_name)


def _upload_causal_effects_internal(run: Run,
                                    causal_effects: Dict,
                                    asset_type: str,
                                    update_properties: Callable[[Dict[str, str]], None],
                                    comment: Optional[str] = None,
                                    datastore_name: Optional[str] = None) -> str:
    """Upload the causal effects to the run.

    :param run: A Run object into which the causal effects need to be uploaded.
    :type run: azureml.core.Run
    :param causal_effects: The dictionary containing the causal effects.
    :type causal_effects: Dict
    :param asset_type: Specifies the 'type' field of the created Asset
    :type asset_type: str
    :param update_properties: Callable which can modify the properties of the created Asset
    :type update_properties: Callable
    :param comment: An optional string to identify the causal effects.
                    The string is displayed when listing causal effects,
                    which allows identification of uploaded causal effects.
    :type comment: str
    :param datastore_name: The datastore to which the causal_effects should be uploaded
    :type datastore_name: str
    :return: The id of the created Asset.
    :rtype: str
    """
    _validate_causal_effects_dict(causal_effects=causal_effects)
    upload_id = str(uuid.uuid4())

    assets_client = AssetsClient(run.experiment.workspace.service_context)
    asset_artifact_list = []
    asset_properties = {}
    asset_properties[AssetProperties.UPLOAD_ID] = upload_id
    if comment is not None:
        asset_properties[AssetProperties.COMMENT] = comment

    rai_causal_artifact_client = RAIArtifactClient(run, datastore_name)
    for causal_effects_key in _CausalEffectsConstants.ALL:
        artifact_upload_return_code = rai_causal_artifact_client.upload_single_object(
            target=causal_effects[causal_effects_key],
            artifact_area_path=get_asset_name_rai_tool(RAITool.CAUSAL),
            upload_id=upload_id,
            artifact_type=causal_effects_key)
        asset_artifact_list.append(artifact_upload_return_code)

    # Call the supplied function to modify the properties if required
    update_properties(asset_properties)

    asset = assets_client.create_asset(
        model_name=get_asset_name_rai_tool(RAITool.CAUSAL),
        artifact_values=asset_artifact_list,
        metadata_dict={},
        run_id=run.id,
        properties=asset_properties,
        asset_type=asset_type)
    return asset.id


@experimental
def download_causal_effects(run: Run, causal_effects_upload_id: Optional[str] = None,
                            comment: Optional[str] = None) -> Dict:
    """Download the causal effects that were previously uploaded in the run.

    :param run: A Run object from which the causal effects need to be downloaded.
    :type run: azureml.core.Run
    :param causal_effects_upload_id: If specified, tries to download the causal effects
                                     from the run with the given causal effects ID.
                                     If unspecified, returns the most recently uploaded
                                     causal effects.
    :type causal_effects_upload_id: str
    :param comment: A string used to download the causal effects based on the comment
                    they were uploaded with. Requires an exact match.
    :type comment: str
    :return: The dictionary containing all the causal effects.
    :rtype: Dict
    """
    upload_id = search_rai_assets(run=run, rai_tool=RAITool.CAUSAL,
                                  query_upload_id=causal_effects_upload_id,
                                  query_comment=comment)
    downloaded_causal_effects = {}

    # When downloading, the datastore_name is not used
    rai_causal_artifact_client = RAIArtifactClient(run)
    for causal_effects_key in _CausalEffectsConstants.ALL:
        downloaded_causal_effects[causal_effects_key] = \
            rai_causal_artifact_client.download_single_object(
                artifact_area_path=get_asset_name_rai_tool(RAITool.CAUSAL),
                upload_id=upload_id,
                artifact_type=causal_effects_key)

    _check_causal_effect_output_against_json_schema(downloaded_causal_effects)

    return downloaded_causal_effects


@experimental
def list_causal_effects(run: Run, comment: Optional[str] = None) -> List[Dict[Any, Any]]:
    """Get the list of upload_ids of the causal effects available to a given Run.

    :param run: A Run object from which the causal effects need to be queried.
    :type run: azureml.core.Run
    :param comment: A string used to filter causal effects based on the strings
                    they were uploaded with. Requires an exact match.
    :type comment: str
    :return: A list of dictionaries with upload GUIDs, comment and upload time of the uploaded
             causal effects.
    :rtype: list[Dict]
    """
    return list_rai_tool(run=run, rai_tool=RAITool.CAUSAL, comment=comment)
