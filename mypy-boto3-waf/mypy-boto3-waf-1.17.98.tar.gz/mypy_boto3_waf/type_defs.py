"""
Type annotations for waf service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/type_defs.html)

Usage::

    ```python
    from mypy_boto3_waf.type_defs import ActivatedRuleTypeDef

    data: ActivatedRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from .literals import (
    ChangeActionType,
    ChangeTokenStatusType,
    ComparisonOperatorType,
    GeoMatchConstraintValueType,
    IPSetDescriptorTypeType,
    MatchFieldTypeType,
    PositionalConstraintType,
    PredicateTypeType,
    TextTransformationType,
    WafActionTypeType,
    WafOverrideActionTypeType,
    WafRuleTypeType,
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
    "ActivatedRuleTypeDef",
    "ByteMatchSetSummaryTypeDef",
    "ByteMatchSetTypeDef",
    "ByteMatchSetUpdateTypeDef",
    "ByteMatchTupleTypeDef",
    "CreateByteMatchSetResponseTypeDef",
    "CreateGeoMatchSetResponseTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRateBasedRuleResponseTypeDef",
    "CreateRegexMatchSetResponseTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSizeConstraintSetResponseTypeDef",
    "CreateSqlInjectionMatchSetResponseTypeDef",
    "CreateWebACLMigrationStackResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "CreateXssMatchSetResponseTypeDef",
    "DeleteByteMatchSetResponseTypeDef",
    "DeleteGeoMatchSetResponseTypeDef",
    "DeleteIPSetResponseTypeDef",
    "DeleteRateBasedRuleResponseTypeDef",
    "DeleteRegexMatchSetResponseTypeDef",
    "DeleteRegexPatternSetResponseTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteRuleResponseTypeDef",
    "DeleteSizeConstraintSetResponseTypeDef",
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    "DeleteWebACLResponseTypeDef",
    "DeleteXssMatchSetResponseTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "GetByteMatchSetResponseTypeDef",
    "GetChangeTokenResponseTypeDef",
    "GetChangeTokenStatusResponseTypeDef",
    "GetGeoMatchSetResponseTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    "GetRateBasedRuleResponseTypeDef",
    "GetRegexMatchSetResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetRuleResponseTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetSizeConstraintSetResponseTypeDef",
    "GetSqlInjectionMatchSetResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "GetXssMatchSetResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    "ListByteMatchSetsResponseTypeDef",
    "ListGeoMatchSetsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRateBasedRulesResponseTypeDef",
    "ListRegexMatchSetsResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListRulesResponseTypeDef",
    "ListSizeConstraintSetsResponseTypeDef",
    "ListSqlInjectionMatchSetsResponseTypeDef",
    "ListSubscribedRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "ListXssMatchSetsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "RateBasedRuleTypeDef",
    "RegexMatchSetSummaryTypeDef",
    "RegexMatchSetTypeDef",
    "RegexMatchSetUpdateTypeDef",
    "RegexMatchTupleTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexPatternSetUpdateTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleGroupUpdateTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "RuleUpdateTypeDef",
    "SampledHTTPRequestTypeDef",
    "SizeConstraintSetSummaryTypeDef",
    "SizeConstraintSetTypeDef",
    "SizeConstraintSetUpdateTypeDef",
    "SizeConstraintTypeDef",
    "SqlInjectionMatchSetSummaryTypeDef",
    "SqlInjectionMatchSetTypeDef",
    "SqlInjectionMatchSetUpdateTypeDef",
    "SqlInjectionMatchTupleTypeDef",
    "SubscribedRuleGroupSummaryTypeDef",
    "TagInfoForResourceTypeDef",
    "TagTypeDef",
    "TimeWindowTypeDef",
    "UpdateByteMatchSetResponseTypeDef",
    "UpdateGeoMatchSetResponseTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRateBasedRuleResponseTypeDef",
    "UpdateRegexMatchSetResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateSizeConstraintSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UpdateXssMatchSetResponseTypeDef",
    "WafActionTypeDef",
    "WafOverrideActionTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "WebACLUpdateTypeDef",
    "XssMatchSetSummaryTypeDef",
    "XssMatchSetTypeDef",
    "XssMatchSetUpdateTypeDef",
    "XssMatchTupleTypeDef",
)

_RequiredActivatedRuleTypeDef = TypedDict(
    "_RequiredActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
    },
)
_OptionalActivatedRuleTypeDef = TypedDict(
    "_OptionalActivatedRuleTypeDef",
    {
        "Action": "WafActionTypeDef",
        "OverrideAction": "WafOverrideActionTypeDef",
        "Type": WafRuleTypeType,
        "ExcludedRules": List["ExcludedRuleTypeDef"],
    },
    total=False,
)


class ActivatedRuleTypeDef(_RequiredActivatedRuleTypeDef, _OptionalActivatedRuleTypeDef):
    pass


ByteMatchSetSummaryTypeDef = TypedDict(
    "ByteMatchSetSummaryTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
    },
)

_RequiredByteMatchSetTypeDef = TypedDict(
    "_RequiredByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "ByteMatchTuples": List["ByteMatchTupleTypeDef"],
    },
)
_OptionalByteMatchSetTypeDef = TypedDict(
    "_OptionalByteMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class ByteMatchSetTypeDef(_RequiredByteMatchSetTypeDef, _OptionalByteMatchSetTypeDef):
    pass


ByteMatchSetUpdateTypeDef = TypedDict(
    "ByteMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ByteMatchTuple": "ByteMatchTupleTypeDef",
    },
)

ByteMatchTupleTypeDef = TypedDict(
    "ByteMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TargetString": Union[bytes, IO[bytes]],
        "TextTransformation": TextTransformationType,
        "PositionalConstraint": PositionalConstraintType,
    },
)

CreateByteMatchSetResponseTypeDef = TypedDict(
    "CreateByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateGeoMatchSetResponseTypeDef = TypedDict(
    "CreateGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateRateBasedRuleResponseTypeDef = TypedDict(
    "CreateRateBasedRuleResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateRegexMatchSetResponseTypeDef = TypedDict(
    "CreateRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateSizeConstraintSetResponseTypeDef = TypedDict(
    "CreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateWebACLMigrationStackResponseTypeDef = TypedDict(
    "CreateWebACLMigrationStackResponseTypeDef",
    {
        "S3ObjectUrl": str,
    },
)

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

CreateXssMatchSetResponseTypeDef = TypedDict(
    "CreateXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
        "ChangeToken": str,
    },
    total=False,
)

DeleteByteMatchSetResponseTypeDef = TypedDict(
    "DeleteByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteGeoMatchSetResponseTypeDef = TypedDict(
    "DeleteGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteIPSetResponseTypeDef = TypedDict(
    "DeleteIPSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteRateBasedRuleResponseTypeDef = TypedDict(
    "DeleteRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteRegexMatchSetResponseTypeDef = TypedDict(
    "DeleteRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteRegexPatternSetResponseTypeDef = TypedDict(
    "DeleteRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteRuleResponseTypeDef = TypedDict(
    "DeleteRuleResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "DeleteSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteWebACLResponseTypeDef = TypedDict(
    "DeleteWebACLResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

DeleteXssMatchSetResponseTypeDef = TypedDict(
    "DeleteXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "RuleId": str,
    },
)

_RequiredFieldToMatchTypeDef = TypedDict(
    "_RequiredFieldToMatchTypeDef",
    {
        "Type": MatchFieldTypeType,
    },
)
_OptionalFieldToMatchTypeDef = TypedDict(
    "_OptionalFieldToMatchTypeDef",
    {
        "Data": str,
    },
    total=False,
)


class FieldToMatchTypeDef(_RequiredFieldToMatchTypeDef, _OptionalFieldToMatchTypeDef):
    pass


GeoMatchConstraintTypeDef = TypedDict(
    "GeoMatchConstraintTypeDef",
    {
        "Type": Literal["Country"],
        "Value": GeoMatchConstraintValueType,
    },
)

GeoMatchSetSummaryTypeDef = TypedDict(
    "GeoMatchSetSummaryTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
    },
)

_RequiredGeoMatchSetTypeDef = TypedDict(
    "_RequiredGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "GeoMatchConstraints": List["GeoMatchConstraintTypeDef"],
    },
)
_OptionalGeoMatchSetTypeDef = TypedDict(
    "_OptionalGeoMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class GeoMatchSetTypeDef(_RequiredGeoMatchSetTypeDef, _OptionalGeoMatchSetTypeDef):
    pass


GeoMatchSetUpdateTypeDef = TypedDict(
    "GeoMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "GeoMatchConstraint": "GeoMatchConstraintTypeDef",
    },
)

GetByteMatchSetResponseTypeDef = TypedDict(
    "GetByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
    },
    total=False,
)

GetChangeTokenResponseTypeDef = TypedDict(
    "GetChangeTokenResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

GetChangeTokenStatusResponseTypeDef = TypedDict(
    "GetChangeTokenStatusResponseTypeDef",
    {
        "ChangeTokenStatus": ChangeTokenStatusType,
    },
    total=False,
)

GetGeoMatchSetResponseTypeDef = TypedDict(
    "GetGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
    },
    total=False,
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
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

GetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    {
        "ManagedKeys": List[str],
        "NextMarker": str,
    },
    total=False,
)

GetRateBasedRuleResponseTypeDef = TypedDict(
    "GetRateBasedRuleResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
    },
    total=False,
)

GetRegexMatchSetResponseTypeDef = TypedDict(
    "GetRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
    },
    total=False,
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
    },
    total=False,
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
    },
    total=False,
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
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

GetSizeConstraintSetResponseTypeDef = TypedDict(
    "GetSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
    },
    total=False,
)

GetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "GetSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
    },
    total=False,
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
    },
    total=False,
)

GetXssMatchSetResponseTypeDef = TypedDict(
    "GetXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
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

IPSetDescriptorTypeDef = TypedDict(
    "IPSetDescriptorTypeDef",
    {
        "Type": IPSetDescriptorTypeType,
        "Value": str,
    },
)

IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "IPSetId": str,
        "Name": str,
    },
)

_RequiredIPSetTypeDef = TypedDict(
    "_RequiredIPSetTypeDef",
    {
        "IPSetId": str,
        "IPSetDescriptors": List["IPSetDescriptorTypeDef"],
    },
)
_OptionalIPSetTypeDef = TypedDict(
    "_OptionalIPSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class IPSetTypeDef(_RequiredIPSetTypeDef, _OptionalIPSetTypeDef):
    pass


IPSetUpdateTypeDef = TypedDict(
    "IPSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "IPSetDescriptor": "IPSetDescriptorTypeDef",
    },
)

ListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List["ActivatedRuleTypeDef"],
    },
    total=False,
)

ListByteMatchSetsResponseTypeDef = TypedDict(
    "ListByteMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ByteMatchSets": List["ByteMatchSetSummaryTypeDef"],
    },
    total=False,
)

ListGeoMatchSetsResponseTypeDef = TypedDict(
    "ListGeoMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "GeoMatchSets": List["GeoMatchSetSummaryTypeDef"],
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

ListRateBasedRulesResponseTypeDef = TypedDict(
    "ListRateBasedRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
    },
    total=False,
)

ListRegexMatchSetsResponseTypeDef = TypedDict(
    "ListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List["RegexMatchSetSummaryTypeDef"],
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

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["RuleGroupSummaryTypeDef"],
    },
    total=False,
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
    },
    total=False,
)

ListSizeConstraintSetsResponseTypeDef = TypedDict(
    "ListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List["SizeConstraintSetSummaryTypeDef"],
    },
    total=False,
)

ListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List["SqlInjectionMatchSetSummaryTypeDef"],
    },
    total=False,
)

ListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "ListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["SubscribedRuleGroupSummaryTypeDef"],
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

ListXssMatchSetsResponseTypeDef = TypedDict(
    "ListXssMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "XssMatchSets": List["XssMatchSetSummaryTypeDef"],
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
    },
    total=False,
)


class LoggingConfigurationTypeDef(
    _RequiredLoggingConfigurationTypeDef, _OptionalLoggingConfigurationTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Negated": bool,
        "Type": PredicateTypeType,
        "DataId": str,
    },
)

PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
    total=False,
)

_RequiredRateBasedRuleTypeDef = TypedDict(
    "_RequiredRateBasedRuleTypeDef",
    {
        "RuleId": str,
        "MatchPredicates": List["PredicateTypeDef"],
        "RateKey": Literal["IP"],
        "RateLimit": int,
    },
)
_OptionalRateBasedRuleTypeDef = TypedDict(
    "_OptionalRateBasedRuleTypeDef",
    {
        "Name": str,
        "MetricName": str,
    },
    total=False,
)


class RateBasedRuleTypeDef(_RequiredRateBasedRuleTypeDef, _OptionalRateBasedRuleTypeDef):
    pass


RegexMatchSetSummaryTypeDef = TypedDict(
    "RegexMatchSetSummaryTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
    },
)

RegexMatchSetTypeDef = TypedDict(
    "RegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List["RegexMatchTupleTypeDef"],
    },
    total=False,
)

RegexMatchSetUpdateTypeDef = TypedDict(
    "RegexMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexMatchTuple": "RegexMatchTupleTypeDef",
    },
)

RegexMatchTupleTypeDef = TypedDict(
    "RegexMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
        "RegexPatternSetId": str,
    },
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "RegexPatternSetId": str,
        "Name": str,
    },
)

_RequiredRegexPatternSetTypeDef = TypedDict(
    "_RequiredRegexPatternSetTypeDef",
    {
        "RegexPatternSetId": str,
        "RegexPatternStrings": List[str],
    },
)
_OptionalRegexPatternSetTypeDef = TypedDict(
    "_OptionalRegexPatternSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class RegexPatternSetTypeDef(_RequiredRegexPatternSetTypeDef, _OptionalRegexPatternSetTypeDef):
    pass


RegexPatternSetUpdateTypeDef = TypedDict(
    "RegexPatternSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexPatternString": str,
    },
)

RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
    },
)

_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "RuleGroupId": str,
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "Name": str,
        "MetricName": str,
    },
    total=False,
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


RuleGroupUpdateTypeDef = TypedDict(
    "RuleGroupUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": "ActivatedRuleTypeDef",
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "RuleId": str,
        "Name": str,
    },
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "RuleId": str,
        "Predicates": List["PredicateTypeDef"],
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Name": str,
        "MetricName": str,
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


RuleUpdateTypeDef = TypedDict(
    "RuleUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "Predicate": "PredicateTypeDef",
    },
)

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
        "RuleWithinRuleGroup": str,
    },
    total=False,
)


class SampledHTTPRequestTypeDef(
    _RequiredSampledHTTPRequestTypeDef, _OptionalSampledHTTPRequestTypeDef
):
    pass


SizeConstraintSetSummaryTypeDef = TypedDict(
    "SizeConstraintSetSummaryTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
    },
)

_RequiredSizeConstraintSetTypeDef = TypedDict(
    "_RequiredSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "SizeConstraints": List["SizeConstraintTypeDef"],
    },
)
_OptionalSizeConstraintSetTypeDef = TypedDict(
    "_OptionalSizeConstraintSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class SizeConstraintSetTypeDef(
    _RequiredSizeConstraintSetTypeDef, _OptionalSizeConstraintSetTypeDef
):
    pass


SizeConstraintSetUpdateTypeDef = TypedDict(
    "SizeConstraintSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SizeConstraint": "SizeConstraintTypeDef",
    },
)

SizeConstraintTypeDef = TypedDict(
    "SizeConstraintTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
    },
)

SqlInjectionMatchSetSummaryTypeDef = TypedDict(
    "SqlInjectionMatchSetSummaryTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
    },
)

_RequiredSqlInjectionMatchSetTypeDef = TypedDict(
    "_RequiredSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "SqlInjectionMatchTuples": List["SqlInjectionMatchTupleTypeDef"],
    },
)
_OptionalSqlInjectionMatchSetTypeDef = TypedDict(
    "_OptionalSqlInjectionMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class SqlInjectionMatchSetTypeDef(
    _RequiredSqlInjectionMatchSetTypeDef, _OptionalSqlInjectionMatchSetTypeDef
):
    pass


SqlInjectionMatchSetUpdateTypeDef = TypedDict(
    "SqlInjectionMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SqlInjectionMatchTuple": "SqlInjectionMatchTupleTypeDef",
    },
)

SqlInjectionMatchTupleTypeDef = TypedDict(
    "SqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
    },
)

SubscribedRuleGroupSummaryTypeDef = TypedDict(
    "SubscribedRuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
        "MetricName": str,
    },
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

TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)

UpdateByteMatchSetResponseTypeDef = TypedDict(
    "UpdateByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateGeoMatchSetResponseTypeDef = TypedDict(
    "UpdateGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateRateBasedRuleResponseTypeDef = TypedDict(
    "UpdateRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateRegexMatchSetResponseTypeDef = TypedDict(
    "UpdateRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "UpdateSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

UpdateXssMatchSetResponseTypeDef = TypedDict(
    "UpdateXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
    },
    total=False,
)

WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": WafActionTypeType,
    },
)

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": WafOverrideActionTypeType,
    },
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "WebACLId": str,
        "Name": str,
    },
)

_RequiredWebACLTypeDef = TypedDict(
    "_RequiredWebACLTypeDef",
    {
        "WebACLId": str,
        "DefaultAction": "WafActionTypeDef",
        "Rules": List["ActivatedRuleTypeDef"],
    },
)
_OptionalWebACLTypeDef = TypedDict(
    "_OptionalWebACLTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "WebACLArn": str,
    },
    total=False,
)


class WebACLTypeDef(_RequiredWebACLTypeDef, _OptionalWebACLTypeDef):
    pass


WebACLUpdateTypeDef = TypedDict(
    "WebACLUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": "ActivatedRuleTypeDef",
    },
)

XssMatchSetSummaryTypeDef = TypedDict(
    "XssMatchSetSummaryTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
    },
)

_RequiredXssMatchSetTypeDef = TypedDict(
    "_RequiredXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "XssMatchTuples": List["XssMatchTupleTypeDef"],
    },
)
_OptionalXssMatchSetTypeDef = TypedDict(
    "_OptionalXssMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class XssMatchSetTypeDef(_RequiredXssMatchSetTypeDef, _OptionalXssMatchSetTypeDef):
    pass


XssMatchSetUpdateTypeDef = TypedDict(
    "XssMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "XssMatchTuple": "XssMatchTupleTypeDef",
    },
)

XssMatchTupleTypeDef = TypedDict(
    "XssMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
    },
)
