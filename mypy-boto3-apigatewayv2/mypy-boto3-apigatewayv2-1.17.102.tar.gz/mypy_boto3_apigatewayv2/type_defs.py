"""
Type annotations for apigatewayv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigatewayv2.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AuthorizationTypeType,
    AuthorizerTypeType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DeploymentStatusType,
    DomainNameStatusType,
    EndpointTypeType,
    IntegrationTypeType,
    JSONYAMLType,
    LoggingLevelType,
    PassthroughBehaviorType,
    ProtocolTypeType,
    SecurityPolicyType,
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
    "ApiMappingTypeDef",
    "ApiTypeDef",
    "AuthorizerTypeDef",
    "CorsTypeDef",
    "CreateApiMappingRequestTypeDef",
    "CreateApiMappingResponseResponseTypeDef",
    "CreateApiRequestTypeDef",
    "CreateApiResponseResponseTypeDef",
    "CreateAuthorizerRequestTypeDef",
    "CreateAuthorizerResponseResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseResponseTypeDef",
    "CreateDomainNameRequestTypeDef",
    "CreateDomainNameResponseResponseTypeDef",
    "CreateIntegrationRequestTypeDef",
    "CreateIntegrationResponseRequestTypeDef",
    "CreateIntegrationResponseResponseResponseTypeDef",
    "CreateIntegrationResultResponseTypeDef",
    "CreateModelRequestTypeDef",
    "CreateModelResponseResponseTypeDef",
    "CreateRouteRequestTypeDef",
    "CreateRouteResponseRequestTypeDef",
    "CreateRouteResponseResponseResponseTypeDef",
    "CreateRouteResultResponseTypeDef",
    "CreateStageRequestTypeDef",
    "CreateStageResponseResponseTypeDef",
    "CreateVpcLinkRequestTypeDef",
    "CreateVpcLinkResponseResponseTypeDef",
    "DeleteAccessLogSettingsRequestTypeDef",
    "DeleteApiMappingRequestTypeDef",
    "DeleteApiRequestTypeDef",
    "DeleteAuthorizerRequestTypeDef",
    "DeleteCorsConfigurationRequestTypeDef",
    "DeleteDeploymentRequestTypeDef",
    "DeleteDomainNameRequestTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteRouteRequestParameterRequestTypeDef",
    "DeleteRouteRequestTypeDef",
    "DeleteRouteResponseRequestTypeDef",
    "DeleteRouteSettingsRequestTypeDef",
    "DeleteStageRequestTypeDef",
    "DeleteVpcLinkRequestTypeDef",
    "DeploymentTypeDef",
    "DomainNameConfigurationTypeDef",
    "DomainNameTypeDef",
    "ExportApiRequestTypeDef",
    "ExportApiResponseResponseTypeDef",
    "GetApiMappingRequestTypeDef",
    "GetApiMappingResponseResponseTypeDef",
    "GetApiMappingsRequestTypeDef",
    "GetApiMappingsResponseResponseTypeDef",
    "GetApiRequestTypeDef",
    "GetApiResponseResponseTypeDef",
    "GetApisRequestTypeDef",
    "GetApisResponseResponseTypeDef",
    "GetAuthorizerRequestTypeDef",
    "GetAuthorizerResponseResponseTypeDef",
    "GetAuthorizersRequestTypeDef",
    "GetAuthorizersResponseResponseTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentResponseResponseTypeDef",
    "GetDeploymentsRequestTypeDef",
    "GetDeploymentsResponseResponseTypeDef",
    "GetDomainNameRequestTypeDef",
    "GetDomainNameResponseResponseTypeDef",
    "GetDomainNamesRequestTypeDef",
    "GetDomainNamesResponseResponseTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseRequestTypeDef",
    "GetIntegrationResponseResponseResponseTypeDef",
    "GetIntegrationResponsesRequestTypeDef",
    "GetIntegrationResponsesResponseResponseTypeDef",
    "GetIntegrationResultResponseTypeDef",
    "GetIntegrationsRequestTypeDef",
    "GetIntegrationsResponseResponseTypeDef",
    "GetModelRequestTypeDef",
    "GetModelResponseResponseTypeDef",
    "GetModelTemplateRequestTypeDef",
    "GetModelTemplateResponseResponseTypeDef",
    "GetModelsRequestTypeDef",
    "GetModelsResponseResponseTypeDef",
    "GetRouteRequestTypeDef",
    "GetRouteResponseRequestTypeDef",
    "GetRouteResponseResponseResponseTypeDef",
    "GetRouteResponsesRequestTypeDef",
    "GetRouteResponsesResponseResponseTypeDef",
    "GetRouteResultResponseTypeDef",
    "GetRoutesRequestTypeDef",
    "GetRoutesResponseResponseTypeDef",
    "GetStageRequestTypeDef",
    "GetStageResponseResponseTypeDef",
    "GetStagesRequestTypeDef",
    "GetStagesResponseResponseTypeDef",
    "GetTagsRequestTypeDef",
    "GetTagsResponseResponseTypeDef",
    "GetVpcLinkRequestTypeDef",
    "GetVpcLinkResponseResponseTypeDef",
    "GetVpcLinksRequestTypeDef",
    "GetVpcLinksResponseResponseTypeDef",
    "ImportApiRequestTypeDef",
    "ImportApiResponseResponseTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "JWTConfigurationTypeDef",
    "ModelTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ReimportApiRequestTypeDef",
    "ReimportApiResponseResponseTypeDef",
    "ResetAuthorizersCacheRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RouteResponseTypeDef",
    "RouteSettingsTypeDef",
    "RouteTypeDef",
    "StageTypeDef",
    "TagResourceRequestTypeDef",
    "TlsConfigInputTypeDef",
    "TlsConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApiMappingRequestTypeDef",
    "UpdateApiMappingResponseResponseTypeDef",
    "UpdateApiRequestTypeDef",
    "UpdateApiResponseResponseTypeDef",
    "UpdateAuthorizerRequestTypeDef",
    "UpdateAuthorizerResponseResponseTypeDef",
    "UpdateDeploymentRequestTypeDef",
    "UpdateDeploymentResponseResponseTypeDef",
    "UpdateDomainNameRequestTypeDef",
    "UpdateDomainNameResponseResponseTypeDef",
    "UpdateIntegrationRequestTypeDef",
    "UpdateIntegrationResponseRequestTypeDef",
    "UpdateIntegrationResponseResponseResponseTypeDef",
    "UpdateIntegrationResultResponseTypeDef",
    "UpdateModelRequestTypeDef",
    "UpdateModelResponseResponseTypeDef",
    "UpdateRouteRequestTypeDef",
    "UpdateRouteResponseRequestTypeDef",
    "UpdateRouteResponseResponseResponseTypeDef",
    "UpdateRouteResultResponseTypeDef",
    "UpdateStageRequestTypeDef",
    "UpdateStageResponseResponseTypeDef",
    "UpdateVpcLinkRequestTypeDef",
    "UpdateVpcLinkResponseResponseTypeDef",
    "VpcLinkTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "DestinationArn": str,
        "Format": str,
    },
    total=False,
)

_RequiredApiMappingTypeDef = TypedDict(
    "_RequiredApiMappingTypeDef",
    {
        "ApiId": str,
        "Stage": str,
    },
)
_OptionalApiMappingTypeDef = TypedDict(
    "_OptionalApiMappingTypeDef",
    {
        "ApiMappingId": str,
        "ApiMappingKey": str,
    },
    total=False,
)


class ApiMappingTypeDef(_RequiredApiMappingTypeDef, _OptionalApiMappingTypeDef):
    pass


_RequiredApiTypeDef = TypedDict(
    "_RequiredApiTypeDef",
    {
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
    },
)
_OptionalApiTypeDef = TypedDict(
    "_OptionalApiTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
    },
    total=False,
)


class ApiTypeDef(_RequiredApiTypeDef, _OptionalApiTypeDef):
    pass


_RequiredAuthorizerTypeDef = TypedDict(
    "_RequiredAuthorizerTypeDef",
    {
        "Name": str,
    },
)
_OptionalAuthorizerTypeDef = TypedDict(
    "_OptionalAuthorizerTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
    },
    total=False,
)


class AuthorizerTypeDef(_RequiredAuthorizerTypeDef, _OptionalAuthorizerTypeDef):
    pass


CorsTypeDef = TypedDict(
    "CorsTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

_RequiredCreateApiMappingRequestTypeDef = TypedDict(
    "_RequiredCreateApiMappingRequestTypeDef",
    {
        "ApiId": str,
        "DomainName": str,
        "Stage": str,
    },
)
_OptionalCreateApiMappingRequestTypeDef = TypedDict(
    "_OptionalCreateApiMappingRequestTypeDef",
    {
        "ApiMappingKey": str,
    },
    total=False,
)


class CreateApiMappingRequestTypeDef(
    _RequiredCreateApiMappingRequestTypeDef, _OptionalCreateApiMappingRequestTypeDef
):
    pass


CreateApiMappingResponseResponseTypeDef = TypedDict(
    "CreateApiMappingResponseResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApiRequestTypeDef = TypedDict(
    "_RequiredCreateApiRequestTypeDef",
    {
        "Name": str,
        "ProtocolType": ProtocolTypeType,
    },
)
_OptionalCreateApiRequestTypeDef = TypedDict(
    "_OptionalCreateApiRequestTypeDef",
    {
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CredentialsArn": str,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "RouteKey": str,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Target": str,
        "Version": str,
    },
    total=False,
)


class CreateApiRequestTypeDef(_RequiredCreateApiRequestTypeDef, _OptionalCreateApiRequestTypeDef):
    pass


CreateApiResponseResponseTypeDef = TypedDict(
    "CreateApiResponseResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAuthorizerRequestTypeDef = TypedDict(
    "_RequiredCreateAuthorizerRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerType": AuthorizerTypeType,
        "IdentitySource": List[str],
        "Name": str,
    },
)
_OptionalCreateAuthorizerRequestTypeDef = TypedDict(
    "_OptionalCreateAuthorizerRequestTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
    },
    total=False,
)


class CreateAuthorizerRequestTypeDef(
    _RequiredCreateAuthorizerRequestTypeDef, _OptionalCreateAuthorizerRequestTypeDef
):
    pass


CreateAuthorizerResponseResponseTypeDef = TypedDict(
    "CreateAuthorizerResponseResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalCreateDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestTypeDef",
    {
        "Description": str,
        "StageName": str,
    },
    total=False,
)


class CreateDeploymentRequestTypeDef(
    _RequiredCreateDeploymentRequestTypeDef, _OptionalCreateDeploymentRequestTypeDef
):
    pass


CreateDeploymentResponseResponseTypeDef = TypedDict(
    "CreateDeploymentResponseResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainNameRequestTypeDef = TypedDict(
    "_RequiredCreateDomainNameRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateDomainNameRequestTypeDef = TypedDict(
    "_OptionalCreateDomainNameRequestTypeDef",
    {
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationInputTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDomainNameRequestTypeDef(
    _RequiredCreateDomainNameRequestTypeDef, _OptionalCreateDomainNameRequestTypeDef
):
    pass


CreateDomainNameResponseResponseTypeDef = TypedDict(
    "CreateDomainNameResponseResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationType": IntegrationTypeType,
    },
)
_OptionalCreateIntegrationRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationRequestTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationMethod": str,
        "IntegrationSubtype": str,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigInputTypeDef",
    },
    total=False,
)


class CreateIntegrationRequestTypeDef(
    _RequiredCreateIntegrationRequestTypeDef, _OptionalCreateIntegrationRequestTypeDef
):
    pass


_RequiredCreateIntegrationResponseRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationResponseRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseKey": str,
    },
)
_OptionalCreateIntegrationResponseRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationResponseRequestTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class CreateIntegrationResponseRequestTypeDef(
    _RequiredCreateIntegrationResponseRequestTypeDef,
    _OptionalCreateIntegrationResponseRequestTypeDef,
):
    pass


CreateIntegrationResponseResponseResponseTypeDef = TypedDict(
    "CreateIntegrationResponseResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIntegrationResultResponseTypeDef = TypedDict(
    "CreateIntegrationResultResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestTypeDef",
    {
        "ApiId": str,
        "Name": str,
        "Schema": str,
    },
)
_OptionalCreateModelRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestTypeDef",
    {
        "ContentType": str,
        "Description": str,
    },
    total=False,
)


class CreateModelRequestTypeDef(
    _RequiredCreateModelRequestTypeDef, _OptionalCreateModelRequestTypeDef
):
    pass


CreateModelResponseResponseTypeDef = TypedDict(
    "CreateModelResponseResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteRequestTypeDef = TypedDict(
    "_RequiredCreateRouteRequestTypeDef",
    {
        "ApiId": str,
        "RouteKey": str,
    },
)
_OptionalCreateRouteRequestTypeDef = TypedDict(
    "_OptionalCreateRouteRequestTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class CreateRouteRequestTypeDef(
    _RequiredCreateRouteRequestTypeDef, _OptionalCreateRouteRequestTypeDef
):
    pass


_RequiredCreateRouteResponseRequestTypeDef = TypedDict(
    "_RequiredCreateRouteResponseRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseKey": str,
    },
)
_OptionalCreateRouteResponseRequestTypeDef = TypedDict(
    "_OptionalCreateRouteResponseRequestTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
    },
    total=False,
)


class CreateRouteResponseRequestTypeDef(
    _RequiredCreateRouteResponseRequestTypeDef, _OptionalCreateRouteResponseRequestTypeDef
):
    pass


CreateRouteResponseResponseResponseTypeDef = TypedDict(
    "CreateRouteResponseResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteResultResponseTypeDef = TypedDict(
    "CreateRouteResultResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStageRequestTypeDef = TypedDict(
    "_RequiredCreateStageRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
_OptionalCreateStageRequestTypeDef = TypedDict(
    "_OptionalCreateStageRequestTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateStageRequestTypeDef(
    _RequiredCreateStageRequestTypeDef, _OptionalCreateStageRequestTypeDef
):
    pass


CreateStageResponseResponseTypeDef = TypedDict(
    "CreateStageResponseResponseTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcLinkRequestTypeDef = TypedDict(
    "_RequiredCreateVpcLinkRequestTypeDef",
    {
        "Name": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateVpcLinkRequestTypeDef = TypedDict(
    "_OptionalCreateVpcLinkRequestTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateVpcLinkRequestTypeDef(
    _RequiredCreateVpcLinkRequestTypeDef, _OptionalCreateVpcLinkRequestTypeDef
):
    pass


CreateVpcLinkResponseResponseTypeDef = TypedDict(
    "CreateVpcLinkResponseResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessLogSettingsRequestTypeDef = TypedDict(
    "DeleteAccessLogSettingsRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)

DeleteApiMappingRequestTypeDef = TypedDict(
    "DeleteApiMappingRequestTypeDef",
    {
        "ApiMappingId": str,
        "DomainName": str,
    },
)

DeleteApiRequestTypeDef = TypedDict(
    "DeleteApiRequestTypeDef",
    {
        "ApiId": str,
    },
)

DeleteAuthorizerRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)

DeleteCorsConfigurationRequestTypeDef = TypedDict(
    "DeleteCorsConfigurationRequestTypeDef",
    {
        "ApiId": str,
    },
)

DeleteDeploymentRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)

DeleteDomainNameRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteIntegrationRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)

DeleteIntegrationResponseRequestTypeDef = TypedDict(
    "DeleteIntegrationResponseRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)

DeleteModelRequestTypeDef = TypedDict(
    "DeleteModelRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)

DeleteRouteRequestParameterRequestTypeDef = TypedDict(
    "DeleteRouteRequestParameterRequestTypeDef",
    {
        "ApiId": str,
        "RequestParameterKey": str,
        "RouteId": str,
    },
)

DeleteRouteRequestTypeDef = TypedDict(
    "DeleteRouteRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)

DeleteRouteResponseRequestTypeDef = TypedDict(
    "DeleteRouteResponseRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)

DeleteRouteSettingsRequestTypeDef = TypedDict(
    "DeleteRouteSettingsRequestTypeDef",
    {
        "ApiId": str,
        "RouteKey": str,
        "StageName": str,
    },
)

DeleteStageRequestTypeDef = TypedDict(
    "DeleteStageRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)

DeleteVpcLinkRequestTypeDef = TypedDict(
    "DeleteVpcLinkRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
    },
    total=False,
)

DomainNameConfigurationTypeDef = TypedDict(
    "DomainNameConfigurationTypeDef",
    {
        "ApiGatewayDomainName": str,
        "CertificateArn": str,
        "CertificateName": str,
        "CertificateUploadDate": Union[datetime, str],
        "DomainNameStatus": DomainNameStatusType,
        "DomainNameStatusMessage": str,
        "EndpointType": EndpointTypeType,
        "HostedZoneId": str,
        "SecurityPolicy": SecurityPolicyType,
    },
    total=False,
)

_RequiredDomainNameTypeDef = TypedDict(
    "_RequiredDomainNameTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainNameTypeDef = TypedDict(
    "_OptionalDomainNameTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class DomainNameTypeDef(_RequiredDomainNameTypeDef, _OptionalDomainNameTypeDef):
    pass


_RequiredExportApiRequestTypeDef = TypedDict(
    "_RequiredExportApiRequestTypeDef",
    {
        "ApiId": str,
        "OutputType": JSONYAMLType,
        "Specification": Literal["OAS30"],
    },
)
_OptionalExportApiRequestTypeDef = TypedDict(
    "_OptionalExportApiRequestTypeDef",
    {
        "ExportVersion": str,
        "IncludeExtensions": bool,
        "StageName": str,
    },
    total=False,
)


class ExportApiRequestTypeDef(_RequiredExportApiRequestTypeDef, _OptionalExportApiRequestTypeDef):
    pass


ExportApiResponseResponseTypeDef = TypedDict(
    "ExportApiResponseResponseTypeDef",
    {
        "body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiMappingRequestTypeDef = TypedDict(
    "GetApiMappingRequestTypeDef",
    {
        "ApiMappingId": str,
        "DomainName": str,
    },
)

GetApiMappingResponseResponseTypeDef = TypedDict(
    "GetApiMappingResponseResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetApiMappingsRequestTypeDef = TypedDict(
    "_RequiredGetApiMappingsRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalGetApiMappingsRequestTypeDef = TypedDict(
    "_OptionalGetApiMappingsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetApiMappingsRequestTypeDef(
    _RequiredGetApiMappingsRequestTypeDef, _OptionalGetApiMappingsRequestTypeDef
):
    pass


GetApiMappingsResponseResponseTypeDef = TypedDict(
    "GetApiMappingsResponseResponseTypeDef",
    {
        "Items": List["ApiMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApiRequestTypeDef = TypedDict(
    "GetApiRequestTypeDef",
    {
        "ApiId": str,
    },
)

GetApiResponseResponseTypeDef = TypedDict(
    "GetApiResponseResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApisRequestTypeDef = TypedDict(
    "GetApisRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

GetApisResponseResponseTypeDef = TypedDict(
    "GetApisResponseResponseTypeDef",
    {
        "Items": List["ApiTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAuthorizerRequestTypeDef = TypedDict(
    "GetAuthorizerRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)

GetAuthorizerResponseResponseTypeDef = TypedDict(
    "GetAuthorizerResponseResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAuthorizersRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizersRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetAuthorizersRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizersRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetAuthorizersRequestTypeDef(
    _RequiredGetAuthorizersRequestTypeDef, _OptionalGetAuthorizersRequestTypeDef
):
    pass


GetAuthorizersResponseResponseTypeDef = TypedDict(
    "GetAuthorizersResponseResponseTypeDef",
    {
        "Items": List["AuthorizerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentRequestTypeDef = TypedDict(
    "GetDeploymentRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)

GetDeploymentResponseResponseTypeDef = TypedDict(
    "GetDeploymentResponseResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeploymentsRequestTypeDef = TypedDict(
    "_RequiredGetDeploymentsRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetDeploymentsRequestTypeDef = TypedDict(
    "_OptionalGetDeploymentsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetDeploymentsRequestTypeDef(
    _RequiredGetDeploymentsRequestTypeDef, _OptionalGetDeploymentsRequestTypeDef
):
    pass


GetDeploymentsResponseResponseTypeDef = TypedDict(
    "GetDeploymentsResponseResponseTypeDef",
    {
        "Items": List["DeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainNameRequestTypeDef = TypedDict(
    "GetDomainNameRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetDomainNameResponseResponseTypeDef = TypedDict(
    "GetDomainNameResponseResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainNamesRequestTypeDef = TypedDict(
    "GetDomainNamesRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

GetDomainNamesResponseResponseTypeDef = TypedDict(
    "GetDomainNamesResponseResponseTypeDef",
    {
        "Items": List["DomainNameTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationRequestTypeDef = TypedDict(
    "GetIntegrationRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)

GetIntegrationResponseRequestTypeDef = TypedDict(
    "GetIntegrationResponseRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)

GetIntegrationResponseResponseResponseTypeDef = TypedDict(
    "GetIntegrationResponseResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntegrationResponsesRequestTypeDef = TypedDict(
    "_RequiredGetIntegrationResponsesRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)
_OptionalGetIntegrationResponsesRequestTypeDef = TypedDict(
    "_OptionalGetIntegrationResponsesRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetIntegrationResponsesRequestTypeDef(
    _RequiredGetIntegrationResponsesRequestTypeDef, _OptionalGetIntegrationResponsesRequestTypeDef
):
    pass


GetIntegrationResponsesResponseResponseTypeDef = TypedDict(
    "GetIntegrationResponsesResponseResponseTypeDef",
    {
        "Items": List["IntegrationResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntegrationResultResponseTypeDef = TypedDict(
    "GetIntegrationResultResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntegrationsRequestTypeDef = TypedDict(
    "_RequiredGetIntegrationsRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetIntegrationsRequestTypeDef = TypedDict(
    "_OptionalGetIntegrationsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetIntegrationsRequestTypeDef(
    _RequiredGetIntegrationsRequestTypeDef, _OptionalGetIntegrationsRequestTypeDef
):
    pass


GetIntegrationsResponseResponseTypeDef = TypedDict(
    "GetIntegrationsResponseResponseTypeDef",
    {
        "Items": List["IntegrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelRequestTypeDef = TypedDict(
    "GetModelRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)

GetModelResponseResponseTypeDef = TypedDict(
    "GetModelResponseResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelTemplateRequestTypeDef = TypedDict(
    "GetModelTemplateRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)

GetModelTemplateResponseResponseTypeDef = TypedDict(
    "GetModelTemplateResponseResponseTypeDef",
    {
        "Value": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetModelsRequestTypeDef = TypedDict(
    "_RequiredGetModelsRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetModelsRequestTypeDef = TypedDict(
    "_OptionalGetModelsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetModelsRequestTypeDef(_RequiredGetModelsRequestTypeDef, _OptionalGetModelsRequestTypeDef):
    pass


GetModelsResponseResponseTypeDef = TypedDict(
    "GetModelsResponseResponseTypeDef",
    {
        "Items": List["ModelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteRequestTypeDef = TypedDict(
    "GetRouteRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)

GetRouteResponseRequestTypeDef = TypedDict(
    "GetRouteResponseRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)

GetRouteResponseResponseResponseTypeDef = TypedDict(
    "GetRouteResponseResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRouteResponsesRequestTypeDef = TypedDict(
    "_RequiredGetRouteResponsesRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)
_OptionalGetRouteResponsesRequestTypeDef = TypedDict(
    "_OptionalGetRouteResponsesRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetRouteResponsesRequestTypeDef(
    _RequiredGetRouteResponsesRequestTypeDef, _OptionalGetRouteResponsesRequestTypeDef
):
    pass


GetRouteResponsesResponseResponseTypeDef = TypedDict(
    "GetRouteResponsesResponseResponseTypeDef",
    {
        "Items": List["RouteResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteResultResponseTypeDef = TypedDict(
    "GetRouteResultResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRoutesRequestTypeDef = TypedDict(
    "_RequiredGetRoutesRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetRoutesRequestTypeDef = TypedDict(
    "_OptionalGetRoutesRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetRoutesRequestTypeDef(_RequiredGetRoutesRequestTypeDef, _OptionalGetRoutesRequestTypeDef):
    pass


GetRoutesResponseResponseTypeDef = TypedDict(
    "GetRoutesResponseResponseTypeDef",
    {
        "Items": List["RouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageRequestTypeDef = TypedDict(
    "GetStageRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)

GetStageResponseResponseTypeDef = TypedDict(
    "GetStageResponseResponseTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStagesRequestTypeDef = TypedDict(
    "_RequiredGetStagesRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalGetStagesRequestTypeDef = TypedDict(
    "_OptionalGetStagesRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class GetStagesRequestTypeDef(_RequiredGetStagesRequestTypeDef, _OptionalGetStagesRequestTypeDef):
    pass


GetStagesResponseResponseTypeDef = TypedDict(
    "GetStagesResponseResponseTypeDef",
    {
        "Items": List["StageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsRequestTypeDef = TypedDict(
    "GetTagsRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetTagsResponseResponseTypeDef = TypedDict(
    "GetTagsResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpcLinkRequestTypeDef = TypedDict(
    "GetVpcLinkRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)

GetVpcLinkResponseResponseTypeDef = TypedDict(
    "GetVpcLinkResponseResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpcLinksRequestTypeDef = TypedDict(
    "GetVpcLinksRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

GetVpcLinksResponseResponseTypeDef = TypedDict(
    "GetVpcLinksResponseResponseTypeDef",
    {
        "Items": List["VpcLinkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportApiRequestTypeDef = TypedDict(
    "_RequiredImportApiRequestTypeDef",
    {
        "Body": str,
    },
)
_OptionalImportApiRequestTypeDef = TypedDict(
    "_OptionalImportApiRequestTypeDef",
    {
        "Basepath": str,
        "FailOnWarnings": bool,
    },
    total=False,
)


class ImportApiRequestTypeDef(_RequiredImportApiRequestTypeDef, _OptionalImportApiRequestTypeDef):
    pass


ImportApiResponseResponseTypeDef = TypedDict(
    "ImportApiResponseResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIntegrationResponseTypeDef = TypedDict(
    "_RequiredIntegrationResponseTypeDef",
    {
        "IntegrationResponseKey": str,
    },
)
_OptionalIntegrationResponseTypeDef = TypedDict(
    "_OptionalIntegrationResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class IntegrationResponseTypeDef(
    _RequiredIntegrationResponseTypeDef, _OptionalIntegrationResponseTypeDef
):
    pass


IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)

JWTConfigurationTypeDef = TypedDict(
    "JWTConfigurationTypeDef",
    {
        "Audience": List[str],
        "Issuer": str,
    },
    total=False,
)

_RequiredModelTypeDef = TypedDict(
    "_RequiredModelTypeDef",
    {
        "Name": str,
    },
)
_OptionalModelTypeDef = TypedDict(
    "_OptionalModelTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Schema": str,
    },
    total=False,
)


class ModelTypeDef(_RequiredModelTypeDef, _OptionalModelTypeDef):
    pass


MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {
        "TruststoreUri": str,
        "TruststoreVersion": str,
    },
    total=False,
)

MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {
        "TruststoreUri": str,
        "TruststoreVersion": str,
        "TruststoreWarnings": List[str],
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
        "Required": bool,
    },
    total=False,
)

_RequiredReimportApiRequestTypeDef = TypedDict(
    "_RequiredReimportApiRequestTypeDef",
    {
        "ApiId": str,
        "Body": str,
    },
)
_OptionalReimportApiRequestTypeDef = TypedDict(
    "_OptionalReimportApiRequestTypeDef",
    {
        "Basepath": str,
        "FailOnWarnings": bool,
    },
    total=False,
)


class ReimportApiRequestTypeDef(
    _RequiredReimportApiRequestTypeDef, _OptionalReimportApiRequestTypeDef
):
    pass


ReimportApiResponseResponseTypeDef = TypedDict(
    "ReimportApiResponseResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetAuthorizersCacheRequestTypeDef = TypedDict(
    "ResetAuthorizersCacheRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
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

_RequiredRouteResponseTypeDef = TypedDict(
    "_RequiredRouteResponseTypeDef",
    {
        "RouteResponseKey": str,
    },
)
_OptionalRouteResponseTypeDef = TypedDict(
    "_OptionalRouteResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
    },
    total=False,
)


class RouteResponseTypeDef(_RequiredRouteResponseTypeDef, _OptionalRouteResponseTypeDef):
    pass


RouteSettingsTypeDef = TypedDict(
    "RouteSettingsTypeDef",
    {
        "DataTraceEnabled": bool,
        "DetailedMetricsEnabled": bool,
        "LoggingLevel": LoggingLevelType,
        "ThrottlingBurstLimit": int,
        "ThrottlingRateLimit": float,
    },
    total=False,
)

_RequiredRouteTypeDef = TypedDict(
    "_RequiredRouteTypeDef",
    {
        "RouteKey": str,
    },
)
_OptionalRouteTypeDef = TypedDict(
    "_OptionalRouteTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class RouteTypeDef(_RequiredRouteTypeDef, _OptionalRouteTypeDef):
    pass


_RequiredStageTypeDef = TypedDict(
    "_RequiredStageTypeDef",
    {
        "StageName": str,
    },
)
_OptionalStageTypeDef = TypedDict(
    "_OptionalStageTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class StageTypeDef(_RequiredStageTypeDef, _OptionalStageTypeDef):
    pass


_RequiredTagResourceRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalTagResourceRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class TagResourceRequestTypeDef(
    _RequiredTagResourceRequestTypeDef, _OptionalTagResourceRequestTypeDef
):
    pass


TlsConfigInputTypeDef = TypedDict(
    "TlsConfigInputTypeDef",
    {
        "ServerNameToVerify": str,
    },
    total=False,
)

TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "ServerNameToVerify": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApiMappingRequestTypeDef = TypedDict(
    "_RequiredUpdateApiMappingRequestTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "DomainName": str,
    },
)
_OptionalUpdateApiMappingRequestTypeDef = TypedDict(
    "_OptionalUpdateApiMappingRequestTypeDef",
    {
        "ApiMappingKey": str,
        "Stage": str,
    },
    total=False,
)


class UpdateApiMappingRequestTypeDef(
    _RequiredUpdateApiMappingRequestTypeDef, _OptionalUpdateApiMappingRequestTypeDef
):
    pass


UpdateApiMappingResponseResponseTypeDef = TypedDict(
    "UpdateApiMappingResponseResponseTypeDef",
    {
        "ApiId": str,
        "ApiMappingId": str,
        "ApiMappingKey": str,
        "Stage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateApiRequestTypeDef = TypedDict(
    "_RequiredUpdateApiRequestTypeDef",
    {
        "ApiId": str,
    },
)
_OptionalUpdateApiRequestTypeDef = TypedDict(
    "_OptionalUpdateApiRequestTypeDef",
    {
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CredentialsArn": str,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "Name": str,
        "RouteKey": str,
        "RouteSelectionExpression": str,
        "Target": str,
        "Version": str,
    },
    total=False,
)


class UpdateApiRequestTypeDef(_RequiredUpdateApiRequestTypeDef, _OptionalUpdateApiRequestTypeDef):
    pass


UpdateApiResponseResponseTypeDef = TypedDict(
    "UpdateApiResponseResponseTypeDef",
    {
        "ApiEndpoint": str,
        "ApiGatewayManaged": bool,
        "ApiId": str,
        "ApiKeySelectionExpression": str,
        "CorsConfiguration": "CorsTypeDef",
        "CreatedDate": datetime,
        "Description": str,
        "DisableSchemaValidation": bool,
        "DisableExecuteApiEndpoint": bool,
        "ImportInfo": List[str],
        "Name": str,
        "ProtocolType": ProtocolTypeType,
        "RouteSelectionExpression": str,
        "Tags": Dict[str, str],
        "Version": str,
        "Warnings": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAuthorizerRequestTypeDef = TypedDict(
    "_RequiredUpdateAuthorizerRequestTypeDef",
    {
        "ApiId": str,
        "AuthorizerId": str,
    },
)
_OptionalUpdateAuthorizerRequestTypeDef = TypedDict(
    "_OptionalUpdateAuthorizerRequestTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
    },
    total=False,
)


class UpdateAuthorizerRequestTypeDef(
    _RequiredUpdateAuthorizerRequestTypeDef, _OptionalUpdateAuthorizerRequestTypeDef
):
    pass


UpdateAuthorizerResponseResponseTypeDef = TypedDict(
    "UpdateAuthorizerResponseResponseTypeDef",
    {
        "AuthorizerCredentialsArn": str,
        "AuthorizerId": str,
        "AuthorizerPayloadFormatVersion": str,
        "AuthorizerResultTtlInSeconds": int,
        "AuthorizerType": AuthorizerTypeType,
        "AuthorizerUri": str,
        "EnableSimpleResponses": bool,
        "IdentitySource": List[str],
        "IdentityValidationExpression": str,
        "JwtConfiguration": "JWTConfigurationTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDeploymentRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentRequestTypeDef",
    {
        "ApiId": str,
        "DeploymentId": str,
    },
)
_OptionalUpdateDeploymentRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateDeploymentRequestTypeDef(
    _RequiredUpdateDeploymentRequestTypeDef, _OptionalUpdateDeploymentRequestTypeDef
):
    pass


UpdateDeploymentResponseResponseTypeDef = TypedDict(
    "UpdateDeploymentResponseResponseTypeDef",
    {
        "AutoDeployed": bool,
        "CreatedDate": datetime,
        "DeploymentId": str,
        "DeploymentStatus": DeploymentStatusType,
        "DeploymentStatusMessage": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainNameRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainNameRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateDomainNameRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainNameRequestTypeDef",
    {
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationInputTypeDef",
    },
    total=False,
)


class UpdateDomainNameRequestTypeDef(
    _RequiredUpdateDomainNameRequestTypeDef, _OptionalUpdateDomainNameRequestTypeDef
):
    pass


UpdateDomainNameResponseResponseTypeDef = TypedDict(
    "UpdateDomainNameResponseResponseTypeDef",
    {
        "ApiMappingSelectionExpression": str,
        "DomainName": str,
        "DomainNameConfigurations": List["DomainNameConfigurationTypeDef"],
        "MutualTlsAuthentication": "MutualTlsAuthenticationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIntegrationRequestTypeDef = TypedDict(
    "_RequiredUpdateIntegrationRequestTypeDef",
    {
        "ApiId": str,
        "IntegrationId": str,
    },
)
_OptionalUpdateIntegrationRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationRequestTypeDef",
    {
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationMethod": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigInputTypeDef",
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
        "ApiId": str,
        "IntegrationId": str,
        "IntegrationResponseId": str,
    },
)
_OptionalUpdateIntegrationResponseRequestTypeDef = TypedDict(
    "_OptionalUpdateIntegrationResponseRequestTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
    },
    total=False,
)


class UpdateIntegrationResponseRequestTypeDef(
    _RequiredUpdateIntegrationResponseRequestTypeDef,
    _OptionalUpdateIntegrationResponseRequestTypeDef,
):
    pass


UpdateIntegrationResponseResponseResponseTypeDef = TypedDict(
    "UpdateIntegrationResponseResponseResponseTypeDef",
    {
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "IntegrationResponseId": str,
        "IntegrationResponseKey": str,
        "ResponseParameters": Dict[str, str],
        "ResponseTemplates": Dict[str, str],
        "TemplateSelectionExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIntegrationResultResponseTypeDef = TypedDict(
    "UpdateIntegrationResultResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ConnectionId": str,
        "ConnectionType": ConnectionTypeType,
        "ContentHandlingStrategy": ContentHandlingStrategyType,
        "CredentialsArn": str,
        "Description": str,
        "IntegrationId": str,
        "IntegrationMethod": str,
        "IntegrationResponseSelectionExpression": str,
        "IntegrationSubtype": str,
        "IntegrationType": IntegrationTypeType,
        "IntegrationUri": str,
        "PassthroughBehavior": PassthroughBehaviorType,
        "PayloadFormatVersion": str,
        "RequestParameters": Dict[str, str],
        "RequestTemplates": Dict[str, str],
        "ResponseParameters": Dict[str, Dict[str, str]],
        "TemplateSelectionExpression": str,
        "TimeoutInMillis": int,
        "TlsConfig": "TlsConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestTypeDef",
    {
        "ApiId": str,
        "ModelId": str,
    },
)
_OptionalUpdateModelRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "Name": str,
        "Schema": str,
    },
    total=False,
)


class UpdateModelRequestTypeDef(
    _RequiredUpdateModelRequestTypeDef, _OptionalUpdateModelRequestTypeDef
):
    pass


UpdateModelResponseResponseTypeDef = TypedDict(
    "UpdateModelResponseResponseTypeDef",
    {
        "ContentType": str,
        "Description": str,
        "ModelId": str,
        "Name": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRouteRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
    },
)
_OptionalUpdateRouteRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteRequestTypeDef",
    {
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
    },
    total=False,
)


class UpdateRouteRequestTypeDef(
    _RequiredUpdateRouteRequestTypeDef, _OptionalUpdateRouteRequestTypeDef
):
    pass


_RequiredUpdateRouteResponseRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteResponseRequestTypeDef",
    {
        "ApiId": str,
        "RouteId": str,
        "RouteResponseId": str,
    },
)
_OptionalUpdateRouteResponseRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteResponseRequestTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseKey": str,
    },
    total=False,
)


class UpdateRouteResponseRequestTypeDef(
    _RequiredUpdateRouteResponseRequestTypeDef, _OptionalUpdateRouteResponseRequestTypeDef
):
    pass


UpdateRouteResponseResponseResponseTypeDef = TypedDict(
    "UpdateRouteResponseResponseResponseTypeDef",
    {
        "ModelSelectionExpression": str,
        "ResponseModels": Dict[str, str],
        "ResponseParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteResponseId": str,
        "RouteResponseKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRouteResultResponseTypeDef = TypedDict(
    "UpdateRouteResultResponseTypeDef",
    {
        "ApiGatewayManaged": bool,
        "ApiKeyRequired": bool,
        "AuthorizationScopes": List[str],
        "AuthorizationType": AuthorizationTypeType,
        "AuthorizerId": str,
        "ModelSelectionExpression": str,
        "OperationName": str,
        "RequestModels": Dict[str, str],
        "RequestParameters": Dict[str, "ParameterConstraintsTypeDef"],
        "RouteId": str,
        "RouteKey": str,
        "RouteResponseSelectionExpression": str,
        "Target": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStageRequestTypeDef = TypedDict(
    "_RequiredUpdateStageRequestTypeDef",
    {
        "ApiId": str,
        "StageName": str,
    },
)
_OptionalUpdateStageRequestTypeDef = TypedDict(
    "_OptionalUpdateStageRequestTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageVariables": Dict[str, str],
    },
    total=False,
)


class UpdateStageRequestTypeDef(
    _RequiredUpdateStageRequestTypeDef, _OptionalUpdateStageRequestTypeDef
):
    pass


UpdateStageResponseResponseTypeDef = TypedDict(
    "UpdateStageResponseResponseTypeDef",
    {
        "AccessLogSettings": "AccessLogSettingsTypeDef",
        "ApiGatewayManaged": bool,
        "AutoDeploy": bool,
        "ClientCertificateId": str,
        "CreatedDate": datetime,
        "DefaultRouteSettings": "RouteSettingsTypeDef",
        "DeploymentId": str,
        "Description": str,
        "LastDeploymentStatusMessage": str,
        "LastUpdatedDate": datetime,
        "RouteSettings": Dict[str, "RouteSettingsTypeDef"],
        "StageName": str,
        "StageVariables": Dict[str, str],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVpcLinkRequestTypeDef = TypedDict(
    "_RequiredUpdateVpcLinkRequestTypeDef",
    {
        "VpcLinkId": str,
    },
)
_OptionalUpdateVpcLinkRequestTypeDef = TypedDict(
    "_OptionalUpdateVpcLinkRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateVpcLinkRequestTypeDef(
    _RequiredUpdateVpcLinkRequestTypeDef, _OptionalUpdateVpcLinkRequestTypeDef
):
    pass


UpdateVpcLinkResponseResponseTypeDef = TypedDict(
    "UpdateVpcLinkResponseResponseTypeDef",
    {
        "CreatedDate": datetime,
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "VpcLinkId": str,
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVpcLinkTypeDef = TypedDict(
    "_RequiredVpcLinkTypeDef",
    {
        "Name": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "VpcLinkId": str,
    },
)
_OptionalVpcLinkTypeDef = TypedDict(
    "_OptionalVpcLinkTypeDef",
    {
        "CreatedDate": datetime,
        "Tags": Dict[str, str],
        "VpcLinkStatus": VpcLinkStatusType,
        "VpcLinkStatusMessage": str,
        "VpcLinkVersion": Literal["V2"],
    },
    total=False,
)


class VpcLinkTypeDef(_RequiredVpcLinkTypeDef, _OptionalVpcLinkTypeDef):
    pass
