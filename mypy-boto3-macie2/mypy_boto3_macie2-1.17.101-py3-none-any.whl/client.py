"""
Type annotations for macie2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_macie2 import Macie2Client

    client: Macie2Client = boto3.client("macie2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingTypeType,
    GroupByType,
    JobStatusType,
    JobTypeType,
    MacieStatusType,
    TimeRangeType,
)
from .paginator import (
    DescribeBucketsPaginator,
    GetUsageStatisticsPaginator,
    ListClassificationJobsPaginator,
    ListCustomDataIdentifiersPaginator,
    ListFindingsFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    SearchResourcesPaginator,
)
from .type_defs import (
    AccountDetailTypeDef,
    BatchGetCustomDataIdentifiersResponseTypeDef,
    BucketCriteriaAdditionalPropertiesTypeDef,
    BucketSortCriteriaTypeDef,
    ClassificationExportConfigurationTypeDef,
    CreateClassificationJobResponseTypeDef,
    CreateCustomDataIdentifierResponseTypeDef,
    CreateFindingsFilterResponseTypeDef,
    CreateInvitationsResponseTypeDef,
    CreateMemberResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DescribeBucketsResponseTypeDef,
    DescribeClassificationJobResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    FindingCriteriaTypeDef,
    FindingStatisticsSortCriteriaTypeDef,
    GetAdministratorAccountResponseTypeDef,
    GetBucketStatisticsResponseTypeDef,
    GetClassificationExportConfigurationResponseTypeDef,
    GetCustomDataIdentifierResponseTypeDef,
    GetFindingsFilterResponseTypeDef,
    GetFindingsPublicationConfigurationResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMacieSessionResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    GetUsageTotalsResponseTypeDef,
    JobScheduleFrequencyTypeDef,
    ListClassificationJobsResponseTypeDef,
    ListCustomDataIdentifiersResponseTypeDef,
    ListFindingsFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListJobsFilterCriteriaTypeDef,
    ListJobsSortCriteriaTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutClassificationExportConfigurationResponseTypeDef,
    S3JobDefinitionTypeDef,
    SearchResourcesBucketCriteriaTypeDef,
    SearchResourcesResponseTypeDef,
    SearchResourcesSortCriteriaTypeDef,
    SecurityHubConfigurationTypeDef,
    SortCriteriaTypeDef,
    TestCustomDataIdentifierResponseTypeDef,
    UpdateFindingsFilterResponseTypeDef,
    UsageStatisticsFilterTypeDef,
    UsageStatisticsSortByTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Macie2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Macie2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_invitation(
        self, *, invitationId: str, administratorAccountId: str = None, masterAccount: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#accept_invitation)
        """

    def batch_get_custom_data_identifiers(
        self, *, ids: List[str] = None
    ) -> BatchGetCustomDataIdentifiersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.batch_get_custom_data_identifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#batch_get_custom_data_identifiers)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#can_paginate)
        """

    def create_classification_job(
        self,
        *,
        clientToken: str,
        jobType: JobTypeType,
        name: str,
        s3JobDefinition: "S3JobDefinitionTypeDef",
        customDataIdentifierIds: List[str] = None,
        description: str = None,
        initialRun: bool = None,
        samplingPercentage: int = None,
        scheduleFrequency: "JobScheduleFrequencyTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateClassificationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.create_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_classification_job)
        """

    def create_custom_data_identifier(
        self,
        *,
        clientToken: str = None,
        description: str = None,
        ignoreWords: List[str] = None,
        keywords: List[str] = None,
        maximumMatchDistance: int = None,
        name: str = None,
        regex: str = None,
        tags: Dict[str, str] = None
    ) -> CreateCustomDataIdentifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.create_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_custom_data_identifier)
        """

    def create_findings_filter(
        self,
        *,
        action: FindingsFilterActionType,
        findingCriteria: "FindingCriteriaTypeDef",
        name: str,
        clientToken: str = None,
        description: str = None,
        position: int = None,
        tags: Dict[str, str] = None
    ) -> CreateFindingsFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.create_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_findings_filter)
        """

    def create_invitations(
        self, *, accountIds: List[str], disableEmailNotification: bool = None, message: str = None
    ) -> CreateInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.create_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_invitations)
        """

    def create_member(
        self, *, account: AccountDetailTypeDef, tags: Dict[str, str] = None
    ) -> CreateMemberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.create_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_member)
        """

    def create_sample_findings(
        self, *, findingTypes: List[FindingTypeType] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.create_sample_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_sample_findings)
        """

    def decline_invitations(self, *, accountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#decline_invitations)
        """

    def delete_custom_data_identifier(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.delete_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_custom_data_identifier)
        """

    def delete_findings_filter(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.delete_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_findings_filter)
        """

    def delete_invitations(self, *, accountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_invitations)
        """

    def delete_member(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.delete_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_member)
        """

    def describe_buckets(
        self,
        *,
        criteria: Dict[str, BucketCriteriaAdditionalPropertiesTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: BucketSortCriteriaTypeDef = None
    ) -> DescribeBucketsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.describe_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#describe_buckets)
        """

    def describe_classification_job(
        self, *, jobId: str
    ) -> DescribeClassificationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.describe_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#describe_classification_job)
        """

    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#describe_organization_configuration)
        """

    def disable_macie(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.disable_macie)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disable_macie)
        """

    def disable_organization_admin_account(self, *, adminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disable_organization_admin_account)
        """

    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.disassociate_from_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disassociate_from_administrator_account)
        """

    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disassociate_from_master_account)
        """

    def disassociate_member(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.disassociate_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disassociate_member)
        """

    def enable_macie(
        self,
        *,
        clientToken: str = None,
        findingPublishingFrequency: FindingPublishingFrequencyType = None,
        status: MacieStatusType = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.enable_macie)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#enable_macie)
        """

    def enable_organization_admin_account(
        self, *, adminAccountId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#enable_organization_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#generate_presigned_url)
        """

    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_administrator_account)
        """

    def get_bucket_statistics(self, *, accountId: str = None) -> GetBucketStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_bucket_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_bucket_statistics)
        """

    def get_classification_export_configuration(
        self,
    ) -> GetClassificationExportConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_classification_export_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_classification_export_configuration)
        """

    def get_custom_data_identifier(self, *, id: str) -> GetCustomDataIdentifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_custom_data_identifier)
        """

    def get_finding_statistics(
        self,
        *,
        groupBy: GroupByType,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        size: int = None,
        sortCriteria: FindingStatisticsSortCriteriaTypeDef = None
    ) -> GetFindingStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_finding_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_finding_statistics)
        """

    def get_findings(
        self, *, findingIds: List[str], sortCriteria: SortCriteriaTypeDef = None
    ) -> GetFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_findings)
        """

    def get_findings_filter(self, *, id: str) -> GetFindingsFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_findings_filter)
        """

    def get_findings_publication_configuration(
        self,
    ) -> GetFindingsPublicationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_findings_publication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_findings_publication_configuration)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_invitations_count)
        """

    def get_macie_session(self) -> GetMacieSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_macie_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_macie_session)
        """

    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_master_account)
        """

    def get_member(self, *, id: str) -> GetMemberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_member)
        """

    def get_usage_statistics(
        self,
        *,
        filterBy: List[UsageStatisticsFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: UsageStatisticsSortByTypeDef = None,
        timeRange: TimeRangeType = None
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_usage_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_usage_statistics)
        """

    def get_usage_totals(self, *, timeRange: str = None) -> GetUsageTotalsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.get_usage_totals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_usage_totals)
        """

    def list_classification_jobs(
        self,
        *,
        filterCriteria: ListJobsFilterCriteriaTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: ListJobsSortCriteriaTypeDef = None
    ) -> ListClassificationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_classification_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_classification_jobs)
        """

    def list_custom_data_identifiers(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListCustomDataIdentifiersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_custom_data_identifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_custom_data_identifiers)
        """

    def list_findings(
        self,
        *,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: SortCriteriaTypeDef = None
    ) -> ListFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_findings)
        """

    def list_findings_filters(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListFindingsFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_findings_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_findings_filters)
        """

    def list_invitations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_invitations)
        """

    def list_members(
        self, *, maxResults: int = None, nextToken: str = None, onlyAssociated: str = None
    ) -> ListMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_members)
        """

    def list_organization_admin_accounts(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_organization_admin_accounts)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_tags_for_resource)
        """

    def put_classification_export_configuration(
        self, *, configuration: "ClassificationExportConfigurationTypeDef"
    ) -> PutClassificationExportConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.put_classification_export_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#put_classification_export_configuration)
        """

    def put_findings_publication_configuration(
        self,
        *,
        clientToken: str = None,
        securityHubConfiguration: "SecurityHubConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.put_findings_publication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#put_findings_publication_configuration)
        """

    def search_resources(
        self,
        *,
        bucketCriteria: SearchResourcesBucketCriteriaTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: SearchResourcesSortCriteriaTypeDef = None
    ) -> SearchResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.search_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#search_resources)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#tag_resource)
        """

    def test_custom_data_identifier(
        self,
        *,
        regex: str,
        sampleText: str,
        ignoreWords: List[str] = None,
        keywords: List[str] = None,
        maximumMatchDistance: int = None
    ) -> TestCustomDataIdentifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.test_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#test_custom_data_identifier)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#untag_resource)
        """

    def update_classification_job(self, *, jobId: str, jobStatus: JobStatusType) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.update_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_classification_job)
        """

    def update_findings_filter(
        self,
        *,
        id: str,
        action: FindingsFilterActionType = None,
        description: str = None,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        name: str = None,
        position: int = None,
        clientToken: str = None
    ) -> UpdateFindingsFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.update_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_findings_filter)
        """

    def update_macie_session(
        self,
        *,
        findingPublishingFrequency: FindingPublishingFrequencyType = None,
        status: MacieStatusType = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.update_macie_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_macie_session)
        """

    def update_member_session(self, *, id: str, status: MacieStatusType) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.update_member_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_member_session)
        """

    def update_organization_configuration(self, *, autoEnable: bool) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_organization_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_buckets"]
    ) -> DescribeBucketsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.DescribeBuckets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#describebucketspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_statistics"]
    ) -> GetUsageStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.GetUsageStatistics)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#getusagestatisticspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_classification_jobs"]
    ) -> ListClassificationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListClassificationJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listclassificationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_data_identifiers"]
    ) -> ListCustomDataIdentifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListCustomDataIdentifiers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listcustomdataidentifierspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listfindingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_findings_filters"]
    ) -> ListFindingsFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListFindingsFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listfindingsfilterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListInvitations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listinvitationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListMembers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listmemberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.ListOrganizationAdminAccounts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listorganizationadminaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> SearchResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/macie2.html#Macie2.Paginator.SearchResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#searchresourcespaginator)
        """
