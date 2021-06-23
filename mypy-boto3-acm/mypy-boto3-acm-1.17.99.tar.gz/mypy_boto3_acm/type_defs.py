"""
Type annotations for acm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_acm.type_defs import CertificateDetailTypeDef

    data: CertificateDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "DomainValidationTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "ExportCertificateResponseTypeDef",
    "ExtendedKeyUsageTypeDef",
    "FiltersTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "ImportCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RenewalSummaryTypeDef",
    "RequestCertificateResponseTypeDef",
    "ResourceRecordTypeDef",
    "TagTypeDef",
    "WaiterConfigTypeDef",
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

DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "Certificate": "CertificateDetailTypeDef",
    },
    total=False,
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

ExportCertificateResponseTypeDef = TypedDict(
    "ExportCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "PrivateKey": str,
    },
    total=False,
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

GetAccountConfigurationResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseTypeDef",
    {
        "ExpiryEvents": "ExpiryEventsConfigurationTypeDef",
    },
    total=False,
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
    },
    total=False,
)

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "CertificateArn": str,
    },
    total=False,
)

KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "Name": KeyUsageNameType,
    },
    total=False,
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "NextToken": str,
        "CertificateSummaryList": List["CertificateSummaryTypeDef"],
    },
    total=False,
)

ListTagsForCertificateResponseTypeDef = TypedDict(
    "ListTagsForCertificateResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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


RequestCertificateResponseTypeDef = TypedDict(
    "RequestCertificateResponseTypeDef",
    {
        "CertificateArn": str,
    },
    total=False,
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Name": str,
        "Type": Literal["CNAME"],
        "Value": str,
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


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
