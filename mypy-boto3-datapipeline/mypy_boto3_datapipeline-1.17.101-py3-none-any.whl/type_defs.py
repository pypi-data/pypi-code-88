"""
Type annotations for datapipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datapipeline.type_defs import CreatePipelineOutputTypeDef

    data: CreatePipelineOutputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import OperatorTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreatePipelineOutputTypeDef",
    "DescribeObjectsOutputTypeDef",
    "DescribePipelinesOutputTypeDef",
    "EvaluateExpressionOutputTypeDef",
    "FieldTypeDef",
    "GetPipelineDefinitionOutputTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesOutputTypeDef",
    "OperatorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterAttributeTypeDef",
    "ParameterObjectTypeDef",
    "ParameterValueTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineIdNameTypeDef",
    "PipelineObjectTypeDef",
    "PollForTaskOutputTypeDef",
    "PutPipelineDefinitionOutputTypeDef",
    "QueryObjectsOutputTypeDef",
    "QueryTypeDef",
    "ReportTaskProgressOutputTypeDef",
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    "ResponseMetadataTypeDef",
    "SelectorTypeDef",
    "TagTypeDef",
    "TaskObjectTypeDef",
    "ValidatePipelineDefinitionOutputTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
)

CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipelineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeObjectsOutputTypeDef = TypedDict(
    "DescribeObjectsOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelinesOutputTypeDef = TypedDict(
    "DescribePipelinesOutputTypeDef",
    {
        "pipelineDescriptionList": List["PipelineDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluateExpressionOutputTypeDef = TypedDict(
    "EvaluateExpressionOutputTypeDef",
    {
        "evaluatedExpression": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFieldTypeDef = TypedDict(
    "_RequiredFieldTypeDef",
    {
        "key": str,
    },
)
_OptionalFieldTypeDef = TypedDict(
    "_OptionalFieldTypeDef",
    {
        "stringValue": str,
        "refValue": str,
    },
    total=False,
)


class FieldTypeDef(_RequiredFieldTypeDef, _OptionalFieldTypeDef):
    pass


GetPipelineDefinitionOutputTypeDef = TypedDict(
    "GetPipelineDefinitionOutputTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "document": str,
        "signature": str,
    },
    total=False,
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelineIdList": List["PipelineIdNameTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperatorTypeDef = TypedDict(
    "OperatorTypeDef",
    {
        "type": OperatorTypeType,
        "values": List[str],
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

ParameterAttributeTypeDef = TypedDict(
    "ParameterAttributeTypeDef",
    {
        "key": str,
        "stringValue": str,
    },
)

ParameterObjectTypeDef = TypedDict(
    "ParameterObjectTypeDef",
    {
        "id": str,
        "attributes": List["ParameterAttributeTypeDef"],
    },
)

ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "id": str,
        "stringValue": str,
    },
)

_RequiredPipelineDescriptionTypeDef = TypedDict(
    "_RequiredPipelineDescriptionTypeDef",
    {
        "pipelineId": str,
        "name": str,
        "fields": List["FieldTypeDef"],
    },
)
_OptionalPipelineDescriptionTypeDef = TypedDict(
    "_OptionalPipelineDescriptionTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PipelineDescriptionTypeDef(
    _RequiredPipelineDescriptionTypeDef, _OptionalPipelineDescriptionTypeDef
):
    pass


PipelineIdNameTypeDef = TypedDict(
    "PipelineIdNameTypeDef",
    {
        "id": str,
        "name": str,
    },
    total=False,
)

PipelineObjectTypeDef = TypedDict(
    "PipelineObjectTypeDef",
    {
        "id": str,
        "name": str,
        "fields": List["FieldTypeDef"],
    },
)

PollForTaskOutputTypeDef = TypedDict(
    "PollForTaskOutputTypeDef",
    {
        "taskObject": "TaskObjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPipelineDefinitionOutputTypeDef = TypedDict(
    "PutPipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryObjectsOutputTypeDef = TypedDict(
    "QueryObjectsOutputTypeDef",
    {
        "ids": List[str],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "selectors": List["SelectorTypeDef"],
    },
    total=False,
)

ReportTaskProgressOutputTypeDef = TypedDict(
    "ReportTaskProgressOutputTypeDef",
    {
        "canceled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportTaskRunnerHeartbeatOutputTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    {
        "terminate": bool,
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

SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "fieldName": str,
        "operator": "OperatorTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TaskObjectTypeDef = TypedDict(
    "TaskObjectTypeDef",
    {
        "taskId": str,
        "pipelineId": str,
        "attemptId": str,
        "objects": Dict[str, "PipelineObjectTypeDef"],
    },
    total=False,
)

ValidatePipelineDefinitionOutputTypeDef = TypedDict(
    "ValidatePipelineDefinitionOutputTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "id": str,
        "errors": List[str],
    },
    total=False,
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "id": str,
        "warnings": List[str],
    },
    total=False,
)
