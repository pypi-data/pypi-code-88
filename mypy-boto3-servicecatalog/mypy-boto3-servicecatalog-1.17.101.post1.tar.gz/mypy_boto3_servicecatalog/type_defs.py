"""
Type annotations for servicecatalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog.type_defs import AcceptPortfolioShareInputTypeDef

    data: AcceptPortfolioShareInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessLevelFilterKeyType,
    AccessStatusType,
    ChangeActionType,
    CopyProductStatusType,
    DescribePortfolioShareTypeType,
    EvaluationTypeType,
    OrganizationNodeTypeType,
    PortfolioShareTypeType,
    ProductTypeType,
    ProductViewFilterByType,
    ProductViewSortByType,
    PropertyKeyType,
    ProvisionedProductPlanStatusType,
    ProvisionedProductStatusType,
    ProvisioningArtifactGuidanceType,
    ProvisioningArtifactTypeType,
    RecordStatusType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ServiceActionAssociationErrorCodeType,
    ServiceActionDefinitionKeyType,
    ShareStatusType,
    SortOrderType,
    StackInstanceStatusType,
    StackSetOperationTypeType,
    StatusType,
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
    "AcceptPortfolioShareInputTypeDef",
    "AccessLevelFilterTypeDef",
    "AssociateBudgetWithResourceInputTypeDef",
    "AssociatePrincipalWithPortfolioInputTypeDef",
    "AssociateProductWithPortfolioInputTypeDef",
    "AssociateServiceActionWithProvisioningArtifactInputTypeDef",
    "AssociateTagOptionWithResourceInputTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactOutputResponseTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputResponseTypeDef",
    "BudgetDetailTypeDef",
    "CloudWatchDashboardTypeDef",
    "ConstraintDetailTypeDef",
    "ConstraintSummaryTypeDef",
    "CopyProductInputTypeDef",
    "CopyProductOutputResponseTypeDef",
    "CreateConstraintInputTypeDef",
    "CreateConstraintOutputResponseTypeDef",
    "CreatePortfolioInputTypeDef",
    "CreatePortfolioOutputResponseTypeDef",
    "CreatePortfolioShareInputTypeDef",
    "CreatePortfolioShareOutputResponseTypeDef",
    "CreateProductInputTypeDef",
    "CreateProductOutputResponseTypeDef",
    "CreateProvisionedProductPlanInputTypeDef",
    "CreateProvisionedProductPlanOutputResponseTypeDef",
    "CreateProvisioningArtifactInputTypeDef",
    "CreateProvisioningArtifactOutputResponseTypeDef",
    "CreateServiceActionInputTypeDef",
    "CreateServiceActionOutputResponseTypeDef",
    "CreateTagOptionInputTypeDef",
    "CreateTagOptionOutputResponseTypeDef",
    "DeleteConstraintInputTypeDef",
    "DeletePortfolioInputTypeDef",
    "DeletePortfolioShareInputTypeDef",
    "DeletePortfolioShareOutputResponseTypeDef",
    "DeleteProductInputTypeDef",
    "DeleteProvisionedProductPlanInputTypeDef",
    "DeleteProvisioningArtifactInputTypeDef",
    "DeleteServiceActionInputTypeDef",
    "DeleteTagOptionInputTypeDef",
    "DescribeConstraintInputTypeDef",
    "DescribeConstraintOutputResponseTypeDef",
    "DescribeCopyProductStatusInputTypeDef",
    "DescribeCopyProductStatusOutputResponseTypeDef",
    "DescribePortfolioInputTypeDef",
    "DescribePortfolioOutputResponseTypeDef",
    "DescribePortfolioShareStatusInputTypeDef",
    "DescribePortfolioShareStatusOutputResponseTypeDef",
    "DescribePortfolioSharesInputTypeDef",
    "DescribePortfolioSharesOutputResponseTypeDef",
    "DescribeProductAsAdminInputTypeDef",
    "DescribeProductAsAdminOutputResponseTypeDef",
    "DescribeProductInputTypeDef",
    "DescribeProductOutputResponseTypeDef",
    "DescribeProductViewInputTypeDef",
    "DescribeProductViewOutputResponseTypeDef",
    "DescribeProvisionedProductInputTypeDef",
    "DescribeProvisionedProductOutputResponseTypeDef",
    "DescribeProvisionedProductPlanInputTypeDef",
    "DescribeProvisionedProductPlanOutputResponseTypeDef",
    "DescribeProvisioningArtifactInputTypeDef",
    "DescribeProvisioningArtifactOutputResponseTypeDef",
    "DescribeProvisioningParametersInputTypeDef",
    "DescribeProvisioningParametersOutputResponseTypeDef",
    "DescribeRecordInputTypeDef",
    "DescribeRecordOutputResponseTypeDef",
    "DescribeServiceActionExecutionParametersInputTypeDef",
    "DescribeServiceActionExecutionParametersOutputResponseTypeDef",
    "DescribeServiceActionInputTypeDef",
    "DescribeServiceActionOutputResponseTypeDef",
    "DescribeTagOptionInputTypeDef",
    "DescribeTagOptionOutputResponseTypeDef",
    "DisassociateBudgetFromResourceInputTypeDef",
    "DisassociatePrincipalFromPortfolioInputTypeDef",
    "DisassociateProductFromPortfolioInputTypeDef",
    "DisassociateServiceActionFromProvisioningArtifactInputTypeDef",
    "DisassociateTagOptionFromResourceInputTypeDef",
    "ExecuteProvisionedProductPlanInputTypeDef",
    "ExecuteProvisionedProductPlanOutputResponseTypeDef",
    "ExecuteProvisionedProductServiceActionInputTypeDef",
    "ExecuteProvisionedProductServiceActionOutputResponseTypeDef",
    "ExecutionParameterTypeDef",
    "FailedServiceActionAssociationTypeDef",
    "GetAWSOrganizationsAccessStatusOutputResponseTypeDef",
    "GetProvisionedProductOutputsInputTypeDef",
    "GetProvisionedProductOutputsOutputResponseTypeDef",
    "ImportAsProvisionedProductInputTypeDef",
    "ImportAsProvisionedProductOutputResponseTypeDef",
    "LaunchPathSummaryTypeDef",
    "LaunchPathTypeDef",
    "ListAcceptedPortfolioSharesInputTypeDef",
    "ListAcceptedPortfolioSharesOutputResponseTypeDef",
    "ListBudgetsForResourceInputTypeDef",
    "ListBudgetsForResourceOutputResponseTypeDef",
    "ListConstraintsForPortfolioInputTypeDef",
    "ListConstraintsForPortfolioOutputResponseTypeDef",
    "ListLaunchPathsInputTypeDef",
    "ListLaunchPathsOutputResponseTypeDef",
    "ListOrganizationPortfolioAccessInputTypeDef",
    "ListOrganizationPortfolioAccessOutputResponseTypeDef",
    "ListPortfolioAccessInputTypeDef",
    "ListPortfolioAccessOutputResponseTypeDef",
    "ListPortfoliosForProductInputTypeDef",
    "ListPortfoliosForProductOutputResponseTypeDef",
    "ListPortfoliosInputTypeDef",
    "ListPortfoliosOutputResponseTypeDef",
    "ListPrincipalsForPortfolioInputTypeDef",
    "ListPrincipalsForPortfolioOutputResponseTypeDef",
    "ListProvisionedProductPlansInputTypeDef",
    "ListProvisionedProductPlansOutputResponseTypeDef",
    "ListProvisioningArtifactsForServiceActionInputTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputResponseTypeDef",
    "ListProvisioningArtifactsInputTypeDef",
    "ListProvisioningArtifactsOutputResponseTypeDef",
    "ListRecordHistoryInputTypeDef",
    "ListRecordHistoryOutputResponseTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ListResourcesForTagOptionInputTypeDef",
    "ListResourcesForTagOptionOutputResponseTypeDef",
    "ListServiceActionsForProvisioningArtifactInputTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputResponseTypeDef",
    "ListServiceActionsInputTypeDef",
    "ListServiceActionsOutputResponseTypeDef",
    "ListStackInstancesForProvisionedProductInputTypeDef",
    "ListStackInstancesForProvisionedProductOutputResponseTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "ListTagOptionsInputTypeDef",
    "ListTagOptionsOutputResponseTypeDef",
    "OrganizationNodeTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "PortfolioDetailTypeDef",
    "PortfolioShareDetailTypeDef",
    "PrincipalTypeDef",
    "ProductViewAggregationValueTypeDef",
    "ProductViewDetailTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisionProductInputTypeDef",
    "ProvisionProductOutputResponseTypeDef",
    "ProvisionedProductAttributeTypeDef",
    "ProvisionedProductDetailTypeDef",
    "ProvisionedProductPlanDetailsTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ProvisioningArtifactDetailTypeDef",
    "ProvisioningArtifactOutputTypeDef",
    "ProvisioningArtifactParameterTypeDef",
    "ProvisioningArtifactPreferencesTypeDef",
    "ProvisioningArtifactPropertiesTypeDef",
    "ProvisioningArtifactSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "ProvisioningParameterTypeDef",
    "ProvisioningPreferencesTypeDef",
    "RecordDetailTypeDef",
    "RecordErrorTypeDef",
    "RecordOutputTypeDef",
    "RecordTagTypeDef",
    "RejectPortfolioShareInputTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceDetailTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "ScanProvisionedProductsInputTypeDef",
    "ScanProvisionedProductsOutputResponseTypeDef",
    "SearchProductsAsAdminInputTypeDef",
    "SearchProductsAsAdminOutputResponseTypeDef",
    "SearchProductsInputTypeDef",
    "SearchProductsOutputResponseTypeDef",
    "SearchProvisionedProductsInputTypeDef",
    "SearchProvisionedProductsOutputResponseTypeDef",
    "ServiceActionAssociationTypeDef",
    "ServiceActionDetailTypeDef",
    "ServiceActionSummaryTypeDef",
    "ShareDetailsTypeDef",
    "ShareErrorTypeDef",
    "StackInstanceTypeDef",
    "TagOptionDetailTypeDef",
    "TagOptionSummaryTypeDef",
    "TagTypeDef",
    "TerminateProvisionedProductInputTypeDef",
    "TerminateProvisionedProductOutputResponseTypeDef",
    "UpdateConstraintInputTypeDef",
    "UpdateConstraintOutputResponseTypeDef",
    "UpdatePortfolioInputTypeDef",
    "UpdatePortfolioOutputResponseTypeDef",
    "UpdatePortfolioShareInputTypeDef",
    "UpdatePortfolioShareOutputResponseTypeDef",
    "UpdateProductInputTypeDef",
    "UpdateProductOutputResponseTypeDef",
    "UpdateProvisionedProductInputTypeDef",
    "UpdateProvisionedProductOutputResponseTypeDef",
    "UpdateProvisionedProductPropertiesInputTypeDef",
    "UpdateProvisionedProductPropertiesOutputResponseTypeDef",
    "UpdateProvisioningArtifactInputTypeDef",
    "UpdateProvisioningArtifactOutputResponseTypeDef",
    "UpdateProvisioningParameterTypeDef",
    "UpdateProvisioningPreferencesTypeDef",
    "UpdateServiceActionInputTypeDef",
    "UpdateServiceActionOutputResponseTypeDef",
    "UpdateTagOptionInputTypeDef",
    "UpdateTagOptionOutputResponseTypeDef",
    "UsageInstructionTypeDef",
)

_RequiredAcceptPortfolioShareInputTypeDef = TypedDict(
    "_RequiredAcceptPortfolioShareInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalAcceptPortfolioShareInputTypeDef = TypedDict(
    "_OptionalAcceptPortfolioShareInputTypeDef",
    {
        "AcceptLanguage": str,
        "PortfolioShareType": PortfolioShareTypeType,
    },
    total=False,
)


class AcceptPortfolioShareInputTypeDef(
    _RequiredAcceptPortfolioShareInputTypeDef, _OptionalAcceptPortfolioShareInputTypeDef
):
    pass


AccessLevelFilterTypeDef = TypedDict(
    "AccessLevelFilterTypeDef",
    {
        "Key": AccessLevelFilterKeyType,
        "Value": str,
    },
    total=False,
)

AssociateBudgetWithResourceInputTypeDef = TypedDict(
    "AssociateBudgetWithResourceInputTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)

_RequiredAssociatePrincipalWithPortfolioInputTypeDef = TypedDict(
    "_RequiredAssociatePrincipalWithPortfolioInputTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
        "PrincipalType": Literal["IAM"],
    },
)
_OptionalAssociatePrincipalWithPortfolioInputTypeDef = TypedDict(
    "_OptionalAssociatePrincipalWithPortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class AssociatePrincipalWithPortfolioInputTypeDef(
    _RequiredAssociatePrincipalWithPortfolioInputTypeDef,
    _OptionalAssociatePrincipalWithPortfolioInputTypeDef,
):
    pass


_RequiredAssociateProductWithPortfolioInputTypeDef = TypedDict(
    "_RequiredAssociateProductWithPortfolioInputTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
    },
)
_OptionalAssociateProductWithPortfolioInputTypeDef = TypedDict(
    "_OptionalAssociateProductWithPortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
        "SourcePortfolioId": str,
    },
    total=False,
)


class AssociateProductWithPortfolioInputTypeDef(
    _RequiredAssociateProductWithPortfolioInputTypeDef,
    _OptionalAssociateProductWithPortfolioInputTypeDef,
):
    pass


_RequiredAssociateServiceActionWithProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredAssociateServiceActionWithProvisioningArtifactInputTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
    },
)
_OptionalAssociateServiceActionWithProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalAssociateServiceActionWithProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class AssociateServiceActionWithProvisioningArtifactInputTypeDef(
    _RequiredAssociateServiceActionWithProvisioningArtifactInputTypeDef,
    _OptionalAssociateServiceActionWithProvisioningArtifactInputTypeDef,
):
    pass


AssociateTagOptionWithResourceInputTypeDef = TypedDict(
    "AssociateTagOptionWithResourceInputTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)

_RequiredBatchAssociateServiceActionWithProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredBatchAssociateServiceActionWithProvisioningArtifactInputTypeDef",
    {
        "ServiceActionAssociations": List["ServiceActionAssociationTypeDef"],
    },
)
_OptionalBatchAssociateServiceActionWithProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalBatchAssociateServiceActionWithProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef(
    _RequiredBatchAssociateServiceActionWithProvisioningArtifactInputTypeDef,
    _OptionalBatchAssociateServiceActionWithProvisioningArtifactInputTypeDef,
):
    pass


BatchAssociateServiceActionWithProvisioningArtifactOutputResponseTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactOutputResponseTypeDef",
    {
        "FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredBatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef",
    {
        "ServiceActionAssociations": List["ServiceActionAssociationTypeDef"],
    },
)
_OptionalBatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalBatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef(
    _RequiredBatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef,
    _OptionalBatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef,
):
    pass


BatchDisassociateServiceActionFromProvisioningArtifactOutputResponseTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputResponseTypeDef",
    {
        "FailedServiceActionAssociations": List["FailedServiceActionAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BudgetDetailTypeDef = TypedDict(
    "BudgetDetailTypeDef",
    {
        "BudgetName": str,
    },
    total=False,
)

CloudWatchDashboardTypeDef = TypedDict(
    "CloudWatchDashboardTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ConstraintDetailTypeDef = TypedDict(
    "ConstraintDetailTypeDef",
    {
        "ConstraintId": str,
        "Type": str,
        "Description": str,
        "Owner": str,
        "ProductId": str,
        "PortfolioId": str,
    },
    total=False,
)

ConstraintSummaryTypeDef = TypedDict(
    "ConstraintSummaryTypeDef",
    {
        "Type": str,
        "Description": str,
    },
    total=False,
)

_RequiredCopyProductInputTypeDef = TypedDict(
    "_RequiredCopyProductInputTypeDef",
    {
        "SourceProductArn": str,
        "IdempotencyToken": str,
    },
)
_OptionalCopyProductInputTypeDef = TypedDict(
    "_OptionalCopyProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "TargetProductId": str,
        "TargetProductName": str,
        "SourceProvisioningArtifactIdentifiers": List[Dict[Literal["Id"], str]],
        "CopyOptions": List[Literal["CopyTags"]],
    },
    total=False,
)


class CopyProductInputTypeDef(_RequiredCopyProductInputTypeDef, _OptionalCopyProductInputTypeDef):
    pass


CopyProductOutputResponseTypeDef = TypedDict(
    "CopyProductOutputResponseTypeDef",
    {
        "CopyProductToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConstraintInputTypeDef = TypedDict(
    "_RequiredCreateConstraintInputTypeDef",
    {
        "PortfolioId": str,
        "ProductId": str,
        "Parameters": str,
        "Type": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateConstraintInputTypeDef = TypedDict(
    "_OptionalCreateConstraintInputTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
    },
    total=False,
)


class CreateConstraintInputTypeDef(
    _RequiredCreateConstraintInputTypeDef, _OptionalCreateConstraintInputTypeDef
):
    pass


CreateConstraintOutputResponseTypeDef = TypedDict(
    "CreateConstraintOutputResponseTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePortfolioInputTypeDef = TypedDict(
    "_RequiredCreatePortfolioInputTypeDef",
    {
        "DisplayName": str,
        "ProviderName": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreatePortfolioInputTypeDef = TypedDict(
    "_OptionalCreatePortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePortfolioInputTypeDef(
    _RequiredCreatePortfolioInputTypeDef, _OptionalCreatePortfolioInputTypeDef
):
    pass


CreatePortfolioOutputResponseTypeDef = TypedDict(
    "CreatePortfolioOutputResponseTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePortfolioShareInputTypeDef = TypedDict(
    "_RequiredCreatePortfolioShareInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalCreatePortfolioShareInputTypeDef = TypedDict(
    "_OptionalCreatePortfolioShareInputTypeDef",
    {
        "AcceptLanguage": str,
        "AccountId": str,
        "OrganizationNode": "OrganizationNodeTypeDef",
        "ShareTagOptions": bool,
    },
    total=False,
)


class CreatePortfolioShareInputTypeDef(
    _RequiredCreatePortfolioShareInputTypeDef, _OptionalCreatePortfolioShareInputTypeDef
):
    pass


CreatePortfolioShareOutputResponseTypeDef = TypedDict(
    "CreatePortfolioShareOutputResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProductInputTypeDef = TypedDict(
    "_RequiredCreateProductInputTypeDef",
    {
        "Name": str,
        "Owner": str,
        "ProductType": ProductTypeType,
        "ProvisioningArtifactParameters": "ProvisioningArtifactPropertiesTypeDef",
        "IdempotencyToken": str,
    },
)
_OptionalCreateProductInputTypeDef = TypedDict(
    "_OptionalCreateProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
        "Distributor": str,
        "SupportDescription": str,
        "SupportEmail": str,
        "SupportUrl": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProductInputTypeDef(
    _RequiredCreateProductInputTypeDef, _OptionalCreateProductInputTypeDef
):
    pass


CreateProductOutputResponseTypeDef = TypedDict(
    "CreateProductOutputResponseTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisionedProductPlanInputTypeDef = TypedDict(
    "_RequiredCreateProvisionedProductPlanInputTypeDef",
    {
        "PlanName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateProvisionedProductPlanInputTypeDef = TypedDict(
    "_OptionalCreateProvisionedProductPlanInputTypeDef",
    {
        "AcceptLanguage": str,
        "NotificationArns": List[str],
        "PathId": str,
        "ProvisioningParameters": List["UpdateProvisioningParameterTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProvisionedProductPlanInputTypeDef(
    _RequiredCreateProvisionedProductPlanInputTypeDef,
    _OptionalCreateProvisionedProductPlanInputTypeDef,
):
    pass


CreateProvisionedProductPlanOutputResponseTypeDef = TypedDict(
    "CreateProvisionedProductPlanOutputResponseTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredCreateProvisioningArtifactInputTypeDef",
    {
        "ProductId": str,
        "Parameters": "ProvisioningArtifactPropertiesTypeDef",
        "IdempotencyToken": str,
    },
)
_OptionalCreateProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalCreateProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class CreateProvisioningArtifactInputTypeDef(
    _RequiredCreateProvisioningArtifactInputTypeDef, _OptionalCreateProvisioningArtifactInputTypeDef
):
    pass


CreateProvisioningArtifactOutputResponseTypeDef = TypedDict(
    "CreateProvisioningArtifactOutputResponseTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceActionInputTypeDef = TypedDict(
    "_RequiredCreateServiceActionInputTypeDef",
    {
        "Name": str,
        "DefinitionType": Literal["SSM_AUTOMATION"],
        "Definition": Dict[ServiceActionDefinitionKeyType, str],
        "IdempotencyToken": str,
    },
)
_OptionalCreateServiceActionInputTypeDef = TypedDict(
    "_OptionalCreateServiceActionInputTypeDef",
    {
        "Description": str,
        "AcceptLanguage": str,
    },
    total=False,
)


class CreateServiceActionInputTypeDef(
    _RequiredCreateServiceActionInputTypeDef, _OptionalCreateServiceActionInputTypeDef
):
    pass


CreateServiceActionOutputResponseTypeDef = TypedDict(
    "CreateServiceActionOutputResponseTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagOptionInputTypeDef = TypedDict(
    "CreateTagOptionInputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

CreateTagOptionOutputResponseTypeDef = TypedDict(
    "CreateTagOptionOutputResponseTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteConstraintInputTypeDef = TypedDict(
    "_RequiredDeleteConstraintInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteConstraintInputTypeDef = TypedDict(
    "_OptionalDeleteConstraintInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DeleteConstraintInputTypeDef(
    _RequiredDeleteConstraintInputTypeDef, _OptionalDeleteConstraintInputTypeDef
):
    pass


_RequiredDeletePortfolioInputTypeDef = TypedDict(
    "_RequiredDeletePortfolioInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeletePortfolioInputTypeDef = TypedDict(
    "_OptionalDeletePortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DeletePortfolioInputTypeDef(
    _RequiredDeletePortfolioInputTypeDef, _OptionalDeletePortfolioInputTypeDef
):
    pass


_RequiredDeletePortfolioShareInputTypeDef = TypedDict(
    "_RequiredDeletePortfolioShareInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalDeletePortfolioShareInputTypeDef = TypedDict(
    "_OptionalDeletePortfolioShareInputTypeDef",
    {
        "AcceptLanguage": str,
        "AccountId": str,
        "OrganizationNode": "OrganizationNodeTypeDef",
    },
    total=False,
)


class DeletePortfolioShareInputTypeDef(
    _RequiredDeletePortfolioShareInputTypeDef, _OptionalDeletePortfolioShareInputTypeDef
):
    pass


DeletePortfolioShareOutputResponseTypeDef = TypedDict(
    "DeletePortfolioShareOutputResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProductInputTypeDef = TypedDict(
    "_RequiredDeleteProductInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteProductInputTypeDef = TypedDict(
    "_OptionalDeleteProductInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DeleteProductInputTypeDef(
    _RequiredDeleteProductInputTypeDef, _OptionalDeleteProductInputTypeDef
):
    pass


_RequiredDeleteProvisionedProductPlanInputTypeDef = TypedDict(
    "_RequiredDeleteProvisionedProductPlanInputTypeDef",
    {
        "PlanId": str,
    },
)
_OptionalDeleteProvisionedProductPlanInputTypeDef = TypedDict(
    "_OptionalDeleteProvisionedProductPlanInputTypeDef",
    {
        "AcceptLanguage": str,
        "IgnoreErrors": bool,
    },
    total=False,
)


class DeleteProvisionedProductPlanInputTypeDef(
    _RequiredDeleteProvisionedProductPlanInputTypeDef,
    _OptionalDeleteProvisionedProductPlanInputTypeDef,
):
    pass


_RequiredDeleteProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredDeleteProvisioningArtifactInputTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalDeleteProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalDeleteProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DeleteProvisioningArtifactInputTypeDef(
    _RequiredDeleteProvisioningArtifactInputTypeDef, _OptionalDeleteProvisioningArtifactInputTypeDef
):
    pass


_RequiredDeleteServiceActionInputTypeDef = TypedDict(
    "_RequiredDeleteServiceActionInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteServiceActionInputTypeDef = TypedDict(
    "_OptionalDeleteServiceActionInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DeleteServiceActionInputTypeDef(
    _RequiredDeleteServiceActionInputTypeDef, _OptionalDeleteServiceActionInputTypeDef
):
    pass


DeleteTagOptionInputTypeDef = TypedDict(
    "DeleteTagOptionInputTypeDef",
    {
        "Id": str,
    },
)

_RequiredDescribeConstraintInputTypeDef = TypedDict(
    "_RequiredDescribeConstraintInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeConstraintInputTypeDef = TypedDict(
    "_OptionalDescribeConstraintInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DescribeConstraintInputTypeDef(
    _RequiredDescribeConstraintInputTypeDef, _OptionalDescribeConstraintInputTypeDef
):
    pass


DescribeConstraintOutputResponseTypeDef = TypedDict(
    "DescribeConstraintOutputResponseTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCopyProductStatusInputTypeDef = TypedDict(
    "_RequiredDescribeCopyProductStatusInputTypeDef",
    {
        "CopyProductToken": str,
    },
)
_OptionalDescribeCopyProductStatusInputTypeDef = TypedDict(
    "_OptionalDescribeCopyProductStatusInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DescribeCopyProductStatusInputTypeDef(
    _RequiredDescribeCopyProductStatusInputTypeDef, _OptionalDescribeCopyProductStatusInputTypeDef
):
    pass


DescribeCopyProductStatusOutputResponseTypeDef = TypedDict(
    "DescribeCopyProductStatusOutputResponseTypeDef",
    {
        "CopyProductStatus": CopyProductStatusType,
        "TargetProductId": str,
        "StatusDetail": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePortfolioInputTypeDef = TypedDict(
    "_RequiredDescribePortfolioInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribePortfolioInputTypeDef = TypedDict(
    "_OptionalDescribePortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DescribePortfolioInputTypeDef(
    _RequiredDescribePortfolioInputTypeDef, _OptionalDescribePortfolioInputTypeDef
):
    pass


DescribePortfolioOutputResponseTypeDef = TypedDict(
    "DescribePortfolioOutputResponseTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortfolioShareStatusInputTypeDef = TypedDict(
    "DescribePortfolioShareStatusInputTypeDef",
    {
        "PortfolioShareToken": str,
    },
)

DescribePortfolioShareStatusOutputResponseTypeDef = TypedDict(
    "DescribePortfolioShareStatusOutputResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": ShareStatusType,
        "ShareDetails": "ShareDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePortfolioSharesInputTypeDef = TypedDict(
    "_RequiredDescribePortfolioSharesInputTypeDef",
    {
        "PortfolioId": str,
        "Type": DescribePortfolioShareTypeType,
    },
)
_OptionalDescribePortfolioSharesInputTypeDef = TypedDict(
    "_OptionalDescribePortfolioSharesInputTypeDef",
    {
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)


class DescribePortfolioSharesInputTypeDef(
    _RequiredDescribePortfolioSharesInputTypeDef, _OptionalDescribePortfolioSharesInputTypeDef
):
    pass


DescribePortfolioSharesOutputResponseTypeDef = TypedDict(
    "DescribePortfolioSharesOutputResponseTypeDef",
    {
        "NextPageToken": str,
        "PortfolioShareDetails": List["PortfolioShareDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductAsAdminInputTypeDef = TypedDict(
    "DescribeProductAsAdminInputTypeDef",
    {
        "AcceptLanguage": str,
        "Id": str,
        "Name": str,
        "SourcePortfolioId": str,
    },
    total=False,
)

DescribeProductAsAdminOutputResponseTypeDef = TypedDict(
    "DescribeProductAsAdminOutputResponseTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "ProvisioningArtifactSummaries": List["ProvisioningArtifactSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "TagOptions": List["TagOptionDetailTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProductInputTypeDef = TypedDict(
    "DescribeProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "Id": str,
        "Name": str,
    },
    total=False,
)

DescribeProductOutputResponseTypeDef = TypedDict(
    "DescribeProductOutputResponseTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
        "Budgets": List["BudgetDetailTypeDef"],
        "LaunchPaths": List["LaunchPathTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProductViewInputTypeDef = TypedDict(
    "_RequiredDescribeProductViewInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeProductViewInputTypeDef = TypedDict(
    "_OptionalDescribeProductViewInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DescribeProductViewInputTypeDef(
    _RequiredDescribeProductViewInputTypeDef, _OptionalDescribeProductViewInputTypeDef
):
    pass


DescribeProductViewOutputResponseTypeDef = TypedDict(
    "DescribeProductViewOutputResponseTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifacts": List["ProvisioningArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisionedProductInputTypeDef = TypedDict(
    "DescribeProvisionedProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "Id": str,
        "Name": str,
    },
    total=False,
)

DescribeProvisionedProductOutputResponseTypeDef = TypedDict(
    "DescribeProvisionedProductOutputResponseTypeDef",
    {
        "ProvisionedProductDetail": "ProvisionedProductDetailTypeDef",
        "CloudWatchDashboards": List["CloudWatchDashboardTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProvisionedProductPlanInputTypeDef = TypedDict(
    "_RequiredDescribeProvisionedProductPlanInputTypeDef",
    {
        "PlanId": str,
    },
)
_OptionalDescribeProvisionedProductPlanInputTypeDef = TypedDict(
    "_OptionalDescribeProvisionedProductPlanInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)


class DescribeProvisionedProductPlanInputTypeDef(
    _RequiredDescribeProvisionedProductPlanInputTypeDef,
    _OptionalDescribeProvisionedProductPlanInputTypeDef,
):
    pass


DescribeProvisionedProductPlanOutputResponseTypeDef = TypedDict(
    "DescribeProvisionedProductPlanOutputResponseTypeDef",
    {
        "ProvisionedProductPlanDetails": "ProvisionedProductPlanDetailsTypeDef",
        "ResourceChanges": List["ResourceChangeTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningArtifactInputTypeDef = TypedDict(
    "DescribeProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisioningArtifactId": str,
        "ProductId": str,
        "ProvisioningArtifactName": str,
        "ProductName": str,
        "Verbose": bool,
    },
    total=False,
)

DescribeProvisioningArtifactOutputResponseTypeDef = TypedDict(
    "DescribeProvisioningArtifactOutputResponseTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProvisioningParametersInputTypeDef = TypedDict(
    "DescribeProvisioningParametersInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "PathId": str,
        "PathName": str,
    },
    total=False,
)

DescribeProvisioningParametersOutputResponseTypeDef = TypedDict(
    "DescribeProvisioningParametersOutputResponseTypeDef",
    {
        "ProvisioningArtifactParameters": List["ProvisioningArtifactParameterTypeDef"],
        "ConstraintSummaries": List["ConstraintSummaryTypeDef"],
        "UsageInstructions": List["UsageInstructionTypeDef"],
        "TagOptions": List["TagOptionSummaryTypeDef"],
        "ProvisioningArtifactPreferences": "ProvisioningArtifactPreferencesTypeDef",
        "ProvisioningArtifactOutputs": List["ProvisioningArtifactOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRecordInputTypeDef = TypedDict(
    "_RequiredDescribeRecordInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeRecordInputTypeDef = TypedDict(
    "_OptionalDescribeRecordInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)


class DescribeRecordInputTypeDef(
    _RequiredDescribeRecordInputTypeDef, _OptionalDescribeRecordInputTypeDef
):
    pass


DescribeRecordOutputResponseTypeDef = TypedDict(
    "DescribeRecordOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "RecordOutputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServiceActionExecutionParametersInputTypeDef = TypedDict(
    "_RequiredDescribeServiceActionExecutionParametersInputTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
    },
)
_OptionalDescribeServiceActionExecutionParametersInputTypeDef = TypedDict(
    "_OptionalDescribeServiceActionExecutionParametersInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DescribeServiceActionExecutionParametersInputTypeDef(
    _RequiredDescribeServiceActionExecutionParametersInputTypeDef,
    _OptionalDescribeServiceActionExecutionParametersInputTypeDef,
):
    pass


DescribeServiceActionExecutionParametersOutputResponseTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersOutputResponseTypeDef",
    {
        "ServiceActionParameters": List["ExecutionParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServiceActionInputTypeDef = TypedDict(
    "_RequiredDescribeServiceActionInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeServiceActionInputTypeDef = TypedDict(
    "_OptionalDescribeServiceActionInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DescribeServiceActionInputTypeDef(
    _RequiredDescribeServiceActionInputTypeDef, _OptionalDescribeServiceActionInputTypeDef
):
    pass


DescribeServiceActionOutputResponseTypeDef = TypedDict(
    "DescribeServiceActionOutputResponseTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagOptionInputTypeDef = TypedDict(
    "DescribeTagOptionInputTypeDef",
    {
        "Id": str,
    },
)

DescribeTagOptionOutputResponseTypeDef = TypedDict(
    "DescribeTagOptionOutputResponseTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateBudgetFromResourceInputTypeDef = TypedDict(
    "DisassociateBudgetFromResourceInputTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)

_RequiredDisassociatePrincipalFromPortfolioInputTypeDef = TypedDict(
    "_RequiredDisassociatePrincipalFromPortfolioInputTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
    },
)
_OptionalDisassociatePrincipalFromPortfolioInputTypeDef = TypedDict(
    "_OptionalDisassociatePrincipalFromPortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DisassociatePrincipalFromPortfolioInputTypeDef(
    _RequiredDisassociatePrincipalFromPortfolioInputTypeDef,
    _OptionalDisassociatePrincipalFromPortfolioInputTypeDef,
):
    pass


_RequiredDisassociateProductFromPortfolioInputTypeDef = TypedDict(
    "_RequiredDisassociateProductFromPortfolioInputTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
    },
)
_OptionalDisassociateProductFromPortfolioInputTypeDef = TypedDict(
    "_OptionalDisassociateProductFromPortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DisassociateProductFromPortfolioInputTypeDef(
    _RequiredDisassociateProductFromPortfolioInputTypeDef,
    _OptionalDisassociateProductFromPortfolioInputTypeDef,
):
    pass


_RequiredDisassociateServiceActionFromProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredDisassociateServiceActionFromProvisioningArtifactInputTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
    },
)
_OptionalDisassociateServiceActionFromProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalDisassociateServiceActionFromProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class DisassociateServiceActionFromProvisioningArtifactInputTypeDef(
    _RequiredDisassociateServiceActionFromProvisioningArtifactInputTypeDef,
    _OptionalDisassociateServiceActionFromProvisioningArtifactInputTypeDef,
):
    pass


DisassociateTagOptionFromResourceInputTypeDef = TypedDict(
    "DisassociateTagOptionFromResourceInputTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)

_RequiredExecuteProvisionedProductPlanInputTypeDef = TypedDict(
    "_RequiredExecuteProvisionedProductPlanInputTypeDef",
    {
        "PlanId": str,
        "IdempotencyToken": str,
    },
)
_OptionalExecuteProvisionedProductPlanInputTypeDef = TypedDict(
    "_OptionalExecuteProvisionedProductPlanInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class ExecuteProvisionedProductPlanInputTypeDef(
    _RequiredExecuteProvisionedProductPlanInputTypeDef,
    _OptionalExecuteProvisionedProductPlanInputTypeDef,
):
    pass


ExecuteProvisionedProductPlanOutputResponseTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteProvisionedProductServiceActionInputTypeDef = TypedDict(
    "_RequiredExecuteProvisionedProductServiceActionInputTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
        "ExecuteToken": str,
    },
)
_OptionalExecuteProvisionedProductServiceActionInputTypeDef = TypedDict(
    "_OptionalExecuteProvisionedProductServiceActionInputTypeDef",
    {
        "AcceptLanguage": str,
        "Parameters": Dict[str, List[str]],
    },
    total=False,
)


class ExecuteProvisionedProductServiceActionInputTypeDef(
    _RequiredExecuteProvisionedProductServiceActionInputTypeDef,
    _OptionalExecuteProvisionedProductServiceActionInputTypeDef,
):
    pass


ExecuteProvisionedProductServiceActionOutputResponseTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecutionParameterTypeDef = TypedDict(
    "ExecutionParameterTypeDef",
    {
        "Name": str,
        "Type": str,
        "DefaultValues": List[str],
    },
    total=False,
)

FailedServiceActionAssociationTypeDef = TypedDict(
    "FailedServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": ServiceActionAssociationErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

GetAWSOrganizationsAccessStatusOutputResponseTypeDef = TypedDict(
    "GetAWSOrganizationsAccessStatusOutputResponseTypeDef",
    {
        "AccessStatus": AccessStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedProductOutputsInputTypeDef = TypedDict(
    "GetProvisionedProductOutputsInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisionedProductId": str,
        "ProvisionedProductName": str,
        "OutputKeys": List[str],
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

GetProvisionedProductOutputsOutputResponseTypeDef = TypedDict(
    "GetProvisionedProductOutputsOutputResponseTypeDef",
    {
        "Outputs": List["RecordOutputTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportAsProvisionedProductInputTypeDef = TypedDict(
    "_RequiredImportAsProvisionedProductInputTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ProvisionedProductName": str,
        "PhysicalId": str,
        "IdempotencyToken": str,
    },
)
_OptionalImportAsProvisionedProductInputTypeDef = TypedDict(
    "_OptionalImportAsProvisionedProductInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class ImportAsProvisionedProductInputTypeDef(
    _RequiredImportAsProvisionedProductInputTypeDef, _OptionalImportAsProvisionedProductInputTypeDef
):
    pass


ImportAsProvisionedProductOutputResponseTypeDef = TypedDict(
    "ImportAsProvisionedProductOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchPathSummaryTypeDef = TypedDict(
    "LaunchPathSummaryTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List["ConstraintSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "Name": str,
    },
    total=False,
)

LaunchPathTypeDef = TypedDict(
    "LaunchPathTypeDef",
    {
        "Id": str,
        "Name": str,
    },
    total=False,
)

ListAcceptedPortfolioSharesInputTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
        "PortfolioShareType": PortfolioShareTypeType,
    },
    total=False,
)

ListAcceptedPortfolioSharesOutputResponseTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesOutputResponseTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBudgetsForResourceInputTypeDef = TypedDict(
    "_RequiredListBudgetsForResourceInputTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListBudgetsForResourceInputTypeDef = TypedDict(
    "_OptionalListBudgetsForResourceInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)


class ListBudgetsForResourceInputTypeDef(
    _RequiredListBudgetsForResourceInputTypeDef, _OptionalListBudgetsForResourceInputTypeDef
):
    pass


ListBudgetsForResourceOutputResponseTypeDef = TypedDict(
    "ListBudgetsForResourceOutputResponseTypeDef",
    {
        "Budgets": List["BudgetDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConstraintsForPortfolioInputTypeDef = TypedDict(
    "_RequiredListConstraintsForPortfolioInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalListConstraintsForPortfolioInputTypeDef = TypedDict(
    "_OptionalListConstraintsForPortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProductId": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)


class ListConstraintsForPortfolioInputTypeDef(
    _RequiredListConstraintsForPortfolioInputTypeDef,
    _OptionalListConstraintsForPortfolioInputTypeDef,
):
    pass


ListConstraintsForPortfolioOutputResponseTypeDef = TypedDict(
    "ListConstraintsForPortfolioOutputResponseTypeDef",
    {
        "ConstraintDetails": List["ConstraintDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchPathsInputTypeDef = TypedDict(
    "_RequiredListLaunchPathsInputTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalListLaunchPathsInputTypeDef = TypedDict(
    "_OptionalListLaunchPathsInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)


class ListLaunchPathsInputTypeDef(
    _RequiredListLaunchPathsInputTypeDef, _OptionalListLaunchPathsInputTypeDef
):
    pass


ListLaunchPathsOutputResponseTypeDef = TypedDict(
    "ListLaunchPathsOutputResponseTypeDef",
    {
        "LaunchPathSummaries": List["LaunchPathSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOrganizationPortfolioAccessInputTypeDef = TypedDict(
    "_RequiredListOrganizationPortfolioAccessInputTypeDef",
    {
        "PortfolioId": str,
        "OrganizationNodeType": OrganizationNodeTypeType,
    },
)
_OptionalListOrganizationPortfolioAccessInputTypeDef = TypedDict(
    "_OptionalListOrganizationPortfolioAccessInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)


class ListOrganizationPortfolioAccessInputTypeDef(
    _RequiredListOrganizationPortfolioAccessInputTypeDef,
    _OptionalListOrganizationPortfolioAccessInputTypeDef,
):
    pass


ListOrganizationPortfolioAccessOutputResponseTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessOutputResponseTypeDef",
    {
        "OrganizationNodes": List["OrganizationNodeTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPortfolioAccessInputTypeDef = TypedDict(
    "_RequiredListPortfolioAccessInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalListPortfolioAccessInputTypeDef = TypedDict(
    "_OptionalListPortfolioAccessInputTypeDef",
    {
        "AcceptLanguage": str,
        "OrganizationParentId": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)


class ListPortfolioAccessInputTypeDef(
    _RequiredListPortfolioAccessInputTypeDef, _OptionalListPortfolioAccessInputTypeDef
):
    pass


ListPortfolioAccessOutputResponseTypeDef = TypedDict(
    "ListPortfolioAccessOutputResponseTypeDef",
    {
        "AccountIds": List[str],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPortfoliosForProductInputTypeDef = TypedDict(
    "_RequiredListPortfoliosForProductInputTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalListPortfoliosForProductInputTypeDef = TypedDict(
    "_OptionalListPortfoliosForProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)


class ListPortfoliosForProductInputTypeDef(
    _RequiredListPortfoliosForProductInputTypeDef, _OptionalListPortfoliosForProductInputTypeDef
):
    pass


ListPortfoliosForProductOutputResponseTypeDef = TypedDict(
    "ListPortfoliosForProductOutputResponseTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortfoliosInputTypeDef = TypedDict(
    "ListPortfoliosInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)

ListPortfoliosOutputResponseTypeDef = TypedDict(
    "ListPortfoliosOutputResponseTypeDef",
    {
        "PortfolioDetails": List["PortfolioDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrincipalsForPortfolioInputTypeDef = TypedDict(
    "_RequiredListPrincipalsForPortfolioInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalListPrincipalsForPortfolioInputTypeDef = TypedDict(
    "_OptionalListPrincipalsForPortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)


class ListPrincipalsForPortfolioInputTypeDef(
    _RequiredListPrincipalsForPortfolioInputTypeDef, _OptionalListPrincipalsForPortfolioInputTypeDef
):
    pass


ListPrincipalsForPortfolioOutputResponseTypeDef = TypedDict(
    "ListPrincipalsForPortfolioOutputResponseTypeDef",
    {
        "Principals": List["PrincipalTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedProductPlansInputTypeDef = TypedDict(
    "ListProvisionedProductPlansInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisionProductId": str,
        "PageSize": int,
        "PageToken": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
    },
    total=False,
)

ListProvisionedProductPlansOutputResponseTypeDef = TypedDict(
    "ListProvisionedProductPlansOutputResponseTypeDef",
    {
        "ProvisionedProductPlans": List["ProvisionedProductPlanSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningArtifactsForServiceActionInputTypeDef = TypedDict(
    "_RequiredListProvisioningArtifactsForServiceActionInputTypeDef",
    {
        "ServiceActionId": str,
    },
)
_OptionalListProvisioningArtifactsForServiceActionInputTypeDef = TypedDict(
    "_OptionalListProvisioningArtifactsForServiceActionInputTypeDef",
    {
        "PageSize": int,
        "PageToken": str,
        "AcceptLanguage": str,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionInputTypeDef(
    _RequiredListProvisioningArtifactsForServiceActionInputTypeDef,
    _OptionalListProvisioningArtifactsForServiceActionInputTypeDef,
):
    pass


ListProvisioningArtifactsForServiceActionOutputResponseTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionOutputResponseTypeDef",
    {
        "ProvisioningArtifactViews": List["ProvisioningArtifactViewTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisioningArtifactsInputTypeDef = TypedDict(
    "_RequiredListProvisioningArtifactsInputTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalListProvisioningArtifactsInputTypeDef = TypedDict(
    "_OptionalListProvisioningArtifactsInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class ListProvisioningArtifactsInputTypeDef(
    _RequiredListProvisioningArtifactsInputTypeDef, _OptionalListProvisioningArtifactsInputTypeDef
):
    pass


ListProvisioningArtifactsOutputResponseTypeDef = TypedDict(
    "ListProvisioningArtifactsOutputResponseTypeDef",
    {
        "ProvisioningArtifactDetails": List["ProvisioningArtifactDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordHistoryInputTypeDef = TypedDict(
    "ListRecordHistoryInputTypeDef",
    {
        "AcceptLanguage": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
        "SearchFilter": "ListRecordHistorySearchFilterTypeDef",
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ListRecordHistoryOutputResponseTypeDef = TypedDict(
    "ListRecordHistoryOutputResponseTypeDef",
    {
        "RecordDetails": List["RecordDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordHistorySearchFilterTypeDef = TypedDict(
    "ListRecordHistorySearchFilterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredListResourcesForTagOptionInputTypeDef = TypedDict(
    "_RequiredListResourcesForTagOptionInputTypeDef",
    {
        "TagOptionId": str,
    },
)
_OptionalListResourcesForTagOptionInputTypeDef = TypedDict(
    "_OptionalListResourcesForTagOptionInputTypeDef",
    {
        "ResourceType": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)


class ListResourcesForTagOptionInputTypeDef(
    _RequiredListResourcesForTagOptionInputTypeDef, _OptionalListResourcesForTagOptionInputTypeDef
):
    pass


ListResourcesForTagOptionOutputResponseTypeDef = TypedDict(
    "ListResourcesForTagOptionOutputResponseTypeDef",
    {
        "ResourceDetails": List["ResourceDetailTypeDef"],
        "PageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceActionsForProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredListServiceActionsForProvisioningArtifactInputTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalListServiceActionsForProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalListServiceActionsForProvisioningArtifactInputTypeDef",
    {
        "PageSize": int,
        "PageToken": str,
        "AcceptLanguage": str,
    },
    total=False,
)


class ListServiceActionsForProvisioningArtifactInputTypeDef(
    _RequiredListServiceActionsForProvisioningArtifactInputTypeDef,
    _OptionalListServiceActionsForProvisioningArtifactInputTypeDef,
):
    pass


ListServiceActionsForProvisioningArtifactOutputResponseTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactOutputResponseTypeDef",
    {
        "ServiceActionSummaries": List["ServiceActionSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceActionsInputTypeDef = TypedDict(
    "ListServiceActionsInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ListServiceActionsOutputResponseTypeDef = TypedDict(
    "ListServiceActionsOutputResponseTypeDef",
    {
        "ServiceActionSummaries": List["ServiceActionSummaryTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackInstancesForProvisionedProductInputTypeDef = TypedDict(
    "_RequiredListStackInstancesForProvisionedProductInputTypeDef",
    {
        "ProvisionedProductId": str,
    },
)
_OptionalListStackInstancesForProvisionedProductInputTypeDef = TypedDict(
    "_OptionalListStackInstancesForProvisionedProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "PageToken": str,
        "PageSize": int,
    },
    total=False,
)


class ListStackInstancesForProvisionedProductInputTypeDef(
    _RequiredListStackInstancesForProvisionedProductInputTypeDef,
    _OptionalListStackInstancesForProvisionedProductInputTypeDef,
):
    pass


ListStackInstancesForProvisionedProductOutputResponseTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductOutputResponseTypeDef",
    {
        "StackInstances": List["StackInstanceTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagOptionsFiltersTypeDef = TypedDict(
    "ListTagOptionsFiltersTypeDef",
    {
        "Key": str,
        "Value": str,
        "Active": bool,
    },
    total=False,
)

ListTagOptionsInputTypeDef = TypedDict(
    "ListTagOptionsInputTypeDef",
    {
        "Filters": "ListTagOptionsFiltersTypeDef",
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ListTagOptionsOutputResponseTypeDef = TypedDict(
    "ListTagOptionsOutputResponseTypeDef",
    {
        "TagOptionDetails": List["TagOptionDetailTypeDef"],
        "PageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef",
    {
        "Type": OrganizationNodeTypeType,
        "Value": str,
    },
    total=False,
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

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": List[str],
        "AllowedPattern": str,
        "ConstraintDescription": str,
        "MaxLength": str,
        "MinLength": str,
        "MaxValue": str,
        "MinValue": str,
    },
    total=False,
)

PortfolioDetailTypeDef = TypedDict(
    "PortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)

PortfolioShareDetailTypeDef = TypedDict(
    "PortfolioShareDetailTypeDef",
    {
        "PrincipalId": str,
        "Type": DescribePortfolioShareTypeType,
        "Accepted": bool,
        "ShareTagOptions": bool,
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "PrincipalARN": str,
        "PrincipalType": Literal["IAM"],
    },
    total=False,
)

ProductViewAggregationValueTypeDef = TypedDict(
    "ProductViewAggregationValueTypeDef",
    {
        "Value": str,
        "ApproximateCount": int,
    },
    total=False,
)

ProductViewDetailTypeDef = TypedDict(
    "ProductViewDetailTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "Status": StatusType,
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ProductViewSummaryTypeDef = TypedDict(
    "ProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": ProductTypeType,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)

_RequiredProvisionProductInputTypeDef = TypedDict(
    "_RequiredProvisionProductInputTypeDef",
    {
        "ProvisionedProductName": str,
        "ProvisionToken": str,
    },
)
_OptionalProvisionProductInputTypeDef = TypedDict(
    "_OptionalProvisionProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "PathId": str,
        "PathName": str,
        "ProvisioningParameters": List["ProvisioningParameterTypeDef"],
        "ProvisioningPreferences": "ProvisioningPreferencesTypeDef",
        "Tags": List["TagTypeDef"],
        "NotificationArns": List[str],
    },
    total=False,
)


class ProvisionProductInputTypeDef(
    _RequiredProvisionProductInputTypeDef, _OptionalProvisionProductInputTypeDef
):
    pass


ProvisionProductOutputResponseTypeDef = TypedDict(
    "ProvisionProductOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedProductAttributeTypeDef = TypedDict(
    "ProvisionedProductAttributeTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": ProvisionedProductStatusType,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "Tags": List["TagTypeDef"],
        "PhysicalId": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "UserArn": str,
        "UserArnSession": str,
    },
    total=False,
)

ProvisionedProductDetailTypeDef = TypedDict(
    "ProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": ProvisionedProductStatusType,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "LaunchRoleArn": str,
    },
    total=False,
)

ProvisionedProductPlanDetailsTypeDef = TypedDict(
    "ProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": datetime,
        "PathId": str,
        "ProductId": str,
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProvisioningArtifactId": str,
        "Status": ProvisionedProductPlanStatusType,
        "UpdatedTime": datetime,
        "NotificationArns": List[str],
        "ProvisioningParameters": List["UpdateProvisioningParameterTypeDef"],
        "Tags": List["TagTypeDef"],
        "StatusMessage": str,
    },
    total=False,
)

ProvisionedProductPlanSummaryTypeDef = TypedDict(
    "ProvisionedProductPlanSummaryTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProvisioningArtifactId": str,
    },
    total=False,
)

ProvisioningArtifactDetailTypeDef = TypedDict(
    "ProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": ProvisioningArtifactTypeType,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": ProvisioningArtifactGuidanceType,
    },
    total=False,
)

ProvisioningArtifactOutputTypeDef = TypedDict(
    "ProvisioningArtifactOutputTypeDef",
    {
        "Key": str,
        "Description": str,
    },
    total=False,
)

ProvisioningArtifactParameterTypeDef = TypedDict(
    "ProvisioningArtifactParameterTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "IsNoEcho": bool,
        "Description": str,
        "ParameterConstraints": "ParameterConstraintsTypeDef",
    },
    total=False,
)

ProvisioningArtifactPreferencesTypeDef = TypedDict(
    "ProvisioningArtifactPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
    },
    total=False,
)

_RequiredProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_RequiredProvisioningArtifactPropertiesTypeDef",
    {
        "Info": Dict[str, str],
    },
)
_OptionalProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_OptionalProvisioningArtifactPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": ProvisioningArtifactTypeType,
        "DisableTemplateValidation": bool,
    },
    total=False,
)


class ProvisioningArtifactPropertiesTypeDef(
    _RequiredProvisioningArtifactPropertiesTypeDef, _OptionalProvisioningArtifactPropertiesTypeDef
):
    pass


ProvisioningArtifactSummaryTypeDef = TypedDict(
    "ProvisioningArtifactSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProvisioningArtifactMetadata": Dict[str, str],
    },
    total=False,
)

ProvisioningArtifactTypeDef = TypedDict(
    "ProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": ProvisioningArtifactGuidanceType,
    },
    total=False,
)

ProvisioningArtifactViewTypeDef = TypedDict(
    "ProvisioningArtifactViewTypeDef",
    {
        "ProductViewSummary": "ProductViewSummaryTypeDef",
        "ProvisioningArtifact": "ProvisioningArtifactTypeDef",
    },
    total=False,
)

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

ProvisioningPreferencesTypeDef = TypedDict(
    "ProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
    },
    total=False,
)

RecordDetailTypeDef = TypedDict(
    "RecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": RecordStatusType,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List["RecordErrorTypeDef"],
        "RecordTags": List["RecordTagTypeDef"],
        "LaunchRoleArn": str,
    },
    total=False,
)

RecordErrorTypeDef = TypedDict(
    "RecordErrorTypeDef",
    {
        "Code": str,
        "Description": str,
    },
    total=False,
)

RecordOutputTypeDef = TypedDict(
    "RecordOutputTypeDef",
    {
        "OutputKey": str,
        "OutputValue": str,
        "Description": str,
    },
    total=False,
)

RecordTagTypeDef = TypedDict(
    "RecordTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredRejectPortfolioShareInputTypeDef = TypedDict(
    "_RequiredRejectPortfolioShareInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalRejectPortfolioShareInputTypeDef = TypedDict(
    "_OptionalRejectPortfolioShareInputTypeDef",
    {
        "AcceptLanguage": str,
        "PortfolioShareType": PortfolioShareTypeType,
    },
    total=False,
)


class RejectPortfolioShareInputTypeDef(
    _RequiredRejectPortfolioShareInputTypeDef, _OptionalRejectPortfolioShareInputTypeDef
):
    pass


ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": EvaluationTypeType,
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": ChangeActionType,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": ReplacementType,
        "Scope": List[ResourceAttributeType],
        "Details": List["ResourceChangeDetailTypeDef"],
    },
    total=False,
)

ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": ResourceAttributeType,
        "Name": str,
        "RequiresRecreation": RequiresRecreationType,
    },
    total=False,
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

ScanProvisionedProductsInputTypeDef = TypedDict(
    "ScanProvisionedProductsInputTypeDef",
    {
        "AcceptLanguage": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

ScanProvisionedProductsOutputResponseTypeDef = TypedDict(
    "ScanProvisionedProductsOutputResponseTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProductsAsAdminInputTypeDef = TypedDict(
    "SearchProductsAsAdminInputTypeDef",
    {
        "AcceptLanguage": str,
        "PortfolioId": str,
        "Filters": Dict[ProductViewFilterByType, List[str]],
        "SortBy": ProductViewSortByType,
        "SortOrder": SortOrderType,
        "PageToken": str,
        "PageSize": int,
        "ProductSource": Literal["ACCOUNT"],
    },
    total=False,
)

SearchProductsAsAdminOutputResponseTypeDef = TypedDict(
    "SearchProductsAsAdminOutputResponseTypeDef",
    {
        "ProductViewDetails": List["ProductViewDetailTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProductsInputTypeDef = TypedDict(
    "SearchProductsInputTypeDef",
    {
        "AcceptLanguage": str,
        "Filters": Dict[ProductViewFilterByType, List[str]],
        "PageSize": int,
        "SortBy": ProductViewSortByType,
        "SortOrder": SortOrderType,
        "PageToken": str,
    },
    total=False,
)

SearchProductsOutputResponseTypeDef = TypedDict(
    "SearchProductsOutputResponseTypeDef",
    {
        "ProductViewSummaries": List["ProductViewSummaryTypeDef"],
        "ProductViewAggregations": Dict[str, List["ProductViewAggregationValueTypeDef"]],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProvisionedProductsInputTypeDef = TypedDict(
    "SearchProvisionedProductsInputTypeDef",
    {
        "AcceptLanguage": str,
        "AccessLevelFilter": "AccessLevelFilterTypeDef",
        "Filters": Dict[Literal["SearchQuery"], List[str]],
        "SortBy": str,
        "SortOrder": SortOrderType,
        "PageSize": int,
        "PageToken": str,
    },
    total=False,
)

SearchProvisionedProductsOutputResponseTypeDef = TypedDict(
    "SearchProvisionedProductsOutputResponseTypeDef",
    {
        "ProvisionedProducts": List["ProvisionedProductAttributeTypeDef"],
        "TotalResultsCount": int,
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceActionAssociationTypeDef = TypedDict(
    "ServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)

ServiceActionDetailTypeDef = TypedDict(
    "ServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": "ServiceActionSummaryTypeDef",
        "Definition": Dict[ServiceActionDefinitionKeyType, str],
    },
    total=False,
)

ServiceActionSummaryTypeDef = TypedDict(
    "ServiceActionSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DefinitionType": Literal["SSM_AUTOMATION"],
    },
    total=False,
)

ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {
        "SuccessfulShares": List[str],
        "ShareErrors": List["ShareErrorTypeDef"],
    },
    total=False,
)

ShareErrorTypeDef = TypedDict(
    "ShareErrorTypeDef",
    {
        "Accounts": List[str],
        "Message": str,
        "Error": str,
    },
    total=False,
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "Account": str,
        "Region": str,
        "StackInstanceStatus": StackInstanceStatusType,
    },
    total=False,
)

TagOptionDetailTypeDef = TypedDict(
    "TagOptionDetailTypeDef",
    {
        "Key": str,
        "Value": str,
        "Active": bool,
        "Id": str,
        "Owner": str,
    },
    total=False,
)

TagOptionSummaryTypeDef = TypedDict(
    "TagOptionSummaryTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTerminateProvisionedProductInputTypeDef = TypedDict(
    "_RequiredTerminateProvisionedProductInputTypeDef",
    {
        "TerminateToken": str,
    },
)
_OptionalTerminateProvisionedProductInputTypeDef = TypedDict(
    "_OptionalTerminateProvisionedProductInputTypeDef",
    {
        "ProvisionedProductName": str,
        "ProvisionedProductId": str,
        "IgnoreErrors": bool,
        "AcceptLanguage": str,
        "RetainPhysicalResources": bool,
    },
    total=False,
)


class TerminateProvisionedProductInputTypeDef(
    _RequiredTerminateProvisionedProductInputTypeDef,
    _OptionalTerminateProvisionedProductInputTypeDef,
):
    pass


TerminateProvisionedProductOutputResponseTypeDef = TypedDict(
    "TerminateProvisionedProductOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConstraintInputTypeDef = TypedDict(
    "_RequiredUpdateConstraintInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateConstraintInputTypeDef = TypedDict(
    "_OptionalUpdateConstraintInputTypeDef",
    {
        "AcceptLanguage": str,
        "Description": str,
        "Parameters": str,
    },
    total=False,
)


class UpdateConstraintInputTypeDef(
    _RequiredUpdateConstraintInputTypeDef, _OptionalUpdateConstraintInputTypeDef
):
    pass


UpdateConstraintOutputResponseTypeDef = TypedDict(
    "UpdateConstraintOutputResponseTypeDef",
    {
        "ConstraintDetail": "ConstraintDetailTypeDef",
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePortfolioInputTypeDef = TypedDict(
    "_RequiredUpdatePortfolioInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdatePortfolioInputTypeDef = TypedDict(
    "_OptionalUpdatePortfolioInputTypeDef",
    {
        "AcceptLanguage": str,
        "DisplayName": str,
        "Description": str,
        "ProviderName": str,
        "AddTags": List["TagTypeDef"],
        "RemoveTags": List[str],
    },
    total=False,
)


class UpdatePortfolioInputTypeDef(
    _RequiredUpdatePortfolioInputTypeDef, _OptionalUpdatePortfolioInputTypeDef
):
    pass


UpdatePortfolioOutputResponseTypeDef = TypedDict(
    "UpdatePortfolioOutputResponseTypeDef",
    {
        "PortfolioDetail": "PortfolioDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePortfolioShareInputTypeDef = TypedDict(
    "_RequiredUpdatePortfolioShareInputTypeDef",
    {
        "PortfolioId": str,
    },
)
_OptionalUpdatePortfolioShareInputTypeDef = TypedDict(
    "_OptionalUpdatePortfolioShareInputTypeDef",
    {
        "AcceptLanguage": str,
        "AccountId": str,
        "OrganizationNode": "OrganizationNodeTypeDef",
        "ShareTagOptions": bool,
    },
    total=False,
)


class UpdatePortfolioShareInputTypeDef(
    _RequiredUpdatePortfolioShareInputTypeDef, _OptionalUpdatePortfolioShareInputTypeDef
):
    pass


UpdatePortfolioShareOutputResponseTypeDef = TypedDict(
    "UpdatePortfolioShareOutputResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "Status": ShareStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProductInputTypeDef = TypedDict(
    "_RequiredUpdateProductInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateProductInputTypeDef = TypedDict(
    "_OptionalUpdateProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "Name": str,
        "Owner": str,
        "Description": str,
        "Distributor": str,
        "SupportDescription": str,
        "SupportEmail": str,
        "SupportUrl": str,
        "AddTags": List["TagTypeDef"],
        "RemoveTags": List[str],
    },
    total=False,
)


class UpdateProductInputTypeDef(
    _RequiredUpdateProductInputTypeDef, _OptionalUpdateProductInputTypeDef
):
    pass


UpdateProductOutputResponseTypeDef = TypedDict(
    "UpdateProductOutputResponseTypeDef",
    {
        "ProductViewDetail": "ProductViewDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisionedProductInputTypeDef = TypedDict(
    "_RequiredUpdateProvisionedProductInputTypeDef",
    {
        "UpdateToken": str,
    },
)
_OptionalUpdateProvisionedProductInputTypeDef = TypedDict(
    "_OptionalUpdateProvisionedProductInputTypeDef",
    {
        "AcceptLanguage": str,
        "ProvisionedProductName": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "PathId": str,
        "PathName": str,
        "ProvisioningParameters": List["UpdateProvisioningParameterTypeDef"],
        "ProvisioningPreferences": "UpdateProvisioningPreferencesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class UpdateProvisionedProductInputTypeDef(
    _RequiredUpdateProvisionedProductInputTypeDef, _OptionalUpdateProvisionedProductInputTypeDef
):
    pass


UpdateProvisionedProductOutputResponseTypeDef = TypedDict(
    "UpdateProvisionedProductOutputResponseTypeDef",
    {
        "RecordDetail": "RecordDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisionedProductPropertiesInputTypeDef = TypedDict(
    "_RequiredUpdateProvisionedProductPropertiesInputTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[PropertyKeyType, str],
        "IdempotencyToken": str,
    },
)
_OptionalUpdateProvisionedProductPropertiesInputTypeDef = TypedDict(
    "_OptionalUpdateProvisionedProductPropertiesInputTypeDef",
    {
        "AcceptLanguage": str,
    },
    total=False,
)


class UpdateProvisionedProductPropertiesInputTypeDef(
    _RequiredUpdateProvisionedProductPropertiesInputTypeDef,
    _OptionalUpdateProvisionedProductPropertiesInputTypeDef,
):
    pass


UpdateProvisionedProductPropertiesOutputResponseTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesOutputResponseTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[PropertyKeyType, str],
        "RecordId": str,
        "Status": RecordStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProvisioningArtifactInputTypeDef = TypedDict(
    "_RequiredUpdateProvisioningArtifactInputTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
_OptionalUpdateProvisioningArtifactInputTypeDef = TypedDict(
    "_OptionalUpdateProvisioningArtifactInputTypeDef",
    {
        "AcceptLanguage": str,
        "Name": str,
        "Description": str,
        "Active": bool,
        "Guidance": ProvisioningArtifactGuidanceType,
    },
    total=False,
)


class UpdateProvisioningArtifactInputTypeDef(
    _RequiredUpdateProvisioningArtifactInputTypeDef, _OptionalUpdateProvisioningArtifactInputTypeDef
):
    pass


UpdateProvisioningArtifactOutputResponseTypeDef = TypedDict(
    "UpdateProvisioningArtifactOutputResponseTypeDef",
    {
        "ProvisioningArtifactDetail": "ProvisioningArtifactDetailTypeDef",
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProvisioningParameterTypeDef = TypedDict(
    "UpdateProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "UsePreviousValue": bool,
    },
    total=False,
)

UpdateProvisioningPreferencesTypeDef = TypedDict(
    "UpdateProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
        "StackSetOperationType": StackSetOperationTypeType,
    },
    total=False,
)

_RequiredUpdateServiceActionInputTypeDef = TypedDict(
    "_RequiredUpdateServiceActionInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateServiceActionInputTypeDef = TypedDict(
    "_OptionalUpdateServiceActionInputTypeDef",
    {
        "Name": str,
        "Definition": Dict[ServiceActionDefinitionKeyType, str],
        "Description": str,
        "AcceptLanguage": str,
    },
    total=False,
)


class UpdateServiceActionInputTypeDef(
    _RequiredUpdateServiceActionInputTypeDef, _OptionalUpdateServiceActionInputTypeDef
):
    pass


UpdateServiceActionOutputResponseTypeDef = TypedDict(
    "UpdateServiceActionOutputResponseTypeDef",
    {
        "ServiceActionDetail": "ServiceActionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTagOptionInputTypeDef = TypedDict(
    "_RequiredUpdateTagOptionInputTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateTagOptionInputTypeDef = TypedDict(
    "_OptionalUpdateTagOptionInputTypeDef",
    {
        "Value": str,
        "Active": bool,
    },
    total=False,
)


class UpdateTagOptionInputTypeDef(
    _RequiredUpdateTagOptionInputTypeDef, _OptionalUpdateTagOptionInputTypeDef
):
    pass


UpdateTagOptionOutputResponseTypeDef = TypedDict(
    "UpdateTagOptionOutputResponseTypeDef",
    {
        "TagOptionDetail": "TagOptionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageInstructionTypeDef = TypedDict(
    "UsageInstructionTypeDef",
    {
        "Type": str,
        "Value": str,
    },
    total=False,
)
