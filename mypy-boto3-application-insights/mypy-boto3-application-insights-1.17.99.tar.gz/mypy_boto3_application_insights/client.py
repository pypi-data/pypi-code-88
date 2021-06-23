"""
Type annotations for application-insights service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_application_insights import ApplicationInsightsClient

    client: ApplicationInsightsClient = boto3.client("application-insights")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import ConfigurationEventStatusType, TierType
from .type_defs import (
    CreateApplicationResponseTypeDef,
    CreateLogPatternResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeComponentConfigurationRecommendationResponseTypeDef,
    DescribeComponentConfigurationResponseTypeDef,
    DescribeComponentResponseTypeDef,
    DescribeLogPatternResponseTypeDef,
    DescribeObservationResponseTypeDef,
    DescribeProblemObservationsResponseTypeDef,
    DescribeProblemResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListConfigurationHistoryResponseTypeDef,
    ListLogPatternSetsResponseTypeDef,
    ListLogPatternsResponseTypeDef,
    ListProblemsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateLogPatternResponseTypeDef,
)

__all__ = ("ApplicationInsightsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagsAlreadyExistException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ApplicationInsightsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#can_paginate)
        """

    def create_application(
        self,
        *,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        CWEMonitorEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#create_application)
        """

    def create_component(
        self, *, ResourceGroupName: str, ComponentName: str, ResourceList: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.create_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#create_component)
        """

    def create_log_pattern(
        self,
        *,
        ResourceGroupName: str,
        PatternSetName: str,
        PatternName: str,
        Pattern: str,
        Rank: int
    ) -> CreateLogPatternResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.create_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#create_log_pattern)
        """

    def delete_application(self, *, ResourceGroupName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#delete_application)
        """

    def delete_component(self, *, ResourceGroupName: str, ComponentName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#delete_component)
        """

    def delete_log_pattern(
        self, *, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.delete_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#delete_log_pattern)
        """

    def describe_application(self, *, ResourceGroupName: str) -> DescribeApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_application)
        """

    def describe_component(
        self, *, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_component)
        """

    def describe_component_configuration(
        self, *, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_component_configuration)
        """

    def describe_component_configuration_recommendation(
        self, *, ResourceGroupName: str, ComponentName: str, Tier: TierType
    ) -> DescribeComponentConfigurationRecommendationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_component_configuration_recommendation)
        """

    def describe_log_pattern(
        self, *, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> DescribeLogPatternResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_log_pattern)
        """

    def describe_observation(self, *, ObservationId: str) -> DescribeObservationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_observation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_observation)
        """

    def describe_problem(self, *, ProblemId: str) -> DescribeProblemResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_problem)
        """

    def describe_problem_observations(
        self, *, ProblemId: str
    ) -> DescribeProblemObservationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem_observations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_problem_observations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#generate_presigned_url)
        """

    def list_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_applications)
        """

    def list_components(
        self, *, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_components)
        """

    def list_configuration_history(
        self,
        *,
        ResourceGroupName: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventStatus: ConfigurationEventStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListConfigurationHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_configuration_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_configuration_history)
        """

    def list_log_pattern_sets(
        self, *, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLogPatternSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_log_pattern_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_log_pattern_sets)
        """

    def list_log_patterns(
        self,
        *,
        ResourceGroupName: str,
        PatternSetName: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListLogPatternsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_log_patterns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_log_patterns)
        """

    def list_problems(
        self,
        *,
        ResourceGroupName: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListProblemsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_problems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_problems)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#untag_resource)
        """

    def update_application(
        self,
        *,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        CWEMonitorEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        RemoveSNSTopic: bool = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_application)
        """

    def update_component(
        self,
        *,
        ResourceGroupName: str,
        ComponentName: str,
        NewComponentName: str = None,
        ResourceList: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.update_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_component)
        """

    def update_component_configuration(
        self,
        *,
        ResourceGroupName: str,
        ComponentName: str,
        Monitor: bool = None,
        Tier: TierType = None,
        ComponentConfiguration: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.update_component_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_component_configuration)
        """

    def update_log_pattern(
        self,
        *,
        ResourceGroupName: str,
        PatternSetName: str,
        PatternName: str,
        Pattern: str = None,
        Rank: int = None
    ) -> UpdateLogPatternResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/application-insights.html#ApplicationInsights.Client.update_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_log_pattern)
        """
