"""
Type annotations for databrew service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/type_defs.html)

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import BatchDeleteRecipeVersionRequestTypeDef

    data: BatchDeleteRecipeVersionRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CompressionFormatType,
    EncryptionModeType,
    InputFormatType,
    JobRunStateType,
    JobTypeType,
    LogSubscriptionType,
    OrderType,
    OutputFormatType,
    ParameterTypeType,
    SampleModeType,
    SampleTypeType,
    SessionStatusType,
    SourceType,
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
    "BatchDeleteRecipeVersionRequestTypeDef",
    "BatchDeleteRecipeVersionResponseResponseTypeDef",
    "ConditionExpressionTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseResponseTypeDef",
    "CreateProfileJobRequestTypeDef",
    "CreateProfileJobResponseResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseResponseTypeDef",
    "CreateRecipeJobRequestTypeDef",
    "CreateRecipeJobResponseResponseTypeDef",
    "CreateRecipeRequestTypeDef",
    "CreateRecipeResponseResponseTypeDef",
    "CreateScheduleRequestTypeDef",
    "CreateScheduleResponseResponseTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatasetParameterTypeDef",
    "DatasetTypeDef",
    "DatetimeOptionsTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteDatasetResponseResponseTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteJobResponseResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResponseResponseTypeDef",
    "DeleteRecipeVersionRequestTypeDef",
    "DeleteRecipeVersionResponseResponseTypeDef",
    "DeleteScheduleRequestTypeDef",
    "DeleteScheduleResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeJobRequestTypeDef",
    "DescribeJobResponseResponseTypeDef",
    "DescribeJobRunRequestTypeDef",
    "DescribeJobRunResponseResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResponseResponseTypeDef",
    "DescribeRecipeRequestTypeDef",
    "DescribeRecipeResponseResponseTypeDef",
    "DescribeScheduleRequestTypeDef",
    "DescribeScheduleResponseResponseTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionTypeDef",
    "FormatOptionsTypeDef",
    "InputTypeDef",
    "JobRunTypeDef",
    "JobSampleTypeDef",
    "JobTypeDef",
    "JsonOptionsTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseResponseTypeDef",
    "ListJobRunsRequestTypeDef",
    "ListJobRunsResponseResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseResponseTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseResponseTypeDef",
    "ListRecipeVersionsRequestTypeDef",
    "ListRecipeVersionsResponseResponseTypeDef",
    "ListRecipesRequestTypeDef",
    "ListRecipesResponseResponseTypeDef",
    "ListSchedulesRequestTypeDef",
    "ListSchedulesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "OutputFormatOptionsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathOptionsTypeDef",
    "ProjectTypeDef",
    "PublishRecipeRequestTypeDef",
    "PublishRecipeResponseResponseTypeDef",
    "RecipeActionTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepTypeDef",
    "RecipeTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SampleTypeDef",
    "ScheduleTypeDef",
    "SendProjectSessionActionRequestTypeDef",
    "SendProjectSessionActionResponseResponseTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseResponseTypeDef",
    "StartProjectSessionRequestTypeDef",
    "StartProjectSessionResponseResponseTypeDef",
    "StopJobRunRequestTypeDef",
    "StopJobRunResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasetRequestTypeDef",
    "UpdateDatasetResponseResponseTypeDef",
    "UpdateProfileJobRequestTypeDef",
    "UpdateProfileJobResponseResponseTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateProjectResponseResponseTypeDef",
    "UpdateRecipeJobRequestTypeDef",
    "UpdateRecipeJobResponseResponseTypeDef",
    "UpdateRecipeRequestTypeDef",
    "UpdateRecipeResponseResponseTypeDef",
    "UpdateScheduleRequestTypeDef",
    "UpdateScheduleResponseResponseTypeDef",
    "ViewFrameTypeDef",
)

BatchDeleteRecipeVersionRequestTypeDef = TypedDict(
    "BatchDeleteRecipeVersionRequestTypeDef",
    {
        "Name": str,
        "RecipeVersions": List[str],
    },
)

BatchDeleteRecipeVersionResponseResponseTypeDef = TypedDict(
    "BatchDeleteRecipeVersionResponseResponseTypeDef",
    {
        "Name": str,
        "Errors": List["RecipeVersionErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConditionExpressionTypeDef = TypedDict(
    "_RequiredConditionExpressionTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
    },
)
_OptionalConditionExpressionTypeDef = TypedDict(
    "_OptionalConditionExpressionTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class ConditionExpressionTypeDef(
    _RequiredConditionExpressionTypeDef, _OptionalConditionExpressionTypeDef
):
    pass


_RequiredCreateDatasetRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
    },
)
_OptionalCreateDatasetRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestTypeDef",
    {
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDatasetRequestTypeDef(
    _RequiredCreateDatasetRequestTypeDef, _OptionalCreateDatasetRequestTypeDef
):
    pass


CreateDatasetResponseResponseTypeDef = TypedDict(
    "CreateDatasetResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileJobRequestTypeDef = TypedDict(
    "_RequiredCreateProfileJobRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "OutputLocation": "S3LocationTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateProfileJobRequestTypeDef = TypedDict(
    "_OptionalCreateProfileJobRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class CreateProfileJobRequestTypeDef(
    _RequiredCreateProfileJobRequestTypeDef, _OptionalCreateProfileJobRequestTypeDef
):
    pass


CreateProfileJobResponseResponseTypeDef = TypedDict(
    "CreateProfileJobResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "RecipeName": str,
        "RoleArn": str,
    },
)
_OptionalCreateProjectRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestTypeDef",
    {
        "Sample": "SampleTypeDef",
        "Tags": Dict[str, str],
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
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecipeJobRequestTypeDef = TypedDict(
    "_RequiredCreateRecipeJobRequestTypeDef",
    {
        "Name": str,
        "Outputs": List["OutputTypeDef"],
        "RoleArn": str,
    },
)
_OptionalCreateRecipeJobRequestTypeDef = TypedDict(
    "_OptionalCreateRecipeJobRequestTypeDef",
    {
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "Tags": Dict[str, str],
        "Timeout": int,
    },
    total=False,
)


class CreateRecipeJobRequestTypeDef(
    _RequiredCreateRecipeJobRequestTypeDef, _OptionalCreateRecipeJobRequestTypeDef
):
    pass


CreateRecipeJobResponseResponseTypeDef = TypedDict(
    "CreateRecipeJobResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecipeRequestTypeDef = TypedDict(
    "_RequiredCreateRecipeRequestTypeDef",
    {
        "Name": str,
        "Steps": List["RecipeStepTypeDef"],
    },
)
_OptionalCreateRecipeRequestTypeDef = TypedDict(
    "_OptionalCreateRecipeRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateRecipeRequestTypeDef(
    _RequiredCreateRecipeRequestTypeDef, _OptionalCreateRecipeRequestTypeDef
):
    pass


CreateRecipeResponseResponseTypeDef = TypedDict(
    "CreateRecipeResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduleRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
    },
)
_OptionalCreateScheduleRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleRequestTypeDef",
    {
        "JobNames": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateScheduleRequestTypeDef(
    _RequiredCreateScheduleRequestTypeDef, _OptionalCreateScheduleRequestTypeDef
):
    pass


CreateScheduleResponseResponseTypeDef = TypedDict(
    "CreateScheduleResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": str,
        "HeaderRow": bool,
    },
    total=False,
)

CsvOutputOptionsTypeDef = TypedDict(
    "CsvOutputOptionsTypeDef",
    {
        "Delimiter": str,
    },
    total=False,
)

_RequiredDataCatalogInputDefinitionTypeDef = TypedDict(
    "_RequiredDataCatalogInputDefinitionTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalDataCatalogInputDefinitionTypeDef = TypedDict(
    "_OptionalDataCatalogInputDefinitionTypeDef",
    {
        "CatalogId": str,
        "TempDirectory": "S3LocationTypeDef",
    },
    total=False,
)


class DataCatalogInputDefinitionTypeDef(
    _RequiredDataCatalogInputDefinitionTypeDef, _OptionalDataCatalogInputDefinitionTypeDef
):
    pass


_RequiredDatabaseInputDefinitionTypeDef = TypedDict(
    "_RequiredDatabaseInputDefinitionTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseTableName": str,
    },
)
_OptionalDatabaseInputDefinitionTypeDef = TypedDict(
    "_OptionalDatabaseInputDefinitionTypeDef",
    {
        "TempDirectory": "S3LocationTypeDef",
    },
    total=False,
)


class DatabaseInputDefinitionTypeDef(
    _RequiredDatabaseInputDefinitionTypeDef, _OptionalDatabaseInputDefinitionTypeDef
):
    pass


_RequiredDatasetParameterTypeDef = TypedDict(
    "_RequiredDatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalDatasetParameterTypeDef = TypedDict(
    "_OptionalDatasetParameterTypeDef",
    {
        "DatetimeOptions": "DatetimeOptionsTypeDef",
        "CreateColumn": bool,
        "Filter": "FilterExpressionTypeDef",
    },
    total=False,
)


class DatasetParameterTypeDef(_RequiredDatasetParameterTypeDef, _OptionalDatasetParameterTypeDef):
    pass


_RequiredDatasetTypeDef = TypedDict(
    "_RequiredDatasetTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
    },
)
_OptionalDatasetTypeDef = TypedDict(
    "_OptionalDatasetTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
    },
    total=False,
)


class DatasetTypeDef(_RequiredDatasetTypeDef, _OptionalDatasetTypeDef):
    pass


_RequiredDatetimeOptionsTypeDef = TypedDict(
    "_RequiredDatetimeOptionsTypeDef",
    {
        "Format": str,
    },
)
_OptionalDatetimeOptionsTypeDef = TypedDict(
    "_OptionalDatetimeOptionsTypeDef",
    {
        "TimezoneOffset": str,
        "LocaleCode": str,
    },
    total=False,
)


class DatetimeOptionsTypeDef(_RequiredDatetimeOptionsTypeDef, _OptionalDatetimeOptionsTypeDef):
    pass


DeleteDatasetRequestTypeDef = TypedDict(
    "DeleteDatasetRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDatasetResponseResponseTypeDef = TypedDict(
    "DeleteDatasetResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJobRequestTypeDef = TypedDict(
    "DeleteJobRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteJobResponseResponseTypeDef = TypedDict(
    "DeleteJobResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestTypeDef = TypedDict(
    "DeleteProjectRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteProjectResponseResponseTypeDef = TypedDict(
    "DeleteProjectResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecipeVersionRequestTypeDef = TypedDict(
    "DeleteRecipeVersionRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
    },
)

DeleteRecipeVersionResponseResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseResponseTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteScheduleRequestTypeDef = TypedDict(
    "DeleteScheduleRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteScheduleResponseResponseTypeDef = TypedDict(
    "DeleteScheduleResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Name": str,
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "Input": "InputTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestTypeDef = TypedDict(
    "DescribeJobRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeJobResponseResponseTypeDef = TypedDict(
    "DescribeJobResponseResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Name": str,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestTypeDef = TypedDict(
    "DescribeJobRunRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

DescribeJobRunResponseResponseTypeDef = TypedDict(
    "DescribeJobRunResponseResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestTypeDef = TypedDict(
    "DescribeProjectRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeProjectResponseResponseTypeDef = TypedDict(
    "DescribeProjectResponseResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Name": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatusType,
        "OpenedBy": str,
        "OpenDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRecipeRequestTypeDef = TypedDict(
    "_RequiredDescribeRecipeRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeRecipeRequestTypeDef = TypedDict(
    "_OptionalDescribeRecipeRequestTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)


class DescribeRecipeRequestTypeDef(
    _RequiredDescribeRecipeRequestTypeDef, _OptionalDescribeRecipeRequestTypeDef
):
    pass


DescribeRecipeResponseResponseTypeDef = TypedDict(
    "DescribeRecipeResponseResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Name": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduleRequestTypeDef = TypedDict(
    "DescribeScheduleRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeScheduleResponseResponseTypeDef = TypedDict(
    "DescribeScheduleResponseResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {
        "SheetNames": List[str],
        "SheetIndexes": List[int],
        "HeaderRow": bool,
    },
    total=False,
)

_RequiredFilesLimitTypeDef = TypedDict(
    "_RequiredFilesLimitTypeDef",
    {
        "MaxFiles": int,
    },
)
_OptionalFilesLimitTypeDef = TypedDict(
    "_OptionalFilesLimitTypeDef",
    {
        "OrderedBy": Literal["LAST_MODIFIED_DATE"],
        "Order": OrderType,
    },
    total=False,
)


class FilesLimitTypeDef(_RequiredFilesLimitTypeDef, _OptionalFilesLimitTypeDef):
    pass


FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Expression": str,
        "ValuesMap": Dict[str, str],
    },
)

FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "Json": "JsonOptionsTypeDef",
        "Excel": "ExcelOptionsTypeDef",
        "Csv": "CsvOptionsTypeDef",
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": "S3LocationTypeDef",
        "DataCatalogInputDefinition": "DataCatalogInputDefinitionTypeDef",
        "DatabaseInputDefinition": "DatabaseInputDefinitionTypeDef",
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)

JobSampleTypeDef = TypedDict(
    "JobSampleTypeDef",
    {
        "Mode": SampleModeType,
        "Size": int,
    },
    total=False,
)

_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef",
    {
        "Name": str,
    },
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Timeout": int,
        "Tags": Dict[str, str],
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


JsonOptionsTypeDef = TypedDict(
    "JsonOptionsTypeDef",
    {
        "MultiLine": bool,
    },
    total=False,
)

ListDatasetsRequestTypeDef = TypedDict(
    "ListDatasetsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDatasetsResponseResponseTypeDef = TypedDict(
    "ListDatasetsResponseResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobRunsRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListJobRunsRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListJobRunsRequestTypeDef(
    _RequiredListJobRunsRequestTypeDef, _OptionalListJobRunsRequestTypeDef
):
    pass


ListJobRunsResponseResponseTypeDef = TypedDict(
    "ListJobRunsResponseResponseTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestTypeDef = TypedDict(
    "ListJobsRequestTypeDef",
    {
        "DatasetName": str,
        "MaxResults": int,
        "NextToken": str,
        "ProjectName": str,
    },
    total=False,
)

ListJobsResponseResponseTypeDef = TypedDict(
    "ListJobsResponseResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestTypeDef = TypedDict(
    "ListProjectsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProjectsResponseResponseTypeDef = TypedDict(
    "ListProjectsResponseResponseTypeDef",
    {
        "Projects": List["ProjectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecipeVersionsRequestTypeDef = TypedDict(
    "_RequiredListRecipeVersionsRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListRecipeVersionsRequestTypeDef = TypedDict(
    "_OptionalListRecipeVersionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListRecipeVersionsRequestTypeDef(
    _RequiredListRecipeVersionsRequestTypeDef, _OptionalListRecipeVersionsRequestTypeDef
):
    pass


ListRecipeVersionsResponseResponseTypeDef = TypedDict(
    "ListRecipeVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Recipes": List["RecipeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesRequestTypeDef = TypedDict(
    "ListRecipesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "RecipeVersion": str,
    },
    total=False,
)

ListRecipesResponseResponseTypeDef = TypedDict(
    "ListRecipesResponseResponseTypeDef",
    {
        "Recipes": List["RecipeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulesRequestTypeDef = TypedDict(
    "ListSchedulesRequestTypeDef",
    {
        "JobName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSchedulesResponseResponseTypeDef = TypedDict(
    "ListSchedulesResponseResponseTypeDef",
    {
        "Schedules": List["ScheduleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef",
    {
        "Csv": "CsvOutputOptionsTypeDef",
    },
    total=False,
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Location": "S3LocationTypeDef",
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "CompressionFormat": CompressionFormatType,
        "Format": OutputFormatType,
        "PartitionColumns": List[str],
        "Overwrite": bool,
        "FormatOptions": "OutputFormatOptionsTypeDef",
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
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

PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": "FilterExpressionTypeDef",
        "FilesLimit": "FilesLimitTypeDef",
        "Parameters": Dict[str, "DatasetParameterTypeDef"],
    },
    total=False,
)

_RequiredProjectTypeDef = TypedDict(
    "_RequiredProjectTypeDef",
    {
        "Name": str,
        "RecipeName": str,
    },
)
_OptionalProjectTypeDef = TypedDict(
    "_OptionalProjectTypeDef",
    {
        "AccountId": str,
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "Tags": Dict[str, str],
        "RoleArn": str,
        "OpenedBy": str,
        "OpenDate": datetime,
    },
    total=False,
)


class ProjectTypeDef(_RequiredProjectTypeDef, _OptionalProjectTypeDef):
    pass


_RequiredPublishRecipeRequestTypeDef = TypedDict(
    "_RequiredPublishRecipeRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalPublishRecipeRequestTypeDef = TypedDict(
    "_OptionalPublishRecipeRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class PublishRecipeRequestTypeDef(
    _RequiredPublishRecipeRequestTypeDef, _OptionalPublishRecipeRequestTypeDef
):
    pass


PublishRecipeResponseResponseTypeDef = TypedDict(
    "PublishRecipeResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecipeActionTypeDef = TypedDict(
    "_RequiredRecipeActionTypeDef",
    {
        "Operation": str,
    },
)
_OptionalRecipeActionTypeDef = TypedDict(
    "_OptionalRecipeActionTypeDef",
    {
        "Parameters": Dict[str, str],
    },
    total=False,
)


class RecipeActionTypeDef(_RequiredRecipeActionTypeDef, _OptionalRecipeActionTypeDef):
    pass


_RequiredRecipeReferenceTypeDef = TypedDict(
    "_RequiredRecipeReferenceTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeReferenceTypeDef = TypedDict(
    "_OptionalRecipeReferenceTypeDef",
    {
        "RecipeVersion": str,
    },
    total=False,
)


class RecipeReferenceTypeDef(_RequiredRecipeReferenceTypeDef, _OptionalRecipeReferenceTypeDef):
    pass


_RequiredRecipeStepTypeDef = TypedDict(
    "_RequiredRecipeStepTypeDef",
    {
        "Action": "RecipeActionTypeDef",
    },
)
_OptionalRecipeStepTypeDef = TypedDict(
    "_OptionalRecipeStepTypeDef",
    {
        "ConditionExpressions": List["ConditionExpressionTypeDef"],
    },
    total=False,
)


class RecipeStepTypeDef(_RequiredRecipeStepTypeDef, _OptionalRecipeStepTypeDef):
    pass


_RequiredRecipeTypeDef = TypedDict(
    "_RequiredRecipeTypeDef",
    {
        "Name": str,
    },
)
_OptionalRecipeTypeDef = TypedDict(
    "_OptionalRecipeTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "ResourceArn": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "RecipeVersion": str,
    },
    total=False,
)


class RecipeTypeDef(_RequiredRecipeTypeDef, _OptionalRecipeTypeDef):
    pass


RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "RecipeVersion": str,
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

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Key": str,
    },
    total=False,
)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


_RequiredSampleTypeDef = TypedDict(
    "_RequiredSampleTypeDef",
    {
        "Type": SampleTypeType,
    },
)
_OptionalSampleTypeDef = TypedDict(
    "_OptionalSampleTypeDef",
    {
        "Size": int,
    },
    total=False,
)


class SampleTypeDef(_RequiredSampleTypeDef, _OptionalSampleTypeDef):
    pass


_RequiredScheduleTypeDef = TypedDict(
    "_RequiredScheduleTypeDef",
    {
        "Name": str,
    },
)
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass


_RequiredSendProjectSessionActionRequestTypeDef = TypedDict(
    "_RequiredSendProjectSessionActionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalSendProjectSessionActionRequestTypeDef = TypedDict(
    "_OptionalSendProjectSessionActionRequestTypeDef",
    {
        "Preview": bool,
        "RecipeStep": "RecipeStepTypeDef",
        "StepIndex": int,
        "ClientSessionId": str,
        "ViewFrame": "ViewFrameTypeDef",
    },
    total=False,
)


class SendProjectSessionActionRequestTypeDef(
    _RequiredSendProjectSessionActionRequestTypeDef, _OptionalSendProjectSessionActionRequestTypeDef
):
    pass


SendProjectSessionActionResponseResponseTypeDef = TypedDict(
    "SendProjectSessionActionResponseResponseTypeDef",
    {
        "Result": str,
        "Name": str,
        "ActionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRunRequestTypeDef = TypedDict(
    "StartJobRunRequestTypeDef",
    {
        "Name": str,
    },
)

StartJobRunResponseResponseTypeDef = TypedDict(
    "StartJobRunResponseResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartProjectSessionRequestTypeDef = TypedDict(
    "_RequiredStartProjectSessionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartProjectSessionRequestTypeDef = TypedDict(
    "_OptionalStartProjectSessionRequestTypeDef",
    {
        "AssumeControl": bool,
    },
    total=False,
)


class StartProjectSessionRequestTypeDef(
    _RequiredStartProjectSessionRequestTypeDef, _OptionalStartProjectSessionRequestTypeDef
):
    pass


StartProjectSessionResponseResponseTypeDef = TypedDict(
    "StartProjectSessionResponseResponseTypeDef",
    {
        "Name": str,
        "ClientSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopJobRunRequestTypeDef = TypedDict(
    "StopJobRunRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StopJobRunResponseResponseTypeDef = TypedDict(
    "StopJobRunResponseResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDatasetRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
    },
)
_OptionalUpdateDatasetRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestTypeDef",
    {
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "PathOptions": "PathOptionsTypeDef",
    },
    total=False,
)


class UpdateDatasetRequestTypeDef(
    _RequiredUpdateDatasetRequestTypeDef, _OptionalUpdateDatasetRequestTypeDef
):
    pass


UpdateDatasetResponseResponseTypeDef = TypedDict(
    "UpdateDatasetResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProfileJobRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileJobRequestTypeDef",
    {
        "Name": str,
        "OutputLocation": "S3LocationTypeDef",
        "RoleArn": str,
    },
)
_OptionalUpdateProfileJobRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileJobRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class UpdateProfileJobRequestTypeDef(
    _RequiredUpdateProfileJobRequestTypeDef, _OptionalUpdateProfileJobRequestTypeDef
):
    pass


UpdateProfileJobResponseResponseTypeDef = TypedDict(
    "UpdateProfileJobResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestTypeDef",
    {
        "RoleArn": str,
        "Name": str,
    },
)
_OptionalUpdateProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestTypeDef",
    {
        "Sample": "SampleTypeDef",
    },
    total=False,
)


class UpdateProjectRequestTypeDef(
    _RequiredUpdateProjectRequestTypeDef, _OptionalUpdateProjectRequestTypeDef
):
    pass


UpdateProjectResponseResponseTypeDef = TypedDict(
    "UpdateProjectResponseResponseTypeDef",
    {
        "LastModifiedDate": datetime,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRecipeJobRequestTypeDef = TypedDict(
    "_RequiredUpdateRecipeJobRequestTypeDef",
    {
        "Name": str,
        "Outputs": List["OutputTypeDef"],
        "RoleArn": str,
    },
)
_OptionalUpdateRecipeJobRequestTypeDef = TypedDict(
    "_OptionalUpdateRecipeJobRequestTypeDef",
    {
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Timeout": int,
    },
    total=False,
)


class UpdateRecipeJobRequestTypeDef(
    _RequiredUpdateRecipeJobRequestTypeDef, _OptionalUpdateRecipeJobRequestTypeDef
):
    pass


UpdateRecipeJobResponseResponseTypeDef = TypedDict(
    "UpdateRecipeJobResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRecipeRequestTypeDef = TypedDict(
    "_RequiredUpdateRecipeRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateRecipeRequestTypeDef = TypedDict(
    "_OptionalUpdateRecipeRequestTypeDef",
    {
        "Description": str,
        "Steps": List["RecipeStepTypeDef"],
    },
    total=False,
)


class UpdateRecipeRequestTypeDef(
    _RequiredUpdateRecipeRequestTypeDef, _OptionalUpdateRecipeRequestTypeDef
):
    pass


UpdateRecipeResponseResponseTypeDef = TypedDict(
    "UpdateRecipeResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScheduleRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduleRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
    },
)
_OptionalUpdateScheduleRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduleRequestTypeDef",
    {
        "JobNames": List[str],
    },
    total=False,
)


class UpdateScheduleRequestTypeDef(
    _RequiredUpdateScheduleRequestTypeDef, _OptionalUpdateScheduleRequestTypeDef
):
    pass


UpdateScheduleResponseResponseTypeDef = TypedDict(
    "UpdateScheduleResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredViewFrameTypeDef = TypedDict(
    "_RequiredViewFrameTypeDef",
    {
        "StartColumnIndex": int,
    },
)
_OptionalViewFrameTypeDef = TypedDict(
    "_OptionalViewFrameTypeDef",
    {
        "ColumnRange": int,
        "HiddenColumns": List[str],
    },
    total=False,
)


class ViewFrameTypeDef(_RequiredViewFrameTypeDef, _OptionalViewFrameTypeDef):
    pass
