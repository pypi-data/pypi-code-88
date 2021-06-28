"""
Type annotations for mgn service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mgn.type_defs import CPUTypeDef

    data: CPUTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ChangeServerLifeCycleStateSourceServerLifecycleStateType,
    DataReplicationErrorStringType,
    DataReplicationInitiationStepNameType,
    DataReplicationInitiationStepStatusType,
    DataReplicationStateType,
    FirstBootType,
    InitiatedByType,
    JobLogEventType,
    JobStatusType,
    JobTypeType,
    LaunchDispositionType,
    LaunchStatusType,
    LifeCycleStateType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
    TargetInstanceTypeRightSizingMethodType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CPUTypeDef",
    "ChangeServerLifeCycleStateRequestTypeDef",
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    "CreateReplicationConfigurationTemplateRequestTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteReplicationConfigurationTemplateRequestTypeDef",
    "DeleteSourceServerRequestTypeDef",
    "DescribeJobLogItemsRequestTypeDef",
    "DescribeJobLogItemsResponseResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsRequestTypeDef",
    "DescribeJobsResponseResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesRequestTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersRequestTypeDef",
    "DescribeSourceServersResponseResponseTypeDef",
    "DisconnectFromServiceRequestTypeDef",
    "DiskTypeDef",
    "FinalizeCutoverRequestTypeDef",
    "GetLaunchConfigurationRequestTypeDef",
    "GetReplicationConfigurationRequestTypeDef",
    "IdentificationHintsTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobTypeDef",
    "LaunchConfigurationResponseTypeDef",
    "LaunchedInstanceTypeDef",
    "LicensingTypeDef",
    "LifeCycleLastCutoverFinalizedTypeDef",
    "LifeCycleLastCutoverInitiatedTypeDef",
    "LifeCycleLastCutoverRevertedTypeDef",
    "LifeCycleLastCutoverTypeDef",
    "LifeCycleLastTestFinalizedTypeDef",
    "LifeCycleLastTestInitiatedTypeDef",
    "LifeCycleLastTestRevertedTypeDef",
    "LifeCycleLastTestTypeDef",
    "LifeCycleTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MarkAsArchivedRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingServerTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationResponseTypeDef",
    "ReplicationConfigurationTemplateResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDataReplicationRequestTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerResponseTypeDef",
    "StartCutoverRequestTypeDef",
    "StartCutoverResponseResponseTypeDef",
    "StartTestRequestTypeDef",
    "StartTestResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TerminateTargetInstancesRequestTypeDef",
    "TerminateTargetInstancesResponseResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLaunchConfigurationRequestTypeDef",
    "UpdateReplicationConfigurationRequestTypeDef",
    "UpdateReplicationConfigurationTemplateRequestTypeDef",
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "cores": int,
        "modelName": str,
    },
    total=False,
)

ChangeServerLifeCycleStateRequestTypeDef = TypedDict(
    "ChangeServerLifeCycleStateRequestTypeDef",
    {
        "lifeCycle": "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
        "sourceServerID": str,
    },
)

ChangeServerLifeCycleStateSourceServerLifecycleTypeDef = TypedDict(
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    {
        "state": ChangeServerLifeCycleStateSourceServerLifecycleStateType,
    },
)

_RequiredCreateReplicationConfigurationTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationConfigurationTemplateRequestTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
)
_OptionalCreateReplicationConfigurationTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationConfigurationTemplateRequestTypeDef",
    {
        "ebsEncryptionKeyArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateReplicationConfigurationTemplateRequestTypeDef(
    _RequiredCreateReplicationConfigurationTemplateRequestTypeDef,
    _OptionalCreateReplicationConfigurationTemplateRequestTypeDef,
):
    pass


DataReplicationErrorTypeDef = TypedDict(
    "DataReplicationErrorTypeDef",
    {
        "error": DataReplicationErrorStringType,
        "rawError": str,
    },
    total=False,
)

DataReplicationInfoReplicatedDiskTypeDef = TypedDict(
    "DataReplicationInfoReplicatedDiskTypeDef",
    {
        "backloggedStorageBytes": int,
        "deviceName": str,
        "replicatedStorageBytes": int,
        "rescannedStorageBytes": int,
        "totalStorageBytes": int,
    },
    total=False,
)

DataReplicationInfoTypeDef = TypedDict(
    "DataReplicationInfoTypeDef",
    {
        "dataReplicationError": "DataReplicationErrorTypeDef",
        "dataReplicationInitiation": "DataReplicationInitiationTypeDef",
        "dataReplicationState": DataReplicationStateType,
        "etaDateTime": str,
        "lagDuration": str,
        "replicatedDisks": List["DataReplicationInfoReplicatedDiskTypeDef"],
    },
    total=False,
)

DataReplicationInitiationStepTypeDef = TypedDict(
    "DataReplicationInitiationStepTypeDef",
    {
        "name": DataReplicationInitiationStepNameType,
        "status": DataReplicationInitiationStepStatusType,
    },
    total=False,
)

DataReplicationInitiationTypeDef = TypedDict(
    "DataReplicationInitiationTypeDef",
    {
        "nextAttemptDateTime": str,
        "startDateTime": str,
        "steps": List["DataReplicationInitiationStepTypeDef"],
    },
    total=False,
)

DeleteJobRequestTypeDef = TypedDict(
    "DeleteJobRequestTypeDef",
    {
        "jobID": str,
    },
)

DeleteReplicationConfigurationTemplateRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationTemplateRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)

DeleteSourceServerRequestTypeDef = TypedDict(
    "DeleteSourceServerRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

_RequiredDescribeJobLogItemsRequestTypeDef = TypedDict(
    "_RequiredDescribeJobLogItemsRequestTypeDef",
    {
        "jobID": str,
    },
)
_OptionalDescribeJobLogItemsRequestTypeDef = TypedDict(
    "_OptionalDescribeJobLogItemsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class DescribeJobLogItemsRequestTypeDef(
    _RequiredDescribeJobLogItemsRequestTypeDef, _OptionalDescribeJobLogItemsRequestTypeDef
):
    pass


DescribeJobLogItemsResponseResponseTypeDef = TypedDict(
    "DescribeJobLogItemsResponseResponseTypeDef",
    {
        "items": List["JobLogTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsRequestFiltersTypeDef = TypedDict(
    "DescribeJobsRequestFiltersTypeDef",
    {
        "fromDate": str,
        "jobIDs": List[str],
        "toDate": str,
    },
    total=False,
)

_RequiredDescribeJobsRequestTypeDef = TypedDict(
    "_RequiredDescribeJobsRequestTypeDef",
    {
        "filters": "DescribeJobsRequestFiltersTypeDef",
    },
)
_OptionalDescribeJobsRequestTypeDef = TypedDict(
    "_OptionalDescribeJobsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class DescribeJobsRequestTypeDef(
    _RequiredDescribeJobsRequestTypeDef, _OptionalDescribeJobsRequestTypeDef
):
    pass


DescribeJobsResponseResponseTypeDef = TypedDict(
    "DescribeJobsResponseResponseTypeDef",
    {
        "items": List["JobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeReplicationConfigurationTemplatesRequestTypeDef = TypedDict(
    "_RequiredDescribeReplicationConfigurationTemplatesRequestTypeDef",
    {
        "replicationConfigurationTemplateIDs": List[str],
    },
)
_OptionalDescribeReplicationConfigurationTemplatesRequestTypeDef = TypedDict(
    "_OptionalDescribeReplicationConfigurationTemplatesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class DescribeReplicationConfigurationTemplatesRequestTypeDef(
    _RequiredDescribeReplicationConfigurationTemplatesRequestTypeDef,
    _OptionalDescribeReplicationConfigurationTemplatesRequestTypeDef,
):
    pass


DescribeReplicationConfigurationTemplatesResponseResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationTemplatesResponseResponseTypeDef",
    {
        "items": List["ReplicationConfigurationTemplateResponseTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSourceServersRequestFiltersTypeDef = TypedDict(
    "DescribeSourceServersRequestFiltersTypeDef",
    {
        "isArchived": bool,
        "sourceServerIDs": List[str],
    },
    total=False,
)

_RequiredDescribeSourceServersRequestTypeDef = TypedDict(
    "_RequiredDescribeSourceServersRequestTypeDef",
    {
        "filters": "DescribeSourceServersRequestFiltersTypeDef",
    },
)
_OptionalDescribeSourceServersRequestTypeDef = TypedDict(
    "_OptionalDescribeSourceServersRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class DescribeSourceServersRequestTypeDef(
    _RequiredDescribeSourceServersRequestTypeDef, _OptionalDescribeSourceServersRequestTypeDef
):
    pass


DescribeSourceServersResponseResponseTypeDef = TypedDict(
    "DescribeSourceServersResponseResponseTypeDef",
    {
        "items": List["SourceServerResponseTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisconnectFromServiceRequestTypeDef = TypedDict(
    "DisconnectFromServiceRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "bytes": int,
        "deviceName": str,
    },
    total=False,
)

FinalizeCutoverRequestTypeDef = TypedDict(
    "FinalizeCutoverRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

GetLaunchConfigurationRequestTypeDef = TypedDict(
    "GetLaunchConfigurationRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

GetReplicationConfigurationRequestTypeDef = TypedDict(
    "GetReplicationConfigurationRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

IdentificationHintsTypeDef = TypedDict(
    "IdentificationHintsTypeDef",
    {
        "awsInstanceID": str,
        "fqdn": str,
        "hostname": str,
        "vmWareUuid": str,
    },
    total=False,
)

JobLogEventDataTypeDef = TypedDict(
    "JobLogEventDataTypeDef",
    {
        "conversionServerID": str,
        "rawError": str,
        "sourceServerID": str,
        "targetInstanceID": str,
    },
    total=False,
)

JobLogTypeDef = TypedDict(
    "JobLogTypeDef",
    {
        "event": JobLogEventType,
        "eventData": "JobLogEventDataTypeDef",
        "logDateTime": str,
    },
    total=False,
)

_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef",
    {
        "jobID": str,
    },
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "arn": str,
        "creationDateTime": str,
        "endDateTime": str,
        "initiatedBy": InitiatedByType,
        "participatingServers": List["ParticipatingServerTypeDef"],
        "status": JobStatusType,
        "tags": Dict[str, str],
        "type": JobTypeType,
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


LaunchConfigurationResponseTypeDef = TypedDict(
    "LaunchConfigurationResponseTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "name": str,
        "sourceServerID": str,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchedInstanceTypeDef = TypedDict(
    "LaunchedInstanceTypeDef",
    {
        "ec2InstanceID": str,
        "firstBoot": FirstBootType,
        "jobID": str,
    },
    total=False,
)

LicensingTypeDef = TypedDict(
    "LicensingTypeDef",
    {
        "osByol": bool,
    },
    total=False,
)

LifeCycleLastCutoverFinalizedTypeDef = TypedDict(
    "LifeCycleLastCutoverFinalizedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastCutoverInitiatedTypeDef = TypedDict(
    "LifeCycleLastCutoverInitiatedTypeDef",
    {
        "apiCallDateTime": str,
        "jobID": str,
    },
    total=False,
)

LifeCycleLastCutoverRevertedTypeDef = TypedDict(
    "LifeCycleLastCutoverRevertedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastCutoverTypeDef = TypedDict(
    "LifeCycleLastCutoverTypeDef",
    {
        "finalized": "LifeCycleLastCutoverFinalizedTypeDef",
        "initiated": "LifeCycleLastCutoverInitiatedTypeDef",
        "reverted": "LifeCycleLastCutoverRevertedTypeDef",
    },
    total=False,
)

LifeCycleLastTestFinalizedTypeDef = TypedDict(
    "LifeCycleLastTestFinalizedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastTestInitiatedTypeDef = TypedDict(
    "LifeCycleLastTestInitiatedTypeDef",
    {
        "apiCallDateTime": str,
        "jobID": str,
    },
    total=False,
)

LifeCycleLastTestRevertedTypeDef = TypedDict(
    "LifeCycleLastTestRevertedTypeDef",
    {
        "apiCallDateTime": str,
    },
    total=False,
)

LifeCycleLastTestTypeDef = TypedDict(
    "LifeCycleLastTestTypeDef",
    {
        "finalized": "LifeCycleLastTestFinalizedTypeDef",
        "initiated": "LifeCycleLastTestInitiatedTypeDef",
        "reverted": "LifeCycleLastTestRevertedTypeDef",
    },
    total=False,
)

LifeCycleTypeDef = TypedDict(
    "LifeCycleTypeDef",
    {
        "addedToServiceDateTime": str,
        "elapsedReplicationDuration": str,
        "firstByteDateTime": str,
        "lastCutover": "LifeCycleLastCutoverTypeDef",
        "lastSeenByServiceDateTime": str,
        "lastTest": "LifeCycleLastTestTypeDef",
        "state": LifeCycleStateType,
    },
    total=False,
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MarkAsArchivedRequestTypeDef = TypedDict(
    "MarkAsArchivedRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "ips": List[str],
        "isPrimary": bool,
        "macAddress": str,
    },
    total=False,
)

OSTypeDef = TypedDict(
    "OSTypeDef",
    {
        "fullString": str,
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

ParticipatingServerTypeDef = TypedDict(
    "ParticipatingServerTypeDef",
    {
        "launchStatus": LaunchStatusType,
        "sourceServerID": str,
    },
    total=False,
)

ReplicationConfigurationReplicatedDiskTypeDef = TypedDict(
    "ReplicationConfigurationReplicatedDiskTypeDef",
    {
        "deviceName": str,
        "iops": int,
        "isBootDisk": bool,
        "stagingDiskType": ReplicationConfigurationReplicatedDiskStagingDiskTypeType,
    },
    total=False,
)

ReplicationConfigurationResponseTypeDef = TypedDict(
    "ReplicationConfigurationResponseTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
        "replicatedDisks": List["ReplicationConfigurationReplicatedDiskTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "sourceServerID": str,
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationConfigurationTemplateResponseTypeDef = TypedDict(
    "ReplicationConfigurationTemplateResponseTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "replicationConfigurationTemplateID": str,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "tags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RetryDataReplicationRequestTypeDef = TypedDict(
    "RetryDataReplicationRequestTypeDef",
    {
        "sourceServerID": str,
    },
)

SourcePropertiesTypeDef = TypedDict(
    "SourcePropertiesTypeDef",
    {
        "cpus": List["CPUTypeDef"],
        "disks": List["DiskTypeDef"],
        "identificationHints": "IdentificationHintsTypeDef",
        "lastUpdatedDateTime": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "os": "OSTypeDef",
        "ramBytes": int,
        "recommendedInstanceType": str,
    },
    total=False,
)

SourceServerResponseTypeDef = TypedDict(
    "SourceServerResponseTypeDef",
    {
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "isArchived": bool,
        "launchedInstance": "LaunchedInstanceTypeDef",
        "lifeCycle": "LifeCycleTypeDef",
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartCutoverRequestTypeDef = TypedDict(
    "_RequiredStartCutoverRequestTypeDef",
    {
        "sourceServerIDs": List[str],
    },
)
_OptionalStartCutoverRequestTypeDef = TypedDict(
    "_OptionalStartCutoverRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class StartCutoverRequestTypeDef(
    _RequiredStartCutoverRequestTypeDef, _OptionalStartCutoverRequestTypeDef
):
    pass


StartCutoverResponseResponseTypeDef = TypedDict(
    "StartCutoverResponseResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTestRequestTypeDef = TypedDict(
    "_RequiredStartTestRequestTypeDef",
    {
        "sourceServerIDs": List[str],
    },
)
_OptionalStartTestRequestTypeDef = TypedDict(
    "_OptionalStartTestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class StartTestRequestTypeDef(_RequiredStartTestRequestTypeDef, _OptionalStartTestRequestTypeDef):
    pass


StartTestResponseResponseTypeDef = TypedDict(
    "StartTestResponseResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTerminateTargetInstancesRequestTypeDef = TypedDict(
    "_RequiredTerminateTargetInstancesRequestTypeDef",
    {
        "sourceServerIDs": List[str],
    },
)
_OptionalTerminateTargetInstancesRequestTypeDef = TypedDict(
    "_OptionalTerminateTargetInstancesRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class TerminateTargetInstancesRequestTypeDef(
    _RequiredTerminateTargetInstancesRequestTypeDef, _OptionalTerminateTargetInstancesRequestTypeDef
):
    pass


TerminateTargetInstancesResponseResponseTypeDef = TypedDict(
    "TerminateTargetInstancesResponseResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateLaunchConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchConfigurationRequestTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalUpdateLaunchConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchConfigurationRequestTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "launchDisposition": LaunchDispositionType,
        "licensing": "LicensingTypeDef",
        "name": str,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethodType,
    },
    total=False,
)


class UpdateLaunchConfigurationRequestTypeDef(
    _RequiredUpdateLaunchConfigurationRequestTypeDef,
    _OptionalUpdateLaunchConfigurationRequestTypeDef,
):
    pass


_RequiredUpdateReplicationConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationConfigurationRequestTypeDef",
    {
        "sourceServerID": str,
    },
)
_OptionalUpdateReplicationConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationConfigurationRequestTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "name": str,
        "replicatedDisks": List["ReplicationConfigurationReplicatedDiskTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)


class UpdateReplicationConfigurationRequestTypeDef(
    _RequiredUpdateReplicationConfigurationRequestTypeDef,
    _OptionalUpdateReplicationConfigurationRequestTypeDef,
):
    pass


_RequiredUpdateReplicationConfigurationTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationConfigurationTemplateRequestTypeDef",
    {
        "replicationConfigurationTemplateID": str,
    },
)
_OptionalUpdateReplicationConfigurationTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationConfigurationTemplateRequestTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRoutingType,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        "ebsEncryption": ReplicationConfigurationEbsEncryptionType,
        "ebsEncryptionKeyArn": str,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)


class UpdateReplicationConfigurationTemplateRequestTypeDef(
    _RequiredUpdateReplicationConfigurationTemplateRequestTypeDef,
    _OptionalUpdateReplicationConfigurationTemplateRequestTypeDef,
):
    pass
