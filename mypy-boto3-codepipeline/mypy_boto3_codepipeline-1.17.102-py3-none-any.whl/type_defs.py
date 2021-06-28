"""
Type annotations for codepipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionCategoryType,
    ActionConfigurationPropertyTypeType,
    ActionExecutionStatusType,
    ActionOwnerType,
    ApprovalStatusType,
    ExecutorTypeType,
    FailureTypeType,
    JobStatusType,
    PipelineExecutionStatusType,
    StageExecutionStatusType,
    StageTransitionTypeType,
    TriggerTypeType,
    WebhookAuthenticationTypeType,
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
    "AWSSessionCredentialsTypeDef",
    "AcknowledgeJobInputTypeDef",
    "AcknowledgeJobOutputResponseTypeDef",
    "AcknowledgeThirdPartyJobInputTypeDef",
    "AcknowledgeThirdPartyJobOutputResponseTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionDeclarationTypeDef",
    "ActionExecutionDetailTypeDef",
    "ActionExecutionFilterTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionTypeDef",
    "ActionStateTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeDeclarationTypeDef",
    "ActionTypeExecutorTypeDef",
    "ActionTypeIdTypeDef",
    "ActionTypeIdentifierTypeDef",
    "ActionTypePermissionsTypeDef",
    "ActionTypePropertyTypeDef",
    "ActionTypeSettingsTypeDef",
    "ActionTypeTypeDef",
    "ActionTypeUrlsTypeDef",
    "ApprovalResultTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactDetailsTypeDef",
    "ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "ArtifactStoreTypeDef",
    "ArtifactTypeDef",
    "BlockerDeclarationTypeDef",
    "CreateCustomActionTypeInputTypeDef",
    "CreateCustomActionTypeOutputResponseTypeDef",
    "CreatePipelineInputTypeDef",
    "CreatePipelineOutputResponseTypeDef",
    "CurrentRevisionTypeDef",
    "DeleteCustomActionTypeInputTypeDef",
    "DeletePipelineInputTypeDef",
    "DeleteWebhookInputTypeDef",
    "DeregisterWebhookWithThirdPartyInputTypeDef",
    "DisableStageTransitionInputTypeDef",
    "EnableStageTransitionInputTypeDef",
    "EncryptionKeyTypeDef",
    "ErrorDetailsTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "ExecutorConfigurationTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeInputTypeDef",
    "GetActionTypeOutputResponseTypeDef",
    "GetJobDetailsInputTypeDef",
    "GetJobDetailsOutputResponseTypeDef",
    "GetPipelineExecutionInputTypeDef",
    "GetPipelineExecutionOutputResponseTypeDef",
    "GetPipelineInputTypeDef",
    "GetPipelineOutputResponseTypeDef",
    "GetPipelineStateInputTypeDef",
    "GetPipelineStateOutputResponseTypeDef",
    "GetThirdPartyJobDetailsInputTypeDef",
    "GetThirdPartyJobDetailsOutputResponseTypeDef",
    "InputArtifactTypeDef",
    "JobDataTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "ListActionExecutionsInputTypeDef",
    "ListActionExecutionsOutputResponseTypeDef",
    "ListActionTypesInputTypeDef",
    "ListActionTypesOutputResponseTypeDef",
    "ListPipelineExecutionsInputTypeDef",
    "ListPipelineExecutionsOutputResponseTypeDef",
    "ListPipelinesInputTypeDef",
    "ListPipelinesOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ListWebhookItemTypeDef",
    "ListWebhooksInputTypeDef",
    "ListWebhooksOutputResponseTypeDef",
    "OutputArtifactTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineContextTypeDef",
    "PipelineDeclarationTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineMetadataTypeDef",
    "PipelineSummaryTypeDef",
    "PollForJobsInputTypeDef",
    "PollForJobsOutputResponseTypeDef",
    "PollForThirdPartyJobsInputTypeDef",
    "PollForThirdPartyJobsOutputResponseTypeDef",
    "PutActionRevisionInputTypeDef",
    "PutActionRevisionOutputResponseTypeDef",
    "PutApprovalResultInputTypeDef",
    "PutApprovalResultOutputResponseTypeDef",
    "PutJobFailureResultInputTypeDef",
    "PutJobSuccessResultInputTypeDef",
    "PutThirdPartyJobFailureResultInputTypeDef",
    "PutThirdPartyJobSuccessResultInputTypeDef",
    "PutWebhookInputTypeDef",
    "PutWebhookOutputResponseTypeDef",
    "RegisterWebhookWithThirdPartyInputTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStageExecutionInputTypeDef",
    "RetryStageExecutionOutputResponseTypeDef",
    "S3ArtifactLocationTypeDef",
    "S3LocationTypeDef",
    "SourceRevisionTypeDef",
    "StageContextTypeDef",
    "StageDeclarationTypeDef",
    "StageExecutionTypeDef",
    "StageStateTypeDef",
    "StartPipelineExecutionInputTypeDef",
    "StartPipelineExecutionOutputResponseTypeDef",
    "StopExecutionTriggerTypeDef",
    "StopPipelineExecutionInputTypeDef",
    "StopPipelineExecutionOutputResponseTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "ThirdPartyJobTypeDef",
    "TransitionStateTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateActionTypeInputTypeDef",
    "UpdatePipelineInputTypeDef",
    "UpdatePipelineOutputResponseTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookDefinitionTypeDef",
    "WebhookFilterRuleTypeDef",
)

AWSSessionCredentialsTypeDef = TypedDict(
    "AWSSessionCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
)

AcknowledgeJobInputTypeDef = TypedDict(
    "AcknowledgeJobInputTypeDef",
    {
        "jobId": str,
        "nonce": str,
    },
)

AcknowledgeJobOutputResponseTypeDef = TypedDict(
    "AcknowledgeJobOutputResponseTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcknowledgeThirdPartyJobInputTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobInputTypeDef",
    {
        "jobId": str,
        "nonce": str,
        "clientToken": str,
    },
)

AcknowledgeThirdPartyJobOutputResponseTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobOutputResponseTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActionConfigurationPropertyTypeDef = TypedDict(
    "_RequiredActionConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
    },
)
_OptionalActionConfigurationPropertyTypeDef = TypedDict(
    "_OptionalActionConfigurationPropertyTypeDef",
    {
        "queryable": bool,
        "description": str,
        "type": ActionConfigurationPropertyTypeType,
    },
    total=False,
)


class ActionConfigurationPropertyTypeDef(
    _RequiredActionConfigurationPropertyTypeDef, _OptionalActionConfigurationPropertyTypeDef
):
    pass


ActionConfigurationTypeDef = TypedDict(
    "ActionConfigurationTypeDef",
    {
        "configuration": Dict[str, str],
    },
    total=False,
)

ActionContextTypeDef = TypedDict(
    "ActionContextTypeDef",
    {
        "name": str,
        "actionExecutionId": str,
    },
    total=False,
)

_RequiredActionDeclarationTypeDef = TypedDict(
    "_RequiredActionDeclarationTypeDef",
    {
        "name": str,
        "actionTypeId": "ActionTypeIdTypeDef",
    },
)
_OptionalActionDeclarationTypeDef = TypedDict(
    "_OptionalActionDeclarationTypeDef",
    {
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List["OutputArtifactTypeDef"],
        "inputArtifacts": List["InputArtifactTypeDef"],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ActionDeclarationTypeDef(
    _RequiredActionDeclarationTypeDef, _OptionalActionDeclarationTypeDef
):
    pass


ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": ActionExecutionStatusType,
        "input": "ActionExecutionInputTypeDef",
        "output": "ActionExecutionOutputTypeDef",
    },
    total=False,
)

ActionExecutionFilterTypeDef = TypedDict(
    "ActionExecutionFilterTypeDef",
    {
        "pipelineExecutionId": str,
    },
    total=False,
)

ActionExecutionInputTypeDef = TypedDict(
    "ActionExecutionInputTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List["ArtifactDetailTypeDef"],
        "namespace": str,
    },
    total=False,
)

ActionExecutionOutputTypeDef = TypedDict(
    "ActionExecutionOutputTypeDef",
    {
        "outputArtifacts": List["ArtifactDetailTypeDef"],
        "executionResult": "ActionExecutionResultTypeDef",
        "outputVariables": Dict[str, str],
    },
    total=False,
)

ActionExecutionResultTypeDef = TypedDict(
    "ActionExecutionResultTypeDef",
    {
        "externalExecutionId": str,
        "externalExecutionSummary": str,
        "externalExecutionUrl": str,
    },
    total=False,
)

ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "actionExecutionId": str,
        "status": ActionExecutionStatusType,
        "summary": str,
        "lastStatusChange": datetime,
        "token": str,
        "lastUpdatedBy": str,
        "externalExecutionId": str,
        "externalExecutionUrl": str,
        "percentComplete": int,
        "errorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

ActionRevisionTypeDef = TypedDict(
    "ActionRevisionTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": datetime,
    },
)

ActionStateTypeDef = TypedDict(
    "ActionStateTypeDef",
    {
        "actionName": str,
        "currentRevision": "ActionRevisionTypeDef",
        "latestExecution": "ActionExecutionTypeDef",
        "entityUrl": str,
        "revisionUrl": str,
    },
    total=False,
)

ActionTypeArtifactDetailsTypeDef = TypedDict(
    "ActionTypeArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

_RequiredActionTypeDeclarationTypeDef = TypedDict(
    "_RequiredActionTypeDeclarationTypeDef",
    {
        "executor": "ActionTypeExecutorTypeDef",
        "id": "ActionTypeIdentifierTypeDef",
        "inputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
        "outputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
    },
)
_OptionalActionTypeDeclarationTypeDef = TypedDict(
    "_OptionalActionTypeDeclarationTypeDef",
    {
        "description": str,
        "permissions": "ActionTypePermissionsTypeDef",
        "properties": List["ActionTypePropertyTypeDef"],
        "urls": "ActionTypeUrlsTypeDef",
    },
    total=False,
)


class ActionTypeDeclarationTypeDef(
    _RequiredActionTypeDeclarationTypeDef, _OptionalActionTypeDeclarationTypeDef
):
    pass


_RequiredActionTypeExecutorTypeDef = TypedDict(
    "_RequiredActionTypeExecutorTypeDef",
    {
        "configuration": "ExecutorConfigurationTypeDef",
        "type": ExecutorTypeType,
    },
)
_OptionalActionTypeExecutorTypeDef = TypedDict(
    "_OptionalActionTypeExecutorTypeDef",
    {
        "policyStatementsTemplate": str,
        "jobTimeout": int,
    },
    total=False,
)


class ActionTypeExecutorTypeDef(
    _RequiredActionTypeExecutorTypeDef, _OptionalActionTypeExecutorTypeDef
):
    pass


ActionTypeIdTypeDef = TypedDict(
    "ActionTypeIdTypeDef",
    {
        "category": ActionCategoryType,
        "owner": ActionOwnerType,
        "provider": str,
        "version": str,
    },
)

ActionTypeIdentifierTypeDef = TypedDict(
    "ActionTypeIdentifierTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

ActionTypePermissionsTypeDef = TypedDict(
    "ActionTypePermissionsTypeDef",
    {
        "allowedAccounts": List[str],
    },
)

_RequiredActionTypePropertyTypeDef = TypedDict(
    "_RequiredActionTypePropertyTypeDef",
    {
        "name": str,
        "optional": bool,
        "key": bool,
        "noEcho": bool,
    },
)
_OptionalActionTypePropertyTypeDef = TypedDict(
    "_OptionalActionTypePropertyTypeDef",
    {
        "queryable": bool,
        "description": str,
    },
    total=False,
)


class ActionTypePropertyTypeDef(
    _RequiredActionTypePropertyTypeDef, _OptionalActionTypePropertyTypeDef
):
    pass


ActionTypeSettingsTypeDef = TypedDict(
    "ActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

_RequiredActionTypeTypeDef = TypedDict(
    "_RequiredActionTypeTypeDef",
    {
        "id": "ActionTypeIdTypeDef",
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
    },
)
_OptionalActionTypeTypeDef = TypedDict(
    "_OptionalActionTypeTypeDef",
    {
        "settings": "ActionTypeSettingsTypeDef",
        "actionConfigurationProperties": List["ActionConfigurationPropertyTypeDef"],
    },
    total=False,
)


class ActionTypeTypeDef(_RequiredActionTypeTypeDef, _OptionalActionTypeTypeDef):
    pass


ActionTypeUrlsTypeDef = TypedDict(
    "ActionTypeUrlsTypeDef",
    {
        "configurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ApprovalResultTypeDef = TypedDict(
    "ApprovalResultTypeDef",
    {
        "summary": str,
        "status": ApprovalStatusType,
    },
)

ArtifactDetailTypeDef = TypedDict(
    "ArtifactDetailTypeDef",
    {
        "name": str,
        "s3location": "S3LocationTypeDef",
    },
    total=False,
)

ArtifactDetailsTypeDef = TypedDict(
    "ArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {
        "type": Literal["S3"],
        "s3Location": "S3ArtifactLocationTypeDef",
    },
    total=False,
)

ArtifactRevisionTypeDef = TypedDict(
    "ArtifactRevisionTypeDef",
    {
        "name": str,
        "revisionId": str,
        "revisionChangeIdentifier": str,
        "revisionSummary": str,
        "created": datetime,
        "revisionUrl": str,
    },
    total=False,
)

_RequiredArtifactStoreTypeDef = TypedDict(
    "_RequiredArtifactStoreTypeDef",
    {
        "type": Literal["S3"],
        "location": str,
    },
)
_OptionalArtifactStoreTypeDef = TypedDict(
    "_OptionalArtifactStoreTypeDef",
    {
        "encryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)


class ArtifactStoreTypeDef(_RequiredArtifactStoreTypeDef, _OptionalArtifactStoreTypeDef):
    pass


ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "name": str,
        "revision": str,
        "location": "ArtifactLocationTypeDef",
    },
    total=False,
)

BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef",
    {
        "name": str,
        "type": Literal["Schedule"],
    },
)

_RequiredCreateCustomActionTypeInputTypeDef = TypedDict(
    "_RequiredCreateCustomActionTypeInputTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
    },
)
_OptionalCreateCustomActionTypeInputTypeDef = TypedDict(
    "_OptionalCreateCustomActionTypeInputTypeDef",
    {
        "settings": "ActionTypeSettingsTypeDef",
        "configurationProperties": List["ActionConfigurationPropertyTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCustomActionTypeInputTypeDef(
    _RequiredCreateCustomActionTypeInputTypeDef, _OptionalCreateCustomActionTypeInputTypeDef
):
    pass


CreateCustomActionTypeOutputResponseTypeDef = TypedDict(
    "CreateCustomActionTypeOutputResponseTypeDef",
    {
        "actionType": "ActionTypeTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineInputTypeDef = TypedDict(
    "_RequiredCreatePipelineInputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
    },
)
_OptionalCreatePipelineInputTypeDef = TypedDict(
    "_OptionalCreatePipelineInputTypeDef",
    {
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
        "pipeline": "PipelineDeclarationTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCurrentRevisionTypeDef = TypedDict(
    "_RequiredCurrentRevisionTypeDef",
    {
        "revision": str,
        "changeIdentifier": str,
    },
)
_OptionalCurrentRevisionTypeDef = TypedDict(
    "_OptionalCurrentRevisionTypeDef",
    {
        "created": Union[datetime, str],
        "revisionSummary": str,
    },
    total=False,
)


class CurrentRevisionTypeDef(_RequiredCurrentRevisionTypeDef, _OptionalCurrentRevisionTypeDef):
    pass


DeleteCustomActionTypeInputTypeDef = TypedDict(
    "DeleteCustomActionTypeInputTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
    },
)

DeletePipelineInputTypeDef = TypedDict(
    "DeletePipelineInputTypeDef",
    {
        "name": str,
    },
)

DeleteWebhookInputTypeDef = TypedDict(
    "DeleteWebhookInputTypeDef",
    {
        "name": str,
    },
)

DeregisterWebhookWithThirdPartyInputTypeDef = TypedDict(
    "DeregisterWebhookWithThirdPartyInputTypeDef",
    {
        "webhookName": str,
    },
    total=False,
)

DisableStageTransitionInputTypeDef = TypedDict(
    "DisableStageTransitionInputTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
        "reason": str,
    },
)

EnableStageTransitionInputTypeDef = TypedDict(
    "EnableStageTransitionInputTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
    },
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "id": str,
        "type": Literal["KMS"],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "summary": str,
        "externalExecutionId": str,
        "percentComplete": int,
    },
    total=False,
)

ExecutionTriggerTypeDef = TypedDict(
    "ExecutionTriggerTypeDef",
    {
        "triggerType": TriggerTypeType,
        "triggerDetail": str,
    },
    total=False,
)

ExecutorConfigurationTypeDef = TypedDict(
    "ExecutorConfigurationTypeDef",
    {
        "lambdaExecutorConfiguration": "LambdaExecutorConfigurationTypeDef",
        "jobWorkerExecutorConfiguration": "JobWorkerExecutorConfigurationTypeDef",
    },
    total=False,
)

_RequiredFailureDetailsTypeDef = TypedDict(
    "_RequiredFailureDetailsTypeDef",
    {
        "type": FailureTypeType,
        "message": str,
    },
)
_OptionalFailureDetailsTypeDef = TypedDict(
    "_OptionalFailureDetailsTypeDef",
    {
        "externalExecutionId": str,
    },
    total=False,
)


class FailureDetailsTypeDef(_RequiredFailureDetailsTypeDef, _OptionalFailureDetailsTypeDef):
    pass


GetActionTypeInputTypeDef = TypedDict(
    "GetActionTypeInputTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

GetActionTypeOutputResponseTypeDef = TypedDict(
    "GetActionTypeOutputResponseTypeDef",
    {
        "actionType": "ActionTypeDeclarationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobDetailsInputTypeDef = TypedDict(
    "GetJobDetailsInputTypeDef",
    {
        "jobId": str,
    },
)

GetJobDetailsOutputResponseTypeDef = TypedDict(
    "GetJobDetailsOutputResponseTypeDef",
    {
        "jobDetails": "JobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineExecutionInputTypeDef = TypedDict(
    "GetPipelineExecutionInputTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)

GetPipelineExecutionOutputResponseTypeDef = TypedDict(
    "GetPipelineExecutionOutputResponseTypeDef",
    {
        "pipelineExecution": "PipelineExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPipelineInputTypeDef = TypedDict(
    "_RequiredGetPipelineInputTypeDef",
    {
        "name": str,
    },
)
_OptionalGetPipelineInputTypeDef = TypedDict(
    "_OptionalGetPipelineInputTypeDef",
    {
        "version": int,
    },
    total=False,
)


class GetPipelineInputTypeDef(_RequiredGetPipelineInputTypeDef, _OptionalGetPipelineInputTypeDef):
    pass


GetPipelineOutputResponseTypeDef = TypedDict(
    "GetPipelineOutputResponseTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "metadata": "PipelineMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineStateInputTypeDef = TypedDict(
    "GetPipelineStateInputTypeDef",
    {
        "name": str,
    },
)

GetPipelineStateOutputResponseTypeDef = TypedDict(
    "GetPipelineStateOutputResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List["StageStateTypeDef"],
        "created": datetime,
        "updated": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThirdPartyJobDetailsInputTypeDef = TypedDict(
    "GetThirdPartyJobDetailsInputTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)

GetThirdPartyJobDetailsOutputResponseTypeDef = TypedDict(
    "GetThirdPartyJobDetailsOutputResponseTypeDef",
    {
        "jobDetails": "ThirdPartyJobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputArtifactTypeDef = TypedDict(
    "InputArtifactTypeDef",
    {
        "name": str,
    },
)

JobDataTypeDef = TypedDict(
    "JobDataTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "actionConfiguration": "ActionConfigurationTypeDef",
        "pipelineContext": "PipelineContextTypeDef",
        "inputArtifacts": List["ArtifactTypeDef"],
        "outputArtifacts": List["ArtifactTypeDef"],
        "artifactCredentials": "AWSSessionCredentialsTypeDef",
        "continuationToken": str,
        "encryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "id": str,
        "data": "JobDataTypeDef",
        "accountId": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "id": str,
        "data": "JobDataTypeDef",
        "nonce": str,
        "accountId": str,
    },
    total=False,
)

JobWorkerExecutorConfigurationTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationTypeDef",
    {
        "pollingAccounts": List[str],
        "pollingServicePrincipals": List[str],
    },
    total=False,
)

LambdaExecutorConfigurationTypeDef = TypedDict(
    "LambdaExecutorConfigurationTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

_RequiredListActionExecutionsInputTypeDef = TypedDict(
    "_RequiredListActionExecutionsInputTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListActionExecutionsInputTypeDef = TypedDict(
    "_OptionalListActionExecutionsInputTypeDef",
    {
        "filter": "ActionExecutionFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListActionExecutionsInputTypeDef(
    _RequiredListActionExecutionsInputTypeDef, _OptionalListActionExecutionsInputTypeDef
):
    pass


ListActionExecutionsOutputResponseTypeDef = TypedDict(
    "ListActionExecutionsOutputResponseTypeDef",
    {
        "actionExecutionDetails": List["ActionExecutionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListActionTypesInputTypeDef = TypedDict(
    "ListActionTypesInputTypeDef",
    {
        "actionOwnerFilter": ActionOwnerType,
        "nextToken": str,
        "regionFilter": str,
    },
    total=False,
)

ListActionTypesOutputResponseTypeDef = TypedDict(
    "ListActionTypesOutputResponseTypeDef",
    {
        "actionTypes": List["ActionTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPipelineExecutionsInputTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsInputTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListPipelineExecutionsInputTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListPipelineExecutionsInputTypeDef(
    _RequiredListPipelineExecutionsInputTypeDef, _OptionalListPipelineExecutionsInputTypeDef
):
    pass


ListPipelineExecutionsOutputResponseTypeDef = TypedDict(
    "ListPipelineExecutionsOutputResponseTypeDef",
    {
        "pipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesInputTypeDef = TypedDict(
    "ListPipelinesInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPipelinesOutputResponseTypeDef = TypedDict(
    "ListPipelinesOutputResponseTypeDef",
    {
        "pipelines": List["PipelineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebhookItemTypeDef = TypedDict(
    "_RequiredListWebhookItemTypeDef",
    {
        "definition": "WebhookDefinitionTypeDef",
        "url": str,
    },
)
_OptionalListWebhookItemTypeDef = TypedDict(
    "_OptionalListWebhookItemTypeDef",
    {
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class ListWebhookItemTypeDef(_RequiredListWebhookItemTypeDef, _OptionalListWebhookItemTypeDef):
    pass


ListWebhooksInputTypeDef = TypedDict(
    "ListWebhooksInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWebhooksOutputResponseTypeDef = TypedDict(
    "ListWebhooksOutputResponseTypeDef",
    {
        "webhooks": List["ListWebhookItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputArtifactTypeDef = TypedDict(
    "OutputArtifactTypeDef",
    {
        "name": str,
    },
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

PipelineContextTypeDef = TypedDict(
    "PipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": "StageContextTypeDef",
        "action": "ActionContextTypeDef",
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)

_RequiredPipelineDeclarationTypeDef = TypedDict(
    "_RequiredPipelineDeclarationTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": List["StageDeclarationTypeDef"],
    },
)
_OptionalPipelineDeclarationTypeDef = TypedDict(
    "_OptionalPipelineDeclarationTypeDef",
    {
        "artifactStore": "ArtifactStoreTypeDef",
        "artifactStores": Dict[str, "ArtifactStoreTypeDef"],
        "version": int,
    },
    total=False,
)


class PipelineDeclarationTypeDef(
    _RequiredPipelineDeclarationTypeDef, _OptionalPipelineDeclarationTypeDef
):
    pass


PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "pipelineExecutionId": str,
        "status": PipelineExecutionStatusType,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List["SourceRevisionTypeDef"],
        "trigger": "ExecutionTriggerTypeDef",
        "stopTrigger": "StopExecutionTriggerTypeDef",
    },
    total=False,
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "pipelineExecutionId": str,
        "status": PipelineExecutionStatusType,
        "statusSummary": str,
        "artifactRevisions": List["ArtifactRevisionTypeDef"],
    },
    total=False,
)

PipelineMetadataTypeDef = TypedDict(
    "PipelineMetadataTypeDef",
    {
        "pipelineArn": str,
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "name": str,
        "version": int,
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)

_RequiredPollForJobsInputTypeDef = TypedDict(
    "_RequiredPollForJobsInputTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
    },
)
_OptionalPollForJobsInputTypeDef = TypedDict(
    "_OptionalPollForJobsInputTypeDef",
    {
        "maxBatchSize": int,
        "queryParam": Dict[str, str],
    },
    total=False,
)


class PollForJobsInputTypeDef(_RequiredPollForJobsInputTypeDef, _OptionalPollForJobsInputTypeDef):
    pass


PollForJobsOutputResponseTypeDef = TypedDict(
    "PollForJobsOutputResponseTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPollForThirdPartyJobsInputTypeDef = TypedDict(
    "_RequiredPollForThirdPartyJobsInputTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
    },
)
_OptionalPollForThirdPartyJobsInputTypeDef = TypedDict(
    "_OptionalPollForThirdPartyJobsInputTypeDef",
    {
        "maxBatchSize": int,
    },
    total=False,
)


class PollForThirdPartyJobsInputTypeDef(
    _RequiredPollForThirdPartyJobsInputTypeDef, _OptionalPollForThirdPartyJobsInputTypeDef
):
    pass


PollForThirdPartyJobsOutputResponseTypeDef = TypedDict(
    "PollForThirdPartyJobsOutputResponseTypeDef",
    {
        "jobs": List["ThirdPartyJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutActionRevisionInputTypeDef = TypedDict(
    "PutActionRevisionInputTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "actionRevision": "ActionRevisionTypeDef",
    },
)

PutActionRevisionOutputResponseTypeDef = TypedDict(
    "PutActionRevisionOutputResponseTypeDef",
    {
        "newRevision": bool,
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutApprovalResultInputTypeDef = TypedDict(
    "PutApprovalResultInputTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "result": "ApprovalResultTypeDef",
        "token": str,
    },
)

PutApprovalResultOutputResponseTypeDef = TypedDict(
    "PutApprovalResultOutputResponseTypeDef",
    {
        "approvedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutJobFailureResultInputTypeDef = TypedDict(
    "PutJobFailureResultInputTypeDef",
    {
        "jobId": str,
        "failureDetails": "FailureDetailsTypeDef",
    },
)

_RequiredPutJobSuccessResultInputTypeDef = TypedDict(
    "_RequiredPutJobSuccessResultInputTypeDef",
    {
        "jobId": str,
    },
)
_OptionalPutJobSuccessResultInputTypeDef = TypedDict(
    "_OptionalPutJobSuccessResultInputTypeDef",
    {
        "currentRevision": "CurrentRevisionTypeDef",
        "continuationToken": str,
        "executionDetails": "ExecutionDetailsTypeDef",
        "outputVariables": Dict[str, str],
    },
    total=False,
)


class PutJobSuccessResultInputTypeDef(
    _RequiredPutJobSuccessResultInputTypeDef, _OptionalPutJobSuccessResultInputTypeDef
):
    pass


PutThirdPartyJobFailureResultInputTypeDef = TypedDict(
    "PutThirdPartyJobFailureResultInputTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "failureDetails": "FailureDetailsTypeDef",
    },
)

_RequiredPutThirdPartyJobSuccessResultInputTypeDef = TypedDict(
    "_RequiredPutThirdPartyJobSuccessResultInputTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)
_OptionalPutThirdPartyJobSuccessResultInputTypeDef = TypedDict(
    "_OptionalPutThirdPartyJobSuccessResultInputTypeDef",
    {
        "currentRevision": "CurrentRevisionTypeDef",
        "continuationToken": str,
        "executionDetails": "ExecutionDetailsTypeDef",
    },
    total=False,
)


class PutThirdPartyJobSuccessResultInputTypeDef(
    _RequiredPutThirdPartyJobSuccessResultInputTypeDef,
    _OptionalPutThirdPartyJobSuccessResultInputTypeDef,
):
    pass


_RequiredPutWebhookInputTypeDef = TypedDict(
    "_RequiredPutWebhookInputTypeDef",
    {
        "webhook": "WebhookDefinitionTypeDef",
    },
)
_OptionalPutWebhookInputTypeDef = TypedDict(
    "_OptionalPutWebhookInputTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutWebhookInputTypeDef(_RequiredPutWebhookInputTypeDef, _OptionalPutWebhookInputTypeDef):
    pass


PutWebhookOutputResponseTypeDef = TypedDict(
    "PutWebhookOutputResponseTypeDef",
    {
        "webhook": "ListWebhookItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterWebhookWithThirdPartyInputTypeDef = TypedDict(
    "RegisterWebhookWithThirdPartyInputTypeDef",
    {
        "webhookName": str,
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

RetryStageExecutionInputTypeDef = TypedDict(
    "RetryStageExecutionInputTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "pipelineExecutionId": str,
        "retryMode": Literal["FAILED_ACTIONS"],
    },
)

RetryStageExecutionOutputResponseTypeDef = TypedDict(
    "RetryStageExecutionOutputResponseTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ArtifactLocationTypeDef = TypedDict(
    "S3ArtifactLocationTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

_RequiredSourceRevisionTypeDef = TypedDict(
    "_RequiredSourceRevisionTypeDef",
    {
        "actionName": str,
    },
)
_OptionalSourceRevisionTypeDef = TypedDict(
    "_OptionalSourceRevisionTypeDef",
    {
        "revisionId": str,
        "revisionSummary": str,
        "revisionUrl": str,
    },
    total=False,
)


class SourceRevisionTypeDef(_RequiredSourceRevisionTypeDef, _OptionalSourceRevisionTypeDef):
    pass


StageContextTypeDef = TypedDict(
    "StageContextTypeDef",
    {
        "name": str,
    },
    total=False,
)

_RequiredStageDeclarationTypeDef = TypedDict(
    "_RequiredStageDeclarationTypeDef",
    {
        "name": str,
        "actions": List["ActionDeclarationTypeDef"],
    },
)
_OptionalStageDeclarationTypeDef = TypedDict(
    "_OptionalStageDeclarationTypeDef",
    {
        "blockers": List["BlockerDeclarationTypeDef"],
    },
    total=False,
)


class StageDeclarationTypeDef(_RequiredStageDeclarationTypeDef, _OptionalStageDeclarationTypeDef):
    pass


StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": StageExecutionStatusType,
    },
)

StageStateTypeDef = TypedDict(
    "StageStateTypeDef",
    {
        "stageName": str,
        "inboundExecution": "StageExecutionTypeDef",
        "inboundTransitionState": "TransitionStateTypeDef",
        "actionStates": List["ActionStateTypeDef"],
        "latestExecution": "StageExecutionTypeDef",
    },
    total=False,
)

_RequiredStartPipelineExecutionInputTypeDef = TypedDict(
    "_RequiredStartPipelineExecutionInputTypeDef",
    {
        "name": str,
    },
)
_OptionalStartPipelineExecutionInputTypeDef = TypedDict(
    "_OptionalStartPipelineExecutionInputTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class StartPipelineExecutionInputTypeDef(
    _RequiredStartPipelineExecutionInputTypeDef, _OptionalStartPipelineExecutionInputTypeDef
):
    pass


StartPipelineExecutionOutputResponseTypeDef = TypedDict(
    "StartPipelineExecutionOutputResponseTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExecutionTriggerTypeDef = TypedDict(
    "StopExecutionTriggerTypeDef",
    {
        "reason": str,
    },
    total=False,
)

_RequiredStopPipelineExecutionInputTypeDef = TypedDict(
    "_RequiredStopPipelineExecutionInputTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)
_OptionalStopPipelineExecutionInputTypeDef = TypedDict(
    "_OptionalStopPipelineExecutionInputTypeDef",
    {
        "abandon": bool,
        "reason": str,
    },
    total=False,
)


class StopPipelineExecutionInputTypeDef(
    _RequiredStopPipelineExecutionInputTypeDef, _OptionalStopPipelineExecutionInputTypeDef
):
    pass


StopPipelineExecutionOutputResponseTypeDef = TypedDict(
    "StopPipelineExecutionOutputResponseTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "resourceArn": str,
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

ThirdPartyJobDataTypeDef = TypedDict(
    "ThirdPartyJobDataTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "actionConfiguration": "ActionConfigurationTypeDef",
        "pipelineContext": "PipelineContextTypeDef",
        "inputArtifacts": List["ArtifactTypeDef"],
        "outputArtifacts": List["ArtifactTypeDef"],
        "artifactCredentials": "AWSSessionCredentialsTypeDef",
        "continuationToken": str,
        "encryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {
        "id": str,
        "data": "ThirdPartyJobDataTypeDef",
        "nonce": str,
    },
    total=False,
)

ThirdPartyJobTypeDef = TypedDict(
    "ThirdPartyJobTypeDef",
    {
        "clientId": str,
        "jobId": str,
    },
    total=False,
)

TransitionStateTypeDef = TypedDict(
    "TransitionStateTypeDef",
    {
        "enabled": bool,
        "lastChangedBy": str,
        "lastChangedAt": datetime,
        "disabledReason": str,
    },
    total=False,
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateActionTypeInputTypeDef = TypedDict(
    "UpdateActionTypeInputTypeDef",
    {
        "actionType": "ActionTypeDeclarationTypeDef",
    },
)

UpdatePipelineInputTypeDef = TypedDict(
    "UpdatePipelineInputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
    },
)

UpdatePipelineOutputResponseTypeDef = TypedDict(
    "UpdatePipelineOutputResponseTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WebhookAuthConfigurationTypeDef = TypedDict(
    "WebhookAuthConfigurationTypeDef",
    {
        "AllowedIPRange": str,
        "SecretToken": str,
    },
    total=False,
)

WebhookDefinitionTypeDef = TypedDict(
    "WebhookDefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List["WebhookFilterRuleTypeDef"],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": "WebhookAuthConfigurationTypeDef",
    },
)

_RequiredWebhookFilterRuleTypeDef = TypedDict(
    "_RequiredWebhookFilterRuleTypeDef",
    {
        "jsonPath": str,
    },
)
_OptionalWebhookFilterRuleTypeDef = TypedDict(
    "_OptionalWebhookFilterRuleTypeDef",
    {
        "matchEquals": str,
    },
    total=False,
)


class WebhookFilterRuleTypeDef(
    _RequiredWebhookFilterRuleTypeDef, _OptionalWebhookFilterRuleTypeDef
):
    pass
