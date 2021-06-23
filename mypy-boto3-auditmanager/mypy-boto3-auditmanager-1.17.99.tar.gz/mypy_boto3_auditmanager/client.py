"""
Type annotations for auditmanager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_auditmanager import AuditManagerClient

    client: AuditManagerClient = boto3.client("auditmanager")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    AssessmentStatusType,
    ControlSetStatusType,
    ControlStatusType,
    ControlTypeType,
    FrameworkTypeType,
    SettingAttributeType,
    SourceTypeType,
)
from .type_defs import (
    AssessmentReportsDestinationTypeDef,
    BatchAssociateAssessmentReportEvidenceResponseTypeDef,
    BatchCreateDelegationByAssessmentResponseTypeDef,
    BatchDeleteDelegationByAssessmentResponseTypeDef,
    BatchDisassociateAssessmentReportEvidenceResponseTypeDef,
    BatchImportEvidenceToAssessmentControlResponseTypeDef,
    ControlMappingSourceTypeDef,
    CreateAssessmentFrameworkControlSetTypeDef,
    CreateAssessmentFrameworkResponseTypeDef,
    CreateAssessmentReportResponseTypeDef,
    CreateAssessmentResponseTypeDef,
    CreateControlMappingSourceTypeDef,
    CreateControlResponseTypeDef,
    CreateDelegationRequestTypeDef,
    DeregisterAccountResponseTypeDef,
    GetAccountStatusResponseTypeDef,
    GetAssessmentFrameworkResponseTypeDef,
    GetAssessmentReportUrlResponseTypeDef,
    GetAssessmentResponseTypeDef,
    GetChangeLogsResponseTypeDef,
    GetControlResponseTypeDef,
    GetDelegationsResponseTypeDef,
    GetEvidenceByEvidenceFolderResponseTypeDef,
    GetEvidenceFolderResponseTypeDef,
    GetEvidenceFoldersByAssessmentControlResponseTypeDef,
    GetEvidenceFoldersByAssessmentResponseTypeDef,
    GetEvidenceResponseTypeDef,
    GetOrganizationAdminAccountResponseTypeDef,
    GetServicesInScopeResponseTypeDef,
    GetSettingsResponseTypeDef,
    ListAssessmentFrameworksResponseTypeDef,
    ListAssessmentReportsResponseTypeDef,
    ListAssessmentsResponseTypeDef,
    ListControlsResponseTypeDef,
    ListKeywordsForDataSourceResponseTypeDef,
    ListNotificationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ManualEvidenceTypeDef,
    RegisterAccountResponseTypeDef,
    RegisterOrganizationAdminAccountResponseTypeDef,
    RoleTypeDef,
    ScopeTypeDef,
    UpdateAssessmentControlResponseTypeDef,
    UpdateAssessmentControlSetStatusResponseTypeDef,
    UpdateAssessmentFrameworkControlSetTypeDef,
    UpdateAssessmentFrameworkResponseTypeDef,
    UpdateAssessmentResponseTypeDef,
    UpdateAssessmentStatusResponseTypeDef,
    UpdateControlResponseTypeDef,
    UpdateSettingsResponseTypeDef,
    ValidateAssessmentReportIntegrityResponseTypeDef,
)

__all__ = ("AuditManagerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AuditManagerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_assessment_report_evidence_folder(
        self, *, assessmentId: str, evidenceFolderId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.associate_assessment_report_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#associate_assessment_report_evidence_folder)
        """

    def batch_associate_assessment_report_evidence(
        self, *, assessmentId: str, evidenceFolderId: str, evidenceIds: List[str]
    ) -> BatchAssociateAssessmentReportEvidenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.batch_associate_assessment_report_evidence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_associate_assessment_report_evidence)
        """

    def batch_create_delegation_by_assessment(
        self, *, createDelegationRequests: List["CreateDelegationRequestTypeDef"], assessmentId: str
    ) -> BatchCreateDelegationByAssessmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.batch_create_delegation_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_create_delegation_by_assessment)
        """

    def batch_delete_delegation_by_assessment(
        self, *, delegationIds: List[str], assessmentId: str
    ) -> BatchDeleteDelegationByAssessmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.batch_delete_delegation_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_delete_delegation_by_assessment)
        """

    def batch_disassociate_assessment_report_evidence(
        self, *, assessmentId: str, evidenceFolderId: str, evidenceIds: List[str]
    ) -> BatchDisassociateAssessmentReportEvidenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.batch_disassociate_assessment_report_evidence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_disassociate_assessment_report_evidence)
        """

    def batch_import_evidence_to_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        manualEvidence: List["ManualEvidenceTypeDef"]
    ) -> BatchImportEvidenceToAssessmentControlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.batch_import_evidence_to_assessment_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_import_evidence_to_assessment_control)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#can_paginate)
        """

    def create_assessment(
        self,
        *,
        name: str,
        assessmentReportsDestination: "AssessmentReportsDestinationTypeDef",
        scope: "ScopeTypeDef",
        roles: List["RoleTypeDef"],
        frameworkId: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssessmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.create_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_assessment)
        """

    def create_assessment_framework(
        self,
        *,
        name: str,
        controlSets: List[CreateAssessmentFrameworkControlSetTypeDef],
        description: str = None,
        complianceType: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssessmentFrameworkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.create_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_assessment_framework)
        """

    def create_assessment_report(
        self, *, name: str, assessmentId: str, description: str = None
    ) -> CreateAssessmentReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.create_assessment_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_assessment_report)
        """

    def create_control(
        self,
        *,
        name: str,
        controlMappingSources: List[CreateControlMappingSourceTypeDef],
        description: str = None,
        testingInformation: str = None,
        actionPlanTitle: str = None,
        actionPlanInstructions: str = None,
        tags: Dict[str, str] = None
    ) -> CreateControlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.create_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_control)
        """

    def delete_assessment(self, *, assessmentId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.delete_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment)
        """

    def delete_assessment_framework(self, *, frameworkId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment_framework)
        """

    def delete_assessment_report(
        self, *, assessmentId: str, assessmentReportId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment_report)
        """

    def delete_control(self, *, controlId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.delete_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_control)
        """

    def deregister_account(self) -> DeregisterAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.deregister_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#deregister_account)
        """

    def deregister_organization_admin_account(
        self, *, adminAccountId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.deregister_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#deregister_organization_admin_account)
        """

    def disassociate_assessment_report_evidence_folder(
        self, *, assessmentId: str, evidenceFolderId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.disassociate_assessment_report_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#disassociate_assessment_report_evidence_folder)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#generate_presigned_url)
        """

    def get_account_status(self) -> GetAccountStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_account_status)
        """

    def get_assessment(self, *, assessmentId: str) -> GetAssessmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_assessment)
        """

    def get_assessment_framework(
        self, *, frameworkId: str
    ) -> GetAssessmentFrameworkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_assessment_framework)
        """

    def get_assessment_report_url(
        self, *, assessmentReportId: str, assessmentId: str
    ) -> GetAssessmentReportUrlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_assessment_report_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_assessment_report_url)
        """

    def get_change_logs(
        self,
        *,
        assessmentId: str,
        controlSetId: str = None,
        controlId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetChangeLogsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_change_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_change_logs)
        """

    def get_control(self, *, controlId: str) -> GetControlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_control)
        """

    def get_delegations(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> GetDelegationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_delegations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_delegations)
        """

    def get_evidence(
        self, *, assessmentId: str, controlSetId: str, evidenceFolderId: str, evidenceId: str
    ) -> GetEvidenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_evidence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence)
        """

    def get_evidence_by_evidence_folder(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        evidenceFolderId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetEvidenceByEvidenceFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_evidence_by_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_by_evidence_folder)
        """

    def get_evidence_folder(
        self, *, assessmentId: str, controlSetId: str, evidenceFolderId: str
    ) -> GetEvidenceFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_folder)
        """

    def get_evidence_folders_by_assessment(
        self, *, assessmentId: str, nextToken: str = None, maxResults: int = None
    ) -> GetEvidenceFoldersByAssessmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_folders_by_assessment)
        """

    def get_evidence_folders_by_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetEvidenceFoldersByAssessmentControlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_folders_by_assessment_control)
        """

    def get_organization_admin_account(self) -> GetOrganizationAdminAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_organization_admin_account)
        """

    def get_services_in_scope(self) -> GetServicesInScopeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_services_in_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_services_in_scope)
        """

    def get_settings(self, *, attribute: SettingAttributeType) -> GetSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.get_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_settings)
        """

    def list_assessment_frameworks(
        self, *, frameworkType: FrameworkTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentFrameworksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_assessment_frameworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessment_frameworks)
        """

    def list_assessment_reports(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_assessment_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessment_reports)
        """

    def list_assessments(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_assessments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessments)
        """

    def list_controls(
        self, *, controlType: ControlTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListControlsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_controls)
        """

    def list_keywords_for_data_source(
        self, *, source: SourceTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListKeywordsForDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_keywords_for_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_keywords_for_data_source)
        """

    def list_notifications(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListNotificationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_notifications)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_tags_for_resource)
        """

    def register_account(
        self, *, kmsKey: str = None, delegatedAdminAccount: str = None
    ) -> RegisterAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.register_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#register_account)
        """

    def register_organization_admin_account(
        self, *, adminAccountId: str
    ) -> RegisterOrganizationAdminAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.register_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#register_organization_admin_account)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#untag_resource)
        """

    def update_assessment(
        self,
        *,
        assessmentId: str,
        scope: "ScopeTypeDef",
        assessmentName: str = None,
        assessmentDescription: str = None,
        assessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
        roles: List["RoleTypeDef"] = None
    ) -> UpdateAssessmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment)
        """

    def update_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        controlStatus: ControlStatusType = None,
        commentBody: str = None
    ) -> UpdateAssessmentControlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_control)
        """

    def update_assessment_control_set_status(
        self, *, assessmentId: str, controlSetId: str, status: ControlSetStatusType, comment: str
    ) -> UpdateAssessmentControlSetStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control_set_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_control_set_status)
        """

    def update_assessment_framework(
        self,
        *,
        frameworkId: str,
        name: str,
        controlSets: List[UpdateAssessmentFrameworkControlSetTypeDef],
        description: str = None,
        complianceType: str = None
    ) -> UpdateAssessmentFrameworkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_framework)
        """

    def update_assessment_status(
        self, *, assessmentId: str, status: AssessmentStatusType
    ) -> UpdateAssessmentStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_assessment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_status)
        """

    def update_control(
        self,
        *,
        controlId: str,
        name: str,
        controlMappingSources: List["ControlMappingSourceTypeDef"],
        description: str = None,
        testingInformation: str = None,
        actionPlanTitle: str = None,
        actionPlanInstructions: str = None
    ) -> UpdateControlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_control)
        """

    def update_settings(
        self,
        *,
        snsTopic: str = None,
        defaultAssessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
        defaultProcessOwners: List["RoleTypeDef"] = None,
        kmsKey: str = None
    ) -> UpdateSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.update_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_settings)
        """

    def validate_assessment_report_integrity(
        self, *, s3RelativePath: str
    ) -> ValidateAssessmentReportIntegrityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/auditmanager.html#AuditManager.Client.validate_assessment_report_integrity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#validate_assessment_report_integrity)
        """
