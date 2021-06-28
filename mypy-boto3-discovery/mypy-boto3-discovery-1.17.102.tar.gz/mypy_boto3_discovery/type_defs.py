"""
Type annotations for discovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef

    data: AgentConfigurationStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentStatusType,
    BatchDeleteImportDataErrorCodeType,
    ConfigurationItemTypeType,
    ContinuousExportStatusType,
    ExportDataFormatType,
    ExportStatusType,
    ImportStatusType,
    ImportTaskFilterNameType,
    orderStringType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgentConfigurationStatusTypeDef",
    "AgentInfoTypeDef",
    "AgentNetworkInfoTypeDef",
    "AssociateConfigurationItemsToApplicationRequestTypeDef",
    "BatchDeleteImportDataErrorTypeDef",
    "BatchDeleteImportDataRequestTypeDef",
    "BatchDeleteImportDataResponseResponseTypeDef",
    "ConfigurationTagTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseResponseTypeDef",
    "CreateTagsRequestTypeDef",
    "CustomerAgentInfoTypeDef",
    "CustomerConnectorInfoTypeDef",
    "DeleteApplicationsRequestTypeDef",
    "DeleteTagsRequestTypeDef",
    "DescribeAgentsRequestTypeDef",
    "DescribeAgentsResponseResponseTypeDef",
    "DescribeConfigurationsRequestTypeDef",
    "DescribeConfigurationsResponseResponseTypeDef",
    "DescribeContinuousExportsRequestTypeDef",
    "DescribeContinuousExportsResponseResponseTypeDef",
    "DescribeExportConfigurationsRequestTypeDef",
    "DescribeExportConfigurationsResponseResponseTypeDef",
    "DescribeExportTasksRequestTypeDef",
    "DescribeExportTasksResponseResponseTypeDef",
    "DescribeImportTasksRequestTypeDef",
    "DescribeImportTasksResponseResponseTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResponseResponseTypeDef",
    "DisassociateConfigurationItemsFromApplicationRequestTypeDef",
    "ExportConfigurationsResponseResponseTypeDef",
    "ExportFilterTypeDef",
    "ExportInfoTypeDef",
    "FilterTypeDef",
    "GetDiscoverySummaryResponseResponseTypeDef",
    "ImportTaskFilterTypeDef",
    "ImportTaskTypeDef",
    "ListConfigurationsRequestTypeDef",
    "ListConfigurationsResponseResponseTypeDef",
    "ListServerNeighborsRequestTypeDef",
    "ListServerNeighborsResponseResponseTypeDef",
    "NeighborConnectionDetailTypeDef",
    "OrderByElementTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartContinuousExportResponseResponseTypeDef",
    "StartDataCollectionByAgentIdsRequestTypeDef",
    "StartDataCollectionByAgentIdsResponseResponseTypeDef",
    "StartExportTaskRequestTypeDef",
    "StartExportTaskResponseResponseTypeDef",
    "StartImportTaskRequestTypeDef",
    "StartImportTaskResponseResponseTypeDef",
    "StopContinuousExportRequestTypeDef",
    "StopContinuousExportResponseResponseTypeDef",
    "StopDataCollectionByAgentIdsRequestTypeDef",
    "StopDataCollectionByAgentIdsResponseResponseTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "UpdateApplicationRequestTypeDef",
)

AgentConfigurationStatusTypeDef = TypedDict(
    "AgentConfigurationStatusTypeDef",
    {
        "agentId": str,
        "operationSucceeded": bool,
        "description": str,
    },
    total=False,
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List["AgentNetworkInfoTypeDef"],
        "connectorId": str,
        "version": str,
        "health": AgentStatusType,
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

AgentNetworkInfoTypeDef = TypedDict(
    "AgentNetworkInfoTypeDef",
    {
        "ipAddress": str,
        "macAddress": str,
    },
    total=False,
)

AssociateConfigurationItemsToApplicationRequestTypeDef = TypedDict(
    "AssociateConfigurationItemsToApplicationRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": List[str],
    },
)

BatchDeleteImportDataErrorTypeDef = TypedDict(
    "BatchDeleteImportDataErrorTypeDef",
    {
        "importTaskId": str,
        "errorCode": BatchDeleteImportDataErrorCodeType,
        "errorDescription": str,
    },
    total=False,
)

BatchDeleteImportDataRequestTypeDef = TypedDict(
    "BatchDeleteImportDataRequestTypeDef",
    {
        "importTaskIds": List[str],
    },
)

BatchDeleteImportDataResponseResponseTypeDef = TypedDict(
    "BatchDeleteImportDataResponseResponseTypeDef",
    {
        "errors": List["BatchDeleteImportDataErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationTagTypeDef = TypedDict(
    "ConfigurationTagTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)

ContinuousExportDescriptionTypeDef = TypedDict(
    "ContinuousExportDescriptionTypeDef",
    {
        "exportId": str,
        "status": ContinuousExportStatusType,
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateApplicationResponseResponseTypeDef = TypedDict(
    "CreateApplicationResponseResponseTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestTypeDef = TypedDict(
    "CreateTagsRequestTypeDef",
    {
        "configurationIds": List[str],
        "tags": List["TagTypeDef"],
    },
)

CustomerAgentInfoTypeDef = TypedDict(
    "CustomerAgentInfoTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
)

CustomerConnectorInfoTypeDef = TypedDict(
    "CustomerConnectorInfoTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
)

DeleteApplicationsRequestTypeDef = TypedDict(
    "DeleteApplicationsRequestTypeDef",
    {
        "configurationIds": List[str],
    },
)

_RequiredDeleteTagsRequestTypeDef = TypedDict(
    "_RequiredDeleteTagsRequestTypeDef",
    {
        "configurationIds": List[str],
    },
)
_OptionalDeleteTagsRequestTypeDef = TypedDict(
    "_OptionalDeleteTagsRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class DeleteTagsRequestTypeDef(
    _RequiredDeleteTagsRequestTypeDef, _OptionalDeleteTagsRequestTypeDef
):
    pass


DescribeAgentsRequestTypeDef = TypedDict(
    "DescribeAgentsRequestTypeDef",
    {
        "agentIds": List[str],
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeAgentsResponseResponseTypeDef = TypedDict(
    "DescribeAgentsResponseResponseTypeDef",
    {
        "agentsInfo": List["AgentInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationsRequestTypeDef = TypedDict(
    "DescribeConfigurationsRequestTypeDef",
    {
        "configurationIds": List[str],
    },
)

DescribeConfigurationsResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationsResponseResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousExportsRequestTypeDef = TypedDict(
    "DescribeContinuousExportsRequestTypeDef",
    {
        "exportIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeContinuousExportsResponseResponseTypeDef = TypedDict(
    "DescribeContinuousExportsResponseResponseTypeDef",
    {
        "descriptions": List["ContinuousExportDescriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportConfigurationsRequestTypeDef = TypedDict(
    "DescribeExportConfigurationsRequestTypeDef",
    {
        "exportIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeExportConfigurationsResponseResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsResponseResponseTypeDef",
    {
        "exportsInfo": List["ExportInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestTypeDef",
    {
        "exportIds": List[str],
        "filters": List["ExportFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeExportTasksResponseResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseResponseTypeDef",
    {
        "exportsInfo": List["ExportInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportTasksRequestTypeDef = TypedDict(
    "DescribeImportTasksRequestTypeDef",
    {
        "filters": List["ImportTaskFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeImportTasksResponseResponseTypeDef = TypedDict(
    "DescribeImportTasksResponseResponseTypeDef",
    {
        "nextToken": str,
        "tasks": List["ImportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestTypeDef = TypedDict(
    "DescribeTagsRequestTypeDef",
    {
        "filters": List["TagFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeTagsResponseResponseTypeDef = TypedDict(
    "DescribeTagsResponseResponseTypeDef",
    {
        "tags": List["ConfigurationTagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateConfigurationItemsFromApplicationRequestTypeDef = TypedDict(
    "DisassociateConfigurationItemsFromApplicationRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": List[str],
    },
)

ExportConfigurationsResponseResponseTypeDef = TypedDict(
    "ExportConfigurationsResponseResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": str,
        "values": List[str],
        "condition": str,
    },
)

_RequiredExportInfoTypeDef = TypedDict(
    "_RequiredExportInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "statusMessage": str,
        "exportRequestTime": datetime,
    },
)
_OptionalExportInfoTypeDef = TypedDict(
    "_OptionalExportInfoTypeDef",
    {
        "configurationsDownloadUrl": str,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class ExportInfoTypeDef(_RequiredExportInfoTypeDef, _OptionalExportInfoTypeDef):
    pass


FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
        "condition": str,
    },
)

GetDiscoverySummaryResponseResponseTypeDef = TypedDict(
    "GetDiscoverySummaryResponseResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": "CustomerAgentInfoTypeDef",
        "connectorSummary": "CustomerConnectorInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportTaskFilterTypeDef = TypedDict(
    "ImportTaskFilterTypeDef",
    {
        "name": ImportTaskFilterNameType,
        "values": List[str],
    },
    total=False,
)

ImportTaskTypeDef = TypedDict(
    "ImportTaskTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": ImportStatusType,
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)

_RequiredListConfigurationsRequestTypeDef = TypedDict(
    "_RequiredListConfigurationsRequestTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
    },
)
_OptionalListConfigurationsRequestTypeDef = TypedDict(
    "_OptionalListConfigurationsRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "orderBy": List["OrderByElementTypeDef"],
    },
    total=False,
)


class ListConfigurationsRequestTypeDef(
    _RequiredListConfigurationsRequestTypeDef, _OptionalListConfigurationsRequestTypeDef
):
    pass


ListConfigurationsResponseResponseTypeDef = TypedDict(
    "ListConfigurationsResponseResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServerNeighborsRequestTypeDef = TypedDict(
    "_RequiredListServerNeighborsRequestTypeDef",
    {
        "configurationId": str,
    },
)
_OptionalListServerNeighborsRequestTypeDef = TypedDict(
    "_OptionalListServerNeighborsRequestTypeDef",
    {
        "portInformationNeeded": bool,
        "neighborConfigurationIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListServerNeighborsRequestTypeDef(
    _RequiredListServerNeighborsRequestTypeDef, _OptionalListServerNeighborsRequestTypeDef
):
    pass


ListServerNeighborsResponseResponseTypeDef = TypedDict(
    "ListServerNeighborsResponseResponseTypeDef",
    {
        "neighbors": List["NeighborConnectionDetailTypeDef"],
        "nextToken": str,
        "knownDependencyCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNeighborConnectionDetailTypeDef = TypedDict(
    "_RequiredNeighborConnectionDetailTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "connectionsCount": int,
    },
)
_OptionalNeighborConnectionDetailTypeDef = TypedDict(
    "_OptionalNeighborConnectionDetailTypeDef",
    {
        "destinationPort": int,
        "transportProtocol": str,
    },
    total=False,
)


class NeighborConnectionDetailTypeDef(
    _RequiredNeighborConnectionDetailTypeDef, _OptionalNeighborConnectionDetailTypeDef
):
    pass


_RequiredOrderByElementTypeDef = TypedDict(
    "_RequiredOrderByElementTypeDef",
    {
        "fieldName": str,
    },
)
_OptionalOrderByElementTypeDef = TypedDict(
    "_OptionalOrderByElementTypeDef",
    {
        "sortOrder": orderStringType,
    },
    total=False,
)


class OrderByElementTypeDef(_RequiredOrderByElementTypeDef, _OptionalOrderByElementTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

StartContinuousExportResponseResponseTypeDef = TypedDict(
    "StartContinuousExportResponseResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDataCollectionByAgentIdsRequestTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsRequestTypeDef",
    {
        "agentIds": List[str],
    },
)

StartDataCollectionByAgentIdsResponseResponseTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsResponseResponseTypeDef",
    {
        "agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartExportTaskRequestTypeDef = TypedDict(
    "StartExportTaskRequestTypeDef",
    {
        "exportDataFormat": List[ExportDataFormatType],
        "filters": List["ExportFilterTypeDef"],
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
    total=False,
)

StartExportTaskResponseResponseTypeDef = TypedDict(
    "StartExportTaskResponseResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportTaskRequestTypeDef = TypedDict(
    "_RequiredStartImportTaskRequestTypeDef",
    {
        "name": str,
        "importUrl": str,
    },
)
_OptionalStartImportTaskRequestTypeDef = TypedDict(
    "_OptionalStartImportTaskRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class StartImportTaskRequestTypeDef(
    _RequiredStartImportTaskRequestTypeDef, _OptionalStartImportTaskRequestTypeDef
):
    pass


StartImportTaskResponseResponseTypeDef = TypedDict(
    "StartImportTaskResponseResponseTypeDef",
    {
        "task": "ImportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContinuousExportRequestTypeDef = TypedDict(
    "StopContinuousExportRequestTypeDef",
    {
        "exportId": str,
    },
)

StopContinuousExportResponseResponseTypeDef = TypedDict(
    "StopContinuousExportResponseResponseTypeDef",
    {
        "startTime": datetime,
        "stopTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDataCollectionByAgentIdsRequestTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsRequestTypeDef",
    {
        "agentIds": List[str],
    },
)

StopDataCollectionByAgentIdsResponseResponseTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsResponseResponseTypeDef",
    {
        "agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredUpdateApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestTypeDef",
    {
        "configurationId": str,
    },
)
_OptionalUpdateApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)


class UpdateApplicationRequestTypeDef(
    _RequiredUpdateApplicationRequestTypeDef, _OptionalUpdateApplicationRequestTypeDef
):
    pass
