"""
Type annotations for cloudtrail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import AddTagsRequestTypeDef

    data: AddTagsRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import LookupAttributeKeyType, ReadWriteTypeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsRequestTypeDef",
    "AdvancedEventSelectorTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CreateTrailRequestTypeDef",
    "CreateTrailResponseResponseTypeDef",
    "DataResourceTypeDef",
    "DeleteTrailRequestTypeDef",
    "DescribeTrailsRequestTypeDef",
    "DescribeTrailsResponseResponseTypeDef",
    "EventSelectorTypeDef",
    "EventTypeDef",
    "GetEventSelectorsRequestTypeDef",
    "GetEventSelectorsResponseResponseTypeDef",
    "GetInsightSelectorsRequestTypeDef",
    "GetInsightSelectorsResponseResponseTypeDef",
    "GetTrailRequestTypeDef",
    "GetTrailResponseResponseTypeDef",
    "GetTrailStatusRequestTypeDef",
    "GetTrailStatusResponseResponseTypeDef",
    "InsightSelectorTypeDef",
    "ListPublicKeysRequestTypeDef",
    "ListPublicKeysResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "ListTrailsRequestTypeDef",
    "ListTrailsResponseResponseTypeDef",
    "LookupAttributeTypeDef",
    "LookupEventsRequestTypeDef",
    "LookupEventsResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublicKeyTypeDef",
    "PutEventSelectorsRequestTypeDef",
    "PutEventSelectorsResponseResponseTypeDef",
    "PutInsightSelectorsRequestTypeDef",
    "PutInsightSelectorsResponseResponseTypeDef",
    "RemoveTagsRequestTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "StartLoggingRequestTypeDef",
    "StopLoggingRequestTypeDef",
    "TagTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
    "UpdateTrailRequestTypeDef",
    "UpdateTrailResponseResponseTypeDef",
)

_RequiredAddTagsRequestTypeDef = TypedDict(
    "_RequiredAddTagsRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalAddTagsRequestTypeDef = TypedDict(
    "_OptionalAddTagsRequestTypeDef",
    {
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)


class AddTagsRequestTypeDef(_RequiredAddTagsRequestTypeDef, _OptionalAddTagsRequestTypeDef):
    pass


_RequiredAdvancedEventSelectorTypeDef = TypedDict(
    "_RequiredAdvancedEventSelectorTypeDef",
    {
        "FieldSelectors": List["AdvancedFieldSelectorTypeDef"],
    },
)
_OptionalAdvancedEventSelectorTypeDef = TypedDict(
    "_OptionalAdvancedEventSelectorTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class AdvancedEventSelectorTypeDef(
    _RequiredAdvancedEventSelectorTypeDef, _OptionalAdvancedEventSelectorTypeDef
):
    pass


_RequiredAdvancedFieldSelectorTypeDef = TypedDict(
    "_RequiredAdvancedFieldSelectorTypeDef",
    {
        "Field": str,
    },
)
_OptionalAdvancedFieldSelectorTypeDef = TypedDict(
    "_OptionalAdvancedFieldSelectorTypeDef",
    {
        "Equals": List[str],
        "StartsWith": List[str],
        "EndsWith": List[str],
        "NotEquals": List[str],
        "NotStartsWith": List[str],
        "NotEndsWith": List[str],
    },
    total=False,
)


class AdvancedFieldSelectorTypeDef(
    _RequiredAdvancedFieldSelectorTypeDef, _OptionalAdvancedFieldSelectorTypeDef
):
    pass


_RequiredCreateTrailRequestTypeDef = TypedDict(
    "_RequiredCreateTrailRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
    },
)
_OptionalCreateTrailRequestTypeDef = TypedDict(
    "_OptionalCreateTrailRequestTypeDef",
    {
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "EnableLogFileValidation": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)


class CreateTrailRequestTypeDef(
    _RequiredCreateTrailRequestTypeDef, _OptionalCreateTrailRequestTypeDef
):
    pass


CreateTrailResponseResponseTypeDef = TypedDict(
    "CreateTrailResponseResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef",
    {
        "Type": str,
        "Values": List[str],
    },
    total=False,
)

DeleteTrailRequestTypeDef = TypedDict(
    "DeleteTrailRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeTrailsRequestTypeDef = TypedDict(
    "DescribeTrailsRequestTypeDef",
    {
        "trailNameList": List[str],
        "includeShadowTrails": bool,
    },
    total=False,
)

DescribeTrailsResponseResponseTypeDef = TypedDict(
    "DescribeTrailsResponseResponseTypeDef",
    {
        "trailList": List["TrailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventSelectorTypeDef = TypedDict(
    "EventSelectorTypeDef",
    {
        "ReadWriteType": ReadWriteTypeType,
        "IncludeManagementEvents": bool,
        "DataResources": List["DataResourceTypeDef"],
        "ExcludeManagementEventSources": List[str],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "EventName": str,
        "ReadOnly": str,
        "AccessKeyId": str,
        "EventTime": datetime,
        "EventSource": str,
        "Username": str,
        "Resources": List["ResourceTypeDef"],
        "CloudTrailEvent": str,
    },
    total=False,
)

GetEventSelectorsRequestTypeDef = TypedDict(
    "GetEventSelectorsRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetEventSelectorsResponseResponseTypeDef = TypedDict(
    "GetEventSelectorsResponseResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightSelectorsRequestTypeDef = TypedDict(
    "GetInsightSelectorsRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetInsightSelectorsResponseResponseTypeDef = TypedDict(
    "GetInsightSelectorsResponseResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailRequestTypeDef = TypedDict(
    "GetTrailRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailResponseResponseTypeDef = TypedDict(
    "GetTrailResponseResponseTypeDef",
    {
        "Trail": "TrailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailStatusRequestTypeDef = TypedDict(
    "GetTrailStatusRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailStatusResponseResponseTypeDef = TypedDict(
    "GetTrailStatusResponseResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightSelectorTypeDef = TypedDict(
    "InsightSelectorTypeDef",
    {
        "InsightType": Literal["ApiCallRateInsight"],
    },
    total=False,
)

ListPublicKeysRequestTypeDef = TypedDict(
    "ListPublicKeysRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": str,
    },
    total=False,
)

ListPublicKeysResponseResponseTypeDef = TypedDict(
    "ListPublicKeysResponseResponseTypeDef",
    {
        "PublicKeyList": List["PublicKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestTypeDef",
    {
        "ResourceIdList": List[str],
    },
)
_OptionalListTagsRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsRequestTypeDef(_RequiredListTagsRequestTypeDef, _OptionalListTagsRequestTypeDef):
    pass


ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "ResourceTagList": List["ResourceTagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrailsRequestTypeDef = TypedDict(
    "ListTrailsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListTrailsResponseResponseTypeDef = TypedDict(
    "ListTrailsResponseResponseTypeDef",
    {
        "Trails": List["TrailInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LookupAttributeTypeDef = TypedDict(
    "LookupAttributeTypeDef",
    {
        "AttributeKey": LookupAttributeKeyType,
        "AttributeValue": str,
    },
)

LookupEventsRequestTypeDef = TypedDict(
    "LookupEventsRequestTypeDef",
    {
        "LookupAttributes": List["LookupAttributeTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventCategory": Literal["insight"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

LookupEventsResponseResponseTypeDef = TypedDict(
    "LookupEventsResponseResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
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

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Value": bytes,
        "ValidityStartTime": datetime,
        "ValidityEndTime": datetime,
        "Fingerprint": str,
    },
    total=False,
)

_RequiredPutEventSelectorsRequestTypeDef = TypedDict(
    "_RequiredPutEventSelectorsRequestTypeDef",
    {
        "TrailName": str,
    },
)
_OptionalPutEventSelectorsRequestTypeDef = TypedDict(
    "_OptionalPutEventSelectorsRequestTypeDef",
    {
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
    },
    total=False,
)


class PutEventSelectorsRequestTypeDef(
    _RequiredPutEventSelectorsRequestTypeDef, _OptionalPutEventSelectorsRequestTypeDef
):
    pass


PutEventSelectorsResponseResponseTypeDef = TypedDict(
    "PutEventSelectorsResponseResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInsightSelectorsRequestTypeDef = TypedDict(
    "PutInsightSelectorsRequestTypeDef",
    {
        "TrailName": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
    },
)

PutInsightSelectorsResponseResponseTypeDef = TypedDict(
    "PutInsightSelectorsResponseResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveTagsRequestTypeDef = TypedDict(
    "_RequiredRemoveTagsRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalRemoveTagsRequestTypeDef = TypedDict(
    "_OptionalRemoveTagsRequestTypeDef",
    {
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)


class RemoveTagsRequestTypeDef(
    _RequiredRemoveTagsRequestTypeDef, _OptionalRemoveTagsRequestTypeDef
):
    pass


ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceId": str,
        "TagsList": List["TagTypeDef"],
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ResourceType": str,
        "ResourceName": str,
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

StartLoggingRequestTypeDef = TypedDict(
    "StartLoggingRequestTypeDef",
    {
        "Name": str,
    },
)

StopLoggingRequestTypeDef = TypedDict(
    "StopLoggingRequestTypeDef",
    {
        "Name": str,
    },
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


TrailInfoTypeDef = TypedDict(
    "TrailInfoTypeDef",
    {
        "TrailARN": str,
        "Name": str,
        "HomeRegion": str,
    },
    total=False,
)

TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "HomeRegion": str,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "HasCustomEventSelectors": bool,
        "HasInsightSelectors": bool,
        "IsOrganizationTrail": bool,
    },
    total=False,
)

_RequiredUpdateTrailRequestTypeDef = TypedDict(
    "_RequiredUpdateTrailRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateTrailRequestTypeDef = TypedDict(
    "_OptionalUpdateTrailRequestTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "EnableLogFileValidation": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
    },
    total=False,
)


class UpdateTrailRequestTypeDef(
    _RequiredUpdateTrailRequestTypeDef, _OptionalUpdateTrailRequestTypeDef
):
    pass


UpdateTrailResponseResponseTypeDef = TypedDict(
    "UpdateTrailResponseResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
