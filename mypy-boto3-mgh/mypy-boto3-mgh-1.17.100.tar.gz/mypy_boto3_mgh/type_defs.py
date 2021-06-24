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
from typing import List

from .literals import ApplicationStatusType, ResourceAttributeTypeType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationStateTypeDef",
    "CreatedArtifactTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "DescribeMigrationTaskResultTypeDef",
    "DiscoveredResourceTypeDef",
    "ListApplicationStatesResultTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "MigrationTaskSummaryTypeDef",
    "MigrationTaskTypeDef",
    "PaginatorConfigTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "ResourceAttributeTypeDef",
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


DescribeApplicationStateResultTypeDef = TypedDict(
    "DescribeApplicationStateResultTypeDef",
    {
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DescribeMigrationTaskResultTypeDef = TypedDict(
    "DescribeMigrationTaskResultTypeDef",
    {
        "MigrationTask": "MigrationTaskTypeDef",
    },
    total=False,
)

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


ListApplicationStatesResultTypeDef = TypedDict(
    "ListApplicationStatesResultTypeDef",
    {
        "ApplicationStateList": List["ApplicationStateTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCreatedArtifactsResultTypeDef = TypedDict(
    "ListCreatedArtifactsResultTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List["CreatedArtifactTypeDef"],
    },
    total=False,
)

ListDiscoveredResourcesResultTypeDef = TypedDict(
    "ListDiscoveredResourcesResultTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List["DiscoveredResourceTypeDef"],
    },
    total=False,
)

ListMigrationTasksResultTypeDef = TypedDict(
    "ListMigrationTasksResultTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List["MigrationTaskSummaryTypeDef"],
    },
    total=False,
)

ListProgressUpdateStreamsResultTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List["ProgressUpdateStreamSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
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

ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
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
