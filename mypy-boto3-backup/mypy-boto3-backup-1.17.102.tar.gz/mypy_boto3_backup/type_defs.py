"""
Type annotations for backup service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs.html)

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingTypeDef

    data: AdvancedBackupSettingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    BackupJobStateType,
    BackupVaultEventType,
    CopyJobStateType,
    RecoveryPointStatusType,
    RestoreJobStatusType,
    StorageClassType,
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
    "AdvancedBackupSettingTypeDef",
    "BackupJobTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "BackupPlanTypeDef",
    "BackupPlansListMemberTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "BackupSelectionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "ConditionTypeDef",
    "CopyActionTypeDef",
    "CopyJobTypeDef",
    "CreateBackupPlanInputTypeDef",
    "CreateBackupPlanOutputResponseTypeDef",
    "CreateBackupSelectionInputTypeDef",
    "CreateBackupSelectionOutputResponseTypeDef",
    "CreateBackupVaultInputTypeDef",
    "CreateBackupVaultOutputResponseTypeDef",
    "DeleteBackupPlanInputTypeDef",
    "DeleteBackupPlanOutputResponseTypeDef",
    "DeleteBackupSelectionInputTypeDef",
    "DeleteBackupVaultAccessPolicyInputTypeDef",
    "DeleteBackupVaultInputTypeDef",
    "DeleteBackupVaultNotificationsInputTypeDef",
    "DeleteRecoveryPointInputTypeDef",
    "DescribeBackupJobInputTypeDef",
    "DescribeBackupJobOutputResponseTypeDef",
    "DescribeBackupVaultInputTypeDef",
    "DescribeBackupVaultOutputResponseTypeDef",
    "DescribeCopyJobInputTypeDef",
    "DescribeCopyJobOutputResponseTypeDef",
    "DescribeGlobalSettingsOutputResponseTypeDef",
    "DescribeProtectedResourceInputTypeDef",
    "DescribeProtectedResourceOutputResponseTypeDef",
    "DescribeRecoveryPointInputTypeDef",
    "DescribeRecoveryPointOutputResponseTypeDef",
    "DescribeRegionSettingsOutputResponseTypeDef",
    "DescribeRestoreJobInputTypeDef",
    "DescribeRestoreJobOutputResponseTypeDef",
    "DisassociateRecoveryPointInputTypeDef",
    "ExportBackupPlanTemplateInputTypeDef",
    "ExportBackupPlanTemplateOutputResponseTypeDef",
    "GetBackupPlanFromJSONInputTypeDef",
    "GetBackupPlanFromJSONOutputResponseTypeDef",
    "GetBackupPlanFromTemplateInputTypeDef",
    "GetBackupPlanFromTemplateOutputResponseTypeDef",
    "GetBackupPlanInputTypeDef",
    "GetBackupPlanOutputResponseTypeDef",
    "GetBackupSelectionInputTypeDef",
    "GetBackupSelectionOutputResponseTypeDef",
    "GetBackupVaultAccessPolicyInputTypeDef",
    "GetBackupVaultAccessPolicyOutputResponseTypeDef",
    "GetBackupVaultNotificationsInputTypeDef",
    "GetBackupVaultNotificationsOutputResponseTypeDef",
    "GetRecoveryPointRestoreMetadataInputTypeDef",
    "GetRecoveryPointRestoreMetadataOutputResponseTypeDef",
    "GetSupportedResourceTypesOutputResponseTypeDef",
    "LifecycleTypeDef",
    "ListBackupJobsInputTypeDef",
    "ListBackupJobsOutputResponseTypeDef",
    "ListBackupPlanTemplatesInputTypeDef",
    "ListBackupPlanTemplatesOutputResponseTypeDef",
    "ListBackupPlanVersionsInputTypeDef",
    "ListBackupPlanVersionsOutputResponseTypeDef",
    "ListBackupPlansInputTypeDef",
    "ListBackupPlansOutputResponseTypeDef",
    "ListBackupSelectionsInputTypeDef",
    "ListBackupSelectionsOutputResponseTypeDef",
    "ListBackupVaultsInputTypeDef",
    "ListBackupVaultsOutputResponseTypeDef",
    "ListCopyJobsInputTypeDef",
    "ListCopyJobsOutputResponseTypeDef",
    "ListProtectedResourcesInputTypeDef",
    "ListProtectedResourcesOutputResponseTypeDef",
    "ListRecoveryPointsByBackupVaultInputTypeDef",
    "ListRecoveryPointsByBackupVaultOutputResponseTypeDef",
    "ListRecoveryPointsByResourceInputTypeDef",
    "ListRecoveryPointsByResourceOutputResponseTypeDef",
    "ListRestoreJobsInputTypeDef",
    "ListRestoreJobsOutputResponseTypeDef",
    "ListTagsInputTypeDef",
    "ListTagsOutputResponseTypeDef",
    "ProtectedResourceTypeDef",
    "PutBackupVaultAccessPolicyInputTypeDef",
    "PutBackupVaultNotificationsInputTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "RecoveryPointByResourceTypeDef",
    "RecoveryPointCreatorTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreJobsListMemberTypeDef",
    "StartBackupJobInputTypeDef",
    "StartBackupJobOutputResponseTypeDef",
    "StartCopyJobInputTypeDef",
    "StartCopyJobOutputResponseTypeDef",
    "StartRestoreJobInputTypeDef",
    "StartRestoreJobOutputResponseTypeDef",
    "StopBackupJobInputTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateBackupPlanInputTypeDef",
    "UpdateBackupPlanOutputResponseTypeDef",
    "UpdateGlobalSettingsInputTypeDef",
    "UpdateRecoveryPointLifecycleInputTypeDef",
    "UpdateRecoveryPointLifecycleOutputResponseTypeDef",
    "UpdateRegionSettingsInputTypeDef",
)

AdvancedBackupSettingTypeDef = TypedDict(
    "AdvancedBackupSettingTypeDef",
    {
        "ResourceType": str,
        "BackupOptions": Dict[str, str],
    },
    total=False,
)

BackupJobTypeDef = TypedDict(
    "BackupJobTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "ResourceType": str,
        "BytesTransferred": int,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
    },
    total=False,
)

_RequiredBackupPlanInputTypeDef = TypedDict(
    "_RequiredBackupPlanInputTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List["BackupRuleInputTypeDef"],
    },
)
_OptionalBackupPlanInputTypeDef = TypedDict(
    "_OptionalBackupPlanInputTypeDef",
    {
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
    },
    total=False,
)


class BackupPlanInputTypeDef(_RequiredBackupPlanInputTypeDef, _OptionalBackupPlanInputTypeDef):
    pass


BackupPlanTemplatesListMemberTypeDef = TypedDict(
    "BackupPlanTemplatesListMemberTypeDef",
    {
        "BackupPlanTemplateId": str,
        "BackupPlanTemplateName": str,
    },
    total=False,
)

_RequiredBackupPlanTypeDef = TypedDict(
    "_RequiredBackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List["BackupRuleTypeDef"],
    },
)
_OptionalBackupPlanTypeDef = TypedDict(
    "_OptionalBackupPlanTypeDef",
    {
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
    },
    total=False,
)


class BackupPlanTypeDef(_RequiredBackupPlanTypeDef, _OptionalBackupPlanTypeDef):
    pass


BackupPlansListMemberTypeDef = TypedDict(
    "BackupPlansListMemberTypeDef",
    {
        "BackupPlanArn": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "VersionId": str,
        "BackupPlanName": str,
        "CreatorRequestId": str,
        "LastExecutionDate": datetime,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
    },
    total=False,
)

_RequiredBackupRuleInputTypeDef = TypedDict(
    "_RequiredBackupRuleInputTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
    },
)
_OptionalBackupRuleInputTypeDef = TypedDict(
    "_OptionalBackupRuleInputTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": "LifecycleTypeDef",
        "RecoveryPointTags": Dict[str, str],
        "CopyActions": List["CopyActionTypeDef"],
        "EnableContinuousBackup": bool,
    },
    total=False,
)


class BackupRuleInputTypeDef(_RequiredBackupRuleInputTypeDef, _OptionalBackupRuleInputTypeDef):
    pass


_RequiredBackupRuleTypeDef = TypedDict(
    "_RequiredBackupRuleTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
    },
)
_OptionalBackupRuleTypeDef = TypedDict(
    "_OptionalBackupRuleTypeDef",
    {
        "ScheduleExpression": str,
        "StartWindowMinutes": int,
        "CompletionWindowMinutes": int,
        "Lifecycle": "LifecycleTypeDef",
        "RecoveryPointTags": Dict[str, str],
        "RuleId": str,
        "CopyActions": List["CopyActionTypeDef"],
        "EnableContinuousBackup": bool,
    },
    total=False,
)


class BackupRuleTypeDef(_RequiredBackupRuleTypeDef, _OptionalBackupRuleTypeDef):
    pass


_RequiredBackupSelectionTypeDef = TypedDict(
    "_RequiredBackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
    },
)
_OptionalBackupSelectionTypeDef = TypedDict(
    "_OptionalBackupSelectionTypeDef",
    {
        "Resources": List[str],
        "ListOfTags": List["ConditionTypeDef"],
    },
    total=False,
)


class BackupSelectionTypeDef(_RequiredBackupSelectionTypeDef, _OptionalBackupSelectionTypeDef):
    pass


BackupSelectionsListMemberTypeDef = TypedDict(
    "BackupSelectionsListMemberTypeDef",
    {
        "SelectionId": str,
        "SelectionName": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "IamRoleArn": str,
    },
    total=False,
)

BackupVaultListMemberTypeDef = TypedDict(
    "BackupVaultListMemberTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
    },
    total=False,
)

CalculatedLifecycleTypeDef = TypedDict(
    "CalculatedLifecycleTypeDef",
    {
        "MoveToColdStorageAt": datetime,
        "DeleteAt": datetime,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ConditionType": Literal["STRINGEQUALS"],
        "ConditionKey": str,
        "ConditionValue": str,
    },
)

_RequiredCopyActionTypeDef = TypedDict(
    "_RequiredCopyActionTypeDef",
    {
        "DestinationBackupVaultArn": str,
    },
)
_OptionalCopyActionTypeDef = TypedDict(
    "_OptionalCopyActionTypeDef",
    {
        "Lifecycle": "LifecycleTypeDef",
    },
    total=False,
)


class CopyActionTypeDef(_RequiredCopyActionTypeDef, _OptionalCopyActionTypeDef):
    pass


CopyJobTypeDef = TypedDict(
    "CopyJobTypeDef",
    {
        "AccountId": str,
        "CopyJobId": str,
        "SourceBackupVaultArn": str,
        "SourceRecoveryPointArn": str,
        "DestinationBackupVaultArn": str,
        "DestinationRecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": CopyJobStateType,
        "StatusMessage": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
    },
    total=False,
)

_RequiredCreateBackupPlanInputTypeDef = TypedDict(
    "_RequiredCreateBackupPlanInputTypeDef",
    {
        "BackupPlan": "BackupPlanInputTypeDef",
    },
)
_OptionalCreateBackupPlanInputTypeDef = TypedDict(
    "_OptionalCreateBackupPlanInputTypeDef",
    {
        "BackupPlanTags": Dict[str, str],
        "CreatorRequestId": str,
    },
    total=False,
)


class CreateBackupPlanInputTypeDef(
    _RequiredCreateBackupPlanInputTypeDef, _OptionalCreateBackupPlanInputTypeDef
):
    pass


CreateBackupPlanOutputResponseTypeDef = TypedDict(
    "CreateBackupPlanOutputResponseTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackupSelectionInputTypeDef = TypedDict(
    "_RequiredCreateBackupSelectionInputTypeDef",
    {
        "BackupPlanId": str,
        "BackupSelection": "BackupSelectionTypeDef",
    },
)
_OptionalCreateBackupSelectionInputTypeDef = TypedDict(
    "_OptionalCreateBackupSelectionInputTypeDef",
    {
        "CreatorRequestId": str,
    },
    total=False,
)


class CreateBackupSelectionInputTypeDef(
    _RequiredCreateBackupSelectionInputTypeDef, _OptionalCreateBackupSelectionInputTypeDef
):
    pass


CreateBackupSelectionOutputResponseTypeDef = TypedDict(
    "CreateBackupSelectionOutputResponseTypeDef",
    {
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackupVaultInputTypeDef = TypedDict(
    "_RequiredCreateBackupVaultInputTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalCreateBackupVaultInputTypeDef = TypedDict(
    "_OptionalCreateBackupVaultInputTypeDef",
    {
        "BackupVaultTags": Dict[str, str],
        "EncryptionKeyArn": str,
        "CreatorRequestId": str,
    },
    total=False,
)


class CreateBackupVaultInputTypeDef(
    _RequiredCreateBackupVaultInputTypeDef, _OptionalCreateBackupVaultInputTypeDef
):
    pass


CreateBackupVaultOutputResponseTypeDef = TypedDict(
    "CreateBackupVaultOutputResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupPlanInputTypeDef = TypedDict(
    "DeleteBackupPlanInputTypeDef",
    {
        "BackupPlanId": str,
    },
)

DeleteBackupPlanOutputResponseTypeDef = TypedDict(
    "DeleteBackupPlanOutputResponseTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "DeletionDate": datetime,
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupSelectionInputTypeDef = TypedDict(
    "DeleteBackupSelectionInputTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

DeleteBackupVaultAccessPolicyInputTypeDef = TypedDict(
    "DeleteBackupVaultAccessPolicyInputTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultInputTypeDef = TypedDict(
    "DeleteBackupVaultInputTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteBackupVaultNotificationsInputTypeDef = TypedDict(
    "DeleteBackupVaultNotificationsInputTypeDef",
    {
        "BackupVaultName": str,
    },
)

DeleteRecoveryPointInputTypeDef = TypedDict(
    "DeleteRecoveryPointInputTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DescribeBackupJobInputTypeDef = TypedDict(
    "DescribeBackupJobInputTypeDef",
    {
        "BackupJobId": str,
    },
)

DescribeBackupJobOutputResponseTypeDef = TypedDict(
    "DescribeBackupJobOutputResponseTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupVaultInputTypeDef = TypedDict(
    "DescribeBackupVaultInputTypeDef",
    {
        "BackupVaultName": str,
    },
)

DescribeBackupVaultOutputResponseTypeDef = TypedDict(
    "DescribeBackupVaultOutputResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCopyJobInputTypeDef = TypedDict(
    "DescribeCopyJobInputTypeDef",
    {
        "CopyJobId": str,
    },
)

DescribeCopyJobOutputResponseTypeDef = TypedDict(
    "DescribeCopyJobOutputResponseTypeDef",
    {
        "CopyJob": "CopyJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalSettingsOutputResponseTypeDef = TypedDict(
    "DescribeGlobalSettingsOutputResponseTypeDef",
    {
        "GlobalSettings": Dict[str, str],
        "LastUpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectedResourceInputTypeDef = TypedDict(
    "DescribeProtectedResourceInputTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeProtectedResourceOutputResponseTypeDef = TypedDict(
    "DescribeProtectedResourceOutputResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecoveryPointInputTypeDef = TypedDict(
    "DescribeRecoveryPointInputTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

DescribeRecoveryPointOutputResponseTypeDef = TypedDict(
    "DescribeRecoveryPointOutputResponseTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": StorageClassType,
        "LastRestoreTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionSettingsOutputResponseTypeDef = TypedDict(
    "DescribeRegionSettingsOutputResponseTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRestoreJobInputTypeDef = TypedDict(
    "DescribeRestoreJobInputTypeDef",
    {
        "RestoreJobId": str,
    },
)

DescribeRestoreJobOutputResponseTypeDef = TypedDict(
    "DescribeRestoreJobOutputResponseTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRecoveryPointInputTypeDef = TypedDict(
    "DisassociateRecoveryPointInputTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

ExportBackupPlanTemplateInputTypeDef = TypedDict(
    "ExportBackupPlanTemplateInputTypeDef",
    {
        "BackupPlanId": str,
    },
)

ExportBackupPlanTemplateOutputResponseTypeDef = TypedDict(
    "ExportBackupPlanTemplateOutputResponseTypeDef",
    {
        "BackupPlanTemplateJson": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupPlanFromJSONInputTypeDef = TypedDict(
    "GetBackupPlanFromJSONInputTypeDef",
    {
        "BackupPlanTemplateJson": str,
    },
)

GetBackupPlanFromJSONOutputResponseTypeDef = TypedDict(
    "GetBackupPlanFromJSONOutputResponseTypeDef",
    {
        "BackupPlan": "BackupPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupPlanFromTemplateInputTypeDef = TypedDict(
    "GetBackupPlanFromTemplateInputTypeDef",
    {
        "BackupPlanTemplateId": str,
    },
)

GetBackupPlanFromTemplateOutputResponseTypeDef = TypedDict(
    "GetBackupPlanFromTemplateOutputResponseTypeDef",
    {
        "BackupPlanDocument": "BackupPlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBackupPlanInputTypeDef = TypedDict(
    "_RequiredGetBackupPlanInputTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalGetBackupPlanInputTypeDef = TypedDict(
    "_OptionalGetBackupPlanInputTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)


class GetBackupPlanInputTypeDef(
    _RequiredGetBackupPlanInputTypeDef, _OptionalGetBackupPlanInputTypeDef
):
    pass


GetBackupPlanOutputResponseTypeDef = TypedDict(
    "GetBackupPlanOutputResponseTypeDef",
    {
        "BackupPlan": "BackupPlanTypeDef",
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupSelectionInputTypeDef = TypedDict(
    "GetBackupSelectionInputTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)

GetBackupSelectionOutputResponseTypeDef = TypedDict(
    "GetBackupSelectionOutputResponseTypeDef",
    {
        "BackupSelection": "BackupSelectionTypeDef",
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupVaultAccessPolicyInputTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyInputTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultAccessPolicyOutputResponseTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyOutputResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackupVaultNotificationsInputTypeDef = TypedDict(
    "GetBackupVaultNotificationsInputTypeDef",
    {
        "BackupVaultName": str,
    },
)

GetBackupVaultNotificationsOutputResponseTypeDef = TypedDict(
    "GetBackupVaultNotificationsOutputResponseTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecoveryPointRestoreMetadataInputTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataInputTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)

GetRecoveryPointRestoreMetadataOutputResponseTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataOutputResponseTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "RestoreMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSupportedResourceTypesOutputResponseTypeDef = TypedDict(
    "GetSupportedResourceTypesOutputResponseTypeDef",
    {
        "ResourceTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecycleTypeDef = TypedDict(
    "LifecycleTypeDef",
    {
        "MoveToColdStorageAfterDays": int,
        "DeleteAfterDays": int,
    },
    total=False,
)

ListBackupJobsInputTypeDef = TypedDict(
    "ListBackupJobsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByState": BackupJobStateType,
        "ByBackupVaultName": str,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByResourceType": str,
        "ByAccountId": str,
    },
    total=False,
)

ListBackupJobsOutputResponseTypeDef = TypedDict(
    "ListBackupJobsOutputResponseTypeDef",
    {
        "BackupJobs": List["BackupJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlanTemplatesInputTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBackupPlanTemplatesOutputResponseTypeDef = TypedDict(
    "ListBackupPlanTemplatesOutputResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanTemplatesList": List["BackupPlanTemplatesListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackupPlanVersionsInputTypeDef = TypedDict(
    "_RequiredListBackupPlanVersionsInputTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupPlanVersionsInputTypeDef = TypedDict(
    "_OptionalListBackupPlanVersionsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListBackupPlanVersionsInputTypeDef(
    _RequiredListBackupPlanVersionsInputTypeDef, _OptionalListBackupPlanVersionsInputTypeDef
):
    pass


ListBackupPlanVersionsOutputResponseTypeDef = TypedDict(
    "ListBackupPlanVersionsOutputResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlanVersionsList": List["BackupPlansListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupPlansInputTypeDef = TypedDict(
    "ListBackupPlansInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncludeDeleted": bool,
    },
    total=False,
)

ListBackupPlansOutputResponseTypeDef = TypedDict(
    "ListBackupPlansOutputResponseTypeDef",
    {
        "NextToken": str,
        "BackupPlansList": List["BackupPlansListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackupSelectionsInputTypeDef = TypedDict(
    "_RequiredListBackupSelectionsInputTypeDef",
    {
        "BackupPlanId": str,
    },
)
_OptionalListBackupSelectionsInputTypeDef = TypedDict(
    "_OptionalListBackupSelectionsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListBackupSelectionsInputTypeDef(
    _RequiredListBackupSelectionsInputTypeDef, _OptionalListBackupSelectionsInputTypeDef
):
    pass


ListBackupSelectionsOutputResponseTypeDef = TypedDict(
    "ListBackupSelectionsOutputResponseTypeDef",
    {
        "NextToken": str,
        "BackupSelectionsList": List["BackupSelectionsListMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBackupVaultsInputTypeDef = TypedDict(
    "ListBackupVaultsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBackupVaultsOutputResponseTypeDef = TypedDict(
    "ListBackupVaultsOutputResponseTypeDef",
    {
        "BackupVaultList": List["BackupVaultListMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCopyJobsInputTypeDef = TypedDict(
    "ListCopyJobsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByState": CopyJobStateType,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByResourceType": str,
        "ByDestinationVaultArn": str,
        "ByAccountId": str,
    },
    total=False,
)

ListCopyJobsOutputResponseTypeDef = TypedDict(
    "ListCopyJobsOutputResponseTypeDef",
    {
        "CopyJobs": List["CopyJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectedResourcesInputTypeDef = TypedDict(
    "ListProtectedResourcesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectedResourcesOutputResponseTypeDef = TypedDict(
    "ListProtectedResourcesOutputResponseTypeDef",
    {
        "Results": List["ProtectedResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecoveryPointsByBackupVaultInputTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByBackupVaultInputTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalListRecoveryPointsByBackupVaultInputTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByBackupVaultInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByResourceArn": str,
        "ByResourceType": str,
        "ByBackupPlanId": str,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
    },
    total=False,
)


class ListRecoveryPointsByBackupVaultInputTypeDef(
    _RequiredListRecoveryPointsByBackupVaultInputTypeDef,
    _OptionalListRecoveryPointsByBackupVaultInputTypeDef,
):
    pass


ListRecoveryPointsByBackupVaultOutputResponseTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultOutputResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List["RecoveryPointByBackupVaultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecoveryPointsByResourceInputTypeDef = TypedDict(
    "_RequiredListRecoveryPointsByResourceInputTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListRecoveryPointsByResourceInputTypeDef = TypedDict(
    "_OptionalListRecoveryPointsByResourceInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRecoveryPointsByResourceInputTypeDef(
    _RequiredListRecoveryPointsByResourceInputTypeDef,
    _OptionalListRecoveryPointsByResourceInputTypeDef,
):
    pass


ListRecoveryPointsByResourceOutputResponseTypeDef = TypedDict(
    "ListRecoveryPointsByResourceOutputResponseTypeDef",
    {
        "NextToken": str,
        "RecoveryPoints": List["RecoveryPointByResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRestoreJobsInputTypeDef = TypedDict(
    "ListRestoreJobsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ByAccountId": str,
        "ByCreatedBefore": Union[datetime, str],
        "ByCreatedAfter": Union[datetime, str],
        "ByStatus": RestoreJobStatusType,
    },
    total=False,
)

ListRestoreJobsOutputResponseTypeDef = TypedDict(
    "ListRestoreJobsOutputResponseTypeDef",
    {
        "RestoreJobs": List["RestoreJobsListMemberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsInputTypeDef = TypedDict(
    "_RequiredListTagsInputTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputTypeDef = TypedDict(
    "_OptionalListTagsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsInputTypeDef(_RequiredListTagsInputTypeDef, _OptionalListTagsInputTypeDef):
    pass


ListTagsOutputResponseTypeDef = TypedDict(
    "ListTagsOutputResponseTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProtectedResourceTypeDef = TypedDict(
    "ProtectedResourceTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
    },
    total=False,
)

_RequiredPutBackupVaultAccessPolicyInputTypeDef = TypedDict(
    "_RequiredPutBackupVaultAccessPolicyInputTypeDef",
    {
        "BackupVaultName": str,
    },
)
_OptionalPutBackupVaultAccessPolicyInputTypeDef = TypedDict(
    "_OptionalPutBackupVaultAccessPolicyInputTypeDef",
    {
        "Policy": str,
    },
    total=False,
)


class PutBackupVaultAccessPolicyInputTypeDef(
    _RequiredPutBackupVaultAccessPolicyInputTypeDef, _OptionalPutBackupVaultAccessPolicyInputTypeDef
):
    pass


PutBackupVaultNotificationsInputTypeDef = TypedDict(
    "PutBackupVaultNotificationsInputTypeDef",
    {
        "BackupVaultName": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
    },
)

RecoveryPointByBackupVaultTypeDef = TypedDict(
    "RecoveryPointByBackupVaultTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": "RecoveryPointCreatorTypeDef",
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "Lifecycle": "LifecycleTypeDef",
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "LastRestoreTime": datetime,
    },
    total=False,
)

RecoveryPointByResourceTypeDef = TypedDict(
    "RecoveryPointByResourceTypeDef",
    {
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "Status": RecoveryPointStatusType,
        "EncryptionKeyArn": str,
        "BackupSizeBytes": int,
        "BackupVaultName": str,
    },
    total=False,
)

RecoveryPointCreatorTypeDef = TypedDict(
    "RecoveryPointCreatorTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "BackupPlanVersion": str,
        "BackupRuleId": str,
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

RestoreJobsListMemberTypeDef = TypedDict(
    "RestoreJobsListMemberTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
    },
    total=False,
)

_RequiredStartBackupJobInputTypeDef = TypedDict(
    "_RequiredStartBackupJobInputTypeDef",
    {
        "BackupVaultName": str,
        "ResourceArn": str,
        "IamRoleArn": str,
    },
)
_OptionalStartBackupJobInputTypeDef = TypedDict(
    "_OptionalStartBackupJobInputTypeDef",
    {
        "IdempotencyToken": str,
        "StartWindowMinutes": int,
        "CompleteWindowMinutes": int,
        "Lifecycle": "LifecycleTypeDef",
        "RecoveryPointTags": Dict[str, str],
        "BackupOptions": Dict[str, str],
    },
    total=False,
)


class StartBackupJobInputTypeDef(
    _RequiredStartBackupJobInputTypeDef, _OptionalStartBackupJobInputTypeDef
):
    pass


StartBackupJobOutputResponseTypeDef = TypedDict(
    "StartBackupJobOutputResponseTypeDef",
    {
        "BackupJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartCopyJobInputTypeDef = TypedDict(
    "_RequiredStartCopyJobInputTypeDef",
    {
        "RecoveryPointArn": str,
        "SourceBackupVaultName": str,
        "DestinationBackupVaultArn": str,
        "IamRoleArn": str,
    },
)
_OptionalStartCopyJobInputTypeDef = TypedDict(
    "_OptionalStartCopyJobInputTypeDef",
    {
        "IdempotencyToken": str,
        "Lifecycle": "LifecycleTypeDef",
    },
    total=False,
)


class StartCopyJobInputTypeDef(
    _RequiredStartCopyJobInputTypeDef, _OptionalStartCopyJobInputTypeDef
):
    pass


StartCopyJobOutputResponseTypeDef = TypedDict(
    "StartCopyJobOutputResponseTypeDef",
    {
        "CopyJobId": str,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartRestoreJobInputTypeDef = TypedDict(
    "_RequiredStartRestoreJobInputTypeDef",
    {
        "RecoveryPointArn": str,
        "Metadata": Dict[str, str],
        "IamRoleArn": str,
    },
)
_OptionalStartRestoreJobInputTypeDef = TypedDict(
    "_OptionalStartRestoreJobInputTypeDef",
    {
        "IdempotencyToken": str,
        "ResourceType": str,
    },
    total=False,
)


class StartRestoreJobInputTypeDef(
    _RequiredStartRestoreJobInputTypeDef, _OptionalStartRestoreJobInputTypeDef
):
    pass


StartRestoreJobOutputResponseTypeDef = TypedDict(
    "StartRestoreJobOutputResponseTypeDef",
    {
        "RestoreJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBackupJobInputTypeDef = TypedDict(
    "StopBackupJobInputTypeDef",
    {
        "BackupJobId": str,
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": List[str],
    },
)

UpdateBackupPlanInputTypeDef = TypedDict(
    "UpdateBackupPlanInputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlan": "BackupPlanInputTypeDef",
    },
)

UpdateBackupPlanOutputResponseTypeDef = TypedDict(
    "UpdateBackupPlanOutputResponseTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List["AdvancedBackupSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSettingsInputTypeDef = TypedDict(
    "UpdateGlobalSettingsInputTypeDef",
    {
        "GlobalSettings": Dict[str, str],
    },
    total=False,
)

_RequiredUpdateRecoveryPointLifecycleInputTypeDef = TypedDict(
    "_RequiredUpdateRecoveryPointLifecycleInputTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
_OptionalUpdateRecoveryPointLifecycleInputTypeDef = TypedDict(
    "_OptionalUpdateRecoveryPointLifecycleInputTypeDef",
    {
        "Lifecycle": "LifecycleTypeDef",
    },
    total=False,
)


class UpdateRecoveryPointLifecycleInputTypeDef(
    _RequiredUpdateRecoveryPointLifecycleInputTypeDef,
    _OptionalUpdateRecoveryPointLifecycleInputTypeDef,
):
    pass


UpdateRecoveryPointLifecycleOutputResponseTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleOutputResponseTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": "LifecycleTypeDef",
        "CalculatedLifecycle": "CalculatedLifecycleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegionSettingsInputTypeDef = TypedDict(
    "UpdateRegionSettingsInputTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
    },
    total=False,
)
