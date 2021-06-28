"""
Type annotations for applicationcostprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_applicationcostprofiler.type_defs import DeleteReportDefinitionRequestTypeDef

    data: DeleteReportDefinitionRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import FormatType, ReportFrequencyType, S3BucketRegionType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteReportDefinitionRequestTypeDef",
    "DeleteReportDefinitionResultResponseTypeDef",
    "GetReportDefinitionRequestTypeDef",
    "GetReportDefinitionResultResponseTypeDef",
    "ImportApplicationUsageRequestTypeDef",
    "ImportApplicationUsageResultResponseTypeDef",
    "ListReportDefinitionsRequestTypeDef",
    "ListReportDefinitionsResultResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutReportDefinitionRequestTypeDef",
    "PutReportDefinitionResultResponseTypeDef",
    "ReportDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SourceS3LocationTypeDef",
    "UpdateReportDefinitionRequestTypeDef",
    "UpdateReportDefinitionResultResponseTypeDef",
)

DeleteReportDefinitionRequestTypeDef = TypedDict(
    "DeleteReportDefinitionRequestTypeDef",
    {
        "reportId": str,
    },
)

DeleteReportDefinitionResultResponseTypeDef = TypedDict(
    "DeleteReportDefinitionResultResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReportDefinitionRequestTypeDef = TypedDict(
    "GetReportDefinitionRequestTypeDef",
    {
        "reportId": str,
    },
)

GetReportDefinitionResultResponseTypeDef = TypedDict(
    "GetReportDefinitionResultResponseTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
        "createdAt": datetime,
        "lastUpdated": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportApplicationUsageRequestTypeDef = TypedDict(
    "ImportApplicationUsageRequestTypeDef",
    {
        "sourceS3Location": "SourceS3LocationTypeDef",
    },
)

ImportApplicationUsageResultResponseTypeDef = TypedDict(
    "ImportApplicationUsageResultResponseTypeDef",
    {
        "importId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportDefinitionsRequestTypeDef = TypedDict(
    "ListReportDefinitionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListReportDefinitionsResultResponseTypeDef = TypedDict(
    "ListReportDefinitionsResultResponseTypeDef",
    {
        "reportDefinitions": List["ReportDefinitionTypeDef"],
        "nextToken": str,
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

PutReportDefinitionRequestTypeDef = TypedDict(
    "PutReportDefinitionRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
    },
)

PutReportDefinitionResultResponseTypeDef = TypedDict(
    "PutReportDefinitionResultResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportDefinitionTypeDef = TypedDict(
    "ReportDefinitionTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
)

_RequiredSourceS3LocationTypeDef = TypedDict(
    "_RequiredSourceS3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
_OptionalSourceS3LocationTypeDef = TypedDict(
    "_OptionalSourceS3LocationTypeDef",
    {
        "region": S3BucketRegionType,
    },
    total=False,
)


class SourceS3LocationTypeDef(_RequiredSourceS3LocationTypeDef, _OptionalSourceS3LocationTypeDef):
    pass


UpdateReportDefinitionRequestTypeDef = TypedDict(
    "UpdateReportDefinitionRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
    },
)

UpdateReportDefinitionResultResponseTypeDef = TypedDict(
    "UpdateReportDefinitionResultResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
