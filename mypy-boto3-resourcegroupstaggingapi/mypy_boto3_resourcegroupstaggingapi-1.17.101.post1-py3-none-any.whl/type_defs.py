"""
Type annotations for resourcegroupstaggingapi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef

    data: ComplianceDetailsTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ErrorCodeType, GroupByAttributeType, TargetIdTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ComplianceDetailsTypeDef",
    "DescribeReportCreationOutputResponseTypeDef",
    "FailureInfoTypeDef",
    "GetComplianceSummaryInputTypeDef",
    "GetComplianceSummaryOutputResponseTypeDef",
    "GetResourcesInputTypeDef",
    "GetResourcesOutputResponseTypeDef",
    "GetTagKeysInputTypeDef",
    "GetTagKeysOutputResponseTypeDef",
    "GetTagValuesInputTypeDef",
    "GetTagValuesOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagMappingTypeDef",
    "ResponseMetadataTypeDef",
    "StartReportCreationInputTypeDef",
    "SummaryTypeDef",
    "TagFilterTypeDef",
    "TagResourcesInputTypeDef",
    "TagResourcesOutputResponseTypeDef",
    "TagTypeDef",
    "UntagResourcesInputTypeDef",
    "UntagResourcesOutputResponseTypeDef",
)

ComplianceDetailsTypeDef = TypedDict(
    "ComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)

DescribeReportCreationOutputResponseTypeDef = TypedDict(
    "DescribeReportCreationOutputResponseTypeDef",
    {
        "Status": str,
        "S3Location": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

GetComplianceSummaryInputTypeDef = TypedDict(
    "GetComplianceSummaryInputTypeDef",
    {
        "TargetIdFilters": List[str],
        "RegionFilters": List[str],
        "ResourceTypeFilters": List[str],
        "TagKeyFilters": List[str],
        "GroupBy": List[GroupByAttributeType],
        "MaxResults": int,
        "PaginationToken": str,
    },
    total=False,
)

GetComplianceSummaryOutputResponseTypeDef = TypedDict(
    "GetComplianceSummaryOutputResponseTypeDef",
    {
        "SummaryList": List["SummaryTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcesInputTypeDef = TypedDict(
    "GetResourcesInputTypeDef",
    {
        "PaginationToken": str,
        "TagFilters": List["TagFilterTypeDef"],
        "ResourcesPerPage": int,
        "TagsPerPage": int,
        "ResourceTypeFilters": List[str],
        "IncludeComplianceDetails": bool,
        "ExcludeCompliantResources": bool,
        "ResourceARNList": List[str],
    },
    total=False,
)

GetResourcesOutputResponseTypeDef = TypedDict(
    "GetResourcesOutputResponseTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List["ResourceTagMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagKeysInputTypeDef = TypedDict(
    "GetTagKeysInputTypeDef",
    {
        "PaginationToken": str,
    },
    total=False,
)

GetTagKeysOutputResponseTypeDef = TypedDict(
    "GetTagKeysOutputResponseTypeDef",
    {
        "PaginationToken": str,
        "TagKeys": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTagValuesInputTypeDef = TypedDict(
    "_RequiredGetTagValuesInputTypeDef",
    {
        "Key": str,
    },
)
_OptionalGetTagValuesInputTypeDef = TypedDict(
    "_OptionalGetTagValuesInputTypeDef",
    {
        "PaginationToken": str,
    },
    total=False,
)


class GetTagValuesInputTypeDef(
    _RequiredGetTagValuesInputTypeDef, _OptionalGetTagValuesInputTypeDef
):
    pass


GetTagValuesOutputResponseTypeDef = TypedDict(
    "GetTagValuesOutputResponseTypeDef",
    {
        "PaginationToken": str,
        "TagValues": List[str],
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

ResourceTagMappingTypeDef = TypedDict(
    "ResourceTagMappingTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "ComplianceDetails": "ComplianceDetailsTypeDef",
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

StartReportCreationInputTypeDef = TypedDict(
    "StartReportCreationInputTypeDef",
    {
        "S3Bucket": str,
    },
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "LastUpdated": str,
        "TargetId": str,
        "TargetIdType": TargetIdTypeType,
        "Region": str,
        "ResourceType": str,
        "NonCompliantResources": int,
    },
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

TagResourcesInputTypeDef = TypedDict(
    "TagResourcesInputTypeDef",
    {
        "ResourceARNList": List[str],
        "Tags": Dict[str, str],
    },
)

TagResourcesOutputResponseTypeDef = TypedDict(
    "TagResourcesOutputResponseTypeDef",
    {
        "FailedResourcesMap": Dict[str, "FailureInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourcesInputTypeDef = TypedDict(
    "UntagResourcesInputTypeDef",
    {
        "ResourceARNList": List[str],
        "TagKeys": List[str],
    },
)

UntagResourcesOutputResponseTypeDef = TypedDict(
    "UntagResourcesOutputResponseTypeDef",
    {
        "FailedResourcesMap": Dict[str, "FailureInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
