"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import ActionConditionTypeDef

    data: ActionConditionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from .literals import (
    ActionValueType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    FallbackBehaviorType,
    FilterBehaviorType,
    FilterRequirementType,
    ForwardedIPPositionType,
    IPAddressVersionType,
    JsonMatchScopeType,
    LabelMatchScopeType,
    PositionalConstraintType,
    RateBasedStatementAggregateKeyTypeType,
    ResponseContentTypeType,
    TextTransformationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionConditionTypeDef",
    "AllowActionTypeDef",
    "AndStatementTypeDef",
    "BlockActionTypeDef",
    "ByteMatchStatementTypeDef",
    "CheckCapacityResponseTypeDef",
    "ConditionTypeDef",
    "CountActionTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "CustomHTTPHeaderTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomResponseBodyTypeDef",
    "CustomResponseTypeDef",
    "DefaultActionTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "FilterTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GeoMatchStatementTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "JsonBodyTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelNameConditionTypeDef",
    "LabelSummaryTypeDef",
    "LabelTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingFilterTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "NotStatementTypeDef",
    "OrStatementTypeDef",
    "OverrideActionTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "RuleActionTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "SampledHTTPRequestTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "SizeConstraintStatementTypeDef",
    "SqliMatchStatementTypeDef",
    "StatementTypeDef",
    "TagInfoForResourceTypeDef",
    "TagTypeDef",
    "TextTransformationTypeDef",
    "TimeWindowTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "VisibilityConfigTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "XssMatchStatementTypeDef",
)

ActionConditionTypeDef = TypedDict(
    "ActionConditionTypeDef",
    {
        "Action": ActionValueType,
    },
)

AllowActionTypeDef = TypedDict(
    "AllowActionTypeDef",
    {
        "CustomRequestHandling": "CustomRequestHandlingTypeDef",
    },
    total=False,
)

AndStatementTypeDef = TypedDict(
    "AndStatementTypeDef",
    {
        "Statements": List["StatementTypeDef"],
    },
)

BlockActionTypeDef = TypedDict(
    "BlockActionTypeDef",
    {
        "CustomResponse": "CustomResponseTypeDef",
    },
    total=False,
)

ByteMatchStatementTypeDef = TypedDict(
    "ByteMatchStatementTypeDef",
    {
        "SearchString": Union[bytes, IO[bytes]],
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
        "PositionalConstraint": PositionalConstraintType,
    },
)

CheckCapacityResponseTypeDef = TypedDict(
    "CheckCapacityResponseTypeDef",
    {
        "Capacity": int,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ActionCondition": "ActionConditionTypeDef",
        "LabelNameCondition": "LabelNameConditionTypeDef",
    },
    total=False,
)

CountActionTypeDef = TypedDict(
    "CountActionTypeDef",
    {
        "CustomRequestHandling": "CustomRequestHandlingTypeDef",
    },
    total=False,
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "Summary": "IPSetSummaryTypeDef",
    },
    total=False,
)

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "Summary": "RegexPatternSetSummaryTypeDef",
    },
    total=False,
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "Summary": "RuleGroupSummaryTypeDef",
    },
    total=False,
)

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "Summary": "WebACLSummaryTypeDef",
    },
    total=False,
)

CustomHTTPHeaderTypeDef = TypedDict(
    "CustomHTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

CustomRequestHandlingTypeDef = TypedDict(
    "CustomRequestHandlingTypeDef",
    {
        "InsertHeaders": List["CustomHTTPHeaderTypeDef"],
    },
)

CustomResponseBodyTypeDef = TypedDict(
    "CustomResponseBodyTypeDef",
    {
        "ContentType": ResponseContentTypeType,
        "Content": str,
    },
)

_RequiredCustomResponseTypeDef = TypedDict(
    "_RequiredCustomResponseTypeDef",
    {
        "ResponseCode": int,
    },
)
_OptionalCustomResponseTypeDef = TypedDict(
    "_OptionalCustomResponseTypeDef",
    {
        "CustomResponseBodyKey": str,
        "ResponseHeaders": List["CustomHTTPHeaderTypeDef"],
    },
    total=False,
)


class CustomResponseTypeDef(_RequiredCustomResponseTypeDef, _OptionalCustomResponseTypeDef):
    pass


DefaultActionTypeDef = TypedDict(
    "DefaultActionTypeDef",
    {
        "Block": "BlockActionTypeDef",
        "Allow": "AllowActionTypeDef",
    },
    total=False,
)

DeleteFirewallManagerRuleGroupsResponseTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    {
        "NextWebACLLockToken": str,
    },
    total=False,
)

DescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "DescribeManagedRuleGroupResponseTypeDef",
    {
        "Capacity": int,
        "Rules": List["RuleSummaryTypeDef"],
        "LabelNamespace": str,
        "AvailableLabels": List["LabelSummaryTypeDef"],
        "ConsumedLabels": List["LabelSummaryTypeDef"],
    },
    total=False,
)

ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "Name": str,
    },
)

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "SingleHeader": "SingleHeaderTypeDef",
        "SingleQueryArgument": "SingleQueryArgumentTypeDef",
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
        "JsonBody": "JsonBodyTypeDef",
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": List["ConditionTypeDef"],
    },
)

FirewallManagerRuleGroupTypeDef = TypedDict(
    "FirewallManagerRuleGroupTypeDef",
    {
        "Name": str,
        "Priority": int,
        "FirewallManagerStatement": "FirewallManagerStatementTypeDef",
        "OverrideAction": "OverrideActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)

FirewallManagerStatementTypeDef = TypedDict(
    "FirewallManagerStatementTypeDef",
    {
        "ManagedRuleGroupStatement": "ManagedRuleGroupStatementTypeDef",
        "RuleGroupReferenceStatement": "RuleGroupReferenceStatementTypeDef",
    },
    total=False,
)

ForwardedIPConfigTypeDef = TypedDict(
    "ForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
    },
)

GeoMatchStatementTypeDef = TypedDict(
    "GeoMatchStatementTypeDef",
    {
        "CountryCodes": List[CountryCodeType],
        "ForwardedIPConfig": "ForwardedIPConfigTypeDef",
    },
    total=False,
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "LockToken": str,
    },
    total=False,
)

GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
    total=False,
)

GetPermissionPolicyResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

GetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": "RateBasedStatementManagedKeysIPSetTypeDef",
        "ManagedKeysIPV6": "RateBasedStatementManagedKeysIPSetTypeDef",
    },
    total=False,
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "LockToken": str,
    },
    total=False,
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "LockToken": str,
    },
    total=False,
)

GetSampledRequestsResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List["SampledHTTPRequestTypeDef"],
        "PopulationSize": int,
        "TimeWindow": "TimeWindowTypeDef",
    },
    total=False,
)

GetWebACLForResourceResponseTypeDef = TypedDict(
    "GetWebACLForResourceResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
    },
    total=False,
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "LockToken": str,
    },
    total=False,
)

HTTPHeaderTypeDef = TypedDict(
    "HTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

HTTPRequestTypeDef = TypedDict(
    "HTTPRequestTypeDef",
    {
        "ClientIP": str,
        "Country": str,
        "URI": str,
        "Method": str,
        "HTTPVersion": str,
        "Headers": List["HTTPHeaderTypeDef"],
    },
    total=False,
)

IPSetForwardedIPConfigTypeDef = TypedDict(
    "IPSetForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
        "Position": ForwardedIPPositionType,
    },
)

_RequiredIPSetReferenceStatementTypeDef = TypedDict(
    "_RequiredIPSetReferenceStatementTypeDef",
    {
        "ARN": str,
    },
)
_OptionalIPSetReferenceStatementTypeDef = TypedDict(
    "_OptionalIPSetReferenceStatementTypeDef",
    {
        "IPSetForwardedIPConfig": "IPSetForwardedIPConfigTypeDef",
    },
    total=False,
)


class IPSetReferenceStatementTypeDef(
    _RequiredIPSetReferenceStatementTypeDef, _OptionalIPSetReferenceStatementTypeDef
):
    pass


IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

_RequiredIPSetTypeDef = TypedDict(
    "_RequiredIPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
)
_OptionalIPSetTypeDef = TypedDict(
    "_OptionalIPSetTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class IPSetTypeDef(_RequiredIPSetTypeDef, _OptionalIPSetTypeDef):
    pass


_RequiredJsonBodyTypeDef = TypedDict(
    "_RequiredJsonBodyTypeDef",
    {
        "MatchPattern": "JsonMatchPatternTypeDef",
        "MatchScope": JsonMatchScopeType,
    },
)
_OptionalJsonBodyTypeDef = TypedDict(
    "_OptionalJsonBodyTypeDef",
    {
        "InvalidFallbackBehavior": BodyParsingFallbackBehaviorType,
    },
    total=False,
)


class JsonBodyTypeDef(_RequiredJsonBodyTypeDef, _OptionalJsonBodyTypeDef):
    pass


JsonMatchPatternTypeDef = TypedDict(
    "JsonMatchPatternTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedPaths": List[str],
    },
    total=False,
)

LabelMatchStatementTypeDef = TypedDict(
    "LabelMatchStatementTypeDef",
    {
        "Scope": LabelMatchScopeType,
        "Key": str,
    },
)

LabelNameConditionTypeDef = TypedDict(
    "LabelNameConditionTypeDef",
    {
        "LabelName": str,
    },
)

LabelSummaryTypeDef = TypedDict(
    "LabelSummaryTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
    },
)

ListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleGroups": List["ManagedRuleGroupSummaryTypeDef"],
    },
    total=False,
)

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List["IPSetSummaryTypeDef"],
    },
    total=False,
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List["LoggingConfigurationTypeDef"],
        "NextMarker": str,
    },
    total=False,
)

ListRegexPatternSetsResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List["RegexPatternSetSummaryTypeDef"],
    },
    total=False,
)

ListResourcesForWebACLResponseTypeDef = TypedDict(
    "ListResourcesForWebACLResponseTypeDef",
    {
        "ResourceArns": List[str],
    },
    total=False,
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["RuleGroupSummaryTypeDef"],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": "TagInfoForResourceTypeDef",
    },
    total=False,
)

ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List["WebACLSummaryTypeDef"],
    },
    total=False,
)

_RequiredLoggingConfigurationTypeDef = TypedDict(
    "_RequiredLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
    },
)
_OptionalLoggingConfigurationTypeDef = TypedDict(
    "_OptionalLoggingConfigurationTypeDef",
    {
        "RedactedFields": List["FieldToMatchTypeDef"],
        "ManagedByFirewallManager": bool,
        "LoggingFilter": "LoggingFilterTypeDef",
    },
    total=False,
)


class LoggingConfigurationTypeDef(
    _RequiredLoggingConfigurationTypeDef, _OptionalLoggingConfigurationTypeDef
):
    pass


LoggingFilterTypeDef = TypedDict(
    "LoggingFilterTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DefaultBehavior": FilterBehaviorType,
    },
)

_RequiredManagedRuleGroupStatementTypeDef = TypedDict(
    "_RequiredManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
    },
)
_OptionalManagedRuleGroupStatementTypeDef = TypedDict(
    "_OptionalManagedRuleGroupStatementTypeDef",
    {
        "ExcludedRules": List["ExcludedRuleTypeDef"],
        "ScopeDownStatement": "StatementTypeDef",
    },
    total=False,
)


class ManagedRuleGroupStatementTypeDef(
    _RequiredManagedRuleGroupStatementTypeDef, _OptionalManagedRuleGroupStatementTypeDef
):
    pass


ManagedRuleGroupSummaryTypeDef = TypedDict(
    "ManagedRuleGroupSummaryTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

NotStatementTypeDef = TypedDict(
    "NotStatementTypeDef",
    {
        "Statement": "StatementTypeDef",
    },
)

OrStatementTypeDef = TypedDict(
    "OrStatementTypeDef",
    {
        "Statements": List["StatementTypeDef"],
    },
)

OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef",
    {
        "Count": "CountActionTypeDef",
        "None": Dict[str, Any],
    },
    total=False,
)

PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
    total=False,
)

RateBasedStatementManagedKeysIPSetTypeDef = TypedDict(
    "RateBasedStatementManagedKeysIPSetTypeDef",
    {
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
    total=False,
)

_RequiredRateBasedStatementTypeDef = TypedDict(
    "_RequiredRateBasedStatementTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
    },
)
_OptionalRateBasedStatementTypeDef = TypedDict(
    "_OptionalRateBasedStatementTypeDef",
    {
        "ScopeDownStatement": Dict[str, Any],
        "ForwardedIPConfig": "ForwardedIPConfigTypeDef",
    },
    total=False,
)


class RateBasedStatementTypeDef(
    _RequiredRateBasedStatementTypeDef, _OptionalRateBasedStatementTypeDef
):
    pass


RegexPatternSetReferenceStatementTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": str,
        "RegularExpressionList": List["RegexTypeDef"],
    },
    total=False,
)

RegexTypeDef = TypedDict(
    "RegexTypeDef",
    {
        "RegexString": str,
    },
    total=False,
)

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "Block": "BlockActionTypeDef",
        "Allow": "AllowActionTypeDef",
        "Count": "CountActionTypeDef",
    },
    total=False,
)

_RequiredRuleGroupReferenceStatementTypeDef = TypedDict(
    "_RequiredRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
    },
)
_OptionalRuleGroupReferenceStatementTypeDef = TypedDict(
    "_OptionalRuleGroupReferenceStatementTypeDef",
    {
        "ExcludedRules": List["ExcludedRuleTypeDef"],
    },
    total=False,
)


class RuleGroupReferenceStatementTypeDef(
    _RequiredRuleGroupReferenceStatementTypeDef, _OptionalRuleGroupReferenceStatementTypeDef
):
    pass


RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "Name": str,
        "Id": str,
        "Capacity": int,
        "ARN": str,
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "LabelNamespace": str,
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
        "AvailableLabels": List["LabelSummaryTypeDef"],
        "ConsumedLabels": List["LabelSummaryTypeDef"],
    },
    total=False,
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Name": str,
        "Action": "RuleActionTypeDef",
    },
    total=False,
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": "StatementTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Action": "RuleActionTypeDef",
        "OverrideAction": "OverrideActionTypeDef",
        "RuleLabels": List["LabelTypeDef"],
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


_RequiredSampledHTTPRequestTypeDef = TypedDict(
    "_RequiredSampledHTTPRequestTypeDef",
    {
        "Request": "HTTPRequestTypeDef",
        "Weight": int,
    },
)
_OptionalSampledHTTPRequestTypeDef = TypedDict(
    "_OptionalSampledHTTPRequestTypeDef",
    {
        "Timestamp": datetime,
        "Action": str,
        "RuleNameWithinRuleGroup": str,
        "RequestHeadersInserted": List["HTTPHeaderTypeDef"],
        "ResponseCodeSent": int,
        "Labels": List["LabelTypeDef"],
    },
    total=False,
)


class SampledHTTPRequestTypeDef(
    _RequiredSampledHTTPRequestTypeDef, _OptionalSampledHTTPRequestTypeDef
):
    pass


SingleHeaderTypeDef = TypedDict(
    "SingleHeaderTypeDef",
    {
        "Name": str,
    },
)

SingleQueryArgumentTypeDef = TypedDict(
    "SingleQueryArgumentTypeDef",
    {
        "Name": str,
    },
)

SizeConstraintStatementTypeDef = TypedDict(
    "SizeConstraintStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

SqliMatchStatementTypeDef = TypedDict(
    "SqliMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "ByteMatchStatement": "ByteMatchStatementTypeDef",
        "SqliMatchStatement": "SqliMatchStatementTypeDef",
        "XssMatchStatement": "XssMatchStatementTypeDef",
        "SizeConstraintStatement": "SizeConstraintStatementTypeDef",
        "GeoMatchStatement": "GeoMatchStatementTypeDef",
        "RuleGroupReferenceStatement": "RuleGroupReferenceStatementTypeDef",
        "IPSetReferenceStatement": "IPSetReferenceStatementTypeDef",
        "RegexPatternSetReferenceStatement": "RegexPatternSetReferenceStatementTypeDef",
        "RateBasedStatement": Dict[str, Any],
        "AndStatement": Dict[str, Any],
        "OrStatement": Dict[str, Any],
        "NotStatement": Dict[str, Any],
        "ManagedRuleGroupStatement": Dict[str, Any],
        "LabelMatchStatement": "LabelMatchStatementTypeDef",
    },
    total=False,
)

TagInfoForResourceTypeDef = TypedDict(
    "TagInfoForResourceTypeDef",
    {
        "ResourceARN": str,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)

TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "NextLockToken": str,
    },
    total=False,
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "NextLockToken": str,
    },
    total=False,
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "NextLockToken": str,
    },
    total=False,
)

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "NextLockToken": str,
    },
    total=False,
)

VisibilityConfigTypeDef = TypedDict(
    "VisibilityConfigTypeDef",
    {
        "SampledRequestsEnabled": bool,
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
    },
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

_RequiredWebACLTypeDef = TypedDict(
    "_RequiredWebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalWebACLTypeDef = TypedDict(
    "_OptionalWebACLTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "Capacity": int,
        "PreProcessFirewallManagerRuleGroups": List["FirewallManagerRuleGroupTypeDef"],
        "PostProcessFirewallManagerRuleGroups": List["FirewallManagerRuleGroupTypeDef"],
        "ManagedByFirewallManager": bool,
        "LabelNamespace": str,
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
    },
    total=False,
)


class WebACLTypeDef(_RequiredWebACLTypeDef, _OptionalWebACLTypeDef):
    pass


XssMatchStatementTypeDef = TypedDict(
    "XssMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)
