"""
Type annotations for es service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_es import ElasticsearchServiceClient

    client: ElasticsearchServiceClient = boto3.client("es")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ESPartitionInstanceTypeType, LogTypeType
from .paginator import (
    DescribeReservedElasticsearchInstanceOfferingsPaginator,
    DescribeReservedElasticsearchInstancesPaginator,
    GetUpgradeHistoryPaginator,
    ListElasticsearchInstanceTypesPaginator,
    ListElasticsearchVersionsPaginator,
)
from .type_defs import (
    AcceptInboundCrossClusterSearchConnectionResponseTypeDef,
    AdvancedSecurityOptionsInputTypeDef,
    AssociatePackageResponseTypeDef,
    AutoTuneOptionsInputTypeDef,
    AutoTuneOptionsTypeDef,
    CancelElasticsearchServiceSoftwareUpdateResponseTypeDef,
    CognitoOptionsTypeDef,
    CreateElasticsearchDomainResponseTypeDef,
    CreateOutboundCrossClusterSearchConnectionResponseTypeDef,
    CreatePackageResponseTypeDef,
    DeleteElasticsearchDomainResponseTypeDef,
    DeleteInboundCrossClusterSearchConnectionResponseTypeDef,
    DeleteOutboundCrossClusterSearchConnectionResponseTypeDef,
    DeletePackageResponseTypeDef,
    DescribeDomainAutoTunesResponseTypeDef,
    DescribeElasticsearchDomainConfigResponseTypeDef,
    DescribeElasticsearchDomainResponseTypeDef,
    DescribeElasticsearchDomainsResponseTypeDef,
    DescribeElasticsearchInstanceTypeLimitsResponseTypeDef,
    DescribeInboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef,
    DescribePackagesFilterTypeDef,
    DescribePackagesResponseTypeDef,
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    DissociatePackageResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    DomainInformationTypeDef,
    EBSOptionsTypeDef,
    ElasticsearchClusterConfigTypeDef,
    EncryptionAtRestOptionsTypeDef,
    FilterTypeDef,
    GetCompatibleElasticsearchVersionsResponseTypeDef,
    GetPackageVersionHistoryResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    GetUpgradeStatusResponseTypeDef,
    ListDomainNamesResponseTypeDef,
    ListDomainsForPackageResponseTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    ListPackagesForDomainResponseTypeDef,
    ListTagsResponseTypeDef,
    LogPublishingOptionTypeDef,
    NodeToNodeEncryptionOptionsTypeDef,
    PackageSourceTypeDef,
    PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef,
    RejectInboundCrossClusterSearchConnectionResponseTypeDef,
    SnapshotOptionsTypeDef,
    StartElasticsearchServiceSoftwareUpdateResponseTypeDef,
    TagTypeDef,
    UpdateElasticsearchDomainConfigResponseTypeDef,
    UpdatePackageResponseTypeDef,
    UpgradeElasticsearchDomainResponseTypeDef,
    VPCOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticsearchServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ElasticsearchServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_inbound_cross_cluster_search_connection(
        self, *, CrossClusterSearchConnectionId: str
    ) -> AcceptInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.accept_inbound_cross_cluster_search_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#accept_inbound_cross_cluster_search_connection)
        """

    def add_tags(self, *, ARN: str, TagList: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#add_tags)
        """

    def associate_package(
        self, *, PackageID: str, DomainName: str
    ) -> AssociatePackageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.associate_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#associate_package)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#can_paginate)
        """

    def cancel_elasticsearch_service_software_update(
        self, *, DomainName: str
    ) -> CancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.cancel_elasticsearch_service_software_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#cancel_elasticsearch_service_software_update)
        """

    def create_elasticsearch_domain(
        self,
        *,
        DomainName: str,
        ElasticsearchVersion: str = None,
        ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        AccessPolicies: str = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        LogPublishingOptions: Dict[LogTypeType, "LogPublishingOptionTypeDef"] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
        AutoTuneOptions: AutoTuneOptionsInputTypeDef = None,
        TagList: List["TagTypeDef"] = None
    ) -> CreateElasticsearchDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.create_elasticsearch_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#create_elasticsearch_domain)
        """

    def create_outbound_cross_cluster_search_connection(
        self,
        *,
        SourceDomainInfo: "DomainInformationTypeDef",
        DestinationDomainInfo: "DomainInformationTypeDef",
        ConnectionAlias: str
    ) -> CreateOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.create_outbound_cross_cluster_search_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#create_outbound_cross_cluster_search_connection)
        """

    def create_package(
        self,
        *,
        PackageName: str,
        PackageType: Literal["TXT-DICTIONARY"],
        PackageSource: PackageSourceTypeDef,
        PackageDescription: str = None
    ) -> CreatePackageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.create_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#create_package)
        """

    def delete_elasticsearch_domain(
        self, *, DomainName: str
    ) -> DeleteElasticsearchDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#delete_elasticsearch_domain)
        """

    def delete_elasticsearch_service_role(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_service_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#delete_elasticsearch_service_role)
        """

    def delete_inbound_cross_cluster_search_connection(
        self, *, CrossClusterSearchConnectionId: str
    ) -> DeleteInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.delete_inbound_cross_cluster_search_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#delete_inbound_cross_cluster_search_connection)
        """

    def delete_outbound_cross_cluster_search_connection(
        self, *, CrossClusterSearchConnectionId: str
    ) -> DeleteOutboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.delete_outbound_cross_cluster_search_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#delete_outbound_cross_cluster_search_connection)
        """

    def delete_package(self, *, PackageID: str) -> DeletePackageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.delete_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#delete_package)
        """

    def describe_domain_auto_tunes(
        self, *, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDomainAutoTunesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_domain_auto_tunes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_domain_auto_tunes)
        """

    def describe_elasticsearch_domain(
        self, *, DomainName: str
    ) -> DescribeElasticsearchDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_elasticsearch_domain)
        """

    def describe_elasticsearch_domain_config(
        self, *, DomainName: str
    ) -> DescribeElasticsearchDomainConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_elasticsearch_domain_config)
        """

    def describe_elasticsearch_domains(
        self, *, DomainNames: List[str]
    ) -> DescribeElasticsearchDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_elasticsearch_domains)
        """

    def describe_elasticsearch_instance_type_limits(
        self,
        *,
        InstanceType: ESPartitionInstanceTypeType,
        ElasticsearchVersion: str,
        DomainName: str = None
    ) -> DescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_instance_type_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_elasticsearch_instance_type_limits)
        """

    def describe_inbound_cross_cluster_search_connections(
        self, *, Filters: List[FilterTypeDef] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeInboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_inbound_cross_cluster_search_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_inbound_cross_cluster_search_connections)
        """

    def describe_outbound_cross_cluster_search_connections(
        self, *, Filters: List[FilterTypeDef] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_outbound_cross_cluster_search_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_outbound_cross_cluster_search_connections)
        """

    def describe_packages(
        self,
        *,
        Filters: List[DescribePackagesFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribePackagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_packages)
        """

    def describe_reserved_elasticsearch_instance_offerings(
        self,
        *,
        ReservedElasticsearchInstanceOfferingId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_reserved_elasticsearch_instance_offerings)
        """

    def describe_reserved_elasticsearch_instances(
        self,
        *,
        ReservedElasticsearchInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#describe_reserved_elasticsearch_instances)
        """

    def dissociate_package(
        self, *, PackageID: str, DomainName: str
    ) -> DissociatePackageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.dissociate_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#dissociate_package)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#generate_presigned_url)
        """

    def get_compatible_elasticsearch_versions(
        self, *, DomainName: str = None
    ) -> GetCompatibleElasticsearchVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.get_compatible_elasticsearch_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#get_compatible_elasticsearch_versions)
        """

    def get_package_version_history(
        self, *, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> GetPackageVersionHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.get_package_version_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#get_package_version_history)
        """

    def get_upgrade_history(
        self, *, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.get_upgrade_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#get_upgrade_history)
        """

    def get_upgrade_status(self, *, DomainName: str) -> GetUpgradeStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.get_upgrade_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#get_upgrade_status)
        """

    def list_domain_names(self) -> ListDomainNamesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.list_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#list_domain_names)
        """

    def list_domains_for_package(
        self, *, PackageID: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDomainsForPackageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.list_domains_for_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#list_domains_for_package)
        """

    def list_elasticsearch_instance_types(
        self,
        *,
        ElasticsearchVersion: str,
        DomainName: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListElasticsearchInstanceTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_instance_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#list_elasticsearch_instance_types)
        """

    def list_elasticsearch_versions(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListElasticsearchVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#list_elasticsearch_versions)
        """

    def list_packages_for_domain(
        self, *, DomainName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPackagesForDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.list_packages_for_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#list_packages_for_domain)
        """

    def list_tags(self, *, ARN: str) -> ListTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#list_tags)
        """

    def purchase_reserved_elasticsearch_instance_offering(
        self,
        *,
        ReservedElasticsearchInstanceOfferingId: str,
        ReservationName: str,
        InstanceCount: int = None
    ) -> PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.purchase_reserved_elasticsearch_instance_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#purchase_reserved_elasticsearch_instance_offering)
        """

    def reject_inbound_cross_cluster_search_connection(
        self, *, CrossClusterSearchConnectionId: str
    ) -> RejectInboundCrossClusterSearchConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.reject_inbound_cross_cluster_search_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#reject_inbound_cross_cluster_search_connection)
        """

    def remove_tags(self, *, ARN: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#remove_tags)
        """

    def start_elasticsearch_service_software_update(
        self, *, DomainName: str
    ) -> StartElasticsearchServiceSoftwareUpdateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.start_elasticsearch_service_software_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#start_elasticsearch_service_software_update)
        """

    def update_elasticsearch_domain_config(
        self,
        *,
        DomainName: str,
        ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
        EBSOptions: "EBSOptionsTypeDef" = None,
        SnapshotOptions: "SnapshotOptionsTypeDef" = None,
        VPCOptions: VPCOptionsTypeDef = None,
        CognitoOptions: "CognitoOptionsTypeDef" = None,
        AdvancedOptions: Dict[str, str] = None,
        AccessPolicies: str = None,
        LogPublishingOptions: Dict[LogTypeType, "LogPublishingOptionTypeDef"] = None,
        DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
        AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
        NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        AutoTuneOptions: "AutoTuneOptionsTypeDef" = None
    ) -> UpdateElasticsearchDomainConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.update_elasticsearch_domain_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#update_elasticsearch_domain_config)
        """

    def update_package(
        self,
        *,
        PackageID: str,
        PackageSource: PackageSourceTypeDef,
        PackageDescription: str = None,
        CommitMessage: str = None
    ) -> UpdatePackageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.update_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#update_package)
        """

    def upgrade_elasticsearch_domain(
        self, *, DomainName: str, TargetVersion: str, PerformCheckOnly: bool = None
    ) -> UpgradeElasticsearchDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Client.upgrade_elasticsearch_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/client.html#upgrade_elasticsearch_domain)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instance_offerings"]
    ) -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/paginators.html#describereservedelasticsearchinstanceofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_elasticsearch_instances"]
    ) -> DescribeReservedElasticsearchInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/paginators.html#describereservedelasticsearchinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_upgrade_history"]
    ) -> GetUpgradeHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/paginators.html#getupgradehistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_instance_types"]
    ) -> ListElasticsearchInstanceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/paginators.html#listelasticsearchinstancetypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_elasticsearch_versions"]
    ) -> ListElasticsearchVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/paginators.html#listelasticsearchversionspaginator)
        """
