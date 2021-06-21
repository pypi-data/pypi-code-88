"""
Type annotations for applicationcostprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_applicationcostprofiler.type_defs import DeleteReportDefinitionResultTypeDef

    data: DeleteReportDefinitionResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import FormatType, ReportFrequencyType, S3BucketRegionType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteReportDefinitionResultTypeDef",
    "GetReportDefinitionResultTypeDef",
    "ImportApplicationUsageResultTypeDef",
    "ListReportDefinitionsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutReportDefinitionResultTypeDef",
    "ReportDefinitionTypeDef",
    "S3LocationTypeDef",
    "SourceS3LocationTypeDef",
    "UpdateReportDefinitionResultTypeDef",
)

DeleteReportDefinitionResultTypeDef = TypedDict(
    "DeleteReportDefinitionResultTypeDef",
    {
        "reportId": str,
    },
    total=False,
)

GetReportDefinitionResultTypeDef = TypedDict(
    "GetReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": "S3LocationTypeDef",
        "createdAt": datetime,
        "lastUpdated": datetime,
    },
)

ImportApplicationUsageResultTypeDef = TypedDict(
    "ImportApplicationUsageResultTypeDef",
    {
        "importId": str,
    },
)

ListReportDefinitionsResultTypeDef = TypedDict(
    "ListReportDefinitionsResultTypeDef",
    {
        "reportDefinitions": List["ReportDefinitionTypeDef"],
        "nextToken": str,
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

PutReportDefinitionResultTypeDef = TypedDict(
    "PutReportDefinitionResultTypeDef",
    {
        "reportId": str,
    },
    total=False,
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


UpdateReportDefinitionResultTypeDef = TypedDict(
    "UpdateReportDefinitionResultTypeDef",
    {
        "reportId": str,
    },
    total=False,
)
