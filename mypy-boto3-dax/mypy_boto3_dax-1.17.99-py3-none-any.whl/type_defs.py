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
from typing import List

from .literals import (
    ChangeTypeType,
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
    "CreateClusterResponseTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "DecreaseReplicationFactorResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeDefaultParametersResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "EndpointTypeDef",
    "EventTypeDef",
    "IncreaseReplicationFactorResponseTypeDef",
    "ListTagsResponseTypeDef",
    "NodeTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterGroupStatusTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "RebootNodeResponseTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "SecurityGroupMembershipTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
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
    },
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

CreateParameterGroupResponseTypeDef = TypedDict(
    "CreateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
    },
    total=False,
)

CreateSubnetGroupResponseTypeDef = TypedDict(
    "CreateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
    },
    total=False,
)

DecreaseReplicationFactorResponseTypeDef = TypedDict(
    "DecreaseReplicationFactorResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

DeleteParameterGroupResponseTypeDef = TypedDict(
    "DeleteParameterGroupResponseTypeDef",
    {
        "DeletionMessage": str,
    },
    total=False,
)

DeleteSubnetGroupResponseTypeDef = TypedDict(
    "DeleteSubnetGroupResponseTypeDef",
    {
        "DeletionMessage": str,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "NextToken": str,
        "Clusters": List["ClusterTypeDef"],
    },
    total=False,
)

DescribeDefaultParametersResponseTypeDef = TypedDict(
    "DescribeDefaultParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "NextToken": str,
        "Events": List["EventTypeDef"],
    },
    total=False,
)

DescribeParameterGroupsResponseTypeDef = TypedDict(
    "DescribeParameterGroupsResponseTypeDef",
    {
        "NextToken": str,
        "ParameterGroups": List["ParameterGroupTypeDef"],
    },
    total=False,
)

DescribeParametersResponseTypeDef = TypedDict(
    "DescribeParametersResponseTypeDef",
    {
        "NextToken": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

DescribeSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeSubnetGroupsResponseTypeDef",
    {
        "NextToken": str,
        "SubnetGroups": List["SubnetGroupTypeDef"],
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
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

IncreaseReplicationFactorResponseTypeDef = TypedDict(
    "IncreaseReplicationFactorResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
    },
    total=False,
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

RebootNodeResponseTypeDef = TypedDict(
    "RebootNodeResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
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

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

UpdateParameterGroupResponseTypeDef = TypedDict(
    "UpdateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": "ParameterGroupTypeDef",
    },
    total=False,
)

UpdateSubnetGroupResponseTypeDef = TypedDict(
    "UpdateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": "SubnetGroupTypeDef",
    },
    total=False,
)
