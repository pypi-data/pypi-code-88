"""
Type annotations for accessanalyzer service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_accessanalyzer import AccessAnalyzerClient

    client: AccessAnalyzerClient = boto3.client("accessanalyzer")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    FindingStatusUpdateType,
    LocaleType,
    PolicyTypeType,
    ResourceTypeType,
    TypeType,
)
from .paginator import (
    ListAccessPreviewFindingsPaginator,
    ListAccessPreviewsPaginator,
    ListAnalyzedResourcesPaginator,
    ListAnalyzersPaginator,
    ListArchiveRulesPaginator,
    ListFindingsPaginator,
    ListPolicyGenerationsPaginator,
    ValidatePolicyPaginator,
)
from .type_defs import (
    CloudTrailDetailsTypeDef,
    ConfigurationTypeDef,
    CreateAccessPreviewResponseTypeDef,
    CreateAnalyzerResponseTypeDef,
    CriterionTypeDef,
    GetAccessPreviewResponseTypeDef,
    GetAnalyzedResourceResponseTypeDef,
    GetAnalyzerResponseTypeDef,
    GetArchiveRuleResponseTypeDef,
    GetFindingResponseTypeDef,
    GetGeneratedPolicyResponseTypeDef,
    InlineArchiveRuleTypeDef,
    ListAccessPreviewFindingsResponseTypeDef,
    ListAccessPreviewsResponseTypeDef,
    ListAnalyzedResourcesResponseTypeDef,
    ListAnalyzersResponseTypeDef,
    ListArchiveRulesResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListPolicyGenerationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PolicyGenerationDetailsTypeDef,
    SortCriteriaTypeDef,
    StartPolicyGenerationResponseTypeDef,
    ValidatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AccessAnalyzerClient",)


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


class AccessAnalyzerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def apply_archive_rule(
        self, *, analyzerArn: str, ruleName: str, clientToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.apply_archive_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#apply_archive_rule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#can_paginate)
        """

    def cancel_policy_generation(self, *, jobId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.cancel_policy_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#cancel_policy_generation)
        """

    def create_access_preview(
        self,
        *,
        analyzerArn: str,
        configurations: Dict[str, "ConfigurationTypeDef"],
        clientToken: str = None
    ) -> CreateAccessPreviewResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_access_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#create_access_preview)
        """

    def create_analyzer(
        self,
        *,
        analyzerName: str,
        type: TypeType,
        archiveRules: List[InlineArchiveRuleTypeDef] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAnalyzerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_analyzer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#create_analyzer)
        """

    def create_archive_rule(
        self,
        *,
        analyzerName: str,
        filter: Dict[str, "CriterionTypeDef"],
        ruleName: str,
        clientToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_archive_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#create_archive_rule)
        """

    def delete_analyzer(self, *, analyzerName: str, clientToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_analyzer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#delete_analyzer)
        """

    def delete_archive_rule(
        self, *, analyzerName: str, ruleName: str, clientToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_archive_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#delete_archive_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#generate_presigned_url)
        """

    def get_access_preview(
        self, *, accessPreviewId: str, analyzerArn: str
    ) -> GetAccessPreviewResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_access_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#get_access_preview)
        """

    def get_analyzed_resource(
        self, *, analyzerArn: str, resourceArn: str
    ) -> GetAnalyzedResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzed_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#get_analyzed_resource)
        """

    def get_analyzer(self, *, analyzerName: str) -> GetAnalyzerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#get_analyzer)
        """

    def get_archive_rule(
        self, *, analyzerName: str, ruleName: str
    ) -> GetArchiveRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_archive_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#get_archive_rule)
        """

    def get_finding(self, *, analyzerArn: str, id: str) -> GetFindingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_finding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#get_finding)
        """

    def get_generated_policy(
        self,
        *,
        jobId: str,
        includeResourcePlaceholders: bool = None,
        includeServiceLevelTemplate: bool = None
    ) -> GetGeneratedPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_generated_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#get_generated_policy)
        """

    def list_access_preview_findings(
        self,
        *,
        accessPreviewId: str,
        analyzerArn: str,
        filter: Dict[str, "CriterionTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListAccessPreviewFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_access_preview_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_access_preview_findings)
        """

    def list_access_previews(
        self, *, analyzerArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAccessPreviewsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_access_previews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_access_previews)
        """

    def list_analyzed_resources(
        self,
        *,
        analyzerArn: str,
        maxResults: int = None,
        nextToken: str = None,
        resourceType: ResourceTypeType = None
    ) -> ListAnalyzedResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzed_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_analyzed_resources)
        """

    def list_analyzers(
        self, *, maxResults: int = None, nextToken: str = None, type: TypeType = None
    ) -> ListAnalyzersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_analyzers)
        """

    def list_archive_rules(
        self, *, analyzerName: str, maxResults: int = None, nextToken: str = None
    ) -> ListArchiveRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_archive_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_archive_rules)
        """

    def list_findings(
        self,
        *,
        analyzerArn: str,
        filter: Dict[str, "CriterionTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        sort: SortCriteriaTypeDef = None
    ) -> ListFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_findings)
        """

    def list_policy_generations(
        self, *, maxResults: int = None, nextToken: str = None, principalArn: str = None
    ) -> ListPolicyGenerationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_policy_generations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_policy_generations)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#list_tags_for_resource)
        """

    def start_policy_generation(
        self,
        *,
        policyGenerationDetails: PolicyGenerationDetailsTypeDef,
        clientToken: str = None,
        cloudTrailDetails: CloudTrailDetailsTypeDef = None
    ) -> StartPolicyGenerationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_policy_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#start_policy_generation)
        """

    def start_resource_scan(self, *, analyzerArn: str, resourceArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_resource_scan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#start_resource_scan)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#untag_resource)
        """

    def update_archive_rule(
        self,
        *,
        analyzerName: str,
        filter: Dict[str, "CriterionTypeDef"],
        ruleName: str,
        clientToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_archive_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#update_archive_rule)
        """

    def update_findings(
        self,
        *,
        analyzerArn: str,
        status: FindingStatusUpdateType,
        clientToken: str = None,
        ids: List[str] = None,
        resourceArn: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#update_findings)
        """

    def validate_policy(
        self,
        *,
        policyDocument: str,
        policyType: PolicyTypeType,
        locale: LocaleType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ValidatePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Client.validate_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/client.html#validate_policy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_preview_findings"]
    ) -> ListAccessPreviewFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAccessPreviewFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listaccesspreviewfindingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_previews"]
    ) -> ListAccessPreviewsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAccessPreviews)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listaccesspreviewspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_analyzed_resources"]
    ) -> ListAnalyzedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzedResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listanalyzedresourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_analyzers"]) -> ListAnalyzersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listanalyzerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_archive_rules"]
    ) -> ListArchiveRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListArchiveRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listarchiverulespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listfindingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_generations"]
    ) -> ListPolicyGenerationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListPolicyGenerations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#listpolicygenerationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["validate_policy"]) -> ValidatePolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ValidatePolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators.html#validatepolicypaginator)
        """
