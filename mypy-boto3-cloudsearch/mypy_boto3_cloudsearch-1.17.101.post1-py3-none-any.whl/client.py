"""
Type annotations for cloudsearch service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearch import CloudSearchClient

    client: CloudSearchClient = boto3.client("cloudsearch")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    AnalysisSchemeTypeDef,
    BuildSuggestersResponseResponseTypeDef,
    CreateDomainResponseResponseTypeDef,
    DefineAnalysisSchemeResponseResponseTypeDef,
    DefineExpressionResponseResponseTypeDef,
    DefineIndexFieldResponseResponseTypeDef,
    DefineSuggesterResponseResponseTypeDef,
    DeleteAnalysisSchemeResponseResponseTypeDef,
    DeleteDomainResponseResponseTypeDef,
    DeleteExpressionResponseResponseTypeDef,
    DeleteIndexFieldResponseResponseTypeDef,
    DeleteSuggesterResponseResponseTypeDef,
    DescribeAnalysisSchemesResponseResponseTypeDef,
    DescribeAvailabilityOptionsResponseResponseTypeDef,
    DescribeDomainEndpointOptionsResponseResponseTypeDef,
    DescribeDomainsResponseResponseTypeDef,
    DescribeExpressionsResponseResponseTypeDef,
    DescribeIndexFieldsResponseResponseTypeDef,
    DescribeScalingParametersResponseResponseTypeDef,
    DescribeServiceAccessPoliciesResponseResponseTypeDef,
    DescribeSuggestersResponseResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    ExpressionTypeDef,
    IndexDocumentsResponseResponseTypeDef,
    IndexFieldTypeDef,
    ListDomainNamesResponseResponseTypeDef,
    ScalingParametersTypeDef,
    SuggesterTypeDef,
    UpdateAvailabilityOptionsResponseResponseTypeDef,
    UpdateDomainEndpointOptionsResponseResponseTypeDef,
    UpdateScalingParametersResponseResponseTypeDef,
    UpdateServiceAccessPoliciesResponseResponseTypeDef,
)

__all__ = ("CloudSearchClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CloudSearchClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def build_suggesters(self, *, DomainName: str) -> BuildSuggestersResponseResponseTypeDef:
        """
        Indexes the search suggestions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.build_suggesters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#build_suggesters)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#can_paginate)
        """

    def create_domain(self, *, DomainName: str) -> CreateDomainResponseResponseTypeDef:
        """
        Creates a new search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#create_domain)
        """

    def define_analysis_scheme(
        self, *, DomainName: str, AnalysisScheme: "AnalysisSchemeTypeDef"
    ) -> DefineAnalysisSchemeResponseResponseTypeDef:
        """
        Configures an analysis scheme that can be applied to a `text` or `text-array`
        field to define language-specific text processing options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.define_analysis_scheme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_analysis_scheme)
        """

    def define_expression(
        self, *, DomainName: str, Expression: "ExpressionTypeDef"
    ) -> DefineExpressionResponseResponseTypeDef:
        """
        Configures an ` Expression` for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.define_expression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_expression)
        """

    def define_index_field(
        self, *, DomainName: str, IndexField: "IndexFieldTypeDef"
    ) -> DefineIndexFieldResponseResponseTypeDef:
        """
        Configures an ` IndexField` for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.define_index_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_index_field)
        """

    def define_suggester(
        self, *, DomainName: str, Suggester: "SuggesterTypeDef"
    ) -> DefineSuggesterResponseResponseTypeDef:
        """
        Configures a suggester for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.define_suggester)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_suggester)
        """

    def delete_analysis_scheme(
        self, *, DomainName: str, AnalysisSchemeName: str
    ) -> DeleteAnalysisSchemeResponseResponseTypeDef:
        """
        Deletes an analysis scheme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.delete_analysis_scheme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_analysis_scheme)
        """

    def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseResponseTypeDef:
        """
        Permanently deletes a search domain and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_domain)
        """

    def delete_expression(
        self, *, DomainName: str, ExpressionName: str
    ) -> DeleteExpressionResponseResponseTypeDef:
        """
        Removes an ` Expression` from the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.delete_expression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_expression)
        """

    def delete_index_field(
        self, *, DomainName: str, IndexFieldName: str
    ) -> DeleteIndexFieldResponseResponseTypeDef:
        """
        Removes an ` IndexField` from the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.delete_index_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_index_field)
        """

    def delete_suggester(
        self, *, DomainName: str, SuggesterName: str
    ) -> DeleteSuggesterResponseResponseTypeDef:
        """
        Deletes a suggester.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.delete_suggester)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_suggester)
        """

    def describe_analysis_schemes(
        self, *, DomainName: str, AnalysisSchemeNames: List[str] = None, Deployed: bool = None
    ) -> DescribeAnalysisSchemesResponseResponseTypeDef:
        """
        Gets the analysis schemes configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_analysis_schemes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_analysis_schemes)
        """

    def describe_availability_options(
        self, *, DomainName: str, Deployed: bool = None
    ) -> DescribeAvailabilityOptionsResponseResponseTypeDef:
        """
        Gets the availability options configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_availability_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_availability_options)
        """

    def describe_domain_endpoint_options(
        self, *, DomainName: str, Deployed: bool = None
    ) -> DescribeDomainEndpointOptionsResponseResponseTypeDef:
        """
        Returns the domain's endpoint options, specifically whether all requests to the
        domain must arrive over HTTPS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_domain_endpoint_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_domain_endpoint_options)
        """

    def describe_domains(
        self, *, DomainNames: List[str] = None
    ) -> DescribeDomainsResponseResponseTypeDef:
        """
        Gets information about the search domains owned by this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_domains)
        """

    def describe_expressions(
        self, *, DomainName: str, ExpressionNames: List[str] = None, Deployed: bool = None
    ) -> DescribeExpressionsResponseResponseTypeDef:
        """
        Gets the expressions configured for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_expressions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_expressions)
        """

    def describe_index_fields(
        self, *, DomainName: str, FieldNames: List[str] = None, Deployed: bool = None
    ) -> DescribeIndexFieldsResponseResponseTypeDef:
        """
        Gets information about the index fields configured for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_index_fields)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_index_fields)
        """

    def describe_scaling_parameters(
        self, *, DomainName: str
    ) -> DescribeScalingParametersResponseResponseTypeDef:
        """
        Gets the scaling parameters configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_scaling_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_scaling_parameters)
        """

    def describe_service_access_policies(
        self, *, DomainName: str, Deployed: bool = None
    ) -> DescribeServiceAccessPoliciesResponseResponseTypeDef:
        """
        Gets information about the access policies that control access to the domain's
        document and search endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_service_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_service_access_policies)
        """

    def describe_suggesters(
        self, *, DomainName: str, SuggesterNames: List[str] = None, Deployed: bool = None
    ) -> DescribeSuggestersResponseResponseTypeDef:
        """
        Gets the suggesters configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.describe_suggesters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_suggesters)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#generate_presigned_url)
        """

    def index_documents(self, *, DomainName: str) -> IndexDocumentsResponseResponseTypeDef:
        """
        Tells the search domain to start indexing its documents using the latest
        indexing options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.index_documents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#index_documents)
        """

    def list_domain_names(self) -> ListDomainNamesResponseResponseTypeDef:
        """
        Lists all search domains owned by an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.list_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#list_domain_names)
        """

    def update_availability_options(
        self, *, DomainName: str, MultiAZ: bool
    ) -> UpdateAvailabilityOptionsResponseResponseTypeDef:
        """
        Configures the availability options for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.update_availability_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_availability_options)
        """

    def update_domain_endpoint_options(
        self, *, DomainName: str, DomainEndpointOptions: "DomainEndpointOptionsTypeDef"
    ) -> UpdateDomainEndpointOptionsResponseResponseTypeDef:
        """
        Updates the domain's endpoint options, specifically whether all requests to the
        domain must arrive over HTTPS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.update_domain_endpoint_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_domain_endpoint_options)
        """

    def update_scaling_parameters(
        self, *, DomainName: str, ScalingParameters: "ScalingParametersTypeDef"
    ) -> UpdateScalingParametersResponseResponseTypeDef:
        """
        Configures scaling parameters for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.update_scaling_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_scaling_parameters)
        """

    def update_service_access_policies(
        self, *, DomainName: str, AccessPolicies: str
    ) -> UpdateServiceAccessPoliciesResponseResponseTypeDef:
        """
        Configures the access rules that control access to the domain's document and
        search endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudsearch.html#CloudSearch.Client.update_service_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_service_access_policies)
        """
