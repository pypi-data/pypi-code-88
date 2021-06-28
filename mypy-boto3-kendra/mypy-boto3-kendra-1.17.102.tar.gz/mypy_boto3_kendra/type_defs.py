"""
Type annotations for kendra service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kendra.type_defs import AccessControlListConfigurationTypeDef

    data: AccessControlListConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ConfluenceAttachmentFieldNameType,
    ConfluenceBlogFieldNameType,
    ConfluencePageFieldNameType,
    ConfluenceSpaceFieldNameType,
    ConfluenceVersionType,
    ContentTypeType,
    DatabaseEngineTypeType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    DocumentAttributeValueTypeType,
    DocumentStatusType,
    ErrorCodeType,
    FaqFileFormatType,
    FaqStatusType,
    HighlightTypeType,
    IndexEditionType,
    IndexStatusType,
    KeyLocationType,
    ModeType,
    OrderType,
    PrincipalTypeType,
    QueryIdentifiersEnclosingOptionType,
    QueryResultTypeType,
    QuerySuggestionsBlockListStatusType,
    QuerySuggestionsStatusType,
    ReadAccessTypeType,
    RelevanceTypeType,
    SalesforceChatterFeedIncludeFilterTypeType,
    SalesforceKnowledgeArticleStateType,
    SalesforceStandardObjectNameType,
    ScoreConfidenceType,
    ServiceNowAuthenticationTypeType,
    ServiceNowBuildVersionTypeType,
    SharePointVersionType,
    SortOrderType,
    ThesaurusStatusType,
    UserContextPolicyType,
    WebCrawlerModeType,
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
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "AdditionalResultAttributeTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "AttributeFilterTypeDef",
    "AuthenticationConfigurationTypeDef",
    "BasicAuthenticationConfigurationTypeDef",
    "BatchDeleteDocumentRequestTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteDocumentResponseResponseTypeDef",
    "BatchGetDocumentStatusRequestTypeDef",
    "BatchGetDocumentStatusResponseErrorTypeDef",
    "BatchGetDocumentStatusResponseResponseTypeDef",
    "BatchPutDocumentRequestTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "BatchPutDocumentResponseResponseTypeDef",
    "CapacityUnitsConfigurationTypeDef",
    "ClearQuerySuggestionsRequestTypeDef",
    "ClickFeedbackTypeDef",
    "ColumnConfigurationTypeDef",
    "ConfluenceAttachmentConfigurationTypeDef",
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    "ConfluenceBlogConfigurationTypeDef",
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    "ConfluenceConfigurationTypeDef",
    "ConfluencePageConfigurationTypeDef",
    "ConfluencePageToIndexFieldMappingTypeDef",
    "ConfluenceSpaceConfigurationTypeDef",
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    "ConnectionConfigurationTypeDef",
    "CreateDataSourceRequestTypeDef",
    "CreateDataSourceResponseResponseTypeDef",
    "CreateFaqRequestTypeDef",
    "CreateFaqResponseResponseTypeDef",
    "CreateIndexRequestTypeDef",
    "CreateIndexResponseResponseTypeDef",
    "CreateQuerySuggestionsBlockListRequestTypeDef",
    "CreateQuerySuggestionsBlockListResponseResponseTypeDef",
    "CreateThesaurusRequestTypeDef",
    "CreateThesaurusResponseResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DatabaseConfigurationTypeDef",
    "DeleteDataSourceRequestTypeDef",
    "DeleteFaqRequestTypeDef",
    "DeleteIndexRequestTypeDef",
    "DeleteQuerySuggestionsBlockListRequestTypeDef",
    "DeleteThesaurusRequestTypeDef",
    "DescribeDataSourceRequestTypeDef",
    "DescribeDataSourceResponseResponseTypeDef",
    "DescribeFaqRequestTypeDef",
    "DescribeFaqResponseResponseTypeDef",
    "DescribeIndexRequestTypeDef",
    "DescribeIndexResponseResponseTypeDef",
    "DescribeQuerySuggestionsBlockListRequestTypeDef",
    "DescribeQuerySuggestionsBlockListResponseResponseTypeDef",
    "DescribeQuerySuggestionsConfigRequestTypeDef",
    "DescribeQuerySuggestionsConfigResponseResponseTypeDef",
    "DescribeThesaurusRequestTypeDef",
    "DescribeThesaurusResponseResponseTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentAttributeValueTypeDef",
    "DocumentInfoTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentRelevanceConfigurationTypeDef",
    "DocumentTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "FacetResultTypeDef",
    "FacetTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "GetQuerySuggestionsRequestTypeDef",
    "GetQuerySuggestionsResponseResponseTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "HighlightTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "IndexStatisticsTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListDataSourceSyncJobsRequestTypeDef",
    "ListDataSourceSyncJobsResponseResponseTypeDef",
    "ListDataSourcesRequestTypeDef",
    "ListDataSourcesResponseResponseTypeDef",
    "ListFaqsRequestTypeDef",
    "ListFaqsResponseResponseTypeDef",
    "ListIndicesRequestTypeDef",
    "ListIndicesResponseResponseTypeDef",
    "ListQuerySuggestionsBlockListsRequestTypeDef",
    "ListQuerySuggestionsBlockListsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListThesauriRequestTypeDef",
    "ListThesauriResponseResponseTypeDef",
    "OneDriveConfigurationTypeDef",
    "OneDriveUsersTypeDef",
    "PrincipalTypeDef",
    "ProxyConfigurationTypeDef",
    "QueryRequestTypeDef",
    "QueryResultItemTypeDef",
    "QueryResultResponseTypeDef",
    "QuerySuggestionsBlockListSummaryTypeDef",
    "RelevanceFeedbackTypeDef",
    "RelevanceTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3PathTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "SearchTypeDef",
    "SeedUrlConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServiceNowConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "SharePointConfigurationTypeDef",
    "SiteMapsConfigurationTypeDef",
    "SortingConfigurationTypeDef",
    "SqlConfigurationTypeDef",
    "StartDataSourceSyncJobRequestTypeDef",
    "StartDataSourceSyncJobResponseResponseTypeDef",
    "StatusTypeDef",
    "StopDataSourceSyncJobRequestTypeDef",
    "SubmitFeedbackRequestTypeDef",
    "SuggestionHighlightTypeDef",
    "SuggestionTextWithHighlightsTypeDef",
    "SuggestionTypeDef",
    "SuggestionValueTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextWithHighlightsTypeDef",
    "ThesaurusSummaryTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDataSourceRequestTypeDef",
    "UpdateIndexRequestTypeDef",
    "UpdateQuerySuggestionsBlockListRequestTypeDef",
    "UpdateQuerySuggestionsConfigRequestTypeDef",
    "UpdateThesaurusRequestTypeDef",
    "UrlsTypeDef",
    "UserContextTypeDef",
    "UserTokenConfigurationTypeDef",
    "WebCrawlerConfigurationTypeDef",
)

AccessControlListConfigurationTypeDef = TypedDict(
    "AccessControlListConfigurationTypeDef",
    {
        "KeyPath": str,
    },
    total=False,
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "AllowedGroupsColumnName": str,
    },
)

AdditionalResultAttributeTypeDef = TypedDict(
    "AdditionalResultAttributeTypeDef",
    {
        "Key": str,
        "ValueType": Literal["TEXT_WITH_HIGHLIGHTS_VALUE"],
        "Value": "AdditionalResultAttributeValueTypeDef",
    },
)

AdditionalResultAttributeValueTypeDef = TypedDict(
    "AdditionalResultAttributeValueTypeDef",
    {
        "TextWithHighlightsValue": "TextWithHighlightsTypeDef",
    },
    total=False,
)

AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "AndAllFilters": List[Dict[str, Any]],
        "OrAllFilters": List[Dict[str, Any]],
        "NotFilter": Dict[str, Any],
        "EqualsTo": "DocumentAttributeTypeDef",
        "ContainsAll": "DocumentAttributeTypeDef",
        "ContainsAny": "DocumentAttributeTypeDef",
        "GreaterThan": "DocumentAttributeTypeDef",
        "GreaterThanOrEquals": "DocumentAttributeTypeDef",
        "LessThan": "DocumentAttributeTypeDef",
        "LessThanOrEquals": "DocumentAttributeTypeDef",
    },
    total=False,
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "BasicAuthentication": List["BasicAuthenticationConfigurationTypeDef"],
    },
    total=False,
)

BasicAuthenticationConfigurationTypeDef = TypedDict(
    "BasicAuthenticationConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": str,
    },
)

_RequiredBatchDeleteDocumentRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteDocumentRequestTypeDef",
    {
        "IndexId": str,
        "DocumentIdList": List[str],
    },
)
_OptionalBatchDeleteDocumentRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteDocumentRequestTypeDef",
    {
        "DataSourceSyncJobMetricTarget": "DataSourceSyncJobMetricTargetTypeDef",
    },
    total=False,
)


class BatchDeleteDocumentRequestTypeDef(
    _RequiredBatchDeleteDocumentRequestTypeDef, _OptionalBatchDeleteDocumentRequestTypeDef
):
    pass


BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchDeleteDocumentResponseResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseResponseTypeDef",
    {
        "FailedDocuments": List["BatchDeleteDocumentResponseFailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDocumentStatusRequestTypeDef = TypedDict(
    "BatchGetDocumentStatusRequestTypeDef",
    {
        "IndexId": str,
        "DocumentInfoList": List["DocumentInfoTypeDef"],
    },
)

BatchGetDocumentStatusResponseErrorTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseErrorTypeDef",
    {
        "DocumentId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchGetDocumentStatusResponseResponseTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseResponseTypeDef",
    {
        "Errors": List["BatchGetDocumentStatusResponseErrorTypeDef"],
        "DocumentStatusList": List["StatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchPutDocumentRequestTypeDef = TypedDict(
    "_RequiredBatchPutDocumentRequestTypeDef",
    {
        "IndexId": str,
        "Documents": List["DocumentTypeDef"],
    },
)
_OptionalBatchPutDocumentRequestTypeDef = TypedDict(
    "_OptionalBatchPutDocumentRequestTypeDef",
    {
        "RoleArn": str,
    },
    total=False,
)


class BatchPutDocumentRequestTypeDef(
    _RequiredBatchPutDocumentRequestTypeDef, _OptionalBatchPutDocumentRequestTypeDef
):
    pass


BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchPutDocumentResponseResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseResponseTypeDef",
    {
        "FailedDocuments": List["BatchPutDocumentResponseFailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "StorageCapacityUnits": int,
        "QueryCapacityUnits": int,
    },
)

ClearQuerySuggestionsRequestTypeDef = TypedDict(
    "ClearQuerySuggestionsRequestTypeDef",
    {
        "IndexId": str,
    },
)

ClickFeedbackTypeDef = TypedDict(
    "ClickFeedbackTypeDef",
    {
        "ResultId": str,
        "ClickTime": Union[datetime, str],
    },
)

_RequiredColumnConfigurationTypeDef = TypedDict(
    "_RequiredColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": List[str],
    },
)
_OptionalColumnConfigurationTypeDef = TypedDict(
    "_OptionalColumnConfigurationTypeDef",
    {
        "DocumentTitleColumnName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)


class ColumnConfigurationTypeDef(
    _RequiredColumnConfigurationTypeDef, _OptionalColumnConfigurationTypeDef
):
    pass


ConfluenceAttachmentConfigurationTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "AttachmentFieldMappings": List["ConfluenceAttachmentToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluenceAttachmentToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceAttachmentFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceBlogConfigurationTypeDef = TypedDict(
    "ConfluenceBlogConfigurationTypeDef",
    {
        "BlogFieldMappings": List["ConfluenceBlogToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluenceBlogToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceBlogFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

_RequiredConfluenceConfigurationTypeDef = TypedDict(
    "_RequiredConfluenceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
    },
)
_OptionalConfluenceConfigurationTypeDef = TypedDict(
    "_OptionalConfluenceConfigurationTypeDef",
    {
        "SpaceConfiguration": "ConfluenceSpaceConfigurationTypeDef",
        "PageConfiguration": "ConfluencePageConfigurationTypeDef",
        "BlogConfiguration": "ConfluenceBlogConfigurationTypeDef",
        "AttachmentConfiguration": "ConfluenceAttachmentConfigurationTypeDef",
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
    },
    total=False,
)


class ConfluenceConfigurationTypeDef(
    _RequiredConfluenceConfigurationTypeDef, _OptionalConfluenceConfigurationTypeDef
):
    pass


ConfluencePageConfigurationTypeDef = TypedDict(
    "ConfluencePageConfigurationTypeDef",
    {
        "PageFieldMappings": List["ConfluencePageToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluencePageToIndexFieldMappingTypeDef = TypedDict(
    "ConfluencePageToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluencePageFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceSpaceConfigurationTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationTypeDef",
    {
        "CrawlPersonalSpaces": bool,
        "CrawlArchivedSpaces": bool,
        "IncludeSpaces": List[str],
        "ExcludeSpaces": List[str],
        "SpaceFieldMappings": List["ConfluenceSpaceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

ConfluenceSpaceToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceSpaceFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConnectionConfigurationTypeDef = TypedDict(
    "ConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
)

_RequiredCreateDataSourceRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "Type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestTypeDef",
    {
        "Configuration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "Schedule": str,
        "RoleArn": str,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
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
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFaqRequestTypeDef = TypedDict(
    "_RequiredCreateFaqRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "S3Path": "S3PathTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateFaqRequestTypeDef = TypedDict(
    "_OptionalCreateFaqRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "FileFormat": FaqFileFormatType,
        "ClientToken": str,
    },
    total=False,
)


class CreateFaqRequestTypeDef(_RequiredCreateFaqRequestTypeDef, _OptionalCreateFaqRequestTypeDef):
    pass


CreateFaqResponseResponseTypeDef = TypedDict(
    "CreateFaqResponseResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIndexRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalCreateIndexRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestTypeDef",
    {
        "Edition": IndexEditionType,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Description": str,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
    },
    total=False,
)


class CreateIndexRequestTypeDef(
    _RequiredCreateIndexRequestTypeDef, _OptionalCreateIndexRequestTypeDef
):
    pass


CreateIndexResponseResponseTypeDef = TypedDict(
    "CreateIndexResponseResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuerySuggestionsBlockListRequestTypeDef = TypedDict(
    "_RequiredCreateQuerySuggestionsBlockListRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "SourceS3Path": "S3PathTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateQuerySuggestionsBlockListRequestTypeDef = TypedDict(
    "_OptionalCreateQuerySuggestionsBlockListRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateQuerySuggestionsBlockListRequestTypeDef(
    _RequiredCreateQuerySuggestionsBlockListRequestTypeDef,
    _OptionalCreateQuerySuggestionsBlockListRequestTypeDef,
):
    pass


CreateQuerySuggestionsBlockListResponseResponseTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListResponseResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThesaurusRequestTypeDef = TypedDict(
    "_RequiredCreateThesaurusRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
    },
)
_OptionalCreateThesaurusRequestTypeDef = TypedDict(
    "_OptionalCreateThesaurusRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)


class CreateThesaurusRequestTypeDef(
    _RequiredCreateThesaurusRequestTypeDef, _OptionalCreateThesaurusRequestTypeDef
):
    pass


CreateThesaurusResponseResponseTypeDef = TypedDict(
    "CreateThesaurusResponseResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "S3Configuration": "S3DataSourceConfigurationTypeDef",
        "SharePointConfiguration": "SharePointConfigurationTypeDef",
        "DatabaseConfiguration": "DatabaseConfigurationTypeDef",
        "SalesforceConfiguration": "SalesforceConfigurationTypeDef",
        "OneDriveConfiguration": "OneDriveConfigurationTypeDef",
        "ServiceNowConfiguration": "ServiceNowConfigurationTypeDef",
        "ConfluenceConfiguration": "ConfluenceConfigurationTypeDef",
        "GoogleDriveConfiguration": "GoogleDriveConfigurationTypeDef",
        "WebCrawlerConfiguration": "WebCrawlerConfigurationTypeDef",
    },
    total=False,
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": DataSourceTypeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": DataSourceStatusType,
    },
    total=False,
)

_RequiredDataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "_RequiredDataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceId": str,
    },
)
_OptionalDataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "_OptionalDataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceSyncJobId": str,
    },
    total=False,
)


class DataSourceSyncJobMetricTargetTypeDef(
    _RequiredDataSourceSyncJobMetricTargetTypeDef, _OptionalDataSourceSyncJobMetricTargetTypeDef
):
    pass


DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "DocumentsAdded": str,
        "DocumentsModified": str,
        "DocumentsDeleted": str,
        "DocumentsFailed": str,
        "DocumentsScanned": str,
    },
    total=False,
)

DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "ExecutionId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Status": DataSourceSyncJobStatusType,
        "ErrorMessage": str,
        "ErrorCode": ErrorCodeType,
        "DataSourceErrorCode": str,
        "Metrics": "DataSourceSyncJobMetricsTypeDef",
    },
    total=False,
)

_RequiredDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_RequiredDataSourceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": str,
        "IndexFieldName": str,
    },
)
_OptionalDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_OptionalDataSourceToIndexFieldMappingTypeDef",
    {
        "DateFieldFormat": str,
    },
    total=False,
)


class DataSourceToIndexFieldMappingTypeDef(
    _RequiredDataSourceToIndexFieldMappingTypeDef, _OptionalDataSourceToIndexFieldMappingTypeDef
):
    pass


DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

_RequiredDatabaseConfigurationTypeDef = TypedDict(
    "_RequiredDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": "ConnectionConfigurationTypeDef",
        "ColumnConfiguration": "ColumnConfigurationTypeDef",
    },
)
_OptionalDatabaseConfigurationTypeDef = TypedDict(
    "_OptionalDatabaseConfigurationTypeDef",
    {
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "AclConfiguration": "AclConfigurationTypeDef",
        "SqlConfiguration": "SqlConfigurationTypeDef",
    },
    total=False,
)


class DatabaseConfigurationTypeDef(
    _RequiredDatabaseConfigurationTypeDef, _OptionalDatabaseConfigurationTypeDef
):
    pass


DeleteDataSourceRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteFaqRequestTypeDef = TypedDict(
    "DeleteFaqRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteIndexRequestTypeDef = TypedDict(
    "DeleteIndexRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteQuerySuggestionsBlockListRequestTypeDef = TypedDict(
    "DeleteQuerySuggestionsBlockListRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DeleteThesaurusRequestTypeDef = TypedDict(
    "DeleteThesaurusRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeDataSourceRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeDataSourceResponseResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Configuration": "DataSourceConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": DataSourceStatusType,
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFaqRequestTypeDef = TypedDict(
    "DescribeFaqRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeFaqResponseResponseTypeDef = TypedDict(
    "DescribeFaqResponseResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "S3Path": "S3PathTypeDef",
        "Status": FaqStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "FileFormat": FaqFileFormatType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexRequestTypeDef = TypedDict(
    "DescribeIndexRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeIndexResponseResponseTypeDef = TypedDict(
    "DescribeIndexResponseResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Status": IndexStatusType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List["DocumentMetadataConfigurationTypeDef"],
        "IndexStatistics": "IndexStatisticsTypeDef",
        "ErrorMessage": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuerySuggestionsBlockListRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DescribeQuerySuggestionsBlockListResponseResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListResponseResponseTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "SourceS3Path": "S3PathTypeDef",
        "ItemCount": int,
        "FileSizeBytes": int,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuerySuggestionsConfigRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigRequestTypeDef",
    {
        "IndexId": str,
    },
)

DescribeQuerySuggestionsConfigResponseResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigResponseResponseTypeDef",
    {
        "Mode": ModeType,
        "Status": QuerySuggestionsStatusType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
        "LastSuggestionsBuildTime": datetime,
        "LastClearTime": datetime,
        "TotalSuggestionsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThesaurusRequestTypeDef = TypedDict(
    "DescribeThesaurusRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeThesaurusResponseResponseTypeDef = TypedDict(
    "DescribeThesaurusResponseResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "Status": ThesaurusStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
        "FileSizeBytes": int,
        "TermCount": int,
        "SynonymRuleCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "Key": str,
        "Value": "DocumentAttributeValueTypeDef",
    },
)

DocumentAttributeValueCountPairTypeDef = TypedDict(
    "DocumentAttributeValueCountPairTypeDef",
    {
        "DocumentAttributeValue": "DocumentAttributeValueTypeDef",
        "Count": int,
    },
    total=False,
)

DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "StringValue": str,
        "StringListValue": List[str],
        "LongValue": int,
        "DateValue": Union[datetime, str],
    },
    total=False,
)

_RequiredDocumentInfoTypeDef = TypedDict(
    "_RequiredDocumentInfoTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalDocumentInfoTypeDef = TypedDict(
    "_OptionalDocumentInfoTypeDef",
    {
        "Attributes": List["DocumentAttributeTypeDef"],
    },
    total=False,
)


class DocumentInfoTypeDef(_RequiredDocumentInfoTypeDef, _OptionalDocumentInfoTypeDef):
    pass


_RequiredDocumentMetadataConfigurationTypeDef = TypedDict(
    "_RequiredDocumentMetadataConfigurationTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
    },
)
_OptionalDocumentMetadataConfigurationTypeDef = TypedDict(
    "_OptionalDocumentMetadataConfigurationTypeDef",
    {
        "Relevance": "RelevanceTypeDef",
        "Search": "SearchTypeDef",
    },
    total=False,
)


class DocumentMetadataConfigurationTypeDef(
    _RequiredDocumentMetadataConfigurationTypeDef, _OptionalDocumentMetadataConfigurationTypeDef
):
    pass


DocumentRelevanceConfigurationTypeDef = TypedDict(
    "DocumentRelevanceConfigurationTypeDef",
    {
        "Name": str,
        "Relevance": "RelevanceTypeDef",
    },
)

_RequiredDocumentTypeDef = TypedDict(
    "_RequiredDocumentTypeDef",
    {
        "Id": str,
    },
)
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "Title": str,
        "Blob": Union[bytes, IO[bytes], StreamingBody],
        "S3Path": "S3PathTypeDef",
        "Attributes": List["DocumentAttributeTypeDef"],
        "AccessControlList": List["PrincipalTypeDef"],
        "ContentType": ContentTypeType,
    },
    total=False,
)


class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass


DocumentsMetadataConfigurationTypeDef = TypedDict(
    "DocumentsMetadataConfigurationTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)

FacetResultTypeDef = TypedDict(
    "FacetResultTypeDef",
    {
        "DocumentAttributeKey": str,
        "DocumentAttributeValueType": DocumentAttributeValueTypeType,
        "DocumentAttributeValueCountPairs": List["DocumentAttributeValueCountPairTypeDef"],
    },
    total=False,
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "DocumentAttributeKey": str,
    },
    total=False,
)

FaqStatisticsTypeDef = TypedDict(
    "FaqStatisticsTypeDef",
    {
        "IndexedQuestionAnswersCount": int,
    },
)

FaqSummaryTypeDef = TypedDict(
    "FaqSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FaqStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "FileFormat": FaqFileFormatType,
    },
    total=False,
)

_RequiredGetQuerySuggestionsRequestTypeDef = TypedDict(
    "_RequiredGetQuerySuggestionsRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
    },
)
_OptionalGetQuerySuggestionsRequestTypeDef = TypedDict(
    "_OptionalGetQuerySuggestionsRequestTypeDef",
    {
        "MaxSuggestionsCount": int,
    },
    total=False,
)


class GetQuerySuggestionsRequestTypeDef(
    _RequiredGetQuerySuggestionsRequestTypeDef, _OptionalGetQuerySuggestionsRequestTypeDef
):
    pass


GetQuerySuggestionsResponseResponseTypeDef = TypedDict(
    "GetQuerySuggestionsResponseResponseTypeDef",
    {
        "QuerySuggestionsId": str,
        "Suggestions": List["SuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGoogleDriveConfigurationTypeDef = TypedDict(
    "_RequiredGoogleDriveConfigurationTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGoogleDriveConfigurationTypeDef = TypedDict(
    "_OptionalGoogleDriveConfigurationTypeDef",
    {
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "ExcludeMimeTypes": List[str],
        "ExcludeUserAccounts": List[str],
        "ExcludeSharedDrives": List[str],
    },
    total=False,
)


class GoogleDriveConfigurationTypeDef(
    _RequiredGoogleDriveConfigurationTypeDef, _OptionalGoogleDriveConfigurationTypeDef
):
    pass


_RequiredHighlightTypeDef = TypedDict(
    "_RequiredHighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
    },
)
_OptionalHighlightTypeDef = TypedDict(
    "_OptionalHighlightTypeDef",
    {
        "TopAnswer": bool,
        "Type": HighlightTypeType,
    },
    total=False,
)


class HighlightTypeDef(_RequiredHighlightTypeDef, _OptionalHighlightTypeDef):
    pass


_RequiredIndexConfigurationSummaryTypeDef = TypedDict(
    "_RequiredIndexConfigurationSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": IndexStatusType,
    },
)
_OptionalIndexConfigurationSummaryTypeDef = TypedDict(
    "_OptionalIndexConfigurationSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
    },
    total=False,
)


class IndexConfigurationSummaryTypeDef(
    _RequiredIndexConfigurationSummaryTypeDef, _OptionalIndexConfigurationSummaryTypeDef
):
    pass


IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "FaqStatistics": "FaqStatisticsTypeDef",
        "TextDocumentStatistics": "TextDocumentStatisticsTypeDef",
    },
)

JsonTokenTypeConfigurationTypeDef = TypedDict(
    "JsonTokenTypeConfigurationTypeDef",
    {
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
    },
)

_RequiredJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_RequiredJwtTokenTypeConfigurationTypeDef",
    {
        "KeyLocation": KeyLocationType,
    },
)
_OptionalJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_OptionalJwtTokenTypeConfigurationTypeDef",
    {
        "URL": str,
        "SecretManagerArn": str,
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
        "Issuer": str,
        "ClaimRegex": str,
    },
    total=False,
)


class JwtTokenTypeConfigurationTypeDef(
    _RequiredJwtTokenTypeConfigurationTypeDef, _OptionalJwtTokenTypeConfigurationTypeDef
):
    pass


_RequiredListDataSourceSyncJobsRequestTypeDef = TypedDict(
    "_RequiredListDataSourceSyncJobsRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListDataSourceSyncJobsRequestTypeDef = TypedDict(
    "_OptionalListDataSourceSyncJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartTimeFilter": "TimeRangeTypeDef",
        "StatusFilter": DataSourceSyncJobStatusType,
    },
    total=False,
)


class ListDataSourceSyncJobsRequestTypeDef(
    _RequiredListDataSourceSyncJobsRequestTypeDef, _OptionalListDataSourceSyncJobsRequestTypeDef
):
    pass


ListDataSourceSyncJobsResponseResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseResponseTypeDef",
    {
        "History": List["DataSourceSyncJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListDataSourcesRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
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
        "SummaryItems": List["DataSourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFaqsRequestTypeDef = TypedDict(
    "_RequiredListFaqsRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListFaqsRequestTypeDef = TypedDict(
    "_OptionalListFaqsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFaqsRequestTypeDef(_RequiredListFaqsRequestTypeDef, _OptionalListFaqsRequestTypeDef):
    pass


ListFaqsResponseResponseTypeDef = TypedDict(
    "ListFaqsResponseResponseTypeDef",
    {
        "NextToken": str,
        "FaqSummaryItems": List["FaqSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndicesRequestTypeDef = TypedDict(
    "ListIndicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListIndicesResponseResponseTypeDef = TypedDict(
    "ListIndicesResponseResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List["IndexConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQuerySuggestionsBlockListsRequestTypeDef = TypedDict(
    "_RequiredListQuerySuggestionsBlockListsRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListQuerySuggestionsBlockListsRequestTypeDef = TypedDict(
    "_OptionalListQuerySuggestionsBlockListsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQuerySuggestionsBlockListsRequestTypeDef(
    _RequiredListQuerySuggestionsBlockListsRequestTypeDef,
    _OptionalListQuerySuggestionsBlockListsRequestTypeDef,
):
    pass


ListQuerySuggestionsBlockListsResponseResponseTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsResponseResponseTypeDef",
    {
        "BlockListSummaryItems": List["QuerySuggestionsBlockListSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThesauriRequestTypeDef = TypedDict(
    "_RequiredListThesauriRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListThesauriRequestTypeDef = TypedDict(
    "_OptionalListThesauriRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListThesauriRequestTypeDef(
    _RequiredListThesauriRequestTypeDef, _OptionalListThesauriRequestTypeDef
):
    pass


ListThesauriResponseResponseTypeDef = TypedDict(
    "ListThesauriResponseResponseTypeDef",
    {
        "NextToken": str,
        "ThesaurusSummaryItems": List["ThesaurusSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOneDriveConfigurationTypeDef = TypedDict(
    "_RequiredOneDriveConfigurationTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": "OneDriveUsersTypeDef",
    },
)
_OptionalOneDriveConfigurationTypeDef = TypedDict(
    "_OptionalOneDriveConfigurationTypeDef",
    {
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "DisableLocalGroups": bool,
    },
    total=False,
)


class OneDriveConfigurationTypeDef(
    _RequiredOneDriveConfigurationTypeDef, _OptionalOneDriveConfigurationTypeDef
):
    pass


OneDriveUsersTypeDef = TypedDict(
    "OneDriveUsersTypeDef",
    {
        "OneDriveUserList": List[str],
        "OneDriveUserS3Path": "S3PathTypeDef",
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Name": str,
        "Type": PrincipalTypeType,
        "Access": ReadAccessTypeType,
    },
)

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {
        "Credentials": str,
    },
    total=False,
)


class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass


_RequiredQueryRequestTypeDef = TypedDict(
    "_RequiredQueryRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
    },
)
_OptionalQueryRequestTypeDef = TypedDict(
    "_OptionalQueryRequestTypeDef",
    {
        "AttributeFilter": "AttributeFilterTypeDef",
        "Facets": List["FacetTypeDef"],
        "RequestedDocumentAttributes": List[str],
        "QueryResultTypeFilter": QueryResultTypeType,
        "DocumentRelevanceOverrideConfigurations": List["DocumentRelevanceConfigurationTypeDef"],
        "PageNumber": int,
        "PageSize": int,
        "SortingConfiguration": "SortingConfigurationTypeDef",
        "UserContext": "UserContextTypeDef",
        "VisitorId": str,
    },
    total=False,
)


class QueryRequestTypeDef(_RequiredQueryRequestTypeDef, _OptionalQueryRequestTypeDef):
    pass


QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": str,
        "Type": QueryResultTypeType,
        "AdditionalAttributes": List["AdditionalResultAttributeTypeDef"],
        "DocumentId": str,
        "DocumentTitle": "TextWithHighlightsTypeDef",
        "DocumentExcerpt": "TextWithHighlightsTypeDef",
        "DocumentURI": str,
        "DocumentAttributes": List["DocumentAttributeTypeDef"],
        "ScoreAttributes": "ScoreAttributesTypeDef",
        "FeedbackToken": str,
    },
    total=False,
)

QueryResultResponseTypeDef = TypedDict(
    "QueryResultResponseTypeDef",
    {
        "QueryId": str,
        "ResultItems": List["QueryResultItemTypeDef"],
        "FacetResults": List["FacetResultTypeDef"],
        "TotalNumberOfResults": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuerySuggestionsBlockListSummaryTypeDef = TypedDict(
    "QuerySuggestionsBlockListSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ItemCount": int,
    },
    total=False,
)

RelevanceFeedbackTypeDef = TypedDict(
    "RelevanceFeedbackTypeDef",
    {
        "ResultId": str,
        "RelevanceValue": RelevanceTypeType,
    },
)

RelevanceTypeDef = TypedDict(
    "RelevanceTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": OrderType,
        "ValueImportanceMap": Dict[str, int],
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

_RequiredS3DataSourceConfigurationTypeDef = TypedDict(
    "_RequiredS3DataSourceConfigurationTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3DataSourceConfigurationTypeDef = TypedDict(
    "_OptionalS3DataSourceConfigurationTypeDef",
    {
        "InclusionPrefixes": List[str],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "DocumentsMetadataConfiguration": "DocumentsMetadataConfigurationTypeDef",
        "AccessControlListConfiguration": "AccessControlListConfigurationTypeDef",
    },
    total=False,
)


class S3DataSourceConfigurationTypeDef(
    _RequiredS3DataSourceConfigurationTypeDef, _OptionalS3DataSourceConfigurationTypeDef
):
    pass


S3PathTypeDef = TypedDict(
    "S3PathTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

_RequiredSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "IncludeFilterTypes": List[SalesforceChatterFeedIncludeFilterTypeType],
    },
    total=False,
)


class SalesforceChatterFeedConfigurationTypeDef(
    _RequiredSalesforceChatterFeedConfigurationTypeDef,
    _OptionalSalesforceChatterFeedConfigurationTypeDef,
):
    pass


_RequiredSalesforceConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
    },
)
_OptionalSalesforceConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceConfigurationTypeDef",
    {
        "StandardObjectConfigurations": List["SalesforceStandardObjectConfigurationTypeDef"],
        "KnowledgeArticleConfiguration": "SalesforceKnowledgeArticleConfigurationTypeDef",
        "ChatterFeedConfiguration": "SalesforceChatterFeedConfigurationTypeDef",
        "CrawlAttachments": bool,
        "StandardObjectAttachmentConfiguration": "SalesforceStandardObjectAttachmentConfigurationTypeDef",
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
    },
    total=False,
)


class SalesforceConfigurationTypeDef(
    _RequiredSalesforceConfigurationTypeDef, _OptionalSalesforceConfigurationTypeDef
):
    pass


_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)


class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
):
    pass


_RequiredSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "IncludedStates": List[SalesforceKnowledgeArticleStateType],
    },
)
_OptionalSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "StandardKnowledgeArticleTypeConfiguration": "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
        "CustomKnowledgeArticleTypeConfigurations": List[
            "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"
        ],
    },
    total=False,
)


class SalesforceKnowledgeArticleConfigurationTypeDef(
    _RequiredSalesforceKnowledgeArticleConfigurationTypeDef,
    _OptionalSalesforceKnowledgeArticleConfigurationTypeDef,
):
    pass


_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)


class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
):
    pass


SalesforceStandardObjectAttachmentConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)

_RequiredSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardObjectConfigurationTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardObjectConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)


class SalesforceStandardObjectConfigurationTypeDef(
    _RequiredSalesforceStandardObjectConfigurationTypeDef,
    _OptionalSalesforceStandardObjectConfigurationTypeDef,
):
    pass


ScoreAttributesTypeDef = TypedDict(
    "ScoreAttributesTypeDef",
    {
        "ScoreConfidence": ScoreConfidenceType,
    },
    total=False,
)

SearchTypeDef = TypedDict(
    "SearchTypeDef",
    {
        "Facetable": bool,
        "Searchable": bool,
        "Displayable": bool,
        "Sortable": bool,
    },
    total=False,
)

_RequiredSeedUrlConfigurationTypeDef = TypedDict(
    "_RequiredSeedUrlConfigurationTypeDef",
    {
        "SeedUrls": List[str],
    },
)
_OptionalSeedUrlConfigurationTypeDef = TypedDict(
    "_OptionalSeedUrlConfigurationTypeDef",
    {
        "WebCrawlerMode": WebCrawlerModeType,
    },
    total=False,
)


class SeedUrlConfigurationTypeDef(
    _RequiredSeedUrlConfigurationTypeDef, _OptionalSeedUrlConfigurationTypeDef
):
    pass


ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredServiceNowConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowConfigurationTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
    },
)
_OptionalServiceNowConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowConfigurationTypeDef",
    {
        "KnowledgeArticleConfiguration": "ServiceNowKnowledgeArticleConfigurationTypeDef",
        "ServiceCatalogConfiguration": "ServiceNowServiceCatalogConfigurationTypeDef",
        "AuthenticationType": ServiceNowAuthenticationTypeType,
    },
    total=False,
)


class ServiceNowConfigurationTypeDef(
    _RequiredServiceNowConfigurationTypeDef, _OptionalServiceNowConfigurationTypeDef
):
    pass


_RequiredServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "FilterQuery": str,
    },
    total=False,
)


class ServiceNowKnowledgeArticleConfigurationTypeDef(
    _RequiredServiceNowKnowledgeArticleConfigurationTypeDef,
    _OptionalServiceNowKnowledgeArticleConfigurationTypeDef,
):
    pass


_RequiredServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowServiceCatalogConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowServiceCatalogConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
    },
    total=False,
)


class ServiceNowServiceCatalogConfigurationTypeDef(
    _RequiredServiceNowServiceCatalogConfigurationTypeDef,
    _OptionalServiceNowServiceCatalogConfigurationTypeDef,
):
    pass


_RequiredSharePointConfigurationTypeDef = TypedDict(
    "_RequiredSharePointConfigurationTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": List[str],
        "SecretArn": str,
    },
)
_OptionalSharePointConfigurationTypeDef = TypedDict(
    "_OptionalSharePointConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "FieldMappings": List["DataSourceToIndexFieldMappingTypeDef"],
        "DocumentTitleFieldName": str,
        "DisableLocalGroups": bool,
        "SslCertificateS3Path": "S3PathTypeDef",
    },
    total=False,
)


class SharePointConfigurationTypeDef(
    _RequiredSharePointConfigurationTypeDef, _OptionalSharePointConfigurationTypeDef
):
    pass


SiteMapsConfigurationTypeDef = TypedDict(
    "SiteMapsConfigurationTypeDef",
    {
        "SiteMaps": List[str],
    },
)

SortingConfigurationTypeDef = TypedDict(
    "SortingConfigurationTypeDef",
    {
        "DocumentAttributeKey": str,
        "SortOrder": SortOrderType,
    },
)

SqlConfigurationTypeDef = TypedDict(
    "SqlConfigurationTypeDef",
    {
        "QueryIdentifiersEnclosingOption": QueryIdentifiersEnclosingOptionType,
    },
    total=False,
)

StartDataSourceSyncJobRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

StartDataSourceSyncJobResponseResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseResponseTypeDef",
    {
        "ExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "DocumentId": str,
        "DocumentStatus": DocumentStatusType,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

StopDataSourceSyncJobRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

_RequiredSubmitFeedbackRequestTypeDef = TypedDict(
    "_RequiredSubmitFeedbackRequestTypeDef",
    {
        "IndexId": str,
        "QueryId": str,
    },
)
_OptionalSubmitFeedbackRequestTypeDef = TypedDict(
    "_OptionalSubmitFeedbackRequestTypeDef",
    {
        "ClickFeedbackItems": List["ClickFeedbackTypeDef"],
        "RelevanceFeedbackItems": List["RelevanceFeedbackTypeDef"],
    },
    total=False,
)


class SubmitFeedbackRequestTypeDef(
    _RequiredSubmitFeedbackRequestTypeDef, _OptionalSubmitFeedbackRequestTypeDef
):
    pass


SuggestionHighlightTypeDef = TypedDict(
    "SuggestionHighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

SuggestionTextWithHighlightsTypeDef = TypedDict(
    "SuggestionTextWithHighlightsTypeDef",
    {
        "Text": str,
        "Highlights": List["SuggestionHighlightTypeDef"],
    },
    total=False,
)

SuggestionTypeDef = TypedDict(
    "SuggestionTypeDef",
    {
        "Id": str,
        "Value": "SuggestionValueTypeDef",
    },
    total=False,
)

SuggestionValueTypeDef = TypedDict(
    "SuggestionValueTypeDef",
    {
        "Text": "SuggestionTextWithHighlightsTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "IndexedTextDocumentsCount": int,
        "IndexedTextBytes": int,
    },
)

TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef",
    {
        "Text": str,
        "Highlights": List["HighlightTypeDef"],
    },
    total=False,
)

ThesaurusSummaryTypeDef = TypedDict(
    "ThesaurusSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ThesaurusStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDataSourceRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateDataSourceRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestTypeDef",
    {
        "Name": str,
        "Configuration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "Schedule": str,
        "RoleArn": str,
    },
    total=False,
)


class UpdateDataSourceRequestTypeDef(
    _RequiredUpdateDataSourceRequestTypeDef, _OptionalUpdateDataSourceRequestTypeDef
):
    pass


_RequiredUpdateIndexRequestTypeDef = TypedDict(
    "_RequiredUpdateIndexRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateIndexRequestTypeDef = TypedDict(
    "_OptionalUpdateIndexRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Description": str,
        "DocumentMetadataConfigurationUpdates": List["DocumentMetadataConfigurationTypeDef"],
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
    },
    total=False,
)


class UpdateIndexRequestTypeDef(
    _RequiredUpdateIndexRequestTypeDef, _OptionalUpdateIndexRequestTypeDef
):
    pass


_RequiredUpdateQuerySuggestionsBlockListRequestTypeDef = TypedDict(
    "_RequiredUpdateQuerySuggestionsBlockListRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
_OptionalUpdateQuerySuggestionsBlockListRequestTypeDef = TypedDict(
    "_OptionalUpdateQuerySuggestionsBlockListRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SourceS3Path": "S3PathTypeDef",
        "RoleArn": str,
    },
    total=False,
)


class UpdateQuerySuggestionsBlockListRequestTypeDef(
    _RequiredUpdateQuerySuggestionsBlockListRequestTypeDef,
    _OptionalUpdateQuerySuggestionsBlockListRequestTypeDef,
):
    pass


_RequiredUpdateQuerySuggestionsConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateQuerySuggestionsConfigRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalUpdateQuerySuggestionsConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateQuerySuggestionsConfigRequestTypeDef",
    {
        "Mode": ModeType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
    },
    total=False,
)


class UpdateQuerySuggestionsConfigRequestTypeDef(
    _RequiredUpdateQuerySuggestionsConfigRequestTypeDef,
    _OptionalUpdateQuerySuggestionsConfigRequestTypeDef,
):
    pass


_RequiredUpdateThesaurusRequestTypeDef = TypedDict(
    "_RequiredUpdateThesaurusRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateThesaurusRequestTypeDef = TypedDict(
    "_OptionalUpdateThesaurusRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
    },
    total=False,
)


class UpdateThesaurusRequestTypeDef(
    _RequiredUpdateThesaurusRequestTypeDef, _OptionalUpdateThesaurusRequestTypeDef
):
    pass


UrlsTypeDef = TypedDict(
    "UrlsTypeDef",
    {
        "SeedUrlConfiguration": "SeedUrlConfigurationTypeDef",
        "SiteMapsConfiguration": "SiteMapsConfigurationTypeDef",
    },
    total=False,
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "Token": str,
    },
    total=False,
)

UserTokenConfigurationTypeDef = TypedDict(
    "UserTokenConfigurationTypeDef",
    {
        "JwtTokenTypeConfiguration": "JwtTokenTypeConfigurationTypeDef",
        "JsonTokenTypeConfiguration": "JsonTokenTypeConfigurationTypeDef",
    },
    total=False,
)

_RequiredWebCrawlerConfigurationTypeDef = TypedDict(
    "_RequiredWebCrawlerConfigurationTypeDef",
    {
        "Urls": "UrlsTypeDef",
    },
)
_OptionalWebCrawlerConfigurationTypeDef = TypedDict(
    "_OptionalWebCrawlerConfigurationTypeDef",
    {
        "CrawlDepth": int,
        "MaxLinksPerPage": int,
        "MaxContentSizePerPageInMegaBytes": float,
        "MaxUrlsPerMinuteCrawlRate": int,
        "UrlInclusionPatterns": List[str],
        "UrlExclusionPatterns": List[str],
        "ProxyConfiguration": "ProxyConfigurationTypeDef",
        "AuthenticationConfiguration": "AuthenticationConfigurationTypeDef",
    },
    total=False,
)


class WebCrawlerConfigurationTypeDef(
    _RequiredWebCrawlerConfigurationTypeDef, _OptionalWebCrawlerConfigurationTypeDef
):
    pass
