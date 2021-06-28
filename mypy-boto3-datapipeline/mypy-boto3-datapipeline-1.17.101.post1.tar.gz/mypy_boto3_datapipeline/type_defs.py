"""
Type annotations for datapipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datapipeline.type_defs import ActivatePipelineInputTypeDef

    data: ActivatePipelineInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import OperatorTypeType, TaskStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivatePipelineInputTypeDef",
    "AddTagsInputTypeDef",
    "CreatePipelineInputTypeDef",
    "CreatePipelineOutputResponseTypeDef",
    "DeactivatePipelineInputTypeDef",
    "DeletePipelineInputTypeDef",
    "DescribeObjectsInputTypeDef",
    "DescribeObjectsOutputResponseTypeDef",
    "DescribePipelinesInputTypeDef",
    "DescribePipelinesOutputResponseTypeDef",
    "EvaluateExpressionInputTypeDef",
    "EvaluateExpressionOutputResponseTypeDef",
    "FieldTypeDef",
    "GetPipelineDefinitionInputTypeDef",
    "GetPipelineDefinitionOutputResponseTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesInputTypeDef",
    "ListPipelinesOutputResponseTypeDef",
    "OperatorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterAttributeTypeDef",
    "ParameterObjectTypeDef",
    "ParameterValueTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineIdNameTypeDef",
    "PipelineObjectTypeDef",
    "PollForTaskInputTypeDef",
    "PollForTaskOutputResponseTypeDef",
    "PutPipelineDefinitionInputTypeDef",
    "PutPipelineDefinitionOutputResponseTypeDef",
    "QueryObjectsInputTypeDef",
    "QueryObjectsOutputResponseTypeDef",
    "QueryTypeDef",
    "RemoveTagsInputTypeDef",
    "ReportTaskProgressInputTypeDef",
    "ReportTaskProgressOutputResponseTypeDef",
    "ReportTaskRunnerHeartbeatInputTypeDef",
    "ReportTaskRunnerHeartbeatOutputResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SelectorTypeDef",
    "SetStatusInputTypeDef",
    "SetTaskStatusInputTypeDef",
    "TagTypeDef",
    "TaskObjectTypeDef",
    "ValidatePipelineDefinitionInputTypeDef",
    "ValidatePipelineDefinitionOutputResponseTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
)

_RequiredActivatePipelineInputTypeDef = TypedDict(
    "_RequiredActivatePipelineInputTypeDef",
    {
        "pipelineId": str,
    },
)
_OptionalActivatePipelineInputTypeDef = TypedDict(
    "_OptionalActivatePipelineInputTypeDef",
    {
        "parameterValues": List["ParameterValueTypeDef"],
        "startTimestamp": Union[datetime, str],
    },
    total=False,
)


class ActivatePipelineInputTypeDef(
    _RequiredActivatePipelineInputTypeDef, _OptionalActivatePipelineInputTypeDef
):
    pass


AddTagsInputTypeDef = TypedDict(
    "AddTagsInputTypeDef",
    {
        "pipelineId": str,
        "tags": List["TagTypeDef"],
    },
)

_RequiredCreatePipelineInputTypeDef = TypedDict(
    "_RequiredCreatePipelineInputTypeDef",
    {
        "name": str,
        "uniqueId": str,
    },
)
_OptionalCreatePipelineInputTypeDef = TypedDict(
    "_OptionalCreatePipelineInputTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePipelineInputTypeDef(
    _RequiredCreatePipelineInputTypeDef, _OptionalCreatePipelineInputTypeDef
):
    pass


CreatePipelineOutputResponseTypeDef = TypedDict(
    "CreatePipelineOutputResponseTypeDef",
    {
        "pipelineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeactivatePipelineInputTypeDef = TypedDict(
    "_RequiredDeactivatePipelineInputTypeDef",
    {
        "pipelineId": str,
    },
)
_OptionalDeactivatePipelineInputTypeDef = TypedDict(
    "_OptionalDeactivatePipelineInputTypeDef",
    {
        "cancelActive": bool,
    },
    total=False,
)


class DeactivatePipelineInputTypeDef(
    _RequiredDeactivatePipelineInputTypeDef, _OptionalDeactivatePipelineInputTypeDef
):
    pass


DeletePipelineInputTypeDef = TypedDict(
    "DeletePipelineInputTypeDef",
    {
        "pipelineId": str,
    },
)

_RequiredDescribeObjectsInputTypeDef = TypedDict(
    "_RequiredDescribeObjectsInputTypeDef",
    {
        "pipelineId": str,
        "objectIds": List[str],
    },
)
_OptionalDescribeObjectsInputTypeDef = TypedDict(
    "_OptionalDescribeObjectsInputTypeDef",
    {
        "evaluateExpressions": bool,
        "marker": str,
    },
    total=False,
)


class DescribeObjectsInputTypeDef(
    _RequiredDescribeObjectsInputTypeDef, _OptionalDescribeObjectsInputTypeDef
):
    pass


DescribeObjectsOutputResponseTypeDef = TypedDict(
    "DescribeObjectsOutputResponseTypeDef",
    {
        "pipelineObjects": List["PipelineObjectTypeDef"],
        "marker": str,
        "hasMoreResults": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelinesInputTypeDef = TypedDict(
    "DescribePipelinesInputTypeDef",
    {
        "pipelineIds": List[str],
    },
)

DescribePipelinesOutputResponseTypeDef = TypedDict(
    "DescribePipelinesOutputResponseTypeDef",
    {
        "pipelineDescriptionList": List["PipelineDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluateExpressionInputTypeDef = TypedDict(
    "EvaluateExpressionInputTypeDef",
    {
        "pipelineId": str,
        "objectId": str,
        "expression": str,
    },
)

EvaluateExpressionOutputResponseTypeDef = TypedDict(
    "EvaluateExpressionOutputResponseTypeDef",
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


_RequiredGetPipelineDefinitionInputTypeDef = TypedDict(
    "_RequiredGetPipelineDefinitionInputTypeDef",
    {
        "pipelineId": str,
    },
)
_OptionalGetPipelineDefinitionInputTypeDef = TypedDict(
    "_OptionalGetPipelineDefinitionInputTypeDef",
    {
        "version": str,
    },
    total=False,
)


class GetPipelineDefinitionInputTypeDef(
    _RequiredGetPipelineDefinitionInputTypeDef, _OptionalGetPipelineDefinitionInputTypeDef
):
    pass


GetPipelineDefinitionOutputResponseTypeDef = TypedDict(
    "GetPipelineDefinitionOutputResponseTypeDef",
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

ListPipelinesInputTypeDef = TypedDict(
    "ListPipelinesInputTypeDef",
    {
        "marker": str,
    },
    total=False,
)

ListPipelinesOutputResponseTypeDef = TypedDict(
    "ListPipelinesOutputResponseTypeDef",
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

_RequiredPollForTaskInputTypeDef = TypedDict(
    "_RequiredPollForTaskInputTypeDef",
    {
        "workerGroup": str,
    },
)
_OptionalPollForTaskInputTypeDef = TypedDict(
    "_OptionalPollForTaskInputTypeDef",
    {
        "hostname": str,
        "instanceIdentity": "InstanceIdentityTypeDef",
    },
    total=False,
)


class PollForTaskInputTypeDef(_RequiredPollForTaskInputTypeDef, _OptionalPollForTaskInputTypeDef):
    pass


PollForTaskOutputResponseTypeDef = TypedDict(
    "PollForTaskOutputResponseTypeDef",
    {
        "taskObject": "TaskObjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutPipelineDefinitionInputTypeDef = TypedDict(
    "_RequiredPutPipelineDefinitionInputTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": List["PipelineObjectTypeDef"],
    },
)
_OptionalPutPipelineDefinitionInputTypeDef = TypedDict(
    "_OptionalPutPipelineDefinitionInputTypeDef",
    {
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
    },
    total=False,
)


class PutPipelineDefinitionInputTypeDef(
    _RequiredPutPipelineDefinitionInputTypeDef, _OptionalPutPipelineDefinitionInputTypeDef
):
    pass


PutPipelineDefinitionOutputResponseTypeDef = TypedDict(
    "PutPipelineDefinitionOutputResponseTypeDef",
    {
        "validationErrors": List["ValidationErrorTypeDef"],
        "validationWarnings": List["ValidationWarningTypeDef"],
        "errored": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredQueryObjectsInputTypeDef = TypedDict(
    "_RequiredQueryObjectsInputTypeDef",
    {
        "pipelineId": str,
        "sphere": str,
    },
)
_OptionalQueryObjectsInputTypeDef = TypedDict(
    "_OptionalQueryObjectsInputTypeDef",
    {
        "query": "QueryTypeDef",
        "marker": str,
        "limit": int,
    },
    total=False,
)


class QueryObjectsInputTypeDef(
    _RequiredQueryObjectsInputTypeDef, _OptionalQueryObjectsInputTypeDef
):
    pass


QueryObjectsOutputResponseTypeDef = TypedDict(
    "QueryObjectsOutputResponseTypeDef",
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

RemoveTagsInputTypeDef = TypedDict(
    "RemoveTagsInputTypeDef",
    {
        "pipelineId": str,
        "tagKeys": List[str],
    },
)

_RequiredReportTaskProgressInputTypeDef = TypedDict(
    "_RequiredReportTaskProgressInputTypeDef",
    {
        "taskId": str,
    },
)
_OptionalReportTaskProgressInputTypeDef = TypedDict(
    "_OptionalReportTaskProgressInputTypeDef",
    {
        "fields": List["FieldTypeDef"],
    },
    total=False,
)


class ReportTaskProgressInputTypeDef(
    _RequiredReportTaskProgressInputTypeDef, _OptionalReportTaskProgressInputTypeDef
):
    pass


ReportTaskProgressOutputResponseTypeDef = TypedDict(
    "ReportTaskProgressOutputResponseTypeDef",
    {
        "canceled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReportTaskRunnerHeartbeatInputTypeDef = TypedDict(
    "_RequiredReportTaskRunnerHeartbeatInputTypeDef",
    {
        "taskrunnerId": str,
    },
)
_OptionalReportTaskRunnerHeartbeatInputTypeDef = TypedDict(
    "_OptionalReportTaskRunnerHeartbeatInputTypeDef",
    {
        "workerGroup": str,
        "hostname": str,
    },
    total=False,
)


class ReportTaskRunnerHeartbeatInputTypeDef(
    _RequiredReportTaskRunnerHeartbeatInputTypeDef, _OptionalReportTaskRunnerHeartbeatInputTypeDef
):
    pass


ReportTaskRunnerHeartbeatOutputResponseTypeDef = TypedDict(
    "ReportTaskRunnerHeartbeatOutputResponseTypeDef",
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

SetStatusInputTypeDef = TypedDict(
    "SetStatusInputTypeDef",
    {
        "pipelineId": str,
        "objectIds": List[str],
        "status": str,
    },
)

_RequiredSetTaskStatusInputTypeDef = TypedDict(
    "_RequiredSetTaskStatusInputTypeDef",
    {
        "taskId": str,
        "taskStatus": TaskStatusType,
    },
)
_OptionalSetTaskStatusInputTypeDef = TypedDict(
    "_OptionalSetTaskStatusInputTypeDef",
    {
        "errorId": str,
        "errorMessage": str,
        "errorStackTrace": str,
    },
    total=False,
)


class SetTaskStatusInputTypeDef(
    _RequiredSetTaskStatusInputTypeDef, _OptionalSetTaskStatusInputTypeDef
):
    pass


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

_RequiredValidatePipelineDefinitionInputTypeDef = TypedDict(
    "_RequiredValidatePipelineDefinitionInputTypeDef",
    {
        "pipelineId": str,
        "pipelineObjects": List["PipelineObjectTypeDef"],
    },
)
_OptionalValidatePipelineDefinitionInputTypeDef = TypedDict(
    "_OptionalValidatePipelineDefinitionInputTypeDef",
    {
        "parameterObjects": List["ParameterObjectTypeDef"],
        "parameterValues": List["ParameterValueTypeDef"],
    },
    total=False,
)


class ValidatePipelineDefinitionInputTypeDef(
    _RequiredValidatePipelineDefinitionInputTypeDef, _OptionalValidatePipelineDefinitionInputTypeDef
):
    pass


ValidatePipelineDefinitionOutputResponseTypeDef = TypedDict(
    "ValidatePipelineDefinitionOutputResponseTypeDef",
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
