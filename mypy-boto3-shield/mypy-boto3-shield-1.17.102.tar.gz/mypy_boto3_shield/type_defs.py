"""
Type annotations for shield service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/type_defs.html)

Usage::

    ```python
    from mypy_boto3_shield.type_defs import AssociateDRTLogBucketRequestTypeDef

    data: AssociateDRTLogBucketRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttackLayerType,
    AttackPropertyIdentifierType,
    AutoRenewType,
    ProactiveEngagementStatusType,
    ProtectedResourceTypeType,
    ProtectionGroupAggregationType,
    ProtectionGroupPatternType,
    SubResourceTypeType,
    SubscriptionStateType,
    UnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateDRTLogBucketRequestTypeDef",
    "AssociateDRTRoleRequestTypeDef",
    "AssociateHealthCheckRequestTypeDef",
    "AssociateProactiveEngagementDetailsRequestTypeDef",
    "AttackDetailTypeDef",
    "AttackPropertyTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "AttackVolumeTypeDef",
    "ContributorTypeDef",
    "CreateProtectionGroupRequestTypeDef",
    "CreateProtectionRequestTypeDef",
    "CreateProtectionResponseResponseTypeDef",
    "DeleteProtectionGroupRequestTypeDef",
    "DeleteProtectionRequestTypeDef",
    "DescribeAttackRequestTypeDef",
    "DescribeAttackResponseResponseTypeDef",
    "DescribeAttackStatisticsResponseResponseTypeDef",
    "DescribeDRTAccessResponseResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseResponseTypeDef",
    "DescribeProtectionGroupRequestTypeDef",
    "DescribeProtectionGroupResponseResponseTypeDef",
    "DescribeProtectionRequestTypeDef",
    "DescribeProtectionResponseResponseTypeDef",
    "DescribeSubscriptionResponseResponseTypeDef",
    "DisassociateDRTLogBucketRequestTypeDef",
    "DisassociateHealthCheckRequestTypeDef",
    "EmergencyContactTypeDef",
    "GetSubscriptionStateResponseResponseTypeDef",
    "LimitTypeDef",
    "ListAttacksRequestTypeDef",
    "ListAttacksResponseResponseTypeDef",
    "ListProtectionGroupsRequestTypeDef",
    "ListProtectionGroupsResponseResponseTypeDef",
    "ListProtectionsRequestTypeDef",
    "ListProtectionsResponseResponseTypeDef",
    "ListResourcesInProtectionGroupRequestTypeDef",
    "ListResourcesInProtectionGroupResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MitigationTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "ProtectionGroupTypeDef",
    "ProtectionLimitsTypeDef",
    "ProtectionTypeDef",
    "ResponseMetadataTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionLimitsTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEmergencyContactSettingsRequestTypeDef",
    "UpdateProtectionGroupRequestTypeDef",
    "UpdateSubscriptionRequestTypeDef",
)

AssociateDRTLogBucketRequestTypeDef = TypedDict(
    "AssociateDRTLogBucketRequestTypeDef",
    {
        "LogBucket": str,
    },
)

AssociateDRTRoleRequestTypeDef = TypedDict(
    "AssociateDRTRoleRequestTypeDef",
    {
        "RoleArn": str,
    },
)

AssociateHealthCheckRequestTypeDef = TypedDict(
    "AssociateHealthCheckRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)

AssociateProactiveEngagementDetailsRequestTypeDef = TypedDict(
    "AssociateProactiveEngagementDetailsRequestTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
    },
)

AttackDetailTypeDef = TypedDict(
    "AttackDetailTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "SubResources": List["SubResourceSummaryTypeDef"],
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackCounters": List["SummarizedCounterTypeDef"],
        "AttackProperties": List["AttackPropertyTypeDef"],
        "Mitigations": List["MitigationTypeDef"],
    },
    total=False,
)

AttackPropertyTypeDef = TypedDict(
    "AttackPropertyTypeDef",
    {
        "AttackLayer": AttackLayerType,
        "AttackPropertyIdentifier": AttackPropertyIdentifierType,
        "TopContributors": List["ContributorTypeDef"],
        "Unit": UnitType,
        "Total": int,
    },
    total=False,
)

_RequiredAttackStatisticsDataItemTypeDef = TypedDict(
    "_RequiredAttackStatisticsDataItemTypeDef",
    {
        "AttackCount": int,
    },
)
_OptionalAttackStatisticsDataItemTypeDef = TypedDict(
    "_OptionalAttackStatisticsDataItemTypeDef",
    {
        "AttackVolume": "AttackVolumeTypeDef",
    },
    total=False,
)


class AttackStatisticsDataItemTypeDef(
    _RequiredAttackStatisticsDataItemTypeDef, _OptionalAttackStatisticsDataItemTypeDef
):
    pass


AttackSummaryTypeDef = TypedDict(
    "AttackSummaryTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List["AttackVectorDescriptionTypeDef"],
    },
    total=False,
)

AttackVectorDescriptionTypeDef = TypedDict(
    "AttackVectorDescriptionTypeDef",
    {
        "VectorType": str,
    },
)

AttackVolumeStatisticsTypeDef = TypedDict(
    "AttackVolumeStatisticsTypeDef",
    {
        "Max": float,
    },
)

AttackVolumeTypeDef = TypedDict(
    "AttackVolumeTypeDef",
    {
        "BitsPerSecond": "AttackVolumeStatisticsTypeDef",
        "PacketsPerSecond": "AttackVolumeStatisticsTypeDef",
        "RequestsPerSecond": "AttackVolumeStatisticsTypeDef",
    },
    total=False,
)

ContributorTypeDef = TypedDict(
    "ContributorTypeDef",
    {
        "Name": str,
        "Value": int,
    },
    total=False,
)

_RequiredCreateProtectionGroupRequestTypeDef = TypedDict(
    "_RequiredCreateProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
    },
)
_OptionalCreateProtectionGroupRequestTypeDef = TypedDict(
    "_OptionalCreateProtectionGroupRequestTypeDef",
    {
        "ResourceType": ProtectedResourceTypeType,
        "Members": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProtectionGroupRequestTypeDef(
    _RequiredCreateProtectionGroupRequestTypeDef, _OptionalCreateProtectionGroupRequestTypeDef
):
    pass


_RequiredCreateProtectionRequestTypeDef = TypedDict(
    "_RequiredCreateProtectionRequestTypeDef",
    {
        "Name": str,
        "ResourceArn": str,
    },
)
_OptionalCreateProtectionRequestTypeDef = TypedDict(
    "_OptionalCreateProtectionRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProtectionRequestTypeDef(
    _RequiredCreateProtectionRequestTypeDef, _OptionalCreateProtectionRequestTypeDef
):
    pass


CreateProtectionResponseResponseTypeDef = TypedDict(
    "CreateProtectionResponseResponseTypeDef",
    {
        "ProtectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProtectionGroupRequestTypeDef = TypedDict(
    "DeleteProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)

DeleteProtectionRequestTypeDef = TypedDict(
    "DeleteProtectionRequestTypeDef",
    {
        "ProtectionId": str,
    },
)

DescribeAttackRequestTypeDef = TypedDict(
    "DescribeAttackRequestTypeDef",
    {
        "AttackId": str,
    },
)

DescribeAttackResponseResponseTypeDef = TypedDict(
    "DescribeAttackResponseResponseTypeDef",
    {
        "Attack": "AttackDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAttackStatisticsResponseResponseTypeDef = TypedDict(
    "DescribeAttackStatisticsResponseResponseTypeDef",
    {
        "TimeRange": "TimeRangeTypeDef",
        "DataItems": List["AttackStatisticsDataItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDRTAccessResponseResponseTypeDef = TypedDict(
    "DescribeDRTAccessResponseResponseTypeDef",
    {
        "RoleArn": str,
        "LogBucketList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEmergencyContactSettingsResponseResponseTypeDef = TypedDict(
    "DescribeEmergencyContactSettingsResponseResponseTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectionGroupRequestTypeDef = TypedDict(
    "DescribeProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)

DescribeProtectionGroupResponseResponseTypeDef = TypedDict(
    "DescribeProtectionGroupResponseResponseTypeDef",
    {
        "ProtectionGroup": "ProtectionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectionRequestTypeDef = TypedDict(
    "DescribeProtectionRequestTypeDef",
    {
        "ProtectionId": str,
        "ResourceArn": str,
    },
    total=False,
)

DescribeProtectionResponseResponseTypeDef = TypedDict(
    "DescribeProtectionResponseResponseTypeDef",
    {
        "Protection": "ProtectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscriptionResponseResponseTypeDef = TypedDict(
    "DescribeSubscriptionResponseResponseTypeDef",
    {
        "Subscription": "SubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateDRTLogBucketRequestTypeDef = TypedDict(
    "DisassociateDRTLogBucketRequestTypeDef",
    {
        "LogBucket": str,
    },
)

DisassociateHealthCheckRequestTypeDef = TypedDict(
    "DisassociateHealthCheckRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)

_RequiredEmergencyContactTypeDef = TypedDict(
    "_RequiredEmergencyContactTypeDef",
    {
        "EmailAddress": str,
    },
)
_OptionalEmergencyContactTypeDef = TypedDict(
    "_OptionalEmergencyContactTypeDef",
    {
        "PhoneNumber": str,
        "ContactNotes": str,
    },
    total=False,
)


class EmergencyContactTypeDef(_RequiredEmergencyContactTypeDef, _OptionalEmergencyContactTypeDef):
    pass


GetSubscriptionStateResponseResponseTypeDef = TypedDict(
    "GetSubscriptionStateResponseResponseTypeDef",
    {
        "SubscriptionState": SubscriptionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Type": str,
        "Max": int,
    },
    total=False,
)

ListAttacksRequestTypeDef = TypedDict(
    "ListAttacksRequestTypeDef",
    {
        "ResourceArns": List[str],
        "StartTime": "TimeRangeTypeDef",
        "EndTime": "TimeRangeTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAttacksResponseResponseTypeDef = TypedDict(
    "ListAttacksResponseResponseTypeDef",
    {
        "AttackSummaries": List["AttackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectionGroupsRequestTypeDef = TypedDict(
    "ListProtectionGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectionGroupsResponseResponseTypeDef = TypedDict(
    "ListProtectionGroupsResponseResponseTypeDef",
    {
        "ProtectionGroups": List["ProtectionGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectionsRequestTypeDef = TypedDict(
    "ListProtectionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectionsResponseResponseTypeDef = TypedDict(
    "ListProtectionsResponseResponseTypeDef",
    {
        "Protections": List["ProtectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesInProtectionGroupRequestTypeDef = TypedDict(
    "_RequiredListResourcesInProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)
_OptionalListResourcesInProtectionGroupRequestTypeDef = TypedDict(
    "_OptionalListResourcesInProtectionGroupRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListResourcesInProtectionGroupRequestTypeDef(
    _RequiredListResourcesInProtectionGroupRequestTypeDef,
    _OptionalListResourcesInProtectionGroupRequestTypeDef,
):
    pass


ListResourcesInProtectionGroupResponseResponseTypeDef = TypedDict(
    "ListResourcesInProtectionGroupResponseResponseTypeDef",
    {
        "ResourceArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MitigationTypeDef = TypedDict(
    "MitigationTypeDef",
    {
        "MitigationName": str,
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

ProtectionGroupArbitraryPatternLimitsTypeDef = TypedDict(
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    {
        "MaxMembers": int,
    },
)

ProtectionGroupLimitsTypeDef = TypedDict(
    "ProtectionGroupLimitsTypeDef",
    {
        "MaxProtectionGroups": int,
        "PatternTypeLimits": "ProtectionGroupPatternTypeLimitsTypeDef",
    },
)

ProtectionGroupPatternTypeLimitsTypeDef = TypedDict(
    "ProtectionGroupPatternTypeLimitsTypeDef",
    {
        "ArbitraryPatternLimits": "ProtectionGroupArbitraryPatternLimitsTypeDef",
    },
)

_RequiredProtectionGroupTypeDef = TypedDict(
    "_RequiredProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "Members": List[str],
    },
)
_OptionalProtectionGroupTypeDef = TypedDict(
    "_OptionalProtectionGroupTypeDef",
    {
        "ResourceType": ProtectedResourceTypeType,
        "ProtectionGroupArn": str,
    },
    total=False,
)


class ProtectionGroupTypeDef(_RequiredProtectionGroupTypeDef, _OptionalProtectionGroupTypeDef):
    pass


ProtectionLimitsTypeDef = TypedDict(
    "ProtectionLimitsTypeDef",
    {
        "ProtectedResourceTypeLimits": List["LimitTypeDef"],
    },
)

ProtectionTypeDef = TypedDict(
    "ProtectionTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceArn": str,
        "HealthCheckIds": List[str],
        "ProtectionArn": str,
    },
    total=False,
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

SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": SubResourceTypeType,
        "Id": str,
        "AttackVectors": List["SummarizedAttackVectorTypeDef"],
        "Counters": List["SummarizedCounterTypeDef"],
    },
    total=False,
)

SubscriptionLimitsTypeDef = TypedDict(
    "SubscriptionLimitsTypeDef",
    {
        "ProtectionLimits": "ProtectionLimitsTypeDef",
        "ProtectionGroupLimits": "ProtectionGroupLimitsTypeDef",
    },
)

_RequiredSubscriptionTypeDef = TypedDict(
    "_RequiredSubscriptionTypeDef",
    {
        "SubscriptionLimits": "SubscriptionLimitsTypeDef",
    },
)
_OptionalSubscriptionTypeDef = TypedDict(
    "_OptionalSubscriptionTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "TimeCommitmentInSeconds": int,
        "AutoRenew": AutoRenewType,
        "Limits": List["LimitTypeDef"],
        "ProactiveEngagementStatus": ProactiveEngagementStatusType,
        "SubscriptionArn": str,
    },
    total=False,
)


class SubscriptionTypeDef(_RequiredSubscriptionTypeDef, _OptionalSubscriptionTypeDef):
    pass


_RequiredSummarizedAttackVectorTypeDef = TypedDict(
    "_RequiredSummarizedAttackVectorTypeDef",
    {
        "VectorType": str,
    },
)
_OptionalSummarizedAttackVectorTypeDef = TypedDict(
    "_OptionalSummarizedAttackVectorTypeDef",
    {
        "VectorCounters": List["SummarizedCounterTypeDef"],
    },
    total=False,
)


class SummarizedAttackVectorTypeDef(
    _RequiredSummarizedAttackVectorTypeDef, _OptionalSummarizedAttackVectorTypeDef
):
    pass


SummarizedCounterTypeDef = TypedDict(
    "SummarizedCounterTypeDef",
    {
        "Name": str,
        "Max": float,
        "Average": float,
        "Sum": float,
        "N": int,
        "Unit": str,
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
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "FromInclusive": datetime,
        "ToExclusive": datetime,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateEmergencyContactSettingsRequestTypeDef = TypedDict(
    "UpdateEmergencyContactSettingsRequestTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
    },
    total=False,
)

_RequiredUpdateProtectionGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
    },
)
_OptionalUpdateProtectionGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateProtectionGroupRequestTypeDef",
    {
        "ResourceType": ProtectedResourceTypeType,
        "Members": List[str],
    },
    total=False,
)


class UpdateProtectionGroupRequestTypeDef(
    _RequiredUpdateProtectionGroupRequestTypeDef, _OptionalUpdateProtectionGroupRequestTypeDef
):
    pass


UpdateSubscriptionRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestTypeDef",
    {
        "AutoRenew": AutoRenewType,
    },
    total=False,
)
