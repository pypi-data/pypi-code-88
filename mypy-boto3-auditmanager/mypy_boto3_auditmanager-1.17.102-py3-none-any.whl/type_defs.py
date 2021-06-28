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
from typing import Any, Dict, List

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
    SettingAttributeType,
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
    "AssociateAssessmentReportEvidenceFolderRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentRequestTypeDef",
    "BatchCreateDelegationByAssessmentResponseResponseTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentRequestTypeDef",
    "BatchDeleteDelegationByAssessmentResponseResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceRequestTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlRequestTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseResponseTypeDef",
    "ChangeLogTypeDef",
    "ControlCommentTypeDef",
    "ControlMappingSourceTypeDef",
    "ControlMetadataTypeDef",
    "ControlSetTypeDef",
    "ControlTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentFrameworkRequestTypeDef",
    "CreateAssessmentFrameworkResponseResponseTypeDef",
    "CreateAssessmentReportRequestTypeDef",
    "CreateAssessmentReportResponseResponseTypeDef",
    "CreateAssessmentRequestTypeDef",
    "CreateAssessmentResponseResponseTypeDef",
    "CreateControlMappingSourceTypeDef",
    "CreateControlRequestTypeDef",
    "CreateControlResponseResponseTypeDef",
    "CreateDelegationRequestTypeDef",
    "DelegationMetadataTypeDef",
    "DelegationTypeDef",
    "DeleteAssessmentFrameworkRequestTypeDef",
    "DeleteAssessmentReportRequestTypeDef",
    "DeleteAssessmentRequestTypeDef",
    "DeleteControlRequestTypeDef",
    "DeregisterAccountResponseResponseTypeDef",
    "DeregisterOrganizationAdminAccountRequestTypeDef",
    "DisassociateAssessmentReportEvidenceFolderRequestTypeDef",
    "EvidenceTypeDef",
    "FrameworkMetadataTypeDef",
    "FrameworkTypeDef",
    "GetAccountStatusResponseResponseTypeDef",
    "GetAssessmentFrameworkRequestTypeDef",
    "GetAssessmentFrameworkResponseResponseTypeDef",
    "GetAssessmentReportUrlRequestTypeDef",
    "GetAssessmentReportUrlResponseResponseTypeDef",
    "GetAssessmentRequestTypeDef",
    "GetAssessmentResponseResponseTypeDef",
    "GetChangeLogsRequestTypeDef",
    "GetChangeLogsResponseResponseTypeDef",
    "GetControlRequestTypeDef",
    "GetControlResponseResponseTypeDef",
    "GetDelegationsRequestTypeDef",
    "GetDelegationsResponseResponseTypeDef",
    "GetEvidenceByEvidenceFolderRequestTypeDef",
    "GetEvidenceByEvidenceFolderResponseResponseTypeDef",
    "GetEvidenceFolderRequestTypeDef",
    "GetEvidenceFolderResponseResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlRequestTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseResponseTypeDef",
    "GetEvidenceFoldersByAssessmentRequestTypeDef",
    "GetEvidenceFoldersByAssessmentResponseResponseTypeDef",
    "GetEvidenceRequestTypeDef",
    "GetEvidenceResponseResponseTypeDef",
    "GetOrganizationAdminAccountResponseResponseTypeDef",
    "GetServicesInScopeResponseResponseTypeDef",
    "GetSettingsRequestTypeDef",
    "GetSettingsResponseResponseTypeDef",
    "ListAssessmentFrameworksRequestTypeDef",
    "ListAssessmentFrameworksResponseResponseTypeDef",
    "ListAssessmentReportsRequestTypeDef",
    "ListAssessmentReportsResponseResponseTypeDef",
    "ListAssessmentsRequestTypeDef",
    "ListAssessmentsResponseResponseTypeDef",
    "ListControlsRequestTypeDef",
    "ListControlsResponseResponseTypeDef",
    "ListKeywordsForDataSourceRequestTypeDef",
    "ListKeywordsForDataSourceResponseResponseTypeDef",
    "ListNotificationsRequestTypeDef",
    "ListNotificationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ManualEvidenceTypeDef",
    "NotificationTypeDef",
    "RegisterAccountRequestTypeDef",
    "RegisterAccountResponseResponseTypeDef",
    "RegisterOrganizationAdminAccountRequestTypeDef",
    "RegisterOrganizationAdminAccountResponseResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RoleTypeDef",
    "ScopeTypeDef",
    "ServiceMetadataTypeDef",
    "SettingsTypeDef",
    "SourceKeywordTypeDef",
    "TagResourceRequestTypeDef",
    "URLTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAssessmentControlRequestTypeDef",
    "UpdateAssessmentControlResponseResponseTypeDef",
    "UpdateAssessmentControlSetStatusRequestTypeDef",
    "UpdateAssessmentControlSetStatusResponseResponseTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkRequestTypeDef",
    "UpdateAssessmentFrameworkResponseResponseTypeDef",
    "UpdateAssessmentRequestTypeDef",
    "UpdateAssessmentResponseResponseTypeDef",
    "UpdateAssessmentStatusRequestTypeDef",
    "UpdateAssessmentStatusResponseResponseTypeDef",
    "UpdateControlRequestTypeDef",
    "UpdateControlResponseResponseTypeDef",
    "UpdateSettingsRequestTypeDef",
    "UpdateSettingsResponseResponseTypeDef",
    "ValidateAssessmentReportIntegrityRequestTypeDef",
    "ValidateAssessmentReportIntegrityResponseResponseTypeDef",
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

AssociateAssessmentReportEvidenceFolderRequestTypeDef = TypedDict(
    "AssociateAssessmentReportEvidenceFolderRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)

BatchAssociateAssessmentReportEvidenceRequestTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": List[str],
    },
)

BatchAssociateAssessmentReportEvidenceResponseResponseTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceResponseResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

BatchCreateDelegationByAssessmentRequestTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentRequestTypeDef",
    {
        "createDelegationRequests": List["CreateDelegationRequestTypeDef"],
        "assessmentId": str,
    },
)

BatchCreateDelegationByAssessmentResponseResponseTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentResponseResponseTypeDef",
    {
        "delegations": List["DelegationTypeDef"],
        "errors": List["BatchCreateDelegationByAssessmentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

BatchDeleteDelegationByAssessmentRequestTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentRequestTypeDef",
    {
        "delegationIds": List[str],
        "assessmentId": str,
    },
)

BatchDeleteDelegationByAssessmentResponseResponseTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentResponseResponseTypeDef",
    {
        "errors": List["BatchDeleteDelegationByAssessmentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateAssessmentReportEvidenceRequestTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": List[str],
    },
)

BatchDisassociateAssessmentReportEvidenceResponseResponseTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceResponseResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

BatchImportEvidenceToAssessmentControlRequestTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "manualEvidence": List["ManualEvidenceTypeDef"],
    },
)

BatchImportEvidenceToAssessmentControlResponseResponseTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlResponseResponseTypeDef",
    {
        "errors": List["BatchImportEvidenceToAssessmentControlErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateAssessmentFrameworkRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentFrameworkRequestTypeDef",
    {
        "name": str,
        "controlSets": List["CreateAssessmentFrameworkControlSetTypeDef"],
    },
)
_OptionalCreateAssessmentFrameworkRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentFrameworkRequestTypeDef",
    {
        "description": str,
        "complianceType": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAssessmentFrameworkRequestTypeDef(
    _RequiredCreateAssessmentFrameworkRequestTypeDef,
    _OptionalCreateAssessmentFrameworkRequestTypeDef,
):
    pass


CreateAssessmentFrameworkResponseResponseTypeDef = TypedDict(
    "CreateAssessmentFrameworkResponseResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssessmentReportRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentReportRequestTypeDef",
    {
        "name": str,
        "assessmentId": str,
    },
)
_OptionalCreateAssessmentReportRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentReportRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class CreateAssessmentReportRequestTypeDef(
    _RequiredCreateAssessmentReportRequestTypeDef, _OptionalCreateAssessmentReportRequestTypeDef
):
    pass


CreateAssessmentReportResponseResponseTypeDef = TypedDict(
    "CreateAssessmentReportResponseResponseTypeDef",
    {
        "assessmentReport": "AssessmentReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssessmentRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentRequestTypeDef",
    {
        "name": str,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "scope": "ScopeTypeDef",
        "roles": List["RoleTypeDef"],
        "frameworkId": str,
    },
)
_OptionalCreateAssessmentRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAssessmentRequestTypeDef(
    _RequiredCreateAssessmentRequestTypeDef, _OptionalCreateAssessmentRequestTypeDef
):
    pass


CreateAssessmentResponseResponseTypeDef = TypedDict(
    "CreateAssessmentResponseResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateControlRequestTypeDef = TypedDict(
    "_RequiredCreateControlRequestTypeDef",
    {
        "name": str,
        "controlMappingSources": List["CreateControlMappingSourceTypeDef"],
    },
)
_OptionalCreateControlRequestTypeDef = TypedDict(
    "_OptionalCreateControlRequestTypeDef",
    {
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateControlRequestTypeDef(
    _RequiredCreateControlRequestTypeDef, _OptionalCreateControlRequestTypeDef
):
    pass


CreateControlResponseResponseTypeDef = TypedDict(
    "CreateControlResponseResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteAssessmentFrameworkRequestTypeDef = TypedDict(
    "DeleteAssessmentFrameworkRequestTypeDef",
    {
        "frameworkId": str,
    },
)

DeleteAssessmentReportRequestTypeDef = TypedDict(
    "DeleteAssessmentReportRequestTypeDef",
    {
        "assessmentId": str,
        "assessmentReportId": str,
    },
)

DeleteAssessmentRequestTypeDef = TypedDict(
    "DeleteAssessmentRequestTypeDef",
    {
        "assessmentId": str,
    },
)

DeleteControlRequestTypeDef = TypedDict(
    "DeleteControlRequestTypeDef",
    {
        "controlId": str,
    },
)

DeregisterAccountResponseResponseTypeDef = TypedDict(
    "DeregisterAccountResponseResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterOrganizationAdminAccountRequestTypeDef = TypedDict(
    "DeregisterOrganizationAdminAccountRequestTypeDef",
    {
        "adminAccountId": str,
    },
    total=False,
)

DisassociateAssessmentReportEvidenceFolderRequestTypeDef = TypedDict(
    "DisassociateAssessmentReportEvidenceFolderRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
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

GetAccountStatusResponseResponseTypeDef = TypedDict(
    "GetAccountStatusResponseResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentFrameworkRequestTypeDef = TypedDict(
    "GetAssessmentFrameworkRequestTypeDef",
    {
        "frameworkId": str,
    },
)

GetAssessmentFrameworkResponseResponseTypeDef = TypedDict(
    "GetAssessmentFrameworkResponseResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentReportUrlRequestTypeDef = TypedDict(
    "GetAssessmentReportUrlRequestTypeDef",
    {
        "assessmentReportId": str,
        "assessmentId": str,
    },
)

GetAssessmentReportUrlResponseResponseTypeDef = TypedDict(
    "GetAssessmentReportUrlResponseResponseTypeDef",
    {
        "preSignedUrl": "URLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentRequestTypeDef = TypedDict(
    "GetAssessmentRequestTypeDef",
    {
        "assessmentId": str,
    },
)

GetAssessmentResponseResponseTypeDef = TypedDict(
    "GetAssessmentResponseResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "userRole": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetChangeLogsRequestTypeDef = TypedDict(
    "_RequiredGetChangeLogsRequestTypeDef",
    {
        "assessmentId": str,
    },
)
_OptionalGetChangeLogsRequestTypeDef = TypedDict(
    "_OptionalGetChangeLogsRequestTypeDef",
    {
        "controlSetId": str,
        "controlId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetChangeLogsRequestTypeDef(
    _RequiredGetChangeLogsRequestTypeDef, _OptionalGetChangeLogsRequestTypeDef
):
    pass


GetChangeLogsResponseResponseTypeDef = TypedDict(
    "GetChangeLogsResponseResponseTypeDef",
    {
        "changeLogs": List["ChangeLogTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetControlRequestTypeDef = TypedDict(
    "GetControlRequestTypeDef",
    {
        "controlId": str,
    },
)

GetControlResponseResponseTypeDef = TypedDict(
    "GetControlResponseResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDelegationsRequestTypeDef = TypedDict(
    "GetDelegationsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetDelegationsResponseResponseTypeDef = TypedDict(
    "GetDelegationsResponseResponseTypeDef",
    {
        "delegations": List["DelegationMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEvidenceByEvidenceFolderRequestTypeDef = TypedDict(
    "_RequiredGetEvidenceByEvidenceFolderRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
    },
)
_OptionalGetEvidenceByEvidenceFolderRequestTypeDef = TypedDict(
    "_OptionalGetEvidenceByEvidenceFolderRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetEvidenceByEvidenceFolderRequestTypeDef(
    _RequiredGetEvidenceByEvidenceFolderRequestTypeDef,
    _OptionalGetEvidenceByEvidenceFolderRequestTypeDef,
):
    pass


GetEvidenceByEvidenceFolderResponseResponseTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderResponseResponseTypeDef",
    {
        "evidence": List["EvidenceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceFolderRequestTypeDef = TypedDict(
    "GetEvidenceFolderRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
    },
)

GetEvidenceFolderResponseResponseTypeDef = TypedDict(
    "GetEvidenceFolderResponseResponseTypeDef",
    {
        "evidenceFolder": "AssessmentEvidenceFolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEvidenceFoldersByAssessmentControlRequestTypeDef = TypedDict(
    "_RequiredGetEvidenceFoldersByAssessmentControlRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
    },
)
_OptionalGetEvidenceFoldersByAssessmentControlRequestTypeDef = TypedDict(
    "_OptionalGetEvidenceFoldersByAssessmentControlRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetEvidenceFoldersByAssessmentControlRequestTypeDef(
    _RequiredGetEvidenceFoldersByAssessmentControlRequestTypeDef,
    _OptionalGetEvidenceFoldersByAssessmentControlRequestTypeDef,
):
    pass


GetEvidenceFoldersByAssessmentControlResponseResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlResponseResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEvidenceFoldersByAssessmentRequestTypeDef = TypedDict(
    "_RequiredGetEvidenceFoldersByAssessmentRequestTypeDef",
    {
        "assessmentId": str,
    },
)
_OptionalGetEvidenceFoldersByAssessmentRequestTypeDef = TypedDict(
    "_OptionalGetEvidenceFoldersByAssessmentRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetEvidenceFoldersByAssessmentRequestTypeDef(
    _RequiredGetEvidenceFoldersByAssessmentRequestTypeDef,
    _OptionalGetEvidenceFoldersByAssessmentRequestTypeDef,
):
    pass


GetEvidenceFoldersByAssessmentResponseResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentResponseResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceRequestTypeDef = TypedDict(
    "GetEvidenceRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
        "evidenceId": str,
    },
)

GetEvidenceResponseResponseTypeDef = TypedDict(
    "GetEvidenceResponseResponseTypeDef",
    {
        "evidence": "EvidenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrganizationAdminAccountResponseResponseTypeDef = TypedDict(
    "GetOrganizationAdminAccountResponseResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServicesInScopeResponseResponseTypeDef = TypedDict(
    "GetServicesInScopeResponseResponseTypeDef",
    {
        "serviceMetadata": List["ServiceMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSettingsRequestTypeDef = TypedDict(
    "GetSettingsRequestTypeDef",
    {
        "attribute": SettingAttributeType,
    },
)

GetSettingsResponseResponseTypeDef = TypedDict(
    "GetSettingsResponseResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssessmentFrameworksRequestTypeDef = TypedDict(
    "_RequiredListAssessmentFrameworksRequestTypeDef",
    {
        "frameworkType": FrameworkTypeType,
    },
)
_OptionalListAssessmentFrameworksRequestTypeDef = TypedDict(
    "_OptionalListAssessmentFrameworksRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssessmentFrameworksRequestTypeDef(
    _RequiredListAssessmentFrameworksRequestTypeDef, _OptionalListAssessmentFrameworksRequestTypeDef
):
    pass


ListAssessmentFrameworksResponseResponseTypeDef = TypedDict(
    "ListAssessmentFrameworksResponseResponseTypeDef",
    {
        "frameworkMetadataList": List["AssessmentFrameworkMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentReportsRequestTypeDef = TypedDict(
    "ListAssessmentReportsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentReportsResponseResponseTypeDef = TypedDict(
    "ListAssessmentReportsResponseResponseTypeDef",
    {
        "assessmentReports": List["AssessmentReportMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentsRequestTypeDef = TypedDict(
    "ListAssessmentsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentsResponseResponseTypeDef = TypedDict(
    "ListAssessmentsResponseResponseTypeDef",
    {
        "assessmentMetadata": List["AssessmentMetadataItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListControlsRequestTypeDef = TypedDict(
    "_RequiredListControlsRequestTypeDef",
    {
        "controlType": ControlTypeType,
    },
)
_OptionalListControlsRequestTypeDef = TypedDict(
    "_OptionalListControlsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListControlsRequestTypeDef(
    _RequiredListControlsRequestTypeDef, _OptionalListControlsRequestTypeDef
):
    pass


ListControlsResponseResponseTypeDef = TypedDict(
    "ListControlsResponseResponseTypeDef",
    {
        "controlMetadataList": List["ControlMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKeywordsForDataSourceRequestTypeDef = TypedDict(
    "_RequiredListKeywordsForDataSourceRequestTypeDef",
    {
        "source": SourceTypeType,
    },
)
_OptionalListKeywordsForDataSourceRequestTypeDef = TypedDict(
    "_OptionalListKeywordsForDataSourceRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListKeywordsForDataSourceRequestTypeDef(
    _RequiredListKeywordsForDataSourceRequestTypeDef,
    _OptionalListKeywordsForDataSourceRequestTypeDef,
):
    pass


ListKeywordsForDataSourceResponseResponseTypeDef = TypedDict(
    "ListKeywordsForDataSourceResponseResponseTypeDef",
    {
        "keywords": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationsRequestTypeDef = TypedDict(
    "ListNotificationsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListNotificationsResponseResponseTypeDef = TypedDict(
    "ListNotificationsResponseResponseTypeDef",
    {
        "notifications": List["NotificationTypeDef"],
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

RegisterAccountRequestTypeDef = TypedDict(
    "RegisterAccountRequestTypeDef",
    {
        "kmsKey": str,
        "delegatedAdminAccount": str,
    },
    total=False,
)

RegisterAccountResponseResponseTypeDef = TypedDict(
    "RegisterAccountResponseResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterOrganizationAdminAccountRequestTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

RegisterOrganizationAdminAccountResponseResponseTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountResponseResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "value": str,
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

URLTypeDef = TypedDict(
    "URLTypeDef",
    {
        "hyperlinkName": str,
        "link": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAssessmentControlRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentControlRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
    },
)
_OptionalUpdateAssessmentControlRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentControlRequestTypeDef",
    {
        "controlStatus": ControlStatusType,
        "commentBody": str,
    },
    total=False,
)


class UpdateAssessmentControlRequestTypeDef(
    _RequiredUpdateAssessmentControlRequestTypeDef, _OptionalUpdateAssessmentControlRequestTypeDef
):
    pass


UpdateAssessmentControlResponseResponseTypeDef = TypedDict(
    "UpdateAssessmentControlResponseResponseTypeDef",
    {
        "control": "AssessmentControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentControlSetStatusRequestTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "status": ControlSetStatusType,
        "comment": str,
    },
)

UpdateAssessmentControlSetStatusResponseResponseTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusResponseResponseTypeDef",
    {
        "controlSet": "AssessmentControlSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


_RequiredUpdateAssessmentFrameworkRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentFrameworkRequestTypeDef",
    {
        "frameworkId": str,
        "name": str,
        "controlSets": List["UpdateAssessmentFrameworkControlSetTypeDef"],
    },
)
_OptionalUpdateAssessmentFrameworkRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentFrameworkRequestTypeDef",
    {
        "description": str,
        "complianceType": str,
    },
    total=False,
)


class UpdateAssessmentFrameworkRequestTypeDef(
    _RequiredUpdateAssessmentFrameworkRequestTypeDef,
    _OptionalUpdateAssessmentFrameworkRequestTypeDef,
):
    pass


UpdateAssessmentFrameworkResponseResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkResponseResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssessmentRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentRequestTypeDef",
    {
        "assessmentId": str,
        "scope": "ScopeTypeDef",
    },
)
_OptionalUpdateAssessmentRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentRequestTypeDef",
    {
        "assessmentName": str,
        "assessmentDescription": str,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "roles": List["RoleTypeDef"],
    },
    total=False,
)


class UpdateAssessmentRequestTypeDef(
    _RequiredUpdateAssessmentRequestTypeDef, _OptionalUpdateAssessmentRequestTypeDef
):
    pass


UpdateAssessmentResponseResponseTypeDef = TypedDict(
    "UpdateAssessmentResponseResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentStatusRequestTypeDef = TypedDict(
    "UpdateAssessmentStatusRequestTypeDef",
    {
        "assessmentId": str,
        "status": AssessmentStatusType,
    },
)

UpdateAssessmentStatusResponseResponseTypeDef = TypedDict(
    "UpdateAssessmentStatusResponseResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateControlRequestTypeDef = TypedDict(
    "_RequiredUpdateControlRequestTypeDef",
    {
        "controlId": str,
        "name": str,
        "controlMappingSources": List["ControlMappingSourceTypeDef"],
    },
)
_OptionalUpdateControlRequestTypeDef = TypedDict(
    "_OptionalUpdateControlRequestTypeDef",
    {
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
    },
    total=False,
)


class UpdateControlRequestTypeDef(
    _RequiredUpdateControlRequestTypeDef, _OptionalUpdateControlRequestTypeDef
):
    pass


UpdateControlResponseResponseTypeDef = TypedDict(
    "UpdateControlResponseResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSettingsRequestTypeDef = TypedDict(
    "UpdateSettingsRequestTypeDef",
    {
        "snsTopic": str,
        "defaultAssessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "defaultProcessOwners": List["RoleTypeDef"],
        "kmsKey": str,
    },
    total=False,
)

UpdateSettingsResponseResponseTypeDef = TypedDict(
    "UpdateSettingsResponseResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateAssessmentReportIntegrityRequestTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityRequestTypeDef",
    {
        "s3RelativePath": str,
    },
)

ValidateAssessmentReportIntegrityResponseResponseTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityResponseResponseTypeDef",
    {
        "signatureValid": bool,
        "signatureAlgorithm": str,
        "signatureDateTime": str,
        "signatureKeyId": str,
        "validationErrors": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
