"""
Type annotations for devops-guru service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_devops_guru import DevOpsGuruClient

    client: DevOpsGuruClient = boto3.client("devops-guru")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from .literals import (
    InsightTypeType,
    LocaleType,
    ResourceCollectionTypeType,
    UpdateResourceCollectionActionType,
)
from .paginator import (
    DescribeResourceCollectionHealthPaginator,
    GetCostEstimationPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListNotificationChannelsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
)
from .type_defs import (
    AddNotificationChannelResponseTypeDef,
    CostEstimationResourceCollectionFilterTypeDef,
    DescribeAccountHealthResponseTypeDef,
    DescribeAccountOverviewResponseTypeDef,
    DescribeAnomalyResponseTypeDef,
    DescribeFeedbackResponseTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    DescribeServiceIntegrationResponseTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    InsightFeedbackTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    NotificationChannelConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
    UpdateResourceCollectionFilterTypeDef,
    UpdateServiceIntegrationConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DevOpsGuruClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class DevOpsGuruClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_notification_channel(
        self, *, Config: "NotificationChannelConfigTypeDef"
    ) -> AddNotificationChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.add_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#add_notification_channel)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#can_paginate)
        """

    def describe_account_health(self) -> DescribeAccountHealthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_account_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_account_health)
        """

    def describe_account_overview(
        self, *, FromTime: datetime, ToTime: datetime = None
    ) -> DescribeAccountOverviewResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_account_overview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_account_overview)
        """

    def describe_anomaly(self, *, Id: str) -> DescribeAnomalyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_anomaly)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_anomaly)
        """

    def describe_feedback(self, *, InsightId: str = None) -> DescribeFeedbackResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_feedback)
        """

    def describe_insight(self, *, Id: str) -> DescribeInsightResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_insight)
        """

    def describe_resource_collection_health(
        self, *, ResourceCollectionType: ResourceCollectionTypeType, NextToken: str = None
    ) -> DescribeResourceCollectionHealthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_resource_collection_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_resource_collection_health)
        """

    def describe_service_integration(self) -> DescribeServiceIntegrationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.describe_service_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_service_integration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#generate_presigned_url)
        """

    def get_cost_estimation(self, *, NextToken: str = None) -> GetCostEstimationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.get_cost_estimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#get_cost_estimation)
        """

    def get_resource_collection(
        self, *, ResourceCollectionType: ResourceCollectionTypeType, NextToken: str = None
    ) -> GetResourceCollectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.get_resource_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#get_resource_collection)
        """

    def list_anomalies_for_insight(
        self,
        *,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAnomaliesForInsightResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.list_anomalies_for_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_anomalies_for_insight)
        """

    def list_events(
        self, *, Filters: ListEventsFiltersTypeDef, MaxResults: int = None, NextToken: str = None
    ) -> ListEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.list_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_events)
        """

    def list_insights(
        self,
        *,
        StatusFilter: ListInsightsStatusFilterTypeDef,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListInsightsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.list_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_insights)
        """

    def list_notification_channels(
        self, *, NextToken: str = None
    ) -> ListNotificationChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.list_notification_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_notification_channels)
        """

    def list_recommendations(
        self, *, InsightId: str, NextToken: str = None, Locale: LocaleType = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_recommendations)
        """

    def put_feedback(self, *, InsightFeedback: "InsightFeedbackTypeDef" = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.put_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#put_feedback)
        """

    def remove_notification_channel(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.remove_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#remove_notification_channel)
        """

    def search_insights(
        self,
        *,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: SearchInsightsFiltersTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchInsightsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.search_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#search_insights)
        """

    def start_cost_estimation(
        self,
        *,
        ResourceCollection: "CostEstimationResourceCollectionFilterTypeDef",
        ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.start_cost_estimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#start_cost_estimation)
        """

    def update_resource_collection(
        self,
        *,
        Action: UpdateResourceCollectionActionType,
        ResourceCollection: UpdateResourceCollectionFilterTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.update_resource_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#update_resource_collection)
        """

    def update_service_integration(
        self, *, ServiceIntegration: UpdateServiceIntegrationConfigTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Client.update_service_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#update_service_integration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_collection_health"]
    ) -> DescribeResourceCollectionHealthPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeresourcecollectionhealthpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_cost_estimation"]
    ) -> GetCostEstimationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetCostEstimation)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getcostestimationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_collection"]
    ) -> GetResourceCollectionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getresourcecollectionpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_anomalies_for_insight"]
    ) -> ListAnomaliesForInsightPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listanomaliesforinsightpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_events"]) -> ListEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listeventspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_insights"]) -> ListInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listinsightspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notification_channels"]
    ) -> ListNotificationChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listnotificationchannelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listrecommendationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_insights"]) -> SearchInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchinsightspaginator)
        """
