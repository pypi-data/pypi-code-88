"""
Type annotations for dax service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dax.type_defs import ClusterTypeDef

    data: ClusterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ChangeTypeType,
    ClusterEndpointEncryptionTypeType,
    IsModifiableType,
    ParameterTypeType,
    SourceTypeType,
    SSEStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClusterTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseResponseTypeDef",
    "CreateParameterGroupRequestTypeDef",
    "CreateParameterGroupResponseResponseTypeDef",
    "CreateSubnetGroupRequestTypeDef",
    "CreateSubnetGroupResponseResponseTypeDef",
    "DecreaseReplicationFactorRequestTypeDef",
    "DecreaseReplicationFactorResponseResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseResponseTypeDef",
    "DeleteParameterGroupRequestTypeDef",
    "DeleteParameterGroupResponseResponseTypeDef",
    "DeleteSubnetGroupRequestTypeDef",
    "DeleteSubnetGroupResponseResponseTypeDef",
    "DescribeClustersRequestTypeDef",
    "DescribeClustersResponseResponseTypeDef",
    "DescribeDefaultParametersRequestTypeDef",
    "DescribeDefaultParametersResponseResponseTypeDef",
    "DescribeEventsRequestTypeDef",
    "DescribeEventsResponseResponseTypeDef",
    "DescribeParameterGroupsRequestTypeDef",
    "DescribeParameterGroupsResponseResponseTypeDef",
    "DescribeParametersRequestTypeDef",
    "DescribeParametersResponseResponseTypeDef",
    "DescribeSubnetGroupsRequestTypeDef",
    "DescribeSubnetGroupsResponseResponseTypeDef",
    "EndpointTypeDef",
    "EventTypeDef",
    "IncreaseReplicationFactorRequestTypeDef",
    "IncreaseReplicationFactorResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "NodeTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterGroupStatusTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "RebootNodeRequestTypeDef",
    "RebootNodeResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "SecurityGroupMembershipTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceRequestTypeDef",
    "TagResourceResponseResponseTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UntagResourceResponseResponseTypeDef",
    "UpdateClusterRequestTypeDef",
    "UpdateClusterResponseResponseTypeDef",
    "UpdateParameterGroupRequestTypeDef",
    "UpdateParameterGroupResponseResponseTypeDef",
    "UpdateSubnetGroupRequestTypeDef",
    "UpdateSubnetGroupResponseResponseTypeDef",
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterName": str,
        "Description": str,
        "ClusterArn": str,
        "TotalNodes": int,
        "ActiveNodes": int,
        "NodeType": str,
        "Status": str,
        "ClusterDiscoveryEndpoint": "EndpointTypeDef",
        "NodeIdsToRemove": List[str],
        "Nodes": List["NodeTypeDef"],
        "PreferredMaintenanceWindow": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "SubnetGroup": str,
        "SecurityGroups": List["SecurityGroupMembershipTypeDef"],
        "IamRoleArn": str,
        "ParameterGroup": "ParameterGroupStatusTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
        "ClusterEndpointEncryptionType": ClusterEndpointEncryptionTypeType,
    },
    total=False,
)

_RequiredCreateClusterRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestTypeDef",
    {
        "ClusterName": str,
        "NodeType": str,
        "ReplicationFactor": int,
        "IamRoleArn": str,
    },
)
_OptionalCreateClusterRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestTypeDef",
    {
        "Description": str,
        "AvailabilityZones": List[str],
        "SubnetGroupName": str,
        "SecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "ParameterGroupName": str,
        "Tags": List["TagTypeDef"],
        "SSESpecification": "SSESpecificationTypeDef",
        "ClusterEndpointEncryptionType": ClusterEndpointEncryptionTypeType,
    },
    total=False,
)


class CreateClusterRequestTypeDef(
    _RequiredCreateClusterRequestTypeDef, _OptionalCreateClusterRequestTypeDef
):
    pass


CreateClusterResponseResponseTypeDef = TypedDict(
    "CreateClusterResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateParameterGroupRequestTypeDef = TypedDict(
    "_RequiredCreateParameterGroupRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalCreateParameterGroupRequestTypeDef = TypedDict(
    "_OptionalCreateParameterGroupRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreateParameterGroupRequestTypeDef(
    _RequiredCreateParameterGroupRequestTypeDef, _OptionalCreateParameterGroupRequestTypeDef
):
    pass


CreateParameterGroupResponseResponseTypeDef = TypedDict(
    "CreateParameterGroupResponseResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubnetGroupRequestTypeDef = TypedDict(
    "_RequiredCreateSubnetGroupRequestTypeDef",
    {
        "SubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateSubnetGroupRequestTypeDef = TypedDict(
    "_OptionalCreateSubnetGroupRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreateSubnetGroupRequestTypeDef(
    _RequiredCreateSubnetGroupRequestTypeDef, _OptionalCreateSubnetGroupRequestTypeDef
):
    pass


CreateSubnetGroupResponseResponseTypeDef = TypedDict(
    "CreateSubnetGroupResponseResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDecreaseReplicationFactorRequestTypeDef = TypedDict(
    "_RequiredDecreaseReplicationFactorRequestTypeDef",
    {
        "ClusterName": str,
        "NewReplicationFactor": int,
    },
)
_OptionalDecreaseReplicationFactorRequestTypeDef = TypedDict(
    "_OptionalDecreaseReplicationFactorRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "NodeIdsToRemove": List[str],
    },
    total=False,
)


class DecreaseReplicationFactorRequestTypeDef(
    _RequiredDecreaseReplicationFactorRequestTypeDef,
    _OptionalDecreaseReplicationFactorRequestTypeDef,
):
    pass


DecreaseReplicationFactorResponseResponseTypeDef = TypedDict(
    "DecreaseReplicationFactorResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestTypeDef = TypedDict(
    "DeleteClusterRequestTypeDef",
    {
        "ClusterName": str,
    },
)

DeleteClusterResponseResponseTypeDef = TypedDict(
    "DeleteClusterResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteParameterGroupRequestTypeDef = TypedDict(
    "DeleteParameterGroupRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)

DeleteParameterGroupResponseResponseTypeDef = TypedDict(
    "DeleteParameterGroupResponseResponseTypeDef",
    {
        "DeletionMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSubnetGroupRequestTypeDef = TypedDict(
    "DeleteSubnetGroupRequestTypeDef",
    {
        "SubnetGroupName": str,
    },
)

DeleteSubnetGroupResponseResponseTypeDef = TypedDict(
    "DeleteSubnetGroupResponseResponseTypeDef",
    {
        "DeletionMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestTypeDef = TypedDict(
    "DescribeClustersRequestTypeDef",
    {
        "ClusterNames": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeClustersResponseResponseTypeDef = TypedDict(
    "DescribeClustersResponseResponseTypeDef",
    {
        "NextToken": str,
        "Clusters": List["ClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultParametersRequestTypeDef = TypedDict(
    "DescribeDefaultParametersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDefaultParametersResponseResponseTypeDef = TypedDict(
    "DescribeDefaultParametersResponseResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsRequestTypeDef = TypedDict(
    "DescribeEventsRequestTypeDef",
    {
        "SourceName": str,
        "SourceType": SourceTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeEventsResponseResponseTypeDef = TypedDict(
    "DescribeEventsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParameterGroupsRequestTypeDef = TypedDict(
    "DescribeParameterGroupsRequestTypeDef",
    {
        "ParameterGroupNames": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeParameterGroupsResponseResponseTypeDef = TypedDict(
    "DescribeParameterGroupsResponseResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List["ParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeParametersRequestTypeDef = TypedDict(
    "_RequiredDescribeParametersRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalDescribeParametersRequestTypeDef = TypedDict(
    "_OptionalDescribeParametersRequestTypeDef",
    {
        "Source": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeParametersRequestTypeDef(
    _RequiredDescribeParametersRequestTypeDef, _OptionalDescribeParametersRequestTypeDef
):
    pass


DescribeParametersResponseResponseTypeDef = TypedDict(
    "DescribeParametersResponseResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubnetGroupsRequestTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestTypeDef",
    {
        "SubnetGroupNames": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeSubnetGroupsResponseResponseTypeDef = TypedDict(
    "DescribeSubnetGroupsResponseResponseTypeDef",
    {
        "NextToken": str,
        "SubnetGroups": List["SubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "URL": str,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceName": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

_RequiredIncreaseReplicationFactorRequestTypeDef = TypedDict(
    "_RequiredIncreaseReplicationFactorRequestTypeDef",
    {
        "ClusterName": str,
        "NewReplicationFactor": int,
    },
)
_OptionalIncreaseReplicationFactorRequestTypeDef = TypedDict(
    "_OptionalIncreaseReplicationFactorRequestTypeDef",
    {
        "AvailabilityZones": List[str],
    },
    total=False,
)


class IncreaseReplicationFactorRequestTypeDef(
    _RequiredIncreaseReplicationFactorRequestTypeDef,
    _OptionalIncreaseReplicationFactorRequestTypeDef,
):
    pass


IncreaseReplicationFactorResponseResponseTypeDef = TypedDict(
    "IncreaseReplicationFactorResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestTypeDef",
    {
        "ResourceName": str,
    },
)
_OptionalListTagsRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsRequestTypeDef(_RequiredListTagsRequestTypeDef, _OptionalListTagsRequestTypeDef):
    pass


ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NodeId": str,
        "Endpoint": "EndpointTypeDef",
        "NodeCreateTime": datetime,
        "AvailabilityZone": str,
        "NodeStatus": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

NodeTypeSpecificValueTypeDef = TypedDict(
    "NodeTypeSpecificValueTypeDef",
    {
        "NodeType": str,
        "Value": str,
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicArn": str,
        "TopicStatus": str,
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

ParameterGroupStatusTypeDef = TypedDict(
    "ParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "NodeIdsToReboot": List[str],
    },
    total=False,
)

ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "Description": str,
    },
    total=False,
)

ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterType": ParameterTypeType,
        "ParameterValue": str,
        "NodeTypeSpecificValues": List["NodeTypeSpecificValueTypeDef"],
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": IsModifiableType,
        "ChangeType": ChangeTypeType,
    },
    total=False,
)

RebootNodeRequestTypeDef = TypedDict(
    "RebootNodeRequestTypeDef",
    {
        "ClusterName": str,
        "NodeId": str,
    },
)

RebootNodeResponseResponseTypeDef = TypedDict(
    "RebootNodeResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatusType,
    },
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
    },
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupIdentifier": str,
        "Status": str,
    },
    total=False,
)

SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {
        "SubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "Subnets": List["SubnetTypeDef"],
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

TagResourceResponseResponseTypeDef = TypedDict(
    "TagResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

UntagResourceResponseResponseTypeDef = TypedDict(
    "UntagResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestTypeDef",
    {
        "ClusterName": str,
    },
)
_OptionalUpdateClusterRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestTypeDef",
    {
        "Description": str,
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "NotificationTopicStatus": str,
        "ParameterGroupName": str,
        "SecurityGroupIds": List[str],
    },
    total=False,
)


class UpdateClusterRequestTypeDef(
    _RequiredUpdateClusterRequestTypeDef, _OptionalUpdateClusterRequestTypeDef
):
    pass


UpdateClusterResponseResponseTypeDef = TypedDict(
    "UpdateClusterResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateParameterGroupRequestTypeDef = TypedDict(
    "UpdateParameterGroupRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterNameValues": List["ParameterNameValueTypeDef"],
    },
)

UpdateParameterGroupResponseResponseTypeDef = TypedDict(
    "UpdateParameterGroupResponseResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubnetGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateSubnetGroupRequestTypeDef",
    {
        "SubnetGroupName": str,
    },
)
_OptionalUpdateSubnetGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateSubnetGroupRequestTypeDef",
    {
        "Description": str,
        "SubnetIds": List[str],
    },
    total=False,
)


class UpdateSubnetGroupRequestTypeDef(
    _RequiredUpdateSubnetGroupRequestTypeDef, _OptionalUpdateSubnetGroupRequestTypeDef
):
    pass


UpdateSubnetGroupResponseResponseTypeDef = TypedDict(
    "UpdateSubnetGroupResponseResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
