"""
Type annotations for appsync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appsync.type_defs import AdditionalAuthenticationProviderTypeDef

    data: AdditionalAuthenticationProviderTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApiCacheStatusType,
    ApiCacheTypeType,
    ApiCachingBehaviorType,
    AuthenticationTypeType,
    ConflictDetectionTypeType,
    ConflictHandlerTypeType,
    DataSourceTypeType,
    DefaultActionType,
    FieldLogLevelType,
    OutputTypeType,
    ResolverKindType,
    SchemaStatusType,
    TypeDefinitionFormatType,
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
    "AdditionalAuthenticationProviderTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "CreateApiCacheRequestTypeDef",
    "CreateApiCacheResponseResponseTypeDef",
    "CreateApiKeyRequestTypeDef",
    "CreateApiKeyResponseResponseTypeDef",
    "CreateDataSourceRequestTypeDef",
    "CreateDataSourceResponseResponseTypeDef",
    "CreateFunctionRequestTypeDef",
    "CreateFunctionResponseResponseTypeDef",
    "CreateGraphqlApiRequestTypeDef",
    "CreateGraphqlApiResponseResponseTypeDef",
    "CreateResolverRequestTypeDef",
    "CreateResolverResponseResponseTypeDef",
    "CreateTypeRequestTypeDef",
    "CreateTypeResponseResponseTypeDef",
    "DataSourceTypeDef",
    "DeleteApiCacheRequestTypeDef",
    "DeleteApiKeyRequestTypeDef",
    "DeleteDataSourceRequestTypeDef",
    "DeleteFunctionRequestTypeDef",
    "DeleteGraphqlApiRequestTypeDef",
    "DeleteResolverRequestTypeDef",
    "DeleteTypeRequestTypeDef",
    "DeltaSyncConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "FlushApiCacheRequestTypeDef",
    "FunctionConfigurationTypeDef",
    "GetApiCacheRequestTypeDef",
    "GetApiCacheResponseResponseTypeDef",
    "GetDataSourceRequestTypeDef",
    "GetDataSourceResponseResponseTypeDef",
    "GetFunctionRequestTypeDef",
    "GetFunctionResponseResponseTypeDef",
    "GetGraphqlApiRequestTypeDef",
    "GetGraphqlApiResponseResponseTypeDef",
    "GetIntrospectionSchemaRequestTypeDef",
    "GetIntrospectionSchemaResponseResponseTypeDef",
    "GetResolverRequestTypeDef",
    "GetResolverResponseResponseTypeDef",
    "GetSchemaCreationStatusRequestTypeDef",
    "GetSchemaCreationStatusResponseResponseTypeDef",
    "GetTypeRequestTypeDef",
    "GetTypeResponseResponseTypeDef",
    "GraphqlApiTypeDef",
    "HttpDataSourceConfigTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "ListApiKeysRequestTypeDef",
    "ListApiKeysResponseResponseTypeDef",
    "ListDataSourcesRequestTypeDef",
    "ListDataSourcesResponseResponseTypeDef",
    "ListFunctionsRequestTypeDef",
    "ListFunctionsResponseResponseTypeDef",
    "ListGraphqlApisRequestTypeDef",
    "ListGraphqlApisResponseResponseTypeDef",
    "ListResolversByFunctionRequestTypeDef",
    "ListResolversByFunctionResponseResponseTypeDef",
    "ListResolversRequestTypeDef",
    "ListResolversResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTypesRequestTypeDef",
    "ListTypesResponseResponseTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "ResponseMetadataTypeDef",
    "StartSchemaCreationRequestTypeDef",
    "StartSchemaCreationResponseResponseTypeDef",
    "SyncConfigTypeDef",
    "TagResourceRequestTypeDef",
    "TypeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApiCacheRequestTypeDef",
    "UpdateApiCacheResponseResponseTypeDef",
    "UpdateApiKeyRequestTypeDef",
    "UpdateApiKeyResponseResponseTypeDef",
    "UpdateDataSourceRequestTypeDef",
    "UpdateDataSourceResponseResponseTypeDef",
    "UpdateFunctionRequestTypeDef",
    "UpdateFunctionResponseResponseTypeDef",
    "UpdateGraphqlApiRequestTypeDef",
    "UpdateGraphqlApiResponseResponseTypeDef",
    "UpdateResolverRequestTypeDef",
    "UpdateResolverResponseResponseTypeDef",
    "UpdateTypeRequestTypeDef",
    "UpdateTypeResponseResponseTypeDef",
    "UserPoolConfigTypeDef",
)

AdditionalAuthenticationProviderTypeDef = TypedDict(
    "AdditionalAuthenticationProviderTypeDef",
    {
        "authenticationType": AuthenticationTypeType,
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "userPoolConfig": "CognitoUserPoolConfigTypeDef",
    },
    total=False,
)

ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": ApiCacheTypeType,
        "status": ApiCacheStatusType,
    },
    total=False,
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": str,
        "description": str,
        "expires": int,
        "deletes": int,
    },
    total=False,
)

_RequiredAuthorizationConfigTypeDef = TypedDict(
    "_RequiredAuthorizationConfigTypeDef",
    {
        "authorizationType": Literal["AWS_IAM"],
    },
)
_OptionalAuthorizationConfigTypeDef = TypedDict(
    "_OptionalAuthorizationConfigTypeDef",
    {
        "awsIamConfig": "AwsIamConfigTypeDef",
    },
    total=False,
)


class AuthorizationConfigTypeDef(
    _RequiredAuthorizationConfigTypeDef, _OptionalAuthorizationConfigTypeDef
):
    pass


AwsIamConfigTypeDef = TypedDict(
    "AwsIamConfigTypeDef",
    {
        "signingRegion": str,
        "signingServiceName": str,
    },
    total=False,
)

CachingConfigTypeDef = TypedDict(
    "CachingConfigTypeDef",
    {
        "ttl": int,
        "cachingKeys": List[str],
    },
    total=False,
)

_RequiredCognitoUserPoolConfigTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
    },
)
_OptionalCognitoUserPoolConfigTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)


class CognitoUserPoolConfigTypeDef(
    _RequiredCognitoUserPoolConfigTypeDef, _OptionalCognitoUserPoolConfigTypeDef
):
    pass


_RequiredCreateApiCacheRequestTypeDef = TypedDict(
    "_RequiredCreateApiCacheRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)
_OptionalCreateApiCacheRequestTypeDef = TypedDict(
    "_OptionalCreateApiCacheRequestTypeDef",
    {
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
    },
    total=False,
)


class CreateApiCacheRequestTypeDef(
    _RequiredCreateApiCacheRequestTypeDef, _OptionalCreateApiCacheRequestTypeDef
):
    pass


CreateApiCacheResponseResponseTypeDef = TypedDict(
    "CreateApiCacheResponseResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApiKeyRequestTypeDef = TypedDict(
    "_RequiredCreateApiKeyRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalCreateApiKeyRequestTypeDef = TypedDict(
    "_OptionalCreateApiKeyRequestTypeDef",
    {
        "description": str,
        "expires": int,
    },
    total=False,
)


class CreateApiKeyRequestTypeDef(
    _RequiredCreateApiKeyRequestTypeDef, _OptionalCreateApiKeyRequestTypeDef
):
    pass


CreateApiKeyResponseResponseTypeDef = TypedDict(
    "CreateApiKeyResponseResponseTypeDef",
    {
        "apiKey": "ApiKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestTypeDef",
    {
        "description": str,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)


class CreateDataSourceRequestTypeDef(
    _RequiredCreateDataSourceRequestTypeDef, _OptionalCreateDataSourceRequestTypeDef
):
    pass


CreateDataSourceResponseResponseTypeDef = TypedDict(
    "CreateDataSourceResponseResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFunctionRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "dataSourceName": str,
        "functionVersion": str,
    },
)
_OptionalCreateFunctionRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)


class CreateFunctionRequestTypeDef(
    _RequiredCreateFunctionRequestTypeDef, _OptionalCreateFunctionRequestTypeDef
):
    pass


CreateFunctionResponseResponseTypeDef = TypedDict(
    "CreateFunctionResponseResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGraphqlApiRequestTypeDef = TypedDict(
    "_RequiredCreateGraphqlApiRequestTypeDef",
    {
        "name": str,
        "authenticationType": AuthenticationTypeType,
    },
)
_OptionalCreateGraphqlApiRequestTypeDef = TypedDict(
    "_OptionalCreateGraphqlApiRequestTypeDef",
    {
        "logConfig": "LogConfigTypeDef",
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
    },
    total=False,
)


class CreateGraphqlApiRequestTypeDef(
    _RequiredCreateGraphqlApiRequestTypeDef, _OptionalCreateGraphqlApiRequestTypeDef
):
    pass


CreateGraphqlApiResponseResponseTypeDef = TypedDict(
    "CreateGraphqlApiResponseResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResolverRequestTypeDef = TypedDict(
    "_RequiredCreateResolverRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)
_OptionalCreateResolverRequestTypeDef = TypedDict(
    "_OptionalCreateResolverRequestTypeDef",
    {
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
    },
    total=False,
)


class CreateResolverRequestTypeDef(
    _RequiredCreateResolverRequestTypeDef, _OptionalCreateResolverRequestTypeDef
):
    pass


CreateResolverResponseResponseTypeDef = TypedDict(
    "CreateResolverResponseResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTypeRequestTypeDef = TypedDict(
    "CreateTypeRequestTypeDef",
    {
        "apiId": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
    },
)

CreateTypeResponseResponseTypeDef = TypedDict(
    "CreateTypeResponseResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": DataSourceTypeType,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)

DeleteApiCacheRequestTypeDef = TypedDict(
    "DeleteApiCacheRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteApiKeyRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)

DeleteDataSourceRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

DeleteFunctionRequestTypeDef = TypedDict(
    "DeleteFunctionRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

DeleteGraphqlApiRequestTypeDef = TypedDict(
    "DeleteGraphqlApiRequestTypeDef",
    {
        "apiId": str,
    },
)

DeleteResolverRequestTypeDef = TypedDict(
    "DeleteResolverRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

DeleteTypeRequestTypeDef = TypedDict(
    "DeleteTypeRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)

DeltaSyncConfigTypeDef = TypedDict(
    "DeltaSyncConfigTypeDef",
    {
        "baseTableTTL": int,
        "deltaSyncTableName": str,
        "deltaSyncTableTTL": int,
    },
    total=False,
)

_RequiredDynamodbDataSourceConfigTypeDef = TypedDict(
    "_RequiredDynamodbDataSourceConfigTypeDef",
    {
        "tableName": str,
        "awsRegion": str,
    },
)
_OptionalDynamodbDataSourceConfigTypeDef = TypedDict(
    "_OptionalDynamodbDataSourceConfigTypeDef",
    {
        "useCallerCredentials": bool,
        "deltaSyncConfig": "DeltaSyncConfigTypeDef",
        "versioned": bool,
    },
    total=False,
)


class DynamodbDataSourceConfigTypeDef(
    _RequiredDynamodbDataSourceConfigTypeDef, _OptionalDynamodbDataSourceConfigTypeDef
):
    pass


ElasticsearchDataSourceConfigTypeDef = TypedDict(
    "ElasticsearchDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "awsRegion": str,
    },
)

FlushApiCacheRequestTypeDef = TypedDict(
    "FlushApiCacheRequestTypeDef",
    {
        "apiId": str,
    },
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)

GetApiCacheRequestTypeDef = TypedDict(
    "GetApiCacheRequestTypeDef",
    {
        "apiId": str,
    },
)

GetApiCacheResponseResponseTypeDef = TypedDict(
    "GetApiCacheResponseResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRequestTypeDef = TypedDict(
    "GetDataSourceRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)

GetDataSourceResponseResponseTypeDef = TypedDict(
    "GetDataSourceResponseResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionRequestTypeDef = TypedDict(
    "GetFunctionRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)

GetFunctionResponseResponseTypeDef = TypedDict(
    "GetFunctionResponseResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGraphqlApiRequestTypeDef = TypedDict(
    "GetGraphqlApiRequestTypeDef",
    {
        "apiId": str,
    },
)

GetGraphqlApiResponseResponseTypeDef = TypedDict(
    "GetGraphqlApiResponseResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntrospectionSchemaRequestTypeDef = TypedDict(
    "_RequiredGetIntrospectionSchemaRequestTypeDef",
    {
        "apiId": str,
        "format": OutputTypeType,
    },
)
_OptionalGetIntrospectionSchemaRequestTypeDef = TypedDict(
    "_OptionalGetIntrospectionSchemaRequestTypeDef",
    {
        "includeDirectives": bool,
    },
    total=False,
)


class GetIntrospectionSchemaRequestTypeDef(
    _RequiredGetIntrospectionSchemaRequestTypeDef, _OptionalGetIntrospectionSchemaRequestTypeDef
):
    pass


GetIntrospectionSchemaResponseResponseTypeDef = TypedDict(
    "GetIntrospectionSchemaResponseResponseTypeDef",
    {
        "schema": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResolverRequestTypeDef = TypedDict(
    "GetResolverRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)

GetResolverResponseResponseTypeDef = TypedDict(
    "GetResolverResponseResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaCreationStatusRequestTypeDef = TypedDict(
    "GetSchemaCreationStatusRequestTypeDef",
    {
        "apiId": str,
    },
)

GetSchemaCreationStatusResponseResponseTypeDef = TypedDict(
    "GetSchemaCreationStatusResponseResponseTypeDef",
    {
        "status": SchemaStatusType,
        "details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTypeRequestTypeDef = TypedDict(
    "GetTypeRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)

GetTypeResponseResponseTypeDef = TypedDict(
    "GetTypeResponseResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphqlApiTypeDef = TypedDict(
    "GraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": AuthenticationTypeType,
        "logConfig": "LogConfigTypeDef",
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
        "wafWebAclArn": str,
    },
    total=False,
)

HttpDataSourceConfigTypeDef = TypedDict(
    "HttpDataSourceConfigTypeDef",
    {
        "endpoint": str,
        "authorizationConfig": "AuthorizationConfigTypeDef",
    },
    total=False,
)

LambdaConflictHandlerConfigTypeDef = TypedDict(
    "LambdaConflictHandlerConfigTypeDef",
    {
        "lambdaConflictHandlerArn": str,
    },
    total=False,
)

LambdaDataSourceConfigTypeDef = TypedDict(
    "LambdaDataSourceConfigTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

_RequiredListApiKeysRequestTypeDef = TypedDict(
    "_RequiredListApiKeysRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListApiKeysRequestTypeDef = TypedDict(
    "_OptionalListApiKeysRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListApiKeysRequestTypeDef(
    _RequiredListApiKeysRequestTypeDef, _OptionalListApiKeysRequestTypeDef
):
    pass


ListApiKeysResponseResponseTypeDef = TypedDict(
    "ListApiKeysResponseResponseTypeDef",
    {
        "apiKeys": List["ApiKeyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListDataSourcesRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDataSourcesRequestTypeDef(
    _RequiredListDataSourcesRequestTypeDef, _OptionalListDataSourcesRequestTypeDef
):
    pass


ListDataSourcesResponseResponseTypeDef = TypedDict(
    "ListDataSourcesResponseResponseTypeDef",
    {
        "dataSources": List["DataSourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionsRequestTypeDef = TypedDict(
    "_RequiredListFunctionsRequestTypeDef",
    {
        "apiId": str,
    },
)
_OptionalListFunctionsRequestTypeDef = TypedDict(
    "_OptionalListFunctionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListFunctionsRequestTypeDef(
    _RequiredListFunctionsRequestTypeDef, _OptionalListFunctionsRequestTypeDef
):
    pass


ListFunctionsResponseResponseTypeDef = TypedDict(
    "ListFunctionsResponseResponseTypeDef",
    {
        "functions": List["FunctionConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGraphqlApisRequestTypeDef = TypedDict(
    "ListGraphqlApisRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListGraphqlApisResponseResponseTypeDef = TypedDict(
    "ListGraphqlApisResponseResponseTypeDef",
    {
        "graphqlApis": List["GraphqlApiTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResolversByFunctionRequestTypeDef = TypedDict(
    "_RequiredListResolversByFunctionRequestTypeDef",
    {
        "apiId": str,
        "functionId": str,
    },
)
_OptionalListResolversByFunctionRequestTypeDef = TypedDict(
    "_OptionalListResolversByFunctionRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListResolversByFunctionRequestTypeDef(
    _RequiredListResolversByFunctionRequestTypeDef, _OptionalListResolversByFunctionRequestTypeDef
):
    pass


ListResolversByFunctionResponseResponseTypeDef = TypedDict(
    "ListResolversByFunctionResponseResponseTypeDef",
    {
        "resolvers": List["ResolverTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResolversRequestTypeDef = TypedDict(
    "_RequiredListResolversRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
    },
)
_OptionalListResolversRequestTypeDef = TypedDict(
    "_OptionalListResolversRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListResolversRequestTypeDef(
    _RequiredListResolversRequestTypeDef, _OptionalListResolversRequestTypeDef
):
    pass


ListResolversResponseResponseTypeDef = TypedDict(
    "ListResolversResponseResponseTypeDef",
    {
        "resolvers": List["ResolverTypeDef"],
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

_RequiredListTypesRequestTypeDef = TypedDict(
    "_RequiredListTypesRequestTypeDef",
    {
        "apiId": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalListTypesRequestTypeDef = TypedDict(
    "_OptionalListTypesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTypesRequestTypeDef(_RequiredListTypesRequestTypeDef, _OptionalListTypesRequestTypeDef):
    pass


ListTypesResponseResponseTypeDef = TypedDict(
    "ListTypesResponseResponseTypeDef",
    {
        "types": List["TypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLogConfigTypeDef = TypedDict(
    "_RequiredLogConfigTypeDef",
    {
        "fieldLogLevel": FieldLogLevelType,
        "cloudWatchLogsRoleArn": str,
    },
)
_OptionalLogConfigTypeDef = TypedDict(
    "_OptionalLogConfigTypeDef",
    {
        "excludeVerboseContent": bool,
    },
    total=False,
)


class LogConfigTypeDef(_RequiredLogConfigTypeDef, _OptionalLogConfigTypeDef):
    pass


_RequiredOpenIDConnectConfigTypeDef = TypedDict(
    "_RequiredOpenIDConnectConfigTypeDef",
    {
        "issuer": str,
    },
)
_OptionalOpenIDConnectConfigTypeDef = TypedDict(
    "_OptionalOpenIDConnectConfigTypeDef",
    {
        "clientId": str,
        "iatTTL": int,
        "authTTL": int,
    },
    total=False,
)


class OpenIDConnectConfigTypeDef(
    _RequiredOpenIDConnectConfigTypeDef, _OptionalOpenIDConnectConfigTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PipelineConfigTypeDef = TypedDict(
    "PipelineConfigTypeDef",
    {
        "functions": List[str],
    },
    total=False,
)

RdsHttpEndpointConfigTypeDef = TypedDict(
    "RdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

RelationalDatabaseDataSourceConfigTypeDef = TypedDict(
    "RelationalDatabaseDataSourceConfigTypeDef",
    {
        "relationalDatabaseSourceType": Literal["RDS_HTTP_ENDPOINT"],
        "rdsHttpEndpointConfig": "RdsHttpEndpointConfigTypeDef",
    },
    total=False,
)

ResolverTypeDef = TypedDict(
    "ResolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
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

StartSchemaCreationRequestTypeDef = TypedDict(
    "StartSchemaCreationRequestTypeDef",
    {
        "apiId": str,
        "definition": Union[bytes, IO[bytes], StreamingBody],
    },
)

StartSchemaCreationResponseResponseTypeDef = TypedDict(
    "StartSchemaCreationResponseResponseTypeDef",
    {
        "status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncConfigTypeDef = TypedDict(
    "SyncConfigTypeDef",
    {
        "conflictHandler": ConflictHandlerTypeType,
        "conflictDetection": ConflictDetectionTypeType,
        "lambdaConflictHandlerConfig": "LambdaConflictHandlerConfigTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": TypeDefinitionFormatType,
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

UpdateApiCacheRequestTypeDef = TypedDict(
    "UpdateApiCacheRequestTypeDef",
    {
        "apiId": str,
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehaviorType,
        "type": ApiCacheTypeType,
    },
)

UpdateApiCacheResponseResponseTypeDef = TypedDict(
    "UpdateApiCacheResponseResponseTypeDef",
    {
        "apiCache": "ApiCacheTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateApiKeyRequestTypeDef = TypedDict(
    "_RequiredUpdateApiKeyRequestTypeDef",
    {
        "apiId": str,
        "id": str,
    },
)
_OptionalUpdateApiKeyRequestTypeDef = TypedDict(
    "_OptionalUpdateApiKeyRequestTypeDef",
    {
        "description": str,
        "expires": int,
    },
    total=False,
)


class UpdateApiKeyRequestTypeDef(
    _RequiredUpdateApiKeyRequestTypeDef, _OptionalUpdateApiKeyRequestTypeDef
):
    pass


UpdateApiKeyResponseResponseTypeDef = TypedDict(
    "UpdateApiKeyResponseResponseTypeDef",
    {
        "apiKey": "ApiKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourceRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "type": DataSourceTypeType,
    },
)
_OptionalUpdateDataSourceRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestTypeDef",
    {
        "description": str,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)


class UpdateDataSourceRequestTypeDef(
    _RequiredUpdateDataSourceRequestTypeDef, _OptionalUpdateDataSourceRequestTypeDef
):
    pass


UpdateDataSourceResponseResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFunctionRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionRequestTypeDef",
    {
        "apiId": str,
        "name": str,
        "functionId": str,
        "dataSourceName": str,
        "functionVersion": str,
    },
)
_OptionalUpdateFunctionRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionRequestTypeDef",
    {
        "description": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)


class UpdateFunctionRequestTypeDef(
    _RequiredUpdateFunctionRequestTypeDef, _OptionalUpdateFunctionRequestTypeDef
):
    pass


UpdateFunctionResponseResponseTypeDef = TypedDict(
    "UpdateFunctionResponseResponseTypeDef",
    {
        "functionConfiguration": "FunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGraphqlApiRequestTypeDef = TypedDict(
    "_RequiredUpdateGraphqlApiRequestTypeDef",
    {
        "apiId": str,
        "name": str,
    },
)
_OptionalUpdateGraphqlApiRequestTypeDef = TypedDict(
    "_OptionalUpdateGraphqlApiRequestTypeDef",
    {
        "logConfig": "LogConfigTypeDef",
        "authenticationType": AuthenticationTypeType,
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
    },
    total=False,
)


class UpdateGraphqlApiRequestTypeDef(
    _RequiredUpdateGraphqlApiRequestTypeDef, _OptionalUpdateGraphqlApiRequestTypeDef
):
    pass


UpdateGraphqlApiResponseResponseTypeDef = TypedDict(
    "UpdateGraphqlApiResponseResponseTypeDef",
    {
        "graphqlApi": "GraphqlApiTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResolverRequestTypeDef = TypedDict(
    "_RequiredUpdateResolverRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "fieldName": str,
    },
)
_OptionalUpdateResolverRequestTypeDef = TypedDict(
    "_OptionalUpdateResolverRequestTypeDef",
    {
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKindType,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
    },
    total=False,
)


class UpdateResolverRequestTypeDef(
    _RequiredUpdateResolverRequestTypeDef, _OptionalUpdateResolverRequestTypeDef
):
    pass


UpdateResolverResponseResponseTypeDef = TypedDict(
    "UpdateResolverResponseResponseTypeDef",
    {
        "resolver": "ResolverTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTypeRequestTypeDef = TypedDict(
    "_RequiredUpdateTypeRequestTypeDef",
    {
        "apiId": str,
        "typeName": str,
        "format": TypeDefinitionFormatType,
    },
)
_OptionalUpdateTypeRequestTypeDef = TypedDict(
    "_OptionalUpdateTypeRequestTypeDef",
    {
        "definition": str,
    },
    total=False,
)


class UpdateTypeRequestTypeDef(
    _RequiredUpdateTypeRequestTypeDef, _OptionalUpdateTypeRequestTypeDef
):
    pass


UpdateTypeResponseResponseTypeDef = TypedDict(
    "UpdateTypeResponseResponseTypeDef",
    {
        "type": "TypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserPoolConfigTypeDef = TypedDict(
    "_RequiredUserPoolConfigTypeDef",
    {
        "userPoolId": str,
        "awsRegion": str,
        "defaultAction": DefaultActionType,
    },
)
_OptionalUserPoolConfigTypeDef = TypedDict(
    "_OptionalUserPoolConfigTypeDef",
    {
        "appIdClientRegex": str,
    },
    total=False,
)


class UserPoolConfigTypeDef(_RequiredUserPoolConfigTypeDef, _OptionalUserPoolConfigTypeDef):
    pass
