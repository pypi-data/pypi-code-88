"""
Type annotations for personalize service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize.type_defs import AlgorithmImageTypeDef

    data: AlgorithmImageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import IngestionModeType, ObjectiveSensitivityType, TrainingModeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlgorithmImageTypeDef",
    "AlgorithmTypeDef",
    "AutoMLConfigTypeDef",
    "AutoMLResultTypeDef",
    "BatchInferenceJobConfigTypeDef",
    "BatchInferenceJobInputTypeDef",
    "BatchInferenceJobOutputTypeDef",
    "BatchInferenceJobSummaryTypeDef",
    "BatchInferenceJobTypeDef",
    "CampaignConfigTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CampaignUpdateSummaryTypeDef",
    "CategoricalHyperParameterRangeTypeDef",
    "ContinuousHyperParameterRangeTypeDef",
    "CreateBatchInferenceJobRequestTypeDef",
    "CreateBatchInferenceJobResponseResponseTypeDef",
    "CreateCampaignRequestTypeDef",
    "CreateCampaignResponseResponseTypeDef",
    "CreateDatasetExportJobRequestTypeDef",
    "CreateDatasetExportJobResponseResponseTypeDef",
    "CreateDatasetGroupRequestTypeDef",
    "CreateDatasetGroupResponseResponseTypeDef",
    "CreateDatasetImportJobRequestTypeDef",
    "CreateDatasetImportJobResponseResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseResponseTypeDef",
    "CreateEventTrackerRequestTypeDef",
    "CreateEventTrackerResponseResponseTypeDef",
    "CreateFilterRequestTypeDef",
    "CreateFilterResponseResponseTypeDef",
    "CreateSchemaRequestTypeDef",
    "CreateSchemaResponseResponseTypeDef",
    "CreateSolutionRequestTypeDef",
    "CreateSolutionResponseResponseTypeDef",
    "CreateSolutionVersionRequestTypeDef",
    "CreateSolutionVersionResponseResponseTypeDef",
    "DataSourceTypeDef",
    "DatasetExportJobOutputTypeDef",
    "DatasetExportJobSummaryTypeDef",
    "DatasetExportJobTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetGroupTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetImportJobTypeDef",
    "DatasetSchemaSummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTypeDef",
    "DefaultCategoricalHyperParameterRangeTypeDef",
    "DefaultContinuousHyperParameterRangeTypeDef",
    "DefaultHyperParameterRangesTypeDef",
    "DefaultIntegerHyperParameterRangeTypeDef",
    "DeleteCampaignRequestTypeDef",
    "DeleteDatasetGroupRequestTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteEventTrackerRequestTypeDef",
    "DeleteFilterRequestTypeDef",
    "DeleteSchemaRequestTypeDef",
    "DeleteSolutionRequestTypeDef",
    "DescribeAlgorithmRequestTypeDef",
    "DescribeAlgorithmResponseResponseTypeDef",
    "DescribeBatchInferenceJobRequestTypeDef",
    "DescribeBatchInferenceJobResponseResponseTypeDef",
    "DescribeCampaignRequestTypeDef",
    "DescribeCampaignResponseResponseTypeDef",
    "DescribeDatasetExportJobRequestTypeDef",
    "DescribeDatasetExportJobResponseResponseTypeDef",
    "DescribeDatasetGroupRequestTypeDef",
    "DescribeDatasetGroupResponseResponseTypeDef",
    "DescribeDatasetImportJobRequestTypeDef",
    "DescribeDatasetImportJobResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeEventTrackerRequestTypeDef",
    "DescribeEventTrackerResponseResponseTypeDef",
    "DescribeFeatureTransformationRequestTypeDef",
    "DescribeFeatureTransformationResponseResponseTypeDef",
    "DescribeFilterRequestTypeDef",
    "DescribeFilterResponseResponseTypeDef",
    "DescribeRecipeRequestTypeDef",
    "DescribeRecipeResponseResponseTypeDef",
    "DescribeSchemaRequestTypeDef",
    "DescribeSchemaResponseResponseTypeDef",
    "DescribeSolutionRequestTypeDef",
    "DescribeSolutionResponseResponseTypeDef",
    "DescribeSolutionVersionRequestTypeDef",
    "DescribeSolutionVersionResponseResponseTypeDef",
    "EventTrackerSummaryTypeDef",
    "EventTrackerTypeDef",
    "FeatureTransformationTypeDef",
    "FilterSummaryTypeDef",
    "FilterTypeDef",
    "GetSolutionMetricsRequestTypeDef",
    "GetSolutionMetricsResponseResponseTypeDef",
    "HPOConfigTypeDef",
    "HPOObjectiveTypeDef",
    "HPOResourceConfigTypeDef",
    "HyperParameterRangesTypeDef",
    "IntegerHyperParameterRangeTypeDef",
    "ListBatchInferenceJobsRequestTypeDef",
    "ListBatchInferenceJobsResponseResponseTypeDef",
    "ListCampaignsRequestTypeDef",
    "ListCampaignsResponseResponseTypeDef",
    "ListDatasetExportJobsRequestTypeDef",
    "ListDatasetExportJobsResponseResponseTypeDef",
    "ListDatasetGroupsRequestTypeDef",
    "ListDatasetGroupsResponseResponseTypeDef",
    "ListDatasetImportJobsRequestTypeDef",
    "ListDatasetImportJobsResponseResponseTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseResponseTypeDef",
    "ListEventTrackersRequestTypeDef",
    "ListEventTrackersResponseResponseTypeDef",
    "ListFiltersRequestTypeDef",
    "ListFiltersResponseResponseTypeDef",
    "ListRecipesRequestTypeDef",
    "ListRecipesResponseResponseTypeDef",
    "ListSchemasRequestTypeDef",
    "ListSchemasResponseResponseTypeDef",
    "ListSolutionVersionsRequestTypeDef",
    "ListSolutionVersionsResponseResponseTypeDef",
    "ListSolutionsRequestTypeDef",
    "ListSolutionsResponseResponseTypeDef",
    "OptimizationObjectiveTypeDef",
    "PaginatorConfigTypeDef",
    "RecipeSummaryTypeDef",
    "RecipeTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataConfigTypeDef",
    "SolutionConfigTypeDef",
    "SolutionSummaryTypeDef",
    "SolutionTypeDef",
    "SolutionVersionSummaryTypeDef",
    "SolutionVersionTypeDef",
    "StopSolutionVersionCreationRequestTypeDef",
    "TunedHPOParamsTypeDef",
    "UpdateCampaignRequestTypeDef",
    "UpdateCampaignResponseResponseTypeDef",
)

_RequiredAlgorithmImageTypeDef = TypedDict(
    "_RequiredAlgorithmImageTypeDef",
    {
        "dockerURI": str,
    },
)
_OptionalAlgorithmImageTypeDef = TypedDict(
    "_OptionalAlgorithmImageTypeDef",
    {
        "name": str,
    },
    total=False,
)


class AlgorithmImageTypeDef(_RequiredAlgorithmImageTypeDef, _OptionalAlgorithmImageTypeDef):
    pass


AlgorithmTypeDef = TypedDict(
    "AlgorithmTypeDef",
    {
        "name": str,
        "algorithmArn": str,
        "algorithmImage": "AlgorithmImageTypeDef",
        "defaultHyperParameters": Dict[str, str],
        "defaultHyperParameterRanges": "DefaultHyperParameterRangesTypeDef",
        "defaultResourceConfig": Dict[str, str],
        "trainingInputMode": str,
        "roleArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

AutoMLConfigTypeDef = TypedDict(
    "AutoMLConfigTypeDef",
    {
        "metricName": str,
        "recipeList": List[str],
    },
    total=False,
)

AutoMLResultTypeDef = TypedDict(
    "AutoMLResultTypeDef",
    {
        "bestRecipeArn": str,
    },
    total=False,
)

BatchInferenceJobConfigTypeDef = TypedDict(
    "BatchInferenceJobConfigTypeDef",
    {
        "itemExplorationConfig": Dict[str, str],
    },
    total=False,
)

BatchInferenceJobInputTypeDef = TypedDict(
    "BatchInferenceJobInputTypeDef",
    {
        "s3DataSource": "S3DataConfigTypeDef",
    },
)

BatchInferenceJobOutputTypeDef = TypedDict(
    "BatchInferenceJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

BatchInferenceJobSummaryTypeDef = TypedDict(
    "BatchInferenceJobSummaryTypeDef",
    {
        "batchInferenceJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
        "solutionVersionArn": str,
    },
    total=False,
)

BatchInferenceJobTypeDef = TypedDict(
    "BatchInferenceJobTypeDef",
    {
        "jobName": str,
        "batchInferenceJobArn": str,
        "filterArn": str,
        "failureReason": str,
        "solutionVersionArn": str,
        "numResults": int,
        "jobInput": "BatchInferenceJobInputTypeDef",
        "jobOutput": "BatchInferenceJobOutputTypeDef",
        "batchInferenceJobConfig": "BatchInferenceJobConfigTypeDef",
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

CampaignConfigTypeDef = TypedDict(
    "CampaignConfigTypeDef",
    {
        "itemExplorationConfig": Dict[str, str],
    },
    total=False,
)

CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "name": str,
        "campaignArn": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestCampaignUpdate": "CampaignUpdateSummaryTypeDef",
    },
    total=False,
)

CampaignUpdateSummaryTypeDef = TypedDict(
    "CampaignUpdateSummaryTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

CategoricalHyperParameterRangeTypeDef = TypedDict(
    "CategoricalHyperParameterRangeTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

ContinuousHyperParameterRangeTypeDef = TypedDict(
    "ContinuousHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": float,
        "maxValue": float,
    },
    total=False,
)

_RequiredCreateBatchInferenceJobRequestTypeDef = TypedDict(
    "_RequiredCreateBatchInferenceJobRequestTypeDef",
    {
        "jobName": str,
        "solutionVersionArn": str,
        "jobInput": "BatchInferenceJobInputTypeDef",
        "jobOutput": "BatchInferenceJobOutputTypeDef",
        "roleArn": str,
    },
)
_OptionalCreateBatchInferenceJobRequestTypeDef = TypedDict(
    "_OptionalCreateBatchInferenceJobRequestTypeDef",
    {
        "filterArn": str,
        "numResults": int,
        "batchInferenceJobConfig": "BatchInferenceJobConfigTypeDef",
    },
    total=False,
)


class CreateBatchInferenceJobRequestTypeDef(
    _RequiredCreateBatchInferenceJobRequestTypeDef, _OptionalCreateBatchInferenceJobRequestTypeDef
):
    pass


CreateBatchInferenceJobResponseResponseTypeDef = TypedDict(
    "CreateBatchInferenceJobResponseResponseTypeDef",
    {
        "batchInferenceJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCampaignRequestTypeDef = TypedDict(
    "_RequiredCreateCampaignRequestTypeDef",
    {
        "name": str,
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
    },
)
_OptionalCreateCampaignRequestTypeDef = TypedDict(
    "_OptionalCreateCampaignRequestTypeDef",
    {
        "campaignConfig": "CampaignConfigTypeDef",
    },
    total=False,
)


class CreateCampaignRequestTypeDef(
    _RequiredCreateCampaignRequestTypeDef, _OptionalCreateCampaignRequestTypeDef
):
    pass


CreateCampaignResponseResponseTypeDef = TypedDict(
    "CreateCampaignResponseResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetExportJobRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetExportJobRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "roleArn": str,
        "jobOutput": "DatasetExportJobOutputTypeDef",
    },
)
_OptionalCreateDatasetExportJobRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetExportJobRequestTypeDef",
    {
        "ingestionMode": IngestionModeType,
    },
    total=False,
)


class CreateDatasetExportJobRequestTypeDef(
    _RequiredCreateDatasetExportJobRequestTypeDef, _OptionalCreateDatasetExportJobRequestTypeDef
):
    pass


CreateDatasetExportJobResponseResponseTypeDef = TypedDict(
    "CreateDatasetExportJobResponseResponseTypeDef",
    {
        "datasetExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetGroupRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetGroupRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateDatasetGroupRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetGroupRequestTypeDef",
    {
        "roleArn": str,
        "kmsKeyArn": str,
    },
    total=False,
)


class CreateDatasetGroupRequestTypeDef(
    _RequiredCreateDatasetGroupRequestTypeDef, _OptionalCreateDatasetGroupRequestTypeDef
):
    pass


CreateDatasetGroupResponseResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseResponseTypeDef",
    {
        "datasetGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetImportJobRequestTypeDef = TypedDict(
    "CreateDatasetImportJobRequestTypeDef",
    {
        "jobName": str,
        "datasetArn": str,
        "dataSource": "DataSourceTypeDef",
        "roleArn": str,
    },
)

CreateDatasetImportJobResponseResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseResponseTypeDef",
    {
        "datasetImportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatasetRequestTypeDef = TypedDict(
    "CreateDatasetRequestTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
    },
)

CreateDatasetResponseResponseTypeDef = TypedDict(
    "CreateDatasetResponseResponseTypeDef",
    {
        "datasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventTrackerRequestTypeDef = TypedDict(
    "CreateEventTrackerRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
    },
)

CreateEventTrackerResponseResponseTypeDef = TypedDict(
    "CreateEventTrackerResponseResponseTypeDef",
    {
        "eventTrackerArn": str,
        "trackingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFilterRequestTypeDef = TypedDict(
    "CreateFilterRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "filterExpression": str,
    },
)

CreateFilterResponseResponseTypeDef = TypedDict(
    "CreateFilterResponseResponseTypeDef",
    {
        "filterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestTypeDef = TypedDict(
    "CreateSchemaRequestTypeDef",
    {
        "name": str,
        "schema": str,
    },
)

CreateSchemaResponseResponseTypeDef = TypedDict(
    "CreateSchemaResponseResponseTypeDef",
    {
        "schemaArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSolutionRequestTypeDef = TypedDict(
    "_RequiredCreateSolutionRequestTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
    },
)
_OptionalCreateSolutionRequestTypeDef = TypedDict(
    "_OptionalCreateSolutionRequestTypeDef",
    {
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "solutionConfig": "SolutionConfigTypeDef",
    },
    total=False,
)


class CreateSolutionRequestTypeDef(
    _RequiredCreateSolutionRequestTypeDef, _OptionalCreateSolutionRequestTypeDef
):
    pass


CreateSolutionResponseResponseTypeDef = TypedDict(
    "CreateSolutionResponseResponseTypeDef",
    {
        "solutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSolutionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateSolutionVersionRequestTypeDef",
    {
        "solutionArn": str,
    },
)
_OptionalCreateSolutionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateSolutionVersionRequestTypeDef",
    {
        "trainingMode": TrainingModeType,
    },
    total=False,
)


class CreateSolutionVersionRequestTypeDef(
    _RequiredCreateSolutionVersionRequestTypeDef, _OptionalCreateSolutionVersionRequestTypeDef
):
    pass


CreateSolutionVersionResponseResponseTypeDef = TypedDict(
    "CreateSolutionVersionResponseResponseTypeDef",
    {
        "solutionVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataLocation": str,
    },
    total=False,
)

DatasetExportJobOutputTypeDef = TypedDict(
    "DatasetExportJobOutputTypeDef",
    {
        "s3DataDestination": "S3DataConfigTypeDef",
    },
)

DatasetExportJobSummaryTypeDef = TypedDict(
    "DatasetExportJobSummaryTypeDef",
    {
        "datasetExportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetExportJobTypeDef = TypedDict(
    "DatasetExportJobTypeDef",
    {
        "jobName": str,
        "datasetExportJobArn": str,
        "datasetArn": str,
        "ingestionMode": IngestionModeType,
        "roleArn": str,
        "status": str,
        "jobOutput": "DatasetExportJobOutputTypeDef",
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetGroupTypeDef = TypedDict(
    "DatasetGroupTypeDef",
    {
        "name": str,
        "datasetGroupArn": str,
        "status": str,
        "roleArn": str,
        "kmsKeyArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "datasetImportJobArn": str,
        "jobName": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetImportJobTypeDef = TypedDict(
    "DatasetImportJobTypeDef",
    {
        "jobName": str,
        "datasetImportJobArn": str,
        "datasetArn": str,
        "dataSource": "DataSourceTypeDef",
        "roleArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

DatasetSchemaSummaryTypeDef = TypedDict(
    "DatasetSchemaSummaryTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "name": str,
        "schemaArn": str,
        "schema": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetType": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": str,
        "datasetArn": str,
        "datasetGroupArn": str,
        "datasetType": str,
        "schemaArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DefaultCategoricalHyperParameterRangeTypeDef = TypedDict(
    "DefaultCategoricalHyperParameterRangeTypeDef",
    {
        "name": str,
        "values": List[str],
        "isTunable": bool,
    },
    total=False,
)

DefaultContinuousHyperParameterRangeTypeDef = TypedDict(
    "DefaultContinuousHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": float,
        "maxValue": float,
        "isTunable": bool,
    },
    total=False,
)

DefaultHyperParameterRangesTypeDef = TypedDict(
    "DefaultHyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List["DefaultIntegerHyperParameterRangeTypeDef"],
        "continuousHyperParameterRanges": List["DefaultContinuousHyperParameterRangeTypeDef"],
        "categoricalHyperParameterRanges": List["DefaultCategoricalHyperParameterRangeTypeDef"],
    },
    total=False,
)

DefaultIntegerHyperParameterRangeTypeDef = TypedDict(
    "DefaultIntegerHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": int,
        "maxValue": int,
        "isTunable": bool,
    },
    total=False,
)

DeleteCampaignRequestTypeDef = TypedDict(
    "DeleteCampaignRequestTypeDef",
    {
        "campaignArn": str,
    },
)

DeleteDatasetGroupRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)

DeleteDatasetRequestTypeDef = TypedDict(
    "DeleteDatasetRequestTypeDef",
    {
        "datasetArn": str,
    },
)

DeleteEventTrackerRequestTypeDef = TypedDict(
    "DeleteEventTrackerRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)

DeleteFilterRequestTypeDef = TypedDict(
    "DeleteFilterRequestTypeDef",
    {
        "filterArn": str,
    },
)

DeleteSchemaRequestTypeDef = TypedDict(
    "DeleteSchemaRequestTypeDef",
    {
        "schemaArn": str,
    },
)

DeleteSolutionRequestTypeDef = TypedDict(
    "DeleteSolutionRequestTypeDef",
    {
        "solutionArn": str,
    },
)

DescribeAlgorithmRequestTypeDef = TypedDict(
    "DescribeAlgorithmRequestTypeDef",
    {
        "algorithmArn": str,
    },
)

DescribeAlgorithmResponseResponseTypeDef = TypedDict(
    "DescribeAlgorithmResponseResponseTypeDef",
    {
        "algorithm": "AlgorithmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchInferenceJobRequestTypeDef = TypedDict(
    "DescribeBatchInferenceJobRequestTypeDef",
    {
        "batchInferenceJobArn": str,
    },
)

DescribeBatchInferenceJobResponseResponseTypeDef = TypedDict(
    "DescribeBatchInferenceJobResponseResponseTypeDef",
    {
        "batchInferenceJob": "BatchInferenceJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCampaignRequestTypeDef = TypedDict(
    "DescribeCampaignRequestTypeDef",
    {
        "campaignArn": str,
    },
)

DescribeCampaignResponseResponseTypeDef = TypedDict(
    "DescribeCampaignResponseResponseTypeDef",
    {
        "campaign": "CampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetExportJobRequestTypeDef = TypedDict(
    "DescribeDatasetExportJobRequestTypeDef",
    {
        "datasetExportJobArn": str,
    },
)

DescribeDatasetExportJobResponseResponseTypeDef = TypedDict(
    "DescribeDatasetExportJobResponseResponseTypeDef",
    {
        "datasetExportJob": "DatasetExportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetGroupRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestTypeDef",
    {
        "datasetGroupArn": str,
    },
)

DescribeDatasetGroupResponseResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseResponseTypeDef",
    {
        "datasetGroup": "DatasetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetImportJobRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestTypeDef",
    {
        "datasetImportJobArn": str,
    },
)

DescribeDatasetImportJobResponseResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseResponseTypeDef",
    {
        "datasetImportJob": "DatasetImportJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "datasetArn": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "dataset": "DatasetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventTrackerRequestTypeDef = TypedDict(
    "DescribeEventTrackerRequestTypeDef",
    {
        "eventTrackerArn": str,
    },
)

DescribeEventTrackerResponseResponseTypeDef = TypedDict(
    "DescribeEventTrackerResponseResponseTypeDef",
    {
        "eventTracker": "EventTrackerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeatureTransformationRequestTypeDef = TypedDict(
    "DescribeFeatureTransformationRequestTypeDef",
    {
        "featureTransformationArn": str,
    },
)

DescribeFeatureTransformationResponseResponseTypeDef = TypedDict(
    "DescribeFeatureTransformationResponseResponseTypeDef",
    {
        "featureTransformation": "FeatureTransformationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFilterRequestTypeDef = TypedDict(
    "DescribeFilterRequestTypeDef",
    {
        "filterArn": str,
    },
)

DescribeFilterResponseResponseTypeDef = TypedDict(
    "DescribeFilterResponseResponseTypeDef",
    {
        "filter": "FilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecipeRequestTypeDef = TypedDict(
    "DescribeRecipeRequestTypeDef",
    {
        "recipeArn": str,
    },
)

DescribeRecipeResponseResponseTypeDef = TypedDict(
    "DescribeRecipeResponseResponseTypeDef",
    {
        "recipe": "RecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchemaRequestTypeDef = TypedDict(
    "DescribeSchemaRequestTypeDef",
    {
        "schemaArn": str,
    },
)

DescribeSchemaResponseResponseTypeDef = TypedDict(
    "DescribeSchemaResponseResponseTypeDef",
    {
        "schema": "DatasetSchemaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSolutionRequestTypeDef = TypedDict(
    "DescribeSolutionRequestTypeDef",
    {
        "solutionArn": str,
    },
)

DescribeSolutionResponseResponseTypeDef = TypedDict(
    "DescribeSolutionResponseResponseTypeDef",
    {
        "solution": "SolutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSolutionVersionRequestTypeDef = TypedDict(
    "DescribeSolutionVersionRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

DescribeSolutionVersionResponseResponseTypeDef = TypedDict(
    "DescribeSolutionVersionResponseResponseTypeDef",
    {
        "solutionVersion": "SolutionVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTrackerSummaryTypeDef = TypedDict(
    "EventTrackerSummaryTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

EventTrackerTypeDef = TypedDict(
    "EventTrackerTypeDef",
    {
        "name": str,
        "eventTrackerArn": str,
        "accountId": str,
        "trackingId": str,
        "datasetGroupArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

FeatureTransformationTypeDef = TypedDict(
    "FeatureTransformationTypeDef",
    {
        "name": str,
        "featureTransformationArn": str,
        "defaultParameters": Dict[str, str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "status": str,
    },
    total=False,
)

FilterSummaryTypeDef = TypedDict(
    "FilterSummaryTypeDef",
    {
        "name": str,
        "filterArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "datasetGroupArn": str,
        "failureReason": str,
        "status": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "filterArn": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "datasetGroupArn": str,
        "failureReason": str,
        "filterExpression": str,
        "status": str,
    },
    total=False,
)

GetSolutionMetricsRequestTypeDef = TypedDict(
    "GetSolutionMetricsRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

GetSolutionMetricsResponseResponseTypeDef = TypedDict(
    "GetSolutionMetricsResponseResponseTypeDef",
    {
        "solutionVersionArn": str,
        "metrics": Dict[str, float],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HPOConfigTypeDef = TypedDict(
    "HPOConfigTypeDef",
    {
        "hpoObjective": "HPOObjectiveTypeDef",
        "hpoResourceConfig": "HPOResourceConfigTypeDef",
        "algorithmHyperParameterRanges": "HyperParameterRangesTypeDef",
    },
    total=False,
)

HPOObjectiveTypeDef = TypedDict(
    "HPOObjectiveTypeDef",
    {
        "type": str,
        "metricName": str,
        "metricRegex": str,
    },
    total=False,
)

HPOResourceConfigTypeDef = TypedDict(
    "HPOResourceConfigTypeDef",
    {
        "maxNumberOfTrainingJobs": str,
        "maxParallelTrainingJobs": str,
    },
    total=False,
)

HyperParameterRangesTypeDef = TypedDict(
    "HyperParameterRangesTypeDef",
    {
        "integerHyperParameterRanges": List["IntegerHyperParameterRangeTypeDef"],
        "continuousHyperParameterRanges": List["ContinuousHyperParameterRangeTypeDef"],
        "categoricalHyperParameterRanges": List["CategoricalHyperParameterRangeTypeDef"],
    },
    total=False,
)

IntegerHyperParameterRangeTypeDef = TypedDict(
    "IntegerHyperParameterRangeTypeDef",
    {
        "name": str,
        "minValue": int,
        "maxValue": int,
    },
    total=False,
)

ListBatchInferenceJobsRequestTypeDef = TypedDict(
    "ListBatchInferenceJobsRequestTypeDef",
    {
        "solutionVersionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListBatchInferenceJobsResponseResponseTypeDef = TypedDict(
    "ListBatchInferenceJobsResponseResponseTypeDef",
    {
        "batchInferenceJobs": List["BatchInferenceJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCampaignsRequestTypeDef = TypedDict(
    "ListCampaignsRequestTypeDef",
    {
        "solutionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCampaignsResponseResponseTypeDef = TypedDict(
    "ListCampaignsResponseResponseTypeDef",
    {
        "campaigns": List["CampaignSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetExportJobsRequestTypeDef = TypedDict(
    "ListDatasetExportJobsRequestTypeDef",
    {
        "datasetArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetExportJobsResponseResponseTypeDef = TypedDict(
    "ListDatasetExportJobsResponseResponseTypeDef",
    {
        "datasetExportJobs": List["DatasetExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetGroupsRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetGroupsResponseResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseResponseTypeDef",
    {
        "datasetGroups": List["DatasetGroupSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetImportJobsRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestTypeDef",
    {
        "datasetArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetImportJobsResponseResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseResponseTypeDef",
    {
        "datasetImportJobs": List["DatasetImportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestTypeDef = TypedDict(
    "ListDatasetsRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDatasetsResponseResponseTypeDef = TypedDict(
    "ListDatasetsResponseResponseTypeDef",
    {
        "datasets": List["DatasetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventTrackersRequestTypeDef = TypedDict(
    "ListEventTrackersRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEventTrackersResponseResponseTypeDef = TypedDict(
    "ListEventTrackersResponseResponseTypeDef",
    {
        "eventTrackers": List["EventTrackerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFiltersRequestTypeDef = TypedDict(
    "ListFiltersRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListFiltersResponseResponseTypeDef = TypedDict(
    "ListFiltersResponseResponseTypeDef",
    {
        "Filters": List["FilterSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesRequestTypeDef = TypedDict(
    "ListRecipesRequestTypeDef",
    {
        "recipeProvider": Literal["SERVICE"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListRecipesResponseResponseTypeDef = TypedDict(
    "ListRecipesResponseResponseTypeDef",
    {
        "recipes": List["RecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasRequestTypeDef = TypedDict(
    "ListSchemasRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSchemasResponseResponseTypeDef = TypedDict(
    "ListSchemasResponseResponseTypeDef",
    {
        "schemas": List["DatasetSchemaSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolutionVersionsRequestTypeDef = TypedDict(
    "ListSolutionVersionsRequestTypeDef",
    {
        "solutionArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSolutionVersionsResponseResponseTypeDef = TypedDict(
    "ListSolutionVersionsResponseResponseTypeDef",
    {
        "solutionVersions": List["SolutionVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolutionsRequestTypeDef = TypedDict(
    "ListSolutionsRequestTypeDef",
    {
        "datasetGroupArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSolutionsResponseResponseTypeDef = TypedDict(
    "ListSolutionsResponseResponseTypeDef",
    {
        "solutions": List["SolutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptimizationObjectiveTypeDef = TypedDict(
    "OptimizationObjectiveTypeDef",
    {
        "itemAttribute": str,
        "objectiveSensitivity": ObjectiveSensitivityType,
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

RecipeSummaryTypeDef = TypedDict(
    "RecipeSummaryTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "name": str,
        "recipeArn": str,
        "algorithmArn": str,
        "featureTransformationArn": str,
        "status": str,
        "description": str,
        "creationDateTime": datetime,
        "recipeType": str,
        "lastUpdatedDateTime": datetime,
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

_RequiredS3DataConfigTypeDef = TypedDict(
    "_RequiredS3DataConfigTypeDef",
    {
        "path": str,
    },
)
_OptionalS3DataConfigTypeDef = TypedDict(
    "_OptionalS3DataConfigTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class S3DataConfigTypeDef(_RequiredS3DataConfigTypeDef, _OptionalS3DataConfigTypeDef):
    pass


SolutionConfigTypeDef = TypedDict(
    "SolutionConfigTypeDef",
    {
        "eventValueThreshold": str,
        "hpoConfig": "HPOConfigTypeDef",
        "algorithmHyperParameters": Dict[str, str],
        "featureTransformationParameters": Dict[str, str],
        "autoMLConfig": "AutoMLConfigTypeDef",
        "optimizationObjective": "OptimizationObjectiveTypeDef",
    },
    total=False,
)

SolutionSummaryTypeDef = TypedDict(
    "SolutionSummaryTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

SolutionTypeDef = TypedDict(
    "SolutionTypeDef",
    {
        "name": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "datasetGroupArn": str,
        "eventType": str,
        "solutionConfig": "SolutionConfigTypeDef",
        "autoMLResult": "AutoMLResultTypeDef",
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "latestSolutionVersion": "SolutionVersionSummaryTypeDef",
    },
    total=False,
)

SolutionVersionSummaryTypeDef = TypedDict(
    "SolutionVersionSummaryTypeDef",
    {
        "solutionVersionArn": str,
        "status": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "failureReason": str,
    },
    total=False,
)

SolutionVersionTypeDef = TypedDict(
    "SolutionVersionTypeDef",
    {
        "solutionVersionArn": str,
        "solutionArn": str,
        "performHPO": bool,
        "performAutoML": bool,
        "recipeArn": str,
        "eventType": str,
        "datasetGroupArn": str,
        "solutionConfig": "SolutionConfigTypeDef",
        "trainingHours": float,
        "trainingMode": TrainingModeType,
        "tunedHPOParams": "TunedHPOParamsTypeDef",
        "status": str,
        "failureReason": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

StopSolutionVersionCreationRequestTypeDef = TypedDict(
    "StopSolutionVersionCreationRequestTypeDef",
    {
        "solutionVersionArn": str,
    },
)

TunedHPOParamsTypeDef = TypedDict(
    "TunedHPOParamsTypeDef",
    {
        "algorithmHyperParameters": Dict[str, str],
    },
    total=False,
)

_RequiredUpdateCampaignRequestTypeDef = TypedDict(
    "_RequiredUpdateCampaignRequestTypeDef",
    {
        "campaignArn": str,
    },
)
_OptionalUpdateCampaignRequestTypeDef = TypedDict(
    "_OptionalUpdateCampaignRequestTypeDef",
    {
        "solutionVersionArn": str,
        "minProvisionedTPS": int,
        "campaignConfig": "CampaignConfigTypeDef",
    },
    total=False,
)


class UpdateCampaignRequestTypeDef(
    _RequiredUpdateCampaignRequestTypeDef, _OptionalUpdateCampaignRequestTypeDef
):
    pass


UpdateCampaignResponseResponseTypeDef = TypedDict(
    "UpdateCampaignResponseResponseTypeDef",
    {
        "campaignArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
