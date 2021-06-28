"""
Type annotations for acm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_acm.type_defs import AddTagsToCertificateRequestTypeDef

    data: AddTagsToCertificateRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    CertificateStatusType,
    CertificateTransparencyLoggingPreferenceType,
    CertificateTypeType,
    DomainStatusType,
    ExtendedKeyUsageNameType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyUsageNameType,
    RenewalEligibilityType,
    RenewalStatusType,
    RevocationReasonType,
    ValidationMethodType,
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
    "AddTagsToCertificateRequestTypeDef",
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DeleteCertificateRequestTypeDef",
    "DescribeCertificateRequestTypeDef",
    "DescribeCertificateResponseResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "DomainValidationTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "ExportCertificateRequestTypeDef",
    "ExportCertificateResponseResponseTypeDef",
    "ExtendedKeyUsageTypeDef",
    "FiltersTypeDef",
    "GetAccountConfigurationResponseResponseTypeDef",
    "GetCertificateRequestTypeDef",
    "GetCertificateResponseResponseTypeDef",
    "ImportCertificateRequestTypeDef",
    "ImportCertificateResponseResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificatesRequestTypeDef",
    "ListCertificatesResponseResponseTypeDef",
    "ListTagsForCertificateRequestTypeDef",
    "ListTagsForCertificateResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountConfigurationRequestTypeDef",
    "RemoveTagsFromCertificateRequestTypeDef",
    "RenewCertificateRequestTypeDef",
    "RenewalSummaryTypeDef",
    "RequestCertificateRequestTypeDef",
    "RequestCertificateResponseResponseTypeDef",
    "ResendValidationEmailRequestTypeDef",
    "ResourceRecordTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "UpdateCertificateOptionsRequestTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToCertificateRequestTypeDef = TypedDict(
    "AddTagsToCertificateRequestTypeDef",
    {
        "CertificateArn": str,
        "Tags": List["TagTypeDef"],
    },
)

CertificateDetailTypeDef = TypedDict(
    "CertificateDetailTypeDef",
    {
        "CertificateArn": str,
        "DomainName": str,
        "SubjectAlternativeNames": List[str],
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "Serial": str,
        "Subject": str,
        "Issuer": str,
        "CreatedAt": datetime,
        "IssuedAt": datetime,
        "ImportedAt": datetime,
        "Status": CertificateStatusType,
        "RevokedAt": datetime,
        "RevocationReason": RevocationReasonType,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "KeyAlgorithm": KeyAlgorithmType,
        "SignatureAlgorithm": str,
        "InUseBy": List[str],
        "FailureReason": FailureReasonType,
        "Type": CertificateTypeType,
        "RenewalSummary": "RenewalSummaryTypeDef",
        "KeyUsages": List["KeyUsageTypeDef"],
        "ExtendedKeyUsages": List["ExtendedKeyUsageTypeDef"],
        "CertificateAuthorityArn": str,
        "RenewalEligibility": RenewalEligibilityType,
        "Options": "CertificateOptionsTypeDef",
    },
    total=False,
)

CertificateOptionsTypeDef = TypedDict(
    "CertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": CertificateTransparencyLoggingPreferenceType,
    },
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "CertificateArn": str,
        "DomainName": str,
    },
    total=False,
)

DeleteCertificateRequestTypeDef = TypedDict(
    "DeleteCertificateRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DescribeCertificateRequestTypeDef = TypedDict(
    "DescribeCertificateRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DescribeCertificateResponseResponseTypeDef = TypedDict(
    "DescribeCertificateResponseResponseTypeDef",
    {
        "Certificate": "CertificateDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainValidationOptionTypeDef = TypedDict(
    "DomainValidationOptionTypeDef",
    {
        "DomainName": str,
        "ValidationDomain": str,
    },
)

_RequiredDomainValidationTypeDef = TypedDict(
    "_RequiredDomainValidationTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainValidationTypeDef = TypedDict(
    "_OptionalDomainValidationTypeDef",
    {
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": DomainStatusType,
        "ResourceRecord": "ResourceRecordTypeDef",
        "ValidationMethod": ValidationMethodType,
    },
    total=False,
)


class DomainValidationTypeDef(_RequiredDomainValidationTypeDef, _OptionalDomainValidationTypeDef):
    pass


ExpiryEventsConfigurationTypeDef = TypedDict(
    "ExpiryEventsConfigurationTypeDef",
    {
        "DaysBeforeExpiry": int,
    },
    total=False,
)

ExportCertificateRequestTypeDef = TypedDict(
    "ExportCertificateRequestTypeDef",
    {
        "CertificateArn": str,
        "Passphrase": Union[bytes, IO[bytes], StreamingBody],
    },
)

ExportCertificateResponseResponseTypeDef = TypedDict(
    "ExportCertificateResponseResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "PrivateKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "Name": ExtendedKeyUsageNameType,
        "OID": str,
    },
    total=False,
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "extendedKeyUsage": List[ExtendedKeyUsageNameType],
        "keyUsage": List[KeyUsageNameType],
        "keyTypes": List[KeyAlgorithmType],
    },
    total=False,
)

GetAccountConfigurationResponseResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseResponseTypeDef",
    {
        "ExpiryEvents": "ExpiryEventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificateRequestTypeDef = TypedDict(
    "GetCertificateRequestTypeDef",
    {
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

_RequiredImportCertificateRequestTypeDef = TypedDict(
    "_RequiredImportCertificateRequestTypeDef",
    {
        "Certificate": Union[bytes, IO[bytes], StreamingBody],
        "PrivateKey": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportCertificateRequestTypeDef = TypedDict(
    "_OptionalImportCertificateRequestTypeDef",
    {
        "CertificateArn": str,
        "CertificateChain": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ImportCertificateRequestTypeDef(
    _RequiredImportCertificateRequestTypeDef, _OptionalImportCertificateRequestTypeDef
):
    pass


ImportCertificateResponseResponseTypeDef = TypedDict(
    "ImportCertificateResponseResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "Name": KeyUsageNameType,
    },
    total=False,
)

ListCertificatesRequestTypeDef = TypedDict(
    "ListCertificatesRequestTypeDef",
    {
        "CertificateStatuses": List[CertificateStatusType],
        "Includes": "FiltersTypeDef",
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListCertificatesResponseResponseTypeDef = TypedDict(
    "ListCertificatesResponseResponseTypeDef",
    {
        "NextToken": str,
        "CertificateSummaryList": List["CertificateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForCertificateRequestTypeDef = TypedDict(
    "ListTagsForCertificateRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

ListTagsForCertificateResponseResponseTypeDef = TypedDict(
    "ListTagsForCertificateResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

_RequiredPutAccountConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutAccountConfigurationRequestTypeDef",
    {
        "IdempotencyToken": str,
    },
)
_OptionalPutAccountConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutAccountConfigurationRequestTypeDef",
    {
        "ExpiryEvents": "ExpiryEventsConfigurationTypeDef",
    },
    total=False,
)


class PutAccountConfigurationRequestTypeDef(
    _RequiredPutAccountConfigurationRequestTypeDef, _OptionalPutAccountConfigurationRequestTypeDef
):
    pass


RemoveTagsFromCertificateRequestTypeDef = TypedDict(
    "RemoveTagsFromCertificateRequestTypeDef",
    {
        "CertificateArn": str,
        "Tags": List["TagTypeDef"],
    },
)

RenewCertificateRequestTypeDef = TypedDict(
    "RenewCertificateRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

_RequiredRenewalSummaryTypeDef = TypedDict(
    "_RequiredRenewalSummaryTypeDef",
    {
        "RenewalStatus": RenewalStatusType,
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "UpdatedAt": datetime,
    },
)
_OptionalRenewalSummaryTypeDef = TypedDict(
    "_OptionalRenewalSummaryTypeDef",
    {
        "RenewalStatusReason": FailureReasonType,
    },
    total=False,
)


class RenewalSummaryTypeDef(_RequiredRenewalSummaryTypeDef, _OptionalRenewalSummaryTypeDef):
    pass


_RequiredRequestCertificateRequestTypeDef = TypedDict(
    "_RequiredRequestCertificateRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalRequestCertificateRequestTypeDef = TypedDict(
    "_OptionalRequestCertificateRequestTypeDef",
    {
        "ValidationMethod": ValidationMethodType,
        "SubjectAlternativeNames": List[str],
        "IdempotencyToken": str,
        "DomainValidationOptions": List["DomainValidationOptionTypeDef"],
        "Options": "CertificateOptionsTypeDef",
        "CertificateAuthorityArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RequestCertificateRequestTypeDef(
    _RequiredRequestCertificateRequestTypeDef, _OptionalRequestCertificateRequestTypeDef
):
    pass


RequestCertificateResponseResponseTypeDef = TypedDict(
    "RequestCertificateResponseResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResendValidationEmailRequestTypeDef = TypedDict(
    "ResendValidationEmailRequestTypeDef",
    {
        "CertificateArn": str,
        "Domain": str,
        "ValidationDomain": str,
    },
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Name": str,
        "Type": Literal["CNAME"],
        "Value": str,
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


UpdateCertificateOptionsRequestTypeDef = TypedDict(
    "UpdateCertificateOptionsRequestTypeDef",
    {
        "CertificateArn": str,
        "Options": "CertificateOptionsTypeDef",
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
