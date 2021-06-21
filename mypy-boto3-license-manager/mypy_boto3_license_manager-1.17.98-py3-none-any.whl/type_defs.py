"""
Type annotations for license-manager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantResponseTypeDef

    data: AcceptGrantResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    AllowedOperationType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
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
    "AcceptGrantResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DatetimeRangeTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseResponseTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
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
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesResponseTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTokensResponseTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "RejectGrantResponseTypeDef",
    "ReportContextTypeDef",
    "ReportFrequencyTypeDef",
    "ReportGeneratorTypeDef",
    "ResourceInventoryTypeDef",
    "S3LocationTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
)

AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
    },
    total=False,
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

CheckoutBorrowLicenseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
    },
    total=False,
)

CheckoutLicenseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseTypeDef",
    {
        "CheckoutType": Literal["PROVISIONAL"],
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
    },
    total=False,
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

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
    },
    total=False,
)

CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
    },
    total=False,
)

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

CreateLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
    total=False,
)

CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": LicenseStatusType,
        "Version": str,
    },
    total=False,
)

CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": LicenseStatusType,
    },
    total=False,
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "TokenId": str,
        "TokenType": Literal["REFRESH_TOKEN"],
        "Token": str,
    },
    total=False,
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


DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
    },
    total=False,
)

DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {
        "Status": LicenseDeletionStatusType,
        "DeletionDate": str,
    },
    total=False,
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


ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Expiration": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)

GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef",
    {
        "Grant": "GrantTypeDef",
    },
    total=False,
)

GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
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
    },
    total=False,
)

GetLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    {
        "ReportGenerator": "ReportGeneratorTypeDef",
    },
    total=False,
)

GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef",
    {
        "License": "LicenseTypeDef",
    },
    total=False,
)

GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef",
    {
        "LicenseUsage": "LicenseUsageTypeDef",
    },
    total=False,
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
    },
    total=False,
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

ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List["LicenseOperationFailureTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List["LicenseConfigurationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLicenseManagerReportGeneratorsResponseTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    {
        "ReportGenerators": List["ReportGeneratorTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List["LicenseSpecificationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {
        "Licenses": List["GrantedLicenseTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List["ResourceInventoryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef",
    {
        "Tokens": List["TokenDataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"],
        "NextToken": str,
    },
    total=False,
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
        "AllowedOperations": List[AllowedOperationType],
    },
    total=False,
)

RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
    },
    total=False,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
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
