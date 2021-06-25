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
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchGetDocumentStatusResponseErrorTypeDef",
    "BatchGetDocumentStatusResponseTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "CapacityUnitsConfigurationTypeDef",
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
    "CreateDataSourceResponseTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    "CreateThesaurusResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DatabaseConfigurationTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    "DescribeThesaurusResponseTypeDef",
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
    "GetQuerySuggestionsResponseTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "HighlightTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "IndexStatisticsTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFaqsResponseTypeDef",
    "ListIndicesResponseTypeDef",
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThesauriResponseTypeDef",
    "OneDriveConfigurationTypeDef",
    "OneDriveUsersTypeDef",
    "PrincipalTypeDef",
    "ProxyConfigurationTypeDef",
    "QueryResultItemTypeDef",
    "QueryResultTypeDef",
    "QuerySuggestionsBlockListSummaryTypeDef",
    "RelevanceFeedbackTypeDef",
    "RelevanceTypeDef",
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
    "StartDataSourceSyncJobResponseTypeDef",
    "StatusTypeDef",
    "SuggestionHighlightTypeDef",
    "SuggestionTextWithHighlightsTypeDef",
    "SuggestionTypeDef",
    "SuggestionValueTypeDef",
    "TagTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextWithHighlightsTypeDef",
    "ThesaurusSummaryTypeDef",
    "TimeRangeTypeDef",
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

BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "FailedDocuments": List["BatchDeleteDocumentResponseFailedDocumentTypeDef"],
    },
    total=False,
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

BatchGetDocumentStatusResponseTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseTypeDef",
    {
        "Errors": List["BatchGetDocumentStatusResponseErrorTypeDef"],
        "DocumentStatusList": List["StatusTypeDef"],
    },
    total=False,
)

BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "FailedDocuments": List["BatchPutDocumentResponseFailedDocumentTypeDef"],
    },
    total=False,
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "StorageCapacityUnits": int,
        "QueryCapacityUnits": int,
    },
)

ClickFeedbackTypeDef = TypedDict(
    "ClickFeedbackTypeDef",
    {
        "ResultId": str,
        "ClickTime": datetime,
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

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Id": str,
    },
)

CreateFaqResponseTypeDef = TypedDict(
    "CreateFaqResponseTypeDef",
    {
        "Id": str,
    },
    total=False,
)

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "Id": str,
    },
    total=False,
)

CreateQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    {
        "Id": str,
    },
    total=False,
)

CreateThesaurusResponseTypeDef = TypedDict(
    "CreateThesaurusResponseTypeDef",
    {
        "Id": str,
    },
    total=False,
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


DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
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
    },
    total=False,
)

DescribeFaqResponseTypeDef = TypedDict(
    "DescribeFaqResponseTypeDef",
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
    },
    total=False,
)

DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
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
    },
    total=False,
)

DescribeQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
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
    },
    total=False,
)

DescribeQuerySuggestionsConfigResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigResponseTypeDef",
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
    },
    total=False,
)

DescribeThesaurusResponseTypeDef = TypedDict(
    "DescribeThesaurusResponseTypeDef",
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
    },
    total=False,
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
        "DateValue": datetime,
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

GetQuerySuggestionsResponseTypeDef = TypedDict(
    "GetQuerySuggestionsResponseTypeDef",
    {
        "QuerySuggestionsId": str,
        "Suggestions": List["SuggestionTypeDef"],
    },
    total=False,
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


ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "History": List["DataSourceSyncJobTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "SummaryItems": List["DataSourceSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListFaqsResponseTypeDef = TypedDict(
    "ListFaqsResponseTypeDef",
    {
        "NextToken": str,
        "FaqSummaryItems": List["FaqSummaryTypeDef"],
    },
    total=False,
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List["IndexConfigurationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListQuerySuggestionsBlockListsResponseTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    {
        "BlockListSummaryItems": List["QuerySuggestionsBlockListSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ListThesauriResponseTypeDef = TypedDict(
    "ListThesauriResponseTypeDef",
    {
        "NextToken": str,
        "ThesaurusSummaryItems": List["ThesaurusSummaryTypeDef"],
    },
    total=False,
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

QueryResultTypeDef = TypedDict(
    "QueryResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List["QueryResultItemTypeDef"],
        "FacetResults": List["FacetResultTypeDef"],
        "TotalNumberOfResults": int,
    },
    total=False,
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

StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "ExecutionId": str,
    },
    total=False,
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
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

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
