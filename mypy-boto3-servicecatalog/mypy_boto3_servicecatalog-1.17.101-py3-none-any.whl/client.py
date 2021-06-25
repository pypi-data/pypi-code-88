"""
Type annotations for servicecatalog service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_servicecatalog import ServiceCatalogClient

    client: ServiceCatalogClient = boto3.client("servicecatalog")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    DescribePortfolioShareTypeType,
    OrganizationNodeTypeType,
    PortfolioShareTypeType,
    ProductTypeType,
    ProductViewFilterByType,
    ProductViewSortByType,
    PropertyKeyType,
    ProvisioningArtifactGuidanceType,
    ServiceActionDefinitionKeyType,
    SortOrderType,
)
from .paginator import (
    ListAcceptedPortfolioSharesPaginator,
    ListConstraintsForPortfolioPaginator,
    ListLaunchPathsPaginator,
    ListOrganizationPortfolioAccessPaginator,
    ListPortfoliosForProductPaginator,
    ListPortfoliosPaginator,
    ListPrincipalsForPortfolioPaginator,
    ListProvisionedProductPlansPaginator,
    ListProvisioningArtifactsForServiceActionPaginator,
    ListRecordHistoryPaginator,
    ListResourcesForTagOptionPaginator,
    ListServiceActionsForProvisioningArtifactPaginator,
    ListServiceActionsPaginator,
    ListTagOptionsPaginator,
    ScanProvisionedProductsPaginator,
    SearchProductsAsAdminPaginator,
)
from .type_defs import (
    AccessLevelFilterTypeDef,
    BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef,
    BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef,
    CopyProductOutputTypeDef,
    CreateConstraintOutputTypeDef,
    CreatePortfolioOutputTypeDef,
    CreatePortfolioShareOutputTypeDef,
    CreateProductOutputTypeDef,
    CreateProvisionedProductPlanOutputTypeDef,
    CreateProvisioningArtifactOutputTypeDef,
    CreateServiceActionOutputTypeDef,
    CreateTagOptionOutputTypeDef,
    DeletePortfolioShareOutputTypeDef,
    DescribeConstraintOutputTypeDef,
    DescribeCopyProductStatusOutputTypeDef,
    DescribePortfolioOutputTypeDef,
    DescribePortfolioSharesOutputTypeDef,
    DescribePortfolioShareStatusOutputTypeDef,
    DescribeProductAsAdminOutputTypeDef,
    DescribeProductOutputTypeDef,
    DescribeProductViewOutputTypeDef,
    DescribeProvisionedProductOutputTypeDef,
    DescribeProvisionedProductPlanOutputTypeDef,
    DescribeProvisioningArtifactOutputTypeDef,
    DescribeProvisioningParametersOutputTypeDef,
    DescribeRecordOutputTypeDef,
    DescribeServiceActionExecutionParametersOutputTypeDef,
    DescribeServiceActionOutputTypeDef,
    DescribeTagOptionOutputTypeDef,
    ExecuteProvisionedProductPlanOutputTypeDef,
    ExecuteProvisionedProductServiceActionOutputTypeDef,
    GetAWSOrganizationsAccessStatusOutputTypeDef,
    GetProvisionedProductOutputsOutputTypeDef,
    ImportAsProvisionedProductOutputTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListBudgetsForResourceOutputTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListProvisioningArtifactsOutputTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListRecordHistorySearchFilterTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsOutputTypeDef,
    ListStackInstancesForProvisionedProductOutputTypeDef,
    ListTagOptionsFiltersTypeDef,
    ListTagOptionsOutputTypeDef,
    OrganizationNodeTypeDef,
    ProvisioningArtifactPropertiesTypeDef,
    ProvisioningParameterTypeDef,
    ProvisioningPreferencesTypeDef,
    ProvisionProductOutputTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminOutputTypeDef,
    SearchProductsOutputTypeDef,
    SearchProvisionedProductsOutputTypeDef,
    ServiceActionAssociationTypeDef,
    TagTypeDef,
    TerminateProvisionedProductOutputTypeDef,
    UpdateConstraintOutputTypeDef,
    UpdatePortfolioOutputTypeDef,
    UpdatePortfolioShareOutputTypeDef,
    UpdateProductOutputTypeDef,
    UpdateProvisionedProductOutputTypeDef,
    UpdateProvisionedProductPropertiesOutputTypeDef,
    UpdateProvisioningArtifactOutputTypeDef,
    UpdateProvisioningParameterTypeDef,
    UpdateProvisioningPreferencesTypeDef,
    UpdateServiceActionOutputTypeDef,
    UpdateTagOptionOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceCatalogClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InvalidParametersException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagOptionNotMigratedException: Type[BotocoreClientError]


class ServiceCatalogClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: PortfolioShareTypeType = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.accept_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#accept_portfolio_share)
        """

    def associate_budget_with_resource(self, *, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_budget_with_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate_budget_with_resource)
        """

    def associate_principal_with_portfolio(
        self,
        *,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: Literal["IAM"],
        AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_principal_with_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate_principal_with_portfolio)
        """

    def associate_product_with_portfolio(
        self,
        *,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str = None,
        SourcePortfolioId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_product_with_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate_product_with_portfolio)
        """

    def associate_service_action_with_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_service_action_with_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate_service_action_with_provisioning_artifact)
        """

    def associate_tag_option_with_resource(
        self, *, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_tag_option_with_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate_tag_option_with_resource)
        """

    def batch_associate_service_action_with_provisioning_artifact(
        self,
        *,
        ServiceActionAssociations: List[ServiceActionAssociationTypeDef],
        AcceptLanguage: str = None
    ) -> BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_associate_service_action_with_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#batch_associate_service_action_with_provisioning_artifact)
        """

    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        *,
        ServiceActionAssociations: List[ServiceActionAssociationTypeDef],
        AcceptLanguage: str = None
    ) -> BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_disassociate_service_action_from_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#batch_disassociate_service_action_from_provisioning_artifact)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#can_paginate)
        """

    def copy_product(
        self,
        *,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        TargetProductId: str = None,
        TargetProductName: str = None,
        SourceProvisioningArtifactIdentifiers: List[Dict[Literal["Id"], str]] = None,
        CopyOptions: List[Literal["CopyTags"]] = None
    ) -> CopyProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.copy_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#copy_product)
        """

    def create_constraint(
        self,
        *,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None
    ) -> CreateConstraintOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_constraint)
        """

    def create_portfolio(
        self,
        *,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_portfolio)
        """

    def create_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: "OrganizationNodeTypeDef" = None,
        ShareTagOptions: bool = None
    ) -> CreatePortfolioShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_portfolio_share)
        """

    def create_product(
        self,
        *,
        Name: str,
        Owner: str,
        ProductType: ProductTypeType,
        ProvisioningArtifactParameters: ProvisioningArtifactPropertiesTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_product)
        """

    def create_provisioned_product_plan(
        self,
        *,
        PlanName: str,
        PlanType: Literal["CLOUDFORMATION"],
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        NotificationArns: List[str] = None,
        PathId: str = None,
        ProvisioningParameters: List["UpdateProvisioningParameterTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateProvisionedProductPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_provisioned_product_plan)
        """

    def create_provisioning_artifact(
        self,
        *,
        ProductId: str,
        Parameters: ProvisioningArtifactPropertiesTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None
    ) -> CreateProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_provisioning_artifact)
        """

    def create_service_action(
        self,
        *,
        Name: str,
        DefinitionType: Literal["SSM_AUTOMATION"],
        Definition: Dict[ServiceActionDefinitionKeyType, str],
        IdempotencyToken: str,
        Description: str = None,
        AcceptLanguage: str = None
    ) -> CreateServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_service_action)
        """

    def create_tag_option(self, *, Key: str, Value: str) -> CreateTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.create_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create_tag_option)
        """

    def delete_constraint(self, *, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_constraint)
        """

    def delete_portfolio(self, *, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_portfolio)
        """

    def delete_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: "OrganizationNodeTypeDef" = None
    ) -> DeletePortfolioShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_portfolio_share)
        """

    def delete_product(self, *, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_product)
        """

    def delete_provisioned_product_plan(
        self, *, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_provisioned_product_plan)
        """

    def delete_provisioning_artifact(
        self, *, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_provisioning_artifact)
        """

    def delete_service_action(self, *, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_service_action)
        """

    def delete_tag_option(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete_tag_option)
        """

    def describe_constraint(
        self, *, Id: str, AcceptLanguage: str = None
    ) -> DescribeConstraintOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_constraint)
        """

    def describe_copy_product_status(
        self, *, CopyProductToken: str, AcceptLanguage: str = None
    ) -> DescribeCopyProductStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_copy_product_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_copy_product_status)
        """

    def describe_portfolio(
        self, *, Id: str, AcceptLanguage: str = None
    ) -> DescribePortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_portfolio)
        """

    def describe_portfolio_share_status(
        self, *, PortfolioShareToken: str
    ) -> DescribePortfolioShareStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio_share_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_portfolio_share_status)
        """

    def describe_portfolio_shares(
        self,
        *,
        PortfolioId: str,
        Type: DescribePortfolioShareTypeType,
        PageToken: str = None,
        PageSize: int = None
    ) -> DescribePortfolioSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_portfolio_shares)
        """

    def describe_product(
        self, *, AcceptLanguage: str = None, Id: str = None, Name: str = None
    ) -> DescribeProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_product)
        """

    def describe_product_as_admin(
        self,
        *,
        AcceptLanguage: str = None,
        Id: str = None,
        Name: str = None,
        SourcePortfolioId: str = None
    ) -> DescribeProductAsAdminOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_as_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_product_as_admin)
        """

    def describe_product_view(
        self, *, Id: str, AcceptLanguage: str = None
    ) -> DescribeProductViewOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_product_view)
        """

    def describe_provisioned_product(
        self, *, AcceptLanguage: str = None, Id: str = None, Name: str = None
    ) -> DescribeProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_provisioned_product)
        """

    def describe_provisioned_product_plan(
        self,
        *,
        PlanId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> DescribeProvisionedProductPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_provisioned_product_plan)
        """

    def describe_provisioning_artifact(
        self,
        *,
        AcceptLanguage: str = None,
        ProvisioningArtifactId: str = None,
        ProductId: str = None,
        ProvisioningArtifactName: str = None,
        ProductName: str = None,
        Verbose: bool = None
    ) -> DescribeProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_provisioning_artifact)
        """

    def describe_provisioning_parameters(
        self,
        *,
        AcceptLanguage: str = None,
        ProductId: str = None,
        ProductName: str = None,
        ProvisioningArtifactId: str = None,
        ProvisioningArtifactName: str = None,
        PathId: str = None,
        PathName: str = None
    ) -> DescribeProvisioningParametersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_provisioning_parameters)
        """

    def describe_record(
        self, *, Id: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> DescribeRecordOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_record)
        """

    def describe_service_action(
        self, *, Id: str, AcceptLanguage: str = None
    ) -> DescribeServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_service_action)
        """

    def describe_service_action_execution_parameters(
        self, *, ProvisionedProductId: str, ServiceActionId: str, AcceptLanguage: str = None
    ) -> DescribeServiceActionExecutionParametersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action_execution_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_service_action_execution_parameters)
        """

    def describe_tag_option(self, *, Id: str) -> DescribeTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe_tag_option)
        """

    def disable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.disable_aws_organizations_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disable_aws_organizations_access)
        """

    def disassociate_budget_from_resource(
        self, *, BudgetName: str, ResourceId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_budget_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate_budget_from_resource)
        """

    def disassociate_principal_from_portfolio(
        self, *, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_principal_from_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate_principal_from_portfolio)
        """

    def disassociate_product_from_portfolio(
        self, *, ProductId: str, PortfolioId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_product_from_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate_product_from_portfolio)
        """

    def disassociate_service_action_from_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_service_action_from_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate_service_action_from_provisioning_artifact)
        """

    def disassociate_tag_option_from_resource(
        self, *, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_tag_option_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate_tag_option_from_resource)
        """

    def enable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.enable_aws_organizations_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#enable_aws_organizations_access)
        """

    def execute_provisioned_product_plan(
        self, *, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None
    ) -> ExecuteProvisionedProductPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#execute_provisioned_product_plan)
        """

    def execute_provisioned_product_service_action(
        self,
        *,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: str = None,
        Parameters: Dict[str, List[str]] = None
    ) -> ExecuteProvisionedProductServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#execute_provisioned_product_service_action)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#generate_presigned_url)
        """

    def get_aws_organizations_access_status(self) -> GetAWSOrganizationsAccessStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.get_aws_organizations_access_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#get_aws_organizations_access_status)
        """

    def get_provisioned_product_outputs(
        self,
        *,
        AcceptLanguage: str = None,
        ProvisionedProductId: str = None,
        ProvisionedProductName: str = None,
        OutputKeys: List[str] = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> GetProvisionedProductOutputsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.get_provisioned_product_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#get_provisioned_product_outputs)
        """

    def import_as_provisioned_product(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        PhysicalId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None
    ) -> ImportAsProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.import_as_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#import_as_provisioned_product)
        """

    def list_accepted_portfolio_shares(
        self,
        *,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
        PortfolioShareType: PortfolioShareTypeType = None
    ) -> ListAcceptedPortfolioSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_accepted_portfolio_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_accepted_portfolio_shares)
        """

    def list_budgets_for_resource(
        self,
        *,
        ResourceId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListBudgetsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_budgets_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_budgets_for_resource)
        """

    def list_constraints_for_portfolio(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListConstraintsForPortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_constraints_for_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_constraints_for_portfolio)
        """

    def list_launch_paths(
        self,
        *,
        ProductId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListLaunchPathsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_launch_paths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_launch_paths)
        """

    def list_organization_portfolio_access(
        self,
        *,
        PortfolioId: str,
        OrganizationNodeType: OrganizationNodeTypeType,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None
    ) -> ListOrganizationPortfolioAccessOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_organization_portfolio_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_organization_portfolio_access)
        """

    def list_portfolio_access(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        OrganizationParentId: str = None,
        PageToken: str = None,
        PageSize: int = None
    ) -> ListPortfolioAccessOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolio_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_portfolio_access)
        """

    def list_portfolios(
        self, *, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> ListPortfoliosOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_portfolios)
        """

    def list_portfolios_for_product(
        self,
        *,
        ProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None
    ) -> ListPortfoliosForProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_portfolios_for_product)
        """

    def list_principals_for_portfolio(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListPrincipalsForPortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_principals_for_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_principals_for_portfolio)
        """

    def list_provisioned_product_plans(
        self,
        *,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None
    ) -> ListProvisionedProductPlansOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioned_product_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_provisioned_product_plans)
        """

    def list_provisioning_artifacts(
        self, *, ProductId: str, AcceptLanguage: str = None
    ) -> ListProvisioningArtifactsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_provisioning_artifacts)
        """

    def list_provisioning_artifacts_for_service_action(
        self,
        *,
        ServiceActionId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None
    ) -> ListProvisioningArtifactsForServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts_for_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_provisioning_artifacts_for_service_action)
        """

    def list_record_history(
        self,
        *,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        SearchFilter: ListRecordHistorySearchFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListRecordHistoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_record_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_record_history)
        """

    def list_resources_for_tag_option(
        self,
        *,
        TagOptionId: str,
        ResourceType: str = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListResourcesForTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_resources_for_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_resources_for_tag_option)
        """

    def list_service_actions(
        self, *, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> ListServiceActionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_service_actions)
        """

    def list_service_actions_for_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None
    ) -> ListServiceActionsForProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions_for_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_service_actions_for_provisioning_artifact)
        """

    def list_stack_instances_for_provisioned_product(
        self,
        *,
        ProvisionedProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None
    ) -> ListStackInstancesForProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_stack_instances_for_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_stack_instances_for_provisioned_product)
        """

    def list_tag_options(
        self,
        *,
        Filters: ListTagOptionsFiltersTypeDef = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ListTagOptionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.list_tag_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list_tag_options)
        """

    def provision_product(
        self,
        *,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        ProductName: str = None,
        ProvisioningArtifactId: str = None,
        ProvisioningArtifactName: str = None,
        PathId: str = None,
        PathName: str = None,
        ProvisioningParameters: List[ProvisioningParameterTypeDef] = None,
        ProvisioningPreferences: ProvisioningPreferencesTypeDef = None,
        Tags: List["TagTypeDef"] = None,
        NotificationArns: List[str] = None
    ) -> ProvisionProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.provision_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#provision_product)
        """

    def reject_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: PortfolioShareTypeType = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.reject_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#reject_portfolio_share)
        """

    def scan_provisioned_products(
        self,
        *,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> ScanProvisionedProductsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.scan_provisioned_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#scan_provisioned_products)
        """

    def search_products(
        self,
        *,
        AcceptLanguage: str = None,
        Filters: Dict[ProductViewFilterByType, List[str]] = None,
        PageSize: int = None,
        SortBy: ProductViewSortByType = None,
        SortOrder: SortOrderType = None,
        PageToken: str = None
    ) -> SearchProductsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#search_products)
        """

    def search_products_as_admin(
        self,
        *,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[ProductViewFilterByType, List[str]] = None,
        SortBy: ProductViewSortByType = None,
        SortOrder: SortOrderType = None,
        PageToken: str = None,
        PageSize: int = None,
        ProductSource: Literal["ACCOUNT"] = None
    ) -> SearchProductsAsAdminOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products_as_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#search_products_as_admin)
        """

    def search_provisioned_products(
        self,
        *,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        Filters: Dict[Literal["SearchQuery"], List[str]] = None,
        SortBy: str = None,
        SortOrder: SortOrderType = None,
        PageSize: int = None,
        PageToken: str = None
    ) -> SearchProvisionedProductsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.search_provisioned_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#search_provisioned_products)
        """

    def terminate_provisioned_product(
        self,
        *,
        TerminateToken: str,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        IgnoreErrors: bool = None,
        AcceptLanguage: str = None,
        RetainPhysicalResources: bool = None
    ) -> TerminateProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.terminate_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#terminate_provisioned_product)
        """

    def update_constraint(
        self,
        *,
        Id: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Parameters: str = None
    ) -> UpdateConstraintOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_constraint)
        """

    def update_portfolio(
        self,
        *,
        Id: str,
        AcceptLanguage: str = None,
        DisplayName: str = None,
        Description: str = None,
        ProviderName: str = None,
        AddTags: List["TagTypeDef"] = None,
        RemoveTags: List[str] = None
    ) -> UpdatePortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_portfolio)
        """

    def update_portfolio_share(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: "OrganizationNodeTypeDef" = None,
        ShareTagOptions: bool = None
    ) -> UpdatePortfolioShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_portfolio_share)
        """

    def update_product(
        self,
        *,
        Id: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Owner: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        AddTags: List["TagTypeDef"] = None,
        RemoveTags: List[str] = None
    ) -> UpdateProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_product)
        """

    def update_provisioned_product(
        self,
        *,
        UpdateToken: str,
        AcceptLanguage: str = None,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        ProductId: str = None,
        ProductName: str = None,
        ProvisioningArtifactId: str = None,
        ProvisioningArtifactName: str = None,
        PathId: str = None,
        PathName: str = None,
        ProvisioningParameters: List["UpdateProvisioningParameterTypeDef"] = None,
        ProvisioningPreferences: UpdateProvisioningPreferencesTypeDef = None,
        Tags: List["TagTypeDef"] = None
    ) -> UpdateProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_provisioned_product)
        """

    def update_provisioned_product_properties(
        self,
        *,
        ProvisionedProductId: str,
        ProvisionedProductProperties: Dict[PropertyKeyType, str],
        IdempotencyToken: str,
        AcceptLanguage: str = None
    ) -> UpdateProvisionedProductPropertiesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_provisioned_product_properties)
        """

    def update_provisioning_artifact(
        self,
        *,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Description: str = None,
        Active: bool = None,
        Guidance: ProvisioningArtifactGuidanceType = None
    ) -> UpdateProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_provisioning_artifact)
        """

    def update_service_action(
        self,
        *,
        Id: str,
        Name: str = None,
        Definition: Dict[ServiceActionDefinitionKeyType, str] = None,
        Description: str = None,
        AcceptLanguage: str = None
    ) -> UpdateServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_service_action)
        """

    def update_tag_option(
        self, *, Id: str, Value: str = None, Active: bool = None
    ) -> UpdateTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Client.update_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update_tag_option)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accepted_portfolio_shares"]
    ) -> ListAcceptedPortfolioSharesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listacceptedportfoliosharespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_constraints_for_portfolio"]
    ) -> ListConstraintsForPortfolioPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listconstraintsforportfoliopaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_paths"]
    ) -> ListLaunchPathsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listlaunchpathspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_portfolio_access"]
    ) -> ListOrganizationPortfolioAccessPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listorganizationportfolioaccesspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_portfolios"]) -> ListPortfoliosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listportfoliospaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_portfolios_for_product"]
    ) -> ListPortfoliosForProductPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listportfoliosforproductpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principals_for_portfolio"]
    ) -> ListPrincipalsForPortfolioPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listprincipalsforportfoliopaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioned_product_plans"]
    ) -> ListProvisionedProductPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listprovisionedproductplanspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_artifacts_for_service_action"]
    ) -> ListProvisioningArtifactsForServiceActionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listprovisioningartifactsforserviceactionpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_record_history"]
    ) -> ListRecordHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listrecordhistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources_for_tag_option"]
    ) -> ListResourcesForTagOptionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listresourcesfortagoptionpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_actions"]
    ) -> ListServiceActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listserviceactionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_actions_for_provisioning_artifact"]
    ) -> ListServiceActionsForProvisioningArtifactPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listserviceactionsforprovisioningartifactpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tag_options"]) -> ListTagOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listtagoptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["scan_provisioned_products"]
    ) -> ScanProvisionedProductsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#scanprovisionedproductspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_products_as_admin"]
    ) -> SearchProductsAsAdminPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#searchproductsasadminpaginator)
        """
