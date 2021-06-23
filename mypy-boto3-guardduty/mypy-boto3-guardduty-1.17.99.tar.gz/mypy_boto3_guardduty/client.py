"""
Type annotations for guardduty service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_guardduty import GuardDutyClient

    client: GuardDutyClient = boto3.client("guardduty")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    ThreatIntelSetFormatType,
    UsageStatisticTypeType,
)
from .paginator import (
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListIPSetsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListThreatIntelSetsPaginator,
)
from .type_defs import (
    AccountDetailTypeDef,
    CreateDetectorResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateMembersResponseTypeDef,
    CreatePublishingDestinationResponseTypeDef,
    CreateThreatIntelSetResponseTypeDef,
    DataSourceConfigurationsTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribePublishingDestinationResponseTypeDef,
    DestinationPropertiesTypeDef,
    DisassociateMembersResponseTypeDef,
    FindingCriteriaTypeDef,
    GetDetectorResponseTypeDef,
    GetFilterResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingsStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberDetectorsResponseTypeDef,
    GetMembersResponseTypeDef,
    GetThreatIntelSetResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListPublishingDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    OrganizationDataSourceConfigurationsTypeDef,
    SortCriteriaTypeDef,
    StartMonitoringMembersResponseTypeDef,
    StopMonitoringMembersResponseTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateMemberDetectorsResponseTypeDef,
    UsageCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GuardDutyClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]


class GuardDutyClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_invitation(
        self, *, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#accept_invitation)
        """

    def archive_findings(self, *, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.archive_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#archive_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#can_paginate)
        """

    def create_detector(
        self,
        *,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: FindingPublishingFrequencyType = None,
        DataSources: DataSourceConfigurationsTypeDef = None,
        Tags: Dict[str, str] = None
    ) -> CreateDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_detector)
        """

    def create_filter(
        self,
        *,
        DetectorId: str,
        Name: str,
        FindingCriteria: "FindingCriteriaTypeDef",
        Description: str = None,
        Action: FilterActionType = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_filter)
        """

    def create_ip_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: IpSetFormatType,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_ip_set)
        """

    def create_members(
        self, *, DetectorId: str, AccountDetails: List[AccountDetailTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_members)
        """

    def create_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationType: Literal["S3"],
        DestinationProperties: "DestinationPropertiesTypeDef",
        ClientToken: str = None
    ) -> CreatePublishingDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_publishing_destination)
        """

    def create_sample_findings(
        self, *, DetectorId: str, FindingTypes: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_sample_findings)
        """

    def create_threat_intel_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: ThreatIntelSetFormatType,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateThreatIntelSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create_threat_intel_set)
        """

    def decline_invitations(self, *, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#decline_invitations)
        """

    def delete_detector(self, *, DetectorId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_detector)
        """

    def delete_filter(self, *, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_filter)
        """

    def delete_invitations(self, *, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_invitations)
        """

    def delete_ip_set(self, *, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_ip_set)
        """

    def delete_members(
        self, *, DetectorId: str, AccountIds: List[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_members)
        """

    def delete_publishing_destination(
        self, *, DetectorId: str, DestinationId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_publishing_destination)
        """

    def delete_threat_intel_set(self, *, DetectorId: str, ThreatIntelSetId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete_threat_intel_set)
        """

    def describe_organization_configuration(
        self, *, DetectorId: str
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#describe_organization_configuration)
        """

    def describe_publishing_destination(
        self, *, DetectorId: str, DestinationId: str
    ) -> DescribePublishingDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#describe_publishing_destination)
        """

    def disable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#disable_organization_admin_account)
        """

    def disassociate_from_master_account(self, *, DetectorId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#disassociate_from_master_account)
        """

    def disassociate_members(
        self, *, DetectorId: str, AccountIds: List[str]
    ) -> DisassociateMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#disassociate_members)
        """

    def enable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#enable_organization_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#generate_presigned_url)
        """

    def get_detector(self, *, DetectorId: str) -> GetDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_detector)
        """

    def get_filter(self, *, DetectorId: str, FilterName: str) -> GetFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_filter)
        """

    def get_findings(
        self, *, DetectorId: str, FindingIds: List[str], SortCriteria: SortCriteriaTypeDef = None
    ) -> GetFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_findings)
        """

    def get_findings_statistics(
        self,
        *,
        DetectorId: str,
        FindingStatisticTypes: List[Literal["COUNT_BY_SEVERITY"]],
        FindingCriteria: "FindingCriteriaTypeDef" = None
    ) -> GetFindingsStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_findings_statistics)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_invitations_count)
        """

    def get_ip_set(self, *, DetectorId: str, IpSetId: str) -> GetIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_ip_set)
        """

    def get_master_account(self, *, DetectorId: str) -> GetMasterAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_master_account)
        """

    def get_member_detectors(
        self, *, DetectorId: str, AccountIds: List[str]
    ) -> GetMemberDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_member_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_member_detectors)
        """

    def get_members(self, *, DetectorId: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_members)
        """

    def get_threat_intel_set(
        self, *, DetectorId: str, ThreatIntelSetId: str
    ) -> GetThreatIntelSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_threat_intel_set)
        """

    def get_usage_statistics(
        self,
        *,
        DetectorId: str,
        UsageStatisticType: UsageStatisticTypeType,
        UsageCriteria: UsageCriteriaTypeDef,
        Unit: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.get_usage_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get_usage_statistics)
        """

    def invite_members(
        self,
        *,
        DetectorId: str,
        AccountIds: List[str],
        DisableEmailNotification: bool = None,
        Message: str = None
    ) -> InviteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.invite_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#invite_members)
        """

    def list_detectors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_detectors)
        """

    def list_filters(
        self, *, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_filters)
        """

    def list_findings(
        self,
        *,
        DetectorId: str,
        FindingCriteria: "FindingCriteriaTypeDef" = None,
        SortCriteria: SortCriteriaTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_findings)
        """

    def list_invitations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_invitations)
        """

    def list_ip_sets(
        self, *, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_ip_sets)
        """

    def list_members(
        self,
        *,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None
    ) -> ListMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_members)
        """

    def list_organization_admin_accounts(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_organization_admin_accounts)
        """

    def list_publishing_destinations(
        self, *, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPublishingDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_publishing_destinations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_tags_for_resource)
        """

    def list_threat_intel_sets(
        self, *, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListThreatIntelSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list_threat_intel_sets)
        """

    def start_monitoring_members(
        self, *, DetectorId: str, AccountIds: List[str]
    ) -> StartMonitoringMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#start_monitoring_members)
        """

    def stop_monitoring_members(
        self, *, DetectorId: str, AccountIds: List[str]
    ) -> StopMonitoringMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#stop_monitoring_members)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#tag_resource)
        """

    def unarchive_findings(self, *, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#unarchive_findings)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#untag_resource)
        """

    def update_detector(
        self,
        *,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: FindingPublishingFrequencyType = None,
        DataSources: DataSourceConfigurationsTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_detector)
        """

    def update_filter(
        self,
        *,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: FilterActionType = None,
        Rank: int = None,
        FindingCriteria: "FindingCriteriaTypeDef" = None
    ) -> UpdateFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_filter)
        """

    def update_findings_feedback(
        self,
        *,
        DetectorId: str,
        FindingIds: List[str],
        Feedback: FeedbackType,
        Comments: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_findings_feedback)
        """

    def update_ip_set(
        self,
        *,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_ip_set)
        """

    def update_member_detectors(
        self,
        *,
        DetectorId: str,
        AccountIds: List[str],
        DataSources: DataSourceConfigurationsTypeDef = None
    ) -> UpdateMemberDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_member_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_member_detectors)
        """

    def update_organization_configuration(
        self,
        *,
        DetectorId: str,
        AutoEnable: bool,
        DataSources: OrganizationDataSourceConfigurationsTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_organization_configuration)
        """

    def update_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: "DestinationPropertiesTypeDef" = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_publishing_destination)
        """

    def update_threat_intel_set(
        self,
        *,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update_threat_intel_set)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_detectors"]) -> ListDetectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listdetectorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listfilterspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listfindingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_sets"]) -> ListIPSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listipsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listinvitationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listmemberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListOrganizationAdminAccounts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listorganizationadminaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> ListThreatIntelSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listthreatintelsetspaginator)
        """
