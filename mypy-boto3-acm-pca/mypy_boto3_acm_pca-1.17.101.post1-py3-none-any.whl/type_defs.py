"""
Type annotations for acm-pca service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/type_defs.html)

Usage::

    ```python
    from mypy_boto3_acm_pca.type_defs import ASN1SubjectTypeDef

    data: ASN1SubjectTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AccessMethodTypeType,
    ActionTypeType,
    AuditReportResponseFormatType,
    AuditReportStatusType,
    CertificateAuthorityStatusType,
    CertificateAuthorityTypeType,
    ExtendedKeyUsageTypeType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyStorageSecurityStandardType,
    ResourceOwnerType,
    RevocationReasonType,
    S3ObjectAclType,
    SigningAlgorithmType,
    ValidityPeriodTypeType,
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
    "ASN1SubjectTypeDef",
    "AccessDescriptionTypeDef",
    "AccessMethodTypeDef",
    "ApiPassthroughTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityAuditReportRequestTypeDef",
    "CreateCertificateAuthorityAuditReportResponseResponseTypeDef",
    "CreateCertificateAuthorityRequestTypeDef",
    "CreateCertificateAuthorityResponseResponseTypeDef",
    "CreatePermissionRequestTypeDef",
    "CrlConfigurationTypeDef",
    "CsrExtensionsTypeDef",
    "DeleteCertificateAuthorityRequestTypeDef",
    "DeletePermissionRequestTypeDef",
    "DeletePolicyRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportRequestTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseResponseTypeDef",
    "DescribeCertificateAuthorityRequestTypeDef",
    "DescribeCertificateAuthorityResponseResponseTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "ExtensionsTypeDef",
    "GeneralNameTypeDef",
    "GetCertificateAuthorityCertificateRequestTypeDef",
    "GetCertificateAuthorityCertificateResponseResponseTypeDef",
    "GetCertificateAuthorityCsrRequestTypeDef",
    "GetCertificateAuthorityCsrResponseResponseTypeDef",
    "GetCertificateRequestTypeDef",
    "GetCertificateResponseResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseResponseTypeDef",
    "ImportCertificateAuthorityCertificateRequestTypeDef",
    "IssueCertificateRequestTypeDef",
    "IssueCertificateResponseResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificateAuthoritiesRequestTypeDef",
    "ListCertificateAuthoritiesResponseResponseTypeDef",
    "ListPermissionsRequestTypeDef",
    "ListPermissionsResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "OtherNameTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PolicyInformationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "PutPolicyRequestTypeDef",
    "QualifierTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCertificateAuthorityRequestTypeDef",
    "RevocationConfigurationTypeDef",
    "RevokeCertificateRequestTypeDef",
    "TagCertificateAuthorityRequestTypeDef",
    "TagTypeDef",
    "UntagCertificateAuthorityRequestTypeDef",
    "UpdateCertificateAuthorityRequestTypeDef",
    "ValidityTypeDef",
    "WaiterConfigTypeDef",
)

ASN1SubjectTypeDef = TypedDict(
    "ASN1SubjectTypeDef",
    {
        "Country": str,
        "Organization": str,
        "OrganizationalUnit": str,
        "DistinguishedNameQualifier": str,
        "State": str,
        "CommonName": str,
        "SerialNumber": str,
        "Locality": str,
        "Title": str,
        "Surname": str,
        "GivenName": str,
        "Initials": str,
        "Pseudonym": str,
        "GenerationQualifier": str,
    },
    total=False,
)

AccessDescriptionTypeDef = TypedDict(
    "AccessDescriptionTypeDef",
    {
        "AccessMethod": "AccessMethodTypeDef",
        "AccessLocation": "GeneralNameTypeDef",
    },
)

AccessMethodTypeDef = TypedDict(
    "AccessMethodTypeDef",
    {
        "CustomObjectIdentifier": str,
        "AccessMethodType": AccessMethodTypeType,
    },
    total=False,
)

ApiPassthroughTypeDef = TypedDict(
    "ApiPassthroughTypeDef",
    {
        "Extensions": "ExtensionsTypeDef",
        "Subject": "ASN1SubjectTypeDef",
    },
    total=False,
)

_RequiredCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_RequiredCertificateAuthorityConfigurationTypeDef",
    {
        "KeyAlgorithm": KeyAlgorithmType,
        "SigningAlgorithm": SigningAlgorithmType,
        "Subject": "ASN1SubjectTypeDef",
    },
)
_OptionalCertificateAuthorityConfigurationTypeDef = TypedDict(
    "_OptionalCertificateAuthorityConfigurationTypeDef",
    {
        "CsrExtensions": "CsrExtensionsTypeDef",
    },
    total=False,
)


class CertificateAuthorityConfigurationTypeDef(
    _RequiredCertificateAuthorityConfigurationTypeDef,
    _OptionalCertificateAuthorityConfigurationTypeDef,
):
    pass


CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": str,
        "OwnerAccount": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": CertificateAuthorityTypeType,
        "Serial": str,
        "Status": CertificateAuthorityStatusType,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": FailureReasonType,
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "RestorableUntil": datetime,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandardType,
    },
    total=False,
)

CreateCertificateAuthorityAuditReportRequestTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "S3BucketName": str,
        "AuditReportResponseFormat": AuditReportResponseFormatType,
    },
)

CreateCertificateAuthorityAuditReportResponseResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityAuditReportResponseResponseTypeDef",
    {
        "AuditReportId": str,
        "S3Key": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateAuthorityRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "CertificateAuthorityType": CertificateAuthorityTypeType,
    },
)
_OptionalCreateCertificateAuthorityRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateAuthorityRequestTypeDef",
    {
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "IdempotencyToken": str,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandardType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCertificateAuthorityRequestTypeDef(
    _RequiredCreateCertificateAuthorityRequestTypeDef,
    _OptionalCreateCertificateAuthorityRequestTypeDef,
):
    pass


CreateCertificateAuthorityResponseResponseTypeDef = TypedDict(
    "CreateCertificateAuthorityResponseResponseTypeDef",
    {
        "CertificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePermissionRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
        "Actions": List[ActionTypeType],
    },
)
_OptionalCreatePermissionRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionRequestTypeDef",
    {
        "SourceAccount": str,
    },
    total=False,
)


class CreatePermissionRequestTypeDef(
    _RequiredCreatePermissionRequestTypeDef, _OptionalCreatePermissionRequestTypeDef
):
    pass


_RequiredCrlConfigurationTypeDef = TypedDict(
    "_RequiredCrlConfigurationTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCrlConfigurationTypeDef = TypedDict(
    "_OptionalCrlConfigurationTypeDef",
    {
        "ExpirationInDays": int,
        "CustomCname": str,
        "S3BucketName": str,
        "S3ObjectAcl": S3ObjectAclType,
    },
    total=False,
)


class CrlConfigurationTypeDef(_RequiredCrlConfigurationTypeDef, _OptionalCrlConfigurationTypeDef):
    pass


CsrExtensionsTypeDef = TypedDict(
    "CsrExtensionsTypeDef",
    {
        "KeyUsage": "KeyUsageTypeDef",
        "SubjectInformationAccess": List["AccessDescriptionTypeDef"],
    },
    total=False,
)

_RequiredDeleteCertificateAuthorityRequestTypeDef = TypedDict(
    "_RequiredDeleteCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalDeleteCertificateAuthorityRequestTypeDef = TypedDict(
    "_OptionalDeleteCertificateAuthorityRequestTypeDef",
    {
        "PermanentDeletionTimeInDays": int,
    },
    total=False,
)


class DeleteCertificateAuthorityRequestTypeDef(
    _RequiredDeleteCertificateAuthorityRequestTypeDef,
    _OptionalDeleteCertificateAuthorityRequestTypeDef,
):
    pass


_RequiredDeletePermissionRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Principal": str,
    },
)
_OptionalDeletePermissionRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionRequestTypeDef",
    {
        "SourceAccount": str,
    },
    total=False,
)


class DeletePermissionRequestTypeDef(
    _RequiredDeletePermissionRequestTypeDef, _OptionalDeletePermissionRequestTypeDef
):
    pass


DeletePolicyRequestTypeDef = TypedDict(
    "DeletePolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeCertificateAuthorityAuditReportRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "AuditReportId": str,
    },
)

DescribeCertificateAuthorityAuditReportResponseResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityAuditReportResponseResponseTypeDef",
    {
        "AuditReportStatus": AuditReportStatusType,
        "S3BucketName": str,
        "S3Key": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificateAuthorityRequestTypeDef = TypedDict(
    "DescribeCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

DescribeCertificateAuthorityResponseResponseTypeDef = TypedDict(
    "DescribeCertificateAuthorityResponseResponseTypeDef",
    {
        "CertificateAuthority": "CertificateAuthorityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEdiPartyNameTypeDef = TypedDict(
    "_RequiredEdiPartyNameTypeDef",
    {
        "PartyName": str,
    },
)
_OptionalEdiPartyNameTypeDef = TypedDict(
    "_OptionalEdiPartyNameTypeDef",
    {
        "NameAssigner": str,
    },
    total=False,
)


class EdiPartyNameTypeDef(_RequiredEdiPartyNameTypeDef, _OptionalEdiPartyNameTypeDef):
    pass


ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "ExtendedKeyUsageType": ExtendedKeyUsageTypeType,
        "ExtendedKeyUsageObjectIdentifier": str,
    },
    total=False,
)

ExtensionsTypeDef = TypedDict(
    "ExtensionsTypeDef",
    {
        "CertificatePolicies": List["PolicyInformationTypeDef"],
        "ExtendedKeyUsage": List["ExtendedKeyUsageTypeDef"],
        "KeyUsage": "KeyUsageTypeDef",
        "SubjectAlternativeNames": List["GeneralNameTypeDef"],
    },
    total=False,
)

GeneralNameTypeDef = TypedDict(
    "GeneralNameTypeDef",
    {
        "OtherName": "OtherNameTypeDef",
        "Rfc822Name": str,
        "DnsName": str,
        "DirectoryName": "ASN1SubjectTypeDef",
        "EdiPartyName": "EdiPartyNameTypeDef",
        "UniformResourceIdentifier": str,
        "IpAddress": str,
        "RegisteredId": str,
    },
    total=False,
)

GetCertificateAuthorityCertificateRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCertificateResponseResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCertificateResponseResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateAuthorityCsrRequestTypeDef = TypedDict(
    "GetCertificateAuthorityCsrRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

GetCertificateAuthorityCsrResponseResponseTypeDef = TypedDict(
    "GetCertificateAuthorityCsrResponseResponseTypeDef",
    {
        "Csr": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateRequestTypeDef = TypedDict(
    "GetCertificateRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateArn": str,
    },
)

GetCertificateResponseResponseTypeDef = TypedDict(
    "GetCertificateResponseResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestTypeDef = TypedDict(
    "GetPolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetPolicyResponseResponseTypeDef = TypedDict(
    "GetPolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportCertificateAuthorityCertificateRequestTypeDef = TypedDict(
    "_RequiredImportCertificateAuthorityCertificateRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Certificate": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportCertificateAuthorityCertificateRequestTypeDef = TypedDict(
    "_OptionalImportCertificateAuthorityCertificateRequestTypeDef",
    {
        "CertificateChain": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class ImportCertificateAuthorityCertificateRequestTypeDef(
    _RequiredImportCertificateAuthorityCertificateRequestTypeDef,
    _OptionalImportCertificateAuthorityCertificateRequestTypeDef,
):
    pass


_RequiredIssueCertificateRequestTypeDef = TypedDict(
    "_RequiredIssueCertificateRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Csr": Union[bytes, IO[bytes], StreamingBody],
        "SigningAlgorithm": SigningAlgorithmType,
        "Validity": "ValidityTypeDef",
    },
)
_OptionalIssueCertificateRequestTypeDef = TypedDict(
    "_OptionalIssueCertificateRequestTypeDef",
    {
        "ApiPassthrough": "ApiPassthroughTypeDef",
        "TemplateArn": str,
        "ValidityNotBefore": "ValidityTypeDef",
        "IdempotencyToken": str,
    },
    total=False,
)


class IssueCertificateRequestTypeDef(
    _RequiredIssueCertificateRequestTypeDef, _OptionalIssueCertificateRequestTypeDef
):
    pass


IssueCertificateResponseResponseTypeDef = TypedDict(
    "IssueCertificateResponseResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "DigitalSignature": bool,
        "NonRepudiation": bool,
        "KeyEncipherment": bool,
        "DataEncipherment": bool,
        "KeyAgreement": bool,
        "KeyCertSign": bool,
        "CRLSign": bool,
        "EncipherOnly": bool,
        "DecipherOnly": bool,
    },
    total=False,
)

ListCertificateAuthoritiesRequestTypeDef = TypedDict(
    "ListCertificateAuthoritiesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ResourceOwner": ResourceOwnerType,
    },
    total=False,
)

ListCertificateAuthoritiesResponseResponseTypeDef = TypedDict(
    "ListCertificateAuthoritiesResponseResponseTypeDef",
    {
        "CertificateAuthorities": List["CertificateAuthorityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionsRequestTypeDef = TypedDict(
    "_RequiredListPermissionsRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListPermissionsRequestTypeDef = TypedDict(
    "_OptionalListPermissionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPermissionsRequestTypeDef(
    _RequiredListPermissionsRequestTypeDef, _OptionalListPermissionsRequestTypeDef
):
    pass


ListPermissionsResponseResponseTypeDef = TypedDict(
    "ListPermissionsResponseResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalListTagsRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsRequestTypeDef(_RequiredListTagsRequestTypeDef, _OptionalListTagsRequestTypeDef):
    pass


ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OtherNameTypeDef = TypedDict(
    "OtherNameTypeDef",
    {
        "TypeId": str,
        "Value": str,
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
        "CertificateAuthorityArn": str,
        "CreatedAt": datetime,
        "Principal": str,
        "SourceAccount": str,
        "Actions": List[ActionTypeType],
        "Policy": str,
    },
    total=False,
)

_RequiredPolicyInformationTypeDef = TypedDict(
    "_RequiredPolicyInformationTypeDef",
    {
        "CertPolicyId": str,
    },
)
_OptionalPolicyInformationTypeDef = TypedDict(
    "_OptionalPolicyInformationTypeDef",
    {
        "PolicyQualifiers": List["PolicyQualifierInfoTypeDef"],
    },
    total=False,
)


class PolicyInformationTypeDef(
    _RequiredPolicyInformationTypeDef, _OptionalPolicyInformationTypeDef
):
    pass


PolicyQualifierInfoTypeDef = TypedDict(
    "PolicyQualifierInfoTypeDef",
    {
        "PolicyQualifierId": Literal["CPS"],
        "Qualifier": "QualifierTypeDef",
    },
)

PutPolicyRequestTypeDef = TypedDict(
    "PutPolicyRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

QualifierTypeDef = TypedDict(
    "QualifierTypeDef",
    {
        "CpsUri": str,
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

RestoreCertificateAuthorityRequestTypeDef = TypedDict(
    "RestoreCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)

RevocationConfigurationTypeDef = TypedDict(
    "RevocationConfigurationTypeDef",
    {
        "CrlConfiguration": "CrlConfigurationTypeDef",
    },
    total=False,
)

RevokeCertificateRequestTypeDef = TypedDict(
    "RevokeCertificateRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CertificateSerial": str,
        "RevocationReason": RevocationReasonType,
    },
)

TagCertificateAuthorityRequestTypeDef = TypedDict(
    "TagCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": List["TagTypeDef"],
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


UntagCertificateAuthorityRequestTypeDef = TypedDict(
    "UntagCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredUpdateCertificateAuthorityRequestTypeDef = TypedDict(
    "_RequiredUpdateCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityArn": str,
    },
)
_OptionalUpdateCertificateAuthorityRequestTypeDef = TypedDict(
    "_OptionalUpdateCertificateAuthorityRequestTypeDef",
    {
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "Status": CertificateAuthorityStatusType,
    },
    total=False,
)


class UpdateCertificateAuthorityRequestTypeDef(
    _RequiredUpdateCertificateAuthorityRequestTypeDef,
    _OptionalUpdateCertificateAuthorityRequestTypeDef,
):
    pass


ValidityTypeDef = TypedDict(
    "ValidityTypeDef",
    {
        "Value": int,
        "Type": ValidityPeriodTypeType,
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
