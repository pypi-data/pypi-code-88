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
    "AddListenerCertificatesInputTypeDef",
    "AddListenerCertificatesOutputResponseTypeDef",
    "AddTagsInputTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
    "CreateListenerInputTypeDef",
    "CreateListenerOutputResponseTypeDef",
    "CreateLoadBalancerInputTypeDef",
    "CreateLoadBalancerOutputResponseTypeDef",
    "CreateRuleInputTypeDef",
    "CreateRuleOutputResponseTypeDef",
    "CreateTargetGroupInputTypeDef",
    "CreateTargetGroupOutputResponseTypeDef",
    "DeleteListenerInputTypeDef",
    "DeleteLoadBalancerInputTypeDef",
    "DeleteRuleInputTypeDef",
    "DeleteTargetGroupInputTypeDef",
    "DeregisterTargetsInputTypeDef",
    "DescribeAccountLimitsInputTypeDef",
    "DescribeAccountLimitsOutputResponseTypeDef",
    "DescribeListenerCertificatesInputTypeDef",
    "DescribeListenerCertificatesOutputResponseTypeDef",
    "DescribeListenersInputTypeDef",
    "DescribeListenersOutputResponseTypeDef",
    "DescribeLoadBalancerAttributesInputTypeDef",
    "DescribeLoadBalancerAttributesOutputResponseTypeDef",
    "DescribeLoadBalancersInputTypeDef",
    "DescribeLoadBalancersOutputResponseTypeDef",
    "DescribeRulesInputTypeDef",
    "DescribeRulesOutputResponseTypeDef",
    "DescribeSSLPoliciesInputTypeDef",
    "DescribeSSLPoliciesOutputResponseTypeDef",
    "DescribeTagsInputTypeDef",
    "DescribeTagsOutputResponseTypeDef",
    "DescribeTargetGroupAttributesInputTypeDef",
    "DescribeTargetGroupAttributesOutputResponseTypeDef",
    "DescribeTargetGroupsInputTypeDef",
    "DescribeTargetGroupsOutputResponseTypeDef",
    "DescribeTargetHealthInputTypeDef",
    "DescribeTargetHealthOutputResponseTypeDef",
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
    "ModifyListenerInputTypeDef",
    "ModifyListenerOutputResponseTypeDef",
    "ModifyLoadBalancerAttributesInputTypeDef",
    "ModifyLoadBalancerAttributesOutputResponseTypeDef",
    "ModifyRuleInputTypeDef",
    "ModifyRuleOutputResponseTypeDef",
    "ModifyTargetGroupAttributesInputTypeDef",
    "ModifyTargetGroupAttributesOutputResponseTypeDef",
    "ModifyTargetGroupInputTypeDef",
    "ModifyTargetGroupOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "RegisterTargetsInputTypeDef",
    "RemoveListenerCertificatesInputTypeDef",
    "RemoveTagsInputTypeDef",
    "ResponseMetadataTypeDef",
    "RuleConditionTypeDef",
    "RulePriorityPairTypeDef",
    "RuleTypeDef",
    "SetIpAddressTypeInputTypeDef",
    "SetIpAddressTypeOutputResponseTypeDef",
    "SetRulePrioritiesInputTypeDef",
    "SetRulePrioritiesOutputResponseTypeDef",
    "SetSecurityGroupsInputTypeDef",
    "SetSecurityGroupsOutputResponseTypeDef",
    "SetSubnetsInputTypeDef",
    "SetSubnetsOutputResponseTypeDef",
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


AddListenerCertificatesInputTypeDef = TypedDict(
    "AddListenerCertificatesInputTypeDef",
    {
        "ListenerArn": str,
        "Certificates": List["CertificateTypeDef"],
    },
)

AddListenerCertificatesOutputResponseTypeDef = TypedDict(
    "AddListenerCertificatesOutputResponseTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputTypeDef = TypedDict(
    "AddTagsInputTypeDef",
    {
        "ResourceArns": List[str],
        "Tags": List["TagTypeDef"],
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

_RequiredCreateListenerInputTypeDef = TypedDict(
    "_RequiredCreateListenerInputTypeDef",
    {
        "LoadBalancerArn": str,
        "DefaultActions": List["ActionTypeDef"],
    },
)
_OptionalCreateListenerInputTypeDef = TypedDict(
    "_OptionalCreateListenerInputTypeDef",
    {
        "Protocol": ProtocolEnumType,
        "Port": int,
        "SslPolicy": str,
        "Certificates": List["CertificateTypeDef"],
        "AlpnPolicy": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateListenerInputTypeDef(
    _RequiredCreateListenerInputTypeDef, _OptionalCreateListenerInputTypeDef
):
    pass


CreateListenerOutputResponseTypeDef = TypedDict(
    "CreateListenerOutputResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoadBalancerInputTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateLoadBalancerInputTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerInputTypeDef",
    {
        "Subnets": List[str],
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "SecurityGroups": List[str],
        "Scheme": LoadBalancerSchemeEnumType,
        "Tags": List["TagTypeDef"],
        "Type": LoadBalancerTypeEnumType,
        "IpAddressType": IpAddressTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)


class CreateLoadBalancerInputTypeDef(
    _RequiredCreateLoadBalancerInputTypeDef, _OptionalCreateLoadBalancerInputTypeDef
):
    pass


CreateLoadBalancerOutputResponseTypeDef = TypedDict(
    "CreateLoadBalancerOutputResponseTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleInputTypeDef = TypedDict(
    "_RequiredCreateRuleInputTypeDef",
    {
        "ListenerArn": str,
        "Conditions": List["RuleConditionTypeDef"],
        "Priority": int,
        "Actions": List["ActionTypeDef"],
    },
)
_OptionalCreateRuleInputTypeDef = TypedDict(
    "_OptionalCreateRuleInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRuleInputTypeDef(_RequiredCreateRuleInputTypeDef, _OptionalCreateRuleInputTypeDef):
    pass


CreateRuleOutputResponseTypeDef = TypedDict(
    "CreateRuleOutputResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTargetGroupInputTypeDef = TypedDict(
    "_RequiredCreateTargetGroupInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTargetGroupInputTypeDef = TypedDict(
    "_OptionalCreateTargetGroupInputTypeDef",
    {
        "Protocol": ProtocolEnumType,
        "ProtocolVersion": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "Matcher": "MatcherTypeDef",
        "TargetType": TargetTypeEnumType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTargetGroupInputTypeDef(
    _RequiredCreateTargetGroupInputTypeDef, _OptionalCreateTargetGroupInputTypeDef
):
    pass


CreateTargetGroupOutputResponseTypeDef = TypedDict(
    "CreateTargetGroupOutputResponseTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteListenerInputTypeDef = TypedDict(
    "DeleteListenerInputTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteLoadBalancerInputTypeDef = TypedDict(
    "DeleteLoadBalancerInputTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DeleteRuleInputTypeDef = TypedDict(
    "DeleteRuleInputTypeDef",
    {
        "RuleArn": str,
    },
)

DeleteTargetGroupInputTypeDef = TypedDict(
    "DeleteTargetGroupInputTypeDef",
    {
        "TargetGroupArn": str,
    },
)

DeregisterTargetsInputTypeDef = TypedDict(
    "DeregisterTargetsInputTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": List["TargetDescriptionTypeDef"],
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

_RequiredDescribeListenerCertificatesInputTypeDef = TypedDict(
    "_RequiredDescribeListenerCertificatesInputTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalDescribeListenerCertificatesInputTypeDef = TypedDict(
    "_OptionalDescribeListenerCertificatesInputTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)


class DescribeListenerCertificatesInputTypeDef(
    _RequiredDescribeListenerCertificatesInputTypeDef,
    _OptionalDescribeListenerCertificatesInputTypeDef,
):
    pass


DescribeListenerCertificatesOutputResponseTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputResponseTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenersInputTypeDef = TypedDict(
    "DescribeListenersInputTypeDef",
    {
        "LoadBalancerArn": str,
        "ListenerArns": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeListenersOutputResponseTypeDef = TypedDict(
    "DescribeListenersOutputResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesInputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DescribeLoadBalancerAttributesOutputResponseTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputResponseTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersInputTypeDef = TypedDict(
    "DescribeLoadBalancersInputTypeDef",
    {
        "LoadBalancerArns": List[str],
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeLoadBalancersOutputResponseTypeDef = TypedDict(
    "DescribeLoadBalancersOutputResponseTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesInputTypeDef = TypedDict(
    "DescribeRulesInputTypeDef",
    {
        "ListenerArn": str,
        "RuleArns": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeRulesOutputResponseTypeDef = TypedDict(
    "DescribeRulesOutputResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSSLPoliciesInputTypeDef = TypedDict(
    "DescribeSSLPoliciesInputTypeDef",
    {
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeSSLPoliciesOutputResponseTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputResponseTypeDef",
    {
        "SslPolicies": List["SslPolicyTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputTypeDef = TypedDict(
    "DescribeTagsInputTypeDef",
    {
        "ResourceArns": List[str],
    },
)

DescribeTagsOutputResponseTypeDef = TypedDict(
    "DescribeTagsOutputResponseTypeDef",
    {
        "TagDescriptions": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupAttributesInputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesInputTypeDef",
    {
        "TargetGroupArn": str,
    },
)

DescribeTargetGroupAttributesOutputResponseTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputResponseTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupsInputTypeDef = TypedDict(
    "DescribeTargetGroupsInputTypeDef",
    {
        "LoadBalancerArn": str,
        "TargetGroupArns": List[str],
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeTargetGroupsOutputResponseTypeDef = TypedDict(
    "DescribeTargetGroupsOutputResponseTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTargetHealthInputTypeDef = TypedDict(
    "_RequiredDescribeTargetHealthInputTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalDescribeTargetHealthInputTypeDef = TypedDict(
    "_OptionalDescribeTargetHealthInputTypeDef",
    {
        "Targets": List["TargetDescriptionTypeDef"],
    },
    total=False,
)


class DescribeTargetHealthInputTypeDef(
    _RequiredDescribeTargetHealthInputTypeDef, _OptionalDescribeTargetHealthInputTypeDef
):
    pass


DescribeTargetHealthOutputResponseTypeDef = TypedDict(
    "DescribeTargetHealthOutputResponseTypeDef",
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

_RequiredModifyListenerInputTypeDef = TypedDict(
    "_RequiredModifyListenerInputTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalModifyListenerInputTypeDef = TypedDict(
    "_OptionalModifyListenerInputTypeDef",
    {
        "Port": int,
        "Protocol": ProtocolEnumType,
        "SslPolicy": str,
        "Certificates": List["CertificateTypeDef"],
        "DefaultActions": List["ActionTypeDef"],
        "AlpnPolicy": List[str],
    },
    total=False,
)


class ModifyListenerInputTypeDef(
    _RequiredModifyListenerInputTypeDef, _OptionalModifyListenerInputTypeDef
):
    pass


ModifyListenerOutputResponseTypeDef = TypedDict(
    "ModifyListenerOutputResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesInputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputTypeDef",
    {
        "LoadBalancerArn": str,
        "Attributes": List["LoadBalancerAttributeTypeDef"],
    },
)

ModifyLoadBalancerAttributesOutputResponseTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputResponseTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyRuleInputTypeDef = TypedDict(
    "_RequiredModifyRuleInputTypeDef",
    {
        "RuleArn": str,
    },
)
_OptionalModifyRuleInputTypeDef = TypedDict(
    "_OptionalModifyRuleInputTypeDef",
    {
        "Conditions": List["RuleConditionTypeDef"],
        "Actions": List["ActionTypeDef"],
    },
    total=False,
)


class ModifyRuleInputTypeDef(_RequiredModifyRuleInputTypeDef, _OptionalModifyRuleInputTypeDef):
    pass


ModifyRuleOutputResponseTypeDef = TypedDict(
    "ModifyRuleOutputResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupAttributesInputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesInputTypeDef",
    {
        "TargetGroupArn": str,
        "Attributes": List["TargetGroupAttributeTypeDef"],
    },
)

ModifyTargetGroupAttributesOutputResponseTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputResponseTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTargetGroupInputTypeDef = TypedDict(
    "_RequiredModifyTargetGroupInputTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalModifyTargetGroupInputTypeDef = TypedDict(
    "_OptionalModifyTargetGroupInputTypeDef",
    {
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckPath": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "Matcher": "MatcherTypeDef",
    },
    total=False,
)


class ModifyTargetGroupInputTypeDef(
    _RequiredModifyTargetGroupInputTypeDef, _OptionalModifyTargetGroupInputTypeDef
):
    pass


ModifyTargetGroupOutputResponseTypeDef = TypedDict(
    "ModifyTargetGroupOutputResponseTypeDef",
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


RegisterTargetsInputTypeDef = TypedDict(
    "RegisterTargetsInputTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": List["TargetDescriptionTypeDef"],
    },
)

RemoveListenerCertificatesInputTypeDef = TypedDict(
    "RemoveListenerCertificatesInputTypeDef",
    {
        "ListenerArn": str,
        "Certificates": List["CertificateTypeDef"],
    },
)

RemoveTagsInputTypeDef = TypedDict(
    "RemoveTagsInputTypeDef",
    {
        "ResourceArns": List[str],
        "TagKeys": List[str],
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

SetIpAddressTypeInputTypeDef = TypedDict(
    "SetIpAddressTypeInputTypeDef",
    {
        "LoadBalancerArn": str,
        "IpAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeOutputResponseTypeDef = TypedDict(
    "SetIpAddressTypeOutputResponseTypeDef",
    {
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetRulePrioritiesInputTypeDef = TypedDict(
    "SetRulePrioritiesInputTypeDef",
    {
        "RulePriorities": List["RulePriorityPairTypeDef"],
    },
)

SetRulePrioritiesOutputResponseTypeDef = TypedDict(
    "SetRulePrioritiesOutputResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSecurityGroupsInputTypeDef = TypedDict(
    "SetSecurityGroupsInputTypeDef",
    {
        "LoadBalancerArn": str,
        "SecurityGroups": List[str],
    },
)

SetSecurityGroupsOutputResponseTypeDef = TypedDict(
    "SetSecurityGroupsOutputResponseTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetSubnetsInputTypeDef = TypedDict(
    "_RequiredSetSubnetsInputTypeDef",
    {
        "LoadBalancerArn": str,
    },
)
_OptionalSetSubnetsInputTypeDef = TypedDict(
    "_OptionalSetSubnetsInputTypeDef",
    {
        "Subnets": List[str],
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "IpAddressType": IpAddressTypeType,
    },
    total=False,
)


class SetSubnetsInputTypeDef(_RequiredSetSubnetsInputTypeDef, _OptionalSetSubnetsInputTypeDef):
    pass


SetSubnetsOutputResponseTypeDef = TypedDict(
    "SetSubnetsOutputResponseTypeDef",
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
