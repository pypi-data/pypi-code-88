"""
Type annotations for route53domains service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53domains.type_defs import AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef

    data: AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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
    "AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef",
    "AcceptDomainTransferFromAnotherAwsAccountResponseResponseTypeDef",
    "BillingRecordTypeDef",
    "CancelDomainTransferToAnotherAwsAccountRequestTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseResponseTypeDef",
    "CheckDomainAvailabilityRequestTypeDef",
    "CheckDomainAvailabilityResponseResponseTypeDef",
    "CheckDomainTransferabilityRequestTypeDef",
    "CheckDomainTransferabilityResponseResponseTypeDef",
    "ContactDetailTypeDef",
    "DeleteTagsForDomainRequestTypeDef",
    "DisableDomainAutoRenewRequestTypeDef",
    "DisableDomainTransferLockRequestTypeDef",
    "DisableDomainTransferLockResponseResponseTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "DomainTransferabilityTypeDef",
    "EnableDomainAutoRenewRequestTypeDef",
    "EnableDomainTransferLockRequestTypeDef",
    "EnableDomainTransferLockResponseResponseTypeDef",
    "ExtraParamTypeDef",
    "GetContactReachabilityStatusRequestTypeDef",
    "GetContactReachabilityStatusResponseResponseTypeDef",
    "GetDomainDetailRequestTypeDef",
    "GetDomainDetailResponseResponseTypeDef",
    "GetDomainSuggestionsRequestTypeDef",
    "GetDomainSuggestionsResponseResponseTypeDef",
    "GetOperationDetailRequestTypeDef",
    "GetOperationDetailResponseResponseTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseResponseTypeDef",
    "ListOperationsRequestTypeDef",
    "ListOperationsResponseResponseTypeDef",
    "ListTagsForDomainRequestTypeDef",
    "ListTagsForDomainResponseResponseTypeDef",
    "NameserverTypeDef",
    "OperationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterDomainRequestTypeDef",
    "RegisterDomainResponseResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountRequestTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseResponseTypeDef",
    "RenewDomainRequestTypeDef",
    "RenewDomainResponseResponseTypeDef",
    "ResendContactReachabilityEmailRequestTypeDef",
    "ResendContactReachabilityEmailResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveDomainAuthCodeRequestTypeDef",
    "RetrieveDomainAuthCodeResponseResponseTypeDef",
    "TagTypeDef",
    "TransferDomainRequestTypeDef",
    "TransferDomainResponseResponseTypeDef",
    "TransferDomainToAnotherAwsAccountRequestTypeDef",
    "TransferDomainToAnotherAwsAccountResponseResponseTypeDef",
    "UpdateDomainContactPrivacyRequestTypeDef",
    "UpdateDomainContactPrivacyResponseResponseTypeDef",
    "UpdateDomainContactRequestTypeDef",
    "UpdateDomainContactResponseResponseTypeDef",
    "UpdateDomainNameserversRequestTypeDef",
    "UpdateDomainNameserversResponseResponseTypeDef",
    "UpdateTagsForDomainRequestTypeDef",
    "ViewBillingRequestTypeDef",
    "ViewBillingResponseResponseTypeDef",
)

AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef",
    {
        "DomainName": str,
        "Password": str,
    },
)

AcceptDomainTransferFromAnotherAwsAccountResponseResponseTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

CancelDomainTransferToAnotherAwsAccountRequestTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelDomainTransferToAnotherAwsAccountResponseResponseTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCheckDomainAvailabilityRequestTypeDef = TypedDict(
    "_RequiredCheckDomainAvailabilityRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCheckDomainAvailabilityRequestTypeDef = TypedDict(
    "_OptionalCheckDomainAvailabilityRequestTypeDef",
    {
        "IdnLangCode": str,
    },
    total=False,
)


class CheckDomainAvailabilityRequestTypeDef(
    _RequiredCheckDomainAvailabilityRequestTypeDef, _OptionalCheckDomainAvailabilityRequestTypeDef
):
    pass


CheckDomainAvailabilityResponseResponseTypeDef = TypedDict(
    "CheckDomainAvailabilityResponseResponseTypeDef",
    {
        "Availability": DomainAvailabilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCheckDomainTransferabilityRequestTypeDef = TypedDict(
    "_RequiredCheckDomainTransferabilityRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCheckDomainTransferabilityRequestTypeDef = TypedDict(
    "_OptionalCheckDomainTransferabilityRequestTypeDef",
    {
        "AuthCode": str,
    },
    total=False,
)


class CheckDomainTransferabilityRequestTypeDef(
    _RequiredCheckDomainTransferabilityRequestTypeDef,
    _OptionalCheckDomainTransferabilityRequestTypeDef,
):
    pass


CheckDomainTransferabilityResponseResponseTypeDef = TypedDict(
    "CheckDomainTransferabilityResponseResponseTypeDef",
    {
        "Transferability": "DomainTransferabilityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeleteTagsForDomainRequestTypeDef = TypedDict(
    "DeleteTagsForDomainRequestTypeDef",
    {
        "DomainName": str,
        "TagsToDelete": List[str],
    },
)

DisableDomainAutoRenewRequestTypeDef = TypedDict(
    "DisableDomainAutoRenewRequestTypeDef",
    {
        "DomainName": str,
    },
)

DisableDomainTransferLockRequestTypeDef = TypedDict(
    "DisableDomainTransferLockRequestTypeDef",
    {
        "DomainName": str,
    },
)

DisableDomainTransferLockResponseResponseTypeDef = TypedDict(
    "DisableDomainTransferLockResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

EnableDomainAutoRenewRequestTypeDef = TypedDict(
    "EnableDomainAutoRenewRequestTypeDef",
    {
        "DomainName": str,
    },
)

EnableDomainTransferLockRequestTypeDef = TypedDict(
    "EnableDomainTransferLockRequestTypeDef",
    {
        "DomainName": str,
    },
)

EnableDomainTransferLockResponseResponseTypeDef = TypedDict(
    "EnableDomainTransferLockResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExtraParamTypeDef = TypedDict(
    "ExtraParamTypeDef",
    {
        "Name": ExtraParamNameType,
        "Value": str,
    },
)

GetContactReachabilityStatusRequestTypeDef = TypedDict(
    "GetContactReachabilityStatusRequestTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

GetContactReachabilityStatusResponseResponseTypeDef = TypedDict(
    "GetContactReachabilityStatusResponseResponseTypeDef",
    {
        "domainName": str,
        "status": ReachabilityStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainDetailRequestTypeDef = TypedDict(
    "GetDomainDetailRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainDetailResponseResponseTypeDef = TypedDict(
    "GetDomainDetailResponseResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List["NameserverTypeDef"],
        "AutoRenew": bool,
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainSuggestionsRequestTypeDef = TypedDict(
    "GetDomainSuggestionsRequestTypeDef",
    {
        "DomainName": str,
        "SuggestionCount": int,
        "OnlyAvailable": bool,
    },
)

GetDomainSuggestionsResponseResponseTypeDef = TypedDict(
    "GetDomainSuggestionsResponseResponseTypeDef",
    {
        "SuggestionsList": List["DomainSuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationDetailRequestTypeDef = TypedDict(
    "GetOperationDetailRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationDetailResponseResponseTypeDef = TypedDict(
    "GetOperationDetailResponseResponseTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Message": str,
        "DomainName": str,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestTypeDef = TypedDict(
    "ListDomainsRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListDomainsResponseResponseTypeDef = TypedDict(
    "ListDomainsResponseResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
        "NextPageMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsRequestTypeDef = TypedDict(
    "ListOperationsRequestTypeDef",
    {
        "SubmittedSince": Union[datetime, str],
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListOperationsResponseResponseTypeDef = TypedDict(
    "ListOperationsResponseResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
        "NextPageMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForDomainRequestTypeDef = TypedDict(
    "ListTagsForDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

ListTagsForDomainResponseResponseTypeDef = TypedDict(
    "ListTagsForDomainResponseResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredRegisterDomainRequestTypeDef = TypedDict(
    "_RequiredRegisterDomainRequestTypeDef",
    {
        "DomainName": str,
        "DurationInYears": int,
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
)
_OptionalRegisterDomainRequestTypeDef = TypedDict(
    "_OptionalRegisterDomainRequestTypeDef",
    {
        "IdnLangCode": str,
        "AutoRenew": bool,
        "PrivacyProtectAdminContact": bool,
        "PrivacyProtectRegistrantContact": bool,
        "PrivacyProtectTechContact": bool,
    },
    total=False,
)


class RegisterDomainRequestTypeDef(
    _RequiredRegisterDomainRequestTypeDef, _OptionalRegisterDomainRequestTypeDef
):
    pass


RegisterDomainResponseResponseTypeDef = TypedDict(
    "RegisterDomainResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectDomainTransferFromAnotherAwsAccountRequestTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountRequestTypeDef",
    {
        "DomainName": str,
    },
)

RejectDomainTransferFromAnotherAwsAccountResponseResponseTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRenewDomainRequestTypeDef = TypedDict(
    "_RequiredRenewDomainRequestTypeDef",
    {
        "DomainName": str,
        "CurrentExpiryYear": int,
    },
)
_OptionalRenewDomainRequestTypeDef = TypedDict(
    "_OptionalRenewDomainRequestTypeDef",
    {
        "DurationInYears": int,
    },
    total=False,
)


class RenewDomainRequestTypeDef(
    _RequiredRenewDomainRequestTypeDef, _OptionalRenewDomainRequestTypeDef
):
    pass


RenewDomainResponseResponseTypeDef = TypedDict(
    "RenewDomainResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResendContactReachabilityEmailRequestTypeDef = TypedDict(
    "ResendContactReachabilityEmailRequestTypeDef",
    {
        "domainName": str,
    },
    total=False,
)

ResendContactReachabilityEmailResponseResponseTypeDef = TypedDict(
    "ResendContactReachabilityEmailResponseResponseTypeDef",
    {
        "domainName": str,
        "emailAddress": str,
        "isAlreadyVerified": bool,
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

RetrieveDomainAuthCodeRequestTypeDef = TypedDict(
    "RetrieveDomainAuthCodeRequestTypeDef",
    {
        "DomainName": str,
    },
)

RetrieveDomainAuthCodeResponseResponseTypeDef = TypedDict(
    "RetrieveDomainAuthCodeResponseResponseTypeDef",
    {
        "AuthCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredTransferDomainRequestTypeDef = TypedDict(
    "_RequiredTransferDomainRequestTypeDef",
    {
        "DomainName": str,
        "DurationInYears": int,
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
)
_OptionalTransferDomainRequestTypeDef = TypedDict(
    "_OptionalTransferDomainRequestTypeDef",
    {
        "IdnLangCode": str,
        "Nameservers": List["NameserverTypeDef"],
        "AuthCode": str,
        "AutoRenew": bool,
        "PrivacyProtectAdminContact": bool,
        "PrivacyProtectRegistrantContact": bool,
        "PrivacyProtectTechContact": bool,
    },
    total=False,
)


class TransferDomainRequestTypeDef(
    _RequiredTransferDomainRequestTypeDef, _OptionalTransferDomainRequestTypeDef
):
    pass


TransferDomainResponseResponseTypeDef = TypedDict(
    "TransferDomainResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TransferDomainToAnotherAwsAccountRequestTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountRequestTypeDef",
    {
        "DomainName": str,
        "AccountId": str,
    },
)

TransferDomainToAnotherAwsAccountResponseResponseTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountResponseResponseTypeDef",
    {
        "OperationId": str,
        "Password": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainContactPrivacyRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainContactPrivacyRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainContactPrivacyRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainContactPrivacyRequestTypeDef",
    {
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
    },
    total=False,
)


class UpdateDomainContactPrivacyRequestTypeDef(
    _RequiredUpdateDomainContactPrivacyRequestTypeDef,
    _OptionalUpdateDomainContactPrivacyRequestTypeDef,
):
    pass


UpdateDomainContactPrivacyResponseResponseTypeDef = TypedDict(
    "UpdateDomainContactPrivacyResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainContactRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainContactRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainContactRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainContactRequestTypeDef",
    {
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
    total=False,
)


class UpdateDomainContactRequestTypeDef(
    _RequiredUpdateDomainContactRequestTypeDef, _OptionalUpdateDomainContactRequestTypeDef
):
    pass


UpdateDomainContactResponseResponseTypeDef = TypedDict(
    "UpdateDomainContactResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainNameserversRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameserversRequestTypeDef",
    {
        "DomainName": str,
        "Nameservers": List["NameserverTypeDef"],
    },
)
_OptionalUpdateDomainNameserversRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameserversRequestTypeDef",
    {
        "FIAuthKey": str,
    },
    total=False,
)


class UpdateDomainNameserversRequestTypeDef(
    _RequiredUpdateDomainNameserversRequestTypeDef, _OptionalUpdateDomainNameserversRequestTypeDef
):
    pass


UpdateDomainNameserversResponseResponseTypeDef = TypedDict(
    "UpdateDomainNameserversResponseResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTagsForDomainRequestTypeDef = TypedDict(
    "_RequiredUpdateTagsForDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateTagsForDomainRequestTypeDef = TypedDict(
    "_OptionalUpdateTagsForDomainRequestTypeDef",
    {
        "TagsToUpdate": List["TagTypeDef"],
    },
    total=False,
)


class UpdateTagsForDomainRequestTypeDef(
    _RequiredUpdateTagsForDomainRequestTypeDef, _OptionalUpdateTagsForDomainRequestTypeDef
):
    pass


ViewBillingRequestTypeDef = TypedDict(
    "ViewBillingRequestTypeDef",
    {
        "Start": Union[datetime, str],
        "End": Union[datetime, str],
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ViewBillingResponseResponseTypeDef = TypedDict(
    "ViewBillingResponseResponseTypeDef",
    {
        "NextPageMarker": str,
        "BillingRecords": List["BillingRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
