"""
Type annotations for managedblockchain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef

    data: ApprovalThresholdPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    EditionType,
    FrameworkType,
    InvitationStatusType,
    MemberStatusType,
    NetworkStatusType,
    NodeStatusType,
    ProposalStatusType,
    StateDBTypeType,
    ThresholdComparatorType,
    VoteValueType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalThresholdPolicyTypeDef",
    "CreateMemberInputTypeDef",
    "CreateMemberOutputResponseTypeDef",
    "CreateNetworkInputTypeDef",
    "CreateNetworkOutputResponseTypeDef",
    "CreateNodeInputTypeDef",
    "CreateNodeOutputResponseTypeDef",
    "CreateProposalInputTypeDef",
    "CreateProposalOutputResponseTypeDef",
    "DeleteMemberInputTypeDef",
    "DeleteNodeInputTypeDef",
    "GetMemberInputTypeDef",
    "GetMemberOutputResponseTypeDef",
    "GetNetworkInputTypeDef",
    "GetNetworkOutputResponseTypeDef",
    "GetNodeInputTypeDef",
    "GetNodeOutputResponseTypeDef",
    "GetProposalInputTypeDef",
    "GetProposalOutputResponseTypeDef",
    "InvitationTypeDef",
    "InviteActionTypeDef",
    "ListInvitationsInputTypeDef",
    "ListInvitationsOutputResponseTypeDef",
    "ListMembersInputTypeDef",
    "ListMembersOutputResponseTypeDef",
    "ListNetworksInputTypeDef",
    "ListNetworksOutputResponseTypeDef",
    "ListNodesInputTypeDef",
    "ListNodesOutputResponseTypeDef",
    "ListProposalVotesInputTypeDef",
    "ListProposalVotesOutputResponseTypeDef",
    "ListProposalsInputTypeDef",
    "ListProposalsOutputResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LogConfigurationTypeDef",
    "LogConfigurationsTypeDef",
    "MemberConfigurationTypeDef",
    "MemberFabricAttributesTypeDef",
    "MemberFabricConfigurationTypeDef",
    "MemberFabricLogPublishingConfigurationTypeDef",
    "MemberFrameworkAttributesTypeDef",
    "MemberFrameworkConfigurationTypeDef",
    "MemberLogPublishingConfigurationTypeDef",
    "MemberSummaryTypeDef",
    "MemberTypeDef",
    "NetworkEthereumAttributesTypeDef",
    "NetworkFabricAttributesTypeDef",
    "NetworkFabricConfigurationTypeDef",
    "NetworkFrameworkAttributesTypeDef",
    "NetworkFrameworkConfigurationTypeDef",
    "NetworkSummaryTypeDef",
    "NetworkTypeDef",
    "NodeConfigurationTypeDef",
    "NodeEthereumAttributesTypeDef",
    "NodeFabricAttributesTypeDef",
    "NodeFabricLogPublishingConfigurationTypeDef",
    "NodeFrameworkAttributesTypeDef",
    "NodeLogPublishingConfigurationTypeDef",
    "NodeSummaryTypeDef",
    "NodeTypeDef",
    "ProposalActionsTypeDef",
    "ProposalSummaryTypeDef",
    "ProposalTypeDef",
    "RejectInvitationInputTypeDef",
    "RemoveActionTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateMemberInputTypeDef",
    "UpdateNodeInputTypeDef",
    "VoteOnProposalInputTypeDef",
    "VoteSummaryTypeDef",
    "VotingPolicyTypeDef",
)

ApprovalThresholdPolicyTypeDef = TypedDict(
    "ApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": int,
        "ProposalDurationInHours": int,
        "ThresholdComparator": ThresholdComparatorType,
    },
    total=False,
)

CreateMemberInputTypeDef = TypedDict(
    "CreateMemberInputTypeDef",
    {
        "ClientRequestToken": str,
        "InvitationId": str,
        "NetworkId": str,
        "MemberConfiguration": "MemberConfigurationTypeDef",
    },
)

CreateMemberOutputResponseTypeDef = TypedDict(
    "CreateMemberOutputResponseTypeDef",
    {
        "MemberId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInputTypeDef = TypedDict(
    "_RequiredCreateNetworkInputTypeDef",
    {
        "ClientRequestToken": str,
        "Name": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "MemberConfiguration": "MemberConfigurationTypeDef",
    },
)
_OptionalCreateNetworkInputTypeDef = TypedDict(
    "_OptionalCreateNetworkInputTypeDef",
    {
        "Description": str,
        "FrameworkConfiguration": "NetworkFrameworkConfigurationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateNetworkInputTypeDef(
    _RequiredCreateNetworkInputTypeDef, _OptionalCreateNetworkInputTypeDef
):
    pass


CreateNetworkOutputResponseTypeDef = TypedDict(
    "CreateNetworkOutputResponseTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNodeInputTypeDef = TypedDict(
    "_RequiredCreateNodeInputTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "NodeConfiguration": "NodeConfigurationTypeDef",
    },
)
_OptionalCreateNodeInputTypeDef = TypedDict(
    "_OptionalCreateNodeInputTypeDef",
    {
        "MemberId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateNodeInputTypeDef(_RequiredCreateNodeInputTypeDef, _OptionalCreateNodeInputTypeDef):
    pass


CreateNodeOutputResponseTypeDef = TypedDict(
    "CreateNodeOutputResponseTypeDef",
    {
        "NodeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProposalInputTypeDef = TypedDict(
    "_RequiredCreateProposalInputTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "MemberId": str,
        "Actions": "ProposalActionsTypeDef",
    },
)
_OptionalCreateProposalInputTypeDef = TypedDict(
    "_OptionalCreateProposalInputTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateProposalInputTypeDef(
    _RequiredCreateProposalInputTypeDef, _OptionalCreateProposalInputTypeDef
):
    pass


CreateProposalOutputResponseTypeDef = TypedDict(
    "CreateProposalOutputResponseTypeDef",
    {
        "ProposalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMemberInputTypeDef = TypedDict(
    "DeleteMemberInputTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)

_RequiredDeleteNodeInputTypeDef = TypedDict(
    "_RequiredDeleteNodeInputTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
    },
)
_OptionalDeleteNodeInputTypeDef = TypedDict(
    "_OptionalDeleteNodeInputTypeDef",
    {
        "MemberId": str,
    },
    total=False,
)


class DeleteNodeInputTypeDef(_RequiredDeleteNodeInputTypeDef, _OptionalDeleteNodeInputTypeDef):
    pass


GetMemberInputTypeDef = TypedDict(
    "GetMemberInputTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)

GetMemberOutputResponseTypeDef = TypedDict(
    "GetMemberOutputResponseTypeDef",
    {
        "Member": "MemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkInputTypeDef = TypedDict(
    "GetNetworkInputTypeDef",
    {
        "NetworkId": str,
    },
)

GetNetworkOutputResponseTypeDef = TypedDict(
    "GetNetworkOutputResponseTypeDef",
    {
        "Network": "NetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNodeInputTypeDef = TypedDict(
    "_RequiredGetNodeInputTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
    },
)
_OptionalGetNodeInputTypeDef = TypedDict(
    "_OptionalGetNodeInputTypeDef",
    {
        "MemberId": str,
    },
    total=False,
)


class GetNodeInputTypeDef(_RequiredGetNodeInputTypeDef, _OptionalGetNodeInputTypeDef):
    pass


GetNodeOutputResponseTypeDef = TypedDict(
    "GetNodeOutputResponseTypeDef",
    {
        "Node": "NodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProposalInputTypeDef = TypedDict(
    "GetProposalInputTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
    },
)

GetProposalOutputResponseTypeDef = TypedDict(
    "GetProposalOutputResponseTypeDef",
    {
        "Proposal": "ProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "InvitationId": str,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Status": InvitationStatusType,
        "NetworkSummary": "NetworkSummaryTypeDef",
        "Arn": str,
    },
    total=False,
)

InviteActionTypeDef = TypedDict(
    "InviteActionTypeDef",
    {
        "Principal": str,
    },
)

ListInvitationsInputTypeDef = TypedDict(
    "ListInvitationsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInvitationsOutputResponseTypeDef = TypedDict(
    "ListInvitationsOutputResponseTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersInputTypeDef = TypedDict(
    "_RequiredListMembersInputTypeDef",
    {
        "NetworkId": str,
    },
)
_OptionalListMembersInputTypeDef = TypedDict(
    "_OptionalListMembersInputTypeDef",
    {
        "Name": str,
        "Status": MemberStatusType,
        "IsOwned": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListMembersInputTypeDef(_RequiredListMembersInputTypeDef, _OptionalListMembersInputTypeDef):
    pass


ListMembersOutputResponseTypeDef = TypedDict(
    "ListMembersOutputResponseTypeDef",
    {
        "Members": List["MemberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworksInputTypeDef = TypedDict(
    "ListNetworksInputTypeDef",
    {
        "Name": str,
        "Framework": FrameworkType,
        "Status": NetworkStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListNetworksOutputResponseTypeDef = TypedDict(
    "ListNetworksOutputResponseTypeDef",
    {
        "Networks": List["NetworkSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNodesInputTypeDef = TypedDict(
    "_RequiredListNodesInputTypeDef",
    {
        "NetworkId": str,
    },
)
_OptionalListNodesInputTypeDef = TypedDict(
    "_OptionalListNodesInputTypeDef",
    {
        "MemberId": str,
        "Status": NodeStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListNodesInputTypeDef(_RequiredListNodesInputTypeDef, _OptionalListNodesInputTypeDef):
    pass


ListNodesOutputResponseTypeDef = TypedDict(
    "ListNodesOutputResponseTypeDef",
    {
        "Nodes": List["NodeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProposalVotesInputTypeDef = TypedDict(
    "_RequiredListProposalVotesInputTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
    },
)
_OptionalListProposalVotesInputTypeDef = TypedDict(
    "_OptionalListProposalVotesInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListProposalVotesInputTypeDef(
    _RequiredListProposalVotesInputTypeDef, _OptionalListProposalVotesInputTypeDef
):
    pass


ListProposalVotesOutputResponseTypeDef = TypedDict(
    "ListProposalVotesOutputResponseTypeDef",
    {
        "ProposalVotes": List["VoteSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProposalsInputTypeDef = TypedDict(
    "_RequiredListProposalsInputTypeDef",
    {
        "NetworkId": str,
    },
)
_OptionalListProposalsInputTypeDef = TypedDict(
    "_OptionalListProposalsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListProposalsInputTypeDef(
    _RequiredListProposalsInputTypeDef, _OptionalListProposalsInputTypeDef
):
    pass


ListProposalsOutputResponseTypeDef = TypedDict(
    "ListProposalsOutputResponseTypeDef",
    {
        "Proposals": List["ProposalSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LogConfigurationsTypeDef = TypedDict(
    "LogConfigurationsTypeDef",
    {
        "Cloudwatch": "LogConfigurationTypeDef",
    },
    total=False,
)

_RequiredMemberConfigurationTypeDef = TypedDict(
    "_RequiredMemberConfigurationTypeDef",
    {
        "Name": str,
        "FrameworkConfiguration": "MemberFrameworkConfigurationTypeDef",
    },
)
_OptionalMemberConfigurationTypeDef = TypedDict(
    "_OptionalMemberConfigurationTypeDef",
    {
        "Description": str,
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
        "Tags": Dict[str, str],
        "KmsKeyArn": str,
    },
    total=False,
)


class MemberConfigurationTypeDef(
    _RequiredMemberConfigurationTypeDef, _OptionalMemberConfigurationTypeDef
):
    pass


MemberFabricAttributesTypeDef = TypedDict(
    "MemberFabricAttributesTypeDef",
    {
        "AdminUsername": str,
        "CaEndpoint": str,
    },
    total=False,
)

MemberFabricConfigurationTypeDef = TypedDict(
    "MemberFabricConfigurationTypeDef",
    {
        "AdminUsername": str,
        "AdminPassword": str,
    },
)

MemberFabricLogPublishingConfigurationTypeDef = TypedDict(
    "MemberFabricLogPublishingConfigurationTypeDef",
    {
        "CaLogs": "LogConfigurationsTypeDef",
    },
    total=False,
)

MemberFrameworkAttributesTypeDef = TypedDict(
    "MemberFrameworkAttributesTypeDef",
    {
        "Fabric": "MemberFabricAttributesTypeDef",
    },
    total=False,
)

MemberFrameworkConfigurationTypeDef = TypedDict(
    "MemberFrameworkConfigurationTypeDef",
    {
        "Fabric": "MemberFabricConfigurationTypeDef",
    },
    total=False,
)

MemberLogPublishingConfigurationTypeDef = TypedDict(
    "MemberLogPublishingConfigurationTypeDef",
    {
        "Fabric": "MemberFabricLogPublishingConfigurationTypeDef",
    },
    total=False,
)

MemberSummaryTypeDef = TypedDict(
    "MemberSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": MemberStatusType,
        "CreationDate": datetime,
        "IsOwned": bool,
        "Arn": str,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "NetworkId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "FrameworkAttributes": "MemberFrameworkAttributesTypeDef",
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
        "Status": MemberStatusType,
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

NetworkEthereumAttributesTypeDef = TypedDict(
    "NetworkEthereumAttributesTypeDef",
    {
        "ChainId": str,
    },
    total=False,
)

NetworkFabricAttributesTypeDef = TypedDict(
    "NetworkFabricAttributesTypeDef",
    {
        "OrderingServiceEndpoint": str,
        "Edition": EditionType,
    },
    total=False,
)

NetworkFabricConfigurationTypeDef = TypedDict(
    "NetworkFabricConfigurationTypeDef",
    {
        "Edition": EditionType,
    },
)

NetworkFrameworkAttributesTypeDef = TypedDict(
    "NetworkFrameworkAttributesTypeDef",
    {
        "Fabric": "NetworkFabricAttributesTypeDef",
        "Ethereum": "NetworkEthereumAttributesTypeDef",
    },
    total=False,
)

NetworkFrameworkConfigurationTypeDef = TypedDict(
    "NetworkFrameworkConfigurationTypeDef",
    {
        "Fabric": "NetworkFabricConfigurationTypeDef",
    },
    total=False,
)

NetworkSummaryTypeDef = TypedDict(
    "NetworkSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "Status": NetworkStatusType,
        "CreationDate": datetime,
        "Arn": str,
    },
    total=False,
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "FrameworkAttributes": "NetworkFrameworkAttributesTypeDef",
        "VpcEndpointServiceName": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "Status": NetworkStatusType,
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

_RequiredNodeConfigurationTypeDef = TypedDict(
    "_RequiredNodeConfigurationTypeDef",
    {
        "InstanceType": str,
    },
)
_OptionalNodeConfigurationTypeDef = TypedDict(
    "_OptionalNodeConfigurationTypeDef",
    {
        "AvailabilityZone": str,
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
        "StateDB": StateDBTypeType,
    },
    total=False,
)


class NodeConfigurationTypeDef(
    _RequiredNodeConfigurationTypeDef, _OptionalNodeConfigurationTypeDef
):
    pass


NodeEthereumAttributesTypeDef = TypedDict(
    "NodeEthereumAttributesTypeDef",
    {
        "HttpEndpoint": str,
        "WebSocketEndpoint": str,
    },
    total=False,
)

NodeFabricAttributesTypeDef = TypedDict(
    "NodeFabricAttributesTypeDef",
    {
        "PeerEndpoint": str,
        "PeerEventEndpoint": str,
    },
    total=False,
)

NodeFabricLogPublishingConfigurationTypeDef = TypedDict(
    "NodeFabricLogPublishingConfigurationTypeDef",
    {
        "ChaincodeLogs": "LogConfigurationsTypeDef",
        "PeerLogs": "LogConfigurationsTypeDef",
    },
    total=False,
)

NodeFrameworkAttributesTypeDef = TypedDict(
    "NodeFrameworkAttributesTypeDef",
    {
        "Fabric": "NodeFabricAttributesTypeDef",
        "Ethereum": "NodeEthereumAttributesTypeDef",
    },
    total=False,
)

NodeLogPublishingConfigurationTypeDef = TypedDict(
    "NodeLogPublishingConfigurationTypeDef",
    {
        "Fabric": "NodeFabricLogPublishingConfigurationTypeDef",
    },
    total=False,
)

NodeSummaryTypeDef = TypedDict(
    "NodeSummaryTypeDef",
    {
        "Id": str,
        "Status": NodeStatusType,
        "CreationDate": datetime,
        "AvailabilityZone": str,
        "InstanceType": str,
        "Arn": str,
    },
    total=False,
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "Id": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "FrameworkAttributes": "NodeFrameworkAttributesTypeDef",
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
        "StateDB": StateDBTypeType,
        "Status": NodeStatusType,
        "CreationDate": datetime,
        "Tags": Dict[str, str],
        "Arn": str,
        "KmsKeyArn": str,
    },
    total=False,
)

ProposalActionsTypeDef = TypedDict(
    "ProposalActionsTypeDef",
    {
        "Invitations": List["InviteActionTypeDef"],
        "Removals": List["RemoveActionTypeDef"],
    },
    total=False,
)

ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "ProposalId": str,
        "Description": str,
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": ProposalStatusType,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "Arn": str,
    },
    total=False,
)

ProposalTypeDef = TypedDict(
    "ProposalTypeDef",
    {
        "ProposalId": str,
        "NetworkId": str,
        "Description": str,
        "Actions": "ProposalActionsTypeDef",
        "ProposedByMemberId": str,
        "ProposedByMemberName": str,
        "Status": ProposalStatusType,
        "CreationDate": datetime,
        "ExpirationDate": datetime,
        "YesVoteCount": int,
        "NoVoteCount": int,
        "OutstandingVoteCount": int,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

RejectInvitationInputTypeDef = TypedDict(
    "RejectInvitationInputTypeDef",
    {
        "InvitationId": str,
    },
)

RemoveActionTypeDef = TypedDict(
    "RemoveActionTypeDef",
    {
        "MemberId": str,
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateMemberInputTypeDef = TypedDict(
    "_RequiredUpdateMemberInputTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)
_OptionalUpdateMemberInputTypeDef = TypedDict(
    "_OptionalUpdateMemberInputTypeDef",
    {
        "LogPublishingConfiguration": "MemberLogPublishingConfigurationTypeDef",
    },
    total=False,
)


class UpdateMemberInputTypeDef(
    _RequiredUpdateMemberInputTypeDef, _OptionalUpdateMemberInputTypeDef
):
    pass


_RequiredUpdateNodeInputTypeDef = TypedDict(
    "_RequiredUpdateNodeInputTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
    },
)
_OptionalUpdateNodeInputTypeDef = TypedDict(
    "_OptionalUpdateNodeInputTypeDef",
    {
        "MemberId": str,
        "LogPublishingConfiguration": "NodeLogPublishingConfigurationTypeDef",
    },
    total=False,
)


class UpdateNodeInputTypeDef(_RequiredUpdateNodeInputTypeDef, _OptionalUpdateNodeInputTypeDef):
    pass


VoteOnProposalInputTypeDef = TypedDict(
    "VoteOnProposalInputTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
        "VoterMemberId": str,
        "Vote": VoteValueType,
    },
)

VoteSummaryTypeDef = TypedDict(
    "VoteSummaryTypeDef",
    {
        "Vote": VoteValueType,
        "MemberName": str,
        "MemberId": str,
    },
    total=False,
)

VotingPolicyTypeDef = TypedDict(
    "VotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": "ApprovalThresholdPolicyTypeDef",
    },
    total=False,
)
