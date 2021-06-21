"""
Type annotations for elb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elb.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessLogTypeDef",
    "AddAvailabilityZonesOutputTypeDef",
    "AdditionalAttributeTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    "BackendServerDescriptionTypeDef",
    "ConfigureHealthCheckOutputTypeDef",
    "ConnectionDrainingTypeDef",
    "ConnectionSettingsTypeDef",
    "CreateAccessPointOutputTypeDef",
    "CrossZoneLoadBalancingTypeDef",
    "DeregisterEndPointsOutputTypeDef",
    "DescribeAccessPointsOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeEndPointStateOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    "HealthCheckTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "LimitTypeDef",
    "ListenerDescriptionTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAttributesTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeDef",
    "PolicyAttributeDescriptionTypeDef",
    "PolicyAttributeTypeDef",
    "PolicyAttributeTypeDescriptionTypeDef",
    "PolicyDescriptionTypeDef",
    "PolicyTypeDescriptionTypeDef",
    "RegisterEndPointsOutputTypeDef",
    "RemoveAvailabilityZonesOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SourceSecurityGroupTypeDef",
    "TagDescriptionTypeDef",
    "TagKeyOnlyTypeDef",
    "TagTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessLogTypeDef = TypedDict(
    "_RequiredAccessLogTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalAccessLogTypeDef = TypedDict(
    "_OptionalAccessLogTypeDef",
    {
        "S3BucketName": str,
        "EmitInterval": int,
        "S3BucketPrefix": str,
    },
    total=False,
)


class AccessLogTypeDef(_RequiredAccessLogTypeDef, _OptionalAccessLogTypeDef):
    pass


AddAvailabilityZonesOutputTypeDef = TypedDict(
    "AddAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdditionalAttributeTypeDef = TypedDict(
    "AdditionalAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

AppCookieStickinessPolicyTypeDef = TypedDict(
    "AppCookieStickinessPolicyTypeDef",
    {
        "PolicyName": str,
        "CookieName": str,
    },
    total=False,
)

ApplySecurityGroupsToLoadBalancerOutputTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerToSubnetsOutputTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackendServerDescriptionTypeDef = TypedDict(
    "BackendServerDescriptionTypeDef",
    {
        "InstancePort": int,
        "PolicyNames": List[str],
    },
    total=False,
)

ConfigureHealthCheckOutputTypeDef = TypedDict(
    "ConfigureHealthCheckOutputTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConnectionDrainingTypeDef = TypedDict(
    "_RequiredConnectionDrainingTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalConnectionDrainingTypeDef = TypedDict(
    "_OptionalConnectionDrainingTypeDef",
    {
        "Timeout": int,
    },
    total=False,
)


class ConnectionDrainingTypeDef(
    _RequiredConnectionDrainingTypeDef, _OptionalConnectionDrainingTypeDef
):
    pass


ConnectionSettingsTypeDef = TypedDict(
    "ConnectionSettingsTypeDef",
    {
        "IdleTimeout": int,
    },
)

CreateAccessPointOutputTypeDef = TypedDict(
    "CreateAccessPointOutputTypeDef",
    {
        "DNSName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CrossZoneLoadBalancingTypeDef = TypedDict(
    "CrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
)

DeregisterEndPointsOutputTypeDef = TypedDict(
    "DeregisterEndPointsOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccessPointsOutputTypeDef = TypedDict(
    "DescribeAccessPointsOutputTypeDef",
    {
        "LoadBalancerDescriptions": List["LoadBalancerDescriptionTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "Limits": List["LimitTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndPointStateOutputTypeDef = TypedDict(
    "DescribeEndPointStateOutputTypeDef",
    {
        "InstanceStates": List["InstanceStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPoliciesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    {
        "PolicyDescriptions": List["PolicyDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPolicyTypesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    {
        "PolicyTypeDescriptions": List["PolicyTypeDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachLoadBalancerFromSubnetsOutputTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    {
        "Subnets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HealthCheckTypeDef = TypedDict(
    "HealthCheckTypeDef",
    {
        "Target": str,
        "Interval": int,
        "Timeout": int,
        "UnhealthyThreshold": int,
        "HealthyThreshold": int,
    },
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "InstanceId": str,
        "State": str,
        "ReasonCode": str,
        "Description": str,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

LBCookieStickinessPolicyTypeDef = TypedDict(
    "LBCookieStickinessPolicyTypeDef",
    {
        "PolicyName": str,
        "CookieExpirationPeriod": int,
    },
    total=False,
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Name": str,
        "Max": str,
    },
    total=False,
)

ListenerDescriptionTypeDef = TypedDict(
    "ListenerDescriptionTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "PolicyNames": List[str],
    },
    total=False,
)

_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef",
    {
        "Protocol": str,
        "LoadBalancerPort": int,
        "InstancePort": int,
    },
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef",
    {
        "InstanceProtocol": str,
        "SSLCertificateId": str,
    },
    total=False,
)


class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass


LoadBalancerAttributesTypeDef = TypedDict(
    "LoadBalancerAttributesTypeDef",
    {
        "CrossZoneLoadBalancing": "CrossZoneLoadBalancingTypeDef",
        "AccessLog": "AccessLogTypeDef",
        "ConnectionDraining": "ConnectionDrainingTypeDef",
        "ConnectionSettings": "ConnectionSettingsTypeDef",
        "AdditionalAttributes": List["AdditionalAttributeTypeDef"],
    },
    total=False,
)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "DNSName": str,
        "CanonicalHostedZoneName": str,
        "CanonicalHostedZoneNameID": str,
        "ListenerDescriptions": List["ListenerDescriptionTypeDef"],
        "Policies": "PoliciesTypeDef",
        "BackendServerDescriptions": List["BackendServerDescriptionTypeDef"],
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "VPCId": str,
        "Instances": List["InstanceTypeDef"],
        "HealthCheck": "HealthCheckTypeDef",
        "SourceSecurityGroup": "SourceSecurityGroupTypeDef",
        "SecurityGroups": List[str],
        "CreatedTime": datetime,
        "Scheme": str,
    },
    total=False,
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PoliciesTypeDef = TypedDict(
    "PoliciesTypeDef",
    {
        "AppCookieStickinessPolicies": List["AppCookieStickinessPolicyTypeDef"],
        "LBCookieStickinessPolicies": List["LBCookieStickinessPolicyTypeDef"],
        "OtherPolicies": List[str],
    },
    total=False,
)

PolicyAttributeDescriptionTypeDef = TypedDict(
    "PolicyAttributeDescriptionTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
    total=False,
)

PolicyAttributeTypeDef = TypedDict(
    "PolicyAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
    },
    total=False,
)

PolicyAttributeTypeDescriptionTypeDef = TypedDict(
    "PolicyAttributeTypeDescriptionTypeDef",
    {
        "AttributeName": str,
        "AttributeType": str,
        "Description": str,
        "DefaultValue": str,
        "Cardinality": str,
    },
    total=False,
)

PolicyDescriptionTypeDef = TypedDict(
    "PolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "PolicyTypeName": str,
        "PolicyAttributeDescriptions": List["PolicyAttributeDescriptionTypeDef"],
    },
    total=False,
)

PolicyTypeDescriptionTypeDef = TypedDict(
    "PolicyTypeDescriptionTypeDef",
    {
        "PolicyTypeName": str,
        "Description": str,
        "PolicyAttributeTypeDescriptions": List["PolicyAttributeTypeDescriptionTypeDef"],
    },
    total=False,
)

RegisterEndPointsOutputTypeDef = TypedDict(
    "RegisterEndPointsOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveAvailabilityZonesOutputTypeDef = TypedDict(
    "RemoveAvailabilityZonesOutputTypeDef",
    {
        "AvailabilityZones": List[str],
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

SourceSecurityGroupTypeDef = TypedDict(
    "SourceSecurityGroupTypeDef",
    {
        "OwnerAlias": str,
        "GroupName": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TagKeyOnlyTypeDef = TypedDict(
    "TagKeyOnlyTypeDef",
    {
        "Key": str,
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
