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
    "CancelJobInputTypeDef",
    "CancelJobOutputResponseTypeDef",
    "CreateJobInputTypeDef",
    "CreateJobOutputResponseTypeDef",
    "GetShippingLabelInputTypeDef",
    "GetShippingLabelOutputResponseTypeDef",
    "GetStatusInputTypeDef",
    "GetStatusOutputResponseTypeDef",
    "JobTypeDef",
    "ListJobsInputTypeDef",
    "ListJobsOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateJobInputTypeDef",
    "UpdateJobOutputResponseTypeDef",
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "Description": str,
        "URL": str,
    },
    total=False,
)

_RequiredCancelJobInputTypeDef = TypedDict(
    "_RequiredCancelJobInputTypeDef",
    {
        "JobId": str,
    },
)
_OptionalCancelJobInputTypeDef = TypedDict(
    "_OptionalCancelJobInputTypeDef",
    {
        "APIVersion": str,
    },
    total=False,
)


class CancelJobInputTypeDef(_RequiredCancelJobInputTypeDef, _OptionalCancelJobInputTypeDef):
    pass


CancelJobOutputResponseTypeDef = TypedDict(
    "CancelJobOutputResponseTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobInputTypeDef = TypedDict(
    "_RequiredCreateJobInputTypeDef",
    {
        "JobType": JobTypeType,
        "Manifest": str,
        "ValidateOnly": bool,
    },
)
_OptionalCreateJobInputTypeDef = TypedDict(
    "_OptionalCreateJobInputTypeDef",
    {
        "ManifestAddendum": str,
        "APIVersion": str,
    },
    total=False,
)


class CreateJobInputTypeDef(_RequiredCreateJobInputTypeDef, _OptionalCreateJobInputTypeDef):
    pass


CreateJobOutputResponseTypeDef = TypedDict(
    "CreateJobOutputResponseTypeDef",
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

_RequiredGetShippingLabelInputTypeDef = TypedDict(
    "_RequiredGetShippingLabelInputTypeDef",
    {
        "jobIds": List[str],
    },
)
_OptionalGetShippingLabelInputTypeDef = TypedDict(
    "_OptionalGetShippingLabelInputTypeDef",
    {
        "name": str,
        "company": str,
        "phoneNumber": str,
        "country": str,
        "stateOrProvince": str,
        "city": str,
        "postalCode": str,
        "street1": str,
        "street2": str,
        "street3": str,
        "APIVersion": str,
    },
    total=False,
)


class GetShippingLabelInputTypeDef(
    _RequiredGetShippingLabelInputTypeDef, _OptionalGetShippingLabelInputTypeDef
):
    pass


GetShippingLabelOutputResponseTypeDef = TypedDict(
    "GetShippingLabelOutputResponseTypeDef",
    {
        "ShippingLabelURL": str,
        "Warning": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStatusInputTypeDef = TypedDict(
    "_RequiredGetStatusInputTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetStatusInputTypeDef = TypedDict(
    "_OptionalGetStatusInputTypeDef",
    {
        "APIVersion": str,
    },
    total=False,
)


class GetStatusInputTypeDef(_RequiredGetStatusInputTypeDef, _OptionalGetStatusInputTypeDef):
    pass


GetStatusOutputResponseTypeDef = TypedDict(
    "GetStatusOutputResponseTypeDef",
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

ListJobsInputTypeDef = TypedDict(
    "ListJobsInputTypeDef",
    {
        "MaxJobs": int,
        "Marker": str,
        "APIVersion": str,
    },
    total=False,
)

ListJobsOutputResponseTypeDef = TypedDict(
    "ListJobsOutputResponseTypeDef",
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

_RequiredUpdateJobInputTypeDef = TypedDict(
    "_RequiredUpdateJobInputTypeDef",
    {
        "JobId": str,
        "Manifest": str,
        "JobType": JobTypeType,
        "ValidateOnly": bool,
    },
)
_OptionalUpdateJobInputTypeDef = TypedDict(
    "_OptionalUpdateJobInputTypeDef",
    {
        "APIVersion": str,
    },
    total=False,
)


class UpdateJobInputTypeDef(_RequiredUpdateJobInputTypeDef, _OptionalUpdateJobInputTypeDef):
    pass


UpdateJobOutputResponseTypeDef = TypedDict(
    "UpdateJobOutputResponseTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
