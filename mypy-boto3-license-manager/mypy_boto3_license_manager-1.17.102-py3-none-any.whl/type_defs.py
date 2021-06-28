"""
Type annotations for license-manager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantRequestTypeDef

    data: AcceptGrantRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AllowedOperationType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
    LicenseConfigurationStatusType,
    LicenseCountingTypeType,
    LicenseDeletionStatusType,
    LicenseStatusType,
    ReceivedStatusType,
    RenewTypeType,
    ReportFrequencyTypeType,
    ReportTypeType,
    ResourceTypeType,
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
    "AcceptGrantRequestTypeDef",
    "AcceptGrantResponseResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckInLicenseRequestTypeDef",
    "CheckoutBorrowLicenseRequestTypeDef",
    "CheckoutBorrowLicenseResponseResponseTypeDef",
    "CheckoutLicenseRequestTypeDef",
    "CheckoutLicenseResponseResponseTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantRequestTypeDef",
    "CreateGrantResponseResponseTypeDef",
    "CreateGrantVersionRequestTypeDef",
    "CreateGrantVersionResponseResponseTypeDef",
    "CreateLicenseConfigurationRequestTypeDef",
    "CreateLicenseConfigurationResponseResponseTypeDef",
    "CreateLicenseManagerReportGeneratorRequestTypeDef",
    "CreateLicenseManagerReportGeneratorResponseResponseTypeDef",
    "CreateLicenseRequestTypeDef",
    "CreateLicenseResponseResponseTypeDef",
    "CreateLicenseVersionRequestTypeDef",
    "CreateLicenseVersionResponseResponseTypeDef",
    "CreateTokenRequestTypeDef",
    "CreateTokenResponseResponseTypeDef",
    "DatetimeRangeTypeDef",
    "DeleteGrantRequestTypeDef",
    "DeleteGrantResponseResponseTypeDef",
    "DeleteLicenseConfigurationRequestTypeDef",
    "DeleteLicenseManagerReportGeneratorRequestTypeDef",
    "DeleteLicenseRequestTypeDef",
    "DeleteLicenseResponseResponseTypeDef",
    "DeleteTokenRequestTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionRequestTypeDef",
    "ExtendLicenseConsumptionResponseResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenRequestTypeDef",
    "GetAccessTokenResponseResponseTypeDef",
    "GetGrantRequestTypeDef",
    "GetGrantResponseResponseTypeDef",
    "GetLicenseConfigurationRequestTypeDef",
    "GetLicenseConfigurationResponseResponseTypeDef",
    "GetLicenseManagerReportGeneratorRequestTypeDef",
    "GetLicenseManagerReportGeneratorResponseResponseTypeDef",
    "GetLicenseRequestTypeDef",
    "GetLicenseResponseResponseTypeDef",
    "GetLicenseUsageRequestTypeDef",
    "GetLicenseUsageResponseResponseTypeDef",
    "GetServiceSettingsResponseResponseTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "InventoryFilterTypeDef",
    "IssuerDetailsTypeDef",
    "IssuerTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ListAssociationsForLicenseConfigurationRequestTypeDef",
    "ListAssociationsForLicenseConfigurationResponseResponseTypeDef",
    "ListDistributedGrantsRequestTypeDef",
    "ListDistributedGrantsResponseResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsRequestTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseResponseTypeDef",
    "ListLicenseConfigurationsRequestTypeDef",
    "ListLicenseConfigurationsResponseResponseTypeDef",
    "ListLicenseManagerReportGeneratorsRequestTypeDef",
    "ListLicenseManagerReportGeneratorsResponseResponseTypeDef",
    "ListLicenseSpecificationsForResourceRequestTypeDef",
    "ListLicenseSpecificationsForResourceResponseResponseTypeDef",
    "ListLicenseVersionsRequestTypeDef",
    "ListLicenseVersionsResponseResponseTypeDef",
    "ListLicensesRequestTypeDef",
    "ListLicensesResponseResponseTypeDef",
    "ListReceivedGrantsRequestTypeDef",
    "ListReceivedGrantsResponseResponseTypeDef",
    "ListReceivedLicensesRequestTypeDef",
    "ListReceivedLicensesResponseResponseTypeDef",
    "ListResourceInventoryRequestTypeDef",
    "ListResourceInventoryResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTokensRequestTypeDef",
    "ListTokensResponseResponseTypeDef",
    "ListUsageForLicenseConfigurationRequestTypeDef",
    "ListUsageForLicenseConfigurationResponseResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "RejectGrantRequestTypeDef",
    "RejectGrantResponseResponseTypeDef",
    "ReportContextTypeDef",
    "ReportFrequencyTypeDef",
    "ReportGeneratorTypeDef",
    "ResourceInventoryTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLicenseConfigurationRequestTypeDef",
    "UpdateLicenseManagerReportGeneratorRequestTypeDef",
    "UpdateLicenseSpecificationsForResourceRequestTypeDef",
    "UpdateServiceSettingsRequestTypeDef",
)

AcceptGrantRequestTypeDef = TypedDict(
    "AcceptGrantRequestTypeDef",
    {
        "GrantArn": str,
    },
)

AcceptGrantResponseResponseTypeDef = TypedDict(
    "AcceptGrantResponseResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef",
    {
        "LastRunTime": datetime,
    },
    total=False,
)

BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef",
    {
        "AllowEarlyCheckIn": bool,
        "MaxTimeToLiveInMinutes": int,
    },
)

_RequiredCheckInLicenseRequestTypeDef = TypedDict(
    "_RequiredCheckInLicenseRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
    },
)
_OptionalCheckInLicenseRequestTypeDef = TypedDict(
    "_OptionalCheckInLicenseRequestTypeDef",
    {
        "Beneficiary": str,
    },
    total=False,
)


class CheckInLicenseRequestTypeDef(
    _RequiredCheckInLicenseRequestTypeDef, _OptionalCheckInLicenseRequestTypeDef
):
    pass


_RequiredCheckoutBorrowLicenseRequestTypeDef = TypedDict(
    "_RequiredCheckoutBorrowLicenseRequestTypeDef",
    {
        "LicenseArn": str,
        "Entitlements": List["EntitlementDataTypeDef"],
        "DigitalSignatureMethod": Literal["JWT_PS384"],
        "ClientToken": str,
    },
)
_OptionalCheckoutBorrowLicenseRequestTypeDef = TypedDict(
    "_OptionalCheckoutBorrowLicenseRequestTypeDef",
    {
        "NodeId": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
    },
    total=False,
)


class CheckoutBorrowLicenseRequestTypeDef(
    _RequiredCheckoutBorrowLicenseRequestTypeDef, _OptionalCheckoutBorrowLicenseRequestTypeDef
):
    pass


CheckoutBorrowLicenseResponseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCheckoutLicenseRequestTypeDef = TypedDict(
    "_RequiredCheckoutLicenseRequestTypeDef",
    {
        "ProductSKU": str,
        "CheckoutType": Literal["PROVISIONAL"],
        "KeyFingerprint": str,
        "Entitlements": List["EntitlementDataTypeDef"],
        "ClientToken": str,
    },
)
_OptionalCheckoutLicenseRequestTypeDef = TypedDict(
    "_OptionalCheckoutLicenseRequestTypeDef",
    {
        "Beneficiary": str,
        "NodeId": str,
    },
    total=False,
)


class CheckoutLicenseRequestTypeDef(
    _RequiredCheckoutLicenseRequestTypeDef, _OptionalCheckoutLicenseRequestTypeDef
):
    pass


CheckoutLicenseResponseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseResponseTypeDef",
    {
        "CheckoutType": Literal["PROVISIONAL"],
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "ConsumedLicenses": int,
    },
    total=False,
)

ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": RenewTypeType,
        "ProvisionalConfiguration": "ProvisionalConfigurationTypeDef",
        "BorrowConfiguration": "BorrowConfigurationTypeDef",
    },
    total=False,
)

CreateGrantRequestTypeDef = TypedDict(
    "CreateGrantRequestTypeDef",
    {
        "ClientToken": str,
        "GrantName": str,
        "LicenseArn": str,
        "Principals": List[str],
        "HomeRegion": str,
        "AllowedOperations": List[AllowedOperationType],
    },
)

CreateGrantResponseResponseTypeDef = TypedDict(
    "CreateGrantResponseResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGrantVersionRequestTypeDef = TypedDict(
    "_RequiredCreateGrantVersionRequestTypeDef",
    {
        "ClientToken": str,
        "GrantArn": str,
    },
)
_OptionalCreateGrantVersionRequestTypeDef = TypedDict(
    "_OptionalCreateGrantVersionRequestTypeDef",
    {
        "GrantName": str,
        "AllowedOperations": List[AllowedOperationType],
        "Status": GrantStatusType,
        "StatusReason": str,
        "SourceVersion": str,
    },
    total=False,
)


class CreateGrantVersionRequestTypeDef(
    _RequiredCreateGrantVersionRequestTypeDef, _OptionalCreateGrantVersionRequestTypeDef
):
    pass


CreateGrantVersionResponseResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseConfigurationRequestTypeDef",
    {
        "Name": str,
        "LicenseCountingType": LicenseCountingTypeType,
    },
)
_OptionalCreateLicenseConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseConfigurationRequestTypeDef",
    {
        "Description": str,
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "LicenseRules": List[str],
        "Tags": List["TagTypeDef"],
        "DisassociateWhenNotFound": bool,
        "ProductInformationList": List["ProductInformationTypeDef"],
    },
    total=False,
)


class CreateLicenseConfigurationRequestTypeDef(
    _RequiredCreateLicenseConfigurationRequestTypeDef,
    _OptionalCreateLicenseConfigurationRequestTypeDef,
):
    pass


CreateLicenseConfigurationResponseResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseManagerReportGeneratorRequestTypeDef",
    {
        "ReportGeneratorName": str,
        "Type": List[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseManagerReportGeneratorRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateLicenseManagerReportGeneratorRequestTypeDef(
    _RequiredCreateLicenseManagerReportGeneratorRequestTypeDef,
    _OptionalCreateLicenseManagerReportGeneratorRequestTypeDef,
):
    pass


CreateLicenseManagerReportGeneratorResponseResponseTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorResponseResponseTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseRequestTypeDef",
    {
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerTypeDef",
        "HomeRegion": str,
        "Validity": "DatetimeRangeTypeDef",
        "Entitlements": List["EntitlementTypeDef"],
        "Beneficiary": str,
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateLicenseRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseRequestTypeDef",
    {
        "LicenseMetadata": List["MetadataTypeDef"],
    },
    total=False,
)


class CreateLicenseRequestTypeDef(
    _RequiredCreateLicenseRequestTypeDef, _OptionalCreateLicenseRequestTypeDef
):
    pass


CreateLicenseResponseResponseTypeDef = TypedDict(
    "CreateLicenseResponseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": LicenseStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseVersionRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseVersionRequestTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "Issuer": "IssuerTypeDef",
        "HomeRegion": str,
        "Validity": "DatetimeRangeTypeDef",
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "Status": LicenseStatusType,
        "ClientToken": str,
    },
)
_OptionalCreateLicenseVersionRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseVersionRequestTypeDef",
    {
        "LicenseMetadata": List["MetadataTypeDef"],
        "SourceVersion": str,
    },
    total=False,
)


class CreateLicenseVersionRequestTypeDef(
    _RequiredCreateLicenseVersionRequestTypeDef, _OptionalCreateLicenseVersionRequestTypeDef
):
    pass


CreateLicenseVersionResponseResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": LicenseStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTokenRequestTypeDef = TypedDict(
    "_RequiredCreateTokenRequestTypeDef",
    {
        "LicenseArn": str,
        "ClientToken": str,
    },
)
_OptionalCreateTokenRequestTypeDef = TypedDict(
    "_OptionalCreateTokenRequestTypeDef",
    {
        "RoleArns": List[str],
        "ExpirationInDays": int,
        "TokenProperties": List[str],
    },
    total=False,
)


class CreateTokenRequestTypeDef(
    _RequiredCreateTokenRequestTypeDef, _OptionalCreateTokenRequestTypeDef
):
    pass


CreateTokenResponseResponseTypeDef = TypedDict(
    "CreateTokenResponseResponseTypeDef",
    {
        "TokenId": str,
        "TokenType": Literal["REFRESH_TOKEN"],
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDatetimeRangeTypeDef = TypedDict(
    "_RequiredDatetimeRangeTypeDef",
    {
        "Begin": str,
    },
)
_OptionalDatetimeRangeTypeDef = TypedDict(
    "_OptionalDatetimeRangeTypeDef",
    {
        "End": str,
    },
    total=False,
)


class DatetimeRangeTypeDef(_RequiredDatetimeRangeTypeDef, _OptionalDatetimeRangeTypeDef):
    pass


_RequiredDeleteGrantRequestTypeDef = TypedDict(
    "_RequiredDeleteGrantRequestTypeDef",
    {
        "GrantArn": str,
        "Version": str,
    },
)
_OptionalDeleteGrantRequestTypeDef = TypedDict(
    "_OptionalDeleteGrantRequestTypeDef",
    {
        "StatusReason": str,
    },
    total=False,
)


class DeleteGrantRequestTypeDef(
    _RequiredDeleteGrantRequestTypeDef, _OptionalDeleteGrantRequestTypeDef
):
    pass


DeleteGrantResponseResponseTypeDef = TypedDict(
    "DeleteGrantResponseResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLicenseConfigurationRequestTypeDef = TypedDict(
    "DeleteLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

DeleteLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "DeleteLicenseManagerReportGeneratorRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

DeleteLicenseRequestTypeDef = TypedDict(
    "DeleteLicenseRequestTypeDef",
    {
        "LicenseArn": str,
        "SourceVersion": str,
    },
)

DeleteLicenseResponseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseResponseTypeDef",
    {
        "Status": LicenseDeletionStatusType,
        "DeletionDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestTypeDef = TypedDict(
    "DeleteTokenRequestTypeDef",
    {
        "TokenId": str,
    },
)

_RequiredEntitlementDataTypeDef = TypedDict(
    "_RequiredEntitlementDataTypeDef",
    {
        "Name": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementDataTypeDef = TypedDict(
    "_OptionalEntitlementDataTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class EntitlementDataTypeDef(_RequiredEntitlementDataTypeDef, _OptionalEntitlementDataTypeDef):
    pass


_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "Name": str,
        "Unit": EntitlementUnitType,
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "Value": str,
        "MaxCount": int,
        "Overage": bool,
        "AllowCheckIn": bool,
    },
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


_RequiredEntitlementUsageTypeDef = TypedDict(
    "_RequiredEntitlementUsageTypeDef",
    {
        "Name": str,
        "ConsumedValue": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementUsageTypeDef = TypedDict(
    "_OptionalEntitlementUsageTypeDef",
    {
        "MaxCount": str,
    },
    total=False,
)


class EntitlementUsageTypeDef(_RequiredEntitlementUsageTypeDef, _OptionalEntitlementUsageTypeDef):
    pass


_RequiredExtendLicenseConsumptionRequestTypeDef = TypedDict(
    "_RequiredExtendLicenseConsumptionRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
    },
)
_OptionalExtendLicenseConsumptionRequestTypeDef = TypedDict(
    "_OptionalExtendLicenseConsumptionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ExtendLicenseConsumptionRequestTypeDef(
    _RequiredExtendLicenseConsumptionRequestTypeDef, _OptionalExtendLicenseConsumptionRequestTypeDef
):
    pass


ExtendLicenseConsumptionResponseResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseResponseTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Expiration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

_RequiredGetAccessTokenRequestTypeDef = TypedDict(
    "_RequiredGetAccessTokenRequestTypeDef",
    {
        "Token": str,
    },
)
_OptionalGetAccessTokenRequestTypeDef = TypedDict(
    "_OptionalGetAccessTokenRequestTypeDef",
    {
        "TokenProperties": List[str],
    },
    total=False,
)


class GetAccessTokenRequestTypeDef(
    _RequiredGetAccessTokenRequestTypeDef, _OptionalGetAccessTokenRequestTypeDef
):
    pass


GetAccessTokenResponseResponseTypeDef = TypedDict(
    "GetAccessTokenResponseResponseTypeDef",
    {
        "AccessToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGrantRequestTypeDef = TypedDict(
    "_RequiredGetGrantRequestTypeDef",
    {
        "GrantArn": str,
    },
)
_OptionalGetGrantRequestTypeDef = TypedDict(
    "_OptionalGetGrantRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetGrantRequestTypeDef(_RequiredGetGrantRequestTypeDef, _OptionalGetGrantRequestTypeDef):
    pass


GetGrantResponseResponseTypeDef = TypedDict(
    "GetGrantResponseResponseTypeDef",
    {
        "Grant": "GrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseConfigurationRequestTypeDef = TypedDict(
    "GetLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

GetLicenseConfigurationResponseResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
        "DisassociateWhenNotFound": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

GetLicenseManagerReportGeneratorResponseResponseTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorResponseResponseTypeDef",
    {
        "ReportGenerator": "ReportGeneratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLicenseRequestTypeDef = TypedDict(
    "_RequiredGetLicenseRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalGetLicenseRequestTypeDef = TypedDict(
    "_OptionalGetLicenseRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetLicenseRequestTypeDef(
    _RequiredGetLicenseRequestTypeDef, _OptionalGetLicenseRequestTypeDef
):
    pass


GetLicenseResponseResponseTypeDef = TypedDict(
    "GetLicenseResponseResponseTypeDef",
    {
        "License": "LicenseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseUsageRequestTypeDef = TypedDict(
    "GetLicenseUsageRequestTypeDef",
    {
        "LicenseArn": str,
    },
)

GetLicenseUsageResponseResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseResponseTypeDef",
    {
        "LicenseUsage": "LicenseUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceSettingsResponseResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrantTypeDef = TypedDict(
    "_RequiredGrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": GrantStatusType,
        "Version": str,
        "GrantedOperations": List[AllowedOperationType],
    },
)
_OptionalGrantTypeDef = TypedDict(
    "_OptionalGrantTypeDef",
    {
        "StatusReason": str,
    },
    total=False,
)


class GrantTypeDef(_RequiredGrantTypeDef, _OptionalGrantTypeDef):
    pass


GrantedLicenseTypeDef = TypedDict(
    "GrantedLicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerDetailsTypeDef",
        "HomeRegion": str,
        "Status": LicenseStatusType,
        "Validity": "DatetimeRangeTypeDef",
        "Beneficiary": str,
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "LicenseMetadata": List["MetadataTypeDef"],
        "CreateTime": str,
        "Version": str,
        "ReceivedMetadata": "ReceivedMetadataTypeDef",
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef",
    {
        "Name": str,
        "Condition": InventoryFilterConditionType,
    },
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef",
    {
        "Name": str,
        "SignKey": str,
        "KeyFingerprint": str,
    },
    total=False,
)

_RequiredIssuerTypeDef = TypedDict(
    "_RequiredIssuerTypeDef",
    {
        "Name": str,
    },
)
_OptionalIssuerTypeDef = TypedDict(
    "_OptionalIssuerTypeDef",
    {
        "SignKey": str,
    },
    total=False,
)


class IssuerTypeDef(_RequiredIssuerTypeDef, _OptionalIssuerTypeDef):
    pass


LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "AmiAssociationScope": str,
    },
    total=False,
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "DisassociateWhenNotFound": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
    },
    total=False,
)

LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

LicenseOperationFailureTypeDef = TypedDict(
    "LicenseOperationFailureTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
        "ErrorMessage": str,
        "FailureTime": datetime,
        "OperationName": str,
        "ResourceOwnerId": str,
        "OperationRequestedBy": str,
        "MetadataList": List["MetadataTypeDef"],
    },
    total=False,
)

_RequiredLicenseSpecificationTypeDef = TypedDict(
    "_RequiredLicenseSpecificationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalLicenseSpecificationTypeDef = TypedDict(
    "_OptionalLicenseSpecificationTypeDef",
    {
        "AmiAssociationScope": str,
    },
    total=False,
)


class LicenseSpecificationTypeDef(
    _RequiredLicenseSpecificationTypeDef, _OptionalLicenseSpecificationTypeDef
):
    pass


LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerDetailsTypeDef",
        "HomeRegion": str,
        "Status": LicenseStatusType,
        "Validity": "DatetimeRangeTypeDef",
        "Beneficiary": str,
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "LicenseMetadata": List["MetadataTypeDef"],
        "CreateTime": str,
        "Version": str,
    },
    total=False,
)

LicenseUsageTypeDef = TypedDict(
    "LicenseUsageTypeDef",
    {
        "EntitlementUsages": List["EntitlementUsageTypeDef"],
    },
    total=False,
)

_RequiredListAssociationsForLicenseConfigurationRequestTypeDef = TypedDict(
    "_RequiredListAssociationsForLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListAssociationsForLicenseConfigurationRequestTypeDef = TypedDict(
    "_OptionalListAssociationsForLicenseConfigurationRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAssociationsForLicenseConfigurationRequestTypeDef(
    _RequiredListAssociationsForLicenseConfigurationRequestTypeDef,
    _OptionalListAssociationsForLicenseConfigurationRequestTypeDef,
):
    pass


ListAssociationsForLicenseConfigurationResponseResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributedGrantsRequestTypeDef = TypedDict(
    "ListDistributedGrantsRequestTypeDef",
    {
        "GrantArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDistributedGrantsResponseResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFailuresForLicenseConfigurationOperationsRequestTypeDef = TypedDict(
    "_RequiredListFailuresForLicenseConfigurationOperationsRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListFailuresForLicenseConfigurationOperationsRequestTypeDef = TypedDict(
    "_OptionalListFailuresForLicenseConfigurationOperationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListFailuresForLicenseConfigurationOperationsRequestTypeDef(
    _RequiredListFailuresForLicenseConfigurationOperationsRequestTypeDef,
    _OptionalListFailuresForLicenseConfigurationOperationsRequestTypeDef,
):
    pass


ListFailuresForLicenseConfigurationOperationsResponseResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseResponseTypeDef",
    {
        "LicenseOperationFailureList": List["LicenseOperationFailureTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseConfigurationsRequestTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestTypeDef",
    {
        "LicenseConfigurationArns": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListLicenseConfigurationsResponseResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseResponseTypeDef",
    {
        "LicenseConfigurations": List["LicenseConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseManagerReportGeneratorsRequestTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLicenseManagerReportGeneratorsResponseResponseTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsResponseResponseTypeDef",
    {
        "ReportGenerators": List["ReportGeneratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLicenseSpecificationsForResourceRequestTypeDef = TypedDict(
    "_RequiredListLicenseSpecificationsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListLicenseSpecificationsForResourceRequestTypeDef = TypedDict(
    "_OptionalListLicenseSpecificationsForResourceRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListLicenseSpecificationsForResourceRequestTypeDef(
    _RequiredListLicenseSpecificationsForResourceRequestTypeDef,
    _OptionalListLicenseSpecificationsForResourceRequestTypeDef,
):
    pass


ListLicenseSpecificationsForResourceResponseResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseResponseTypeDef",
    {
        "LicenseSpecifications": List["LicenseSpecificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLicenseVersionsRequestTypeDef = TypedDict(
    "_RequiredListLicenseVersionsRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalListLicenseVersionsRequestTypeDef = TypedDict(
    "_OptionalListLicenseVersionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLicenseVersionsRequestTypeDef(
    _RequiredListLicenseVersionsRequestTypeDef, _OptionalListLicenseVersionsRequestTypeDef
):
    pass


ListLicenseVersionsResponseResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicensesRequestTypeDef = TypedDict(
    "ListLicensesRequestTypeDef",
    {
        "LicenseArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLicensesResponseResponseTypeDef = TypedDict(
    "ListLicensesResponseResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedGrantsRequestTypeDef = TypedDict(
    "ListReceivedGrantsRequestTypeDef",
    {
        "GrantArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReceivedGrantsResponseResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedLicensesRequestTypeDef = TypedDict(
    "ListReceivedLicensesRequestTypeDef",
    {
        "LicenseArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReceivedLicensesResponseResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseResponseTypeDef",
    {
        "Licenses": List["GrantedLicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceInventoryRequestTypeDef = TypedDict(
    "ListResourceInventoryRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["InventoryFilterTypeDef"],
    },
    total=False,
)

ListResourceInventoryResponseResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseResponseTypeDef",
    {
        "ResourceInventoryList": List["ResourceInventoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTokensRequestTypeDef = TypedDict(
    "ListTokensRequestTypeDef",
    {
        "TokenIds": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTokensResponseResponseTypeDef = TypedDict(
    "ListTokensResponseResponseTypeDef",
    {
        "Tokens": List["TokenDataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsageForLicenseConfigurationRequestTypeDef = TypedDict(
    "_RequiredListUsageForLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListUsageForLicenseConfigurationRequestTypeDef = TypedDict(
    "_OptionalListUsageForLicenseConfigurationRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)


class ListUsageForLicenseConfigurationRequestTypeDef(
    _RequiredListUsageForLicenseConfigurationRequestTypeDef,
    _OptionalListUsageForLicenseConfigurationRequestTypeDef,
):
    pass


ListUsageForLicenseConfigurationResponseResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "AssociationCount": int,
    },
    total=False,
)

MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "EnableIntegration": bool,
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

_RequiredProductInformationFilterTypeDef = TypedDict(
    "_RequiredProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
    },
)
_OptionalProductInformationFilterTypeDef = TypedDict(
    "_OptionalProductInformationFilterTypeDef",
    {
        "ProductInformationFilterValue": List[str],
    },
    total=False,
)


class ProductInformationFilterTypeDef(
    _RequiredProductInformationFilterTypeDef, _OptionalProductInformationFilterTypeDef
):
    pass


ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List["ProductInformationFilterTypeDef"],
    },
)

ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef",
    {
        "MaxTimeToLiveInMinutes": int,
    },
)

ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {
        "ReceivedStatus": ReceivedStatusType,
        "ReceivedStatusReason": str,
        "AllowedOperations": List[AllowedOperationType],
    },
    total=False,
)

RejectGrantRequestTypeDef = TypedDict(
    "RejectGrantRequestTypeDef",
    {
        "GrantArn": str,
    },
)

RejectGrantResponseResponseTypeDef = TypedDict(
    "RejectGrantResponseResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportContextTypeDef = TypedDict(
    "ReportContextTypeDef",
    {
        "licenseConfigurationArns": List[str],
    },
)

ReportFrequencyTypeDef = TypedDict(
    "ReportFrequencyTypeDef",
    {
        "value": int,
        "period": ReportFrequencyTypeType,
    },
    total=False,
)

ReportGeneratorTypeDef = TypedDict(
    "ReportGeneratorTypeDef",
    {
        "ReportGeneratorName": str,
        "ReportType": List[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "LicenseManagerReportGeneratorArn": str,
        "LastRunStatus": str,
        "LastRunFailureReason": str,
        "LastReportGenerationTime": str,
        "ReportCreatorAccount": str,
        "Description": str,
        "S3Location": "S3LocationTypeDef",
        "CreateTime": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
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

TokenDataTypeDef = TypedDict(
    "TokenDataTypeDef",
    {
        "TokenId": str,
        "TokenType": str,
        "LicenseArn": str,
        "ExpirationTime": str,
        "TokenProperties": List[str],
        "RoleArns": List[str],
        "Status": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateLicenseConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalUpdateLicenseConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationStatus": LicenseConfigurationStatusType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "Name": str,
        "Description": str,
        "ProductInformationList": List["ProductInformationTypeDef"],
        "DisassociateWhenNotFound": bool,
    },
    total=False,
)


class UpdateLicenseConfigurationRequestTypeDef(
    _RequiredUpdateLicenseConfigurationRequestTypeDef,
    _OptionalUpdateLicenseConfigurationRequestTypeDef,
):
    pass


_RequiredUpdateLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseManagerReportGeneratorRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ReportGeneratorName": str,
        "Type": List[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "ClientToken": str,
    },
)
_OptionalUpdateLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseManagerReportGeneratorRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateLicenseManagerReportGeneratorRequestTypeDef(
    _RequiredUpdateLicenseManagerReportGeneratorRequestTypeDef,
    _OptionalUpdateLicenseManagerReportGeneratorRequestTypeDef,
):
    pass


_RequiredUpdateLicenseSpecificationsForResourceRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseSpecificationsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalUpdateLicenseSpecificationsForResourceRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseSpecificationsForResourceRequestTypeDef",
    {
        "AddLicenseSpecifications": List["LicenseSpecificationTypeDef"],
        "RemoveLicenseSpecifications": List["LicenseSpecificationTypeDef"],
    },
    total=False,
)


class UpdateLicenseSpecificationsForResourceRequestTypeDef(
    _RequiredUpdateLicenseSpecificationsForResourceRequestTypeDef,
    _OptionalUpdateLicenseSpecificationsForResourceRequestTypeDef,
):
    pass


UpdateServiceSettingsRequestTypeDef = TypedDict(
    "UpdateServiceSettingsRequestTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
    },
    total=False,
)
