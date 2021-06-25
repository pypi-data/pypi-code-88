"""
Type annotations for snowball service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_snowball import SnowballClient

    client: SnowballClient = boto3.client("snowball")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from .literals import (
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ShipmentStateType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
)
from .paginator import (
    DescribeAddressesPaginator,
    ListClusterJobsPaginator,
    ListClustersPaginator,
    ListCompatibleImagesPaginator,
    ListJobsPaginator,
)
from .type_defs import (
    AddressTypeDef,
    CreateAddressResultTypeDef,
    CreateClusterResultTypeDef,
    CreateJobResultTypeDef,
    CreateLongTermPricingResultTypeDef,
    CreateReturnShippingLabelResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAddressResultTypeDef,
    DescribeClusterResultTypeDef,
    DescribeJobResultTypeDef,
    DescribeReturnShippingLabelResultTypeDef,
    DeviceConfigurationTypeDef,
    GetJobManifestResultTypeDef,
    GetJobUnlockCodeResultTypeDef,
    GetSnowballUsageResultTypeDef,
    GetSoftwareUpdatesResultTypeDef,
    JobResourceTypeDef,
    ListClusterJobsResultTypeDef,
    ListClustersResultTypeDef,
    ListCompatibleImagesResultTypeDef,
    ListJobsResultTypeDef,
    ListLongTermPricingResultTypeDef,
    NotificationTypeDef,
    OnDeviceServiceConfigurationTypeDef,
    TaxDocumentsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SnowballClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClusterLimitExceededException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    Ec2RequestFailedException: Type[BotocoreClientError]
    InvalidAddressException: Type[BotocoreClientError]
    InvalidInputCombinationException: Type[BotocoreClientError]
    InvalidJobStateException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidResourceException: Type[BotocoreClientError]
    KMSRequestFailedException: Type[BotocoreClientError]
    ReturnShippingLabelAlreadyExistsException: Type[BotocoreClientError]
    UnsupportedAddressException: Type[BotocoreClientError]


class SnowballClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#can_paginate)
        """

    def cancel_cluster(self, *, ClusterId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.cancel_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#cancel_cluster)
        """

    def cancel_job(self, *, JobId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#cancel_job)
        """

    def create_address(self, *, Address: "AddressTypeDef") -> CreateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.create_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_address)
        """

    def create_cluster(
        self,
        *,
        JobType: JobTypeType,
        Resources: "JobResourceTypeDef",
        AddressId: str,
        RoleARN: str,
        SnowballType: SnowballTypeType,
        ShippingOption: ShippingOptionType,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        Description: str = None,
        KmsKeyARN: str = None,
        Notification: "NotificationTypeDef" = None,
        ForwardingAddressId: str = None,
        TaxDocuments: "TaxDocumentsTypeDef" = None,
        RemoteManagement: RemoteManagementType = None
    ) -> CreateClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_cluster)
        """

    def create_job(
        self,
        *,
        JobType: JobTypeType = None,
        Resources: "JobResourceTypeDef" = None,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        Description: str = None,
        AddressId: str = None,
        KmsKeyARN: str = None,
        RoleARN: str = None,
        SnowballCapacityPreference: SnowballCapacityType = None,
        ShippingOption: ShippingOptionType = None,
        Notification: "NotificationTypeDef" = None,
        ClusterId: str = None,
        SnowballType: SnowballTypeType = None,
        ForwardingAddressId: str = None,
        TaxDocuments: "TaxDocumentsTypeDef" = None,
        DeviceConfiguration: "DeviceConfigurationTypeDef" = None,
        RemoteManagement: RemoteManagementType = None,
        LongTermPricingId: str = None
    ) -> CreateJobResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_job)
        """

    def create_long_term_pricing(
        self,
        *,
        LongTermPricingType: LongTermPricingTypeType,
        IsLongTermPricingAutoRenew: bool = None,
        SnowballType: SnowballTypeType = None
    ) -> CreateLongTermPricingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.create_long_term_pricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_long_term_pricing)
        """

    def create_return_shipping_label(
        self, *, JobId: str, ShippingOption: ShippingOptionType = None
    ) -> CreateReturnShippingLabelResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.create_return_shipping_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#create_return_shipping_label)
        """

    def describe_address(self, *, AddressId: str) -> DescribeAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.describe_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_address)
        """

    def describe_addresses(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeAddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.describe_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_addresses)
        """

    def describe_cluster(self, *, ClusterId: str) -> DescribeClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_cluster)
        """

    def describe_job(self, *, JobId: str) -> DescribeJobResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_job)
        """

    def describe_return_shipping_label(
        self, *, JobId: str
    ) -> DescribeReturnShippingLabelResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.describe_return_shipping_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#describe_return_shipping_label)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#generate_presigned_url)
        """

    def get_job_manifest(self, *, JobId: str) -> GetJobManifestResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.get_job_manifest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_job_manifest)
        """

    def get_job_unlock_code(self, *, JobId: str) -> GetJobUnlockCodeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.get_job_unlock_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_job_unlock_code)
        """

    def get_snowball_usage(self) -> GetSnowballUsageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.get_snowball_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_snowball_usage)
        """

    def get_software_updates(self, *, JobId: str) -> GetSoftwareUpdatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.get_software_updates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#get_software_updates)
        """

    def list_cluster_jobs(
        self, *, ClusterId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListClusterJobsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.list_cluster_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_cluster_jobs)
        """

    def list_clusters(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListClustersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_clusters)
        """

    def list_compatible_images(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCompatibleImagesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.list_compatible_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_compatible_images)
        """

    def list_jobs(self, *, MaxResults: int = None, NextToken: str = None) -> ListJobsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_jobs)
        """

    def list_long_term_pricing(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListLongTermPricingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.list_long_term_pricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#list_long_term_pricing)
        """

    def update_cluster(
        self,
        *,
        ClusterId: str,
        RoleARN: str = None,
        Description: str = None,
        Resources: "JobResourceTypeDef" = None,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        AddressId: str = None,
        ShippingOption: ShippingOptionType = None,
        Notification: "NotificationTypeDef" = None,
        ForwardingAddressId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.update_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_cluster)
        """

    def update_job(
        self,
        *,
        JobId: str,
        RoleARN: str = None,
        Notification: "NotificationTypeDef" = None,
        Resources: "JobResourceTypeDef" = None,
        OnDeviceServiceConfiguration: "OnDeviceServiceConfigurationTypeDef" = None,
        AddressId: str = None,
        ShippingOption: ShippingOptionType = None,
        Description: str = None,
        SnowballCapacityPreference: SnowballCapacityType = None,
        ForwardingAddressId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_job)
        """

    def update_job_shipment_state(
        self, *, JobId: str, ShipmentState: ShipmentStateType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.update_job_shipment_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_job_shipment_state)
        """

    def update_long_term_pricing(
        self,
        *,
        LongTermPricingId: str,
        ReplacementJob: str = None,
        IsLongTermPricingAutoRenew: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Client.update_long_term_pricing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/client.html#update_long_term_pricing)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses"]
    ) -> DescribeAddressesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#describeaddressespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_jobs"]
    ) -> ListClusterJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listclusterjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Paginator.ListClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compatible_images"]
    ) -> ListCompatibleImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listcompatibleimagespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/snowball.html#Snowball.Paginator.ListJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/paginators.html#listjobspaginator)
        """
