"""
Type annotations for iotsitewise service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsitewise.type_defs import AccessPolicySummaryTypeDef

    data: AccessPolicySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AggregateTypeType,
    AssetModelStateType,
    AssetStateType,
    AuthModeType,
    BatchPutAssetPropertyValueErrorCodeType,
    CapabilitySyncStatusType,
    ConfigurationStateType,
    EncryptionTypeType,
    ErrorCodeType,
    IdentityTypeType,
    ListAssetsFilterType,
    LoggingLevelType,
    MonitorErrorCodeType,
    PermissionType,
    PortalStateType,
    PropertyDataTypeType,
    PropertyNotificationStateType,
    QualityType,
    ResourceTypeType,
    TimeOrderingType,
    TraversalDirectionType,
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
    "AccessPolicySummaryTypeDef",
    "AggregatedValueTypeDef",
    "AggregatesTypeDef",
    "AlarmsTypeDef",
    "AssetCompositeModelTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyInfoTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelCompositeModelDefinitionTypeDef",
    "AssetModelCompositeModelTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelStatusTypeDef",
    "AssetModelSummaryTypeDef",
    "AssetPropertyTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetRelationshipSummaryTypeDef",
    "AssetStatusTypeDef",
    "AssetSummaryTypeDef",
    "AssociateAssetsRequestTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "AttributeTypeDef",
    "BatchAssociateProjectAssetsRequestTypeDef",
    "BatchAssociateProjectAssetsResponseResponseTypeDef",
    "BatchDisassociateProjectAssetsRequestTypeDef",
    "BatchDisassociateProjectAssetsResponseResponseTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "BatchPutAssetPropertyValueRequestTypeDef",
    "BatchPutAssetPropertyValueResponseResponseTypeDef",
    "CompositeModelPropertyTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "ConfigurationStatusTypeDef",
    "CreateAccessPolicyRequestTypeDef",
    "CreateAccessPolicyResponseResponseTypeDef",
    "CreateAssetModelRequestTypeDef",
    "CreateAssetModelResponseResponseTypeDef",
    "CreateAssetRequestTypeDef",
    "CreateAssetResponseResponseTypeDef",
    "CreateDashboardRequestTypeDef",
    "CreateDashboardResponseResponseTypeDef",
    "CreateGatewayRequestTypeDef",
    "CreateGatewayResponseResponseTypeDef",
    "CreatePortalRequestTypeDef",
    "CreatePortalResponseResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseResponseTypeDef",
    "DashboardSummaryTypeDef",
    "DeleteAccessPolicyRequestTypeDef",
    "DeleteAssetModelRequestTypeDef",
    "DeleteAssetModelResponseResponseTypeDef",
    "DeleteAssetRequestTypeDef",
    "DeleteAssetResponseResponseTypeDef",
    "DeleteDashboardRequestTypeDef",
    "DeleteGatewayRequestTypeDef",
    "DeletePortalRequestTypeDef",
    "DeletePortalResponseResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DescribeAccessPolicyRequestTypeDef",
    "DescribeAccessPolicyResponseResponseTypeDef",
    "DescribeAssetModelRequestTypeDef",
    "DescribeAssetModelResponseResponseTypeDef",
    "DescribeAssetPropertyRequestTypeDef",
    "DescribeAssetPropertyResponseResponseTypeDef",
    "DescribeAssetRequestTypeDef",
    "DescribeAssetResponseResponseTypeDef",
    "DescribeDashboardRequestTypeDef",
    "DescribeDashboardResponseResponseTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationRequestTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseResponseTypeDef",
    "DescribeGatewayRequestTypeDef",
    "DescribeGatewayResponseResponseTypeDef",
    "DescribeLoggingOptionsResponseResponseTypeDef",
    "DescribePortalRequestTypeDef",
    "DescribePortalResponseResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResponseResponseTypeDef",
    "DisassociateAssetsRequestTypeDef",
    "ErrorDetailsTypeDef",
    "ExpressionVariableTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "GatewayPlatformTypeDef",
    "GatewaySummaryTypeDef",
    "GetAssetPropertyAggregatesRequestTypeDef",
    "GetAssetPropertyAggregatesResponseResponseTypeDef",
    "GetAssetPropertyValueHistoryRequestTypeDef",
    "GetAssetPropertyValueHistoryResponseResponseTypeDef",
    "GetAssetPropertyValueRequestTypeDef",
    "GetAssetPropertyValueResponseResponseTypeDef",
    "GetInterpolatedAssetPropertyValuesRequestTypeDef",
    "GetInterpolatedAssetPropertyValuesResponseResponseTypeDef",
    "GreengrassTypeDef",
    "GroupIdentityTypeDef",
    "IAMRoleIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "IdentityTypeDef",
    "ImageFileTypeDef",
    "ImageLocationTypeDef",
    "ImageTypeDef",
    "InterpolatedAssetPropertyValueTypeDef",
    "ListAccessPoliciesRequestTypeDef",
    "ListAccessPoliciesResponseResponseTypeDef",
    "ListAssetModelsRequestTypeDef",
    "ListAssetModelsResponseResponseTypeDef",
    "ListAssetRelationshipsRequestTypeDef",
    "ListAssetRelationshipsResponseResponseTypeDef",
    "ListAssetsRequestTypeDef",
    "ListAssetsResponseResponseTypeDef",
    "ListAssociatedAssetsRequestTypeDef",
    "ListAssociatedAssetsResponseResponseTypeDef",
    "ListDashboardsRequestTypeDef",
    "ListDashboardsResponseResponseTypeDef",
    "ListGatewaysRequestTypeDef",
    "ListGatewaysResponseResponseTypeDef",
    "ListPortalsRequestTypeDef",
    "ListPortalsResponseResponseTypeDef",
    "ListProjectAssetsRequestTypeDef",
    "ListProjectAssetsResponseResponseTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MetricTypeDef",
    "MetricWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PortalResourceTypeDef",
    "PortalStatusTypeDef",
    "PortalSummaryTypeDef",
    "ProjectResourceTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNotificationTypeDef",
    "PropertyTypeDef",
    "PropertyTypeTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutDefaultEncryptionConfigurationRequestTypeDef",
    "PutDefaultEncryptionConfigurationResponseResponseTypeDef",
    "PutLoggingOptionsRequestTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TimeInNanosTypeDef",
    "TransformTypeDef",
    "TumblingWindowTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessPolicyRequestTypeDef",
    "UpdateAssetModelRequestTypeDef",
    "UpdateAssetModelResponseResponseTypeDef",
    "UpdateAssetPropertyRequestTypeDef",
    "UpdateAssetRequestTypeDef",
    "UpdateAssetResponseResponseTypeDef",
    "UpdateDashboardRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationRequestTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseResponseTypeDef",
    "UpdateGatewayRequestTypeDef",
    "UpdatePortalRequestTypeDef",
    "UpdatePortalResponseResponseTypeDef",
    "UpdateProjectRequestTypeDef",
    "UserIdentityTypeDef",
    "VariableValueTypeDef",
    "VariantTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessPolicySummaryTypeDef = TypedDict(
    "_RequiredAccessPolicySummaryTypeDef",
    {
        "id": str,
        "identity": "IdentityTypeDef",
        "resource": "ResourceTypeDef",
        "permission": PermissionType,
    },
)
_OptionalAccessPolicySummaryTypeDef = TypedDict(
    "_OptionalAccessPolicySummaryTypeDef",
    {
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
    total=False,
)


class AccessPolicySummaryTypeDef(
    _RequiredAccessPolicySummaryTypeDef, _OptionalAccessPolicySummaryTypeDef
):
    pass


_RequiredAggregatedValueTypeDef = TypedDict(
    "_RequiredAggregatedValueTypeDef",
    {
        "timestamp": datetime,
        "value": "AggregatesTypeDef",
    },
)
_OptionalAggregatedValueTypeDef = TypedDict(
    "_OptionalAggregatedValueTypeDef",
    {
        "quality": QualityType,
    },
    total=False,
)


class AggregatedValueTypeDef(_RequiredAggregatedValueTypeDef, _OptionalAggregatedValueTypeDef):
    pass


AggregatesTypeDef = TypedDict(
    "AggregatesTypeDef",
    {
        "average": float,
        "count": float,
        "maximum": float,
        "minimum": float,
        "sum": float,
        "standardDeviation": float,
    },
    total=False,
)

_RequiredAlarmsTypeDef = TypedDict(
    "_RequiredAlarmsTypeDef",
    {
        "alarmRoleArn": str,
    },
)
_OptionalAlarmsTypeDef = TypedDict(
    "_OptionalAlarmsTypeDef",
    {
        "notificationLambdaArn": str,
    },
    total=False,
)


class AlarmsTypeDef(_RequiredAlarmsTypeDef, _OptionalAlarmsTypeDef):
    pass


_RequiredAssetCompositeModelTypeDef = TypedDict(
    "_RequiredAssetCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
        "properties": List["AssetPropertyTypeDef"],
    },
)
_OptionalAssetCompositeModelTypeDef = TypedDict(
    "_OptionalAssetCompositeModelTypeDef",
    {
        "description": str,
    },
    total=False,
)


class AssetCompositeModelTypeDef(
    _RequiredAssetCompositeModelTypeDef, _OptionalAssetCompositeModelTypeDef
):
    pass


AssetErrorDetailsTypeDef = TypedDict(
    "AssetErrorDetailsTypeDef",
    {
        "assetId": str,
        "code": Literal["INTERNAL_FAILURE"],
        "message": str,
    },
)

AssetHierarchyInfoTypeDef = TypedDict(
    "AssetHierarchyInfoTypeDef",
    {
        "parentAssetId": str,
        "childAssetId": str,
    },
    total=False,
)

_RequiredAssetHierarchyTypeDef = TypedDict(
    "_RequiredAssetHierarchyTypeDef",
    {
        "name": str,
    },
)
_OptionalAssetHierarchyTypeDef = TypedDict(
    "_OptionalAssetHierarchyTypeDef",
    {
        "id": str,
    },
    total=False,
)


class AssetHierarchyTypeDef(_RequiredAssetHierarchyTypeDef, _OptionalAssetHierarchyTypeDef):
    pass


_RequiredAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelDefinitionTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelDefinitionTypeDef",
    {
        "description": str,
        "properties": List["AssetModelPropertyDefinitionTypeDef"],
    },
    total=False,
)


class AssetModelCompositeModelDefinitionTypeDef(
    _RequiredAssetModelCompositeModelDefinitionTypeDef,
    _OptionalAssetModelCompositeModelDefinitionTypeDef,
):
    pass


_RequiredAssetModelCompositeModelTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalAssetModelCompositeModelTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelTypeDef",
    {
        "description": str,
        "properties": List["AssetModelPropertyTypeDef"],
    },
    total=False,
)


class AssetModelCompositeModelTypeDef(
    _RequiredAssetModelCompositeModelTypeDef, _OptionalAssetModelCompositeModelTypeDef
):
    pass


AssetModelHierarchyDefinitionTypeDef = TypedDict(
    "AssetModelHierarchyDefinitionTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
    },
)

_RequiredAssetModelHierarchyTypeDef = TypedDict(
    "_RequiredAssetModelHierarchyTypeDef",
    {
        "name": str,
        "childAssetModelId": str,
    },
)
_OptionalAssetModelHierarchyTypeDef = TypedDict(
    "_OptionalAssetModelHierarchyTypeDef",
    {
        "id": str,
    },
    total=False,
)


class AssetModelHierarchyTypeDef(
    _RequiredAssetModelHierarchyTypeDef, _OptionalAssetModelHierarchyTypeDef
):
    pass


_RequiredAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelPropertyDefinitionTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelPropertyDefinitionTypeDef",
    {
        "dataTypeSpec": str,
        "unit": str,
    },
    total=False,
)


class AssetModelPropertyDefinitionTypeDef(
    _RequiredAssetModelPropertyDefinitionTypeDef, _OptionalAssetModelPropertyDefinitionTypeDef
):
    pass


_RequiredAssetModelPropertyTypeDef = TypedDict(
    "_RequiredAssetModelPropertyTypeDef",
    {
        "name": str,
        "dataType": PropertyDataTypeType,
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertyTypeDef = TypedDict(
    "_OptionalAssetModelPropertyTypeDef",
    {
        "id": str,
        "dataTypeSpec": str,
        "unit": str,
    },
    total=False,
)


class AssetModelPropertyTypeDef(
    _RequiredAssetModelPropertyTypeDef, _OptionalAssetModelPropertyTypeDef
):
    pass


_RequiredAssetModelStatusTypeDef = TypedDict(
    "_RequiredAssetModelStatusTypeDef",
    {
        "state": AssetModelStateType,
    },
)
_OptionalAssetModelStatusTypeDef = TypedDict(
    "_OptionalAssetModelStatusTypeDef",
    {
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)


class AssetModelStatusTypeDef(_RequiredAssetModelStatusTypeDef, _OptionalAssetModelStatusTypeDef):
    pass


AssetModelSummaryTypeDef = TypedDict(
    "AssetModelSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetModelStatusTypeDef",
    },
)

_RequiredAssetPropertyTypeDef = TypedDict(
    "_RequiredAssetPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
    },
)
_OptionalAssetPropertyTypeDef = TypedDict(
    "_OptionalAssetPropertyTypeDef",
    {
        "alias": str,
        "notification": "PropertyNotificationTypeDef",
        "dataTypeSpec": str,
        "unit": str,
    },
    total=False,
)


class AssetPropertyTypeDef(_RequiredAssetPropertyTypeDef, _OptionalAssetPropertyTypeDef):
    pass


_RequiredAssetPropertyValueTypeDef = TypedDict(
    "_RequiredAssetPropertyValueTypeDef",
    {
        "value": "VariantTypeDef",
        "timestamp": "TimeInNanosTypeDef",
    },
)
_OptionalAssetPropertyValueTypeDef = TypedDict(
    "_OptionalAssetPropertyValueTypeDef",
    {
        "quality": QualityType,
    },
    total=False,
)


class AssetPropertyValueTypeDef(
    _RequiredAssetPropertyValueTypeDef, _OptionalAssetPropertyValueTypeDef
):
    pass


_RequiredAssetRelationshipSummaryTypeDef = TypedDict(
    "_RequiredAssetRelationshipSummaryTypeDef",
    {
        "relationshipType": Literal["HIERARCHY"],
    },
)
_OptionalAssetRelationshipSummaryTypeDef = TypedDict(
    "_OptionalAssetRelationshipSummaryTypeDef",
    {
        "hierarchyInfo": "AssetHierarchyInfoTypeDef",
    },
    total=False,
)


class AssetRelationshipSummaryTypeDef(
    _RequiredAssetRelationshipSummaryTypeDef, _OptionalAssetRelationshipSummaryTypeDef
):
    pass


_RequiredAssetStatusTypeDef = TypedDict(
    "_RequiredAssetStatusTypeDef",
    {
        "state": AssetStateType,
    },
)
_OptionalAssetStatusTypeDef = TypedDict(
    "_OptionalAssetStatusTypeDef",
    {
        "error": "ErrorDetailsTypeDef",
    },
    total=False,
)


class AssetStatusTypeDef(_RequiredAssetStatusTypeDef, _OptionalAssetStatusTypeDef):
    pass


AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

_RequiredAssociateAssetsRequestTypeDef = TypedDict(
    "_RequiredAssociateAssetsRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
    },
)
_OptionalAssociateAssetsRequestTypeDef = TypedDict(
    "_OptionalAssociateAssetsRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class AssociateAssetsRequestTypeDef(
    _RequiredAssociateAssetsRequestTypeDef, _OptionalAssociateAssetsRequestTypeDef
):
    pass


AssociatedAssetsSummaryTypeDef = TypedDict(
    "AssociatedAssetsSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "defaultValue": str,
    },
    total=False,
)

_RequiredBatchAssociateProjectAssetsRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateProjectAssetsRequestTypeDef",
    {
        "projectId": str,
        "assetIds": List[str],
    },
)
_OptionalBatchAssociateProjectAssetsRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateProjectAssetsRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class BatchAssociateProjectAssetsRequestTypeDef(
    _RequiredBatchAssociateProjectAssetsRequestTypeDef,
    _OptionalBatchAssociateProjectAssetsRequestTypeDef,
):
    pass


BatchAssociateProjectAssetsResponseResponseTypeDef = TypedDict(
    "BatchAssociateProjectAssetsResponseResponseTypeDef",
    {
        "errors": List["AssetErrorDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateProjectAssetsRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateProjectAssetsRequestTypeDef",
    {
        "projectId": str,
        "assetIds": List[str],
    },
)
_OptionalBatchDisassociateProjectAssetsRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateProjectAssetsRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class BatchDisassociateProjectAssetsRequestTypeDef(
    _RequiredBatchDisassociateProjectAssetsRequestTypeDef,
    _OptionalBatchDisassociateProjectAssetsRequestTypeDef,
):
    pass


BatchDisassociateProjectAssetsResponseResponseTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsResponseResponseTypeDef",
    {
        "errors": List["AssetErrorDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutAssetPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorEntryTypeDef",
    {
        "entryId": str,
        "errors": List["BatchPutAssetPropertyErrorTypeDef"],
    },
)

BatchPutAssetPropertyErrorTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorTypeDef",
    {
        "errorCode": BatchPutAssetPropertyValueErrorCodeType,
        "errorMessage": str,
        "timestamps": List["TimeInNanosTypeDef"],
    },
)

BatchPutAssetPropertyValueRequestTypeDef = TypedDict(
    "BatchPutAssetPropertyValueRequestTypeDef",
    {
        "entries": List["PutAssetPropertyValueEntryTypeDef"],
    },
)

BatchPutAssetPropertyValueResponseResponseTypeDef = TypedDict(
    "BatchPutAssetPropertyValueResponseResponseTypeDef",
    {
        "errorEntries": List["BatchPutAssetPropertyErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompositeModelPropertyTypeDef = TypedDict(
    "CompositeModelPropertyTypeDef",
    {
        "name": str,
        "type": str,
        "assetProperty": "PropertyTypeDef",
    },
)

ConfigurationErrorDetailsTypeDef = TypedDict(
    "ConfigurationErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
)

_RequiredConfigurationStatusTypeDef = TypedDict(
    "_RequiredConfigurationStatusTypeDef",
    {
        "state": ConfigurationStateType,
    },
)
_OptionalConfigurationStatusTypeDef = TypedDict(
    "_OptionalConfigurationStatusTypeDef",
    {
        "error": "ConfigurationErrorDetailsTypeDef",
    },
    total=False,
)


class ConfigurationStatusTypeDef(
    _RequiredConfigurationStatusTypeDef, _OptionalConfigurationStatusTypeDef
):
    pass


_RequiredCreateAccessPolicyRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPolicyRequestTypeDef",
    {
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
    },
)
_OptionalCreateAccessPolicyRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPolicyRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAccessPolicyRequestTypeDef(
    _RequiredCreateAccessPolicyRequestTypeDef, _OptionalCreateAccessPolicyRequestTypeDef
):
    pass


CreateAccessPolicyResponseResponseTypeDef = TypedDict(
    "CreateAccessPolicyResponseResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetModelRequestTypeDef = TypedDict(
    "_RequiredCreateAssetModelRequestTypeDef",
    {
        "assetModelName": str,
    },
)
_OptionalCreateAssetModelRequestTypeDef = TypedDict(
    "_OptionalCreateAssetModelRequestTypeDef",
    {
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyDefinitionTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyDefinitionTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelDefinitionTypeDef"],
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAssetModelRequestTypeDef(
    _RequiredCreateAssetModelRequestTypeDef, _OptionalCreateAssetModelRequestTypeDef
):
    pass


CreateAssetModelResponseResponseTypeDef = TypedDict(
    "CreateAssetModelResponseResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetRequestTypeDef = TypedDict(
    "_RequiredCreateAssetRequestTypeDef",
    {
        "assetName": str,
        "assetModelId": str,
    },
)
_OptionalCreateAssetRequestTypeDef = TypedDict(
    "_OptionalCreateAssetRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAssetRequestTypeDef(
    _RequiredCreateAssetRequestTypeDef, _OptionalCreateAssetRequestTypeDef
):
    pass


CreateAssetResponseResponseTypeDef = TypedDict(
    "CreateAssetResponseResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDashboardRequestTypeDef = TypedDict(
    "_RequiredCreateDashboardRequestTypeDef",
    {
        "projectId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
    },
)
_OptionalCreateDashboardRequestTypeDef = TypedDict(
    "_OptionalCreateDashboardRequestTypeDef",
    {
        "dashboardDescription": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateDashboardRequestTypeDef(
    _RequiredCreateDashboardRequestTypeDef, _OptionalCreateDashboardRequestTypeDef
):
    pass


CreateDashboardResponseResponseTypeDef = TypedDict(
    "CreateDashboardResponseResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateGatewayRequestTypeDef",
    {
        "gatewayName": str,
        "gatewayPlatform": "GatewayPlatformTypeDef",
    },
)
_OptionalCreateGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateGatewayRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateGatewayRequestTypeDef(
    _RequiredCreateGatewayRequestTypeDef, _OptionalCreateGatewayRequestTypeDef
):
    pass


CreateGatewayResponseResponseTypeDef = TypedDict(
    "CreateGatewayResponseResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePortalRequestTypeDef = TypedDict(
    "_RequiredCreatePortalRequestTypeDef",
    {
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
    },
)
_OptionalCreatePortalRequestTypeDef = TypedDict(
    "_OptionalCreatePortalRequestTypeDef",
    {
        "portalDescription": str,
        "clientToken": str,
        "portalLogoImageFile": "ImageFileTypeDef",
        "tags": Dict[str, str],
        "portalAuthMode": AuthModeType,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
    },
    total=False,
)


class CreatePortalRequestTypeDef(
    _RequiredCreatePortalRequestTypeDef, _OptionalCreatePortalRequestTypeDef
):
    pass


CreatePortalResponseResponseTypeDef = TypedDict(
    "CreatePortalResponseResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalStartUrl": str,
        "portalStatus": "PortalStatusTypeDef",
        "ssoApplicationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestTypeDef",
    {
        "portalId": str,
        "projectName": str,
    },
)
_OptionalCreateProjectRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestTypeDef",
    {
        "projectDescription": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateProjectRequestTypeDef(
    _RequiredCreateProjectRequestTypeDef, _OptionalCreateProjectRequestTypeDef
):
    pass


CreateProjectResponseResponseTypeDef = TypedDict(
    "CreateProjectResponseResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDashboardSummaryTypeDef = TypedDict(
    "_RequiredDashboardSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)
_OptionalDashboardSummaryTypeDef = TypedDict(
    "_OptionalDashboardSummaryTypeDef",
    {
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
    total=False,
)


class DashboardSummaryTypeDef(_RequiredDashboardSummaryTypeDef, _OptionalDashboardSummaryTypeDef):
    pass


_RequiredDeleteAccessPolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteAccessPolicyRequestTypeDef",
    {
        "accessPolicyId": str,
    },
)
_OptionalDeleteAccessPolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteAccessPolicyRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteAccessPolicyRequestTypeDef(
    _RequiredDeleteAccessPolicyRequestTypeDef, _OptionalDeleteAccessPolicyRequestTypeDef
):
    pass


_RequiredDeleteAssetModelRequestTypeDef = TypedDict(
    "_RequiredDeleteAssetModelRequestTypeDef",
    {
        "assetModelId": str,
    },
)
_OptionalDeleteAssetModelRequestTypeDef = TypedDict(
    "_OptionalDeleteAssetModelRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteAssetModelRequestTypeDef(
    _RequiredDeleteAssetModelRequestTypeDef, _OptionalDeleteAssetModelRequestTypeDef
):
    pass


DeleteAssetModelResponseResponseTypeDef = TypedDict(
    "DeleteAssetModelResponseResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAssetRequestTypeDef = TypedDict(
    "_RequiredDeleteAssetRequestTypeDef",
    {
        "assetId": str,
    },
)
_OptionalDeleteAssetRequestTypeDef = TypedDict(
    "_OptionalDeleteAssetRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteAssetRequestTypeDef(
    _RequiredDeleteAssetRequestTypeDef, _OptionalDeleteAssetRequestTypeDef
):
    pass


DeleteAssetResponseResponseTypeDef = TypedDict(
    "DeleteAssetResponseResponseTypeDef",
    {
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDashboardRequestTypeDef = TypedDict(
    "_RequiredDeleteDashboardRequestTypeDef",
    {
        "dashboardId": str,
    },
)
_OptionalDeleteDashboardRequestTypeDef = TypedDict(
    "_OptionalDeleteDashboardRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteDashboardRequestTypeDef(
    _RequiredDeleteDashboardRequestTypeDef, _OptionalDeleteDashboardRequestTypeDef
):
    pass


DeleteGatewayRequestTypeDef = TypedDict(
    "DeleteGatewayRequestTypeDef",
    {
        "gatewayId": str,
    },
)

_RequiredDeletePortalRequestTypeDef = TypedDict(
    "_RequiredDeletePortalRequestTypeDef",
    {
        "portalId": str,
    },
)
_OptionalDeletePortalRequestTypeDef = TypedDict(
    "_OptionalDeletePortalRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeletePortalRequestTypeDef(
    _RequiredDeletePortalRequestTypeDef, _OptionalDeletePortalRequestTypeDef
):
    pass


DeletePortalResponseResponseTypeDef = TypedDict(
    "DeletePortalResponseResponseTypeDef",
    {
        "portalStatus": "PortalStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalDeleteProjectRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteProjectRequestTypeDef(
    _RequiredDeleteProjectRequestTypeDef, _OptionalDeleteProjectRequestTypeDef
):
    pass


DescribeAccessPolicyRequestTypeDef = TypedDict(
    "DescribeAccessPolicyRequestTypeDef",
    {
        "accessPolicyId": str,
    },
)

DescribeAccessPolicyResponseResponseTypeDef = TypedDict(
    "DescribeAccessPolicyResponseResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
        "accessPolicyCreationDate": datetime,
        "accessPolicyLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetModelRequestTypeDef = TypedDict(
    "DescribeAssetModelRequestTypeDef",
    {
        "assetModelId": str,
    },
)

DescribeAssetModelResponseResponseTypeDef = TypedDict(
    "DescribeAssetModelResponseResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelName": str,
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelTypeDef"],
        "assetModelCreationDate": datetime,
        "assetModelLastUpdateDate": datetime,
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetPropertyRequestTypeDef = TypedDict(
    "DescribeAssetPropertyRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
    },
)

DescribeAssetPropertyResponseResponseTypeDef = TypedDict(
    "DescribeAssetPropertyResponseResponseTypeDef",
    {
        "assetId": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperty": "PropertyTypeDef",
        "compositeModel": "CompositeModelPropertyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssetRequestTypeDef = TypedDict(
    "DescribeAssetRequestTypeDef",
    {
        "assetId": str,
    },
)

DescribeAssetResponseResponseTypeDef = TypedDict(
    "DescribeAssetResponseResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperties": List["AssetPropertyTypeDef"],
        "assetHierarchies": List["AssetHierarchyTypeDef"],
        "assetCompositeModels": List["AssetCompositeModelTypeDef"],
        "assetCreationDate": datetime,
        "assetLastUpdateDate": datetime,
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDashboardRequestTypeDef = TypedDict(
    "DescribeDashboardRequestTypeDef",
    {
        "dashboardId": str,
    },
)

DescribeDashboardResponseResponseTypeDef = TypedDict(
    "DescribeDashboardResponseResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "dashboardName": str,
        "projectId": str,
        "dashboardDescription": str,
        "dashboardDefinition": str,
        "dashboardCreationDate": datetime,
        "dashboardLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDefaultEncryptionConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeDefaultEncryptionConfigurationResponseResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayCapabilityConfigurationRequestTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
    },
)

DescribeGatewayCapabilityConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationResponseResponseTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayRequestTypeDef = TypedDict(
    "DescribeGatewayRequestTypeDef",
    {
        "gatewayId": str,
    },
)

DescribeGatewayResponseResponseTypeDef = TypedDict(
    "DescribeGatewayResponseResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "gatewayArn": str,
        "gatewayPlatform": "GatewayPlatformTypeDef",
        "gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"],
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePortalRequestTypeDef = TypedDict(
    "DescribePortalRequestTypeDef",
    {
        "portalId": str,
    },
)

DescribePortalResponseResponseTypeDef = TypedDict(
    "DescribePortalResponseResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalName": str,
        "portalDescription": str,
        "portalClientId": str,
        "portalStartUrl": str,
        "portalContactEmail": str,
        "portalStatus": "PortalStatusTypeDef",
        "portalCreationDate": datetime,
        "portalLastUpdateDate": datetime,
        "portalLogoImageLocation": "ImageLocationTypeDef",
        "roleArn": str,
        "portalAuthMode": AuthModeType,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestTypeDef = TypedDict(
    "DescribeProjectRequestTypeDef",
    {
        "projectId": str,
    },
)

DescribeProjectResponseResponseTypeDef = TypedDict(
    "DescribeProjectResponseResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "projectName": str,
        "portalId": str,
        "projectDescription": str,
        "projectCreationDate": datetime,
        "projectLastUpdateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateAssetsRequestTypeDef = TypedDict(
    "_RequiredDisassociateAssetsRequestTypeDef",
    {
        "assetId": str,
        "hierarchyId": str,
        "childAssetId": str,
    },
)
_OptionalDisassociateAssetsRequestTypeDef = TypedDict(
    "_OptionalDisassociateAssetsRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DisassociateAssetsRequestTypeDef(
    _RequiredDisassociateAssetsRequestTypeDef, _OptionalDisassociateAssetsRequestTypeDef
):
    pass


ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": ErrorCodeType,
        "message": str,
    },
)

ExpressionVariableTypeDef = TypedDict(
    "ExpressionVariableTypeDef",
    {
        "name": str,
        "value": "VariableValueTypeDef",
    },
)

GatewayCapabilitySummaryTypeDef = TypedDict(
    "GatewayCapabilitySummaryTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
    },
)

GatewayPlatformTypeDef = TypedDict(
    "GatewayPlatformTypeDef",
    {
        "greengrass": "GreengrassTypeDef",
    },
)

_RequiredGatewaySummaryTypeDef = TypedDict(
    "_RequiredGatewaySummaryTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
)
_OptionalGatewaySummaryTypeDef = TypedDict(
    "_OptionalGatewaySummaryTypeDef",
    {
        "gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"],
    },
    total=False,
)


class GatewaySummaryTypeDef(_RequiredGatewaySummaryTypeDef, _OptionalGatewaySummaryTypeDef):
    pass


_RequiredGetAssetPropertyAggregatesRequestTypeDef = TypedDict(
    "_RequiredGetAssetPropertyAggregatesRequestTypeDef",
    {
        "aggregateTypes": List[AggregateTypeType],
        "resolution": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
    },
)
_OptionalGetAssetPropertyAggregatesRequestTypeDef = TypedDict(
    "_OptionalGetAssetPropertyAggregatesRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "qualities": List[QualityType],
        "timeOrdering": TimeOrderingType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetAssetPropertyAggregatesRequestTypeDef(
    _RequiredGetAssetPropertyAggregatesRequestTypeDef,
    _OptionalGetAssetPropertyAggregatesRequestTypeDef,
):
    pass


GetAssetPropertyAggregatesResponseResponseTypeDef = TypedDict(
    "GetAssetPropertyAggregatesResponseResponseTypeDef",
    {
        "aggregatedValues": List["AggregatedValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssetPropertyValueHistoryRequestTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "startDate": Union[datetime, str],
        "endDate": Union[datetime, str],
        "qualities": List[QualityType],
        "timeOrdering": TimeOrderingType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetAssetPropertyValueHistoryResponseResponseTypeDef = TypedDict(
    "GetAssetPropertyValueHistoryResponseResponseTypeDef",
    {
        "assetPropertyValueHistory": List["AssetPropertyValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssetPropertyValueRequestTypeDef = TypedDict(
    "GetAssetPropertyValueRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)

GetAssetPropertyValueResponseResponseTypeDef = TypedDict(
    "GetAssetPropertyValueResponseResponseTypeDef",
    {
        "propertyValue": "AssetPropertyValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInterpolatedAssetPropertyValuesRequestTypeDef = TypedDict(
    "_RequiredGetInterpolatedAssetPropertyValuesRequestTypeDef",
    {
        "startTimeInSeconds": int,
        "endTimeInSeconds": int,
        "quality": QualityType,
        "intervalInSeconds": int,
        "type": str,
    },
)
_OptionalGetInterpolatedAssetPropertyValuesRequestTypeDef = TypedDict(
    "_OptionalGetInterpolatedAssetPropertyValuesRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "startTimeOffsetInNanos": int,
        "endTimeOffsetInNanos": int,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetInterpolatedAssetPropertyValuesRequestTypeDef(
    _RequiredGetInterpolatedAssetPropertyValuesRequestTypeDef,
    _OptionalGetInterpolatedAssetPropertyValuesRequestTypeDef,
):
    pass


GetInterpolatedAssetPropertyValuesResponseResponseTypeDef = TypedDict(
    "GetInterpolatedAssetPropertyValuesResponseResponseTypeDef",
    {
        "interpolatedAssetPropertyValues": List["InterpolatedAssetPropertyValueTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GreengrassTypeDef = TypedDict(
    "GreengrassTypeDef",
    {
        "groupArn": str,
    },
)

GroupIdentityTypeDef = TypedDict(
    "GroupIdentityTypeDef",
    {
        "id": str,
    },
)

IAMRoleIdentityTypeDef = TypedDict(
    "IAMRoleIdentityTypeDef",
    {
        "arn": str,
    },
)

IAMUserIdentityTypeDef = TypedDict(
    "IAMUserIdentityTypeDef",
    {
        "arn": str,
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "user": "UserIdentityTypeDef",
        "group": "GroupIdentityTypeDef",
        "iamUser": "IAMUserIdentityTypeDef",
        "iamRole": "IAMRoleIdentityTypeDef",
    },
    total=False,
)

ImageFileTypeDef = TypedDict(
    "ImageFileTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "type": Literal["PNG"],
    },
)

ImageLocationTypeDef = TypedDict(
    "ImageLocationTypeDef",
    {
        "id": str,
        "url": str,
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "id": str,
        "file": "ImageFileTypeDef",
    },
    total=False,
)

InterpolatedAssetPropertyValueTypeDef = TypedDict(
    "InterpolatedAssetPropertyValueTypeDef",
    {
        "timestamp": "TimeInNanosTypeDef",
        "value": "VariantTypeDef",
    },
)

ListAccessPoliciesRequestTypeDef = TypedDict(
    "ListAccessPoliciesRequestTypeDef",
    {
        "identityType": IdentityTypeType,
        "identityId": str,
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "iamArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAccessPoliciesResponseResponseTypeDef = TypedDict(
    "ListAccessPoliciesResponseResponseTypeDef",
    {
        "accessPolicySummaries": List["AccessPolicySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetModelsRequestTypeDef = TypedDict(
    "ListAssetModelsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssetModelsResponseResponseTypeDef = TypedDict(
    "ListAssetModelsResponseResponseTypeDef",
    {
        "assetModelSummaries": List["AssetModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssetRelationshipsRequestTypeDef = TypedDict(
    "_RequiredListAssetRelationshipsRequestTypeDef",
    {
        "assetId": str,
        "traversalType": Literal["PATH_TO_ROOT"],
    },
)
_OptionalListAssetRelationshipsRequestTypeDef = TypedDict(
    "_OptionalListAssetRelationshipsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssetRelationshipsRequestTypeDef(
    _RequiredListAssetRelationshipsRequestTypeDef, _OptionalListAssetRelationshipsRequestTypeDef
):
    pass


ListAssetRelationshipsResponseResponseTypeDef = TypedDict(
    "ListAssetRelationshipsResponseResponseTypeDef",
    {
        "assetRelationshipSummaries": List["AssetRelationshipSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssetsRequestTypeDef = TypedDict(
    "ListAssetsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "assetModelId": str,
        "filter": ListAssetsFilterType,
    },
    total=False,
)

ListAssetsResponseResponseTypeDef = TypedDict(
    "ListAssetsResponseResponseTypeDef",
    {
        "assetSummaries": List["AssetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedAssetsRequestTypeDef = TypedDict(
    "_RequiredListAssociatedAssetsRequestTypeDef",
    {
        "assetId": str,
    },
)
_OptionalListAssociatedAssetsRequestTypeDef = TypedDict(
    "_OptionalListAssociatedAssetsRequestTypeDef",
    {
        "hierarchyId": str,
        "traversalDirection": TraversalDirectionType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssociatedAssetsRequestTypeDef(
    _RequiredListAssociatedAssetsRequestTypeDef, _OptionalListAssociatedAssetsRequestTypeDef
):
    pass


ListAssociatedAssetsResponseResponseTypeDef = TypedDict(
    "ListAssociatedAssetsResponseResponseTypeDef",
    {
        "assetSummaries": List["AssociatedAssetsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDashboardsRequestTypeDef = TypedDict(
    "_RequiredListDashboardsRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListDashboardsRequestTypeDef = TypedDict(
    "_OptionalListDashboardsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDashboardsRequestTypeDef(
    _RequiredListDashboardsRequestTypeDef, _OptionalListDashboardsRequestTypeDef
):
    pass


ListDashboardsResponseResponseTypeDef = TypedDict(
    "ListDashboardsResponseResponseTypeDef",
    {
        "dashboardSummaries": List["DashboardSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysRequestTypeDef = TypedDict(
    "ListGatewaysRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListGatewaysResponseResponseTypeDef = TypedDict(
    "ListGatewaysResponseResponseTypeDef",
    {
        "gatewaySummaries": List["GatewaySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortalsRequestTypeDef = TypedDict(
    "ListPortalsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPortalsResponseResponseTypeDef = TypedDict(
    "ListPortalsResponseResponseTypeDef",
    {
        "portalSummaries": List["PortalSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectAssetsRequestTypeDef = TypedDict(
    "_RequiredListProjectAssetsRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListProjectAssetsRequestTypeDef = TypedDict(
    "_OptionalListProjectAssetsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListProjectAssetsRequestTypeDef(
    _RequiredListProjectAssetsRequestTypeDef, _OptionalListProjectAssetsRequestTypeDef
):
    pass


ListProjectAssetsResponseResponseTypeDef = TypedDict(
    "ListProjectAssetsResponseResponseTypeDef",
    {
        "assetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectsRequestTypeDef = TypedDict(
    "_RequiredListProjectsRequestTypeDef",
    {
        "portalId": str,
    },
)
_OptionalListProjectsRequestTypeDef = TypedDict(
    "_OptionalListProjectsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListProjectsRequestTypeDef(
    _RequiredListProjectsRequestTypeDef, _OptionalListProjectsRequestTypeDef
):
    pass


ListProjectsResponseResponseTypeDef = TypedDict(
    "ListProjectsResponseResponseTypeDef",
    {
        "projectSummaries": List["ProjectSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "level": LoggingLevelType,
    },
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "expression": str,
        "variables": List["ExpressionVariableTypeDef"],
        "window": "MetricWindowTypeDef",
    },
)

MetricWindowTypeDef = TypedDict(
    "MetricWindowTypeDef",
    {
        "tumbling": "TumblingWindowTypeDef",
    },
    total=False,
)

MonitorErrorDetailsTypeDef = TypedDict(
    "MonitorErrorDetailsTypeDef",
    {
        "code": MonitorErrorCodeType,
        "message": str,
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

PortalResourceTypeDef = TypedDict(
    "PortalResourceTypeDef",
    {
        "id": str,
    },
)

_RequiredPortalStatusTypeDef = TypedDict(
    "_RequiredPortalStatusTypeDef",
    {
        "state": PortalStateType,
    },
)
_OptionalPortalStatusTypeDef = TypedDict(
    "_OptionalPortalStatusTypeDef",
    {
        "error": "MonitorErrorDetailsTypeDef",
    },
    total=False,
)


class PortalStatusTypeDef(_RequiredPortalStatusTypeDef, _OptionalPortalStatusTypeDef):
    pass


_RequiredPortalSummaryTypeDef = TypedDict(
    "_RequiredPortalSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "startUrl": str,
        "status": "PortalStatusTypeDef",
    },
)
_OptionalPortalSummaryTypeDef = TypedDict(
    "_OptionalPortalSummaryTypeDef",
    {
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "roleArn": str,
    },
    total=False,
)


class PortalSummaryTypeDef(_RequiredPortalSummaryTypeDef, _OptionalPortalSummaryTypeDef):
    pass


ProjectResourceTypeDef = TypedDict(
    "ProjectResourceTypeDef",
    {
        "id": str,
    },
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
    total=False,
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass


PropertyNotificationTypeDef = TypedDict(
    "PropertyNotificationTypeDef",
    {
        "topic": str,
        "state": PropertyNotificationStateType,
    },
)

_RequiredPropertyTypeDef = TypedDict(
    "_RequiredPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": PropertyDataTypeType,
    },
)
_OptionalPropertyTypeDef = TypedDict(
    "_OptionalPropertyTypeDef",
    {
        "alias": str,
        "notification": "PropertyNotificationTypeDef",
        "unit": str,
        "type": "PropertyTypeTypeDef",
    },
    total=False,
)


class PropertyTypeDef(_RequiredPropertyTypeDef, _OptionalPropertyTypeDef):
    pass


PropertyTypeTypeDef = TypedDict(
    "PropertyTypeTypeDef",
    {
        "attribute": "AttributeTypeDef",
        "measurement": Dict[str, Any],
        "transform": "TransformTypeDef",
        "metric": "MetricTypeDef",
    },
    total=False,
)

_RequiredPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryTypeDef",
    {
        "entryId": str,
        "propertyValues": List["AssetPropertyValueTypeDef"],
    },
)
_OptionalPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryTypeDef",
    {
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
    },
    total=False,
)


class PutAssetPropertyValueEntryTypeDef(
    _RequiredPutAssetPropertyValueEntryTypeDef, _OptionalPutAssetPropertyValueEntryTypeDef
):
    pass


_RequiredPutDefaultEncryptionConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutDefaultEncryptionConfigurationRequestTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalPutDefaultEncryptionConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutDefaultEncryptionConfigurationRequestTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)


class PutDefaultEncryptionConfigurationRequestTypeDef(
    _RequiredPutDefaultEncryptionConfigurationRequestTypeDef,
    _OptionalPutDefaultEncryptionConfigurationRequestTypeDef,
):
    pass


PutDefaultEncryptionConfigurationResponseResponseTypeDef = TypedDict(
    "PutDefaultEncryptionConfigurationResponseResponseTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyArn": str,
        "configurationStatus": "ConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "portal": "PortalResourceTypeDef",
        "project": "ProjectResourceTypeDef",
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTimeInNanosTypeDef = TypedDict(
    "_RequiredTimeInNanosTypeDef",
    {
        "timeInSeconds": int,
    },
)
_OptionalTimeInNanosTypeDef = TypedDict(
    "_OptionalTimeInNanosTypeDef",
    {
        "offsetInNanos": int,
    },
    total=False,
)


class TimeInNanosTypeDef(_RequiredTimeInNanosTypeDef, _OptionalTimeInNanosTypeDef):
    pass


TransformTypeDef = TypedDict(
    "TransformTypeDef",
    {
        "expression": str,
        "variables": List["ExpressionVariableTypeDef"],
    },
)

TumblingWindowTypeDef = TypedDict(
    "TumblingWindowTypeDef",
    {
        "interval": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAccessPolicyRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessPolicyRequestTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": PermissionType,
    },
)
_OptionalUpdateAccessPolicyRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessPolicyRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateAccessPolicyRequestTypeDef(
    _RequiredUpdateAccessPolicyRequestTypeDef, _OptionalUpdateAccessPolicyRequestTypeDef
):
    pass


_RequiredUpdateAssetModelRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetModelRequestTypeDef",
    {
        "assetModelId": str,
        "assetModelName": str,
    },
)
_OptionalUpdateAssetModelRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetModelRequestTypeDef",
    {
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyTypeDef"],
        "assetModelCompositeModels": List["AssetModelCompositeModelTypeDef"],
        "clientToken": str,
    },
    total=False,
)


class UpdateAssetModelRequestTypeDef(
    _RequiredUpdateAssetModelRequestTypeDef, _OptionalUpdateAssetModelRequestTypeDef
):
    pass


UpdateAssetModelResponseResponseTypeDef = TypedDict(
    "UpdateAssetModelResponseResponseTypeDef",
    {
        "assetModelStatus": "AssetModelStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssetPropertyRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetPropertyRequestTypeDef",
    {
        "assetId": str,
        "propertyId": str,
    },
)
_OptionalUpdateAssetPropertyRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetPropertyRequestTypeDef",
    {
        "propertyAlias": str,
        "propertyNotificationState": PropertyNotificationStateType,
        "clientToken": str,
    },
    total=False,
)


class UpdateAssetPropertyRequestTypeDef(
    _RequiredUpdateAssetPropertyRequestTypeDef, _OptionalUpdateAssetPropertyRequestTypeDef
):
    pass


_RequiredUpdateAssetRequestTypeDef = TypedDict(
    "_RequiredUpdateAssetRequestTypeDef",
    {
        "assetId": str,
        "assetName": str,
    },
)
_OptionalUpdateAssetRequestTypeDef = TypedDict(
    "_OptionalUpdateAssetRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateAssetRequestTypeDef(
    _RequiredUpdateAssetRequestTypeDef, _OptionalUpdateAssetRequestTypeDef
):
    pass


UpdateAssetResponseResponseTypeDef = TypedDict(
    "UpdateAssetResponseResponseTypeDef",
    {
        "assetStatus": "AssetStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDashboardRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardRequestTypeDef",
    {
        "dashboardId": str,
        "dashboardName": str,
        "dashboardDefinition": str,
    },
)
_OptionalUpdateDashboardRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardRequestTypeDef",
    {
        "dashboardDescription": str,
        "clientToken": str,
    },
    total=False,
)


class UpdateDashboardRequestTypeDef(
    _RequiredUpdateDashboardRequestTypeDef, _OptionalUpdateDashboardRequestTypeDef
):
    pass


UpdateGatewayCapabilityConfigurationRequestTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationRequestTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
    },
)

UpdateGatewayCapabilityConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationResponseResponseTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": CapabilitySyncStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayRequestTypeDef = TypedDict(
    "UpdateGatewayRequestTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
    },
)

_RequiredUpdatePortalRequestTypeDef = TypedDict(
    "_RequiredUpdatePortalRequestTypeDef",
    {
        "portalId": str,
        "portalName": str,
        "portalContactEmail": str,
        "roleArn": str,
    },
)
_OptionalUpdatePortalRequestTypeDef = TypedDict(
    "_OptionalUpdatePortalRequestTypeDef",
    {
        "portalDescription": str,
        "portalLogoImage": "ImageTypeDef",
        "clientToken": str,
        "notificationSenderEmail": str,
        "alarms": "AlarmsTypeDef",
    },
    total=False,
)


class UpdatePortalRequestTypeDef(
    _RequiredUpdatePortalRequestTypeDef, _OptionalUpdatePortalRequestTypeDef
):
    pass


UpdatePortalResponseResponseTypeDef = TypedDict(
    "UpdatePortalResponseResponseTypeDef",
    {
        "portalStatus": "PortalStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestTypeDef",
    {
        "projectId": str,
        "projectName": str,
    },
)
_OptionalUpdateProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestTypeDef",
    {
        "projectDescription": str,
        "clientToken": str,
    },
    total=False,
)


class UpdateProjectRequestTypeDef(
    _RequiredUpdateProjectRequestTypeDef, _OptionalUpdateProjectRequestTypeDef
):
    pass


UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "id": str,
    },
)

_RequiredVariableValueTypeDef = TypedDict(
    "_RequiredVariableValueTypeDef",
    {
        "propertyId": str,
    },
)
_OptionalVariableValueTypeDef = TypedDict(
    "_OptionalVariableValueTypeDef",
    {
        "hierarchyId": str,
    },
    total=False,
)


class VariableValueTypeDef(_RequiredVariableValueTypeDef, _OptionalVariableValueTypeDef):
    pass


VariantTypeDef = TypedDict(
    "VariantTypeDef",
    {
        "stringValue": str,
        "integerValue": int,
        "doubleValue": float,
        "booleanValue": bool,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
