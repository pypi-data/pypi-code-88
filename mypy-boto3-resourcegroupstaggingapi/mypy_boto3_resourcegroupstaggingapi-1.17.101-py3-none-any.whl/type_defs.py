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

from .literals import ErrorCodeType, TargetIdTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ComplianceDetailsTypeDef",
    "DescribeReportCreationOutputTypeDef",
    "FailureInfoTypeDef",
    "GetComplianceSummaryOutputTypeDef",
    "GetResourcesOutputTypeDef",
    "GetTagKeysOutputTypeDef",
    "GetTagValuesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagMappingTypeDef",
    "ResponseMetadataTypeDef",
    "SummaryTypeDef",
    "TagFilterTypeDef",
    "TagResourcesOutputTypeDef",
    "TagTypeDef",
    "UntagResourcesOutputTypeDef",
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

DescribeReportCreationOutputTypeDef = TypedDict(
    "DescribeReportCreationOutputTypeDef",
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

GetComplianceSummaryOutputTypeDef = TypedDict(
    "GetComplianceSummaryOutputTypeDef",
    {
        "SummaryList": List["SummaryTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcesOutputTypeDef = TypedDict(
    "GetResourcesOutputTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List["ResourceTagMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagKeysOutputTypeDef = TypedDict(
    "GetTagKeysOutputTypeDef",
    {
        "PaginationToken": str,
        "TagKeys": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagValuesOutputTypeDef = TypedDict(
    "GetTagValuesOutputTypeDef",
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

TagResourcesOutputTypeDef = TypedDict(
    "TagResourcesOutputTypeDef",
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

UntagResourcesOutputTypeDef = TypedDict(
    "UntagResourcesOutputTypeDef",
    {
        "FailedResourcesMap": Dict[str, "FailureInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
