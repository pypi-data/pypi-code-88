"""
Type annotations for signer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_signer.type_defs import AddProfilePermissionRequestTypeDef

    data: AddProfilePermissionRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EncryptionAlgorithmType,
    HashAlgorithmType,
    ImageFormatType,
    SigningProfileStatusType,
    SigningStatusType,
    ValidityTypeType,
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
    "AddProfilePermissionRequestTypeDef",
    "AddProfilePermissionResponseResponseTypeDef",
    "CancelSigningProfileRequestTypeDef",
    "DescribeSigningJobRequestTypeDef",
    "DescribeSigningJobResponseResponseTypeDef",
    "DestinationTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "GetSigningPlatformRequestTypeDef",
    "GetSigningPlatformResponseResponseTypeDef",
    "GetSigningProfileRequestTypeDef",
    "GetSigningProfileResponseResponseTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsRequestTypeDef",
    "ListProfilePermissionsResponseResponseTypeDef",
    "ListSigningJobsRequestTypeDef",
    "ListSigningJobsResponseResponseTypeDef",
    "ListSigningPlatformsRequestTypeDef",
    "ListSigningPlatformsResponseResponseTypeDef",
    "ListSigningProfilesRequestTypeDef",
    "ListSigningProfilesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutSigningProfileRequestTypeDef",
    "PutSigningProfileResponseResponseTypeDef",
    "RemoveProfilePermissionRequestTypeDef",
    "RemoveProfilePermissionResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeSignatureRequestTypeDef",
    "RevokeSigningProfileRequestTypeDef",
    "S3DestinationTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
    "SignatureValidityPeriodTypeDef",
    "SignedObjectTypeDef",
    "SigningConfigurationOverridesTypeDef",
    "SigningConfigurationTypeDef",
    "SigningImageFormatTypeDef",
    "SigningJobRevocationRecordTypeDef",
    "SigningJobTypeDef",
    "SigningMaterialTypeDef",
    "SigningPlatformOverridesTypeDef",
    "SigningPlatformTypeDef",
    "SigningProfileRevocationRecordTypeDef",
    "SigningProfileTypeDef",
    "SourceTypeDef",
    "StartSigningJobRequestTypeDef",
    "StartSigningJobResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAddProfilePermissionRequestTypeDef = TypedDict(
    "_RequiredAddProfilePermissionRequestTypeDef",
    {
        "profileName": str,
        "action": str,
        "principal": str,
        "statementId": str,
    },
)
_OptionalAddProfilePermissionRequestTypeDef = TypedDict(
    "_OptionalAddProfilePermissionRequestTypeDef",
    {
        "profileVersion": str,
        "revisionId": str,
    },
    total=False,
)


class AddProfilePermissionRequestTypeDef(
    _RequiredAddProfilePermissionRequestTypeDef, _OptionalAddProfilePermissionRequestTypeDef
):
    pass


AddProfilePermissionResponseResponseTypeDef = TypedDict(
    "AddProfilePermissionResponseResponseTypeDef",
    {
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSigningProfileRequestTypeDef = TypedDict(
    "CancelSigningProfileRequestTypeDef",
    {
        "profileName": str,
    },
)

DescribeSigningJobRequestTypeDef = TypedDict(
    "DescribeSigningJobRequestTypeDef",
    {
        "jobId": str,
    },
)

DescribeSigningJobResponseResponseTypeDef = TypedDict(
    "DescribeSigningJobResponseResponseTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "profileName": str,
        "profileVersion": str,
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "signatureExpiresAt": datetime,
        "requestedBy": str,
        "status": SigningStatusType,
        "statusReason": str,
        "revocationRecord": "SigningJobRevocationRecordTypeDef",
        "signedObject": "SignedObjectTypeDef",
        "jobOwner": str,
        "jobInvoker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3": "S3DestinationTypeDef",
    },
    total=False,
)

EncryptionAlgorithmOptionsTypeDef = TypedDict(
    "EncryptionAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[EncryptionAlgorithmType],
        "defaultValue": EncryptionAlgorithmType,
    },
)

GetSigningPlatformRequestTypeDef = TypedDict(
    "GetSigningPlatformRequestTypeDef",
    {
        "platformId": str,
    },
)

GetSigningPlatformResponseResponseTypeDef = TypedDict(
    "GetSigningPlatformResponseResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": "SigningConfigurationTypeDef",
        "signingImageFormat": "SigningImageFormatTypeDef",
        "maxSizeInMB": int,
        "revocationSupported": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSigningProfileRequestTypeDef = TypedDict(
    "_RequiredGetSigningProfileRequestTypeDef",
    {
        "profileName": str,
    },
)
_OptionalGetSigningProfileRequestTypeDef = TypedDict(
    "_OptionalGetSigningProfileRequestTypeDef",
    {
        "profileOwner": str,
    },
    total=False,
)


class GetSigningProfileRequestTypeDef(
    _RequiredGetSigningProfileRequestTypeDef, _OptionalGetSigningProfileRequestTypeDef
):
    pass


GetSigningProfileResponseResponseTypeDef = TypedDict(
    "GetSigningProfileResponseResponseTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "revocationRecord": "SigningProfileRevocationRecordTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "status": SigningProfileStatusType,
        "statusReason": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[HashAlgorithmType],
        "defaultValue": HashAlgorithmType,
    },
)

_RequiredListProfilePermissionsRequestTypeDef = TypedDict(
    "_RequiredListProfilePermissionsRequestTypeDef",
    {
        "profileName": str,
    },
)
_OptionalListProfilePermissionsRequestTypeDef = TypedDict(
    "_OptionalListProfilePermissionsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListProfilePermissionsRequestTypeDef(
    _RequiredListProfilePermissionsRequestTypeDef, _OptionalListProfilePermissionsRequestTypeDef
):
    pass


ListProfilePermissionsResponseResponseTypeDef = TypedDict(
    "ListProfilePermissionsResponseResponseTypeDef",
    {
        "revisionId": str,
        "policySizeBytes": int,
        "permissions": List["PermissionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningJobsRequestTypeDef = TypedDict(
    "ListSigningJobsRequestTypeDef",
    {
        "status": SigningStatusType,
        "platformId": str,
        "requestedBy": str,
        "maxResults": int,
        "nextToken": str,
        "isRevoked": bool,
        "signatureExpiresBefore": Union[datetime, str],
        "signatureExpiresAfter": Union[datetime, str],
        "jobInvoker": str,
    },
    total=False,
)

ListSigningJobsResponseResponseTypeDef = TypedDict(
    "ListSigningJobsResponseResponseTypeDef",
    {
        "jobs": List["SigningJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningPlatformsRequestTypeDef = TypedDict(
    "ListSigningPlatformsRequestTypeDef",
    {
        "category": str,
        "partner": str,
        "target": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSigningPlatformsResponseResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseResponseTypeDef",
    {
        "platforms": List["SigningPlatformTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningProfilesRequestTypeDef = TypedDict(
    "ListSigningProfilesRequestTypeDef",
    {
        "includeCanceled": bool,
        "maxResults": int,
        "nextToken": str,
        "platformId": str,
        "statuses": List[SigningProfileStatusType],
    },
    total=False,
)

ListSigningProfilesResponseResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseResponseTypeDef",
    {
        "profiles": List["SigningProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "action": str,
        "principal": str,
        "statementId": str,
        "profileVersion": str,
    },
    total=False,
)

_RequiredPutSigningProfileRequestTypeDef = TypedDict(
    "_RequiredPutSigningProfileRequestTypeDef",
    {
        "profileName": str,
        "platformId": str,
    },
)
_OptionalPutSigningProfileRequestTypeDef = TypedDict(
    "_OptionalPutSigningProfileRequestTypeDef",
    {
        "signingMaterial": "SigningMaterialTypeDef",
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "overrides": "SigningPlatformOverridesTypeDef",
        "signingParameters": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)


class PutSigningProfileRequestTypeDef(
    _RequiredPutSigningProfileRequestTypeDef, _OptionalPutSigningProfileRequestTypeDef
):
    pass


PutSigningProfileResponseResponseTypeDef = TypedDict(
    "PutSigningProfileResponseResponseTypeDef",
    {
        "arn": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveProfilePermissionRequestTypeDef = TypedDict(
    "RemoveProfilePermissionRequestTypeDef",
    {
        "profileName": str,
        "revisionId": str,
        "statementId": str,
    },
)

RemoveProfilePermissionResponseResponseTypeDef = TypedDict(
    "RemoveProfilePermissionResponseResponseTypeDef",
    {
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredRevokeSignatureRequestTypeDef = TypedDict(
    "_RequiredRevokeSignatureRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)
_OptionalRevokeSignatureRequestTypeDef = TypedDict(
    "_OptionalRevokeSignatureRequestTypeDef",
    {
        "jobOwner": str,
    },
    total=False,
)


class RevokeSignatureRequestTypeDef(
    _RequiredRevokeSignatureRequestTypeDef, _OptionalRevokeSignatureRequestTypeDef
):
    pass


RevokeSigningProfileRequestTypeDef = TypedDict(
    "RevokeSigningProfileRequestTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "reason": str,
        "effectiveTime": Union[datetime, str],
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucketName": str,
        "prefix": str,
    },
    total=False,
)

S3SignedObjectTypeDef = TypedDict(
    "S3SignedObjectTypeDef",
    {
        "bucketName": str,
        "key": str,
    },
    total=False,
)

S3SourceTypeDef = TypedDict(
    "S3SourceTypeDef",
    {
        "bucketName": str,
        "key": str,
        "version": str,
    },
)

SignatureValidityPeriodTypeDef = TypedDict(
    "SignatureValidityPeriodTypeDef",
    {
        "value": int,
        "type": ValidityTypeType,
    },
    total=False,
)

SignedObjectTypeDef = TypedDict(
    "SignedObjectTypeDef",
    {
        "s3": "S3SignedObjectTypeDef",
    },
    total=False,
)

SigningConfigurationOverridesTypeDef = TypedDict(
    "SigningConfigurationOverridesTypeDef",
    {
        "encryptionAlgorithm": EncryptionAlgorithmType,
        "hashAlgorithm": HashAlgorithmType,
    },
    total=False,
)

SigningConfigurationTypeDef = TypedDict(
    "SigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": "EncryptionAlgorithmOptionsTypeDef",
        "hashAlgorithmOptions": "HashAlgorithmOptionsTypeDef",
    },
)

SigningImageFormatTypeDef = TypedDict(
    "SigningImageFormatTypeDef",
    {
        "supportedFormats": List[ImageFormatType],
        "defaultFormat": ImageFormatType,
    },
)

SigningJobRevocationRecordTypeDef = TypedDict(
    "SigningJobRevocationRecordTypeDef",
    {
        "reason": str,
        "revokedAt": datetime,
        "revokedBy": str,
    },
    total=False,
)

SigningJobTypeDef = TypedDict(
    "SigningJobTypeDef",
    {
        "jobId": str,
        "source": "SourceTypeDef",
        "signedObject": "SignedObjectTypeDef",
        "signingMaterial": "SigningMaterialTypeDef",
        "createdAt": datetime,
        "status": SigningStatusType,
        "isRevoked": bool,
        "profileName": str,
        "profileVersion": str,
        "platformId": str,
        "platformDisplayName": str,
        "signatureExpiresAt": datetime,
        "jobOwner": str,
        "jobInvoker": str,
    },
    total=False,
)

SigningMaterialTypeDef = TypedDict(
    "SigningMaterialTypeDef",
    {
        "certificateArn": str,
    },
)

SigningPlatformOverridesTypeDef = TypedDict(
    "SigningPlatformOverridesTypeDef",
    {
        "signingConfiguration": "SigningConfigurationOverridesTypeDef",
        "signingImageFormat": ImageFormatType,
    },
    total=False,
)

SigningPlatformTypeDef = TypedDict(
    "SigningPlatformTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": "SigningConfigurationTypeDef",
        "signingImageFormat": "SigningImageFormatTypeDef",
        "maxSizeInMB": int,
        "revocationSupported": bool,
    },
    total=False,
)

SigningProfileRevocationRecordTypeDef = TypedDict(
    "SigningProfileRevocationRecordTypeDef",
    {
        "revocationEffectiveFrom": datetime,
        "revokedAt": datetime,
        "revokedBy": str,
    },
    total=False,
)

SigningProfileTypeDef = TypedDict(
    "SigningProfileTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "signingMaterial": "SigningMaterialTypeDef",
        "signatureValidityPeriod": "SignatureValidityPeriodTypeDef",
        "platformId": str,
        "platformDisplayName": str,
        "signingParameters": Dict[str, str],
        "status": SigningProfileStatusType,
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3": "S3SourceTypeDef",
    },
    total=False,
)

_RequiredStartSigningJobRequestTypeDef = TypedDict(
    "_RequiredStartSigningJobRequestTypeDef",
    {
        "source": "SourceTypeDef",
        "destination": "DestinationTypeDef",
        "profileName": str,
        "clientRequestToken": str,
    },
)
_OptionalStartSigningJobRequestTypeDef = TypedDict(
    "_OptionalStartSigningJobRequestTypeDef",
    {
        "profileOwner": str,
    },
    total=False,
)


class StartSigningJobRequestTypeDef(
    _RequiredStartSigningJobRequestTypeDef, _OptionalStartSigningJobRequestTypeDef
):
    pass


StartSigningJobResponseResponseTypeDef = TypedDict(
    "StartSigningJobResponseResponseTypeDef",
    {
        "jobId": str,
        "jobOwner": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
