"""
Type annotations for frauddetector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_frauddetector.type_defs import BatchCreateVariableErrorTypeDef

    data: BatchCreateVariableErrorTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AsyncJobStatusType,
    DataSourceType,
    DataTypeType,
    DetectorVersionStatusType,
    ModelEndpointStatusType,
    ModelInputDataFormatType,
    ModelOutputDataFormatType,
    ModelVersionStatusType,
    RuleExecutionModeType,
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
    "BatchCreateVariableErrorTypeDef",
    "BatchCreateVariableRequestTypeDef",
    "BatchCreateVariableResultResponseTypeDef",
    "BatchGetVariableErrorTypeDef",
    "BatchGetVariableRequestTypeDef",
    "BatchGetVariableResultResponseTypeDef",
    "BatchPredictionTypeDef",
    "CancelBatchPredictionJobRequestTypeDef",
    "CreateBatchPredictionJobRequestTypeDef",
    "CreateDetectorVersionRequestTypeDef",
    "CreateDetectorVersionResultResponseTypeDef",
    "CreateModelRequestTypeDef",
    "CreateModelVersionRequestTypeDef",
    "CreateModelVersionResultResponseTypeDef",
    "CreateRuleRequestTypeDef",
    "CreateRuleResultResponseTypeDef",
    "CreateVariableRequestTypeDef",
    "DataValidationMetricsTypeDef",
    "DeleteBatchPredictionJobRequestTypeDef",
    "DeleteDetectorRequestTypeDef",
    "DeleteDetectorVersionRequestTypeDef",
    "DeleteEntityTypeRequestTypeDef",
    "DeleteEventRequestTypeDef",
    "DeleteEventTypeRequestTypeDef",
    "DeleteExternalModelRequestTypeDef",
    "DeleteLabelRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteModelVersionRequestTypeDef",
    "DeleteOutcomeRequestTypeDef",
    "DeleteRuleRequestTypeDef",
    "DeleteVariableRequestTypeDef",
    "DescribeDetectorRequestTypeDef",
    "DescribeDetectorResultResponseTypeDef",
    "DescribeModelVersionsRequestTypeDef",
    "DescribeModelVersionsResultResponseTypeDef",
    "DetectorTypeDef",
    "DetectorVersionSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypeTypeDef",
    "EventTypeTypeDef",
    "ExternalEventsDetailTypeDef",
    "ExternalModelTypeDef",
    "FieldValidationMessageTypeDef",
    "FileValidationMessageTypeDef",
    "GetBatchPredictionJobsRequestTypeDef",
    "GetBatchPredictionJobsResultResponseTypeDef",
    "GetDetectorVersionRequestTypeDef",
    "GetDetectorVersionResultResponseTypeDef",
    "GetDetectorsRequestTypeDef",
    "GetDetectorsResultResponseTypeDef",
    "GetEntityTypesRequestTypeDef",
    "GetEntityTypesResultResponseTypeDef",
    "GetEventPredictionRequestTypeDef",
    "GetEventPredictionResultResponseTypeDef",
    "GetEventTypesRequestTypeDef",
    "GetEventTypesResultResponseTypeDef",
    "GetExternalModelsRequestTypeDef",
    "GetExternalModelsResultResponseTypeDef",
    "GetKMSEncryptionKeyResultResponseTypeDef",
    "GetLabelsRequestTypeDef",
    "GetLabelsResultResponseTypeDef",
    "GetModelVersionRequestTypeDef",
    "GetModelVersionResultResponseTypeDef",
    "GetModelsRequestTypeDef",
    "GetModelsResultResponseTypeDef",
    "GetOutcomesRequestTypeDef",
    "GetOutcomesResultResponseTypeDef",
    "GetRulesRequestTypeDef",
    "GetRulesResultResponseTypeDef",
    "GetVariablesRequestTypeDef",
    "GetVariablesResultResponseTypeDef",
    "KMSKeyTypeDef",
    "LabelSchemaTypeDef",
    "LabelTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "MetricDataPointTypeDef",
    "ModelEndpointDataBlobTypeDef",
    "ModelInputConfigurationTypeDef",
    "ModelOutputConfigurationTypeDef",
    "ModelScoresTypeDef",
    "ModelTypeDef",
    "ModelVersionDetailTypeDef",
    "ModelVersionTypeDef",
    "OutcomeTypeDef",
    "PutDetectorRequestTypeDef",
    "PutEntityTypeRequestTypeDef",
    "PutEventTypeRequestTypeDef",
    "PutExternalModelRequestTypeDef",
    "PutKMSEncryptionKeyRequestTypeDef",
    "PutLabelRequestTypeDef",
    "PutOutcomeRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleDetailTypeDef",
    "RuleResultTypeDef",
    "RuleTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TrainingDataSchemaTypeDef",
    "TrainingMetricsTypeDef",
    "TrainingResultTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDetectorVersionMetadataRequestTypeDef",
    "UpdateDetectorVersionRequestTypeDef",
    "UpdateDetectorVersionStatusRequestTypeDef",
    "UpdateModelRequestTypeDef",
    "UpdateModelVersionRequestTypeDef",
    "UpdateModelVersionResultResponseTypeDef",
    "UpdateModelVersionStatusRequestTypeDef",
    "UpdateRuleMetadataRequestTypeDef",
    "UpdateRuleVersionRequestTypeDef",
    "UpdateRuleVersionResultResponseTypeDef",
    "UpdateVariableRequestTypeDef",
    "VariableEntryTypeDef",
    "VariableTypeDef",
)

BatchCreateVariableErrorTypeDef = TypedDict(
    "BatchCreateVariableErrorTypeDef",
    {
        "name": str,
        "code": int,
        "message": str,
    },
    total=False,
)

_RequiredBatchCreateVariableRequestTypeDef = TypedDict(
    "_RequiredBatchCreateVariableRequestTypeDef",
    {
        "variableEntries": List["VariableEntryTypeDef"],
    },
)
_OptionalBatchCreateVariableRequestTypeDef = TypedDict(
    "_OptionalBatchCreateVariableRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class BatchCreateVariableRequestTypeDef(
    _RequiredBatchCreateVariableRequestTypeDef, _OptionalBatchCreateVariableRequestTypeDef
):
    pass


BatchCreateVariableResultResponseTypeDef = TypedDict(
    "BatchCreateVariableResultResponseTypeDef",
    {
        "errors": List["BatchCreateVariableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetVariableErrorTypeDef = TypedDict(
    "BatchGetVariableErrorTypeDef",
    {
        "name": str,
        "code": int,
        "message": str,
    },
    total=False,
)

BatchGetVariableRequestTypeDef = TypedDict(
    "BatchGetVariableRequestTypeDef",
    {
        "names": List[str],
    },
)

BatchGetVariableResultResponseTypeDef = TypedDict(
    "BatchGetVariableResultResponseTypeDef",
    {
        "variables": List["VariableTypeDef"],
        "errors": List["BatchGetVariableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "jobId": str,
        "status": AsyncJobStatusType,
        "failureReason": str,
        "startTime": str,
        "completionTime": str,
        "lastHeartbeatTime": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "detectorVersion": str,
        "iamRoleArn": str,
        "arn": str,
        "processedRecordsCount": int,
        "totalRecordsCount": int,
    },
    total=False,
)

CancelBatchPredictionJobRequestTypeDef = TypedDict(
    "CancelBatchPredictionJobRequestTypeDef",
    {
        "jobId": str,
    },
)

_RequiredCreateBatchPredictionJobRequestTypeDef = TypedDict(
    "_RequiredCreateBatchPredictionJobRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "iamRoleArn": str,
    },
)
_OptionalCreateBatchPredictionJobRequestTypeDef = TypedDict(
    "_OptionalCreateBatchPredictionJobRequestTypeDef",
    {
        "detectorVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateBatchPredictionJobRequestTypeDef(
    _RequiredCreateBatchPredictionJobRequestTypeDef, _OptionalCreateBatchPredictionJobRequestTypeDef
):
    pass


_RequiredCreateDetectorVersionRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorVersionRequestTypeDef",
    {
        "detectorId": str,
        "rules": List["RuleTypeDef"],
    },
)
_OptionalCreateDetectorVersionRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorVersionRequestTypeDef",
    {
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List["ModelVersionTypeDef"],
        "ruleExecutionMode": RuleExecutionModeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDetectorVersionRequestTypeDef(
    _RequiredCreateDetectorVersionRequestTypeDef, _OptionalCreateDetectorVersionRequestTypeDef
):
    pass


CreateDetectorVersionResultResponseTypeDef = TypedDict(
    "CreateDetectorVersionResultResponseTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "eventTypeName": str,
    },
)
_OptionalCreateModelRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelRequestTypeDef(
    _RequiredCreateModelRequestTypeDef, _OptionalCreateModelRequestTypeDef
):
    pass


_RequiredCreateModelVersionRequestTypeDef = TypedDict(
    "_RequiredCreateModelVersionRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "trainingDataSource": Literal["EXTERNAL_EVENTS"],
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
    },
)
_OptionalCreateModelVersionRequestTypeDef = TypedDict(
    "_OptionalCreateModelVersionRequestTypeDef",
    {
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelVersionRequestTypeDef(
    _RequiredCreateModelVersionRequestTypeDef, _OptionalCreateModelVersionRequestTypeDef
):
    pass


CreateModelVersionResultResponseTypeDef = TypedDict(
    "CreateModelVersionResultResponseTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestTypeDef",
    {
        "ruleId": str,
        "detectorId": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
    },
)
_OptionalCreateRuleRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRuleRequestTypeDef(
    _RequiredCreateRuleRequestTypeDef, _OptionalCreateRuleRequestTypeDef
):
    pass


CreateRuleResultResponseTypeDef = TypedDict(
    "CreateRuleResultResponseTypeDef",
    {
        "rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVariableRequestTypeDef = TypedDict(
    "_RequiredCreateVariableRequestTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
    },
)
_OptionalCreateVariableRequestTypeDef = TypedDict(
    "_OptionalCreateVariableRequestTypeDef",
    {
        "description": str,
        "variableType": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateVariableRequestTypeDef(
    _RequiredCreateVariableRequestTypeDef, _OptionalCreateVariableRequestTypeDef
):
    pass


DataValidationMetricsTypeDef = TypedDict(
    "DataValidationMetricsTypeDef",
    {
        "fileLevelMessages": List["FileValidationMessageTypeDef"],
        "fieldLevelMessages": List["FieldValidationMessageTypeDef"],
    },
    total=False,
)

DeleteBatchPredictionJobRequestTypeDef = TypedDict(
    "DeleteBatchPredictionJobRequestTypeDef",
    {
        "jobId": str,
    },
)

DeleteDetectorRequestTypeDef = TypedDict(
    "DeleteDetectorRequestTypeDef",
    {
        "detectorId": str,
    },
)

DeleteDetectorVersionRequestTypeDef = TypedDict(
    "DeleteDetectorVersionRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

DeleteEntityTypeRequestTypeDef = TypedDict(
    "DeleteEntityTypeRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEventRequestTypeDef = TypedDict(
    "DeleteEventRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
    },
)

DeleteEventTypeRequestTypeDef = TypedDict(
    "DeleteEventTypeRequestTypeDef",
    {
        "name": str,
    },
)

DeleteExternalModelRequestTypeDef = TypedDict(
    "DeleteExternalModelRequestTypeDef",
    {
        "modelEndpoint": str,
    },
)

DeleteLabelRequestTypeDef = TypedDict(
    "DeleteLabelRequestTypeDef",
    {
        "name": str,
    },
)

DeleteModelRequestTypeDef = TypedDict(
    "DeleteModelRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
    },
)

DeleteModelVersionRequestTypeDef = TypedDict(
    "DeleteModelVersionRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
    },
)

DeleteOutcomeRequestTypeDef = TypedDict(
    "DeleteOutcomeRequestTypeDef",
    {
        "name": str,
    },
)

DeleteRuleRequestTypeDef = TypedDict(
    "DeleteRuleRequestTypeDef",
    {
        "rule": "RuleTypeDef",
    },
)

DeleteVariableRequestTypeDef = TypedDict(
    "DeleteVariableRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredDescribeDetectorRequestTypeDef = TypedDict(
    "_RequiredDescribeDetectorRequestTypeDef",
    {
        "detectorId": str,
    },
)
_OptionalDescribeDetectorRequestTypeDef = TypedDict(
    "_OptionalDescribeDetectorRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeDetectorRequestTypeDef(
    _RequiredDescribeDetectorRequestTypeDef, _OptionalDescribeDetectorRequestTypeDef
):
    pass


DescribeDetectorResultResponseTypeDef = TypedDict(
    "DescribeDetectorResultResponseTypeDef",
    {
        "detectorId": str,
        "detectorVersionSummaries": List["DetectorVersionSummaryTypeDef"],
        "nextToken": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelVersionsRequestTypeDef = TypedDict(
    "DescribeModelVersionsRequestTypeDef",
    {
        "modelId": str,
        "modelVersionNumber": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeModelVersionsResultResponseTypeDef = TypedDict(
    "DescribeModelVersionsResultResponseTypeDef",
    {
        "modelVersionDetails": List["ModelVersionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorId": str,
        "description": str,
        "eventTypeName": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

DetectorVersionSummaryTypeDef = TypedDict(
    "DetectorVersionSummaryTypeDef",
    {
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "description": str,
        "lastUpdatedTime": str,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "entityType": str,
        "entityId": str,
    },
)

EntityTypeTypeDef = TypedDict(
    "EntityTypeTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "name": str,
        "description": str,
        "eventVariables": List[str],
        "labels": List[str],
        "entityTypes": List[str],
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

ExternalEventsDetailTypeDef = TypedDict(
    "ExternalEventsDetailTypeDef",
    {
        "dataLocation": str,
        "dataAccessRoleArn": str,
    },
)

ExternalModelTypeDef = TypedDict(
    "ExternalModelTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": "ModelInputConfigurationTypeDef",
        "outputConfiguration": "ModelOutputConfigurationTypeDef",
        "modelEndpointStatus": ModelEndpointStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

FieldValidationMessageTypeDef = TypedDict(
    "FieldValidationMessageTypeDef",
    {
        "fieldName": str,
        "identifier": str,
        "title": str,
        "content": str,
        "type": str,
    },
    total=False,
)

FileValidationMessageTypeDef = TypedDict(
    "FileValidationMessageTypeDef",
    {
        "title": str,
        "content": str,
        "type": str,
    },
    total=False,
)

GetBatchPredictionJobsRequestTypeDef = TypedDict(
    "GetBatchPredictionJobsRequestTypeDef",
    {
        "jobId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetBatchPredictionJobsResultResponseTypeDef = TypedDict(
    "GetBatchPredictionJobsResultResponseTypeDef",
    {
        "batchPredictions": List["BatchPredictionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorVersionRequestTypeDef = TypedDict(
    "GetDetectorVersionRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)

GetDetectorVersionResultResponseTypeDef = TypedDict(
    "GetDetectorVersionResultResponseTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List["ModelVersionTypeDef"],
        "rules": List["RuleTypeDef"],
        "status": DetectorVersionStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "ruleExecutionMode": RuleExecutionModeType,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDetectorsRequestTypeDef = TypedDict(
    "GetDetectorsRequestTypeDef",
    {
        "detectorId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetDetectorsResultResponseTypeDef = TypedDict(
    "GetDetectorsResultResponseTypeDef",
    {
        "detectors": List["DetectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEntityTypesRequestTypeDef = TypedDict(
    "GetEntityTypesRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEntityTypesResultResponseTypeDef = TypedDict(
    "GetEntityTypesResultResponseTypeDef",
    {
        "entityTypes": List["EntityTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEventPredictionRequestTypeDef = TypedDict(
    "_RequiredGetEventPredictionRequestTypeDef",
    {
        "detectorId": str,
        "eventId": str,
        "eventTypeName": str,
        "entities": List["EntityTypeDef"],
        "eventTimestamp": str,
        "eventVariables": Dict[str, str],
    },
)
_OptionalGetEventPredictionRequestTypeDef = TypedDict(
    "_OptionalGetEventPredictionRequestTypeDef",
    {
        "detectorVersionId": str,
        "externalModelEndpointDataBlobs": Dict[str, "ModelEndpointDataBlobTypeDef"],
    },
    total=False,
)


class GetEventPredictionRequestTypeDef(
    _RequiredGetEventPredictionRequestTypeDef, _OptionalGetEventPredictionRequestTypeDef
):
    pass


GetEventPredictionResultResponseTypeDef = TypedDict(
    "GetEventPredictionResultResponseTypeDef",
    {
        "modelScores": List["ModelScoresTypeDef"],
        "ruleResults": List["RuleResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventTypesRequestTypeDef = TypedDict(
    "GetEventTypesRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetEventTypesResultResponseTypeDef = TypedDict(
    "GetEventTypesResultResponseTypeDef",
    {
        "eventTypes": List["EventTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExternalModelsRequestTypeDef = TypedDict(
    "GetExternalModelsRequestTypeDef",
    {
        "modelEndpoint": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetExternalModelsResultResponseTypeDef = TypedDict(
    "GetExternalModelsResultResponseTypeDef",
    {
        "externalModels": List["ExternalModelTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKMSEncryptionKeyResultResponseTypeDef = TypedDict(
    "GetKMSEncryptionKeyResultResponseTypeDef",
    {
        "kmsKey": "KMSKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLabelsRequestTypeDef = TypedDict(
    "GetLabelsRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetLabelsResultResponseTypeDef = TypedDict(
    "GetLabelsResultResponseTypeDef",
    {
        "labels": List["LabelTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelVersionRequestTypeDef = TypedDict(
    "GetModelVersionRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
    },
)

GetModelVersionResultResponseTypeDef = TypedDict(
    "GetModelVersionResultResponseTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "trainingDataSource": Literal["EXTERNAL_EVENTS"],
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "status": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelsRequestTypeDef = TypedDict(
    "GetModelsRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetModelsResultResponseTypeDef = TypedDict(
    "GetModelsResultResponseTypeDef",
    {
        "nextToken": str,
        "models": List["ModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutcomesRequestTypeDef = TypedDict(
    "GetOutcomesRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetOutcomesResultResponseTypeDef = TypedDict(
    "GetOutcomesResultResponseTypeDef",
    {
        "outcomes": List["OutcomeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRulesRequestTypeDef = TypedDict(
    "_RequiredGetRulesRequestTypeDef",
    {
        "detectorId": str,
    },
)
_OptionalGetRulesRequestTypeDef = TypedDict(
    "_OptionalGetRulesRequestTypeDef",
    {
        "ruleId": str,
        "ruleVersion": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetRulesRequestTypeDef(_RequiredGetRulesRequestTypeDef, _OptionalGetRulesRequestTypeDef):
    pass


GetRulesResultResponseTypeDef = TypedDict(
    "GetRulesResultResponseTypeDef",
    {
        "ruleDetails": List["RuleDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVariablesRequestTypeDef = TypedDict(
    "GetVariablesRequestTypeDef",
    {
        "name": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetVariablesResultResponseTypeDef = TypedDict(
    "GetVariablesResultResponseTypeDef",
    {
        "variables": List["VariableTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KMSKeyTypeDef = TypedDict(
    "KMSKeyTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
    total=False,
)

LabelSchemaTypeDef = TypedDict(
    "LabelSchemaTypeDef",
    {
        "labelMapper": Dict[str, List[str]],
    },
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "resourceARN": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricDataPointTypeDef = TypedDict(
    "MetricDataPointTypeDef",
    {
        "fpr": float,
        "precision": float,
        "tpr": float,
        "threshold": float,
    },
    total=False,
)

ModelEndpointDataBlobTypeDef = TypedDict(
    "ModelEndpointDataBlobTypeDef",
    {
        "byteBuffer": Union[bytes, IO[bytes], StreamingBody],
        "contentType": str,
    },
    total=False,
)

_RequiredModelInputConfigurationTypeDef = TypedDict(
    "_RequiredModelInputConfigurationTypeDef",
    {
        "useEventVariables": bool,
    },
)
_OptionalModelInputConfigurationTypeDef = TypedDict(
    "_OptionalModelInputConfigurationTypeDef",
    {
        "eventTypeName": str,
        "format": ModelInputDataFormatType,
        "jsonInputTemplate": str,
        "csvInputTemplate": str,
    },
    total=False,
)


class ModelInputConfigurationTypeDef(
    _RequiredModelInputConfigurationTypeDef, _OptionalModelInputConfigurationTypeDef
):
    pass


_RequiredModelOutputConfigurationTypeDef = TypedDict(
    "_RequiredModelOutputConfigurationTypeDef",
    {
        "format": ModelOutputDataFormatType,
    },
)
_OptionalModelOutputConfigurationTypeDef = TypedDict(
    "_OptionalModelOutputConfigurationTypeDef",
    {
        "jsonKeyToVariableMap": Dict[str, str],
        "csvIndexToVariableMap": Dict[str, str],
    },
    total=False,
)


class ModelOutputConfigurationTypeDef(
    _RequiredModelOutputConfigurationTypeDef, _OptionalModelOutputConfigurationTypeDef
):
    pass


ModelScoresTypeDef = TypedDict(
    "ModelScoresTypeDef",
    {
        "modelVersion": "ModelVersionTypeDef",
        "scores": Dict[str, float],
    },
    total=False,
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "description": str,
        "eventTypeName": str,
        "createdTime": str,
        "lastUpdatedTime": str,
        "arn": str,
    },
    total=False,
)

ModelVersionDetailTypeDef = TypedDict(
    "ModelVersionDetailTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": str,
        "trainingDataSource": Literal["EXTERNAL_EVENTS"],
        "trainingDataSchema": "TrainingDataSchemaTypeDef",
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "trainingResult": "TrainingResultTypeDef",
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredModelVersionTypeDef = TypedDict(
    "_RequiredModelVersionTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
    },
)
_OptionalModelVersionTypeDef = TypedDict(
    "_OptionalModelVersionTypeDef",
    {
        "arn": str,
    },
    total=False,
)


class ModelVersionTypeDef(_RequiredModelVersionTypeDef, _OptionalModelVersionTypeDef):
    pass


OutcomeTypeDef = TypedDict(
    "OutcomeTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

_RequiredPutDetectorRequestTypeDef = TypedDict(
    "_RequiredPutDetectorRequestTypeDef",
    {
        "detectorId": str,
        "eventTypeName": str,
    },
)
_OptionalPutDetectorRequestTypeDef = TypedDict(
    "_OptionalPutDetectorRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutDetectorRequestTypeDef(
    _RequiredPutDetectorRequestTypeDef, _OptionalPutDetectorRequestTypeDef
):
    pass


_RequiredPutEntityTypeRequestTypeDef = TypedDict(
    "_RequiredPutEntityTypeRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutEntityTypeRequestTypeDef = TypedDict(
    "_OptionalPutEntityTypeRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutEntityTypeRequestTypeDef(
    _RequiredPutEntityTypeRequestTypeDef, _OptionalPutEntityTypeRequestTypeDef
):
    pass


_RequiredPutEventTypeRequestTypeDef = TypedDict(
    "_RequiredPutEventTypeRequestTypeDef",
    {
        "name": str,
        "eventVariables": List[str],
        "entityTypes": List[str],
    },
)
_OptionalPutEventTypeRequestTypeDef = TypedDict(
    "_OptionalPutEventTypeRequestTypeDef",
    {
        "description": str,
        "labels": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutEventTypeRequestTypeDef(
    _RequiredPutEventTypeRequestTypeDef, _OptionalPutEventTypeRequestTypeDef
):
    pass


_RequiredPutExternalModelRequestTypeDef = TypedDict(
    "_RequiredPutExternalModelRequestTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": "ModelInputConfigurationTypeDef",
        "outputConfiguration": "ModelOutputConfigurationTypeDef",
        "modelEndpointStatus": ModelEndpointStatusType,
    },
)
_OptionalPutExternalModelRequestTypeDef = TypedDict(
    "_OptionalPutExternalModelRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutExternalModelRequestTypeDef(
    _RequiredPutExternalModelRequestTypeDef, _OptionalPutExternalModelRequestTypeDef
):
    pass


PutKMSEncryptionKeyRequestTypeDef = TypedDict(
    "PutKMSEncryptionKeyRequestTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
)

_RequiredPutLabelRequestTypeDef = TypedDict(
    "_RequiredPutLabelRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutLabelRequestTypeDef = TypedDict(
    "_OptionalPutLabelRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutLabelRequestTypeDef(_RequiredPutLabelRequestTypeDef, _OptionalPutLabelRequestTypeDef):
    pass


_RequiredPutOutcomeRequestTypeDef = TypedDict(
    "_RequiredPutOutcomeRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutOutcomeRequestTypeDef = TypedDict(
    "_OptionalPutOutcomeRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutOutcomeRequestTypeDef(
    _RequiredPutOutcomeRequestTypeDef, _OptionalPutOutcomeRequestTypeDef
):
    pass


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

RuleDetailTypeDef = TypedDict(
    "RuleDetailTypeDef",
    {
        "ruleId": str,
        "description": str,
        "detectorId": str,
        "ruleVersion": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)

RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "ruleId": str,
        "outcomes": List[str],
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "detectorId": str,
        "ruleId": str,
        "ruleVersion": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceARN": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TrainingDataSchemaTypeDef = TypedDict(
    "TrainingDataSchemaTypeDef",
    {
        "modelVariables": List[str],
        "labelSchema": "LabelSchemaTypeDef",
    },
)

TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "auc": float,
        "metricDataPoints": List["MetricDataPointTypeDef"],
    },
    total=False,
)

TrainingResultTypeDef = TypedDict(
    "TrainingResultTypeDef",
    {
        "dataValidationMetrics": "DataValidationMetricsTypeDef",
        "trainingMetrics": "TrainingMetricsTypeDef",
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": List[str],
    },
)

UpdateDetectorVersionMetadataRequestTypeDef = TypedDict(
    "UpdateDetectorVersionMetadataRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
    },
)

_RequiredUpdateDetectorVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorVersionRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "externalModelEndpoints": List[str],
        "rules": List["RuleTypeDef"],
    },
)
_OptionalUpdateDetectorVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorVersionRequestTypeDef",
    {
        "description": str,
        "modelVersions": List["ModelVersionTypeDef"],
        "ruleExecutionMode": RuleExecutionModeType,
    },
    total=False,
)


class UpdateDetectorVersionRequestTypeDef(
    _RequiredUpdateDetectorVersionRequestTypeDef, _OptionalUpdateDetectorVersionRequestTypeDef
):
    pass


UpdateDetectorVersionStatusRequestTypeDef = TypedDict(
    "UpdateDetectorVersionStatusRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
    },
)

_RequiredUpdateModelRequestTypeDef = TypedDict(
    "_RequiredUpdateModelRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
    },
)
_OptionalUpdateModelRequestTypeDef = TypedDict(
    "_OptionalUpdateModelRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateModelRequestTypeDef(
    _RequiredUpdateModelRequestTypeDef, _OptionalUpdateModelRequestTypeDef
):
    pass


_RequiredUpdateModelVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateModelVersionRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "majorVersionNumber": str,
    },
)
_OptionalUpdateModelVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateModelVersionRequestTypeDef",
    {
        "externalEventsDetail": "ExternalEventsDetailTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class UpdateModelVersionRequestTypeDef(
    _RequiredUpdateModelVersionRequestTypeDef, _OptionalUpdateModelVersionRequestTypeDef
):
    pass


UpdateModelVersionResultResponseTypeDef = TypedDict(
    "UpdateModelVersionResultResponseTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateModelVersionStatusRequestTypeDef = TypedDict(
    "UpdateModelVersionStatusRequestTypeDef",
    {
        "modelId": str,
        "modelType": Literal["ONLINE_FRAUD_INSIGHTS"],
        "modelVersionNumber": str,
        "status": ModelVersionStatusType,
    },
)

UpdateRuleMetadataRequestTypeDef = TypedDict(
    "UpdateRuleMetadataRequestTypeDef",
    {
        "rule": "RuleTypeDef",
        "description": str,
    },
)

_RequiredUpdateRuleVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleVersionRequestTypeDef",
    {
        "rule": "RuleTypeDef",
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": List[str],
    },
)
_OptionalUpdateRuleVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleVersionRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class UpdateRuleVersionRequestTypeDef(
    _RequiredUpdateRuleVersionRequestTypeDef, _OptionalUpdateRuleVersionRequestTypeDef
):
    pass


UpdateRuleVersionResultResponseTypeDef = TypedDict(
    "UpdateRuleVersionResultResponseTypeDef",
    {
        "rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVariableRequestTypeDef = TypedDict(
    "_RequiredUpdateVariableRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateVariableRequestTypeDef = TypedDict(
    "_OptionalUpdateVariableRequestTypeDef",
    {
        "defaultValue": str,
        "description": str,
        "variableType": str,
    },
    total=False,
)


class UpdateVariableRequestTypeDef(
    _RequiredUpdateVariableRequestTypeDef, _OptionalUpdateVariableRequestTypeDef
):
    pass


VariableEntryTypeDef = TypedDict(
    "VariableEntryTypeDef",
    {
        "name": str,
        "dataType": str,
        "dataSource": str,
        "defaultValue": str,
        "description": str,
        "variableType": str,
    },
    total=False,
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
        "description": str,
        "variableType": str,
        "lastUpdatedTime": str,
        "createdTime": str,
        "arn": str,
    },
    total=False,
)
