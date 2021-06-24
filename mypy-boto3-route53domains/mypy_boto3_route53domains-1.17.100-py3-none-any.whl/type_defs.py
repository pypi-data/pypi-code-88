"""
Type annotations for route53domains service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53domains.type_defs import AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef

    data: AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    ContactTypeType,
    CountryCodeType,
    DomainAvailabilityType,
    ExtraParamNameType,
    OperationStatusType,
    OperationTypeType,
    ReachabilityStatusType,
    TransferableType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "BillingRecordTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    "CheckDomainAvailabilityResponseTypeDef",
    "CheckDomainTransferabilityResponseTypeDef",
    "ContactDetailTypeDef",
    "DisableDomainTransferLockResponseTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "DomainTransferabilityTypeDef",
    "EnableDomainTransferLockResponseTypeDef",
    "ExtraParamTypeDef",
    "GetContactReachabilityStatusResponseTypeDef",
    "GetDomainDetailResponseTypeDef",
    "GetDomainSuggestionsResponseTypeDef",
    "GetOperationDetailResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListTagsForDomainResponseTypeDef",
    "NameserverTypeDef",
    "OperationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterDomainResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "RenewDomainResponseTypeDef",
    "ResendContactReachabilityEmailResponseTypeDef",
    "RetrieveDomainAuthCodeResponseTypeDef",
    "TagTypeDef",
    "TransferDomainResponseTypeDef",
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    "UpdateDomainContactPrivacyResponseTypeDef",
    "UpdateDomainContactResponseTypeDef",
    "UpdateDomainNameserversResponseTypeDef",
    "ViewBillingResponseTypeDef",
)

AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

BillingRecordTypeDef = TypedDict(
    "BillingRecordTypeDef",
    {
        "DomainName": str,
        "Operation": OperationTypeType,
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)

CancelDomainTransferToAnotherAwsAccountResponseTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

CheckDomainAvailabilityResponseTypeDef = TypedDict(
    "CheckDomainAvailabilityResponseTypeDef",
    {
        "Availability": DomainAvailabilityType,
    },
)

CheckDomainTransferabilityResponseTypeDef = TypedDict(
    "CheckDomainTransferabilityResponseTypeDef",
    {
        "Transferability": "DomainTransferabilityTypeDef",
    },
)

ContactDetailTypeDef = TypedDict(
    "ContactDetailTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": ContactTypeType,
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": CountryCodeType,
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List["ExtraParamTypeDef"],
    },
    total=False,
)

DisableDomainTransferLockResponseTypeDef = TypedDict(
    "DisableDomainTransferLockResponseTypeDef",
    {
        "OperationId": str,
    },
)

DomainSuggestionTypeDef = TypedDict(
    "DomainSuggestionTypeDef",
    {
        "DomainName": str,
        "Availability": str,
    },
    total=False,
)

_RequiredDomainSummaryTypeDef = TypedDict(
    "_RequiredDomainSummaryTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainSummaryTypeDef = TypedDict(
    "_OptionalDomainSummaryTypeDef",
    {
        "AutoRenew": bool,
        "TransferLock": bool,
        "Expiry": datetime,
    },
    total=False,
)


class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, _OptionalDomainSummaryTypeDef):
    pass


DomainTransferabilityTypeDef = TypedDict(
    "DomainTransferabilityTypeDef",
    {
        "Transferable": TransferableType,
    },
    total=False,
)

EnableDomainTransferLockResponseTypeDef = TypedDict(
    "EnableDomainTransferLockResponseTypeDef",
    {
        "OperationId": str,
    },
)

ExtraParamTypeDef = TypedDict(
    "ExtraParamTypeDef",
    {
        "Name": ExtraParamNameType,
        "Value": str,
    },
)

GetContactReachabilityStatusResponseTypeDef = TypedDict(
    "GetContactReachabilityStatusResponseTypeDef",
    {
        "domainName": str,
        "status": ReachabilityStatusType,
    },
    total=False,
)

_RequiredGetDomainDetailResponseTypeDef = TypedDict(
    "_RequiredGetDomainDetailResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List["NameserverTypeDef"],
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
)
_OptionalGetDomainDetailResponseTypeDef = TypedDict(
    "_OptionalGetDomainDetailResponseTypeDef",
    {
        "AutoRenew": bool,
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
        "RegistrarName": str,
        "WhoIsServer": str,
        "RegistrarUrl": str,
        "AbuseContactEmail": str,
        "AbuseContactPhone": str,
        "RegistryDomainId": str,
        "CreationDate": datetime,
        "UpdatedDate": datetime,
        "ExpirationDate": datetime,
        "Reseller": str,
        "DnsSec": str,
        "StatusList": List[str],
    },
    total=False,
)


class GetDomainDetailResponseTypeDef(
    _RequiredGetDomainDetailResponseTypeDef, _OptionalGetDomainDetailResponseTypeDef
):
    pass


GetDomainSuggestionsResponseTypeDef = TypedDict(
    "GetDomainSuggestionsResponseTypeDef",
    {
        "SuggestionsList": List["DomainSuggestionTypeDef"],
    },
    total=False,
)

GetOperationDetailResponseTypeDef = TypedDict(
    "GetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Message": str,
        "DomainName": str,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
    },
    total=False,
)

_RequiredListDomainsResponseTypeDef = TypedDict(
    "_RequiredListDomainsResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
    },
)
_OptionalListDomainsResponseTypeDef = TypedDict(
    "_OptionalListDomainsResponseTypeDef",
    {
        "NextPageMarker": str,
    },
    total=False,
)


class ListDomainsResponseTypeDef(
    _RequiredListDomainsResponseTypeDef, _OptionalListDomainsResponseTypeDef
):
    pass


_RequiredListOperationsResponseTypeDef = TypedDict(
    "_RequiredListOperationsResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
    },
)
_OptionalListOperationsResponseTypeDef = TypedDict(
    "_OptionalListOperationsResponseTypeDef",
    {
        "NextPageMarker": str,
    },
    total=False,
)


class ListOperationsResponseTypeDef(
    _RequiredListOperationsResponseTypeDef, _OptionalListOperationsResponseTypeDef
):
    pass


ListTagsForDomainResponseTypeDef = TypedDict(
    "ListTagsForDomainResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
)

_RequiredNameserverTypeDef = TypedDict(
    "_RequiredNameserverTypeDef",
    {
        "Name": str,
    },
)
_OptionalNameserverTypeDef = TypedDict(
    "_OptionalNameserverTypeDef",
    {
        "GlueIps": List[str],
    },
    total=False,
)


class NameserverTypeDef(_RequiredNameserverTypeDef, _OptionalNameserverTypeDef):
    pass


OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
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

RegisterDomainResponseTypeDef = TypedDict(
    "RegisterDomainResponseTypeDef",
    {
        "OperationId": str,
    },
)

RejectDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
    },
    total=False,
)

RenewDomainResponseTypeDef = TypedDict(
    "RenewDomainResponseTypeDef",
    {
        "OperationId": str,
    },
)

ResendContactReachabilityEmailResponseTypeDef = TypedDict(
    "ResendContactReachabilityEmailResponseTypeDef",
    {
        "domainName": str,
        "emailAddress": str,
        "isAlreadyVerified": bool,
    },
    total=False,
)

RetrieveDomainAuthCodeResponseTypeDef = TypedDict(
    "RetrieveDomainAuthCodeResponseTypeDef",
    {
        "AuthCode": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TransferDomainResponseTypeDef = TypedDict(
    "TransferDomainResponseTypeDef",
    {
        "OperationId": str,
    },
)

TransferDomainToAnotherAwsAccountResponseTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "Password": str,
    },
    total=False,
)

UpdateDomainContactPrivacyResponseTypeDef = TypedDict(
    "UpdateDomainContactPrivacyResponseTypeDef",
    {
        "OperationId": str,
    },
)

UpdateDomainContactResponseTypeDef = TypedDict(
    "UpdateDomainContactResponseTypeDef",
    {
        "OperationId": str,
    },
)

UpdateDomainNameserversResponseTypeDef = TypedDict(
    "UpdateDomainNameserversResponseTypeDef",
    {
        "OperationId": str,
    },
)

ViewBillingResponseTypeDef = TypedDict(
    "ViewBillingResponseTypeDef",
    {
        "NextPageMarker": str,
        "BillingRecords": List["BillingRecordTypeDef"],
    },
    total=False,
)
