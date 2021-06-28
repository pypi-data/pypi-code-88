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
    "AddAvailabilityZonesInputTypeDef",
    "AddAvailabilityZonesOutputResponseTypeDef",
    "AddTagsInputTypeDef",
    "AdditionalAttributeTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "ApplySecurityGroupsToLoadBalancerInputTypeDef",
    "ApplySecurityGroupsToLoadBalancerOutputResponseTypeDef",
    "AttachLoadBalancerToSubnetsInputTypeDef",
    "AttachLoadBalancerToSubnetsOutputResponseTypeDef",
    "BackendServerDescriptionTypeDef",
    "ConfigureHealthCheckInputTypeDef",
    "ConfigureHealthCheckOutputResponseTypeDef",
    "ConnectionDrainingTypeDef",
    "ConnectionSettingsTypeDef",
    "CreateAccessPointInputTypeDef",
    "CreateAccessPointOutputResponseTypeDef",
    "CreateAppCookieStickinessPolicyInputTypeDef",
    "CreateLBCookieStickinessPolicyInputTypeDef",
    "CreateLoadBalancerListenerInputTypeDef",
    "CreateLoadBalancerPolicyInputTypeDef",
    "CrossZoneLoadBalancingTypeDef",
    "DeleteAccessPointInputTypeDef",
    "DeleteLoadBalancerListenerInputTypeDef",
    "DeleteLoadBalancerPolicyInputTypeDef",
    "DeregisterEndPointsInputTypeDef",
    "DeregisterEndPointsOutputResponseTypeDef",
    "DescribeAccessPointsInputTypeDef",
    "DescribeAccessPointsOutputResponseTypeDef",
    "DescribeAccountLimitsInputTypeDef",
    "DescribeAccountLimitsOutputResponseTypeDef",
    "DescribeEndPointStateInputTypeDef",
    "DescribeEndPointStateOutputResponseTypeDef",
    "DescribeLoadBalancerAttributesInputTypeDef",
    "DescribeLoadBalancerAttributesOutputResponseTypeDef",
    "DescribeLoadBalancerPoliciesInputTypeDef",
    "DescribeLoadBalancerPoliciesOutputResponseTypeDef",
    "DescribeLoadBalancerPolicyTypesInputTypeDef",
    "DescribeLoadBalancerPolicyTypesOutputResponseTypeDef",
    "DescribeTagsInputTypeDef",
    "DescribeTagsOutputResponseTypeDef",
    "DetachLoadBalancerFromSubnetsInputTypeDef",
    "DetachLoadBalancerFromSubnetsOutputResponseTypeDef",
    "HealthCheckTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "LimitTypeDef",
    "ListenerDescriptionTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAttributesTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "ModifyLoadBalancerAttributesInputTypeDef",
    "ModifyLoadBalancerAttributesOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeDef",
    "PolicyAttributeDescriptionTypeDef",
    "PolicyAttributeTypeDef",
    "PolicyAttributeTypeDescriptionTypeDef",
    "PolicyDescriptionTypeDef",
    "PolicyTypeDescriptionTypeDef",
    "RegisterEndPointsInputTypeDef",
    "RegisterEndPointsOutputResponseTypeDef",
    "RemoveAvailabilityZonesInputTypeDef",
    "RemoveAvailabilityZonesOutputResponseTypeDef",
    "RemoveTagsInputTypeDef",
    "ResponseMetadataTypeDef",
    "SetLoadBalancerListenerSSLCertificateInputTypeDef",
    "SetLoadBalancerPoliciesForBackendServerInputTypeDef",
    "SetLoadBalancerPoliciesOfListenerInputTypeDef",
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


AddAvailabilityZonesInputTypeDef = TypedDict(
    "AddAvailabilityZonesInputTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": List[str],
    },
)

AddAvailabilityZonesOutputResponseTypeDef = TypedDict(
    "AddAvailabilityZonesOutputResponseTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputTypeDef = TypedDict(
    "AddTagsInputTypeDef",
    {
        "LoadBalancerNames": List[str],
        "Tags": List["TagTypeDef"],
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

ApplySecurityGroupsToLoadBalancerInputTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerInputTypeDef",
    {
        "LoadBalancerName": str,
        "SecurityGroups": List[str],
    },
)

ApplySecurityGroupsToLoadBalancerOutputResponseTypeDef = TypedDict(
    "ApplySecurityGroupsToLoadBalancerOutputResponseTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerToSubnetsInputTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsInputTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": List[str],
    },
)

AttachLoadBalancerToSubnetsOutputResponseTypeDef = TypedDict(
    "AttachLoadBalancerToSubnetsOutputResponseTypeDef",
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

ConfigureHealthCheckInputTypeDef = TypedDict(
    "ConfigureHealthCheckInputTypeDef",
    {
        "LoadBalancerName": str,
        "HealthCheck": "HealthCheckTypeDef",
    },
)

ConfigureHealthCheckOutputResponseTypeDef = TypedDict(
    "ConfigureHealthCheckOutputResponseTypeDef",
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

_RequiredCreateAccessPointInputTypeDef = TypedDict(
    "_RequiredCreateAccessPointInputTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": List["ListenerTypeDef"],
    },
)
_OptionalCreateAccessPointInputTypeDef = TypedDict(
    "_OptionalCreateAccessPointInputTypeDef",
    {
        "AvailabilityZones": List[str],
        "Subnets": List[str],
        "SecurityGroups": List[str],
        "Scheme": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAccessPointInputTypeDef(
    _RequiredCreateAccessPointInputTypeDef, _OptionalCreateAccessPointInputTypeDef
):
    pass


CreateAccessPointOutputResponseTypeDef = TypedDict(
    "CreateAccessPointOutputResponseTypeDef",
    {
        "DNSName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppCookieStickinessPolicyInputTypeDef = TypedDict(
    "CreateAppCookieStickinessPolicyInputTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "CookieName": str,
    },
)

_RequiredCreateLBCookieStickinessPolicyInputTypeDef = TypedDict(
    "_RequiredCreateLBCookieStickinessPolicyInputTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
    },
)
_OptionalCreateLBCookieStickinessPolicyInputTypeDef = TypedDict(
    "_OptionalCreateLBCookieStickinessPolicyInputTypeDef",
    {
        "CookieExpirationPeriod": int,
    },
    total=False,
)


class CreateLBCookieStickinessPolicyInputTypeDef(
    _RequiredCreateLBCookieStickinessPolicyInputTypeDef,
    _OptionalCreateLBCookieStickinessPolicyInputTypeDef,
):
    pass


CreateLoadBalancerListenerInputTypeDef = TypedDict(
    "CreateLoadBalancerListenerInputTypeDef",
    {
        "LoadBalancerName": str,
        "Listeners": List["ListenerTypeDef"],
    },
)

_RequiredCreateLoadBalancerPolicyInputTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerPolicyInputTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
        "PolicyTypeName": str,
    },
)
_OptionalCreateLoadBalancerPolicyInputTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerPolicyInputTypeDef",
    {
        "PolicyAttributes": List["PolicyAttributeTypeDef"],
    },
    total=False,
)


class CreateLoadBalancerPolicyInputTypeDef(
    _RequiredCreateLoadBalancerPolicyInputTypeDef, _OptionalCreateLoadBalancerPolicyInputTypeDef
):
    pass


CrossZoneLoadBalancingTypeDef = TypedDict(
    "CrossZoneLoadBalancingTypeDef",
    {
        "Enabled": bool,
    },
)

DeleteAccessPointInputTypeDef = TypedDict(
    "DeleteAccessPointInputTypeDef",
    {
        "LoadBalancerName": str,
    },
)

DeleteLoadBalancerListenerInputTypeDef = TypedDict(
    "DeleteLoadBalancerListenerInputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPorts": List[int],
    },
)

DeleteLoadBalancerPolicyInputTypeDef = TypedDict(
    "DeleteLoadBalancerPolicyInputTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyName": str,
    },
)

DeregisterEndPointsInputTypeDef = TypedDict(
    "DeregisterEndPointsInputTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": List["InstanceTypeDef"],
    },
)

DeregisterEndPointsOutputResponseTypeDef = TypedDict(
    "DeregisterEndPointsOutputResponseTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccessPointsInputTypeDef = TypedDict(
    "DescribeAccessPointsInputTypeDef",
    {
        "LoadBalancerNames": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeAccessPointsOutputResponseTypeDef = TypedDict(
    "DescribeAccessPointsOutputResponseTypeDef",
    {
        "LoadBalancerDescriptions": List["LoadBalancerDescriptionTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountLimitsInputTypeDef = TypedDict(
    "DescribeAccountLimitsInputTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeAccountLimitsOutputResponseTypeDef = TypedDict(
    "DescribeAccountLimitsOutputResponseTypeDef",
    {
        "Limits": List["LimitTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEndPointStateInputTypeDef = TypedDict(
    "_RequiredDescribeEndPointStateInputTypeDef",
    {
        "LoadBalancerName": str,
    },
)
_OptionalDescribeEndPointStateInputTypeDef = TypedDict(
    "_OptionalDescribeEndPointStateInputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
    },
    total=False,
)


class DescribeEndPointStateInputTypeDef(
    _RequiredDescribeEndPointStateInputTypeDef, _OptionalDescribeEndPointStateInputTypeDef
):
    pass


DescribeEndPointStateOutputResponseTypeDef = TypedDict(
    "DescribeEndPointStateOutputResponseTypeDef",
    {
        "InstanceStates": List["InstanceStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesInputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputTypeDef",
    {
        "LoadBalancerName": str,
    },
)

DescribeLoadBalancerAttributesOutputResponseTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputResponseTypeDef",
    {
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPoliciesInputTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesInputTypeDef",
    {
        "LoadBalancerName": str,
        "PolicyNames": List[str],
    },
    total=False,
)

DescribeLoadBalancerPoliciesOutputResponseTypeDef = TypedDict(
    "DescribeLoadBalancerPoliciesOutputResponseTypeDef",
    {
        "PolicyDescriptions": List["PolicyDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerPolicyTypesInputTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesInputTypeDef",
    {
        "PolicyTypeNames": List[str],
    },
    total=False,
)

DescribeLoadBalancerPolicyTypesOutputResponseTypeDef = TypedDict(
    "DescribeLoadBalancerPolicyTypesOutputResponseTypeDef",
    {
        "PolicyTypeDescriptions": List["PolicyTypeDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputTypeDef = TypedDict(
    "DescribeTagsInputTypeDef",
    {
        "LoadBalancerNames": List[str],
    },
)

DescribeTagsOutputResponseTypeDef = TypedDict(
    "DescribeTagsOutputResponseTypeDef",
    {
        "TagDescriptions": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachLoadBalancerFromSubnetsInputTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsInputTypeDef",
    {
        "LoadBalancerName": str,
        "Subnets": List[str],
    },
)

DetachLoadBalancerFromSubnetsOutputResponseTypeDef = TypedDict(
    "DetachLoadBalancerFromSubnetsOutputResponseTypeDef",
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

ModifyLoadBalancerAttributesInputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerAttributes": "LoadBalancerAttributesTypeDef",
    },
)

ModifyLoadBalancerAttributesOutputResponseTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputResponseTypeDef",
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

RegisterEndPointsInputTypeDef = TypedDict(
    "RegisterEndPointsInputTypeDef",
    {
        "LoadBalancerName": str,
        "Instances": List["InstanceTypeDef"],
    },
)

RegisterEndPointsOutputResponseTypeDef = TypedDict(
    "RegisterEndPointsOutputResponseTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveAvailabilityZonesInputTypeDef = TypedDict(
    "RemoveAvailabilityZonesInputTypeDef",
    {
        "LoadBalancerName": str,
        "AvailabilityZones": List[str],
    },
)

RemoveAvailabilityZonesOutputResponseTypeDef = TypedDict(
    "RemoveAvailabilityZonesOutputResponseTypeDef",
    {
        "AvailabilityZones": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsInputTypeDef = TypedDict(
    "RemoveTagsInputTypeDef",
    {
        "LoadBalancerNames": List[str],
        "Tags": List["TagKeyOnlyTypeDef"],
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

SetLoadBalancerListenerSSLCertificateInputTypeDef = TypedDict(
    "SetLoadBalancerListenerSSLCertificateInputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "SSLCertificateId": str,
    },
)

SetLoadBalancerPoliciesForBackendServerInputTypeDef = TypedDict(
    "SetLoadBalancerPoliciesForBackendServerInputTypeDef",
    {
        "LoadBalancerName": str,
        "InstancePort": int,
        "PolicyNames": List[str],
    },
)

SetLoadBalancerPoliciesOfListenerInputTypeDef = TypedDict(
    "SetLoadBalancerPoliciesOfListenerInputTypeDef",
    {
        "LoadBalancerName": str,
        "LoadBalancerPort": int,
        "PolicyNames": List[str],
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
