"""
Type annotations for auditmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef

    data: AWSAccountTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    AccountStatusType,
    ActionEnumType,
    AssessmentReportStatusType,
    AssessmentStatusType,
    ControlResponseType,
    ControlSetStatusType,
    ControlStatusType,
    ControlTypeType,
    DelegationStatusType,
    FrameworkTypeType,
    ObjectTypeEnumType,
    RoleTypeType,
    SourceFrequencyType,
    SourceSetUpOptionType,
    SourceTypeType,
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
    "AWSAccountTypeDef",
    "AWSServiceTypeDef",
    "AssessmentControlSetTypeDef",
    "AssessmentControlTypeDef",
    "AssessmentEvidenceFolderTypeDef",
    "AssessmentFrameworkMetadataTypeDef",
    "AssessmentFrameworkTypeDef",
    "AssessmentMetadataItemTypeDef",
    "AssessmentMetadataTypeDef",
    "AssessmentReportEvidenceErrorTypeDef",
    "AssessmentReportMetadataTypeDef",
    "AssessmentReportTypeDef",
    "AssessmentReportsDestinationTypeDef",
    "AssessmentTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    "ChangeLogTypeDef",
    "ControlCommentTypeDef",
    "ControlMappingSourceTypeDef",
    "ControlMetadataTypeDef",
    "ControlSetTypeDef",
    "ControlTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentFrameworkResponseTypeDef",
    "CreateAssessmentReportResponseTypeDef",
    "CreateAssessmentResponseTypeDef",
    "CreateControlMappingSourceTypeDef",
    "CreateControlResponseTypeDef",
    "CreateDelegationRequestTypeDef",
    "DelegationMetadataTypeDef",
    "DelegationTypeDef",
    "DeregisterAccountResponseTypeDef",
    "EvidenceTypeDef",
    "FrameworkMetadataTypeDef",
    "FrameworkTypeDef",
    "GetAccountStatusResponseTypeDef",
    "GetAssessmentFrameworkResponseTypeDef",
    "GetAssessmentReportUrlResponseTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetChangeLogsResponseTypeDef",
    "GetControlResponseTypeDef",
    "GetDelegationsResponseTypeDef",
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    "GetEvidenceFolderResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    "GetEvidenceResponseTypeDef",
    "GetOrganizationAdminAccountResponseTypeDef",
    "GetServicesInScopeResponseTypeDef",
    "GetSettingsResponseTypeDef",
    "ListAssessmentFrameworksResponseTypeDef",
    "ListAssessmentReportsResponseTypeDef",
    "ListAssessmentsResponseTypeDef",
    "ListControlsResponseTypeDef",
    "ListKeywordsForDataSourceResponseTypeDef",
    "ListNotificationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManualEvidenceTypeDef",
    "NotificationTypeDef",
    "RegisterAccountResponseTypeDef",
    "RegisterOrganizationAdminAccountResponseTypeDef",
    "ResourceTypeDef",
    "RoleTypeDef",
    "ScopeTypeDef",
    "ServiceMetadataTypeDef",
    "SettingsTypeDef",
    "SourceKeywordTypeDef",
    "URLTypeDef",
    "UpdateAssessmentControlResponseTypeDef",
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkResponseTypeDef",
    "UpdateAssessmentResponseTypeDef",
    "UpdateAssessmentStatusResponseTypeDef",
    "UpdateControlResponseTypeDef",
    "UpdateSettingsResponseTypeDef",
    "ValidateAssessmentReportIntegrityResponseTypeDef",
)

AWSAccountTypeDef = TypedDict(
    "AWSAccountTypeDef",
    {
        "id": str,
        "emailAddress": str,
        "name": str,
    },
    total=False,
)

AWSServiceTypeDef = TypedDict(
    "AWSServiceTypeDef",
    {
        "serviceName": str,
    },
    total=False,
)

AssessmentControlSetTypeDef = TypedDict(
    "AssessmentControlSetTypeDef",
    {
        "id": str,
        "description": str,
        "status": ControlSetStatusType,
        "roles": List["RoleTypeDef"],
        "controls": List["AssessmentControlTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "systemEvidenceCount": int,
        "manualEvidenceCount": int,
    },
    total=False,
)

AssessmentControlTypeDef = TypedDict(
    "AssessmentControlTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "status": ControlStatusType,
        "response": ControlResponseType,
        "comments": List["ControlCommentTypeDef"],
        "evidenceSources": List[str],
        "evidenceCount": int,
        "assessmentReportEvidenceCount": int,
    },
    total=False,
)

AssessmentEvidenceFolderTypeDef = TypedDict(
    "AssessmentEvidenceFolderTypeDef",
    {
        "name": str,
        "date": datetime,
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "id": str,
        "dataSource": str,
        "author": str,
        "totalEvidence": int,
        "assessmentReportSelectionCount": int,
        "controlName": str,
        "evidenceResourcesIncludedCount": int,
        "evidenceByTypeConfigurationDataCount": int,
        "evidenceByTypeManualCount": int,
        "evidenceByTypeComplianceCheckCount": int,
        "evidenceByTypeComplianceCheckIssuesCount": int,
        "evidenceByTypeUserActivityCount": int,
        "evidenceAwsServiceSourceCount": int,
    },
    total=False,
)

AssessmentFrameworkMetadataTypeDef = TypedDict(
    "AssessmentFrameworkMetadataTypeDef",
    {
        "arn": str,
        "id": str,
        "type": FrameworkTypeType,
        "name": str,
        "description": str,
        "logo": str,
        "complianceType": str,
        "controlsCount": int,
        "controlSetsCount": int,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

AssessmentFrameworkTypeDef = TypedDict(
    "AssessmentFrameworkTypeDef",
    {
        "id": str,
        "arn": str,
        "metadata": "FrameworkMetadataTypeDef",
        "controlSets": List["AssessmentControlSetTypeDef"],
    },
    total=False,
)

AssessmentMetadataItemTypeDef = TypedDict(
    "AssessmentMetadataItemTypeDef",
    {
        "name": str,
        "id": str,
        "complianceType": str,
        "status": AssessmentStatusType,
        "roles": List["RoleTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "creationTime": datetime,
        "lastUpdated": datetime,
    },
    total=False,
)

AssessmentMetadataTypeDef = TypedDict(
    "AssessmentMetadataTypeDef",
    {
        "name": str,
        "id": str,
        "description": str,
        "complianceType": str,
        "status": AssessmentStatusType,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "scope": "ScopeTypeDef",
        "roles": List["RoleTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "creationTime": datetime,
        "lastUpdated": datetime,
    },
    total=False,
)

AssessmentReportEvidenceErrorTypeDef = TypedDict(
    "AssessmentReportEvidenceErrorTypeDef",
    {
        "evidenceId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

AssessmentReportMetadataTypeDef = TypedDict(
    "AssessmentReportMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "assessmentId": str,
        "assessmentName": str,
        "author": str,
        "status": AssessmentReportStatusType,
        "creationTime": datetime,
    },
    total=False,
)

AssessmentReportTypeDef = TypedDict(
    "AssessmentReportTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "awsAccountId": str,
        "assessmentId": str,
        "assessmentName": str,
        "author": str,
        "status": AssessmentReportStatusType,
        "creationTime": datetime,
    },
    total=False,
)

AssessmentReportsDestinationTypeDef = TypedDict(
    "AssessmentReportsDestinationTypeDef",
    {
        "destinationType": Literal["S3"],
        "destination": str,
    },
    total=False,
)

AssessmentTypeDef = TypedDict(
    "AssessmentTypeDef",
    {
        "arn": str,
        "awsAccount": "AWSAccountTypeDef",
        "metadata": "AssessmentMetadataTypeDef",
        "framework": "AssessmentFrameworkTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

BatchAssociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
    },
    total=False,
)

BatchCreateDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    {
        "createDelegationRequest": "CreateDelegationRequestTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchCreateDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    {
        "delegations": List["DelegationTypeDef"],
        "errors": List["BatchCreateDelegationByAssessmentErrorTypeDef"],
    },
    total=False,
)

BatchDeleteDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    {
        "delegationId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchDeleteDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    {
        "errors": List["BatchDeleteDelegationByAssessmentErrorTypeDef"],
    },
    total=False,
)

BatchDisassociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
    },
    total=False,
)

BatchImportEvidenceToAssessmentControlErrorTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    {
        "manualEvidence": "ManualEvidenceTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchImportEvidenceToAssessmentControlResponseTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    {
        "errors": List["BatchImportEvidenceToAssessmentControlErrorTypeDef"],
    },
    total=False,
)

ChangeLogTypeDef = TypedDict(
    "ChangeLogTypeDef",
    {
        "objectType": ObjectTypeEnumType,
        "objectName": str,
        "action": ActionEnumType,
        "createdAt": datetime,
        "createdBy": str,
    },
    total=False,
)

ControlCommentTypeDef = TypedDict(
    "ControlCommentTypeDef",
    {
        "authorName": str,
        "commentBody": str,
        "postedDate": datetime,
    },
    total=False,
)

ControlMappingSourceTypeDef = TypedDict(
    "ControlMappingSourceTypeDef",
    {
        "sourceId": str,
        "sourceName": str,
        "sourceDescription": str,
        "sourceSetUpOption": SourceSetUpOptionType,
        "sourceType": SourceTypeType,
        "sourceKeyword": "SourceKeywordTypeDef",
        "sourceFrequency": SourceFrequencyType,
        "troubleshootingText": str,
    },
    total=False,
)

ControlMetadataTypeDef = TypedDict(
    "ControlMetadataTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "controlSources": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

ControlSetTypeDef = TypedDict(
    "ControlSetTypeDef",
    {
        "id": str,
        "name": str,
        "controls": List["ControlTypeDef"],
    },
    total=False,
)

ControlTypeDef = TypedDict(
    "ControlTypeDef",
    {
        "arn": str,
        "id": str,
        "type": ControlTypeType,
        "name": str,
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
        "controlSources": str,
        "controlMappingSources": List["ControlMappingSourceTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_RequiredCreateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_OptionalCreateAssessmentFrameworkControlSetTypeDef",
    {
        "controls": List["CreateAssessmentFrameworkControlTypeDef"],
    },
    total=False,
)


class CreateAssessmentFrameworkControlSetTypeDef(
    _RequiredCreateAssessmentFrameworkControlSetTypeDef,
    _OptionalCreateAssessmentFrameworkControlSetTypeDef,
):
    pass


CreateAssessmentFrameworkControlTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlTypeDef",
    {
        "id": str,
    },
    total=False,
)

CreateAssessmentFrameworkResponseTypeDef = TypedDict(
    "CreateAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
    },
    total=False,
)

CreateAssessmentReportResponseTypeDef = TypedDict(
    "CreateAssessmentReportResponseTypeDef",
    {
        "assessmentReport": "AssessmentReportTypeDef",
    },
    total=False,
)

CreateAssessmentResponseTypeDef = TypedDict(
    "CreateAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
    },
    total=False,
)

CreateControlMappingSourceTypeDef = TypedDict(
    "CreateControlMappingSourceTypeDef",
    {
        "sourceName": str,
        "sourceDescription": str,
        "sourceSetUpOption": SourceSetUpOptionType,
        "sourceType": SourceTypeType,
        "sourceKeyword": "SourceKeywordTypeDef",
        "sourceFrequency": SourceFrequencyType,
        "troubleshootingText": str,
    },
    total=False,
)

CreateControlResponseTypeDef = TypedDict(
    "CreateControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
    },
    total=False,
)

CreateDelegationRequestTypeDef = TypedDict(
    "CreateDelegationRequestTypeDef",
    {
        "comment": str,
        "controlSetId": str,
        "roleArn": str,
        "roleType": RoleTypeType,
    },
    total=False,
)

DelegationMetadataTypeDef = TypedDict(
    "DelegationMetadataTypeDef",
    {
        "id": str,
        "assessmentName": str,
        "assessmentId": str,
        "status": DelegationStatusType,
        "roleArn": str,
        "creationTime": datetime,
        "controlSetName": str,
    },
    total=False,
)

DelegationTypeDef = TypedDict(
    "DelegationTypeDef",
    {
        "id": str,
        "assessmentName": str,
        "assessmentId": str,
        "status": DelegationStatusType,
        "roleArn": str,
        "roleType": RoleTypeType,
        "creationTime": datetime,
        "lastUpdated": datetime,
        "controlSetId": str,
        "comment": str,
        "createdBy": str,
    },
    total=False,
)

DeregisterAccountResponseTypeDef = TypedDict(
    "DeregisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
    },
    total=False,
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "dataSource": str,
        "evidenceAwsAccountId": str,
        "time": datetime,
        "eventSource": str,
        "eventName": str,
        "evidenceByType": str,
        "resourcesIncluded": List["ResourceTypeDef"],
        "attributes": Dict[str, str],
        "iamId": str,
        "complianceCheck": str,
        "awsOrganization": str,
        "awsAccountId": str,
        "evidenceFolderId": str,
        "id": str,
        "assessmentReportSelection": str,
    },
    total=False,
)

FrameworkMetadataTypeDef = TypedDict(
    "FrameworkMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "logo": str,
        "complianceType": str,
    },
    total=False,
)

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "type": FrameworkTypeType,
        "complianceType": str,
        "description": str,
        "logo": str,
        "controlSources": str,
        "controlSets": List["ControlSetTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GetAccountStatusResponseTypeDef = TypedDict(
    "GetAccountStatusResponseTypeDef",
    {
        "status": AccountStatusType,
    },
    total=False,
)

GetAssessmentFrameworkResponseTypeDef = TypedDict(
    "GetAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
    },
    total=False,
)

GetAssessmentReportUrlResponseTypeDef = TypedDict(
    "GetAssessmentReportUrlResponseTypeDef",
    {
        "preSignedUrl": "URLTypeDef",
    },
    total=False,
)

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "userRole": "RoleTypeDef",
    },
    total=False,
)

GetChangeLogsResponseTypeDef = TypedDict(
    "GetChangeLogsResponseTypeDef",
    {
        "changeLogs": List["ChangeLogTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetControlResponseTypeDef = TypedDict(
    "GetControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
    },
    total=False,
)

GetDelegationsResponseTypeDef = TypedDict(
    "GetDelegationsResponseTypeDef",
    {
        "delegations": List["DelegationMetadataTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetEvidenceByEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    {
        "evidence": List["EvidenceTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceFolderResponseTypeDef",
    {
        "evidenceFolder": "AssessmentEvidenceFolderTypeDef",
    },
    total=False,
)

GetEvidenceFoldersByAssessmentControlResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetEvidenceFoldersByAssessmentResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetEvidenceResponseTypeDef = TypedDict(
    "GetEvidenceResponseTypeDef",
    {
        "evidence": "EvidenceTypeDef",
    },
    total=False,
)

GetOrganizationAdminAccountResponseTypeDef = TypedDict(
    "GetOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
    },
    total=False,
)

GetServicesInScopeResponseTypeDef = TypedDict(
    "GetServicesInScopeResponseTypeDef",
    {
        "serviceMetadata": List["ServiceMetadataTypeDef"],
    },
    total=False,
)

GetSettingsResponseTypeDef = TypedDict(
    "GetSettingsResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
    },
    total=False,
)

ListAssessmentFrameworksResponseTypeDef = TypedDict(
    "ListAssessmentFrameworksResponseTypeDef",
    {
        "frameworkMetadataList": List["AssessmentFrameworkMetadataTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListAssessmentReportsResponseTypeDef = TypedDict(
    "ListAssessmentReportsResponseTypeDef",
    {
        "assessmentReports": List["AssessmentReportMetadataTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListAssessmentsResponseTypeDef = TypedDict(
    "ListAssessmentsResponseTypeDef",
    {
        "assessmentMetadata": List["AssessmentMetadataItemTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListControlsResponseTypeDef = TypedDict(
    "ListControlsResponseTypeDef",
    {
        "controlMetadataList": List["ControlMetadataTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListKeywordsForDataSourceResponseTypeDef = TypedDict(
    "ListKeywordsForDataSourceResponseTypeDef",
    {
        "keywords": List[str],
        "nextToken": str,
    },
    total=False,
)

ListNotificationsResponseTypeDef = TypedDict(
    "ListNotificationsResponseTypeDef",
    {
        "notifications": List["NotificationTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

ManualEvidenceTypeDef = TypedDict(
    "ManualEvidenceTypeDef",
    {
        "s3ResourcePath": str,
    },
    total=False,
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "id": str,
        "assessmentId": str,
        "assessmentName": str,
        "controlSetId": str,
        "controlSetName": str,
        "description": str,
        "eventTime": datetime,
        "source": str,
    },
    total=False,
)

RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
    },
    total=False,
)

RegisterOrganizationAdminAccountResponseTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "value": str,
    },
    total=False,
)

RoleTypeDef = TypedDict(
    "RoleTypeDef",
    {
        "roleType": RoleTypeType,
        "roleArn": str,
    },
    total=False,
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "awsAccounts": List["AWSAccountTypeDef"],
        "awsServices": List["AWSServiceTypeDef"],
    },
    total=False,
)

ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "name": str,
        "displayName": str,
        "description": str,
        "category": str,
    },
    total=False,
)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "isAwsOrgEnabled": bool,
        "snsTopic": str,
        "defaultAssessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "defaultProcessOwners": List["RoleTypeDef"],
        "kmsKey": str,
    },
    total=False,
)

SourceKeywordTypeDef = TypedDict(
    "SourceKeywordTypeDef",
    {
        "keywordInputType": Literal["SELECT_FROM_LIST"],
        "keywordValue": str,
    },
    total=False,
)

URLTypeDef = TypedDict(
    "URLTypeDef",
    {
        "hyperlinkName": str,
        "link": str,
    },
    total=False,
)

UpdateAssessmentControlResponseTypeDef = TypedDict(
    "UpdateAssessmentControlResponseTypeDef",
    {
        "control": "AssessmentControlTypeDef",
    },
    total=False,
)

UpdateAssessmentControlSetStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    {
        "controlSet": "AssessmentControlSetTypeDef",
    },
    total=False,
)

_RequiredUpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_RequiredUpdateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_OptionalUpdateAssessmentFrameworkControlSetTypeDef",
    {
        "id": str,
        "controls": List["CreateAssessmentFrameworkControlTypeDef"],
    },
    total=False,
)


class UpdateAssessmentFrameworkControlSetTypeDef(
    _RequiredUpdateAssessmentFrameworkControlSetTypeDef,
    _OptionalUpdateAssessmentFrameworkControlSetTypeDef,
):
    pass


UpdateAssessmentFrameworkResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
    },
    total=False,
)

UpdateAssessmentResponseTypeDef = TypedDict(
    "UpdateAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
    },
    total=False,
)

UpdateAssessmentStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentStatusResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
    },
    total=False,
)

UpdateControlResponseTypeDef = TypedDict(
    "UpdateControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
    },
    total=False,
)

UpdateSettingsResponseTypeDef = TypedDict(
    "UpdateSettingsResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
    },
    total=False,
)

ValidateAssessmentReportIntegrityResponseTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityResponseTypeDef",
    {
        "signatureValid": bool,
        "signatureAlgorithm": str,
        "signatureDateTime": str,
        "signatureKeyId": str,
        "validationErrors": List[str],
    },
    total=False,
)
