"""
Type annotations for signer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_signer.type_defs import AddProfilePermissionResponseTypeDef

    data: AddProfilePermissionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

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
    "AddProfilePermissionResponseTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "DestinationTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "GetSigningProfileResponseTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsResponseTypeDef",
    "ListSigningJobsResponseTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutSigningProfileResponseTypeDef",
    "RemoveProfilePermissionResponseTypeDef",
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
    "StartSigningJobResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddProfilePermissionResponseTypeDef = TypedDict(
    "AddProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
    },
    total=False,
)

DescribeSigningJobResponseTypeDef = TypedDict(
    "DescribeSigningJobResponseTypeDef",
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
    },
    total=False,
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

GetSigningPlatformResponseTypeDef = TypedDict(
    "GetSigningPlatformResponseTypeDef",
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

GetSigningProfileResponseTypeDef = TypedDict(
    "GetSigningProfileResponseTypeDef",
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
    },
    total=False,
)

HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[HashAlgorithmType],
        "defaultValue": HashAlgorithmType,
    },
)

ListProfilePermissionsResponseTypeDef = TypedDict(
    "ListProfilePermissionsResponseTypeDef",
    {
        "revisionId": str,
        "policySizeBytes": int,
        "permissions": List["PermissionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSigningJobsResponseTypeDef = TypedDict(
    "ListSigningJobsResponseTypeDef",
    {
        "jobs": List["SigningJobTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSigningPlatformsResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseTypeDef",
    {
        "platforms": List["SigningPlatformTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSigningProfilesResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseTypeDef",
    {
        "profiles": List["SigningProfileTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
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

PutSigningProfileResponseTypeDef = TypedDict(
    "PutSigningProfileResponseTypeDef",
    {
        "arn": str,
        "profileVersion": str,
        "profileVersionArn": str,
    },
    total=False,
)

RemoveProfilePermissionResponseTypeDef = TypedDict(
    "RemoveProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
    },
    total=False,
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

StartSigningJobResponseTypeDef = TypedDict(
    "StartSigningJobResponseTypeDef",
    {
        "jobId": str,
        "jobOwner": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
