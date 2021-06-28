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
from typing import Any, Dict, List, Union

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
    "CreateByteMatchSetRequestTypeDef",
    "CreateByteMatchSetResponseResponseTypeDef",
    "CreateGeoMatchSetRequestTypeDef",
    "CreateGeoMatchSetResponseResponseTypeDef",
    "CreateIPSetRequestTypeDef",
    "CreateIPSetResponseResponseTypeDef",
    "CreateRateBasedRuleRequestTypeDef",
    "CreateRateBasedRuleResponseResponseTypeDef",
    "CreateRegexMatchSetRequestTypeDef",
    "CreateRegexMatchSetResponseResponseTypeDef",
    "CreateRegexPatternSetRequestTypeDef",
    "CreateRegexPatternSetResponseResponseTypeDef",
    "CreateRuleGroupRequestTypeDef",
    "CreateRuleGroupResponseResponseTypeDef",
    "CreateRuleRequestTypeDef",
    "CreateRuleResponseResponseTypeDef",
    "CreateSizeConstraintSetRequestTypeDef",
    "CreateSizeConstraintSetResponseResponseTypeDef",
    "CreateSqlInjectionMatchSetRequestTypeDef",
    "CreateSqlInjectionMatchSetResponseResponseTypeDef",
    "CreateWebACLMigrationStackRequestTypeDef",
    "CreateWebACLMigrationStackResponseResponseTypeDef",
    "CreateWebACLRequestTypeDef",
    "CreateWebACLResponseResponseTypeDef",
    "CreateXssMatchSetRequestTypeDef",
    "CreateXssMatchSetResponseResponseTypeDef",
    "DeleteByteMatchSetRequestTypeDef",
    "DeleteByteMatchSetResponseResponseTypeDef",
    "DeleteGeoMatchSetRequestTypeDef",
    "DeleteGeoMatchSetResponseResponseTypeDef",
    "DeleteIPSetRequestTypeDef",
    "DeleteIPSetResponseResponseTypeDef",
    "DeleteLoggingConfigurationRequestTypeDef",
    "DeletePermissionPolicyRequestTypeDef",
    "DeleteRateBasedRuleRequestTypeDef",
    "DeleteRateBasedRuleResponseResponseTypeDef",
    "DeleteRegexMatchSetRequestTypeDef",
    "DeleteRegexMatchSetResponseResponseTypeDef",
    "DeleteRegexPatternSetRequestTypeDef",
    "DeleteRegexPatternSetResponseResponseTypeDef",
    "DeleteRuleGroupRequestTypeDef",
    "DeleteRuleGroupResponseResponseTypeDef",
    "DeleteRuleRequestTypeDef",
    "DeleteRuleResponseResponseTypeDef",
    "DeleteSizeConstraintSetRequestTypeDef",
    "DeleteSizeConstraintSetResponseResponseTypeDef",
    "DeleteSqlInjectionMatchSetRequestTypeDef",
    "DeleteSqlInjectionMatchSetResponseResponseTypeDef",
    "DeleteWebACLRequestTypeDef",
    "DeleteWebACLResponseResponseTypeDef",
    "DeleteXssMatchSetRequestTypeDef",
    "DeleteXssMatchSetResponseResponseTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "GetByteMatchSetRequestTypeDef",
    "GetByteMatchSetResponseResponseTypeDef",
    "GetChangeTokenResponseResponseTypeDef",
    "GetChangeTokenStatusRequestTypeDef",
    "GetChangeTokenStatusResponseResponseTypeDef",
    "GetGeoMatchSetRequestTypeDef",
    "GetGeoMatchSetResponseResponseTypeDef",
    "GetIPSetRequestTypeDef",
    "GetIPSetResponseResponseTypeDef",
    "GetLoggingConfigurationRequestTypeDef",
    "GetLoggingConfigurationResponseResponseTypeDef",
    "GetPermissionPolicyRequestTypeDef",
    "GetPermissionPolicyResponseResponseTypeDef",
    "GetRateBasedRuleManagedKeysRequestTypeDef",
    "GetRateBasedRuleManagedKeysResponseResponseTypeDef",
    "GetRateBasedRuleRequestTypeDef",
    "GetRateBasedRuleResponseResponseTypeDef",
    "GetRegexMatchSetRequestTypeDef",
    "GetRegexMatchSetResponseResponseTypeDef",
    "GetRegexPatternSetRequestTypeDef",
    "GetRegexPatternSetResponseResponseTypeDef",
    "GetRuleGroupRequestTypeDef",
    "GetRuleGroupResponseResponseTypeDef",
    "GetRuleRequestTypeDef",
    "GetRuleResponseResponseTypeDef",
    "GetSampledRequestsRequestTypeDef",
    "GetSampledRequestsResponseResponseTypeDef",
    "GetSizeConstraintSetRequestTypeDef",
    "GetSizeConstraintSetResponseResponseTypeDef",
    "GetSqlInjectionMatchSetRequestTypeDef",
    "GetSqlInjectionMatchSetResponseResponseTypeDef",
    "GetWebACLRequestTypeDef",
    "GetWebACLResponseResponseTypeDef",
    "GetXssMatchSetRequestTypeDef",
    "GetXssMatchSetResponseResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListActivatedRulesInRuleGroupRequestTypeDef",
    "ListActivatedRulesInRuleGroupResponseResponseTypeDef",
    "ListByteMatchSetsRequestTypeDef",
    "ListByteMatchSetsResponseResponseTypeDef",
    "ListGeoMatchSetsRequestTypeDef",
    "ListGeoMatchSetsResponseResponseTypeDef",
    "ListIPSetsRequestTypeDef",
    "ListIPSetsResponseResponseTypeDef",
    "ListLoggingConfigurationsRequestTypeDef",
    "ListLoggingConfigurationsResponseResponseTypeDef",
    "ListRateBasedRulesRequestTypeDef",
    "ListRateBasedRulesResponseResponseTypeDef",
    "ListRegexMatchSetsRequestTypeDef",
    "ListRegexMatchSetsResponseResponseTypeDef",
    "ListRegexPatternSetsRequestTypeDef",
    "ListRegexPatternSetsResponseResponseTypeDef",
    "ListRuleGroupsRequestTypeDef",
    "ListRuleGroupsResponseResponseTypeDef",
    "ListRulesRequestTypeDef",
    "ListRulesResponseResponseTypeDef",
    "ListSizeConstraintSetsRequestTypeDef",
    "ListSizeConstraintSetsResponseResponseTypeDef",
    "ListSqlInjectionMatchSetsRequestTypeDef",
    "ListSqlInjectionMatchSetsResponseResponseTypeDef",
    "ListSubscribedRuleGroupsRequestTypeDef",
    "ListSubscribedRuleGroupsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListWebACLsRequestTypeDef",
    "ListWebACLsResponseResponseTypeDef",
    "ListXssMatchSetsRequestTypeDef",
    "ListXssMatchSetsResponseResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "PutLoggingConfigurationRequestTypeDef",
    "PutLoggingConfigurationResponseResponseTypeDef",
    "PutPermissionPolicyRequestTypeDef",
    "RateBasedRuleTypeDef",
    "RegexMatchSetSummaryTypeDef",
    "RegexMatchSetTypeDef",
    "RegexMatchSetUpdateTypeDef",
    "RegexMatchTupleTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexPatternSetUpdateTypeDef",
    "ResponseMetadataTypeDef",
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
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeWindowTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateByteMatchSetRequestTypeDef",
    "UpdateByteMatchSetResponseResponseTypeDef",
    "UpdateGeoMatchSetRequestTypeDef",
    "UpdateGeoMatchSetResponseResponseTypeDef",
    "UpdateIPSetRequestTypeDef",
    "UpdateIPSetResponseResponseTypeDef",
    "UpdateRateBasedRuleRequestTypeDef",
    "UpdateRateBasedRuleResponseResponseTypeDef",
    "UpdateRegexMatchSetRequestTypeDef",
    "UpdateRegexMatchSetResponseResponseTypeDef",
    "UpdateRegexPatternSetRequestTypeDef",
    "UpdateRegexPatternSetResponseResponseTypeDef",
    "UpdateRuleGroupRequestTypeDef",
    "UpdateRuleGroupResponseResponseTypeDef",
    "UpdateRuleRequestTypeDef",
    "UpdateRuleResponseResponseTypeDef",
    "UpdateSizeConstraintSetRequestTypeDef",
    "UpdateSizeConstraintSetResponseResponseTypeDef",
    "UpdateSqlInjectionMatchSetRequestTypeDef",
    "UpdateSqlInjectionMatchSetResponseResponseTypeDef",
    "UpdateWebACLRequestTypeDef",
    "UpdateWebACLResponseResponseTypeDef",
    "UpdateXssMatchSetRequestTypeDef",
    "UpdateXssMatchSetResponseResponseTypeDef",
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
        "TargetString": bytes,
        "TextTransformation": TextTransformationType,
        "PositionalConstraint": PositionalConstraintType,
    },
)

CreateByteMatchSetRequestTypeDef = TypedDict(
    "CreateByteMatchSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateByteMatchSetResponseResponseTypeDef = TypedDict(
    "CreateByteMatchSetResponseResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGeoMatchSetRequestTypeDef = TypedDict(
    "CreateGeoMatchSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateGeoMatchSetResponseResponseTypeDef = TypedDict(
    "CreateGeoMatchSetResponseResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIPSetRequestTypeDef = TypedDict(
    "CreateIPSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateIPSetResponseResponseTypeDef = TypedDict(
    "CreateIPSetResponseResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRateBasedRuleRequestTypeDef = TypedDict(
    "_RequiredCreateRateBasedRuleRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "RateKey": Literal["IP"],
        "RateLimit": int,
        "ChangeToken": str,
    },
)
_OptionalCreateRateBasedRuleRequestTypeDef = TypedDict(
    "_OptionalCreateRateBasedRuleRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRateBasedRuleRequestTypeDef(
    _RequiredCreateRateBasedRuleRequestTypeDef, _OptionalCreateRateBasedRuleRequestTypeDef
):
    pass


CreateRateBasedRuleResponseResponseTypeDef = TypedDict(
    "CreateRateBasedRuleResponseResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexMatchSetRequestTypeDef = TypedDict(
    "CreateRegexMatchSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateRegexMatchSetResponseResponseTypeDef = TypedDict(
    "CreateRegexMatchSetResponseResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexPatternSetRequestTypeDef = TypedDict(
    "CreateRegexPatternSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateRegexPatternSetResponseResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
    },
)
_OptionalCreateRuleGroupRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRuleGroupRequestTypeDef(
    _RequiredCreateRuleGroupRequestTypeDef, _OptionalCreateRuleGroupRequestTypeDef
):
    pass


CreateRuleGroupResponseResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
    },
)
_OptionalCreateRuleRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRuleRequestTypeDef(
    _RequiredCreateRuleRequestTypeDef, _OptionalCreateRuleRequestTypeDef
):
    pass


CreateRuleResponseResponseTypeDef = TypedDict(
    "CreateRuleResponseResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSizeConstraintSetRequestTypeDef = TypedDict(
    "CreateSizeConstraintSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateSizeConstraintSetResponseResponseTypeDef = TypedDict(
    "CreateSizeConstraintSetResponseResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSqlInjectionMatchSetRequestTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateSqlInjectionMatchSetResponseResponseTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetResponseResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebACLMigrationStackRequestTypeDef = TypedDict(
    "CreateWebACLMigrationStackRequestTypeDef",
    {
        "WebACLId": str,
        "S3BucketName": str,
        "IgnoreUnsupportedType": bool,
    },
)

CreateWebACLMigrationStackResponseResponseTypeDef = TypedDict(
    "CreateWebACLMigrationStackResponseResponseTypeDef",
    {
        "S3ObjectUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWebACLRequestTypeDef = TypedDict(
    "_RequiredCreateWebACLRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "DefaultAction": "WafActionTypeDef",
        "ChangeToken": str,
    },
)
_OptionalCreateWebACLRequestTypeDef = TypedDict(
    "_OptionalCreateWebACLRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWebACLRequestTypeDef(
    _RequiredCreateWebACLRequestTypeDef, _OptionalCreateWebACLRequestTypeDef
):
    pass


CreateWebACLResponseResponseTypeDef = TypedDict(
    "CreateWebACLResponseResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateXssMatchSetRequestTypeDef = TypedDict(
    "CreateXssMatchSetRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateXssMatchSetResponseResponseTypeDef = TypedDict(
    "CreateXssMatchSetResponseResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteByteMatchSetRequestTypeDef = TypedDict(
    "DeleteByteMatchSetRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteByteMatchSetResponseResponseTypeDef = TypedDict(
    "DeleteByteMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGeoMatchSetRequestTypeDef = TypedDict(
    "DeleteGeoMatchSetRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteGeoMatchSetResponseResponseTypeDef = TypedDict(
    "DeleteGeoMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIPSetRequestTypeDef = TypedDict(
    "DeleteIPSetRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
    },
)

DeleteIPSetResponseResponseTypeDef = TypedDict(
    "DeleteIPSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLoggingConfigurationRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeletePermissionPolicyRequestTypeDef = TypedDict(
    "DeletePermissionPolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRateBasedRuleRequestTypeDef = TypedDict(
    "DeleteRateBasedRuleRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)

DeleteRateBasedRuleResponseResponseTypeDef = TypedDict(
    "DeleteRateBasedRuleResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegexMatchSetRequestTypeDef = TypedDict(
    "DeleteRegexMatchSetRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteRegexMatchSetResponseResponseTypeDef = TypedDict(
    "DeleteRegexMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegexPatternSetRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "ChangeToken": str,
    },
)

DeleteRegexPatternSetResponseResponseTypeDef = TypedDict(
    "DeleteRegexPatternSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleGroupRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestTypeDef",
    {
        "RuleGroupId": str,
        "ChangeToken": str,
    },
)

DeleteRuleGroupResponseResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleRequestTypeDef = TypedDict(
    "DeleteRuleRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)

DeleteRuleResponseResponseTypeDef = TypedDict(
    "DeleteRuleResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSizeConstraintSetRequestTypeDef = TypedDict(
    "DeleteSizeConstraintSetRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
    },
)

DeleteSizeConstraintSetResponseResponseTypeDef = TypedDict(
    "DeleteSizeConstraintSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSqlInjectionMatchSetRequestTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteSqlInjectionMatchSetResponseResponseTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebACLRequestTypeDef = TypedDict(
    "DeleteWebACLRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
    },
)

DeleteWebACLResponseResponseTypeDef = TypedDict(
    "DeleteWebACLResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteXssMatchSetRequestTypeDef = TypedDict(
    "DeleteXssMatchSetRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteXssMatchSetResponseResponseTypeDef = TypedDict(
    "DeleteXssMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetByteMatchSetRequestTypeDef = TypedDict(
    "GetByteMatchSetRequestTypeDef",
    {
        "ByteMatchSetId": str,
    },
)

GetByteMatchSetResponseResponseTypeDef = TypedDict(
    "GetByteMatchSetResponseResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeTokenResponseResponseTypeDef = TypedDict(
    "GetChangeTokenResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeTokenStatusRequestTypeDef = TypedDict(
    "GetChangeTokenStatusRequestTypeDef",
    {
        "ChangeToken": str,
    },
)

GetChangeTokenStatusResponseResponseTypeDef = TypedDict(
    "GetChangeTokenStatusResponseResponseTypeDef",
    {
        "ChangeTokenStatus": ChangeTokenStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeoMatchSetRequestTypeDef = TypedDict(
    "GetGeoMatchSetRequestTypeDef",
    {
        "GeoMatchSetId": str,
    },
)

GetGeoMatchSetResponseResponseTypeDef = TypedDict(
    "GetGeoMatchSetResponseResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIPSetRequestTypeDef = TypedDict(
    "GetIPSetRequestTypeDef",
    {
        "IPSetId": str,
    },
)

GetIPSetResponseResponseTypeDef = TypedDict(
    "GetIPSetResponseResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingConfigurationRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionPolicyRequestTypeDef = TypedDict(
    "GetPermissionPolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetPermissionPolicyResponseResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRateBasedRuleManagedKeysRequestTypeDef = TypedDict(
    "_RequiredGetRateBasedRuleManagedKeysRequestTypeDef",
    {
        "RuleId": str,
    },
)
_OptionalGetRateBasedRuleManagedKeysRequestTypeDef = TypedDict(
    "_OptionalGetRateBasedRuleManagedKeysRequestTypeDef",
    {
        "NextMarker": str,
    },
    total=False,
)


class GetRateBasedRuleManagedKeysRequestTypeDef(
    _RequiredGetRateBasedRuleManagedKeysRequestTypeDef,
    _OptionalGetRateBasedRuleManagedKeysRequestTypeDef,
):
    pass


GetRateBasedRuleManagedKeysResponseResponseTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysResponseResponseTypeDef",
    {
        "ManagedKeys": List[str],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRateBasedRuleRequestTypeDef = TypedDict(
    "GetRateBasedRuleRequestTypeDef",
    {
        "RuleId": str,
    },
)

GetRateBasedRuleResponseResponseTypeDef = TypedDict(
    "GetRateBasedRuleResponseResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexMatchSetRequestTypeDef = TypedDict(
    "GetRegexMatchSetRequestTypeDef",
    {
        "RegexMatchSetId": str,
    },
)

GetRegexMatchSetResponseResponseTypeDef = TypedDict(
    "GetRegexMatchSetResponseResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexPatternSetRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestTypeDef",
    {
        "RegexPatternSetId": str,
    },
)

GetRegexPatternSetResponseResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleGroupRequestTypeDef = TypedDict(
    "GetRuleGroupRequestTypeDef",
    {
        "RuleGroupId": str,
    },
)

GetRuleGroupResponseResponseTypeDef = TypedDict(
    "GetRuleGroupResponseResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleRequestTypeDef = TypedDict(
    "GetRuleRequestTypeDef",
    {
        "RuleId": str,
    },
)

GetRuleResponseResponseTypeDef = TypedDict(
    "GetRuleResponseResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampledRequestsRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestTypeDef",
    {
        "WebAclId": str,
        "RuleId": str,
        "TimeWindow": "TimeWindowTypeDef",
        "MaxItems": int,
    },
)

GetSampledRequestsResponseResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseResponseTypeDef",
    {
        "SampledRequests": List["SampledHTTPRequestTypeDef"],
        "PopulationSize": int,
        "TimeWindow": "TimeWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSizeConstraintSetRequestTypeDef = TypedDict(
    "GetSizeConstraintSetRequestTypeDef",
    {
        "SizeConstraintSetId": str,
    },
)

GetSizeConstraintSetResponseResponseTypeDef = TypedDict(
    "GetSizeConstraintSetResponseResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSqlInjectionMatchSetRequestTypeDef = TypedDict(
    "GetSqlInjectionMatchSetRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
    },
)

GetSqlInjectionMatchSetResponseResponseTypeDef = TypedDict(
    "GetSqlInjectionMatchSetResponseResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLRequestTypeDef = TypedDict(
    "GetWebACLRequestTypeDef",
    {
        "WebACLId": str,
    },
)

GetWebACLResponseResponseTypeDef = TypedDict(
    "GetWebACLResponseResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetXssMatchSetRequestTypeDef = TypedDict(
    "GetXssMatchSetRequestTypeDef",
    {
        "XssMatchSetId": str,
    },
)

GetXssMatchSetResponseResponseTypeDef = TypedDict(
    "GetXssMatchSetResponseResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListActivatedRulesInRuleGroupRequestTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupRequestTypeDef",
    {
        "RuleGroupId": str,
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListActivatedRulesInRuleGroupResponseResponseTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupResponseResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List["ActivatedRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListByteMatchSetsRequestTypeDef = TypedDict(
    "ListByteMatchSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListByteMatchSetsResponseResponseTypeDef = TypedDict(
    "ListByteMatchSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "ByteMatchSets": List["ByteMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeoMatchSetsRequestTypeDef = TypedDict(
    "ListGeoMatchSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListGeoMatchSetsResponseResponseTypeDef = TypedDict(
    "ListGeoMatchSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "GeoMatchSets": List["GeoMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIPSetsRequestTypeDef = TypedDict(
    "ListIPSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListIPSetsResponseResponseTypeDef = TypedDict(
    "ListIPSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List["IPSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggingConfigurationsRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListLoggingConfigurationsResponseResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseResponseTypeDef",
    {
        "LoggingConfigurations": List["LoggingConfigurationTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRateBasedRulesRequestTypeDef = TypedDict(
    "ListRateBasedRulesRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRateBasedRulesResponseResponseTypeDef = TypedDict(
    "ListRateBasedRulesResponseResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexMatchSetsRequestTypeDef = TypedDict(
    "ListRegexMatchSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRegexMatchSetsResponseResponseTypeDef = TypedDict(
    "ListRegexMatchSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List["RegexMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexPatternSetsRequestTypeDef = TypedDict(
    "ListRegexPatternSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRegexPatternSetsResponseResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List["RegexPatternSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRuleGroupsRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRuleGroupsResponseResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["RuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestTypeDef = TypedDict(
    "ListRulesRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRulesResponseResponseTypeDef = TypedDict(
    "ListRulesResponseResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSizeConstraintSetsRequestTypeDef = TypedDict(
    "ListSizeConstraintSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListSizeConstraintSetsResponseResponseTypeDef = TypedDict(
    "ListSizeConstraintSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List["SizeConstraintSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSqlInjectionMatchSetsRequestTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListSqlInjectionMatchSetsResponseResponseTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List["SqlInjectionMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribedRuleGroupsRequestTypeDef = TypedDict(
    "ListSubscribedRuleGroupsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListSubscribedRuleGroupsResponseResponseTypeDef = TypedDict(
    "ListSubscribedRuleGroupsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["SubscribedRuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
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
        "NextMarker": str,
        "TagInfoForResource": "TagInfoForResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWebACLsRequestTypeDef = TypedDict(
    "ListWebACLsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListWebACLsResponseResponseTypeDef = TypedDict(
    "ListWebACLsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List["WebACLSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListXssMatchSetsRequestTypeDef = TypedDict(
    "ListXssMatchSetsRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListXssMatchSetsResponseResponseTypeDef = TypedDict(
    "ListXssMatchSetsResponseResponseTypeDef",
    {
        "NextMarker": str,
        "XssMatchSets": List["XssMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutLoggingConfigurationRequestTypeDef = TypedDict(
    "PutLoggingConfigurationRequestTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPermissionPolicyRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
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
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateByteMatchSetRequestTypeDef = TypedDict(
    "UpdateByteMatchSetRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["ByteMatchSetUpdateTypeDef"],
    },
)

UpdateByteMatchSetResponseResponseTypeDef = TypedDict(
    "UpdateByteMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGeoMatchSetRequestTypeDef = TypedDict(
    "UpdateGeoMatchSetRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["GeoMatchSetUpdateTypeDef"],
    },
)

UpdateGeoMatchSetResponseResponseTypeDef = TypedDict(
    "UpdateGeoMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIPSetRequestTypeDef = TypedDict(
    "UpdateIPSetRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
        "Updates": List["IPSetUpdateTypeDef"],
    },
)

UpdateIPSetResponseResponseTypeDef = TypedDict(
    "UpdateIPSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRateBasedRuleRequestTypeDef = TypedDict(
    "UpdateRateBasedRuleRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": List["RuleUpdateTypeDef"],
        "RateLimit": int,
    },
)

UpdateRateBasedRuleResponseResponseTypeDef = TypedDict(
    "UpdateRateBasedRuleResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexMatchSetRequestTypeDef = TypedDict(
    "UpdateRegexMatchSetRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "Updates": List["RegexMatchSetUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRegexMatchSetResponseResponseTypeDef = TypedDict(
    "UpdateRegexMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexPatternSetRequestTypeDef = TypedDict(
    "UpdateRegexPatternSetRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "Updates": List["RegexPatternSetUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRegexPatternSetResponseResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleGroupRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestTypeDef",
    {
        "RuleGroupId": str,
        "Updates": List["RuleGroupUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRuleGroupResponseResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleRequestTypeDef = TypedDict(
    "UpdateRuleRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": List["RuleUpdateTypeDef"],
    },
)

UpdateRuleResponseResponseTypeDef = TypedDict(
    "UpdateRuleResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSizeConstraintSetRequestTypeDef = TypedDict(
    "UpdateSizeConstraintSetRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
        "Updates": List["SizeConstraintSetUpdateTypeDef"],
    },
)

UpdateSizeConstraintSetResponseResponseTypeDef = TypedDict(
    "UpdateSizeConstraintSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSqlInjectionMatchSetRequestTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["SqlInjectionMatchSetUpdateTypeDef"],
    },
)

UpdateSqlInjectionMatchSetResponseResponseTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWebACLRequestTypeDef = TypedDict(
    "_RequiredUpdateWebACLRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
    },
)
_OptionalUpdateWebACLRequestTypeDef = TypedDict(
    "_OptionalUpdateWebACLRequestTypeDef",
    {
        "Updates": List["WebACLUpdateTypeDef"],
        "DefaultAction": "WafActionTypeDef",
    },
    total=False,
)


class UpdateWebACLRequestTypeDef(
    _RequiredUpdateWebACLRequestTypeDef, _OptionalUpdateWebACLRequestTypeDef
):
    pass


UpdateWebACLResponseResponseTypeDef = TypedDict(
    "UpdateWebACLResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateXssMatchSetRequestTypeDef = TypedDict(
    "UpdateXssMatchSetRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["XssMatchSetUpdateTypeDef"],
    },
)

UpdateXssMatchSetResponseResponseTypeDef = TypedDict(
    "UpdateXssMatchSetResponseResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
