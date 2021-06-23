from typing import List

from tecton._internals import metadata_service
from tecton._internals.sdk_decorators import sdk_public_method
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllEntitiesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllFeatureServicesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllSavedFeatureDataFramesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllTransformationsRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllVirtualDataSourcesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import ListWorkspacesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import QueryFeaturePackagesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import QueryFeatureViewsRequest


@sdk_public_method
def list_feature_packages() -> List[str]:
    """
    Returns a list of all registered FeaturePackages.

    :return: A list of strings.
    """
    request = QueryFeaturePackagesRequest()
    response = metadata_service.instance().QueryFeaturePackages(request)
    return [proto.fco_metadata.name for proto in response.feature_packages]


@sdk_public_method
def list_feature_views() -> List[str]:
    """
    Returns a list of all registered FeatureViews.

    :return: A list of strings.
    """
    request = QueryFeatureViewsRequest()
    response = metadata_service.instance().QueryFeatureViews(request)
    return [proto.fco_metadata.name for proto in response.feature_views if not proto.HasField("feature_table")]


@sdk_public_method
def list_feature_tables() -> List[str]:
    """
    Returns a list of all registered FeatureTables.

    :return: A list of strings.
    """
    request = QueryFeatureViewsRequest()
    response = metadata_service.instance().QueryFeatureViews(request)
    return [proto.fco_metadata.name for proto in response.feature_views if proto.HasField("feature_table")]


@sdk_public_method
def list_feature_services() -> List[str]:
    """
    Returns a list of all registered FeatureServices.

    :return: A list of strings.
    """
    request = GetAllFeatureServicesRequest()
    response = metadata_service.instance().GetAllFeatureServices(request)
    return [proto.fco_metadata.name for proto in response.feature_services]


@sdk_public_method
def list_transformations() -> List[str]:
    """
    Returns a list of all registered Transformations.

    :return: A list of strings.
    """
    request = GetAllTransformationsRequest()
    response = metadata_service.instance().GetAllTransformations(request)
    return [proto.fco_metadata.name for proto in response.transformations]


@sdk_public_method
def list_new_transformations() -> List[str]:
    """
    Returns a list of all registered Transformations.

    :return: A list of strings.
    """
    request = GetAllTransformationsRequest()
    response = metadata_service.instance().GetAllTransformations(request)
    return [proto.fco_metadata.name for proto in response.new_transformations]


@sdk_public_method
def list_entities() -> List[str]:
    """
    Returns a list of all registered Entities.

    :returns: A list of strings.
    """
    request = GetAllEntitiesRequest()
    response = metadata_service.instance().GetAllEntities(request)
    return [proto.fco_metadata.name for proto in response.entities]


@sdk_public_method
def list_virtual_data_sources() -> List[str]:
    """
    Returns a list of all registered VirtualDataSources.

    :return: A list of strings.
    """
    request = GetAllVirtualDataSourcesRequest()
    response = metadata_service.instance().GetAllVirtualDataSources(request)
    return [proto.fco_metadata.name for proto in response.virtual_data_sources]


@sdk_public_method
def list_data_sources() -> List[str]:
    """
    Returns a list of the names of all registered Data Sources.

    :return: A list of strings.
    """
    request = GetAllVirtualDataSourcesRequest()
    response = metadata_service.instance().GetAllVirtualDataSources(request)
    return [proto.fco_metadata.name for proto in response.virtual_data_sources]


@sdk_public_method
def list_workspaces() -> List[str]:
    """
    Returns a list of all registered Workspaces.

    :return: A list of strings.
    """
    request = ListWorkspacesRequest()
    response = metadata_service.instance().ListWorkspaces(request)
    # add "prod" which is not stored by name internally
    workspace_names = ["prod"] + [workspace.name for workspace in response.workspaces]
    return workspace_names


@sdk_public_method
def list_datasets() -> List[str]:
    """
    Returns a list of all registered Datasets.

    :return: A list of strings.
    """
    request = GetAllSavedFeatureDataFramesRequest()
    response = metadata_service.instance().GetAllSavedFeatureDataFrames(request)
    return [sfdf.info.name for sfdf in response.saved_feature_dataframes]
