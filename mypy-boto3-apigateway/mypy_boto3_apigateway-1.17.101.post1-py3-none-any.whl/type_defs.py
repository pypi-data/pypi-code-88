"""
Type annotations for apigateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApiKeySourceTypeType,
    AuthorizerTypeType,
    CacheClusterSizeType,
    CacheClusterStatusType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DocumentationPartTypeType,
    DomainNameStatusType,
    EndpointTypeType,
    GatewayResponseTypeType,
    IntegrationTypeType,
    LocationStatusTypeType,
    OpType,
    PutModeType,
    QuotaPeriodTypeType,
    SecurityPolicyType,
    UnauthorizedCacheControlHeaderStrategyType,
    VpcLinkStatusType,
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
    "AccessLogSettingsTypeDef",
    "AccountResponseTypeDef",
    "ApiKeyIdsResponseTypeDef",
    "ApiKeyResponseTypeDef",
    "ApiKeysResponseTypeDef",
    "ApiStageTypeDef",
    "AuthorizerResponseTypeDef",
    "AuthorizersResponseTypeDef",
    "BasePathMappingResponseTypeDef",
    "BasePathMappingsResponseTypeDef",
    "CanarySettingsTypeDef",
    "ClientCertificateResponseTypeDef",
    "ClientCertificatesResponseTypeDef",
    "CreateApiKeyRequestTypeDef",
    "CreateAuthorizerRequestTypeDef",
    "CreateBasePathMappingRequestTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDocumentationPartRequestTypeDef",
    "CreateDocumentationVersionRequestTypeDef",
    "CreateDomainNameRequestTypeDef",
    "CreateModelRequestTypeDef",
    "CreateRequestValidatorRequestTypeDef",
    "CreateResourceRequestTypeDef",
    "CreateRestApiRequestTypeDef",
    "CreateStageRequestTypeDef",
    "CreateUsagePlanKeyRequestTypeDef",
    "CreateUsagePlanRequestTypeDef",
    "CreateVpcLinkRequestTypeDef",
    "DeleteApiKeyRequestTypeDef",
    "DeleteAuthorizerRequestTypeDef",
    "DeleteBasePathMappingRequestTypeDef",
    "DeleteClientCertificateRequestTypeDef",
    "DeleteDeploymentRequestTypeDef",
    "DeleteDocumentationPartRequestTypeDef",
    "DeleteDocumentationVersionRequestTypeDef",
    "DeleteDomainNameRequestTypeDef",
    "DeleteGatewayResponseRequestTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseRequestTypeDef",
    "DeleteMethodRequestTypeDef",
    "DeleteMethodResponseRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteRequestValidatorRequestTypeDef",
    "DeleteResourceRequestTypeDef",
    "DeleteRestApiRequestTypeDef",
    "DeleteStageRequestTypeDef",
    "DeleteUsagePlanKeyRequestTypeDef",
    "DeleteUsagePlanRequestTypeDef",
    "DeleteVpcLinkRequestTypeDef",
    "DeploymentCanarySettingsTypeDef",
    "DeploymentResponseTypeDef",
    "DeploymentsResponseTypeDef",
    "DocumentationPartIdsResponseTypeDef",
    "DocumentationPartLocationTypeDef",
    "DocumentationPartResponseTypeDef",
    "DocumentationPartsResponseTypeDef",
    "DocumentationVersionResponseTypeDef",
    "DocumentationVersionsResponseTypeDef",
    "DomainNameResponseTypeDef",
    "DomainNamesResponseTypeDef",
    "EndpointConfigurationTypeDef",
    "ExportResponseResponseTypeDef",
    "FlushStageAuthorizersCacheRequestTypeDef",
    "FlushStageCacheRequestTypeDef",
    "GatewayResponseResponseTypeDef",
    "GatewayResponsesResponseTypeDef",
    "GenerateClientCertificateRequestTypeDef",
    "GetApiKeyRequestTypeDef",
    "GetApiKeysRequestTypeDef",
    "GetAuthorizerRequestTypeDef",
    "GetAuthorizersRequestTypeDef",
    "GetBasePathMappingRequestTypeDef",
    "GetBasePathMappingsRequestTypeDef",
    "GetClientCertificateRequestTypeDef",
    "GetClientCertificatesRequestTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentsRequestTypeDef",
    "GetDocumentationPartRequestTypeDef",
    "GetDocumentationPartsRequestTypeDef",
    "GetDocumentationVersionRequestTypeDef",
    "GetDocumentationVersionsRequestTypeDef",
    "GetDomainNameRequestTypeDef",
    "GetDomainNamesRequestTypeDef",
    "GetExportRequestTypeDef",
    "GetGatewayResponseRequestTypeDef",
    "GetGatewayResponsesRequestTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseRequestTypeDef",
    "GetMethodRequestTypeDef",
    "GetMethodResponseRequestTypeDef",
    "GetModelRequestTypeDef",
    "GetModelTemplateRequestTypeDef",
    "GetModelsRequestTypeDef",
    "GetRequestValidatorRequestTypeDef",
    "GetRequestValidatorsRequestTypeDef",
    "GetResourceRequestTypeDef",
    "GetResourcesRequestTypeDef",
    "GetRestApiRequestTypeDef",
    "GetRestApisRequestTypeDef",
    "GetSdkRequestTypeDef",
    "GetSdkTypeRequestTypeDef",
    "GetSdkTypesRequestTypeDef",
    "GetStageRequestTypeDef",
    "GetStagesRequestTypeDef",
    "GetTagsRequestTypeDef",
    "GetUsagePlanKeyRequestTypeDef",
    "GetUsagePlanKeysRequestTypeDef",
    "GetUsagePlanRequestTypeDef",
    "GetUsagePlansRequestTypeDef",
    "GetUsageRequestTypeDef",
    "GetVpcLinkRequestTypeDef",
    "GetVpcLinksRequestTypeDef",
    "ImportApiKeysRequestTypeDef",
    "ImportDocumentationPartsRequestTypeDef",
    "ImportRestApiRequestTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "MethodResponseTypeDef",
    "MethodSettingTypeDef",
    "MethodSnapshotTypeDef",
    "MethodTypeDef",
    "ModelResponseTypeDef",
    "ModelsResponseTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "PatchOperationTypeDef",
    "PutGatewayResponseRequestTypeDef",
    "PutIntegrationRequestTypeDef",
    "PutIntegrationResponseRequestTypeDef",
    "PutMethodRequestTypeDef",
    "PutMethodResponseRequestTypeDef",
    "PutRestApiRequestTypeDef",
    "QuotaSettingsTypeDef",
    "RequestValidatorResponseTypeDef",
    "RequestValidatorsResponseTypeDef",
    "ResourceResponseTypeDef",
    "ResourcesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestApiResponseTypeDef",
    "RestApisResponseTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "SdkResponseResponseTypeDef",
    "SdkTypeResponseTypeDef",
    "SdkTypesResponseTypeDef",
    "StageKeyTypeDef",
    "StageResponseTypeDef",
    "StagesResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagsResponseTypeDef",
    "TemplateResponseTypeDef",
    "TestInvokeAuthorizerRequestTypeDef",
    "TestInvokeAuthorizerResponseResponseTypeDef",
    "TestInvokeMethodRequestTypeDef",
    "TestInvokeMethodResponseResponseTypeDef",
    "ThrottleSettingsTypeDef",
    "TlsConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountRequestTypeDef",
    "UpdateApiKeyRequestTypeDef",
    "UpdateAuthorizerRequestTypeDef",
    "UpdateBasePathMappingRequestTypeDef",
    "UpdateClientCertificateRequestTypeDef",
    "UpdateDeploymentRequestTypeDef",
    "UpdateDocumentationPartRequestTypeDef",
    "UpdateDocumentationVersionRequestTypeDef",
    "UpdateDomainNameRequestTypeDef",
    "UpdateGatewayResponseRequestTypeDef",
    "UpdateIntegrationRequestTypeDef",
    "UpdateIntegrationResponseRequestTypeDef",
    "UpdateMethodRequestTypeDef",
    "UpdateMethodResponseRequestTypeDef",
    "UpdateModelRequestTypeDef",
    "UpdateRequestValidatorRequestTypeDef",
    "UpdateResourceRequestTypeDef",
    "UpdateRestApiRequestTypeDef",
    "UpdateStageRequestTypeDef",
    "UpdateUsagePlanRequestTypeDef",
    "UpdateUsageRequestTypeDef",
    "UpdateVpcLinkRequestTypeDef",
    "UsagePlanKeyResponseTypeDef",
    "UsagePlanKeysResponseTypeDef",
    "UsagePlanResponseTypeDef",
    "UsagePlansResponseTypeDef",
    "UsageResponseTypeDef",
    "VpcLinkResponseTypeDef",
    "VpcLinksResponseTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "format": str,
        "destinationArn": str,
    },
    total=False,
)

AccountResponseTypeDef = TypedDict(
    "AccountResponseTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": "ThrottleSettingsTypeDef",
        "features": List[str],
        "apiKeyVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiKeyIdsResponseTypeDef = TypedDict(
    "ApiKeyIdsResponseTypeDef",
    {
        "ids": List[str],
        "warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiKeyResponseTypeDef = TypedDict(
    "ApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiKeysResponseTypeDef = TypedDict(
    "ApiKeysResponseTypeDef",
    {
        "warnings": List[str],
        "position": str,
        "items": List["ApiKeyResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApiStageTypeDef = TypedDict(
    "ApiStageTypeDef",
    {
        "apiId": str,
        "stage": str,
        "throttle": Dict[str, "ThrottleSettingsTypeDef"],
    },
    total=False,
)

AuthorizerResponseTypeDef = TypedDict(
    "AuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": AuthorizerTypeType,
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizersResponseTypeDef = TypedDict(
    "AuthorizersResponseTypeDef",
    {
        "position": str,
        "items": List["AuthorizerResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BasePathMappingResponseTypeDef = TypedDict(
    "BasePathMappingResponseTypeDef",
    {
        "basePath": str,
        "restApiId": str,
        "stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BasePathMappingsResponseTypeDef = TypedDict(
    "BasePathMappingsResponseTypeDef",
    {
        "position": str,
        "items": List["BasePathMappingResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CanarySettingsTypeDef = TypedDict(
    "CanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "deploymentId": str,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

ClientCertificateResponseTypeDef = TypedDict(
    "ClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClientCertificatesResponseTypeDef = TypedDict(
    "ClientCertificatesResponseTypeDef",
    {
        "position": str,
        "items": List["ClientCertificateResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateApiKeyRequestTypeDef = TypedDict(
    "CreateApiKeyRequestTypeDef",
    {
        "name": str,
        "description": str,
        "enabled": bool,
        "generateDistinctId": bool,
        "value": str,
        "stageKeys": List["StageKeyTypeDef"],
        "customerId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateAuthorizerRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "type": AuthorizerTypeType,
    },
)
_OptionalCreateAuthorizerRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestTypeDef",
    {
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class CreateAuthorizerRequestTypeDef(
    _RequiredCreateAuthorizerRequestTypeDef, _OptionalCreateAuthorizerRequestTypeDef
):
    pass


_RequiredCreateBasePathMappingRequestTypeDef = TypedDict(
    "_RequiredCreateBasePathMappingRequestTypeDef",
    {
        "domainName": str,
        "restApiId": str,
    },
)
_OptionalCreateBasePathMappingRequestTypeDef = TypedDict(
    "_OptionalCreateBasePathMappingRequestTypeDef",
    {
        "basePath": str,
        "stage": str,
    },
    total=False,
)


class CreateBasePathMappingRequestTypeDef(
    _RequiredCreateBasePathMappingRequestTypeDef, _OptionalCreateBasePathMappingRequestTypeDef
):
    pass


_RequiredCreateDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalCreateDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestTypeDef",
    {
        "stageName": str,
        "stageDescription": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "variables": Dict[str, str],
        "canarySettings": "DeploymentCanarySettingsTypeDef",
        "tracingEnabled": bool,
    },
    total=False,
)


class CreateDeploymentRequestTypeDef(
    _RequiredCreateDeploymentRequestTypeDef, _OptionalCreateDeploymentRequestTypeDef
):
    pass


CreateDocumentationPartRequestTypeDef = TypedDict(
    "CreateDocumentationPartRequestTypeDef",
    {
        "restApiId": str,
        "location": "DocumentationPartLocationTypeDef",
        "properties": str,
    },
)

_RequiredCreateDocumentationVersionRequestTypeDef = TypedDict(
    "_RequiredCreateDocumentationVersionRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)
_OptionalCreateDocumentationVersionRequestTypeDef = TypedDict(
    "_OptionalCreateDocumentationVersionRequestTypeDef",
    {
        "stageName": str,
        "description": str,
    },
    total=False,
)


class CreateDocumentationVersionRequestTypeDef(
    _RequiredCreateDocumentationVersionRequestTypeDef,
    _OptionalCreateDocumentationVersionRequestTypeDef,
):
    pass


_RequiredCreateDomainNameRequestTypeDef = TypedDict(
    "_RequiredCreateDomainNameRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCreateDomainNameRequestTypeDef = TypedDict(
    "_OptionalCreateDomainNameRequestTypeDef",
    {
        "certificateName": str,
        "certificateBody": str,
        "certificatePrivateKey": str,
        "certificateChain": str,
        "certificateArn": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "tags": Dict[str, str],
        "securityPolicy": SecurityPolicyType,
        "mutualTlsAuthentication": "MutualTlsAuthenticationInputTypeDef",
    },
    total=False,
)


class CreateDomainNameRequestTypeDef(
    _RequiredCreateDomainNameRequestTypeDef, _OptionalCreateDomainNameRequestTypeDef
):
    pass


_RequiredCreateModelRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "contentType": str,
    },
)
_OptionalCreateModelRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestTypeDef",
    {
        "description": str,
        "schema": str,
    },
    total=False,
)


class CreateModelRequestTypeDef(
    _RequiredCreateModelRequestTypeDef, _OptionalCreateModelRequestTypeDef
):
    pass


_RequiredCreateRequestValidatorRequestTypeDef = TypedDict(
    "_RequiredCreateRequestValidatorRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalCreateRequestValidatorRequestTypeDef = TypedDict(
    "_OptionalCreateRequestValidatorRequestTypeDef",
    {
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
    },
    total=False,
)


class CreateRequestValidatorRequestTypeDef(
    _RequiredCreateRequestValidatorRequestTypeDef, _OptionalCreateRequestValidatorRequestTypeDef
):
    pass


CreateResourceRequestTypeDef = TypedDict(
    "CreateResourceRequestTypeDef",
    {
        "restApiId": str,
        "parentId": str,
        "pathPart": str,
    },
)

_RequiredCreateRestApiRequestTypeDef = TypedDict(
    "_RequiredCreateRestApiRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateRestApiRequestTypeDef = TypedDict(
    "_OptionalCreateRestApiRequestTypeDef",
    {
        "description": str,
        "version": str,
        "cloneFrom": str,
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": ApiKeySourceTypeType,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
    },
    total=False,
)


class CreateRestApiRequestTypeDef(
    _RequiredCreateRestApiRequestTypeDef, _OptionalCreateRestApiRequestTypeDef
):
    pass


_RequiredCreateStageRequestTypeDef = TypedDict(
    "_RequiredCreateStageRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "deploymentId": str,
    },
)
_OptionalCreateStageRequestTypeDef = TypedDict(
    "_OptionalCreateStageRequestTypeDef",
    {
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "variables": Dict[str, str],
        "documentationVersion": str,
        "canarySettings": "CanarySettingsTypeDef",
        "tracingEnabled": bool,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateStageRequestTypeDef(
    _RequiredCreateStageRequestTypeDef, _OptionalCreateStageRequestTypeDef
):
    pass


CreateUsagePlanKeyRequestTypeDef = TypedDict(
    "CreateUsagePlanKeyRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
        "keyType": str,
    },
)

_RequiredCreateUsagePlanRequestTypeDef = TypedDict(
    "_RequiredCreateUsagePlanRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateUsagePlanRequestTypeDef = TypedDict(
    "_OptionalCreateUsagePlanRequestTypeDef",
    {
        "description": str,
        "apiStages": List["ApiStageTypeDef"],
        "throttle": "ThrottleSettingsTypeDef",
        "quota": "QuotaSettingsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateUsagePlanRequestTypeDef(
    _RequiredCreateUsagePlanRequestTypeDef, _OptionalCreateUsagePlanRequestTypeDef
):
    pass


_RequiredCreateVpcLinkRequestTypeDef = TypedDict(
    "_RequiredCreateVpcLinkRequestTypeDef",
    {
        "name": str,
        "targetArns": List[str],
    },
)
_OptionalCreateVpcLinkRequestTypeDef = TypedDict(
    "_OptionalCreateVpcLinkRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateVpcLinkRequestTypeDef(
    _RequiredCreateVpcLinkRequestTypeDef, _OptionalCreateVpcLinkRequestTypeDef
):
    pass


DeleteApiKeyRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestTypeDef",
    {
        "apiKey": str,
    },
)

DeleteAuthorizerRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)

DeleteBasePathMappingRequestTypeDef = TypedDict(
    "DeleteBasePathMappingRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)

DeleteClientCertificateRequestTypeDef = TypedDict(
    "DeleteClientCertificateRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)

DeleteDeploymentRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)

DeleteDocumentationPartRequestTypeDef = TypedDict(
    "DeleteDocumentationPartRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)

DeleteDocumentationVersionRequestTypeDef = TypedDict(
    "DeleteDocumentationVersionRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)

DeleteDomainNameRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteGatewayResponseRequestTypeDef = TypedDict(
    "DeleteGatewayResponseRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)

DeleteIntegrationRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

DeleteIntegrationResponseRequestTypeDef = TypedDict(
    "DeleteIntegrationResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

DeleteMethodRequestTypeDef = TypedDict(
    "DeleteMethodRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

DeleteMethodResponseRequestTypeDef = TypedDict(
    "DeleteMethodResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

DeleteModelRequestTypeDef = TypedDict(
    "DeleteModelRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)

DeleteRequestValidatorRequestTypeDef = TypedDict(
    "DeleteRequestValidatorRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)

DeleteResourceRequestTypeDef = TypedDict(
    "DeleteResourceRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)

DeleteRestApiRequestTypeDef = TypedDict(
    "DeleteRestApiRequestTypeDef",
    {
        "restApiId": str,
    },
)

DeleteStageRequestTypeDef = TypedDict(
    "DeleteStageRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

DeleteUsagePlanKeyRequestTypeDef = TypedDict(
    "DeleteUsagePlanKeyRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)

DeleteUsagePlanRequestTypeDef = TypedDict(
    "DeleteUsagePlanRequestTypeDef",
    {
        "usagePlanId": str,
    },
)

DeleteVpcLinkRequestTypeDef = TypedDict(
    "DeleteVpcLinkRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)

DeploymentCanarySettingsTypeDef = TypedDict(
    "DeploymentCanarySettingsTypeDef",
    {
        "percentTraffic": float,
        "stageVariableOverrides": Dict[str, str],
        "useStageCache": bool,
    },
    total=False,
)

DeploymentResponseTypeDef = TypedDict(
    "DeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, "MethodSnapshotTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentsResponseTypeDef = TypedDict(
    "DeploymentsResponseTypeDef",
    {
        "position": str,
        "items": List["DeploymentResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationPartIdsResponseTypeDef = TypedDict(
    "DocumentationPartIdsResponseTypeDef",
    {
        "ids": List[str],
        "warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredDocumentationPartLocationTypeDef",
    {
        "type": DocumentationPartTypeType,
    },
)
_OptionalDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalDocumentationPartLocationTypeDef",
    {
        "path": str,
        "method": str,
        "statusCode": str,
        "name": str,
    },
    total=False,
)


class DocumentationPartLocationTypeDef(
    _RequiredDocumentationPartLocationTypeDef, _OptionalDocumentationPartLocationTypeDef
):
    pass


DocumentationPartResponseTypeDef = TypedDict(
    "DocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": "DocumentationPartLocationTypeDef",
        "properties": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationPartsResponseTypeDef = TypedDict(
    "DocumentationPartsResponseTypeDef",
    {
        "position": str,
        "items": List["DocumentationPartResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationVersionResponseTypeDef = TypedDict(
    "DocumentationVersionResponseTypeDef",
    {
        "version": str,
        "createdDate": datetime,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentationVersionsResponseTypeDef = TypedDict(
    "DocumentationVersionsResponseTypeDef",
    {
        "position": str,
        "items": List["DocumentationVersionResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainNameResponseTypeDef = TypedDict(
    "DomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "domainNameStatus": DomainNameStatusType,
        "domainNameStatusMessage": str,
        "securityPolicy": SecurityPolicyType,
        "tags": Dict[str, str],
        "mutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainNamesResponseTypeDef = TypedDict(
    "DomainNamesResponseTypeDef",
    {
        "position": str,
        "items": List["DomainNameResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "types": List[EndpointTypeType],
        "vpcEndpointIds": List[str],
    },
    total=False,
)

ExportResponseResponseTypeDef = TypedDict(
    "ExportResponseResponseTypeDef",
    {
        "contentType": str,
        "contentDisposition": str,
        "body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FlushStageAuthorizersCacheRequestTypeDef = TypedDict(
    "FlushStageAuthorizersCacheRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

FlushStageCacheRequestTypeDef = TypedDict(
    "FlushStageCacheRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

GatewayResponseResponseTypeDef = TypedDict(
    "GatewayResponseResponseTypeDef",
    {
        "responseType": GatewayResponseTypeType,
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GatewayResponsesResponseTypeDef = TypedDict(
    "GatewayResponsesResponseTypeDef",
    {
        "position": str,
        "items": List["GatewayResponseResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateClientCertificateRequestTypeDef = TypedDict(
    "GenerateClientCertificateRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredGetApiKeyRequestTypeDef = TypedDict(
    "_RequiredGetApiKeyRequestTypeDef",
    {
        "apiKey": str,
    },
)
_OptionalGetApiKeyRequestTypeDef = TypedDict(
    "_OptionalGetApiKeyRequestTypeDef",
    {
        "includeValue": bool,
    },
    total=False,
)


class GetApiKeyRequestTypeDef(_RequiredGetApiKeyRequestTypeDef, _OptionalGetApiKeyRequestTypeDef):
    pass


GetApiKeysRequestTypeDef = TypedDict(
    "GetApiKeysRequestTypeDef",
    {
        "position": str,
        "limit": int,
        "nameQuery": str,
        "customerId": str,
        "includeValues": bool,
    },
    total=False,
)

GetAuthorizerRequestTypeDef = TypedDict(
    "GetAuthorizerRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)

_RequiredGetAuthorizersRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizersRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetAuthorizersRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizersRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetAuthorizersRequestTypeDef(
    _RequiredGetAuthorizersRequestTypeDef, _OptionalGetAuthorizersRequestTypeDef
):
    pass


GetBasePathMappingRequestTypeDef = TypedDict(
    "GetBasePathMappingRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)

_RequiredGetBasePathMappingsRequestTypeDef = TypedDict(
    "_RequiredGetBasePathMappingsRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalGetBasePathMappingsRequestTypeDef = TypedDict(
    "_OptionalGetBasePathMappingsRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetBasePathMappingsRequestTypeDef(
    _RequiredGetBasePathMappingsRequestTypeDef, _OptionalGetBasePathMappingsRequestTypeDef
):
    pass


GetClientCertificateRequestTypeDef = TypedDict(
    "GetClientCertificateRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)

GetClientCertificatesRequestTypeDef = TypedDict(
    "GetClientCertificatesRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetDeploymentRequestTypeDef = TypedDict(
    "_RequiredGetDeploymentRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)
_OptionalGetDeploymentRequestTypeDef = TypedDict(
    "_OptionalGetDeploymentRequestTypeDef",
    {
        "embed": List[str],
    },
    total=False,
)


class GetDeploymentRequestTypeDef(
    _RequiredGetDeploymentRequestTypeDef, _OptionalGetDeploymentRequestTypeDef
):
    pass


_RequiredGetDeploymentsRequestTypeDef = TypedDict(
    "_RequiredGetDeploymentsRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetDeploymentsRequestTypeDef = TypedDict(
    "_OptionalGetDeploymentsRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetDeploymentsRequestTypeDef(
    _RequiredGetDeploymentsRequestTypeDef, _OptionalGetDeploymentsRequestTypeDef
):
    pass


GetDocumentationPartRequestTypeDef = TypedDict(
    "GetDocumentationPartRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)

_RequiredGetDocumentationPartsRequestTypeDef = TypedDict(
    "_RequiredGetDocumentationPartsRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetDocumentationPartsRequestTypeDef = TypedDict(
    "_OptionalGetDocumentationPartsRequestTypeDef",
    {
        "type": DocumentationPartTypeType,
        "nameQuery": str,
        "path": str,
        "position": str,
        "limit": int,
        "locationStatus": LocationStatusTypeType,
    },
    total=False,
)


class GetDocumentationPartsRequestTypeDef(
    _RequiredGetDocumentationPartsRequestTypeDef, _OptionalGetDocumentationPartsRequestTypeDef
):
    pass


GetDocumentationVersionRequestTypeDef = TypedDict(
    "GetDocumentationVersionRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)

_RequiredGetDocumentationVersionsRequestTypeDef = TypedDict(
    "_RequiredGetDocumentationVersionsRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetDocumentationVersionsRequestTypeDef = TypedDict(
    "_OptionalGetDocumentationVersionsRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetDocumentationVersionsRequestTypeDef(
    _RequiredGetDocumentationVersionsRequestTypeDef, _OptionalGetDocumentationVersionsRequestTypeDef
):
    pass


GetDomainNameRequestTypeDef = TypedDict(
    "GetDomainNameRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainNamesRequestTypeDef = TypedDict(
    "GetDomainNamesRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetExportRequestTypeDef = TypedDict(
    "_RequiredGetExportRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "exportType": str,
    },
)
_OptionalGetExportRequestTypeDef = TypedDict(
    "_OptionalGetExportRequestTypeDef",
    {
        "parameters": Dict[str, str],
        "accepts": str,
    },
    total=False,
)


class GetExportRequestTypeDef(_RequiredGetExportRequestTypeDef, _OptionalGetExportRequestTypeDef):
    pass


GetGatewayResponseRequestTypeDef = TypedDict(
    "GetGatewayResponseRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)

_RequiredGetGatewayResponsesRequestTypeDef = TypedDict(
    "_RequiredGetGatewayResponsesRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetGatewayResponsesRequestTypeDef = TypedDict(
    "_OptionalGetGatewayResponsesRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetGatewayResponsesRequestTypeDef(
    _RequiredGetGatewayResponsesRequestTypeDef, _OptionalGetGatewayResponsesRequestTypeDef
):
    pass


GetIntegrationRequestTypeDef = TypedDict(
    "GetIntegrationRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

GetIntegrationResponseRequestTypeDef = TypedDict(
    "GetIntegrationResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

GetMethodRequestTypeDef = TypedDict(
    "GetMethodRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)

GetMethodResponseRequestTypeDef = TypedDict(
    "GetMethodResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)

_RequiredGetModelRequestTypeDef = TypedDict(
    "_RequiredGetModelRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)
_OptionalGetModelRequestTypeDef = TypedDict(
    "_OptionalGetModelRequestTypeDef",
    {
        "flatten": bool,
    },
    total=False,
)


class GetModelRequestTypeDef(_RequiredGetModelRequestTypeDef, _OptionalGetModelRequestTypeDef):
    pass


GetModelTemplateRequestTypeDef = TypedDict(
    "GetModelTemplateRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)

_RequiredGetModelsRequestTypeDef = TypedDict(
    "_RequiredGetModelsRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetModelsRequestTypeDef = TypedDict(
    "_OptionalGetModelsRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetModelsRequestTypeDef(_RequiredGetModelsRequestTypeDef, _OptionalGetModelsRequestTypeDef):
    pass


GetRequestValidatorRequestTypeDef = TypedDict(
    "GetRequestValidatorRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)

_RequiredGetRequestValidatorsRequestTypeDef = TypedDict(
    "_RequiredGetRequestValidatorsRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetRequestValidatorsRequestTypeDef = TypedDict(
    "_OptionalGetRequestValidatorsRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetRequestValidatorsRequestTypeDef(
    _RequiredGetRequestValidatorsRequestTypeDef, _OptionalGetRequestValidatorsRequestTypeDef
):
    pass


_RequiredGetResourceRequestTypeDef = TypedDict(
    "_RequiredGetResourceRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)
_OptionalGetResourceRequestTypeDef = TypedDict(
    "_OptionalGetResourceRequestTypeDef",
    {
        "embed": List[str],
    },
    total=False,
)


class GetResourceRequestTypeDef(
    _RequiredGetResourceRequestTypeDef, _OptionalGetResourceRequestTypeDef
):
    pass


_RequiredGetResourcesRequestTypeDef = TypedDict(
    "_RequiredGetResourcesRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetResourcesRequestTypeDef = TypedDict(
    "_OptionalGetResourcesRequestTypeDef",
    {
        "position": str,
        "limit": int,
        "embed": List[str],
    },
    total=False,
)


class GetResourcesRequestTypeDef(
    _RequiredGetResourcesRequestTypeDef, _OptionalGetResourcesRequestTypeDef
):
    pass


GetRestApiRequestTypeDef = TypedDict(
    "GetRestApiRequestTypeDef",
    {
        "restApiId": str,
    },
)

GetRestApisRequestTypeDef = TypedDict(
    "GetRestApisRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetSdkRequestTypeDef = TypedDict(
    "_RequiredGetSdkRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "sdkType": str,
    },
)
_OptionalGetSdkRequestTypeDef = TypedDict(
    "_OptionalGetSdkRequestTypeDef",
    {
        "parameters": Dict[str, str],
    },
    total=False,
)


class GetSdkRequestTypeDef(_RequiredGetSdkRequestTypeDef, _OptionalGetSdkRequestTypeDef):
    pass


GetSdkTypeRequestTypeDef = TypedDict(
    "GetSdkTypeRequestTypeDef",
    {
        "id": str,
    },
)

GetSdkTypesRequestTypeDef = TypedDict(
    "GetSdkTypesRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

GetStageRequestTypeDef = TypedDict(
    "GetStageRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)

_RequiredGetStagesRequestTypeDef = TypedDict(
    "_RequiredGetStagesRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalGetStagesRequestTypeDef = TypedDict(
    "_OptionalGetStagesRequestTypeDef",
    {
        "deploymentId": str,
    },
    total=False,
)


class GetStagesRequestTypeDef(_RequiredGetStagesRequestTypeDef, _OptionalGetStagesRequestTypeDef):
    pass


_RequiredGetTagsRequestTypeDef = TypedDict(
    "_RequiredGetTagsRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalGetTagsRequestTypeDef = TypedDict(
    "_OptionalGetTagsRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetTagsRequestTypeDef(_RequiredGetTagsRequestTypeDef, _OptionalGetTagsRequestTypeDef):
    pass


GetUsagePlanKeyRequestTypeDef = TypedDict(
    "GetUsagePlanKeyRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)

_RequiredGetUsagePlanKeysRequestTypeDef = TypedDict(
    "_RequiredGetUsagePlanKeysRequestTypeDef",
    {
        "usagePlanId": str,
    },
)
_OptionalGetUsagePlanKeysRequestTypeDef = TypedDict(
    "_OptionalGetUsagePlanKeysRequestTypeDef",
    {
        "position": str,
        "limit": int,
        "nameQuery": str,
    },
    total=False,
)


class GetUsagePlanKeysRequestTypeDef(
    _RequiredGetUsagePlanKeysRequestTypeDef, _OptionalGetUsagePlanKeysRequestTypeDef
):
    pass


GetUsagePlanRequestTypeDef = TypedDict(
    "GetUsagePlanRequestTypeDef",
    {
        "usagePlanId": str,
    },
)

GetUsagePlansRequestTypeDef = TypedDict(
    "GetUsagePlansRequestTypeDef",
    {
        "position": str,
        "keyId": str,
        "limit": int,
    },
    total=False,
)

_RequiredGetUsageRequestTypeDef = TypedDict(
    "_RequiredGetUsageRequestTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
    },
)
_OptionalGetUsageRequestTypeDef = TypedDict(
    "_OptionalGetUsageRequestTypeDef",
    {
        "keyId": str,
        "position": str,
        "limit": int,
    },
    total=False,
)


class GetUsageRequestTypeDef(_RequiredGetUsageRequestTypeDef, _OptionalGetUsageRequestTypeDef):
    pass


GetVpcLinkRequestTypeDef = TypedDict(
    "GetVpcLinkRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)

GetVpcLinksRequestTypeDef = TypedDict(
    "GetVpcLinksRequestTypeDef",
    {
        "position": str,
        "limit": int,
    },
    total=False,
)

_RequiredImportApiKeysRequestTypeDef = TypedDict(
    "_RequiredImportApiKeysRequestTypeDef",
    {
        "body": Union[bytes, IO[bytes], StreamingBody],
        "format": Literal["csv"],
    },
)
_OptionalImportApiKeysRequestTypeDef = TypedDict(
    "_OptionalImportApiKeysRequestTypeDef",
    {
        "failOnWarnings": bool,
    },
    total=False,
)


class ImportApiKeysRequestTypeDef(
    _RequiredImportApiKeysRequestTypeDef, _OptionalImportApiKeysRequestTypeDef
):
    pass


_RequiredImportDocumentationPartsRequestTypeDef = TypedDict(
    "_RequiredImportDocumentationPartsRequestTypeDef",
    {
        "restApiId": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportDocumentationPartsRequestTypeDef = TypedDict(
    "_OptionalImportDocumentationPartsRequestTypeDef",
    {
        "mode": PutModeType,
        "failOnWarnings": bool,
    },
    total=False,
)


class ImportDocumentationPartsRequestTypeDef(
    _RequiredImportDocumentationPartsRequestTypeDef, _OptionalImportDocumentationPartsRequestTypeDef
):
    pass


_RequiredImportRestApiRequestTypeDef = TypedDict(
    "_RequiredImportRestApiRequestTypeDef",
    {
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportRestApiRequestTypeDef = TypedDict(
    "_OptionalImportRestApiRequestTypeDef",
    {
        "failOnWarnings": bool,
        "parameters": Dict[str, str],
    },
    total=False,
)


class ImportRestApiRequestTypeDef(
    _RequiredImportRestApiRequestTypeDef, _OptionalImportRestApiRequestTypeDef
):
    pass


IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": ContentHandlingStrategyType,
    },
    total=False,
)

IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "type": IntegrationTypeType,
        "httpMethod": str,
        "uri": str,
        "connectionType": ConnectionTypeType,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": ContentHandlingStrategyType,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, "IntegrationResponseTypeDef"],
        "tlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)

MethodResponseTypeDef = TypedDict(
    "MethodResponseTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)

MethodSettingTypeDef = TypedDict(
    "MethodSettingTypeDef",
    {
        "metricsEnabled": bool,
        "loggingLevel": str,
        "dataTraceEnabled": bool,
        "throttlingBurstLimit": int,
        "throttlingRateLimit": float,
        "cachingEnabled": bool,
        "cacheTtlInSeconds": int,
        "cacheDataEncrypted": bool,
        "requireAuthorizationForCacheControl": bool,
        "unauthorizedCacheControlHeaderStrategy": UnauthorizedCacheControlHeaderStrategyType,
    },
    total=False,
)

MethodSnapshotTypeDef = TypedDict(
    "MethodSnapshotTypeDef",
    {
        "authorizationType": str,
        "apiKeyRequired": bool,
    },
    total=False,
)

MethodTypeDef = TypedDict(
    "MethodTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, "MethodResponseTypeDef"],
        "methodIntegration": "IntegrationTypeDef",
        "authorizationScopes": List[str],
    },
    total=False,
)

ModelResponseTypeDef = TypedDict(
    "ModelResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "schema": str,
        "contentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelsResponseTypeDef = TypedDict(
    "ModelsResponseTypeDef",
    {
        "position": str,
        "items": List["ModelResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {
        "truststoreUri": str,
        "truststoreVersion": str,
    },
    total=False,
)

MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {
        "truststoreUri": str,
        "truststoreVersion": str,
        "truststoreWarnings": List[str],
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

PatchOperationTypeDef = TypedDict(
    "PatchOperationTypeDef",
    {
        "op": OpType,
        "path": str,
        "value": str,
        "from": str,
    },
    total=False,
)

_RequiredPutGatewayResponseRequestTypeDef = TypedDict(
    "_RequiredPutGatewayResponseRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)
_OptionalPutGatewayResponseRequestTypeDef = TypedDict(
    "_OptionalPutGatewayResponseRequestTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
    },
    total=False,
)


class PutGatewayResponseRequestTypeDef(
    _RequiredPutGatewayResponseRequestTypeDef, _OptionalPutGatewayResponseRequestTypeDef
):
    pass


_RequiredPutIntegrationRequestTypeDef = TypedDict(
    "_RequiredPutIntegrationRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "type": IntegrationTypeType,
    },
)
_OptionalPutIntegrationRequestTypeDef = TypedDict(
    "_OptionalPutIntegrationRequestTypeDef",
    {
        "integrationHttpMethod": str,
        "uri": str,
        "connectionType": ConnectionTypeType,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "contentHandling": ContentHandlingStrategyType,
        "timeoutInMillis": int,
        "tlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)


class PutIntegrationRequestTypeDef(
    _RequiredPutIntegrationRequestTypeDef, _OptionalPutIntegrationRequestTypeDef
):
    pass


_RequiredPutIntegrationResponseRequestTypeDef = TypedDict(
    "_RequiredPutIntegrationResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalPutIntegrationResponseRequestTypeDef = TypedDict(
    "_OptionalPutIntegrationResponseRequestTypeDef",
    {
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": ContentHandlingStrategyType,
    },
    total=False,
)


class PutIntegrationResponseRequestTypeDef(
    _RequiredPutIntegrationResponseRequestTypeDef, _OptionalPutIntegrationResponseRequestTypeDef
):
    pass


_RequiredPutMethodRequestTypeDef = TypedDict(
    "_RequiredPutMethodRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "authorizationType": str,
    },
)
_OptionalPutMethodRequestTypeDef = TypedDict(
    "_OptionalPutMethodRequestTypeDef",
    {
        "authorizerId": str,
        "apiKeyRequired": bool,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "requestValidatorId": str,
        "authorizationScopes": List[str],
    },
    total=False,
)


class PutMethodRequestTypeDef(_RequiredPutMethodRequestTypeDef, _OptionalPutMethodRequestTypeDef):
    pass


_RequiredPutMethodResponseRequestTypeDef = TypedDict(
    "_RequiredPutMethodResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalPutMethodResponseRequestTypeDef = TypedDict(
    "_OptionalPutMethodResponseRequestTypeDef",
    {
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
    },
    total=False,
)


class PutMethodResponseRequestTypeDef(
    _RequiredPutMethodResponseRequestTypeDef, _OptionalPutMethodResponseRequestTypeDef
):
    pass


_RequiredPutRestApiRequestTypeDef = TypedDict(
    "_RequiredPutRestApiRequestTypeDef",
    {
        "restApiId": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalPutRestApiRequestTypeDef = TypedDict(
    "_OptionalPutRestApiRequestTypeDef",
    {
        "mode": PutModeType,
        "failOnWarnings": bool,
        "parameters": Dict[str, str],
    },
    total=False,
)


class PutRestApiRequestTypeDef(
    _RequiredPutRestApiRequestTypeDef, _OptionalPutRestApiRequestTypeDef
):
    pass


QuotaSettingsTypeDef = TypedDict(
    "QuotaSettingsTypeDef",
    {
        "limit": int,
        "offset": int,
        "period": QuotaPeriodTypeType,
    },
    total=False,
)

RequestValidatorResponseTypeDef = TypedDict(
    "RequestValidatorResponseTypeDef",
    {
        "id": str,
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestValidatorsResponseTypeDef = TypedDict(
    "RequestValidatorsResponseTypeDef",
    {
        "position": str,
        "items": List["RequestValidatorResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceResponseTypeDef = TypedDict(
    "ResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, "MethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourcesResponseTypeDef = TypedDict(
    "ResourcesResponseTypeDef",
    {
        "position": str,
        "items": List["ResourceResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RestApiResponseTypeDef = TypedDict(
    "RestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": ApiKeySourceTypeType,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestApisResponseTypeDef = TypedDict(
    "RestApisResponseTypeDef",
    {
        "position": str,
        "items": List["RestApiResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SdkConfigurationPropertyTypeDef = TypedDict(
    "SdkConfigurationPropertyTypeDef",
    {
        "name": str,
        "friendlyName": str,
        "description": str,
        "required": bool,
        "defaultValue": str,
    },
    total=False,
)

SdkResponseResponseTypeDef = TypedDict(
    "SdkResponseResponseTypeDef",
    {
        "contentType": str,
        "contentDisposition": str,
        "body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SdkTypeResponseTypeDef = TypedDict(
    "SdkTypeResponseTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List["SdkConfigurationPropertyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SdkTypesResponseTypeDef = TypedDict(
    "SdkTypesResponseTypeDef",
    {
        "position": str,
        "items": List["SdkTypeResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StageKeyTypeDef = TypedDict(
    "StageKeyTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
    total=False,
)

StageResponseTypeDef = TypedDict(
    "StageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "cacheClusterStatus": CacheClusterStatusType,
        "methodSettings": Dict[str, "MethodSettingTypeDef"],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": "AccessLogSettingsTypeDef",
        "canarySettings": "CanarySettingsTypeDef",
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StagesResponseTypeDef = TypedDict(
    "StagesResponseTypeDef",
    {
        "item": List["StageResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TagsResponseTypeDef = TypedDict(
    "TagsResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TemplateResponseTypeDef = TypedDict(
    "TemplateResponseTypeDef",
    {
        "value": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestInvokeAuthorizerRequestTypeDef = TypedDict(
    "_RequiredTestInvokeAuthorizerRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)
_OptionalTestInvokeAuthorizerRequestTypeDef = TypedDict(
    "_OptionalTestInvokeAuthorizerRequestTypeDef",
    {
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "pathWithQueryString": str,
        "body": str,
        "stageVariables": Dict[str, str],
        "additionalContext": Dict[str, str],
    },
    total=False,
)


class TestInvokeAuthorizerRequestTypeDef(
    _RequiredTestInvokeAuthorizerRequestTypeDef, _OptionalTestInvokeAuthorizerRequestTypeDef
):
    pass


TestInvokeAuthorizerResponseResponseTypeDef = TypedDict(
    "TestInvokeAuthorizerResponseResponseTypeDef",
    {
        "clientStatus": int,
        "log": str,
        "latency": int,
        "principalId": str,
        "policy": str,
        "authorization": Dict[str, List[str]],
        "claims": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTestInvokeMethodRequestTypeDef = TypedDict(
    "_RequiredTestInvokeMethodRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
_OptionalTestInvokeMethodRequestTypeDef = TypedDict(
    "_OptionalTestInvokeMethodRequestTypeDef",
    {
        "pathWithQueryString": str,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "clientCertificateId": str,
        "stageVariables": Dict[str, str],
    },
    total=False,
)


class TestInvokeMethodRequestTypeDef(
    _RequiredTestInvokeMethodRequestTypeDef, _OptionalTestInvokeMethodRequestTypeDef
):
    pass


TestInvokeMethodResponseResponseTypeDef = TypedDict(
    "TestInvokeMethodResponseResponseTypeDef",
    {
        "status": int,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "log": str,
        "latency": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThrottleSettingsTypeDef = TypedDict(
    "ThrottleSettingsTypeDef",
    {
        "burstLimit": int,
        "rateLimit": float,
    },
    total=False,
)

TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "insecureSkipVerification": bool,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccountRequestTypeDef = TypedDict(
    "UpdateAccountRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)

_RequiredUpdateApiKeyRequestTypeDef = TypedDict(
    "_RequiredUpdateApiKeyRequestTypeDef",
    {
        "apiKey": str,
    },
)
_OptionalUpdateApiKeyRequestTypeDef = TypedDict(
    "_OptionalUpdateApiKeyRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateApiKeyRequestTypeDef(
    _RequiredUpdateApiKeyRequestTypeDef, _OptionalUpdateApiKeyRequestTypeDef
):
    pass


_RequiredUpdateAuthorizerRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)
_OptionalUpdateAuthorizerRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateAuthorizerRequestTypeDef(
    _RequiredUpdateAuthorizerRequestTypeDef, _OptionalUpdateAuthorizerRequestTypeDef
):
    pass


_RequiredUpdateBasePathMappingRequestTypeDef = TypedDict(
    "_RequiredUpdateBasePathMappingRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)
_OptionalUpdateBasePathMappingRequestTypeDef = TypedDict(
    "_OptionalUpdateBasePathMappingRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateBasePathMappingRequestTypeDef(
    _RequiredUpdateBasePathMappingRequestTypeDef, _OptionalUpdateBasePathMappingRequestTypeDef
):
    pass


_RequiredUpdateClientCertificateRequestTypeDef = TypedDict(
    "_RequiredUpdateClientCertificateRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)
_OptionalUpdateClientCertificateRequestTypeDef = TypedDict(
    "_OptionalUpdateClientCertificateRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateClientCertificateRequestTypeDef(
    _RequiredUpdateClientCertificateRequestTypeDef, _OptionalUpdateClientCertificateRequestTypeDef
):
    pass


_RequiredUpdateDeploymentRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)
_OptionalUpdateDeploymentRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateDeploymentRequestTypeDef(
    _RequiredUpdateDeploymentRequestTypeDef, _OptionalUpdateDeploymentRequestTypeDef
):
    pass


_RequiredUpdateDocumentationPartRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentationPartRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)
_OptionalUpdateDocumentationPartRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentationPartRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateDocumentationPartRequestTypeDef(
    _RequiredUpdateDocumentationPartRequestTypeDef, _OptionalUpdateDocumentationPartRequestTypeDef
):
    pass


_RequiredUpdateDocumentationVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentationVersionRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)
_OptionalUpdateDocumentationVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentationVersionRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateDocumentationVersionRequestTypeDef(
    _RequiredUpdateDocumentationVersionRequestTypeDef,
    _OptionalUpdateDocumentationVersionRequestTypeDef,
):
    pass


_RequiredUpdateDomainNameRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalUpdateDomainNameRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateDomainNameRequestTypeDef(
    _RequiredUpdateDomainNameRequestTypeDef, _OptionalUpdateDomainNameRequestTypeDef
):
    pass


_RequiredUpdateGatewayResponseRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayResponseRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)
_OptionalUpdateGatewayResponseRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayResponseRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateGatewayResponseRequestTypeDef(
    _RequiredUpdateGatewayResponseRequestTypeDef, _OptionalUpdateGatewayResponseRequestTypeDef
):
    pass


_RequiredUpdateIntegrationRequestTypeDef = TypedDict(
    "_RequiredUpdateIntegrationRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
_OptionalUpdateIntegrationRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateIntegrationRequestTypeDef(
    _RequiredUpdateIntegrationRequestTypeDef, _OptionalUpdateIntegrationRequestTypeDef
):
    pass


_RequiredUpdateIntegrationResponseRequestTypeDef = TypedDict(
    "_RequiredUpdateIntegrationResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalUpdateIntegrationResponseRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationResponseRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateIntegrationResponseRequestTypeDef(
    _RequiredUpdateIntegrationResponseRequestTypeDef,
    _OptionalUpdateIntegrationResponseRequestTypeDef,
):
    pass


_RequiredUpdateMethodRequestTypeDef = TypedDict(
    "_RequiredUpdateMethodRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
_OptionalUpdateMethodRequestTypeDef = TypedDict(
    "_OptionalUpdateMethodRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateMethodRequestTypeDef(
    _RequiredUpdateMethodRequestTypeDef, _OptionalUpdateMethodRequestTypeDef
):
    pass


_RequiredUpdateMethodResponseRequestTypeDef = TypedDict(
    "_RequiredUpdateMethodResponseRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
_OptionalUpdateMethodResponseRequestTypeDef = TypedDict(
    "_OptionalUpdateMethodResponseRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateMethodResponseRequestTypeDef(
    _RequiredUpdateMethodResponseRequestTypeDef, _OptionalUpdateMethodResponseRequestTypeDef
):
    pass


_RequiredUpdateModelRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)
_OptionalUpdateModelRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateModelRequestTypeDef(
    _RequiredUpdateModelRequestTypeDef, _OptionalUpdateModelRequestTypeDef
):
    pass


_RequiredUpdateRequestValidatorRequestTypeDef = TypedDict(
    "_RequiredUpdateRequestValidatorRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)
_OptionalUpdateRequestValidatorRequestTypeDef = TypedDict(
    "_OptionalUpdateRequestValidatorRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateRequestValidatorRequestTypeDef(
    _RequiredUpdateRequestValidatorRequestTypeDef, _OptionalUpdateRequestValidatorRequestTypeDef
):
    pass


_RequiredUpdateResourceRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)
_OptionalUpdateResourceRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateResourceRequestTypeDef(
    _RequiredUpdateResourceRequestTypeDef, _OptionalUpdateResourceRequestTypeDef
):
    pass


_RequiredUpdateRestApiRequestTypeDef = TypedDict(
    "_RequiredUpdateRestApiRequestTypeDef",
    {
        "restApiId": str,
    },
)
_OptionalUpdateRestApiRequestTypeDef = TypedDict(
    "_OptionalUpdateRestApiRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateRestApiRequestTypeDef(
    _RequiredUpdateRestApiRequestTypeDef, _OptionalUpdateRestApiRequestTypeDef
):
    pass


_RequiredUpdateStageRequestTypeDef = TypedDict(
    "_RequiredUpdateStageRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)
_OptionalUpdateStageRequestTypeDef = TypedDict(
    "_OptionalUpdateStageRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateStageRequestTypeDef(
    _RequiredUpdateStageRequestTypeDef, _OptionalUpdateStageRequestTypeDef
):
    pass


_RequiredUpdateUsagePlanRequestTypeDef = TypedDict(
    "_RequiredUpdateUsagePlanRequestTypeDef",
    {
        "usagePlanId": str,
    },
)
_OptionalUpdateUsagePlanRequestTypeDef = TypedDict(
    "_OptionalUpdateUsagePlanRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateUsagePlanRequestTypeDef(
    _RequiredUpdateUsagePlanRequestTypeDef, _OptionalUpdateUsagePlanRequestTypeDef
):
    pass


_RequiredUpdateUsageRequestTypeDef = TypedDict(
    "_RequiredUpdateUsageRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)
_OptionalUpdateUsageRequestTypeDef = TypedDict(
    "_OptionalUpdateUsageRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateUsageRequestTypeDef(
    _RequiredUpdateUsageRequestTypeDef, _OptionalUpdateUsageRequestTypeDef
):
    pass


_RequiredUpdateVpcLinkRequestTypeDef = TypedDict(
    "_RequiredUpdateVpcLinkRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)
_OptionalUpdateVpcLinkRequestTypeDef = TypedDict(
    "_OptionalUpdateVpcLinkRequestTypeDef",
    {
        "patchOperations": List["PatchOperationTypeDef"],
    },
    total=False,
)


class UpdateVpcLinkRequestTypeDef(
    _RequiredUpdateVpcLinkRequestTypeDef, _OptionalUpdateVpcLinkRequestTypeDef
):
    pass


UsagePlanKeyResponseTypeDef = TypedDict(
    "UsagePlanKeyResponseTypeDef",
    {
        "id": str,
        "type": str,
        "value": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsagePlanKeysResponseTypeDef = TypedDict(
    "UsagePlanKeysResponseTypeDef",
    {
        "position": str,
        "items": List["UsagePlanKeyResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsagePlanResponseTypeDef = TypedDict(
    "UsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List["ApiStageTypeDef"],
        "throttle": "ThrottleSettingsTypeDef",
        "quota": "QuotaSettingsTypeDef",
        "productCode": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsagePlansResponseTypeDef = TypedDict(
    "UsagePlansResponseTypeDef",
    {
        "position": str,
        "items": List["UsagePlanResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageResponseTypeDef = TypedDict(
    "UsageResponseTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcLinkResponseTypeDef = TypedDict(
    "VpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": VpcLinkStatusType,
        "statusMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcLinksResponseTypeDef = TypedDict(
    "VpcLinksResponseTypeDef",
    {
        "position": str,
        "items": List["VpcLinkResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
