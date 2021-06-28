"""
Type annotations for mgh service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef

    data: ApplicationStateTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import ApplicationStatusType, ResourceAttributeTypeType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationStateTypeDef",
    "AssociateCreatedArtifactRequestTypeDef",
    "AssociateDiscoveredResourceRequestTypeDef",
    "CreateProgressUpdateStreamRequestTypeDef",
    "CreatedArtifactTypeDef",
    "DeleteProgressUpdateStreamRequestTypeDef",
    "DescribeApplicationStateRequestTypeDef",
    "DescribeApplicationStateResultResponseTypeDef",
    "DescribeMigrationTaskRequestTypeDef",
    "DescribeMigrationTaskResultResponseTypeDef",
    "DisassociateCreatedArtifactRequestTypeDef",
    "DisassociateDiscoveredResourceRequestTypeDef",
    "DiscoveredResourceTypeDef",
    "ImportMigrationTaskRequestTypeDef",
    "ListApplicationStatesRequestTypeDef",
    "ListApplicationStatesResultResponseTypeDef",
    "ListCreatedArtifactsRequestTypeDef",
    "ListCreatedArtifactsResultResponseTypeDef",
    "ListDiscoveredResourcesRequestTypeDef",
    "ListDiscoveredResourcesResultResponseTypeDef",
    "ListMigrationTasksRequestTypeDef",
    "ListMigrationTasksResultResponseTypeDef",
    "ListProgressUpdateStreamsRequestTypeDef",
    "ListProgressUpdateStreamsResultResponseTypeDef",
    "MigrationTaskSummaryTypeDef",
    "MigrationTaskTypeDef",
    "NotifyApplicationStateRequestTypeDef",
    "NotifyMigrationTaskStateRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "PutResourceAttributesRequestTypeDef",
    "ResourceAttributeTypeDef",
    "ResponseMetadataTypeDef",
    "TaskTypeDef",
)

ApplicationStateTypeDef = TypedDict(
    "ApplicationStateTypeDef",
    {
        "ApplicationId": str,
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredAssociateCreatedArtifactRequestTypeDef = TypedDict(
    "_RequiredAssociateCreatedArtifactRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifact": "CreatedArtifactTypeDef",
    },
)
_OptionalAssociateCreatedArtifactRequestTypeDef = TypedDict(
    "_OptionalAssociateCreatedArtifactRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateCreatedArtifactRequestTypeDef(
    _RequiredAssociateCreatedArtifactRequestTypeDef, _OptionalAssociateCreatedArtifactRequestTypeDef
):
    pass


_RequiredAssociateDiscoveredResourceRequestTypeDef = TypedDict(
    "_RequiredAssociateDiscoveredResourceRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "DiscoveredResource": "DiscoveredResourceTypeDef",
    },
)
_OptionalAssociateDiscoveredResourceRequestTypeDef = TypedDict(
    "_OptionalAssociateDiscoveredResourceRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateDiscoveredResourceRequestTypeDef(
    _RequiredAssociateDiscoveredResourceRequestTypeDef,
    _OptionalAssociateDiscoveredResourceRequestTypeDef,
):
    pass


_RequiredCreateProgressUpdateStreamRequestTypeDef = TypedDict(
    "_RequiredCreateProgressUpdateStreamRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
    },
)
_OptionalCreateProgressUpdateStreamRequestTypeDef = TypedDict(
    "_OptionalCreateProgressUpdateStreamRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateProgressUpdateStreamRequestTypeDef(
    _RequiredCreateProgressUpdateStreamRequestTypeDef,
    _OptionalCreateProgressUpdateStreamRequestTypeDef,
):
    pass


_RequiredCreatedArtifactTypeDef = TypedDict(
    "_RequiredCreatedArtifactTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatedArtifactTypeDef = TypedDict(
    "_OptionalCreatedArtifactTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreatedArtifactTypeDef(_RequiredCreatedArtifactTypeDef, _OptionalCreatedArtifactTypeDef):
    pass


_RequiredDeleteProgressUpdateStreamRequestTypeDef = TypedDict(
    "_RequiredDeleteProgressUpdateStreamRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
    },
)
_OptionalDeleteProgressUpdateStreamRequestTypeDef = TypedDict(
    "_OptionalDeleteProgressUpdateStreamRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteProgressUpdateStreamRequestTypeDef(
    _RequiredDeleteProgressUpdateStreamRequestTypeDef,
    _OptionalDeleteProgressUpdateStreamRequestTypeDef,
):
    pass


DescribeApplicationStateRequestTypeDef = TypedDict(
    "DescribeApplicationStateRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DescribeApplicationStateResultResponseTypeDef = TypedDict(
    "DescribeApplicationStateResultResponseTypeDef",
    {
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMigrationTaskRequestTypeDef = TypedDict(
    "DescribeMigrationTaskRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)

DescribeMigrationTaskResultResponseTypeDef = TypedDict(
    "DescribeMigrationTaskResultResponseTypeDef",
    {
        "MigrationTask": "MigrationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateCreatedArtifactRequestTypeDef = TypedDict(
    "_RequiredDisassociateCreatedArtifactRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifactName": str,
    },
)
_OptionalDisassociateCreatedArtifactRequestTypeDef = TypedDict(
    "_OptionalDisassociateCreatedArtifactRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateCreatedArtifactRequestTypeDef(
    _RequiredDisassociateCreatedArtifactRequestTypeDef,
    _OptionalDisassociateCreatedArtifactRequestTypeDef,
):
    pass


_RequiredDisassociateDiscoveredResourceRequestTypeDef = TypedDict(
    "_RequiredDisassociateDiscoveredResourceRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ConfigurationId": str,
    },
)
_OptionalDisassociateDiscoveredResourceRequestTypeDef = TypedDict(
    "_OptionalDisassociateDiscoveredResourceRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateDiscoveredResourceRequestTypeDef(
    _RequiredDisassociateDiscoveredResourceRequestTypeDef,
    _OptionalDisassociateDiscoveredResourceRequestTypeDef,
):
    pass


_RequiredDiscoveredResourceTypeDef = TypedDict(
    "_RequiredDiscoveredResourceTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalDiscoveredResourceTypeDef = TypedDict(
    "_OptionalDiscoveredResourceTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class DiscoveredResourceTypeDef(
    _RequiredDiscoveredResourceTypeDef, _OptionalDiscoveredResourceTypeDef
):
    pass


_RequiredImportMigrationTaskRequestTypeDef = TypedDict(
    "_RequiredImportMigrationTaskRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalImportMigrationTaskRequestTypeDef = TypedDict(
    "_OptionalImportMigrationTaskRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ImportMigrationTaskRequestTypeDef(
    _RequiredImportMigrationTaskRequestTypeDef, _OptionalImportMigrationTaskRequestTypeDef
):
    pass


ListApplicationStatesRequestTypeDef = TypedDict(
    "ListApplicationStatesRequestTypeDef",
    {
        "ApplicationIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListApplicationStatesResultResponseTypeDef = TypedDict(
    "ListApplicationStatesResultResponseTypeDef",
    {
        "ApplicationStateList": List["ApplicationStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCreatedArtifactsRequestTypeDef = TypedDict(
    "_RequiredListCreatedArtifactsRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalListCreatedArtifactsRequestTypeDef = TypedDict(
    "_OptionalListCreatedArtifactsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListCreatedArtifactsRequestTypeDef(
    _RequiredListCreatedArtifactsRequestTypeDef, _OptionalListCreatedArtifactsRequestTypeDef
):
    pass


ListCreatedArtifactsResultResponseTypeDef = TypedDict(
    "ListCreatedArtifactsResultResponseTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List["CreatedArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDiscoveredResourcesRequestTypeDef = TypedDict(
    "_RequiredListDiscoveredResourcesRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
_OptionalListDiscoveredResourcesRequestTypeDef = TypedDict(
    "_OptionalListDiscoveredResourcesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDiscoveredResourcesRequestTypeDef(
    _RequiredListDiscoveredResourcesRequestTypeDef, _OptionalListDiscoveredResourcesRequestTypeDef
):
    pass


ListDiscoveredResourcesResultResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResultResponseTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List["DiscoveredResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMigrationTasksRequestTypeDef = TypedDict(
    "ListMigrationTasksRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResourceName": str,
    },
    total=False,
)

ListMigrationTasksResultResponseTypeDef = TypedDict(
    "ListMigrationTasksResultResponseTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List["MigrationTaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProgressUpdateStreamsRequestTypeDef = TypedDict(
    "ListProgressUpdateStreamsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProgressUpdateStreamsResultResponseTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultResponseTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List["ProgressUpdateStreamSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MigrationTaskSummaryTypeDef = TypedDict(
    "MigrationTaskSummaryTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": StatusType,
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)

MigrationTaskTypeDef = TypedDict(
    "MigrationTaskTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": "TaskTypeDef",
        "UpdateDateTime": datetime,
        "ResourceAttributeList": List["ResourceAttributeTypeDef"],
    },
    total=False,
)

_RequiredNotifyApplicationStateRequestTypeDef = TypedDict(
    "_RequiredNotifyApplicationStateRequestTypeDef",
    {
        "ApplicationId": str,
        "Status": ApplicationStatusType,
    },
)
_OptionalNotifyApplicationStateRequestTypeDef = TypedDict(
    "_OptionalNotifyApplicationStateRequestTypeDef",
    {
        "UpdateDateTime": Union[datetime, str],
        "DryRun": bool,
    },
    total=False,
)


class NotifyApplicationStateRequestTypeDef(
    _RequiredNotifyApplicationStateRequestTypeDef, _OptionalNotifyApplicationStateRequestTypeDef
):
    pass


_RequiredNotifyMigrationTaskStateRequestTypeDef = TypedDict(
    "_RequiredNotifyMigrationTaskStateRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": "TaskTypeDef",
        "UpdateDateTime": Union[datetime, str],
        "NextUpdateSeconds": int,
    },
)
_OptionalNotifyMigrationTaskStateRequestTypeDef = TypedDict(
    "_OptionalNotifyMigrationTaskStateRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class NotifyMigrationTaskStateRequestTypeDef(
    _RequiredNotifyMigrationTaskStateRequestTypeDef, _OptionalNotifyMigrationTaskStateRequestTypeDef
):
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

ProgressUpdateStreamSummaryTypeDef = TypedDict(
    "ProgressUpdateStreamSummaryTypeDef",
    {
        "ProgressUpdateStreamName": str,
    },
    total=False,
)

_RequiredPutResourceAttributesRequestTypeDef = TypedDict(
    "_RequiredPutResourceAttributesRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ResourceAttributeList": List["ResourceAttributeTypeDef"],
    },
)
_OptionalPutResourceAttributesRequestTypeDef = TypedDict(
    "_OptionalPutResourceAttributesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class PutResourceAttributesRequestTypeDef(
    _RequiredPutResourceAttributesRequestTypeDef, _OptionalPutResourceAttributesRequestTypeDef
):
    pass


ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
    },
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

_RequiredTaskTypeDef = TypedDict(
    "_RequiredTaskTypeDef",
    {
        "Status": StatusType,
    },
)
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef",
    {
        "StatusDetail": str,
        "ProgressPercent": int,
    },
    total=False,
)


class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass
