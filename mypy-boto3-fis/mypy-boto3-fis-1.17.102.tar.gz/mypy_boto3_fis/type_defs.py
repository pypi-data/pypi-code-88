"""
Type annotations for fis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fis.type_defs import ActionParameterTypeDef

    data: ActionParameterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ExperimentActionStatusType, ExperimentStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionParameterTypeDef",
    "ActionSummaryTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "CreateExperimentTemplateActionInputTypeDef",
    "CreateExperimentTemplateRequestTypeDef",
    "CreateExperimentTemplateResponseResponseTypeDef",
    "CreateExperimentTemplateStopConditionInputTypeDef",
    "CreateExperimentTemplateTargetInputTypeDef",
    "DeleteExperimentTemplateRequestTypeDef",
    "DeleteExperimentTemplateResponseResponseTypeDef",
    "ExperimentActionStateTypeDef",
    "ExperimentActionTypeDef",
    "ExperimentStateTypeDef",
    "ExperimentStopConditionTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTargetFilterTypeDef",
    "ExperimentTargetTypeDef",
    "ExperimentTemplateActionTypeDef",
    "ExperimentTemplateStopConditionTypeDef",
    "ExperimentTemplateSummaryTypeDef",
    "ExperimentTemplateTargetFilterTypeDef",
    "ExperimentTemplateTargetInputFilterTypeDef",
    "ExperimentTemplateTargetTypeDef",
    "ExperimentTemplateTypeDef",
    "ExperimentTypeDef",
    "GetActionRequestTypeDef",
    "GetActionResponseResponseTypeDef",
    "GetExperimentRequestTypeDef",
    "GetExperimentResponseResponseTypeDef",
    "GetExperimentTemplateRequestTypeDef",
    "GetExperimentTemplateResponseResponseTypeDef",
    "ListActionsRequestTypeDef",
    "ListActionsResponseResponseTypeDef",
    "ListExperimentTemplatesRequestTypeDef",
    "ListExperimentTemplatesResponseResponseTypeDef",
    "ListExperimentsRequestTypeDef",
    "ListExperimentsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartExperimentRequestTypeDef",
    "StartExperimentResponseResponseTypeDef",
    "StopExperimentRequestTypeDef",
    "StopExperimentResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateExperimentTemplateActionInputItemTypeDef",
    "UpdateExperimentTemplateRequestTypeDef",
    "UpdateExperimentTemplateResponseResponseTypeDef",
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    "UpdateExperimentTemplateTargetInputTypeDef",
)

ActionParameterTypeDef = TypedDict(
    "ActionParameterTypeDef",
    {
        "description": str,
        "required": bool,
    },
    total=False,
)

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "id": str,
        "description": str,
        "targets": Dict[str, "ActionTargetTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "resourceType": str,
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "id": str,
        "description": str,
        "parameters": Dict[str, "ActionParameterTypeDef"],
        "targets": Dict[str, "ActionTargetTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateExperimentTemplateActionInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateActionInputTypeDef",
    {
        "actionId": str,
    },
)
_OptionalCreateExperimentTemplateActionInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateActionInputTypeDef",
    {
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
    },
    total=False,
)


class CreateExperimentTemplateActionInputTypeDef(
    _RequiredCreateExperimentTemplateActionInputTypeDef,
    _OptionalCreateExperimentTemplateActionInputTypeDef,
):
    pass


_RequiredCreateExperimentTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "stopConditions": List["CreateExperimentTemplateStopConditionInputTypeDef"],
        "actions": Dict[str, "CreateExperimentTemplateActionInputTypeDef"],
        "roleArn": str,
    },
)
_OptionalCreateExperimentTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateRequestTypeDef",
    {
        "targets": Dict[str, "CreateExperimentTemplateTargetInputTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateExperimentTemplateRequestTypeDef(
    _RequiredCreateExperimentTemplateRequestTypeDef, _OptionalCreateExperimentTemplateRequestTypeDef
):
    pass


CreateExperimentTemplateResponseResponseTypeDef = TypedDict(
    "CreateExperimentTemplateResponseResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
    },
)
_OptionalCreateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateStopConditionInputTypeDef",
    {
        "value": str,
    },
    total=False,
)


class CreateExperimentTemplateStopConditionInputTypeDef(
    _RequiredCreateExperimentTemplateStopConditionInputTypeDef,
    _OptionalCreateExperimentTemplateStopConditionInputTypeDef,
):
    pass


_RequiredCreateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
    },
)
_OptionalCreateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateTargetInputTypeDef",
    {
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTemplateTargetInputFilterTypeDef"],
    },
    total=False,
)


class CreateExperimentTemplateTargetInputTypeDef(
    _RequiredCreateExperimentTemplateTargetInputTypeDef,
    _OptionalCreateExperimentTemplateTargetInputTypeDef,
):
    pass


DeleteExperimentTemplateRequestTypeDef = TypedDict(
    "DeleteExperimentTemplateRequestTypeDef",
    {
        "id": str,
    },
)

DeleteExperimentTemplateResponseResponseTypeDef = TypedDict(
    "DeleteExperimentTemplateResponseResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExperimentActionStateTypeDef = TypedDict(
    "ExperimentActionStateTypeDef",
    {
        "status": ExperimentActionStatusType,
        "reason": str,
    },
    total=False,
)

ExperimentActionTypeDef = TypedDict(
    "ExperimentActionTypeDef",
    {
        "actionId": str,
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
        "state": "ExperimentActionStateTypeDef",
    },
    total=False,
)

ExperimentStateTypeDef = TypedDict(
    "ExperimentStateTypeDef",
    {
        "status": ExperimentStatusType,
        "reason": str,
    },
    total=False,
)

ExperimentStopConditionTypeDef = TypedDict(
    "ExperimentStopConditionTypeDef",
    {
        "source": str,
        "value": str,
    },
    total=False,
)

ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "id": str,
        "experimentTemplateId": str,
        "state": "ExperimentStateTypeDef",
        "creationTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ExperimentTargetFilterTypeDef = TypedDict(
    "ExperimentTargetFilterTypeDef",
    {
        "path": str,
        "values": List[str],
    },
    total=False,
)

ExperimentTargetTypeDef = TypedDict(
    "ExperimentTargetTypeDef",
    {
        "resourceType": str,
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTargetFilterTypeDef"],
        "selectionMode": str,
    },
    total=False,
)

ExperimentTemplateActionTypeDef = TypedDict(
    "ExperimentTemplateActionTypeDef",
    {
        "actionId": str,
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
    },
    total=False,
)

ExperimentTemplateStopConditionTypeDef = TypedDict(
    "ExperimentTemplateStopConditionTypeDef",
    {
        "source": str,
        "value": str,
    },
    total=False,
)

ExperimentTemplateSummaryTypeDef = TypedDict(
    "ExperimentTemplateSummaryTypeDef",
    {
        "id": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ExperimentTemplateTargetFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetFilterTypeDef",
    {
        "path": str,
        "values": List[str],
    },
    total=False,
)

ExperimentTemplateTargetInputFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetInputFilterTypeDef",
    {
        "path": str,
        "values": List[str],
    },
)

ExperimentTemplateTargetTypeDef = TypedDict(
    "ExperimentTemplateTargetTypeDef",
    {
        "resourceType": str,
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTemplateTargetFilterTypeDef"],
        "selectionMode": str,
    },
    total=False,
)

ExperimentTemplateTypeDef = TypedDict(
    "ExperimentTemplateTypeDef",
    {
        "id": str,
        "description": str,
        "targets": Dict[str, "ExperimentTemplateTargetTypeDef"],
        "actions": Dict[str, "ExperimentTemplateActionTypeDef"],
        "stopConditions": List["ExperimentTemplateStopConditionTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "roleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "id": str,
        "experimentTemplateId": str,
        "roleArn": str,
        "state": "ExperimentStateTypeDef",
        "targets": Dict[str, "ExperimentTargetTypeDef"],
        "actions": Dict[str, "ExperimentActionTypeDef"],
        "stopConditions": List["ExperimentStopConditionTypeDef"],
        "creationTime": datetime,
        "startTime": datetime,
        "endTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

GetActionRequestTypeDef = TypedDict(
    "GetActionRequestTypeDef",
    {
        "id": str,
    },
)

GetActionResponseResponseTypeDef = TypedDict(
    "GetActionResponseResponseTypeDef",
    {
        "action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentRequestTypeDef = TypedDict(
    "GetExperimentRequestTypeDef",
    {
        "id": str,
    },
)

GetExperimentResponseResponseTypeDef = TypedDict(
    "GetExperimentResponseResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentTemplateRequestTypeDef = TypedDict(
    "GetExperimentTemplateRequestTypeDef",
    {
        "id": str,
    },
)

GetExperimentTemplateResponseResponseTypeDef = TypedDict(
    "GetExperimentTemplateResponseResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListActionsRequestTypeDef = TypedDict(
    "ListActionsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListActionsResponseResponseTypeDef = TypedDict(
    "ListActionsResponseResponseTypeDef",
    {
        "actions": List["ActionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentTemplatesRequestTypeDef = TypedDict(
    "ListExperimentTemplatesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExperimentTemplatesResponseResponseTypeDef = TypedDict(
    "ListExperimentTemplatesResponseResponseTypeDef",
    {
        "experimentTemplates": List["ExperimentTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentsRequestTypeDef = TypedDict(
    "ListExperimentsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExperimentsResponseResponseTypeDef = TypedDict(
    "ListExperimentsResponseResponseTypeDef",
    {
        "experiments": List["ExperimentSummaryTypeDef"],
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

_RequiredStartExperimentRequestTypeDef = TypedDict(
    "_RequiredStartExperimentRequestTypeDef",
    {
        "clientToken": str,
        "experimentTemplateId": str,
    },
)
_OptionalStartExperimentRequestTypeDef = TypedDict(
    "_OptionalStartExperimentRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class StartExperimentRequestTypeDef(
    _RequiredStartExperimentRequestTypeDef, _OptionalStartExperimentRequestTypeDef
):
    pass


StartExperimentResponseResponseTypeDef = TypedDict(
    "StartExperimentResponseResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExperimentRequestTypeDef = TypedDict(
    "StopExperimentRequestTypeDef",
    {
        "id": str,
    },
)

StopExperimentResponseResponseTypeDef = TypedDict(
    "StopExperimentResponseResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
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

_RequiredUntagResourceRequestTypeDef = TypedDict(
    "_RequiredUntagResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalUntagResourceRequestTypeDef = TypedDict(
    "_OptionalUntagResourceRequestTypeDef",
    {
        "tagKeys": List[str],
    },
    total=False,
)


class UntagResourceRequestTypeDef(
    _RequiredUntagResourceRequestTypeDef, _OptionalUntagResourceRequestTypeDef
):
    pass


UpdateExperimentTemplateActionInputItemTypeDef = TypedDict(
    "UpdateExperimentTemplateActionInputItemTypeDef",
    {
        "actionId": str,
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
    },
    total=False,
)

_RequiredUpdateExperimentTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentTemplateRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateExperimentTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentTemplateRequestTypeDef",
    {
        "description": str,
        "stopConditions": List["UpdateExperimentTemplateStopConditionInputTypeDef"],
        "targets": Dict[str, "UpdateExperimentTemplateTargetInputTypeDef"],
        "actions": Dict[str, "UpdateExperimentTemplateActionInputItemTypeDef"],
        "roleArn": str,
    },
    total=False,
)


class UpdateExperimentTemplateRequestTypeDef(
    _RequiredUpdateExperimentTemplateRequestTypeDef, _OptionalUpdateExperimentTemplateRequestTypeDef
):
    pass


UpdateExperimentTemplateResponseResponseTypeDef = TypedDict(
    "UpdateExperimentTemplateResponseResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_RequiredUpdateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
    },
)
_OptionalUpdateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_OptionalUpdateExperimentTemplateStopConditionInputTypeDef",
    {
        "value": str,
    },
    total=False,
)


class UpdateExperimentTemplateStopConditionInputTypeDef(
    _RequiredUpdateExperimentTemplateStopConditionInputTypeDef,
    _OptionalUpdateExperimentTemplateStopConditionInputTypeDef,
):
    pass


_RequiredUpdateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_RequiredUpdateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
    },
)
_OptionalUpdateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_OptionalUpdateExperimentTemplateTargetInputTypeDef",
    {
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTemplateTargetInputFilterTypeDef"],
    },
    total=False,
)


class UpdateExperimentTemplateTargetInputTypeDef(
    _RequiredUpdateExperimentTemplateTargetInputTypeDef,
    _OptionalUpdateExperimentTemplateTargetInputTypeDef,
):
    pass
