"""
Type annotations for marketplacecommerceanalytics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplacecommerceanalytics import MarketplaceCommerceAnalyticsClient

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    ```
"""
from datetime import datetime
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .literals import DataSetTypeType, SupportDataSetTypeType
from .type_defs import GenerateDataSetResultTypeDef, StartSupportDataExportResultTypeDef

__all__ = ("MarketplaceCommerceAnalyticsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    MarketplaceCommerceAnalyticsException: Type[BotocoreClientError]


class MarketplaceCommerceAnalyticsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#can_paginate)
        """

    def generate_data_set(
        self,
        *,
        dataSetType: DataSetTypeType,
        dataSetPublicationDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None
    ) -> GenerateDataSetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#generate_data_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#generate_presigned_url)
        """

    def start_support_data_export(
        self,
        *,
        dataSetType: SupportDataSetTypeType,
        fromDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None
    ) -> StartSupportDataExportResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.start_support_data_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/client.html#start_support_data_export)
        """
