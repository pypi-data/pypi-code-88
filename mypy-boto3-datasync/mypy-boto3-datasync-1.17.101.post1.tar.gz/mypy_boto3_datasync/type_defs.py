"""
Type annotations for datasync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datasync.type_defs import AgentListEntryTypeDef

    data: AgentListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AgentStatusType,
    AtimeType,
    EndpointTypeType,
    GidType,
    LocationFilterNameType,
    LogLevelType,
    MtimeType,
    NfsVersionType,
    ObjectStorageServerProtocolType,
    OperatorType,
    OverwriteModeType,
    PhaseStatusType,
    PosixPermissionsType,
    PreserveDeletedFilesType,
    PreserveDevicesType,
    S3StorageClassType,
    SmbSecurityDescriptorCopyFlagsType,
    SmbVersionType,
    TaskExecutionStatusType,
    TaskFilterNameType,
    TaskQueueingType,
    TaskStatusType,
    TransferModeType,
    UidType,
    VerifyModeType,
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
    "AgentListEntryTypeDef",
    "CancelTaskExecutionRequestTypeDef",
    "CreateAgentRequestTypeDef",
    "CreateAgentResponseResponseTypeDef",
    "CreateLocationEfsRequestTypeDef",
    "CreateLocationEfsResponseResponseTypeDef",
    "CreateLocationFsxWindowsRequestTypeDef",
    "CreateLocationFsxWindowsResponseResponseTypeDef",
    "CreateLocationNfsRequestTypeDef",
    "CreateLocationNfsResponseResponseTypeDef",
    "CreateLocationObjectStorageRequestTypeDef",
    "CreateLocationObjectStorageResponseResponseTypeDef",
    "CreateLocationS3RequestTypeDef",
    "CreateLocationS3ResponseResponseTypeDef",
    "CreateLocationSmbRequestTypeDef",
    "CreateLocationSmbResponseResponseTypeDef",
    "CreateTaskRequestTypeDef",
    "CreateTaskResponseResponseTypeDef",
    "DeleteAgentRequestTypeDef",
    "DeleteLocationRequestTypeDef",
    "DeleteTaskRequestTypeDef",
    "DescribeAgentRequestTypeDef",
    "DescribeAgentResponseResponseTypeDef",
    "DescribeLocationEfsRequestTypeDef",
    "DescribeLocationEfsResponseResponseTypeDef",
    "DescribeLocationFsxWindowsRequestTypeDef",
    "DescribeLocationFsxWindowsResponseResponseTypeDef",
    "DescribeLocationNfsRequestTypeDef",
    "DescribeLocationNfsResponseResponseTypeDef",
    "DescribeLocationObjectStorageRequestTypeDef",
    "DescribeLocationObjectStorageResponseResponseTypeDef",
    "DescribeLocationS3RequestTypeDef",
    "DescribeLocationS3ResponseResponseTypeDef",
    "DescribeLocationSmbRequestTypeDef",
    "DescribeLocationSmbResponseResponseTypeDef",
    "DescribeTaskExecutionRequestTypeDef",
    "DescribeTaskExecutionResponseResponseTypeDef",
    "DescribeTaskRequestTypeDef",
    "DescribeTaskResponseResponseTypeDef",
    "Ec2ConfigTypeDef",
    "FilterRuleTypeDef",
    "ListAgentsRequestTypeDef",
    "ListAgentsResponseResponseTypeDef",
    "ListLocationsRequestTypeDef",
    "ListLocationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTaskExecutionsRequestTypeDef",
    "ListTaskExecutionsResponseResponseTypeDef",
    "ListTasksRequestTypeDef",
    "ListTasksResponseResponseTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "OptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateLinkConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "StartTaskExecutionRequestTypeDef",
    "StartTaskExecutionResponseResponseTypeDef",
    "TagListEntryTypeDef",
    "TagResourceRequestTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "TaskScheduleTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentRequestTypeDef",
    "UpdateLocationNfsRequestTypeDef",
    "UpdateLocationObjectStorageRequestTypeDef",
    "UpdateLocationSmbRequestTypeDef",
    "UpdateTaskExecutionRequestTypeDef",
    "UpdateTaskRequestTypeDef",
)

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
    },
    total=False,
)

CancelTaskExecutionRequestTypeDef = TypedDict(
    "CancelTaskExecutionRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

_RequiredCreateAgentRequestTypeDef = TypedDict(
    "_RequiredCreateAgentRequestTypeDef",
    {
        "ActivationKey": str,
    },
)
_OptionalCreateAgentRequestTypeDef = TypedDict(
    "_OptionalCreateAgentRequestTypeDef",
    {
        "AgentName": str,
        "Tags": List["TagListEntryTypeDef"],
        "VpcEndpointId": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)


class CreateAgentRequestTypeDef(
    _RequiredCreateAgentRequestTypeDef, _OptionalCreateAgentRequestTypeDef
):
    pass


CreateAgentResponseResponseTypeDef = TypedDict(
    "CreateAgentResponseResponseTypeDef",
    {
        "AgentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationEfsRequestTypeDef = TypedDict(
    "_RequiredCreateLocationEfsRequestTypeDef",
    {
        "EfsFilesystemArn": str,
        "Ec2Config": "Ec2ConfigTypeDef",
    },
)
_OptionalCreateLocationEfsRequestTypeDef = TypedDict(
    "_OptionalCreateLocationEfsRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)


class CreateLocationEfsRequestTypeDef(
    _RequiredCreateLocationEfsRequestTypeDef, _OptionalCreateLocationEfsRequestTypeDef
):
    pass


CreateLocationEfsResponseResponseTypeDef = TypedDict(
    "CreateLocationEfsResponseResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationFsxWindowsRequestTypeDef = TypedDict(
    "_RequiredCreateLocationFsxWindowsRequestTypeDef",
    {
        "FsxFilesystemArn": str,
        "SecurityGroupArns": List[str],
        "User": str,
        "Password": str,
    },
)
_OptionalCreateLocationFsxWindowsRequestTypeDef = TypedDict(
    "_OptionalCreateLocationFsxWindowsRequestTypeDef",
    {
        "Subdirectory": str,
        "Tags": List["TagListEntryTypeDef"],
        "Domain": str,
    },
    total=False,
)


class CreateLocationFsxWindowsRequestTypeDef(
    _RequiredCreateLocationFsxWindowsRequestTypeDef, _OptionalCreateLocationFsxWindowsRequestTypeDef
):
    pass


CreateLocationFsxWindowsResponseResponseTypeDef = TypedDict(
    "CreateLocationFsxWindowsResponseResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationNfsRequestTypeDef = TypedDict(
    "_RequiredCreateLocationNfsRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "OnPremConfig": "OnPremConfigTypeDef",
    },
)
_OptionalCreateLocationNfsRequestTypeDef = TypedDict(
    "_OptionalCreateLocationNfsRequestTypeDef",
    {
        "MountOptions": "NfsMountOptionsTypeDef",
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)


class CreateLocationNfsRequestTypeDef(
    _RequiredCreateLocationNfsRequestTypeDef, _OptionalCreateLocationNfsRequestTypeDef
):
    pass


CreateLocationNfsResponseResponseTypeDef = TypedDict(
    "CreateLocationNfsResponseResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationObjectStorageRequestTypeDef = TypedDict(
    "_RequiredCreateLocationObjectStorageRequestTypeDef",
    {
        "ServerHostname": str,
        "BucketName": str,
        "AgentArns": List[str],
    },
)
_OptionalCreateLocationObjectStorageRequestTypeDef = TypedDict(
    "_OptionalCreateLocationObjectStorageRequestTypeDef",
    {
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "Subdirectory": str,
        "AccessKey": str,
        "SecretKey": str,
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)


class CreateLocationObjectStorageRequestTypeDef(
    _RequiredCreateLocationObjectStorageRequestTypeDef,
    _OptionalCreateLocationObjectStorageRequestTypeDef,
):
    pass


CreateLocationObjectStorageResponseResponseTypeDef = TypedDict(
    "CreateLocationObjectStorageResponseResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationS3RequestTypeDef = TypedDict(
    "_RequiredCreateLocationS3RequestTypeDef",
    {
        "S3BucketArn": str,
        "S3Config": "S3ConfigTypeDef",
    },
)
_OptionalCreateLocationS3RequestTypeDef = TypedDict(
    "_OptionalCreateLocationS3RequestTypeDef",
    {
        "Subdirectory": str,
        "S3StorageClass": S3StorageClassType,
        "AgentArns": List[str],
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)


class CreateLocationS3RequestTypeDef(
    _RequiredCreateLocationS3RequestTypeDef, _OptionalCreateLocationS3RequestTypeDef
):
    pass


CreateLocationS3ResponseResponseTypeDef = TypedDict(
    "CreateLocationS3ResponseResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocationSmbRequestTypeDef = TypedDict(
    "_RequiredCreateLocationSmbRequestTypeDef",
    {
        "Subdirectory": str,
        "ServerHostname": str,
        "User": str,
        "Password": str,
        "AgentArns": List[str],
    },
)
_OptionalCreateLocationSmbRequestTypeDef = TypedDict(
    "_OptionalCreateLocationSmbRequestTypeDef",
    {
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)


class CreateLocationSmbRequestTypeDef(
    _RequiredCreateLocationSmbRequestTypeDef, _OptionalCreateLocationSmbRequestTypeDef
):
    pass


CreateLocationSmbResponseResponseTypeDef = TypedDict(
    "CreateLocationSmbResponseResponseTypeDef",
    {
        "LocationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTaskRequestTypeDef = TypedDict(
    "_RequiredCreateTaskRequestTypeDef",
    {
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
    },
)
_OptionalCreateTaskRequestTypeDef = TypedDict(
    "_OptionalCreateTaskRequestTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Name": str,
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "Tags": List["TagListEntryTypeDef"],
    },
    total=False,
)


class CreateTaskRequestTypeDef(
    _RequiredCreateTaskRequestTypeDef, _OptionalCreateTaskRequestTypeDef
):
    pass


CreateTaskResponseResponseTypeDef = TypedDict(
    "CreateTaskResponseResponseTypeDef",
    {
        "TaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAgentRequestTypeDef = TypedDict(
    "DeleteAgentRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DeleteLocationRequestTypeDef = TypedDict(
    "DeleteLocationRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DeleteTaskRequestTypeDef = TypedDict(
    "DeleteTaskRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeAgentRequestTypeDef = TypedDict(
    "DescribeAgentRequestTypeDef",
    {
        "AgentArn": str,
    },
)

DescribeAgentResponseResponseTypeDef = TypedDict(
    "DescribeAgentResponseResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatusType,
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": EndpointTypeType,
        "PrivateLinkConfig": "PrivateLinkConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationEfsRequestTypeDef = TypedDict(
    "DescribeLocationEfsRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationEfsResponseResponseTypeDef = TypedDict(
    "DescribeLocationEfsResponseResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": "Ec2ConfigTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationFsxWindowsRequestTypeDef = TypedDict(
    "DescribeLocationFsxWindowsRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationFsxWindowsResponseResponseTypeDef = TypedDict(
    "DescribeLocationFsxWindowsResponseResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "User": str,
        "Domain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationNfsRequestTypeDef = TypedDict(
    "DescribeLocationNfsRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationNfsResponseResponseTypeDef = TypedDict(
    "DescribeLocationNfsResponseResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": "NfsMountOptionsTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationObjectStorageRequestTypeDef = TypedDict(
    "DescribeLocationObjectStorageRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationObjectStorageResponseResponseTypeDef = TypedDict(
    "DescribeLocationObjectStorageResponseResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AccessKey": str,
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationS3RequestTypeDef = TypedDict(
    "DescribeLocationS3RequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationS3ResponseResponseTypeDef = TypedDict(
    "DescribeLocationS3ResponseResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": S3StorageClassType,
        "S3Config": "S3ConfigTypeDef",
        "AgentArns": List[str],
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocationSmbRequestTypeDef = TypedDict(
    "DescribeLocationSmbRequestTypeDef",
    {
        "LocationArn": str,
    },
)

DescribeLocationSmbResponseResponseTypeDef = TypedDict(
    "DescribeLocationSmbResponseResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskExecutionRequestTypeDef = TypedDict(
    "DescribeTaskExecutionRequestTypeDef",
    {
        "TaskExecutionArn": str,
    },
)

DescribeTaskExecutionResponseResponseTypeDef = TypedDict(
    "DescribeTaskExecutionResponseResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Includes": List["FilterRuleTypeDef"],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": "TaskExecutionResultDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTaskRequestTypeDef = TypedDict(
    "DescribeTaskRequestTypeDef",
    {
        "TaskArn": str,
    },
)

DescribeTaskResponseResponseTypeDef = TypedDict(
    "DescribeTaskResponseResponseTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Ec2ConfigTypeDef = TypedDict(
    "Ec2ConfigTypeDef",
    {
        "SubnetArn": str,
        "SecurityGroupArns": List[str],
    },
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "FilterType": Literal["SIMPLE_PATTERN"],
        "Value": str,
    },
    total=False,
)

ListAgentsRequestTypeDef = TypedDict(
    "ListAgentsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAgentsResponseResponseTypeDef = TypedDict(
    "ListAgentsResponseResponseTypeDef",
    {
        "Agents": List["AgentListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocationsRequestTypeDef = TypedDict(
    "ListLocationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["LocationFilterTypeDef"],
    },
    total=False,
)

ListLocationsResponseResponseTypeDef = TypedDict(
    "ListLocationsResponseResponseTypeDef",
    {
        "Locations": List["LocationListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskExecutionsRequestTypeDef = TypedDict(
    "ListTaskExecutionsRequestTypeDef",
    {
        "TaskArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTaskExecutionsResponseResponseTypeDef = TypedDict(
    "ListTaskExecutionsResponseResponseTypeDef",
    {
        "TaskExecutions": List["TaskExecutionListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestTypeDef = TypedDict(
    "ListTasksRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["TaskFilterTypeDef"],
    },
    total=False,
)

ListTasksResponseResponseTypeDef = TypedDict(
    "ListTasksResponseResponseTypeDef",
    {
        "Tasks": List["TaskListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationFilterTypeDef = TypedDict(
    "LocationFilterTypeDef",
    {
        "Name": LocationFilterNameType,
        "Values": List[str],
        "Operator": OperatorType,
    },
)

LocationListEntryTypeDef = TypedDict(
    "LocationListEntryTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
    },
    total=False,
)

NfsMountOptionsTypeDef = TypedDict(
    "NfsMountOptionsTypeDef",
    {
        "Version": NfsVersionType,
    },
    total=False,
)

OnPremConfigTypeDef = TypedDict(
    "OnPremConfigTypeDef",
    {
        "AgentArns": List[str],
    },
)

OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "VerifyMode": VerifyModeType,
        "OverwriteMode": OverwriteModeType,
        "Atime": AtimeType,
        "Mtime": MtimeType,
        "Uid": UidType,
        "Gid": GidType,
        "PreserveDeletedFiles": PreserveDeletedFilesType,
        "PreserveDevices": PreserveDevicesType,
        "PosixPermissions": PosixPermissionsType,
        "BytesPerSecond": int,
        "TaskQueueing": TaskQueueingType,
        "LogLevel": LogLevelType,
        "TransferMode": TransferModeType,
        "SecurityDescriptorCopyFlags": SmbSecurityDescriptorCopyFlagsType,
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

PrivateLinkConfigTypeDef = TypedDict(
    "PrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
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

S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketAccessRoleArn": str,
    },
)

SmbMountOptionsTypeDef = TypedDict(
    "SmbMountOptionsTypeDef",
    {
        "Version": SmbVersionType,
    },
    total=False,
)

_RequiredStartTaskExecutionRequestTypeDef = TypedDict(
    "_RequiredStartTaskExecutionRequestTypeDef",
    {
        "TaskArn": str,
    },
)
_OptionalStartTaskExecutionRequestTypeDef = TypedDict(
    "_OptionalStartTaskExecutionRequestTypeDef",
    {
        "OverrideOptions": "OptionsTypeDef",
        "Includes": List["FilterRuleTypeDef"],
    },
    total=False,
)


class StartTaskExecutionRequestTypeDef(
    _RequiredStartTaskExecutionRequestTypeDef, _OptionalStartTaskExecutionRequestTypeDef
):
    pass


StartTaskExecutionResponseResponseTypeDef = TypedDict(
    "StartTaskExecutionResponseResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagListEntryTypeDef = TypedDict(
    "_RequiredTagListEntryTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagListEntryTypeDef = TypedDict(
    "_OptionalTagListEntryTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagListEntryTypeDef(_RequiredTagListEntryTypeDef, _OptionalTagListEntryTypeDef):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagListEntryTypeDef"],
    },
)

TaskExecutionListEntryTypeDef = TypedDict(
    "TaskExecutionListEntryTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatusType,
    },
    total=False,
)

TaskExecutionResultDetailTypeDef = TypedDict(
    "TaskExecutionResultDetailTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": PhaseStatusType,
        "TotalDuration": int,
        "TransferDuration": int,
        "TransferStatus": PhaseStatusType,
        "VerifyDuration": int,
        "VerifyStatus": PhaseStatusType,
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)

TaskFilterTypeDef = TypedDict(
    "TaskFilterTypeDef",
    {
        "Name": TaskFilterNameType,
        "Values": List[str],
        "Operator": OperatorType,
    },
)

TaskListEntryTypeDef = TypedDict(
    "TaskListEntryTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatusType,
        "Name": str,
    },
    total=False,
)

TaskScheduleTypeDef = TypedDict(
    "TaskScheduleTypeDef",
    {
        "ScheduleExpression": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Keys": List[str],
    },
)

_RequiredUpdateAgentRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentRequestTypeDef",
    {
        "AgentArn": str,
    },
)
_OptionalUpdateAgentRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateAgentRequestTypeDef(
    _RequiredUpdateAgentRequestTypeDef, _OptionalUpdateAgentRequestTypeDef
):
    pass


_RequiredUpdateLocationNfsRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationNfsRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationNfsRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationNfsRequestTypeDef",
    {
        "Subdirectory": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": "NfsMountOptionsTypeDef",
    },
    total=False,
)


class UpdateLocationNfsRequestTypeDef(
    _RequiredUpdateLocationNfsRequestTypeDef, _OptionalUpdateLocationNfsRequestTypeDef
):
    pass


_RequiredUpdateLocationObjectStorageRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationObjectStorageRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationObjectStorageRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationObjectStorageRequestTypeDef",
    {
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocolType,
        "Subdirectory": str,
        "AccessKey": str,
        "SecretKey": str,
        "AgentArns": List[str],
    },
    total=False,
)


class UpdateLocationObjectStorageRequestTypeDef(
    _RequiredUpdateLocationObjectStorageRequestTypeDef,
    _OptionalUpdateLocationObjectStorageRequestTypeDef,
):
    pass


_RequiredUpdateLocationSmbRequestTypeDef = TypedDict(
    "_RequiredUpdateLocationSmbRequestTypeDef",
    {
        "LocationArn": str,
    },
)
_OptionalUpdateLocationSmbRequestTypeDef = TypedDict(
    "_OptionalUpdateLocationSmbRequestTypeDef",
    {
        "Subdirectory": str,
        "User": str,
        "Domain": str,
        "Password": str,
        "AgentArns": List[str],
        "MountOptions": "SmbMountOptionsTypeDef",
    },
    total=False,
)


class UpdateLocationSmbRequestTypeDef(
    _RequiredUpdateLocationSmbRequestTypeDef, _OptionalUpdateLocationSmbRequestTypeDef
):
    pass


UpdateTaskExecutionRequestTypeDef = TypedDict(
    "UpdateTaskExecutionRequestTypeDef",
    {
        "TaskExecutionArn": str,
        "Options": "OptionsTypeDef",
    },
)

_RequiredUpdateTaskRequestTypeDef = TypedDict(
    "_RequiredUpdateTaskRequestTypeDef",
    {
        "TaskArn": str,
    },
)
_OptionalUpdateTaskRequestTypeDef = TypedDict(
    "_OptionalUpdateTaskRequestTypeDef",
    {
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "Name": str,
        "CloudWatchLogGroupArn": str,
    },
    total=False,
)


class UpdateTaskRequestTypeDef(
    _RequiredUpdateTaskRequestTypeDef, _OptionalUpdateTaskRequestTypeDef
):
    pass
