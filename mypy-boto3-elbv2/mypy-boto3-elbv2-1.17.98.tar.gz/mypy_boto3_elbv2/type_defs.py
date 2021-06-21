"""
Type annotations for elbv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActionTypeEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
    "CreateListenerOutputTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "DescribeListenersOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "DescribeRulesOutputTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "ForwardActionConfigTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "LimitTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAddressTypeDef",
    "LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTypeDef",
    "MatcherTypeDef",
    "ModifyListenerOutputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyRuleOutputTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RuleConditionTypeDef",
    "RulePriorityPairTypeDef",
    "RuleTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "SetSubnetsOutputTypeDef",
    "SourceIpConditionConfigTypeDef",
    "SslPolicyTypeDef",
    "SubnetMappingTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TargetDescriptionTypeDef",
    "TargetGroupAttributeTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "TargetGroupTypeDef",
    "TargetHealthDescriptionTypeDef",
    "TargetHealthTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredActionTypeDef = TypedDict(
    "_RequiredActionTypeDef",
    {
        "Type": ActionTypeEnumType,
    },
)
_OptionalActionTypeDef = TypedDict(
    "_OptionalActionTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": "AuthenticateOidcActionConfigTypeDef",
        "AuthenticateCognitoConfig": "AuthenticateCognitoActionConfigTypeDef",
        "Order": int,
        "RedirectConfig": "RedirectActionConfigTypeDef",
        "FixedResponseConfig": "FixedResponseActionConfigTypeDef",
        "ForwardConfig": "ForwardActionConfigTypeDef",
    },
    total=False,
)


class ActionTypeDef(_RequiredActionTypeDef, _OptionalActionTypeDef):
    pass


AddListenerCertificatesOutputTypeDef = TypedDict(
    "AddListenerCertificatesOutputTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateCognitoActionConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
    },
)
_OptionalAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateCognitoActionConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": AuthenticateCognitoActionConditionalBehaviorEnumType,
    },
    total=False,
)


class AuthenticateCognitoActionConfigTypeDef(
    _RequiredAuthenticateCognitoActionConfigTypeDef, _OptionalAuthenticateCognitoActionConfigTypeDef
):
    pass


_RequiredAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateOidcActionConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateOidcActionConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": AuthenticateOidcActionConditionalBehaviorEnumType,
        "UseExistingClientSecret": bool,
    },
    total=False,
)


class AuthenticateOidcActionConfigTypeDef(
    _RequiredAuthenticateOidcActionConfigTypeDef, _OptionalAuthenticateOidcActionConfigTypeDef
):
    pass


AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "OutpostId": str,
        "LoadBalancerAddresses": List["LoadBalancerAddressTypeDef"],
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateArn": str,
        "IsDefault": bool,
    },
    total=False,
)

CipherTypeDef = TypedDict(
    "CipherTypeDef",
    {
        "Name": str,
        "Priority": int,
    },
    total=False,
)

CreateListenerOutputTypeDef = TypedDict(
    "CreateListenerOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoadBalancerOutputTypeDef = TypedDict(
    "CreateLoadBalancerOutputTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleOutputTypeDef = TypedDict(
    "CreateRuleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTargetGroupOutputTypeDef = TypedDict(
    "CreateTargetGroupOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
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

DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {
        "SslPolicies": List["SslPolicyTypeDef"],
        "NextMarker": str,
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

DescribeTargetGroupAttributesOutputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetHealthOutputTypeDef = TypedDict(
    "DescribeTargetHealthOutputTypeDef",
    {
        "TargetHealthDescriptions": List["TargetHealthDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFixedResponseActionConfigTypeDef = TypedDict(
    "_RequiredFixedResponseActionConfigTypeDef",
    {
        "StatusCode": str,
    },
)
_OptionalFixedResponseActionConfigTypeDef = TypedDict(
    "_OptionalFixedResponseActionConfigTypeDef",
    {
        "MessageBody": str,
        "ContentType": str,
    },
    total=False,
)


class FixedResponseActionConfigTypeDef(
    _RequiredFixedResponseActionConfigTypeDef, _OptionalFixedResponseActionConfigTypeDef
):
    pass


ForwardActionConfigTypeDef = TypedDict(
    "ForwardActionConfigTypeDef",
    {
        "TargetGroups": List["TargetGroupTupleTypeDef"],
        "TargetGroupStickinessConfig": "TargetGroupStickinessConfigTypeDef",
    },
    total=False,
)

HostHeaderConditionConfigTypeDef = TypedDict(
    "HostHeaderConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef",
    {
        "HttpHeaderName": str,
        "Values": List[str],
    },
    total=False,
)

HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef",
    {
        "Values": List[str],
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

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": ProtocolEnumType,
        "Certificates": List["CertificateTypeDef"],
        "SslPolicy": str,
        "DefaultActions": List["ActionTypeDef"],
        "AlpnPolicy": List[str],
    },
    total=False,
)

LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {
        "IpAddress": str,
        "AllocationId": str,
        "PrivateIPv4Address": str,
        "IPv6Address": str,
    },
    total=False,
)

LoadBalancerAttributeTypeDef = TypedDict(
    "LoadBalancerAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": LoadBalancerStateEnumType,
        "Reason": str,
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": LoadBalancerSchemeEnumType,
        "VpcId": str,
        "State": "LoadBalancerStateTypeDef",
        "Type": LoadBalancerTypeEnumType,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "SecurityGroups": List[str],
        "IpAddressType": IpAddressTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)

MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "HttpCode": str,
        "GrpcCode": str,
    },
    total=False,
)

ModifyListenerOutputTypeDef = TypedDict(
    "ModifyListenerOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyRuleOutputTypeDef = TypedDict(
    "ModifyRuleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupAttributesOutputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupOutputTypeDef = TypedDict(
    "ModifyTargetGroupOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
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

PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {
        "Values": List["QueryStringKeyValuePairTypeDef"],
    },
    total=False,
)

QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredRedirectActionConfigTypeDef = TypedDict(
    "_RequiredRedirectActionConfigTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
    },
)
_OptionalRedirectActionConfigTypeDef = TypedDict(
    "_OptionalRedirectActionConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
    },
    total=False,
)


class RedirectActionConfigTypeDef(
    _RequiredRedirectActionConfigTypeDef, _OptionalRedirectActionConfigTypeDef
):
    pass


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

RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": "HostHeaderConditionConfigTypeDef",
        "PathPatternConfig": "PathPatternConditionConfigTypeDef",
        "HttpHeaderConfig": "HttpHeaderConditionConfigTypeDef",
        "QueryStringConfig": "QueryStringConditionConfigTypeDef",
        "HttpRequestMethodConfig": "HttpRequestMethodConditionConfigTypeDef",
        "SourceIpConfig": "SourceIpConditionConfigTypeDef",
    },
    total=False,
)

RulePriorityPairTypeDef = TypedDict(
    "RulePriorityPairTypeDef",
    {
        "RuleArn": str,
        "Priority": int,
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List["RuleConditionTypeDef"],
        "Actions": List["ActionTypeDef"],
        "IsDefault": bool,
    },
    total=False,
)

SetIpAddressTypeOutputTypeDef = TypedDict(
    "SetIpAddressTypeOutputTypeDef",
    {
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetRulePrioritiesOutputTypeDef = TypedDict(
    "SetRulePrioritiesOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSubnetsOutputTypeDef = TypedDict(
    "SetSubnetsOutputTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List["CipherTypeDef"],
        "Name": str,
    },
    total=False,
)

SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": str,
        "AllocationId": str,
        "PrivateIPv4Address": str,
        "IPv6Address": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
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


_RequiredTargetDescriptionTypeDef = TypedDict(
    "_RequiredTargetDescriptionTypeDef",
    {
        "Id": str,
    },
)
_OptionalTargetDescriptionTypeDef = TypedDict(
    "_OptionalTargetDescriptionTypeDef",
    {
        "Port": int,
        "AvailabilityZone": str,
    },
    total=False,
)


class TargetDescriptionTypeDef(
    _RequiredTargetDescriptionTypeDef, _OptionalTargetDescriptionTypeDef
):
    pass


TargetGroupAttributeTypeDef = TypedDict(
    "TargetGroupAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef",
    {
        "Enabled": bool,
        "DurationSeconds": int,
    },
    total=False,
)

TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef",
    {
        "TargetGroupArn": str,
        "Weight": int,
    },
    total=False,
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": ProtocolEnumType,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": "MatcherTypeDef",
        "LoadBalancerArns": List[str],
        "TargetType": TargetTypeEnumType,
        "ProtocolVersion": str,
    },
    total=False,
)

TargetHealthDescriptionTypeDef = TypedDict(
    "TargetHealthDescriptionTypeDef",
    {
        "Target": "TargetDescriptionTypeDef",
        "HealthCheckPort": str,
        "TargetHealth": "TargetHealthTypeDef",
    },
    total=False,
)

TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": TargetHealthStateEnumType,
        "Reason": TargetHealthReasonEnumType,
        "Description": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
