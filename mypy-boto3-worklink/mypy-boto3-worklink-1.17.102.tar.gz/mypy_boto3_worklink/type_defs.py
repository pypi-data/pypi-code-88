"""
Type annotations for worklink service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_worklink/type_defs.html)

Usage::

    ```python
    from mypy_boto3_worklink.type_defs import AssociateDomainRequestTypeDef

    data: AssociateDomainRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import DeviceStatusType, DomainStatusType, FleetStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateDomainRequestTypeDef",
    "AssociateWebsiteAuthorizationProviderRequestTypeDef",
    "AssociateWebsiteAuthorizationProviderResponseResponseTypeDef",
    "AssociateWebsiteCertificateAuthorityRequestTypeDef",
    "AssociateWebsiteCertificateAuthorityResponseResponseTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResponseResponseTypeDef",
    "DeleteFleetRequestTypeDef",
    "DescribeAuditStreamConfigurationRequestTypeDef",
    "DescribeAuditStreamConfigurationResponseResponseTypeDef",
    "DescribeCompanyNetworkConfigurationRequestTypeDef",
    "DescribeCompanyNetworkConfigurationResponseResponseTypeDef",
    "DescribeDevicePolicyConfigurationRequestTypeDef",
    "DescribeDevicePolicyConfigurationResponseResponseTypeDef",
    "DescribeDeviceRequestTypeDef",
    "DescribeDeviceResponseResponseTypeDef",
    "DescribeDomainRequestTypeDef",
    "DescribeDomainResponseResponseTypeDef",
    "DescribeFleetMetadataRequestTypeDef",
    "DescribeFleetMetadataResponseResponseTypeDef",
    "DescribeIdentityProviderConfigurationRequestTypeDef",
    "DescribeIdentityProviderConfigurationResponseResponseTypeDef",
    "DescribeWebsiteCertificateAuthorityRequestTypeDef",
    "DescribeWebsiteCertificateAuthorityResponseResponseTypeDef",
    "DeviceSummaryTypeDef",
    "DisassociateDomainRequestTypeDef",
    "DisassociateWebsiteAuthorizationProviderRequestTypeDef",
    "DisassociateWebsiteCertificateAuthorityRequestTypeDef",
    "DomainSummaryTypeDef",
    "FleetSummaryTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResponseResponseTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseResponseTypeDef",
    "ListFleetsRequestTypeDef",
    "ListFleetsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListWebsiteAuthorizationProvidersRequestTypeDef",
    "ListWebsiteAuthorizationProvidersResponseResponseTypeDef",
    "ListWebsiteCertificateAuthoritiesRequestTypeDef",
    "ListWebsiteCertificateAuthoritiesResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDomainAccessRequestTypeDef",
    "RevokeDomainAccessRequestTypeDef",
    "SignOutUserRequestTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAuditStreamConfigurationRequestTypeDef",
    "UpdateCompanyNetworkConfigurationRequestTypeDef",
    "UpdateDevicePolicyConfigurationRequestTypeDef",
    "UpdateDomainMetadataRequestTypeDef",
    "UpdateFleetMetadataRequestTypeDef",
    "UpdateIdentityProviderConfigurationRequestTypeDef",
    "WebsiteAuthorizationProviderSummaryTypeDef",
    "WebsiteCaSummaryTypeDef",
)

_RequiredAssociateDomainRequestTypeDef = TypedDict(
    "_RequiredAssociateDomainRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
        "AcmCertificateArn": str,
    },
)
_OptionalAssociateDomainRequestTypeDef = TypedDict(
    "_OptionalAssociateDomainRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class AssociateDomainRequestTypeDef(
    _RequiredAssociateDomainRequestTypeDef, _OptionalAssociateDomainRequestTypeDef
):
    pass


_RequiredAssociateWebsiteAuthorizationProviderRequestTypeDef = TypedDict(
    "_RequiredAssociateWebsiteAuthorizationProviderRequestTypeDef",
    {
        "FleetArn": str,
        "AuthorizationProviderType": Literal["SAML"],
    },
)
_OptionalAssociateWebsiteAuthorizationProviderRequestTypeDef = TypedDict(
    "_OptionalAssociateWebsiteAuthorizationProviderRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)


class AssociateWebsiteAuthorizationProviderRequestTypeDef(
    _RequiredAssociateWebsiteAuthorizationProviderRequestTypeDef,
    _OptionalAssociateWebsiteAuthorizationProviderRequestTypeDef,
):
    pass


AssociateWebsiteAuthorizationProviderResponseResponseTypeDef = TypedDict(
    "AssociateWebsiteAuthorizationProviderResponseResponseTypeDef",
    {
        "AuthorizationProviderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateWebsiteCertificateAuthorityRequestTypeDef = TypedDict(
    "_RequiredAssociateWebsiteCertificateAuthorityRequestTypeDef",
    {
        "FleetArn": str,
        "Certificate": str,
    },
)
_OptionalAssociateWebsiteCertificateAuthorityRequestTypeDef = TypedDict(
    "_OptionalAssociateWebsiteCertificateAuthorityRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class AssociateWebsiteCertificateAuthorityRequestTypeDef(
    _RequiredAssociateWebsiteCertificateAuthorityRequestTypeDef,
    _OptionalAssociateWebsiteCertificateAuthorityRequestTypeDef,
):
    pass


AssociateWebsiteCertificateAuthorityResponseResponseTypeDef = TypedDict(
    "AssociateWebsiteCertificateAuthorityResponseResponseTypeDef",
    {
        "WebsiteCaId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestTypeDef",
    {
        "FleetName": str,
    },
)
_OptionalCreateFleetRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestTypeDef",
    {
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateFleetRequestTypeDef(
    _RequiredCreateFleetRequestTypeDef, _OptionalCreateFleetRequestTypeDef
):
    pass


CreateFleetResponseResponseTypeDef = TypedDict(
    "CreateFleetResponseResponseTypeDef",
    {
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetRequestTypeDef = TypedDict(
    "DeleteFleetRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeAuditStreamConfigurationRequestTypeDef = TypedDict(
    "DescribeAuditStreamConfigurationRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeAuditStreamConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeAuditStreamConfigurationResponseResponseTypeDef",
    {
        "AuditStreamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCompanyNetworkConfigurationRequestTypeDef = TypedDict(
    "DescribeCompanyNetworkConfigurationRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeCompanyNetworkConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeCompanyNetworkConfigurationResponseResponseTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDevicePolicyConfigurationRequestTypeDef = TypedDict(
    "DescribeDevicePolicyConfigurationRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeDevicePolicyConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeDevicePolicyConfigurationResponseResponseTypeDef",
    {
        "DeviceCaCertificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestTypeDef = TypedDict(
    "DescribeDeviceRequestTypeDef",
    {
        "FleetArn": str,
        "DeviceId": str,
    },
)

DescribeDeviceResponseResponseTypeDef = TypedDict(
    "DescribeDeviceResponseResponseTypeDef",
    {
        "Status": DeviceStatusType,
        "Model": str,
        "Manufacturer": str,
        "OperatingSystem": str,
        "OperatingSystemVersion": str,
        "PatchLevel": str,
        "FirstAccessedTime": datetime,
        "LastAccessedTime": datetime,
        "Username": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestTypeDef = TypedDict(
    "DescribeDomainRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

DescribeDomainResponseResponseTypeDef = TypedDict(
    "DescribeDomainResponseResponseTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": DomainStatusType,
        "AcmCertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetMetadataRequestTypeDef = TypedDict(
    "DescribeFleetMetadataRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeFleetMetadataResponseResponseTypeDef = TypedDict(
    "DescribeFleetMetadataResponseResponseTypeDef",
    {
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "CompanyCode": str,
        "FleetStatus": FleetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderConfigurationRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigurationRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeIdentityProviderConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigurationResponseResponseTypeDef",
    {
        "IdentityProviderType": Literal["SAML"],
        "ServiceProviderSamlMetadata": str,
        "IdentityProviderSamlMetadata": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWebsiteCertificateAuthorityRequestTypeDef = TypedDict(
    "DescribeWebsiteCertificateAuthorityRequestTypeDef",
    {
        "FleetArn": str,
        "WebsiteCaId": str,
    },
)

DescribeWebsiteCertificateAuthorityResponseResponseTypeDef = TypedDict(
    "DescribeWebsiteCertificateAuthorityResponseResponseTypeDef",
    {
        "Certificate": str,
        "CreatedTime": datetime,
        "DisplayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "DeviceId": str,
        "DeviceStatus": DeviceStatusType,
    },
    total=False,
)

DisassociateDomainRequestTypeDef = TypedDict(
    "DisassociateDomainRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

DisassociateWebsiteAuthorizationProviderRequestTypeDef = TypedDict(
    "DisassociateWebsiteAuthorizationProviderRequestTypeDef",
    {
        "FleetArn": str,
        "AuthorizationProviderId": str,
    },
)

DisassociateWebsiteCertificateAuthorityRequestTypeDef = TypedDict(
    "DisassociateWebsiteCertificateAuthorityRequestTypeDef",
    {
        "FleetArn": str,
        "WebsiteCaId": str,
    },
)

_RequiredDomainSummaryTypeDef = TypedDict(
    "_RequiredDomainSummaryTypeDef",
    {
        "DomainName": str,
        "CreatedTime": datetime,
        "DomainStatus": DomainStatusType,
    },
)
_OptionalDomainSummaryTypeDef = TypedDict(
    "_OptionalDomainSummaryTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, _OptionalDomainSummaryTypeDef):
    pass


FleetSummaryTypeDef = TypedDict(
    "FleetSummaryTypeDef",
    {
        "FleetArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "CompanyCode": str,
        "FleetStatus": FleetStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredListDevicesRequestTypeDef = TypedDict(
    "_RequiredListDevicesRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListDevicesRequestTypeDef = TypedDict(
    "_OptionalListDevicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDevicesRequestTypeDef(
    _RequiredListDevicesRequestTypeDef, _OptionalListDevicesRequestTypeDef
):
    pass


ListDevicesResponseResponseTypeDef = TypedDict(
    "ListDevicesResponseResponseTypeDef",
    {
        "Devices": List["DeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainsRequestTypeDef = TypedDict(
    "_RequiredListDomainsRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListDomainsRequestTypeDef = TypedDict(
    "_OptionalListDomainsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDomainsRequestTypeDef(
    _RequiredListDomainsRequestTypeDef, _OptionalListDomainsRequestTypeDef
):
    pass


ListDomainsResponseResponseTypeDef = TypedDict(
    "ListDomainsResponseResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestTypeDef = TypedDict(
    "ListFleetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFleetsResponseResponseTypeDef = TypedDict(
    "ListFleetsResponseResponseTypeDef",
    {
        "FleetSummaryList": List["FleetSummaryTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebsiteAuthorizationProvidersRequestTypeDef = TypedDict(
    "_RequiredListWebsiteAuthorizationProvidersRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListWebsiteAuthorizationProvidersRequestTypeDef = TypedDict(
    "_OptionalListWebsiteAuthorizationProvidersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListWebsiteAuthorizationProvidersRequestTypeDef(
    _RequiredListWebsiteAuthorizationProvidersRequestTypeDef,
    _OptionalListWebsiteAuthorizationProvidersRequestTypeDef,
):
    pass


ListWebsiteAuthorizationProvidersResponseResponseTypeDef = TypedDict(
    "ListWebsiteAuthorizationProvidersResponseResponseTypeDef",
    {
        "WebsiteAuthorizationProviders": List["WebsiteAuthorizationProviderSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebsiteCertificateAuthoritiesRequestTypeDef = TypedDict(
    "_RequiredListWebsiteCertificateAuthoritiesRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalListWebsiteCertificateAuthoritiesRequestTypeDef = TypedDict(
    "_OptionalListWebsiteCertificateAuthoritiesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListWebsiteCertificateAuthoritiesRequestTypeDef(
    _RequiredListWebsiteCertificateAuthoritiesRequestTypeDef,
    _OptionalListWebsiteCertificateAuthoritiesRequestTypeDef,
):
    pass


ListWebsiteCertificateAuthoritiesResponseResponseTypeDef = TypedDict(
    "ListWebsiteCertificateAuthoritiesResponseResponseTypeDef",
    {
        "WebsiteCertificateAuthorities": List["WebsiteCaSummaryTypeDef"],
        "NextToken": str,
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

RestoreDomainAccessRequestTypeDef = TypedDict(
    "RestoreDomainAccessRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

RevokeDomainAccessRequestTypeDef = TypedDict(
    "RevokeDomainAccessRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

SignOutUserRequestTypeDef = TypedDict(
    "SignOutUserRequestTypeDef",
    {
        "FleetArn": str,
        "Username": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAuditStreamConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateAuditStreamConfigurationRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalUpdateAuditStreamConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateAuditStreamConfigurationRequestTypeDef",
    {
        "AuditStreamArn": str,
    },
    total=False,
)


class UpdateAuditStreamConfigurationRequestTypeDef(
    _RequiredUpdateAuditStreamConfigurationRequestTypeDef,
    _OptionalUpdateAuditStreamConfigurationRequestTypeDef,
):
    pass


UpdateCompanyNetworkConfigurationRequestTypeDef = TypedDict(
    "UpdateCompanyNetworkConfigurationRequestTypeDef",
    {
        "FleetArn": str,
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

_RequiredUpdateDevicePolicyConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateDevicePolicyConfigurationRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalUpdateDevicePolicyConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateDevicePolicyConfigurationRequestTypeDef",
    {
        "DeviceCaCertificate": str,
    },
    total=False,
)


class UpdateDevicePolicyConfigurationRequestTypeDef(
    _RequiredUpdateDevicePolicyConfigurationRequestTypeDef,
    _OptionalUpdateDevicePolicyConfigurationRequestTypeDef,
):
    pass


_RequiredUpdateDomainMetadataRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainMetadataRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)
_OptionalUpdateDomainMetadataRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainMetadataRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class UpdateDomainMetadataRequestTypeDef(
    _RequiredUpdateDomainMetadataRequestTypeDef, _OptionalUpdateDomainMetadataRequestTypeDef
):
    pass


_RequiredUpdateFleetMetadataRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetMetadataRequestTypeDef",
    {
        "FleetArn": str,
    },
)
_OptionalUpdateFleetMetadataRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetMetadataRequestTypeDef",
    {
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
    },
    total=False,
)


class UpdateFleetMetadataRequestTypeDef(
    _RequiredUpdateFleetMetadataRequestTypeDef, _OptionalUpdateFleetMetadataRequestTypeDef
):
    pass


_RequiredUpdateIdentityProviderConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderConfigurationRequestTypeDef",
    {
        "FleetArn": str,
        "IdentityProviderType": Literal["SAML"],
    },
)
_OptionalUpdateIdentityProviderConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderConfigurationRequestTypeDef",
    {
        "IdentityProviderSamlMetadata": str,
    },
    total=False,
)


class UpdateIdentityProviderConfigurationRequestTypeDef(
    _RequiredUpdateIdentityProviderConfigurationRequestTypeDef,
    _OptionalUpdateIdentityProviderConfigurationRequestTypeDef,
):
    pass


_RequiredWebsiteAuthorizationProviderSummaryTypeDef = TypedDict(
    "_RequiredWebsiteAuthorizationProviderSummaryTypeDef",
    {
        "AuthorizationProviderType": Literal["SAML"],
    },
)
_OptionalWebsiteAuthorizationProviderSummaryTypeDef = TypedDict(
    "_OptionalWebsiteAuthorizationProviderSummaryTypeDef",
    {
        "AuthorizationProviderId": str,
        "DomainName": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class WebsiteAuthorizationProviderSummaryTypeDef(
    _RequiredWebsiteAuthorizationProviderSummaryTypeDef,
    _OptionalWebsiteAuthorizationProviderSummaryTypeDef,
):
    pass


WebsiteCaSummaryTypeDef = TypedDict(
    "WebsiteCaSummaryTypeDef",
    {
        "WebsiteCaId": str,
        "CreatedTime": datetime,
        "DisplayName": str,
    },
    total=False,
)
