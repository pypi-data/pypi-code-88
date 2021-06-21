"""
Type annotations for importexport service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/type_defs.html)

Usage::

    ```python
    from mypy_boto3_importexport.type_defs import ArtifactTypeDef

    data: ArtifactTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import JobTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArtifactTypeDef",
    "CancelJobOutputTypeDef",
    "CreateJobOutputTypeDef",
    "GetShippingLabelOutputTypeDef",
    "GetStatusOutputTypeDef",
    "JobTypeDef",
    "ListJobsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateJobOutputTypeDef",
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "Description": str,
        "URL": str,
    },
    total=False,
)

CancelJobOutputTypeDef = TypedDict(
    "CancelJobOutputTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetShippingLabelOutputTypeDef = TypedDict(
    "GetShippingLabelOutputTypeDef",
    {
        "ShippingLabelURL": str,
        "Warning": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStatusOutputTypeDef = TypedDict(
    "GetStatusOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": JobTypeType,
    },
    total=False,
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "IsTruncated": bool,
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

UpdateJobOutputTypeDef = TypedDict(
    "UpdateJobOutputTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
