"""
Type annotations for dlm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dlm.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    GettablePolicyStateValuesType,
    LocationValuesType,
    PolicyTypeValuesType,
    ResourceLocationValuesType,
    ResourceTypeValuesType,
    RetentionIntervalUnitValuesType,
    SettablePolicyStateValuesType,
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
    "ActionTypeDef",
    "CreateLifecyclePolicyRequestTypeDef",
    "CreateLifecyclePolicyResponseResponseTypeDef",
    "CreateRuleTypeDef",
    "CrossRegionCopyActionTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "DeleteLifecyclePolicyRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "EventParametersTypeDef",
    "EventSourceTypeDef",
    "FastRestoreRuleTypeDef",
    "GetLifecyclePoliciesRequestTypeDef",
    "GetLifecyclePoliciesResponseResponseTypeDef",
    "GetLifecyclePolicyRequestTypeDef",
    "GetLifecyclePolicyResponseResponseTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ParametersTypeDef",
    "PolicyDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "RetainRuleTypeDef",
    "ScheduleTypeDef",
    "ShareRuleTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLifecyclePolicyRequestTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Name": str,
        "CrossRegionCopy": List["CrossRegionCopyActionTypeDef"],
    },
)

_RequiredCreateLifecyclePolicyRequestTypeDef = TypedDict(
    "_RequiredCreateLifecyclePolicyRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "Description": str,
        "State": SettablePolicyStateValuesType,
        "PolicyDetails": "PolicyDetailsTypeDef",
    },
)
_OptionalCreateLifecyclePolicyRequestTypeDef = TypedDict(
    "_OptionalCreateLifecyclePolicyRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateLifecyclePolicyRequestTypeDef(
    _RequiredCreateLifecyclePolicyRequestTypeDef, _OptionalCreateLifecyclePolicyRequestTypeDef
):
    pass


CreateLifecyclePolicyResponseResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseResponseTypeDef",
    {
        "PolicyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRuleTypeDef = TypedDict(
    "CreateRuleTypeDef",
    {
        "Location": LocationValuesType,
        "Interval": int,
        "IntervalUnit": Literal["HOURS"],
        "Times": List[str],
        "CronExpression": str,
    },
    total=False,
)

_RequiredCrossRegionCopyActionTypeDef = TypedDict(
    "_RequiredCrossRegionCopyActionTypeDef",
    {
        "Target": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
)
_OptionalCrossRegionCopyActionTypeDef = TypedDict(
    "_OptionalCrossRegionCopyActionTypeDef",
    {
        "RetainRule": "CrossRegionCopyRetainRuleTypeDef",
    },
    total=False,
)


class CrossRegionCopyActionTypeDef(
    _RequiredCrossRegionCopyActionTypeDef, _OptionalCrossRegionCopyActionTypeDef
):
    pass


CrossRegionCopyRetainRuleTypeDef = TypedDict(
    "CrossRegionCopyRetainRuleTypeDef",
    {
        "Interval": int,
        "IntervalUnit": RetentionIntervalUnitValuesType,
    },
    total=False,
)

_RequiredCrossRegionCopyRuleTypeDef = TypedDict(
    "_RequiredCrossRegionCopyRuleTypeDef",
    {
        "Encrypted": bool,
    },
)
_OptionalCrossRegionCopyRuleTypeDef = TypedDict(
    "_OptionalCrossRegionCopyRuleTypeDef",
    {
        "TargetRegion": str,
        "Target": str,
        "CmkArn": str,
        "CopyTags": bool,
        "RetainRule": "CrossRegionCopyRetainRuleTypeDef",
    },
    total=False,
)


class CrossRegionCopyRuleTypeDef(
    _RequiredCrossRegionCopyRuleTypeDef, _OptionalCrossRegionCopyRuleTypeDef
):
    pass


DeleteLifecyclePolicyRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "Encrypted": bool,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "CmkArn": str,
    },
    total=False,
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


EventParametersTypeDef = TypedDict(
    "EventParametersTypeDef",
    {
        "EventType": Literal["shareSnapshot"],
        "SnapshotOwner": List[str],
        "DescriptionRegex": str,
    },
)

_RequiredEventSourceTypeDef = TypedDict(
    "_RequiredEventSourceTypeDef",
    {
        "Type": Literal["MANAGED_CWE"],
    },
)
_OptionalEventSourceTypeDef = TypedDict(
    "_OptionalEventSourceTypeDef",
    {
        "Parameters": "EventParametersTypeDef",
    },
    total=False,
)


class EventSourceTypeDef(_RequiredEventSourceTypeDef, _OptionalEventSourceTypeDef):
    pass


_RequiredFastRestoreRuleTypeDef = TypedDict(
    "_RequiredFastRestoreRuleTypeDef",
    {
        "AvailabilityZones": List[str],
    },
)
_OptionalFastRestoreRuleTypeDef = TypedDict(
    "_OptionalFastRestoreRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": RetentionIntervalUnitValuesType,
    },
    total=False,
)


class FastRestoreRuleTypeDef(_RequiredFastRestoreRuleTypeDef, _OptionalFastRestoreRuleTypeDef):
    pass


GetLifecyclePoliciesRequestTypeDef = TypedDict(
    "GetLifecyclePoliciesRequestTypeDef",
    {
        "PolicyIds": List[str],
        "State": GettablePolicyStateValuesType,
        "ResourceTypes": List[ResourceTypeValuesType],
        "TargetTags": List[str],
        "TagsToAdd": List[str],
    },
    total=False,
)

GetLifecyclePoliciesResponseResponseTypeDef = TypedDict(
    "GetLifecyclePoliciesResponseResponseTypeDef",
    {
        "Policies": List["LifecyclePolicySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)

GetLifecyclePolicyResponseResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseResponseTypeDef",
    {
        "Policy": "LifecyclePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": GettablePolicyStateValuesType,
        "Tags": Dict[str, str],
        "PolicyType": PolicyTypeValuesType,
    },
    total=False,
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": GettablePolicyStateValuesType,
        "StatusMessage": str,
        "ExecutionRoleArn": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "PolicyDetails": "PolicyDetailsTypeDef",
        "Tags": Dict[str, str],
        "PolicyArn": str,
    },
    total=False,
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "ExcludeBootVolume": bool,
        "NoReboot": bool,
    },
    total=False,
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "PolicyType": PolicyTypeValuesType,
        "ResourceTypes": List[ResourceTypeValuesType],
        "ResourceLocations": List[ResourceLocationValuesType],
        "TargetTags": List["TagTypeDef"],
        "Schedules": List["ScheduleTypeDef"],
        "Parameters": "ParametersTypeDef",
        "EventSource": "EventSourceTypeDef",
        "Actions": List["ActionTypeDef"],
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

RetainRuleTypeDef = TypedDict(
    "RetainRuleTypeDef",
    {
        "Count": int,
        "Interval": int,
        "IntervalUnit": RetentionIntervalUnitValuesType,
    },
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List["TagTypeDef"],
        "VariableTags": List["TagTypeDef"],
        "CreateRule": "CreateRuleTypeDef",
        "RetainRule": "RetainRuleTypeDef",
        "FastRestoreRule": "FastRestoreRuleTypeDef",
        "CrossRegionCopyRules": List["CrossRegionCopyRuleTypeDef"],
        "ShareRules": List["ShareRuleTypeDef"],
    },
    total=False,
)

_RequiredShareRuleTypeDef = TypedDict(
    "_RequiredShareRuleTypeDef",
    {
        "TargetAccounts": List[str],
    },
)
_OptionalShareRuleTypeDef = TypedDict(
    "_OptionalShareRuleTypeDef",
    {
        "UnshareInterval": int,
        "UnshareIntervalUnit": RetentionIntervalUnitValuesType,
    },
    total=False,
)


class ShareRuleTypeDef(_RequiredShareRuleTypeDef, _OptionalShareRuleTypeDef):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateLifecyclePolicyRequestTypeDef = TypedDict(
    "_RequiredUpdateLifecyclePolicyRequestTypeDef",
    {
        "PolicyId": str,
    },
)
_OptionalUpdateLifecyclePolicyRequestTypeDef = TypedDict(
    "_OptionalUpdateLifecyclePolicyRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "State": SettablePolicyStateValuesType,
        "Description": str,
        "PolicyDetails": "PolicyDetailsTypeDef",
    },
    total=False,
)


class UpdateLifecyclePolicyRequestTypeDef(
    _RequiredUpdateLifecyclePolicyRequestTypeDef, _OptionalUpdateLifecyclePolicyRequestTypeDef
):
    pass
