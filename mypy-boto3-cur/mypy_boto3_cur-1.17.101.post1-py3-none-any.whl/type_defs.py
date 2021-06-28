"""
Type annotations for cur service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cur.type_defs import DeleteReportDefinitionRequestTypeDef

    data: DeleteReportDefinitionRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AdditionalArtifactType,
    AWSRegionType,
    CompressionFormatType,
    ReportFormatType,
    ReportVersioningType,
    TimeUnitType,
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
    "DeleteReportDefinitionRequestTypeDef",
    "DeleteReportDefinitionResponseResponseTypeDef",
    "DescribeReportDefinitionsRequestTypeDef",
    "DescribeReportDefinitionsResponseResponseTypeDef",
    "ModifyReportDefinitionRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutReportDefinitionRequestTypeDef",
    "ReportDefinitionTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteReportDefinitionRequestTypeDef = TypedDict(
    "DeleteReportDefinitionRequestTypeDef",
    {
        "ReportName": str,
    },
    total=False,
)

DeleteReportDefinitionResponseResponseTypeDef = TypedDict(
    "DeleteReportDefinitionResponseResponseTypeDef",
    {
        "ResponseMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReportDefinitionsRequestTypeDef = TypedDict(
    "DescribeReportDefinitionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReportDefinitionsResponseResponseTypeDef = TypedDict(
    "DescribeReportDefinitionsResponseResponseTypeDef",
    {
        "ReportDefinitions": List["ReportDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyReportDefinitionRequestTypeDef = TypedDict(
    "ModifyReportDefinitionRequestTypeDef",
    {
        "ReportName": str,
        "ReportDefinition": "ReportDefinitionTypeDef",
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
        "ReportDefinition": "ReportDefinitionTypeDef",
    },
)

_RequiredReportDefinitionTypeDef = TypedDict(
    "_RequiredReportDefinitionTypeDef",
    {
        "ReportName": str,
        "TimeUnit": TimeUnitType,
        "Format": ReportFormatType,
        "Compression": CompressionFormatType,
        "AdditionalSchemaElements": List[Literal["RESOURCES"]],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": AWSRegionType,
    },
)
_OptionalReportDefinitionTypeDef = TypedDict(
    "_OptionalReportDefinitionTypeDef",
    {
        "AdditionalArtifacts": List[AdditionalArtifactType],
        "RefreshClosedReports": bool,
        "ReportVersioning": ReportVersioningType,
        "BillingViewArn": str,
    },
    total=False,
)


class ReportDefinitionTypeDef(_RequiredReportDefinitionTypeDef, _OptionalReportDefinitionTypeDef):
    pass


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
