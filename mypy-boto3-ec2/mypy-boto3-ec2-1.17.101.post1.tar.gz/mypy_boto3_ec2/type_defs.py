"""
Type annotations for ec2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ec2.type_defs import AcceptReservedInstancesExchangeQuoteRequestTypeDef

    data: AcceptReservedInstancesExchangeQuoteRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Optional, Union

from botocore.response import StreamingBody

from .literals import (
    AccountAttributeNameType,
    ActivityStatusType,
    AffinityType,
    AllocationStateType,
    AllocationStrategyType,
    AllowsMultipleInstanceTypesType,
    AnalysisStatusType,
    ApplianceModeSupportValueType,
    ArchitectureTypeType,
    ArchitectureValuesType,
    AssociationStatusCodeType,
    AttachmentStatusType,
    AutoAcceptSharedAssociationsValueType,
    AutoAcceptSharedAttachmentsValueType,
    AutoPlacementType,
    AvailabilityZoneOptInStatusType,
    AvailabilityZoneStateType,
    BatchStateType,
    BgpStatusType,
    BootModeTypeType,
    BootModeValuesType,
    BundleTaskStateType,
    ByoipCidrStateType,
    CancelBatchErrorCodeType,
    CancelSpotInstanceRequestStateType,
    CapacityReservationInstancePlatformType,
    CapacityReservationPreferenceType,
    CapacityReservationStateType,
    CapacityReservationTenancyType,
    CarrierGatewayStateType,
    ClientCertificateRevocationListStatusCodeType,
    ClientVpnAuthenticationTypeType,
    ClientVpnAuthorizationRuleStatusCodeType,
    ClientVpnConnectionStatusCodeType,
    ClientVpnEndpointAttributeStatusCodeType,
    ClientVpnEndpointStatusCodeType,
    ClientVpnRouteStatusCodeType,
    ConnectionNotificationStateType,
    ConnectivityTypeType,
    ConversionTaskStateType,
    DatafeedSubscriptionStateType,
    DefaultRouteTableAssociationValueType,
    DefaultRouteTablePropagationValueType,
    DefaultTargetCapacityTypeType,
    DeleteFleetErrorCodeType,
    DeleteQueuedReservedInstancesErrorCodeType,
    DeviceTypeType,
    DiskImageFormatType,
    DiskTypeType,
    DnsNameStateType,
    DnsSupportValueType,
    DomainTypeType,
    EbsEncryptionSupportType,
    EbsNvmeSupportType,
    EbsOptimizedSupportType,
    ElasticGpuStatusType,
    EnaSupportType,
    EndDateTypeType,
    EphemeralNvmeSupportType,
    EventCodeType,
    EventTypeType,
    ExcessCapacityTerminationPolicyType,
    ExportEnvironmentType,
    ExportTaskStateType,
    FastSnapshotRestoreStateCodeType,
    FleetActivityStatusType,
    FleetEventTypeType,
    FleetExcessCapacityTerminationPolicyType,
    FleetOnDemandAllocationStrategyType,
    FleetStateCodeType,
    FleetTypeType,
    FlowLogsResourceTypeType,
    FpgaImageAttributeNameType,
    FpgaImageStateCodeType,
    HostRecoveryType,
    HostTenancyType,
    HttpTokensStateType,
    HypervisorTypeType,
    IamInstanceProfileAssociationStateType,
    Igmpv2SupportValueType,
    ImageAttributeNameType,
    ImageStateType,
    ImageTypeValuesType,
    InstanceAttributeNameType,
    InstanceHealthStatusType,
    InstanceInterruptionBehaviorType,
    InstanceLifecycleType,
    InstanceLifecycleTypeType,
    InstanceMatchCriteriaType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataOptionsStateType,
    InstanceStateNameType,
    InstanceTypeHypervisorType,
    InstanceTypeType,
    InterfacePermissionTypeType,
    InterfaceProtocolTypeType,
    Ipv6SupportValueType,
    LaunchTemplateErrorCodeType,
    LaunchTemplateHttpTokensStateType,
    LaunchTemplateInstanceMetadataEndpointStateType,
    LaunchTemplateInstanceMetadataOptionsStateType,
    ListingStateType,
    ListingStatusType,
    LocalGatewayRouteStateType,
    LocalGatewayRouteTypeType,
    LocationTypeType,
    LogDestinationTypeType,
    MembershipTypeType,
    ModifyAvailabilityZoneOptInStatusType,
    MonitoringStateType,
    MoveStatusType,
    MulticastSupportValueType,
    NatGatewayStateType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    NetworkInterfacePermissionStateCodeType,
    NetworkInterfaceStatusType,
    NetworkInterfaceTypeType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    OnDemandAllocationStrategyType,
    OperationTypeType,
    PartitionLoadFrequencyType,
    PaymentOptionType,
    PlacementGroupStateType,
    PlacementGroupStrategyType,
    PlacementStrategyType,
    PrefixListStateType,
    PrincipalTypeType,
    ProductCodeValuesType,
    ProtocolType,
    ReplaceRootVolumeTaskStateType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    ReservationStateType,
    ReservedInstanceStateType,
    ResourceTypeType,
    RIProductDescriptionType,
    RootDeviceTypeType,
    RouteOriginType,
    RouteStateType,
    RouteTableAssociationStateCodeType,
    RuleActionType,
    SelfServicePortalType,
    ServiceStateType,
    ServiceTypeType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotStateType,
    SpotAllocationStrategyType,
    SpotInstanceInterruptionBehaviorType,
    SpotInstanceStateType,
    SpotInstanceTypeType,
    StateType,
    StaticSourcesSupportValueType,
    StatusType,
    StatusTypeType,
    SubnetCidrBlockStateCodeType,
    SubnetStateType,
    SummaryStatusType,
    TelemetryStatusType,
    TenancyType,
    TrafficDirectionType,
    TrafficMirrorFilterRuleFieldType,
    TrafficMirrorRuleActionType,
    TrafficMirrorSessionFieldType,
    TrafficMirrorTargetTypeType,
    TrafficTypeType,
    TransitGatewayAssociationStateType,
    TransitGatewayAttachmentResourceTypeType,
    TransitGatewayAttachmentStateType,
    TransitGatewayConnectPeerStateType,
    TransitGatewayMulitcastDomainAssociationStateType,
    TransitGatewayMulticastDomainStateType,
    TransitGatewayPrefixListReferenceStateType,
    TransitGatewayPropagationStateType,
    TransitGatewayRouteStateType,
    TransitGatewayRouteTableStateType,
    TransitGatewayRouteTypeType,
    TransitGatewayStateType,
    TransportProtocolType,
    TunnelInsideIpVersionType,
    UnlimitedSupportedInstanceFamilyType,
    UnsuccessfulInstanceCreditSpecificationErrorCodeType,
    UsageClassTypeType,
    VirtualizationTypeType,
    VolumeAttachmentStateType,
    VolumeAttributeNameType,
    VolumeModificationStateType,
    VolumeStateType,
    VolumeStatusInfoStatusType,
    VolumeStatusNameType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcCidrBlockStateCodeType,
    VpcEndpointTypeType,
    VpcPeeringConnectionStateReasonCodeType,
    VpcStateType,
    VpnEcmpSupportValueType,
    VpnStateType,
    scopeType,
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
    "AcceptReservedInstancesExchangeQuoteRequestTypeDef",
    "AcceptReservedInstancesExchangeQuoteResultResponseTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsRequestTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsResultResponseTypeDef",
    "AcceptTransitGatewayPeeringAttachmentRequestTypeDef",
    "AcceptTransitGatewayPeeringAttachmentResultResponseTypeDef",
    "AcceptTransitGatewayVpcAttachmentRequestTypeDef",
    "AcceptTransitGatewayVpcAttachmentResultResponseTypeDef",
    "AcceptVpcEndpointConnectionsRequestTypeDef",
    "AcceptVpcEndpointConnectionsResultResponseTypeDef",
    "AcceptVpcPeeringConnectionRequestTypeDef",
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    "AcceptVpcPeeringConnectionResultResponseTypeDef",
    "AccountAttributeTypeDef",
    "AccountAttributeValueTypeDef",
    "ActiveInstanceTypeDef",
    "AddPrefixListEntryTypeDef",
    "AddressAttributeTypeDef",
    "AddressTypeDef",
    "AdvertiseByoipCidrRequestTypeDef",
    "AdvertiseByoipCidrResultResponseTypeDef",
    "AllocateAddressRequestTypeDef",
    "AllocateAddressResultResponseTypeDef",
    "AllocateHostsRequestTypeDef",
    "AllocateHostsResultResponseTypeDef",
    "AllowedPrincipalTypeDef",
    "AlternatePathHintTypeDef",
    "AnalysisAclRuleTypeDef",
    "AnalysisComponentTypeDef",
    "AnalysisLoadBalancerListenerTypeDef",
    "AnalysisLoadBalancerTargetTypeDef",
    "AnalysisPacketHeaderTypeDef",
    "AnalysisRouteTableRouteTypeDef",
    "AnalysisSecurityGroupRuleTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkResultResponseTypeDef",
    "AssignIpv6AddressesRequestTypeDef",
    "AssignIpv6AddressesResultResponseTypeDef",
    "AssignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    "AssignPrivateIpAddressesRequestTypeDef",
    "AssignPrivateIpAddressesResultResponseTypeDef",
    "AssignedPrivateIpAddressTypeDef",
    "AssociateAddressRequestClassicAddressTypeDef",
    "AssociateAddressRequestTypeDef",
    "AssociateAddressRequestVpcAddressTypeDef",
    "AssociateAddressResultResponseTypeDef",
    "AssociateClientVpnTargetNetworkRequestTypeDef",
    "AssociateClientVpnTargetNetworkResultResponseTypeDef",
    "AssociateDhcpOptionsRequestDhcpOptionsTypeDef",
    "AssociateDhcpOptionsRequestTypeDef",
    "AssociateDhcpOptionsRequestVpcTypeDef",
    "AssociateEnclaveCertificateIamRoleRequestTypeDef",
    "AssociateEnclaveCertificateIamRoleResultResponseTypeDef",
    "AssociateIamInstanceProfileRequestTypeDef",
    "AssociateIamInstanceProfileResultResponseTypeDef",
    "AssociateRouteTableRequestRouteTableTypeDef",
    "AssociateRouteTableRequestTypeDef",
    "AssociateRouteTableResultResponseTypeDef",
    "AssociateSubnetCidrBlockRequestTypeDef",
    "AssociateSubnetCidrBlockResultResponseTypeDef",
    "AssociateTransitGatewayMulticastDomainRequestTypeDef",
    "AssociateTransitGatewayMulticastDomainResultResponseTypeDef",
    "AssociateTransitGatewayRouteTableRequestTypeDef",
    "AssociateTransitGatewayRouteTableResultResponseTypeDef",
    "AssociateTrunkInterfaceRequestTypeDef",
    "AssociateTrunkInterfaceResultResponseTypeDef",
    "AssociateVpcCidrBlockRequestTypeDef",
    "AssociateVpcCidrBlockResultResponseTypeDef",
    "AssociatedRoleTypeDef",
    "AssociatedTargetNetworkTypeDef",
    "AssociationStatusTypeDef",
    "AthenaIntegrationTypeDef",
    "AttachClassicLinkVpcRequestInstanceTypeDef",
    "AttachClassicLinkVpcRequestTypeDef",
    "AttachClassicLinkVpcRequestVpcTypeDef",
    "AttachClassicLinkVpcResultResponseTypeDef",
    "AttachInternetGatewayRequestInternetGatewayTypeDef",
    "AttachInternetGatewayRequestTypeDef",
    "AttachInternetGatewayRequestVpcTypeDef",
    "AttachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    "AttachNetworkInterfaceRequestTypeDef",
    "AttachNetworkInterfaceResultResponseTypeDef",
    "AttachVolumeRequestInstanceTypeDef",
    "AttachVolumeRequestTypeDef",
    "AttachVolumeRequestVolumeTypeDef",
    "AttachVpnGatewayRequestTypeDef",
    "AttachVpnGatewayResultResponseTypeDef",
    "AttributeBooleanValueTypeDef",
    "AttributeValueTypeDef",
    "AuthorizationRuleTypeDef",
    "AuthorizeClientVpnIngressRequestTypeDef",
    "AuthorizeClientVpnIngressResultResponseTypeDef",
    "AuthorizeSecurityGroupEgressRequestSecurityGroupTypeDef",
    "AuthorizeSecurityGroupEgressRequestTypeDef",
    "AuthorizeSecurityGroupIngressRequestSecurityGroupTypeDef",
    "AuthorizeSecurityGroupIngressRequestTypeDef",
    "AvailabilityZoneMessageTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableCapacityTypeDef",
    "BlobAttributeValueTypeDef",
    "BlockDeviceMappingTypeDef",
    "BundleInstanceRequestTypeDef",
    "BundleInstanceResultResponseTypeDef",
    "BundleTaskErrorTypeDef",
    "BundleTaskTypeDef",
    "ByoipCidrTypeDef",
    "CancelBundleTaskRequestTypeDef",
    "CancelBundleTaskResultResponseTypeDef",
    "CancelCapacityReservationRequestTypeDef",
    "CancelCapacityReservationResultResponseTypeDef",
    "CancelConversionRequestTypeDef",
    "CancelExportTaskRequestTypeDef",
    "CancelImportTaskRequestTypeDef",
    "CancelImportTaskResultResponseTypeDef",
    "CancelReservedInstancesListingRequestTypeDef",
    "CancelReservedInstancesListingResultResponseTypeDef",
    "CancelSpotFleetRequestsErrorItemTypeDef",
    "CancelSpotFleetRequestsErrorTypeDef",
    "CancelSpotFleetRequestsRequestTypeDef",
    "CancelSpotFleetRequestsResponseResponseTypeDef",
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    "CancelSpotInstanceRequestsRequestTypeDef",
    "CancelSpotInstanceRequestsResultResponseTypeDef",
    "CancelledSpotInstanceRequestTypeDef",
    "CapacityReservationGroupTypeDef",
    "CapacityReservationOptionsRequestTypeDef",
    "CapacityReservationOptionsTypeDef",
    "CapacityReservationSpecificationResponseTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CapacityReservationTargetResponseTypeDef",
    "CapacityReservationTargetTypeDef",
    "CapacityReservationTypeDef",
    "CarrierGatewayTypeDef",
    "CertificateAuthenticationRequestTypeDef",
    "CertificateAuthenticationTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CidrBlockTypeDef",
    "ClassicLinkDnsSupportTypeDef",
    "ClassicLinkInstanceTypeDef",
    "ClassicLoadBalancerTypeDef",
    "ClassicLoadBalancersConfigTypeDef",
    "ClientCertificateRevocationListStatusTypeDef",
    "ClientConnectOptionsTypeDef",
    "ClientConnectResponseOptionsTypeDef",
    "ClientDataTypeDef",
    "ClientVpnAuthenticationRequestTypeDef",
    "ClientVpnAuthenticationTypeDef",
    "ClientVpnAuthorizationRuleStatusTypeDef",
    "ClientVpnConnectionStatusTypeDef",
    "ClientVpnConnectionTypeDef",
    "ClientVpnEndpointAttributeStatusTypeDef",
    "ClientVpnEndpointStatusTypeDef",
    "ClientVpnEndpointTypeDef",
    "ClientVpnRouteStatusTypeDef",
    "ClientVpnRouteTypeDef",
    "CoipAddressUsageTypeDef",
    "CoipPoolTypeDef",
    "ConfirmProductInstanceRequestTypeDef",
    "ConfirmProductInstanceResultResponseTypeDef",
    "ConnectionLogOptionsTypeDef",
    "ConnectionLogResponseOptionsTypeDef",
    "ConnectionNotificationTypeDef",
    "ConversionTaskTypeDef",
    "CopyFpgaImageRequestTypeDef",
    "CopyFpgaImageResultResponseTypeDef",
    "CopyImageRequestTypeDef",
    "CopyImageResultResponseTypeDef",
    "CopySnapshotRequestSnapshotTypeDef",
    "CopySnapshotRequestTypeDef",
    "CopySnapshotResultResponseTypeDef",
    "CpuOptionsRequestTypeDef",
    "CpuOptionsTypeDef",
    "CreateCapacityReservationRequestTypeDef",
    "CreateCapacityReservationResultResponseTypeDef",
    "CreateCarrierGatewayRequestTypeDef",
    "CreateCarrierGatewayResultResponseTypeDef",
    "CreateClientVpnEndpointRequestTypeDef",
    "CreateClientVpnEndpointResultResponseTypeDef",
    "CreateClientVpnRouteRequestTypeDef",
    "CreateClientVpnRouteResultResponseTypeDef",
    "CreateCustomerGatewayRequestTypeDef",
    "CreateCustomerGatewayResultResponseTypeDef",
    "CreateDefaultSubnetRequestTypeDef",
    "CreateDefaultSubnetResultResponseTypeDef",
    "CreateDefaultVpcRequestTypeDef",
    "CreateDefaultVpcResultResponseTypeDef",
    "CreateDhcpOptionsRequestServiceResourceTypeDef",
    "CreateDhcpOptionsRequestTypeDef",
    "CreateDhcpOptionsResultResponseTypeDef",
    "CreateEgressOnlyInternetGatewayRequestTypeDef",
    "CreateEgressOnlyInternetGatewayResultResponseTypeDef",
    "CreateFleetErrorTypeDef",
    "CreateFleetInstanceTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResultResponseTypeDef",
    "CreateFlowLogsRequestTypeDef",
    "CreateFlowLogsResultResponseTypeDef",
    "CreateFpgaImageRequestTypeDef",
    "CreateFpgaImageResultResponseTypeDef",
    "CreateImageRequestInstanceTypeDef",
    "CreateImageRequestTypeDef",
    "CreateImageResultResponseTypeDef",
    "CreateInstanceExportTaskRequestTypeDef",
    "CreateInstanceExportTaskResultResponseTypeDef",
    "CreateInternetGatewayRequestServiceResourceTypeDef",
    "CreateInternetGatewayRequestTypeDef",
    "CreateInternetGatewayResultResponseTypeDef",
    "CreateKeyPairRequestServiceResourceTypeDef",
    "CreateKeyPairRequestTypeDef",
    "CreateLaunchTemplateRequestTypeDef",
    "CreateLaunchTemplateResultResponseTypeDef",
    "CreateLaunchTemplateVersionRequestTypeDef",
    "CreateLaunchTemplateVersionResultResponseTypeDef",
    "CreateLocalGatewayRouteRequestTypeDef",
    "CreateLocalGatewayRouteResultResponseTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationRequestTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationResultResponseTypeDef",
    "CreateManagedPrefixListRequestTypeDef",
    "CreateManagedPrefixListResultResponseTypeDef",
    "CreateNatGatewayRequestTypeDef",
    "CreateNatGatewayResultResponseTypeDef",
    "CreateNetworkAclEntryRequestNetworkAclTypeDef",
    "CreateNetworkAclEntryRequestTypeDef",
    "CreateNetworkAclRequestServiceResourceTypeDef",
    "CreateNetworkAclRequestTypeDef",
    "CreateNetworkAclRequestVpcTypeDef",
    "CreateNetworkAclResultResponseTypeDef",
    "CreateNetworkInsightsPathRequestTypeDef",
    "CreateNetworkInsightsPathResultResponseTypeDef",
    "CreateNetworkInterfacePermissionRequestTypeDef",
    "CreateNetworkInterfacePermissionResultResponseTypeDef",
    "CreateNetworkInterfaceRequestServiceResourceTypeDef",
    "CreateNetworkInterfaceRequestSubnetTypeDef",
    "CreateNetworkInterfaceRequestTypeDef",
    "CreateNetworkInterfaceResultResponseTypeDef",
    "CreatePlacementGroupRequestServiceResourceTypeDef",
    "CreatePlacementGroupRequestTypeDef",
    "CreatePlacementGroupResultResponseTypeDef",
    "CreateReplaceRootVolumeTaskRequestTypeDef",
    "CreateReplaceRootVolumeTaskResultResponseTypeDef",
    "CreateReservedInstancesListingRequestTypeDef",
    "CreateReservedInstancesListingResultResponseTypeDef",
    "CreateRestoreImageTaskRequestTypeDef",
    "CreateRestoreImageTaskResultResponseTypeDef",
    "CreateRouteRequestRouteTableTypeDef",
    "CreateRouteRequestTypeDef",
    "CreateRouteResultResponseTypeDef",
    "CreateRouteTableRequestServiceResourceTypeDef",
    "CreateRouteTableRequestTypeDef",
    "CreateRouteTableRequestVpcTypeDef",
    "CreateRouteTableResultResponseTypeDef",
    "CreateSecurityGroupRequestServiceResourceTypeDef",
    "CreateSecurityGroupRequestTypeDef",
    "CreateSecurityGroupRequestVpcTypeDef",
    "CreateSecurityGroupResultResponseTypeDef",
    "CreateSnapshotRequestServiceResourceTypeDef",
    "CreateSnapshotRequestTypeDef",
    "CreateSnapshotRequestVolumeTypeDef",
    "CreateSnapshotsRequestTypeDef",
    "CreateSnapshotsResultResponseTypeDef",
    "CreateSpotDatafeedSubscriptionRequestTypeDef",
    "CreateSpotDatafeedSubscriptionResultResponseTypeDef",
    "CreateStoreImageTaskRequestTypeDef",
    "CreateStoreImageTaskResultResponseTypeDef",
    "CreateSubnetRequestServiceResourceTypeDef",
    "CreateSubnetRequestTypeDef",
    "CreateSubnetRequestVpcTypeDef",
    "CreateSubnetResultResponseTypeDef",
    "CreateTagsRequestDhcpOptionsTypeDef",
    "CreateTagsRequestImageTypeDef",
    "CreateTagsRequestInstanceTypeDef",
    "CreateTagsRequestInternetGatewayTypeDef",
    "CreateTagsRequestNetworkAclTypeDef",
    "CreateTagsRequestNetworkInterfaceTypeDef",
    "CreateTagsRequestRouteTableTypeDef",
    "CreateTagsRequestSecurityGroupTypeDef",
    "CreateTagsRequestServiceResourceTypeDef",
    "CreateTagsRequestSnapshotTypeDef",
    "CreateTagsRequestSubnetTypeDef",
    "CreateTagsRequestTypeDef",
    "CreateTagsRequestVolumeTypeDef",
    "CreateTagsRequestVpcTypeDef",
    "CreateTrafficMirrorFilterRequestTypeDef",
    "CreateTrafficMirrorFilterResultResponseTypeDef",
    "CreateTrafficMirrorFilterRuleRequestTypeDef",
    "CreateTrafficMirrorFilterRuleResultResponseTypeDef",
    "CreateTrafficMirrorSessionRequestTypeDef",
    "CreateTrafficMirrorSessionResultResponseTypeDef",
    "CreateTrafficMirrorTargetRequestTypeDef",
    "CreateTrafficMirrorTargetResultResponseTypeDef",
    "CreateTransitGatewayConnectPeerRequestTypeDef",
    "CreateTransitGatewayConnectPeerResultResponseTypeDef",
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    "CreateTransitGatewayConnectRequestTypeDef",
    "CreateTransitGatewayConnectResultResponseTypeDef",
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    "CreateTransitGatewayMulticastDomainRequestTypeDef",
    "CreateTransitGatewayMulticastDomainResultResponseTypeDef",
    "CreateTransitGatewayPeeringAttachmentRequestTypeDef",
    "CreateTransitGatewayPeeringAttachmentResultResponseTypeDef",
    "CreateTransitGatewayPrefixListReferenceRequestTypeDef",
    "CreateTransitGatewayPrefixListReferenceResultResponseTypeDef",
    "CreateTransitGatewayRequestTypeDef",
    "CreateTransitGatewayResultResponseTypeDef",
    "CreateTransitGatewayRouteRequestTypeDef",
    "CreateTransitGatewayRouteResultResponseTypeDef",
    "CreateTransitGatewayRouteTableRequestTypeDef",
    "CreateTransitGatewayRouteTableResultResponseTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestTypeDef",
    "CreateTransitGatewayVpcAttachmentResultResponseTypeDef",
    "CreateVolumePermissionModificationsTypeDef",
    "CreateVolumePermissionTypeDef",
    "CreateVolumeRequestServiceResourceTypeDef",
    "CreateVolumeRequestTypeDef",
    "CreateVpcEndpointConnectionNotificationRequestTypeDef",
    "CreateVpcEndpointConnectionNotificationResultResponseTypeDef",
    "CreateVpcEndpointRequestTypeDef",
    "CreateVpcEndpointResultResponseTypeDef",
    "CreateVpcEndpointServiceConfigurationRequestTypeDef",
    "CreateVpcEndpointServiceConfigurationResultResponseTypeDef",
    "CreateVpcPeeringConnectionRequestServiceResourceTypeDef",
    "CreateVpcPeeringConnectionRequestTypeDef",
    "CreateVpcPeeringConnectionRequestVpcTypeDef",
    "CreateVpcPeeringConnectionResultResponseTypeDef",
    "CreateVpcRequestServiceResourceTypeDef",
    "CreateVpcRequestTypeDef",
    "CreateVpcResultResponseTypeDef",
    "CreateVpnConnectionRequestTypeDef",
    "CreateVpnConnectionResultResponseTypeDef",
    "CreateVpnConnectionRouteRequestTypeDef",
    "CreateVpnGatewayRequestTypeDef",
    "CreateVpnGatewayResultResponseTypeDef",
    "CreditSpecificationRequestTypeDef",
    "CreditSpecificationTypeDef",
    "CustomerGatewayTypeDef",
    "DeleteCarrierGatewayRequestTypeDef",
    "DeleteCarrierGatewayResultResponseTypeDef",
    "DeleteClientVpnEndpointRequestTypeDef",
    "DeleteClientVpnEndpointResultResponseTypeDef",
    "DeleteClientVpnRouteRequestTypeDef",
    "DeleteClientVpnRouteResultResponseTypeDef",
    "DeleteCustomerGatewayRequestTypeDef",
    "DeleteDhcpOptionsRequestDhcpOptionsTypeDef",
    "DeleteDhcpOptionsRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayResultResponseTypeDef",
    "DeleteFleetErrorItemTypeDef",
    "DeleteFleetErrorTypeDef",
    "DeleteFleetSuccessItemTypeDef",
    "DeleteFleetsRequestTypeDef",
    "DeleteFleetsResultResponseTypeDef",
    "DeleteFlowLogsRequestTypeDef",
    "DeleteFlowLogsResultResponseTypeDef",
    "DeleteFpgaImageRequestTypeDef",
    "DeleteFpgaImageResultResponseTypeDef",
    "DeleteInternetGatewayRequestInternetGatewayTypeDef",
    "DeleteInternetGatewayRequestTypeDef",
    "DeleteKeyPairRequestKeyPairInfoTypeDef",
    "DeleteKeyPairRequestKeyPairTypeDef",
    "DeleteKeyPairRequestTypeDef",
    "DeleteLaunchTemplateRequestTypeDef",
    "DeleteLaunchTemplateResultResponseTypeDef",
    "DeleteLaunchTemplateVersionsRequestTypeDef",
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    "DeleteLaunchTemplateVersionsResultResponseTypeDef",
    "DeleteLocalGatewayRouteRequestTypeDef",
    "DeleteLocalGatewayRouteResultResponseTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationResultResponseTypeDef",
    "DeleteManagedPrefixListRequestTypeDef",
    "DeleteManagedPrefixListResultResponseTypeDef",
    "DeleteNatGatewayRequestTypeDef",
    "DeleteNatGatewayResultResponseTypeDef",
    "DeleteNetworkAclEntryRequestNetworkAclTypeDef",
    "DeleteNetworkAclEntryRequestTypeDef",
    "DeleteNetworkAclRequestNetworkAclTypeDef",
    "DeleteNetworkAclRequestTypeDef",
    "DeleteNetworkInsightsAnalysisRequestTypeDef",
    "DeleteNetworkInsightsAnalysisResultResponseTypeDef",
    "DeleteNetworkInsightsPathRequestTypeDef",
    "DeleteNetworkInsightsPathResultResponseTypeDef",
    "DeleteNetworkInterfacePermissionRequestTypeDef",
    "DeleteNetworkInterfacePermissionResultResponseTypeDef",
    "DeleteNetworkInterfaceRequestNetworkInterfaceTypeDef",
    "DeleteNetworkInterfaceRequestTypeDef",
    "DeletePlacementGroupRequestPlacementGroupTypeDef",
    "DeletePlacementGroupRequestTypeDef",
    "DeleteQueuedReservedInstancesErrorTypeDef",
    "DeleteQueuedReservedInstancesRequestTypeDef",
    "DeleteQueuedReservedInstancesResultResponseTypeDef",
    "DeleteRouteRequestRouteTypeDef",
    "DeleteRouteRequestTypeDef",
    "DeleteRouteTableRequestRouteTableTypeDef",
    "DeleteRouteTableRequestTypeDef",
    "DeleteSecurityGroupRequestSecurityGroupTypeDef",
    "DeleteSecurityGroupRequestTypeDef",
    "DeleteSnapshotRequestSnapshotTypeDef",
    "DeleteSnapshotRequestTypeDef",
    "DeleteSpotDatafeedSubscriptionRequestTypeDef",
    "DeleteSubnetRequestSubnetTypeDef",
    "DeleteSubnetRequestTypeDef",
    "DeleteTagsRequestTagTypeDef",
    "DeleteTagsRequestTypeDef",
    "DeleteTrafficMirrorFilterRequestTypeDef",
    "DeleteTrafficMirrorFilterResultResponseTypeDef",
    "DeleteTrafficMirrorFilterRuleRequestTypeDef",
    "DeleteTrafficMirrorFilterRuleResultResponseTypeDef",
    "DeleteTrafficMirrorSessionRequestTypeDef",
    "DeleteTrafficMirrorSessionResultResponseTypeDef",
    "DeleteTrafficMirrorTargetRequestTypeDef",
    "DeleteTrafficMirrorTargetResultResponseTypeDef",
    "DeleteTransitGatewayConnectPeerRequestTypeDef",
    "DeleteTransitGatewayConnectPeerResultResponseTypeDef",
    "DeleteTransitGatewayConnectRequestTypeDef",
    "DeleteTransitGatewayConnectResultResponseTypeDef",
    "DeleteTransitGatewayMulticastDomainRequestTypeDef",
    "DeleteTransitGatewayMulticastDomainResultResponseTypeDef",
    "DeleteTransitGatewayPeeringAttachmentRequestTypeDef",
    "DeleteTransitGatewayPeeringAttachmentResultResponseTypeDef",
    "DeleteTransitGatewayPrefixListReferenceRequestTypeDef",
    "DeleteTransitGatewayPrefixListReferenceResultResponseTypeDef",
    "DeleteTransitGatewayRequestTypeDef",
    "DeleteTransitGatewayResultResponseTypeDef",
    "DeleteTransitGatewayRouteRequestTypeDef",
    "DeleteTransitGatewayRouteResultResponseTypeDef",
    "DeleteTransitGatewayRouteTableRequestTypeDef",
    "DeleteTransitGatewayRouteTableResultResponseTypeDef",
    "DeleteTransitGatewayVpcAttachmentRequestTypeDef",
    "DeleteTransitGatewayVpcAttachmentResultResponseTypeDef",
    "DeleteVolumeRequestTypeDef",
    "DeleteVolumeRequestVolumeTypeDef",
    "DeleteVpcEndpointConnectionNotificationsRequestTypeDef",
    "DeleteVpcEndpointConnectionNotificationsResultResponseTypeDef",
    "DeleteVpcEndpointServiceConfigurationsRequestTypeDef",
    "DeleteVpcEndpointServiceConfigurationsResultResponseTypeDef",
    "DeleteVpcEndpointsRequestTypeDef",
    "DeleteVpcEndpointsResultResponseTypeDef",
    "DeleteVpcPeeringConnectionRequestTypeDef",
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    "DeleteVpcPeeringConnectionResultResponseTypeDef",
    "DeleteVpcRequestTypeDef",
    "DeleteVpcRequestVpcTypeDef",
    "DeleteVpnConnectionRequestTypeDef",
    "DeleteVpnConnectionRouteRequestTypeDef",
    "DeleteVpnGatewayRequestTypeDef",
    "DeprovisionByoipCidrRequestTypeDef",
    "DeprovisionByoipCidrResultResponseTypeDef",
    "DeregisterImageRequestImageTypeDef",
    "DeregisterImageRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesResultResponseTypeDef",
    "DeregisterInstanceTagAttributeRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersResultResponseTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesResultResponseTypeDef",
    "DescribeAccountAttributesRequestTypeDef",
    "DescribeAccountAttributesResultResponseTypeDef",
    "DescribeAddressesAttributeRequestTypeDef",
    "DescribeAddressesAttributeResultResponseTypeDef",
    "DescribeAddressesRequestTypeDef",
    "DescribeAddressesResultResponseTypeDef",
    "DescribeAggregateIdFormatRequestTypeDef",
    "DescribeAggregateIdFormatResultResponseTypeDef",
    "DescribeAvailabilityZonesRequestTypeDef",
    "DescribeAvailabilityZonesResultResponseTypeDef",
    "DescribeBundleTasksRequestTypeDef",
    "DescribeBundleTasksResultResponseTypeDef",
    "DescribeByoipCidrsRequestTypeDef",
    "DescribeByoipCidrsResultResponseTypeDef",
    "DescribeCapacityReservationsRequestTypeDef",
    "DescribeCapacityReservationsResultResponseTypeDef",
    "DescribeCarrierGatewaysRequestTypeDef",
    "DescribeCarrierGatewaysResultResponseTypeDef",
    "DescribeClassicLinkInstancesRequestTypeDef",
    "DescribeClassicLinkInstancesResultResponseTypeDef",
    "DescribeClientVpnAuthorizationRulesRequestTypeDef",
    "DescribeClientVpnAuthorizationRulesResultResponseTypeDef",
    "DescribeClientVpnConnectionsRequestTypeDef",
    "DescribeClientVpnConnectionsResultResponseTypeDef",
    "DescribeClientVpnEndpointsRequestTypeDef",
    "DescribeClientVpnEndpointsResultResponseTypeDef",
    "DescribeClientVpnRoutesRequestTypeDef",
    "DescribeClientVpnRoutesResultResponseTypeDef",
    "DescribeClientVpnTargetNetworksRequestTypeDef",
    "DescribeClientVpnTargetNetworksResultResponseTypeDef",
    "DescribeCoipPoolsRequestTypeDef",
    "DescribeCoipPoolsResultResponseTypeDef",
    "DescribeConversionTasksRequestTypeDef",
    "DescribeConversionTasksResultResponseTypeDef",
    "DescribeCustomerGatewaysRequestTypeDef",
    "DescribeCustomerGatewaysResultResponseTypeDef",
    "DescribeDhcpOptionsRequestTypeDef",
    "DescribeDhcpOptionsResultResponseTypeDef",
    "DescribeEgressOnlyInternetGatewaysRequestTypeDef",
    "DescribeEgressOnlyInternetGatewaysResultResponseTypeDef",
    "DescribeElasticGpusRequestTypeDef",
    "DescribeElasticGpusResultResponseTypeDef",
    "DescribeExportImageTasksRequestTypeDef",
    "DescribeExportImageTasksResultResponseTypeDef",
    "DescribeExportTasksRequestTypeDef",
    "DescribeExportTasksResultResponseTypeDef",
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    "DescribeFastSnapshotRestoresRequestTypeDef",
    "DescribeFastSnapshotRestoresResultResponseTypeDef",
    "DescribeFleetErrorTypeDef",
    "DescribeFleetHistoryRequestTypeDef",
    "DescribeFleetHistoryResultResponseTypeDef",
    "DescribeFleetInstancesRequestTypeDef",
    "DescribeFleetInstancesResultResponseTypeDef",
    "DescribeFleetsInstancesTypeDef",
    "DescribeFleetsRequestTypeDef",
    "DescribeFleetsResultResponseTypeDef",
    "DescribeFlowLogsRequestTypeDef",
    "DescribeFlowLogsResultResponseTypeDef",
    "DescribeFpgaImageAttributeRequestTypeDef",
    "DescribeFpgaImageAttributeResultResponseTypeDef",
    "DescribeFpgaImagesRequestTypeDef",
    "DescribeFpgaImagesResultResponseTypeDef",
    "DescribeHostReservationOfferingsRequestTypeDef",
    "DescribeHostReservationOfferingsResultResponseTypeDef",
    "DescribeHostReservationsRequestTypeDef",
    "DescribeHostReservationsResultResponseTypeDef",
    "DescribeHostsRequestTypeDef",
    "DescribeHostsResultResponseTypeDef",
    "DescribeIamInstanceProfileAssociationsRequestTypeDef",
    "DescribeIamInstanceProfileAssociationsResultResponseTypeDef",
    "DescribeIdFormatRequestTypeDef",
    "DescribeIdFormatResultResponseTypeDef",
    "DescribeIdentityIdFormatRequestTypeDef",
    "DescribeIdentityIdFormatResultResponseTypeDef",
    "DescribeImageAttributeRequestImageTypeDef",
    "DescribeImageAttributeRequestTypeDef",
    "DescribeImagesRequestTypeDef",
    "DescribeImagesResultResponseTypeDef",
    "DescribeImportImageTasksRequestTypeDef",
    "DescribeImportImageTasksResultResponseTypeDef",
    "DescribeImportSnapshotTasksRequestTypeDef",
    "DescribeImportSnapshotTasksResultResponseTypeDef",
    "DescribeInstanceAttributeRequestInstanceTypeDef",
    "DescribeInstanceAttributeRequestTypeDef",
    "DescribeInstanceCreditSpecificationsRequestTypeDef",
    "DescribeInstanceCreditSpecificationsResultResponseTypeDef",
    "DescribeInstanceEventNotificationAttributesRequestTypeDef",
    "DescribeInstanceEventNotificationAttributesResultResponseTypeDef",
    "DescribeInstanceStatusRequestTypeDef",
    "DescribeInstanceStatusResultResponseTypeDef",
    "DescribeInstanceTypeOfferingsRequestTypeDef",
    "DescribeInstanceTypeOfferingsResultResponseTypeDef",
    "DescribeInstanceTypesRequestTypeDef",
    "DescribeInstanceTypesResultResponseTypeDef",
    "DescribeInstancesRequestTypeDef",
    "DescribeInstancesResultResponseTypeDef",
    "DescribeInternetGatewaysRequestTypeDef",
    "DescribeInternetGatewaysResultResponseTypeDef",
    "DescribeIpv6PoolsRequestTypeDef",
    "DescribeIpv6PoolsResultResponseTypeDef",
    "DescribeKeyPairsRequestTypeDef",
    "DescribeKeyPairsResultResponseTypeDef",
    "DescribeLaunchTemplateVersionsRequestTypeDef",
    "DescribeLaunchTemplateVersionsResultResponseTypeDef",
    "DescribeLaunchTemplatesRequestTypeDef",
    "DescribeLaunchTemplatesResultResponseTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultResponseTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsResultResponseTypeDef",
    "DescribeLocalGatewayRouteTablesRequestTypeDef",
    "DescribeLocalGatewayRouteTablesResultResponseTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsResultResponseTypeDef",
    "DescribeLocalGatewayVirtualInterfacesRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfacesResultResponseTypeDef",
    "DescribeLocalGatewaysRequestTypeDef",
    "DescribeLocalGatewaysResultResponseTypeDef",
    "DescribeManagedPrefixListsRequestTypeDef",
    "DescribeManagedPrefixListsResultResponseTypeDef",
    "DescribeMovingAddressesRequestTypeDef",
    "DescribeMovingAddressesResultResponseTypeDef",
    "DescribeNatGatewaysRequestTypeDef",
    "DescribeNatGatewaysResultResponseTypeDef",
    "DescribeNetworkAclsRequestTypeDef",
    "DescribeNetworkAclsResultResponseTypeDef",
    "DescribeNetworkInsightsAnalysesRequestTypeDef",
    "DescribeNetworkInsightsAnalysesResultResponseTypeDef",
    "DescribeNetworkInsightsPathsRequestTypeDef",
    "DescribeNetworkInsightsPathsResultResponseTypeDef",
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    "DescribeNetworkInterfaceAttributeRequestTypeDef",
    "DescribeNetworkInterfaceAttributeResultResponseTypeDef",
    "DescribeNetworkInterfacePermissionsRequestTypeDef",
    "DescribeNetworkInterfacePermissionsResultResponseTypeDef",
    "DescribeNetworkInterfacesRequestTypeDef",
    "DescribeNetworkInterfacesResultResponseTypeDef",
    "DescribePlacementGroupsRequestTypeDef",
    "DescribePlacementGroupsResultResponseTypeDef",
    "DescribePrefixListsRequestTypeDef",
    "DescribePrefixListsResultResponseTypeDef",
    "DescribePrincipalIdFormatRequestTypeDef",
    "DescribePrincipalIdFormatResultResponseTypeDef",
    "DescribePublicIpv4PoolsRequestTypeDef",
    "DescribePublicIpv4PoolsResultResponseTypeDef",
    "DescribeRegionsRequestTypeDef",
    "DescribeRegionsResultResponseTypeDef",
    "DescribeReplaceRootVolumeTasksRequestTypeDef",
    "DescribeReplaceRootVolumeTasksResultResponseTypeDef",
    "DescribeReservedInstancesListingsRequestTypeDef",
    "DescribeReservedInstancesListingsResultResponseTypeDef",
    "DescribeReservedInstancesModificationsRequestTypeDef",
    "DescribeReservedInstancesModificationsResultResponseTypeDef",
    "DescribeReservedInstancesOfferingsRequestTypeDef",
    "DescribeReservedInstancesOfferingsResultResponseTypeDef",
    "DescribeReservedInstancesRequestTypeDef",
    "DescribeReservedInstancesResultResponseTypeDef",
    "DescribeRouteTablesRequestTypeDef",
    "DescribeRouteTablesResultResponseTypeDef",
    "DescribeScheduledInstanceAvailabilityRequestTypeDef",
    "DescribeScheduledInstanceAvailabilityResultResponseTypeDef",
    "DescribeScheduledInstancesRequestTypeDef",
    "DescribeScheduledInstancesResultResponseTypeDef",
    "DescribeSecurityGroupReferencesRequestTypeDef",
    "DescribeSecurityGroupReferencesResultResponseTypeDef",
    "DescribeSecurityGroupsRequestTypeDef",
    "DescribeSecurityGroupsResultResponseTypeDef",
    "DescribeSnapshotAttributeRequestSnapshotTypeDef",
    "DescribeSnapshotAttributeRequestTypeDef",
    "DescribeSnapshotAttributeResultResponseTypeDef",
    "DescribeSnapshotsRequestTypeDef",
    "DescribeSnapshotsResultResponseTypeDef",
    "DescribeSpotDatafeedSubscriptionRequestTypeDef",
    "DescribeSpotDatafeedSubscriptionResultResponseTypeDef",
    "DescribeSpotFleetInstancesRequestTypeDef",
    "DescribeSpotFleetInstancesResponseResponseTypeDef",
    "DescribeSpotFleetRequestHistoryRequestTypeDef",
    "DescribeSpotFleetRequestHistoryResponseResponseTypeDef",
    "DescribeSpotFleetRequestsRequestTypeDef",
    "DescribeSpotFleetRequestsResponseResponseTypeDef",
    "DescribeSpotInstanceRequestsRequestTypeDef",
    "DescribeSpotInstanceRequestsResultResponseTypeDef",
    "DescribeSpotPriceHistoryRequestTypeDef",
    "DescribeSpotPriceHistoryResultResponseTypeDef",
    "DescribeStaleSecurityGroupsRequestTypeDef",
    "DescribeStaleSecurityGroupsResultResponseTypeDef",
    "DescribeStoreImageTasksRequestTypeDef",
    "DescribeStoreImageTasksResultResponseTypeDef",
    "DescribeSubnetsRequestTypeDef",
    "DescribeSubnetsResultResponseTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResultResponseTypeDef",
    "DescribeTrafficMirrorFiltersRequestTypeDef",
    "DescribeTrafficMirrorFiltersResultResponseTypeDef",
    "DescribeTrafficMirrorSessionsRequestTypeDef",
    "DescribeTrafficMirrorSessionsResultResponseTypeDef",
    "DescribeTrafficMirrorTargetsRequestTypeDef",
    "DescribeTrafficMirrorTargetsResultResponseTypeDef",
    "DescribeTransitGatewayAttachmentsRequestTypeDef",
    "DescribeTransitGatewayAttachmentsResultResponseTypeDef",
    "DescribeTransitGatewayConnectPeersRequestTypeDef",
    "DescribeTransitGatewayConnectPeersResultResponseTypeDef",
    "DescribeTransitGatewayConnectsRequestTypeDef",
    "DescribeTransitGatewayConnectsResultResponseTypeDef",
    "DescribeTransitGatewayMulticastDomainsRequestTypeDef",
    "DescribeTransitGatewayMulticastDomainsResultResponseTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsRequestTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsResultResponseTypeDef",
    "DescribeTransitGatewayRouteTablesRequestTypeDef",
    "DescribeTransitGatewayRouteTablesResultResponseTypeDef",
    "DescribeTransitGatewayVpcAttachmentsRequestTypeDef",
    "DescribeTransitGatewayVpcAttachmentsResultResponseTypeDef",
    "DescribeTransitGatewaysRequestTypeDef",
    "DescribeTransitGatewaysResultResponseTypeDef",
    "DescribeTrunkInterfaceAssociationsRequestTypeDef",
    "DescribeTrunkInterfaceAssociationsResultResponseTypeDef",
    "DescribeVolumeAttributeRequestTypeDef",
    "DescribeVolumeAttributeRequestVolumeTypeDef",
    "DescribeVolumeAttributeResultResponseTypeDef",
    "DescribeVolumeStatusRequestTypeDef",
    "DescribeVolumeStatusRequestVolumeTypeDef",
    "DescribeVolumeStatusResultResponseTypeDef",
    "DescribeVolumesModificationsRequestTypeDef",
    "DescribeVolumesModificationsResultResponseTypeDef",
    "DescribeVolumesRequestTypeDef",
    "DescribeVolumesResultResponseTypeDef",
    "DescribeVpcAttributeRequestTypeDef",
    "DescribeVpcAttributeRequestVpcTypeDef",
    "DescribeVpcAttributeResultResponseTypeDef",
    "DescribeVpcClassicLinkDnsSupportRequestTypeDef",
    "DescribeVpcClassicLinkDnsSupportResultResponseTypeDef",
    "DescribeVpcClassicLinkRequestTypeDef",
    "DescribeVpcClassicLinkResultResponseTypeDef",
    "DescribeVpcEndpointConnectionNotificationsRequestTypeDef",
    "DescribeVpcEndpointConnectionNotificationsResultResponseTypeDef",
    "DescribeVpcEndpointConnectionsRequestTypeDef",
    "DescribeVpcEndpointConnectionsResultResponseTypeDef",
    "DescribeVpcEndpointServiceConfigurationsRequestTypeDef",
    "DescribeVpcEndpointServiceConfigurationsResultResponseTypeDef",
    "DescribeVpcEndpointServicePermissionsRequestTypeDef",
    "DescribeVpcEndpointServicePermissionsResultResponseTypeDef",
    "DescribeVpcEndpointServicesRequestTypeDef",
    "DescribeVpcEndpointServicesResultResponseTypeDef",
    "DescribeVpcEndpointsRequestTypeDef",
    "DescribeVpcEndpointsResultResponseTypeDef",
    "DescribeVpcPeeringConnectionsRequestTypeDef",
    "DescribeVpcPeeringConnectionsResultResponseTypeDef",
    "DescribeVpcsRequestTypeDef",
    "DescribeVpcsResultResponseTypeDef",
    "DescribeVpnConnectionsRequestTypeDef",
    "DescribeVpnConnectionsResultResponseTypeDef",
    "DescribeVpnGatewaysRequestTypeDef",
    "DescribeVpnGatewaysResultResponseTypeDef",
    "DetachClassicLinkVpcRequestInstanceTypeDef",
    "DetachClassicLinkVpcRequestTypeDef",
    "DetachClassicLinkVpcRequestVpcTypeDef",
    "DetachClassicLinkVpcResultResponseTypeDef",
    "DetachInternetGatewayRequestInternetGatewayTypeDef",
    "DetachInternetGatewayRequestTypeDef",
    "DetachInternetGatewayRequestVpcTypeDef",
    "DetachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    "DetachNetworkInterfaceRequestTypeDef",
    "DetachVolumeRequestInstanceTypeDef",
    "DetachVolumeRequestTypeDef",
    "DetachVolumeRequestVolumeTypeDef",
    "DetachVpnGatewayRequestTypeDef",
    "DhcpConfigurationTypeDef",
    "DhcpOptionsTypeDef",
    "DirectoryServiceAuthenticationRequestTypeDef",
    "DirectoryServiceAuthenticationTypeDef",
    "DisableEbsEncryptionByDefaultRequestTypeDef",
    "DisableEbsEncryptionByDefaultResultResponseTypeDef",
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    "DisableFastSnapshotRestoresRequestTypeDef",
    "DisableFastSnapshotRestoresResultResponseTypeDef",
    "DisableImageDeprecationRequestTypeDef",
    "DisableImageDeprecationResultResponseTypeDef",
    "DisableSerialConsoleAccessRequestTypeDef",
    "DisableSerialConsoleAccessResultResponseTypeDef",
    "DisableTransitGatewayRouteTablePropagationRequestTypeDef",
    "DisableTransitGatewayRouteTablePropagationResultResponseTypeDef",
    "DisableVgwRoutePropagationRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportResultResponseTypeDef",
    "DisableVpcClassicLinkRequestTypeDef",
    "DisableVpcClassicLinkRequestVpcTypeDef",
    "DisableVpcClassicLinkResultResponseTypeDef",
    "DisassociateAddressRequestClassicAddressTypeDef",
    "DisassociateAddressRequestNetworkInterfaceAssociationTypeDef",
    "DisassociateAddressRequestTypeDef",
    "DisassociateClientVpnTargetNetworkRequestTypeDef",
    "DisassociateClientVpnTargetNetworkResultResponseTypeDef",
    "DisassociateEnclaveCertificateIamRoleRequestTypeDef",
    "DisassociateEnclaveCertificateIamRoleResultResponseTypeDef",
    "DisassociateIamInstanceProfileRequestTypeDef",
    "DisassociateIamInstanceProfileResultResponseTypeDef",
    "DisassociateRouteTableRequestRouteTableAssociationTypeDef",
    "DisassociateRouteTableRequestServiceResourceTypeDef",
    "DisassociateRouteTableRequestTypeDef",
    "DisassociateSubnetCidrBlockRequestTypeDef",
    "DisassociateSubnetCidrBlockResultResponseTypeDef",
    "DisassociateTransitGatewayMulticastDomainRequestTypeDef",
    "DisassociateTransitGatewayMulticastDomainResultResponseTypeDef",
    "DisassociateTransitGatewayRouteTableRequestTypeDef",
    "DisassociateTransitGatewayRouteTableResultResponseTypeDef",
    "DisassociateTrunkInterfaceRequestTypeDef",
    "DisassociateTrunkInterfaceResultResponseTypeDef",
    "DisassociateVpcCidrBlockRequestTypeDef",
    "DisassociateVpcCidrBlockResultResponseTypeDef",
    "DiskImageDescriptionTypeDef",
    "DiskImageDetailTypeDef",
    "DiskImageTypeDef",
    "DiskImageVolumeDescriptionTypeDef",
    "DiskInfoTypeDef",
    "DnsEntryTypeDef",
    "DnsServersOptionsModifyStructureTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsInfoTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "EbsOptimizedInfoTypeDef",
    "EfaInfoTypeDef",
    "EgressOnlyInternetGatewayTypeDef",
    "ElasticGpuAssociationTypeDef",
    "ElasticGpuHealthTypeDef",
    "ElasticGpuSpecificationResponseTypeDef",
    "ElasticGpuSpecificationTypeDef",
    "ElasticGpusTypeDef",
    "ElasticInferenceAcceleratorAssociationTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "EnableEbsEncryptionByDefaultRequestTypeDef",
    "EnableEbsEncryptionByDefaultResultResponseTypeDef",
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    "EnableFastSnapshotRestoresRequestTypeDef",
    "EnableFastSnapshotRestoresResultResponseTypeDef",
    "EnableImageDeprecationRequestTypeDef",
    "EnableImageDeprecationResultResponseTypeDef",
    "EnableSerialConsoleAccessRequestTypeDef",
    "EnableSerialConsoleAccessResultResponseTypeDef",
    "EnableTransitGatewayRouteTablePropagationRequestTypeDef",
    "EnableTransitGatewayRouteTablePropagationResultResponseTypeDef",
    "EnableVgwRoutePropagationRequestTypeDef",
    "EnableVolumeIORequestTypeDef",
    "EnableVolumeIORequestVolumeTypeDef",
    "EnableVpcClassicLinkDnsSupportRequestTypeDef",
    "EnableVpcClassicLinkDnsSupportResultResponseTypeDef",
    "EnableVpcClassicLinkRequestTypeDef",
    "EnableVpcClassicLinkRequestVpcTypeDef",
    "EnableVpcClassicLinkResultResponseTypeDef",
    "EnclaveOptionsRequestTypeDef",
    "EnclaveOptionsTypeDef",
    "EventInformationTypeDef",
    "ExplanationTypeDef",
    "ExportClientVpnClientCertificateRevocationListRequestTypeDef",
    "ExportClientVpnClientCertificateRevocationListResultResponseTypeDef",
    "ExportClientVpnClientConfigurationRequestTypeDef",
    "ExportClientVpnClientConfigurationResultResponseTypeDef",
    "ExportImageRequestTypeDef",
    "ExportImageResultResponseTypeDef",
    "ExportImageTaskTypeDef",
    "ExportTaskS3LocationRequestTypeDef",
    "ExportTaskS3LocationTypeDef",
    "ExportTaskTypeDef",
    "ExportToS3TaskSpecificationTypeDef",
    "ExportToS3TaskTypeDef",
    "ExportTransitGatewayRoutesRequestTypeDef",
    "ExportTransitGatewayRoutesResultResponseTypeDef",
    "FailedQueuedPurchaseDeletionTypeDef",
    "FederatedAuthenticationRequestTypeDef",
    "FederatedAuthenticationTypeDef",
    "FilterTypeDef",
    "FleetDataTypeDef",
    "FleetLaunchTemplateConfigRequestTypeDef",
    "FleetLaunchTemplateConfigTypeDef",
    "FleetLaunchTemplateOverridesRequestTypeDef",
    "FleetLaunchTemplateOverridesTypeDef",
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    "FleetLaunchTemplateSpecificationTypeDef",
    "FleetSpotCapacityRebalanceRequestTypeDef",
    "FleetSpotCapacityRebalanceTypeDef",
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    "FleetSpotMaintenanceStrategiesTypeDef",
    "FlowLogTypeDef",
    "FpgaDeviceInfoTypeDef",
    "FpgaDeviceMemoryInfoTypeDef",
    "FpgaImageAttributeTypeDef",
    "FpgaImageStateTypeDef",
    "FpgaImageTypeDef",
    "FpgaInfoTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesRequestTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesResultResponseTypeDef",
    "GetAssociatedIpv6PoolCidrsRequestTypeDef",
    "GetAssociatedIpv6PoolCidrsResultResponseTypeDef",
    "GetCapacityReservationUsageRequestTypeDef",
    "GetCapacityReservationUsageResultResponseTypeDef",
    "GetCoipPoolUsageRequestTypeDef",
    "GetCoipPoolUsageResultResponseTypeDef",
    "GetConsoleOutputRequestInstanceTypeDef",
    "GetConsoleOutputRequestTypeDef",
    "GetConsoleOutputResultResponseTypeDef",
    "GetConsoleScreenshotRequestTypeDef",
    "GetConsoleScreenshotResultResponseTypeDef",
    "GetDefaultCreditSpecificationRequestTypeDef",
    "GetDefaultCreditSpecificationResultResponseTypeDef",
    "GetEbsDefaultKmsKeyIdRequestTypeDef",
    "GetEbsDefaultKmsKeyIdResultResponseTypeDef",
    "GetEbsEncryptionByDefaultRequestTypeDef",
    "GetEbsEncryptionByDefaultResultResponseTypeDef",
    "GetFlowLogsIntegrationTemplateRequestTypeDef",
    "GetFlowLogsIntegrationTemplateResultResponseTypeDef",
    "GetGroupsForCapacityReservationRequestTypeDef",
    "GetGroupsForCapacityReservationResultResponseTypeDef",
    "GetHostReservationPurchasePreviewRequestTypeDef",
    "GetHostReservationPurchasePreviewResultResponseTypeDef",
    "GetLaunchTemplateDataRequestTypeDef",
    "GetLaunchTemplateDataResultResponseTypeDef",
    "GetManagedPrefixListAssociationsRequestTypeDef",
    "GetManagedPrefixListAssociationsResultResponseTypeDef",
    "GetManagedPrefixListEntriesRequestTypeDef",
    "GetManagedPrefixListEntriesResultResponseTypeDef",
    "GetPasswordDataRequestInstanceTypeDef",
    "GetPasswordDataRequestTypeDef",
    "GetPasswordDataResultResponseTypeDef",
    "GetReservedInstancesExchangeQuoteRequestTypeDef",
    "GetReservedInstancesExchangeQuoteResultResponseTypeDef",
    "GetSerialConsoleAccessStatusRequestTypeDef",
    "GetSerialConsoleAccessStatusResultResponseTypeDef",
    "GetTransitGatewayAttachmentPropagationsRequestTypeDef",
    "GetTransitGatewayAttachmentPropagationsResultResponseTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsRequestTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsResultResponseTypeDef",
    "GetTransitGatewayPrefixListReferencesRequestTypeDef",
    "GetTransitGatewayPrefixListReferencesResultResponseTypeDef",
    "GetTransitGatewayRouteTableAssociationsRequestTypeDef",
    "GetTransitGatewayRouteTableAssociationsResultResponseTypeDef",
    "GetTransitGatewayRouteTablePropagationsRequestTypeDef",
    "GetTransitGatewayRouteTablePropagationsResultResponseTypeDef",
    "GpuDeviceInfoTypeDef",
    "GpuDeviceMemoryInfoTypeDef",
    "GpuInfoTypeDef",
    "GroupIdentifierTypeDef",
    "HibernationOptionsRequestTypeDef",
    "HibernationOptionsTypeDef",
    "HistoryRecordEntryTypeDef",
    "HistoryRecordTypeDef",
    "HostInstanceTypeDef",
    "HostOfferingTypeDef",
    "HostPropertiesTypeDef",
    "HostReservationTypeDef",
    "HostTypeDef",
    "IKEVersionsListValueTypeDef",
    "IKEVersionsRequestListValueTypeDef",
    "IamInstanceProfileAssociationTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "IamInstanceProfileTypeDef",
    "IcmpTypeCodeTypeDef",
    "IdFormatTypeDef",
    "ImageAttributeResponseTypeDef",
    "ImageDiskContainerTypeDef",
    "ImageTypeDef",
    "ImportClientVpnClientCertificateRevocationListRequestTypeDef",
    "ImportClientVpnClientCertificateRevocationListResultResponseTypeDef",
    "ImportImageLicenseConfigurationRequestTypeDef",
    "ImportImageLicenseConfigurationResponseTypeDef",
    "ImportImageRequestTypeDef",
    "ImportImageResultResponseTypeDef",
    "ImportImageTaskTypeDef",
    "ImportInstanceLaunchSpecificationTypeDef",
    "ImportInstanceRequestTypeDef",
    "ImportInstanceResultResponseTypeDef",
    "ImportInstanceTaskDetailsTypeDef",
    "ImportInstanceVolumeDetailItemTypeDef",
    "ImportKeyPairRequestServiceResourceTypeDef",
    "ImportKeyPairRequestTypeDef",
    "ImportKeyPairResultResponseTypeDef",
    "ImportSnapshotRequestTypeDef",
    "ImportSnapshotResultResponseTypeDef",
    "ImportSnapshotTaskTypeDef",
    "ImportVolumeRequestTypeDef",
    "ImportVolumeResultResponseTypeDef",
    "ImportVolumeTaskDetailsTypeDef",
    "InferenceAcceleratorInfoTypeDef",
    "InferenceDeviceInfoTypeDef",
    "InstanceAttributeResponseTypeDef",
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceCapacityTypeDef",
    "InstanceCountTypeDef",
    "InstanceCreditSpecificationRequestTypeDef",
    "InstanceCreditSpecificationTypeDef",
    "InstanceDeleteTagsRequestTypeDef",
    "InstanceExportDetailsTypeDef",
    "InstanceFamilyCreditSpecificationTypeDef",
    "InstanceIpv6AddressRequestTypeDef",
    "InstanceIpv6AddressTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceMetadataOptionsResponseTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceNetworkInterfaceAssociationTypeDef",
    "InstanceNetworkInterfaceAttachmentTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "InstanceNetworkInterfaceTypeDef",
    "InstancePrivateIpAddressTypeDef",
    "InstanceSpecificationTypeDef",
    "InstanceStateChangeTypeDef",
    "InstanceStateTypeDef",
    "InstanceStatusDetailsTypeDef",
    "InstanceStatusEventTypeDef",
    "InstanceStatusSummaryTypeDef",
    "InstanceStatusTypeDef",
    "InstanceStorageInfoTypeDef",
    "InstanceTagNotificationAttributeTypeDef",
    "InstanceTypeDef",
    "InstanceTypeInfoTypeDef",
    "InstanceTypeOfferingTypeDef",
    "InstanceUsageTypeDef",
    "IntegrateServicesTypeDef",
    "InternetGatewayAttachmentTypeDef",
    "InternetGatewayTypeDef",
    "IpPermissionTypeDef",
    "IpRangeTypeDef",
    "Ipv6CidrAssociationTypeDef",
    "Ipv6CidrBlockTypeDef",
    "Ipv6PoolTypeDef",
    "Ipv6RangeTypeDef",
    "KeyPairInfoTypeDef",
    "KeyPairResponseTypeDef",
    "LastErrorTypeDef",
    "LaunchPermissionModificationsTypeDef",
    "LaunchPermissionTypeDef",
    "LaunchSpecificationTypeDef",
    "LaunchTemplateAndOverridesResponseTypeDef",
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    "LaunchTemplateBlockDeviceMappingTypeDef",
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    "LaunchTemplateConfigTypeDef",
    "LaunchTemplateCpuOptionsRequestTypeDef",
    "LaunchTemplateCpuOptionsTypeDef",
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    "LaunchTemplateEbsBlockDeviceTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    "LaunchTemplateEnclaveOptionsTypeDef",
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    "LaunchTemplateHibernationOptionsTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    "LaunchTemplateLicenseConfigurationTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplatePlacementRequestTypeDef",
    "LaunchTemplatePlacementTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    "LaunchTemplateSpotMarketOptionsTypeDef",
    "LaunchTemplateTagSpecificationRequestTypeDef",
    "LaunchTemplateTagSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LaunchTemplateVersionTypeDef",
    "LaunchTemplatesMonitoringRequestTypeDef",
    "LaunchTemplatesMonitoringTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "LicenseConfigurationTypeDef",
    "LoadBalancersConfigTypeDef",
    "LoadPermissionModificationsTypeDef",
    "LoadPermissionRequestTypeDef",
    "LoadPermissionTypeDef",
    "LocalGatewayRouteTableTypeDef",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    "LocalGatewayRouteTypeDef",
    "LocalGatewayTypeDef",
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    "LocalGatewayVirtualInterfaceTypeDef",
    "ManagedPrefixListTypeDef",
    "MemoryInfoTypeDef",
    "ModifyAddressAttributeRequestTypeDef",
    "ModifyAddressAttributeResultResponseTypeDef",
    "ModifyAvailabilityZoneGroupRequestTypeDef",
    "ModifyAvailabilityZoneGroupResultResponseTypeDef",
    "ModifyCapacityReservationRequestTypeDef",
    "ModifyCapacityReservationResultResponseTypeDef",
    "ModifyClientVpnEndpointRequestTypeDef",
    "ModifyClientVpnEndpointResultResponseTypeDef",
    "ModifyDefaultCreditSpecificationRequestTypeDef",
    "ModifyDefaultCreditSpecificationResultResponseTypeDef",
    "ModifyEbsDefaultKmsKeyIdRequestTypeDef",
    "ModifyEbsDefaultKmsKeyIdResultResponseTypeDef",
    "ModifyFleetRequestTypeDef",
    "ModifyFleetResultResponseTypeDef",
    "ModifyFpgaImageAttributeRequestTypeDef",
    "ModifyFpgaImageAttributeResultResponseTypeDef",
    "ModifyHostsRequestTypeDef",
    "ModifyHostsResultResponseTypeDef",
    "ModifyIdFormatRequestTypeDef",
    "ModifyIdentityIdFormatRequestTypeDef",
    "ModifyImageAttributeRequestImageTypeDef",
    "ModifyImageAttributeRequestTypeDef",
    "ModifyInstanceAttributeRequestInstanceTypeDef",
    "ModifyInstanceAttributeRequestTypeDef",
    "ModifyInstanceCapacityReservationAttributesRequestTypeDef",
    "ModifyInstanceCapacityReservationAttributesResultResponseTypeDef",
    "ModifyInstanceCreditSpecificationRequestTypeDef",
    "ModifyInstanceCreditSpecificationResultResponseTypeDef",
    "ModifyInstanceEventStartTimeRequestTypeDef",
    "ModifyInstanceEventStartTimeResultResponseTypeDef",
    "ModifyInstanceMetadataOptionsRequestTypeDef",
    "ModifyInstanceMetadataOptionsResultResponseTypeDef",
    "ModifyInstancePlacementRequestTypeDef",
    "ModifyInstancePlacementResultResponseTypeDef",
    "ModifyLaunchTemplateRequestTypeDef",
    "ModifyLaunchTemplateResultResponseTypeDef",
    "ModifyManagedPrefixListRequestTypeDef",
    "ModifyManagedPrefixListResultResponseTypeDef",
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    "ModifyNetworkInterfaceAttributeRequestTypeDef",
    "ModifyReservedInstancesRequestTypeDef",
    "ModifyReservedInstancesResultResponseTypeDef",
    "ModifySnapshotAttributeRequestSnapshotTypeDef",
    "ModifySnapshotAttributeRequestTypeDef",
    "ModifySpotFleetRequestRequestTypeDef",
    "ModifySpotFleetRequestResponseResponseTypeDef",
    "ModifySubnetAttributeRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesResultResponseTypeDef",
    "ModifyTrafficMirrorFilterRuleRequestTypeDef",
    "ModifyTrafficMirrorFilterRuleResultResponseTypeDef",
    "ModifyTrafficMirrorSessionRequestTypeDef",
    "ModifyTrafficMirrorSessionResultResponseTypeDef",
    "ModifyTransitGatewayOptionsTypeDef",
    "ModifyTransitGatewayPrefixListReferenceRequestTypeDef",
    "ModifyTransitGatewayPrefixListReferenceResultResponseTypeDef",
    "ModifyTransitGatewayRequestTypeDef",
    "ModifyTransitGatewayResultResponseTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestTypeDef",
    "ModifyTransitGatewayVpcAttachmentResultResponseTypeDef",
    "ModifyVolumeAttributeRequestTypeDef",
    "ModifyVolumeAttributeRequestVolumeTypeDef",
    "ModifyVolumeRequestTypeDef",
    "ModifyVolumeResultResponseTypeDef",
    "ModifyVpcAttributeRequestTypeDef",
    "ModifyVpcAttributeRequestVpcTypeDef",
    "ModifyVpcEndpointConnectionNotificationRequestTypeDef",
    "ModifyVpcEndpointConnectionNotificationResultResponseTypeDef",
    "ModifyVpcEndpointRequestTypeDef",
    "ModifyVpcEndpointResultResponseTypeDef",
    "ModifyVpcEndpointServiceConfigurationRequestTypeDef",
    "ModifyVpcEndpointServiceConfigurationResultResponseTypeDef",
    "ModifyVpcEndpointServicePermissionsRequestTypeDef",
    "ModifyVpcEndpointServicePermissionsResultResponseTypeDef",
    "ModifyVpcPeeringConnectionOptionsRequestTypeDef",
    "ModifyVpcPeeringConnectionOptionsResultResponseTypeDef",
    "ModifyVpcTenancyRequestTypeDef",
    "ModifyVpcTenancyResultResponseTypeDef",
    "ModifyVpnConnectionOptionsRequestTypeDef",
    "ModifyVpnConnectionOptionsResultResponseTypeDef",
    "ModifyVpnConnectionRequestTypeDef",
    "ModifyVpnConnectionResultResponseTypeDef",
    "ModifyVpnTunnelCertificateRequestTypeDef",
    "ModifyVpnTunnelCertificateResultResponseTypeDef",
    "ModifyVpnTunnelOptionsRequestTypeDef",
    "ModifyVpnTunnelOptionsResultResponseTypeDef",
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    "MonitorInstancesRequestInstanceTypeDef",
    "MonitorInstancesRequestTypeDef",
    "MonitorInstancesResultResponseTypeDef",
    "MonitoringTypeDef",
    "MoveAddressToVpcRequestTypeDef",
    "MoveAddressToVpcResultResponseTypeDef",
    "MovingAddressStatusTypeDef",
    "NatGatewayAddressTypeDef",
    "NatGatewayTypeDef",
    "NetworkAclAssociationTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkAclTypeDef",
    "NetworkCardInfoTypeDef",
    "NetworkInfoTypeDef",
    "NetworkInsightsAnalysisTypeDef",
    "NetworkInsightsPathTypeDef",
    "NetworkInterfaceAssociationTypeDef",
    "NetworkInterfaceAttachmentChangesTypeDef",
    "NetworkInterfaceAttachmentTypeDef",
    "NetworkInterfaceIpv6AddressTypeDef",
    "NetworkInterfacePermissionStateTypeDef",
    "NetworkInterfacePermissionTypeDef",
    "NetworkInterfacePrivateIpAddressTypeDef",
    "NetworkInterfaceTypeDef",
    "NewDhcpConfigurationTypeDef",
    "OnDemandOptionsRequestTypeDef",
    "OnDemandOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "PciIdTypeDef",
    "PeeringAttachmentStatusTypeDef",
    "PeeringConnectionOptionsRequestTypeDef",
    "PeeringConnectionOptionsTypeDef",
    "PeeringTgwInfoTypeDef",
    "Phase1DHGroupNumbersListValueTypeDef",
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    "Phase2DHGroupNumbersListValueTypeDef",
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    "PlacementGroupInfoTypeDef",
    "PlacementGroupTypeDef",
    "PlacementResponseTypeDef",
    "PlacementTypeDef",
    "PoolCidrBlockTypeDef",
    "PortRangeTypeDef",
    "PrefixListAssociationTypeDef",
    "PrefixListEntryTypeDef",
    "PrefixListIdTypeDef",
    "PrefixListTypeDef",
    "PriceScheduleSpecificationTypeDef",
    "PriceScheduleTypeDef",
    "PricingDetailTypeDef",
    "PrincipalIdFormatTypeDef",
    "PrivateDnsDetailsTypeDef",
    "PrivateDnsNameConfigurationTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "ProcessorInfoTypeDef",
    "ProductCodeTypeDef",
    "PropagatingVgwTypeDef",
    "ProvisionByoipCidrRequestTypeDef",
    "ProvisionByoipCidrResultResponseTypeDef",
    "ProvisionedBandwidthTypeDef",
    "PtrUpdateStatusTypeDef",
    "PublicIpv4PoolRangeTypeDef",
    "PublicIpv4PoolTypeDef",
    "PurchaseHostReservationRequestTypeDef",
    "PurchaseHostReservationResultResponseTypeDef",
    "PurchaseRequestTypeDef",
    "PurchaseReservedInstancesOfferingRequestTypeDef",
    "PurchaseReservedInstancesOfferingResultResponseTypeDef",
    "PurchaseScheduledInstancesRequestTypeDef",
    "PurchaseScheduledInstancesResultResponseTypeDef",
    "PurchaseTypeDef",
    "RebootInstancesRequestInstanceTypeDef",
    "RebootInstancesRequestTypeDef",
    "RecurringChargeTypeDef",
    "RegionTypeDef",
    "RegisterImageRequestServiceResourceTypeDef",
    "RegisterImageRequestTypeDef",
    "RegisterImageResultResponseTypeDef",
    "RegisterInstanceEventNotificationAttributesRequestTypeDef",
    "RegisterInstanceEventNotificationAttributesResultResponseTypeDef",
    "RegisterInstanceTagAttributeRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersResultResponseTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesResultResponseTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsRequestTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsResultResponseTypeDef",
    "RejectTransitGatewayPeeringAttachmentRequestTypeDef",
    "RejectTransitGatewayPeeringAttachmentResultResponseTypeDef",
    "RejectTransitGatewayVpcAttachmentRequestTypeDef",
    "RejectTransitGatewayVpcAttachmentResultResponseTypeDef",
    "RejectVpcEndpointConnectionsRequestTypeDef",
    "RejectVpcEndpointConnectionsResultResponseTypeDef",
    "RejectVpcPeeringConnectionRequestTypeDef",
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    "RejectVpcPeeringConnectionResultResponseTypeDef",
    "ReleaseAddressRequestClassicAddressTypeDef",
    "ReleaseAddressRequestTypeDef",
    "ReleaseAddressRequestVpcAddressTypeDef",
    "ReleaseHostsRequestTypeDef",
    "ReleaseHostsResultResponseTypeDef",
    "RemovePrefixListEntryTypeDef",
    "ReplaceIamInstanceProfileAssociationRequestTypeDef",
    "ReplaceIamInstanceProfileAssociationResultResponseTypeDef",
    "ReplaceNetworkAclAssociationRequestNetworkAclTypeDef",
    "ReplaceNetworkAclAssociationRequestTypeDef",
    "ReplaceNetworkAclAssociationResultResponseTypeDef",
    "ReplaceNetworkAclEntryRequestNetworkAclTypeDef",
    "ReplaceNetworkAclEntryRequestTypeDef",
    "ReplaceRootVolumeTaskTypeDef",
    "ReplaceRouteRequestRouteTypeDef",
    "ReplaceRouteRequestTypeDef",
    "ReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef",
    "ReplaceRouteTableAssociationRequestTypeDef",
    "ReplaceRouteTableAssociationResultResponseTypeDef",
    "ReplaceTransitGatewayRouteRequestTypeDef",
    "ReplaceTransitGatewayRouteResultResponseTypeDef",
    "ReportInstanceStatusRequestInstanceTypeDef",
    "ReportInstanceStatusRequestTypeDef",
    "RequestLaunchTemplateDataTypeDef",
    "RequestSpotFleetRequestTypeDef",
    "RequestSpotFleetResponseResponseTypeDef",
    "RequestSpotInstancesRequestTypeDef",
    "RequestSpotInstancesResultResponseTypeDef",
    "RequestSpotLaunchSpecificationTypeDef",
    "ReservationTypeDef",
    "ReservationValueTypeDef",
    "ReservedInstanceLimitPriceTypeDef",
    "ReservedInstanceReservationValueTypeDef",
    "ReservedInstancesConfigurationTypeDef",
    "ReservedInstancesIdTypeDef",
    "ReservedInstancesListingTypeDef",
    "ReservedInstancesModificationResultTypeDef",
    "ReservedInstancesModificationTypeDef",
    "ReservedInstancesOfferingTypeDef",
    "ReservedInstancesTypeDef",
    "ResetAddressAttributeRequestTypeDef",
    "ResetAddressAttributeResultResponseTypeDef",
    "ResetEbsDefaultKmsKeyIdRequestTypeDef",
    "ResetEbsDefaultKmsKeyIdResultResponseTypeDef",
    "ResetFpgaImageAttributeRequestTypeDef",
    "ResetFpgaImageAttributeResultResponseTypeDef",
    "ResetImageAttributeRequestImageTypeDef",
    "ResetImageAttributeRequestTypeDef",
    "ResetInstanceAttributeRequestInstanceTypeDef",
    "ResetInstanceAttributeRequestTypeDef",
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    "ResetNetworkInterfaceAttributeRequestTypeDef",
    "ResetSnapshotAttributeRequestSnapshotTypeDef",
    "ResetSnapshotAttributeRequestTypeDef",
    "ResponseErrorTypeDef",
    "ResponseLaunchTemplateDataTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreAddressToClassicRequestTypeDef",
    "RestoreAddressToClassicResultResponseTypeDef",
    "RestoreManagedPrefixListVersionRequestTypeDef",
    "RestoreManagedPrefixListVersionResultResponseTypeDef",
    "RevokeClientVpnIngressRequestTypeDef",
    "RevokeClientVpnIngressResultResponseTypeDef",
    "RevokeSecurityGroupEgressRequestSecurityGroupTypeDef",
    "RevokeSecurityGroupEgressRequestTypeDef",
    "RevokeSecurityGroupEgressResultResponseTypeDef",
    "RevokeSecurityGroupIngressRequestSecurityGroupTypeDef",
    "RevokeSecurityGroupIngressRequestTypeDef",
    "RevokeSecurityGroupIngressResultResponseTypeDef",
    "RouteTableAssociationStateTypeDef",
    "RouteTableAssociationTypeDef",
    "RouteTableTypeDef",
    "RouteTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "RunInstancesRequestServiceResourceTypeDef",
    "RunInstancesRequestSubnetTypeDef",
    "RunInstancesRequestTypeDef",
    "RunScheduledInstancesRequestTypeDef",
    "RunScheduledInstancesResultResponseTypeDef",
    "S3ObjectTagTypeDef",
    "S3StorageTypeDef",
    "ScheduledInstanceAvailabilityTypeDef",
    "ScheduledInstanceRecurrenceRequestTypeDef",
    "ScheduledInstanceRecurrenceTypeDef",
    "ScheduledInstanceTypeDef",
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    "ScheduledInstancesEbsTypeDef",
    "ScheduledInstancesIamInstanceProfileTypeDef",
    "ScheduledInstancesIpv6AddressTypeDef",
    "ScheduledInstancesLaunchSpecificationTypeDef",
    "ScheduledInstancesMonitoringTypeDef",
    "ScheduledInstancesNetworkInterfaceTypeDef",
    "ScheduledInstancesPlacementTypeDef",
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    "SearchLocalGatewayRoutesRequestTypeDef",
    "SearchLocalGatewayRoutesResultResponseTypeDef",
    "SearchTransitGatewayMulticastGroupsRequestTypeDef",
    "SearchTransitGatewayMulticastGroupsResultResponseTypeDef",
    "SearchTransitGatewayRoutesRequestTypeDef",
    "SearchTransitGatewayRoutesResultResponseTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SecurityGroupReferenceTypeDef",
    "SecurityGroupTypeDef",
    "SendDiagnosticInterruptRequestTypeDef",
    "ServiceConfigurationTypeDef",
    "ServiceDetailTypeDef",
    "ServiceResourceClassicAddressRequestTypeDef",
    "ServiceResourceDhcpOptionsRequestTypeDef",
    "ServiceResourceImageRequestTypeDef",
    "ServiceResourceInstanceRequestTypeDef",
    "ServiceResourceInternetGatewayRequestTypeDef",
    "ServiceResourceKeyPairRequestTypeDef",
    "ServiceResourceNetworkAclRequestTypeDef",
    "ServiceResourceNetworkInterfaceAssociationRequestTypeDef",
    "ServiceResourceNetworkInterfaceRequestTypeDef",
    "ServiceResourcePlacementGroupRequestTypeDef",
    "ServiceResourceRouteRequestTypeDef",
    "ServiceResourceRouteTableAssociationRequestTypeDef",
    "ServiceResourceRouteTableRequestTypeDef",
    "ServiceResourceSecurityGroupRequestTypeDef",
    "ServiceResourceSnapshotRequestTypeDef",
    "ServiceResourceSubnetRequestTypeDef",
    "ServiceResourceTagRequestTypeDef",
    "ServiceResourceVolumeRequestTypeDef",
    "ServiceResourceVpcAddressRequestTypeDef",
    "ServiceResourceVpcPeeringConnectionRequestTypeDef",
    "ServiceResourceVpcRequestTypeDef",
    "ServiceTypeDetailTypeDef",
    "SlotDateTimeRangeRequestTypeDef",
    "SlotStartTimeRangeRequestTypeDef",
    "SnapshotDetailTypeDef",
    "SnapshotDiskContainerTypeDef",
    "SnapshotInfoTypeDef",
    "SnapshotResponseTypeDef",
    "SnapshotTaskDetailTypeDef",
    "SpotCapacityRebalanceTypeDef",
    "SpotDatafeedSubscriptionTypeDef",
    "SpotFleetLaunchSpecificationTypeDef",
    "SpotFleetMonitoringTypeDef",
    "SpotFleetRequestConfigDataTypeDef",
    "SpotFleetRequestConfigTypeDef",
    "SpotFleetTagSpecificationTypeDef",
    "SpotInstanceRequestTypeDef",
    "SpotInstanceStateFaultTypeDef",
    "SpotInstanceStatusTypeDef",
    "SpotMaintenanceStrategiesTypeDef",
    "SpotMarketOptionsTypeDef",
    "SpotOptionsRequestTypeDef",
    "SpotOptionsTypeDef",
    "SpotPlacementTypeDef",
    "SpotPriceTypeDef",
    "StaleIpPermissionTypeDef",
    "StaleSecurityGroupTypeDef",
    "StartInstancesRequestInstanceTypeDef",
    "StartInstancesRequestTypeDef",
    "StartInstancesResultResponseTypeDef",
    "StartNetworkInsightsAnalysisRequestTypeDef",
    "StartNetworkInsightsAnalysisResultResponseTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationRequestTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationResultResponseTypeDef",
    "StateReasonTypeDef",
    "StopInstancesRequestInstanceTypeDef",
    "StopInstancesRequestTypeDef",
    "StopInstancesResultResponseTypeDef",
    "StorageLocationTypeDef",
    "StorageTypeDef",
    "StoreImageTaskResultTypeDef",
    "SubnetAssociationTypeDef",
    "SubnetCidrBlockStateTypeDef",
    "SubnetIpv6CidrBlockAssociationTypeDef",
    "SubnetTypeDef",
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    "TagDescriptionTypeDef",
    "TagSpecificationTypeDef",
    "TagTypeDef",
    "TargetCapacitySpecificationRequestTypeDef",
    "TargetCapacitySpecificationTypeDef",
    "TargetConfigurationRequestTypeDef",
    "TargetConfigurationTypeDef",
    "TargetGroupTypeDef",
    "TargetGroupsConfigTypeDef",
    "TargetNetworkTypeDef",
    "TargetReservationValueTypeDef",
    "TerminateClientVpnConnectionsRequestTypeDef",
    "TerminateClientVpnConnectionsResultResponseTypeDef",
    "TerminateConnectionStatusTypeDef",
    "TerminateInstancesRequestInstanceTypeDef",
    "TerminateInstancesRequestTypeDef",
    "TerminateInstancesResultResponseTypeDef",
    "TrafficMirrorFilterRuleTypeDef",
    "TrafficMirrorFilterTypeDef",
    "TrafficMirrorPortRangeRequestTypeDef",
    "TrafficMirrorPortRangeTypeDef",
    "TrafficMirrorSessionTypeDef",
    "TrafficMirrorTargetTypeDef",
    "TransitGatewayAssociationTypeDef",
    "TransitGatewayAttachmentAssociationTypeDef",
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    "TransitGatewayAttachmentPropagationTypeDef",
    "TransitGatewayAttachmentTypeDef",
    "TransitGatewayConnectOptionsTypeDef",
    "TransitGatewayConnectPeerConfigurationTypeDef",
    "TransitGatewayConnectPeerTypeDef",
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    "TransitGatewayConnectTypeDef",
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    "TransitGatewayMulticastDomainAssociationTypeDef",
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    "TransitGatewayMulticastDomainOptionsTypeDef",
    "TransitGatewayMulticastDomainTypeDef",
    "TransitGatewayMulticastGroupTypeDef",
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    "TransitGatewayOptionsTypeDef",
    "TransitGatewayPeeringAttachmentTypeDef",
    "TransitGatewayPrefixListAttachmentTypeDef",
    "TransitGatewayPrefixListReferenceTypeDef",
    "TransitGatewayPropagationTypeDef",
    "TransitGatewayRequestOptionsTypeDef",
    "TransitGatewayRouteAttachmentTypeDef",
    "TransitGatewayRouteTableAssociationTypeDef",
    "TransitGatewayRouteTablePropagationTypeDef",
    "TransitGatewayRouteTableTypeDef",
    "TransitGatewayRouteTypeDef",
    "TransitGatewayTypeDef",
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    "TransitGatewayVpcAttachmentTypeDef",
    "TrunkInterfaceAssociationTypeDef",
    "TunnelOptionTypeDef",
    "UnassignIpv6AddressesRequestTypeDef",
    "UnassignIpv6AddressesResultResponseTypeDef",
    "UnassignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    "UnassignPrivateIpAddressesRequestTypeDef",
    "UnmonitorInstancesRequestInstanceTypeDef",
    "UnmonitorInstancesRequestTypeDef",
    "UnmonitorInstancesResultResponseTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    "UnsuccessfulItemErrorTypeDef",
    "UnsuccessfulItemTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressResultResponseTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressResultResponseTypeDef",
    "UserBucketDetailsTypeDef",
    "UserBucketTypeDef",
    "UserDataTypeDef",
    "UserIdGroupPairTypeDef",
    "VCpuInfoTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "VgwTelemetryTypeDef",
    "VolumeAttachmentResponseTypeDef",
    "VolumeDetailTypeDef",
    "VolumeModificationTypeDef",
    "VolumeResponseTypeDef",
    "VolumeStatusActionTypeDef",
    "VolumeStatusAttachmentStatusTypeDef",
    "VolumeStatusDetailsTypeDef",
    "VolumeStatusEventTypeDef",
    "VolumeStatusInfoTypeDef",
    "VolumeStatusItemTypeDef",
    "VpcAttachmentTypeDef",
    "VpcCidrBlockAssociationTypeDef",
    "VpcCidrBlockStateTypeDef",
    "VpcClassicLinkTypeDef",
    "VpcEndpointConnectionTypeDef",
    "VpcEndpointTypeDef",
    "VpcIpv6CidrBlockAssociationTypeDef",
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    "VpcPeeringConnectionStateReasonTypeDef",
    "VpcPeeringConnectionTypeDef",
    "VpcPeeringConnectionVpcInfoTypeDef",
    "VpcTypeDef",
    "VpnConnectionOptionsSpecificationTypeDef",
    "VpnConnectionOptionsTypeDef",
    "VpnConnectionTypeDef",
    "VpnGatewayTypeDef",
    "VpnStaticRouteTypeDef",
    "VpnTunnelOptionsSpecificationTypeDef",
    "WaiterConfigTypeDef",
    "WithdrawByoipCidrRequestTypeDef",
    "WithdrawByoipCidrResultResponseTypeDef",
)

_RequiredAcceptReservedInstancesExchangeQuoteRequestTypeDef = TypedDict(
    "_RequiredAcceptReservedInstancesExchangeQuoteRequestTypeDef",
    {
        "ReservedInstanceIds": List[str],
    },
)
_OptionalAcceptReservedInstancesExchangeQuoteRequestTypeDef = TypedDict(
    "_OptionalAcceptReservedInstancesExchangeQuoteRequestTypeDef",
    {
        "DryRun": bool,
        "TargetConfigurations": List["TargetConfigurationRequestTypeDef"],
    },
    total=False,
)


class AcceptReservedInstancesExchangeQuoteRequestTypeDef(
    _RequiredAcceptReservedInstancesExchangeQuoteRequestTypeDef,
    _OptionalAcceptReservedInstancesExchangeQuoteRequestTypeDef,
):
    pass


AcceptReservedInstancesExchangeQuoteResultResponseTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteResultResponseTypeDef",
    {
        "ExchangeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptTransitGatewayMulticastDomainAssociationsRequestTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

AcceptTransitGatewayMulticastDomainAssociationsResultResponseTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsResultResponseTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_RequiredAcceptTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAcceptTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_OptionalAcceptTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AcceptTransitGatewayPeeringAttachmentRequestTypeDef(
    _RequiredAcceptTransitGatewayPeeringAttachmentRequestTypeDef,
    _OptionalAcceptTransitGatewayPeeringAttachmentRequestTypeDef,
):
    pass


AcceptTransitGatewayPeeringAttachmentResultResponseTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentResultResponseTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_RequiredAcceptTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAcceptTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_OptionalAcceptTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AcceptTransitGatewayVpcAttachmentRequestTypeDef(
    _RequiredAcceptTransitGatewayVpcAttachmentRequestTypeDef,
    _OptionalAcceptTransitGatewayVpcAttachmentRequestTypeDef,
):
    pass


AcceptTransitGatewayVpcAttachmentResultResponseTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentResultResponseTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptVpcEndpointConnectionsRequestTypeDef = TypedDict(
    "_RequiredAcceptVpcEndpointConnectionsRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": List[str],
    },
)
_OptionalAcceptVpcEndpointConnectionsRequestTypeDef = TypedDict(
    "_OptionalAcceptVpcEndpointConnectionsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AcceptVpcEndpointConnectionsRequestTypeDef(
    _RequiredAcceptVpcEndpointConnectionsRequestTypeDef,
    _OptionalAcceptVpcEndpointConnectionsRequestTypeDef,
):
    pass


AcceptVpcEndpointConnectionsResultResponseTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsResultResponseTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptVpcPeeringConnectionRequestTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestTypeDef",
    {
        "DryRun": bool,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

AcceptVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

AcceptVpcPeeringConnectionResultResponseTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionResultResponseTypeDef",
    {
        "VpcPeeringConnection": "VpcPeeringConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List["AccountAttributeValueTypeDef"],
    },
    total=False,
)

AccountAttributeValueTypeDef = TypedDict(
    "AccountAttributeValueTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

ActiveInstanceTypeDef = TypedDict(
    "ActiveInstanceTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "SpotInstanceRequestId": str,
        "InstanceHealth": InstanceHealthStatusType,
    },
    total=False,
)

_RequiredAddPrefixListEntryTypeDef = TypedDict(
    "_RequiredAddPrefixListEntryTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalAddPrefixListEntryTypeDef = TypedDict(
    "_OptionalAddPrefixListEntryTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class AddPrefixListEntryTypeDef(
    _RequiredAddPrefixListEntryTypeDef, _OptionalAddPrefixListEntryTypeDef
):
    pass


AddressAttributeTypeDef = TypedDict(
    "AddressAttributeTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PtrRecord": str,
        "PtrRecordUpdate": "PtrUpdateStatusTypeDef",
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllocationId": str,
        "AssociationId": str,
        "Domain": DomainTypeType,
        "NetworkInterfaceId": str,
        "NetworkInterfaceOwnerId": str,
        "PrivateIpAddress": str,
        "Tags": List["TagTypeDef"],
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
    },
    total=False,
)

_RequiredAdvertiseByoipCidrRequestTypeDef = TypedDict(
    "_RequiredAdvertiseByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalAdvertiseByoipCidrRequestTypeDef = TypedDict(
    "_OptionalAdvertiseByoipCidrRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AdvertiseByoipCidrRequestTypeDef(
    _RequiredAdvertiseByoipCidrRequestTypeDef, _OptionalAdvertiseByoipCidrRequestTypeDef
):
    pass


AdvertiseByoipCidrResultResponseTypeDef = TypedDict(
    "AdvertiseByoipCidrResultResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateAddressRequestTypeDef = TypedDict(
    "AllocateAddressRequestTypeDef",
    {
        "Domain": DomainTypeType,
        "Address": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "CustomerOwnedIpv4Pool": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

AllocateAddressResultResponseTypeDef = TypedDict(
    "AllocateAddressResultResponseTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "Domain": DomainTypeType,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAllocateHostsRequestTypeDef = TypedDict(
    "_RequiredAllocateHostsRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Quantity": int,
    },
)
_OptionalAllocateHostsRequestTypeDef = TypedDict(
    "_OptionalAllocateHostsRequestTypeDef",
    {
        "AutoPlacement": AutoPlacementType,
        "ClientToken": str,
        "InstanceType": str,
        "InstanceFamily": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "HostRecovery": HostRecoveryType,
    },
    total=False,
)


class AllocateHostsRequestTypeDef(
    _RequiredAllocateHostsRequestTypeDef, _OptionalAllocateHostsRequestTypeDef
):
    pass


AllocateHostsResultResponseTypeDef = TypedDict(
    "AllocateHostsResultResponseTypeDef",
    {
        "HostIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllowedPrincipalTypeDef = TypedDict(
    "AllowedPrincipalTypeDef",
    {
        "PrincipalType": PrincipalTypeType,
        "Principal": str,
    },
    total=False,
)

AlternatePathHintTypeDef = TypedDict(
    "AlternatePathHintTypeDef",
    {
        "ComponentId": str,
        "ComponentArn": str,
    },
    total=False,
)

AnalysisAclRuleTypeDef = TypedDict(
    "AnalysisAclRuleTypeDef",
    {
        "Cidr": str,
        "Egress": bool,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
    },
    total=False,
)

AnalysisComponentTypeDef = TypedDict(
    "AnalysisComponentTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

AnalysisLoadBalancerListenerTypeDef = TypedDict(
    "AnalysisLoadBalancerListenerTypeDef",
    {
        "LoadBalancerPort": int,
        "InstancePort": int,
    },
    total=False,
)

AnalysisLoadBalancerTargetTypeDef = TypedDict(
    "AnalysisLoadBalancerTargetTypeDef",
    {
        "Address": str,
        "AvailabilityZone": str,
        "Instance": "AnalysisComponentTypeDef",
        "Port": int,
    },
    total=False,
)

AnalysisPacketHeaderTypeDef = TypedDict(
    "AnalysisPacketHeaderTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPortRanges": List["PortRangeTypeDef"],
        "Protocol": str,
        "SourceAddresses": List[str],
        "SourcePortRanges": List["PortRangeTypeDef"],
    },
    total=False,
)

AnalysisRouteTableRouteTypeDef = TypedDict(
    "AnalysisRouteTableRouteTypeDef",
    {
        "DestinationCidr": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "NatGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": str,
        "TransitGatewayId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

AnalysisSecurityGroupRuleTypeDef = TypedDict(
    "AnalysisSecurityGroupRuleTypeDef",
    {
        "Cidr": str,
        "Direction": str,
        "SecurityGroupId": str,
        "PortRange": "PortRangeTypeDef",
        "PrefixListId": str,
        "Protocol": str,
    },
    total=False,
)

_RequiredApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef = TypedDict(
    "_RequiredApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": List[str],
    },
)
_OptionalApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef = TypedDict(
    "_OptionalApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef(
    _RequiredApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef,
    _OptionalApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef,
):
    pass


ApplySecurityGroupsToClientVpnTargetNetworkResultResponseTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkResultResponseTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssignIpv6AddressesRequestTypeDef = TypedDict(
    "_RequiredAssignIpv6AddressesRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalAssignIpv6AddressesRequestTypeDef = TypedDict(
    "_OptionalAssignIpv6AddressesRequestTypeDef",
    {
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List[str],
    },
    total=False,
)


class AssignIpv6AddressesRequestTypeDef(
    _RequiredAssignIpv6AddressesRequestTypeDef, _OptionalAssignIpv6AddressesRequestTypeDef
):
    pass


AssignIpv6AddressesResultResponseTypeDef = TypedDict(
    "AssignIpv6AddressesResultResponseTypeDef",
    {
        "AssignedIpv6Addresses": List[str],
        "NetworkInterfaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignPrivateIpAddressesRequestNetworkInterfaceTypeDef = TypedDict(
    "AssignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    {
        "AllowReassignment": bool,
        "PrivateIpAddresses": List[str],
        "SecondaryPrivateIpAddressCount": int,
    },
    total=False,
)

_RequiredAssignPrivateIpAddressesRequestTypeDef = TypedDict(
    "_RequiredAssignPrivateIpAddressesRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalAssignPrivateIpAddressesRequestTypeDef = TypedDict(
    "_OptionalAssignPrivateIpAddressesRequestTypeDef",
    {
        "AllowReassignment": bool,
        "PrivateIpAddresses": List[str],
        "SecondaryPrivateIpAddressCount": int,
    },
    total=False,
)


class AssignPrivateIpAddressesRequestTypeDef(
    _RequiredAssignPrivateIpAddressesRequestTypeDef, _OptionalAssignPrivateIpAddressesRequestTypeDef
):
    pass


AssignPrivateIpAddressesResultResponseTypeDef = TypedDict(
    "AssignPrivateIpAddressesResultResponseTypeDef",
    {
        "NetworkInterfaceId": str,
        "AssignedPrivateIpAddresses": List["AssignedPrivateIpAddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignedPrivateIpAddressTypeDef = TypedDict(
    "AssignedPrivateIpAddressTypeDef",
    {
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressRequestClassicAddressTypeDef = TypedDict(
    "AssociateAddressRequestClassicAddressTypeDef",
    {
        "AllocationId": str,
        "InstanceId": str,
        "AllowReassociation": bool,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressRequestTypeDef = TypedDict(
    "AssociateAddressRequestTypeDef",
    {
        "AllocationId": str,
        "InstanceId": str,
        "PublicIp": str,
        "AllowReassociation": bool,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressRequestVpcAddressTypeDef = TypedDict(
    "AssociateAddressRequestVpcAddressTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllowReassociation": bool,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressResultResponseTypeDef = TypedDict(
    "AssociateAddressResultResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateClientVpnTargetNetworkRequestTypeDef = TypedDict(
    "_RequiredAssociateClientVpnTargetNetworkRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "SubnetId": str,
    },
)
_OptionalAssociateClientVpnTargetNetworkRequestTypeDef = TypedDict(
    "_OptionalAssociateClientVpnTargetNetworkRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)


class AssociateClientVpnTargetNetworkRequestTypeDef(
    _RequiredAssociateClientVpnTargetNetworkRequestTypeDef,
    _OptionalAssociateClientVpnTargetNetworkRequestTypeDef,
):
    pass


AssociateClientVpnTargetNetworkResultResponseTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkResultResponseTypeDef",
    {
        "AssociationId": str,
        "Status": "AssociationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateDhcpOptionsRequestDhcpOptionsTypeDef = TypedDict(
    "_RequiredAssociateDhcpOptionsRequestDhcpOptionsTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalAssociateDhcpOptionsRequestDhcpOptionsTypeDef = TypedDict(
    "_OptionalAssociateDhcpOptionsRequestDhcpOptionsTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateDhcpOptionsRequestDhcpOptionsTypeDef(
    _RequiredAssociateDhcpOptionsRequestDhcpOptionsTypeDef,
    _OptionalAssociateDhcpOptionsRequestDhcpOptionsTypeDef,
):
    pass


_RequiredAssociateDhcpOptionsRequestTypeDef = TypedDict(
    "_RequiredAssociateDhcpOptionsRequestTypeDef",
    {
        "DhcpOptionsId": str,
        "VpcId": str,
    },
)
_OptionalAssociateDhcpOptionsRequestTypeDef = TypedDict(
    "_OptionalAssociateDhcpOptionsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateDhcpOptionsRequestTypeDef(
    _RequiredAssociateDhcpOptionsRequestTypeDef, _OptionalAssociateDhcpOptionsRequestTypeDef
):
    pass


_RequiredAssociateDhcpOptionsRequestVpcTypeDef = TypedDict(
    "_RequiredAssociateDhcpOptionsRequestVpcTypeDef",
    {
        "DhcpOptionsId": str,
    },
)
_OptionalAssociateDhcpOptionsRequestVpcTypeDef = TypedDict(
    "_OptionalAssociateDhcpOptionsRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateDhcpOptionsRequestVpcTypeDef(
    _RequiredAssociateDhcpOptionsRequestVpcTypeDef, _OptionalAssociateDhcpOptionsRequestVpcTypeDef
):
    pass


AssociateEnclaveCertificateIamRoleRequestTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleRequestTypeDef",
    {
        "CertificateArn": str,
        "RoleArn": str,
        "DryRun": bool,
    },
    total=False,
)

AssociateEnclaveCertificateIamRoleResultResponseTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleResultResponseTypeDef",
    {
        "CertificateS3BucketName": str,
        "CertificateS3ObjectKey": str,
        "EncryptionKmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIamInstanceProfileRequestTypeDef = TypedDict(
    "AssociateIamInstanceProfileRequestTypeDef",
    {
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceId": str,
    },
)

AssociateIamInstanceProfileResultResponseTypeDef = TypedDict(
    "AssociateIamInstanceProfileResultResponseTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateRouteTableRequestRouteTableTypeDef = TypedDict(
    "AssociateRouteTableRequestRouteTableTypeDef",
    {
        "DryRun": bool,
        "SubnetId": str,
        "GatewayId": str,
    },
    total=False,
)

_RequiredAssociateRouteTableRequestTypeDef = TypedDict(
    "_RequiredAssociateRouteTableRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalAssociateRouteTableRequestTypeDef = TypedDict(
    "_OptionalAssociateRouteTableRequestTypeDef",
    {
        "DryRun": bool,
        "SubnetId": str,
        "GatewayId": str,
    },
    total=False,
)


class AssociateRouteTableRequestTypeDef(
    _RequiredAssociateRouteTableRequestTypeDef, _OptionalAssociateRouteTableRequestTypeDef
):
    pass


AssociateRouteTableResultResponseTypeDef = TypedDict(
    "AssociateRouteTableResultResponseTypeDef",
    {
        "AssociationId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSubnetCidrBlockRequestTypeDef = TypedDict(
    "AssociateSubnetCidrBlockRequestTypeDef",
    {
        "Ipv6CidrBlock": str,
        "SubnetId": str,
    },
)

AssociateSubnetCidrBlockResultResponseTypeDef = TypedDict(
    "AssociateSubnetCidrBlockResultResponseTypeDef",
    {
        "Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef",
        "SubnetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTransitGatewayMulticastDomainRequestTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

AssociateTransitGatewayMulticastDomainResultResponseTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainResultResponseTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_RequiredAssociateTransitGatewayRouteTableRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAssociateTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_OptionalAssociateTransitGatewayRouteTableRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AssociateTransitGatewayRouteTableRequestTypeDef(
    _RequiredAssociateTransitGatewayRouteTableRequestTypeDef,
    _OptionalAssociateTransitGatewayRouteTableRequestTypeDef,
):
    pass


AssociateTransitGatewayRouteTableResultResponseTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableResultResponseTypeDef",
    {
        "Association": "TransitGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTrunkInterfaceRequestTypeDef = TypedDict(
    "_RequiredAssociateTrunkInterfaceRequestTypeDef",
    {
        "BranchInterfaceId": str,
        "TrunkInterfaceId": str,
    },
)
_OptionalAssociateTrunkInterfaceRequestTypeDef = TypedDict(
    "_OptionalAssociateTrunkInterfaceRequestTypeDef",
    {
        "VlanId": int,
        "GreKey": int,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)


class AssociateTrunkInterfaceRequestTypeDef(
    _RequiredAssociateTrunkInterfaceRequestTypeDef, _OptionalAssociateTrunkInterfaceRequestTypeDef
):
    pass


AssociateTrunkInterfaceResultResponseTypeDef = TypedDict(
    "AssociateTrunkInterfaceResultResponseTypeDef",
    {
        "InterfaceAssociation": "TrunkInterfaceAssociationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateVpcCidrBlockRequestTypeDef = TypedDict(
    "_RequiredAssociateVpcCidrBlockRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalAssociateVpcCidrBlockRequestTypeDef = TypedDict(
    "_OptionalAssociateVpcCidrBlockRequestTypeDef",
    {
        "AmazonProvidedIpv6CidrBlock": bool,
        "CidrBlock": str,
        "Ipv6CidrBlockNetworkBorderGroup": str,
        "Ipv6Pool": str,
        "Ipv6CidrBlock": str,
    },
    total=False,
)


class AssociateVpcCidrBlockRequestTypeDef(
    _RequiredAssociateVpcCidrBlockRequestTypeDef, _OptionalAssociateVpcCidrBlockRequestTypeDef
):
    pass


AssociateVpcCidrBlockResultResponseTypeDef = TypedDict(
    "AssociateVpcCidrBlockResultResponseTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatedRoleTypeDef = TypedDict(
    "AssociatedRoleTypeDef",
    {
        "AssociatedRoleArn": str,
        "CertificateS3BucketName": str,
        "CertificateS3ObjectKey": str,
        "EncryptionKmsKeyId": str,
    },
    total=False,
)

AssociatedTargetNetworkTypeDef = TypedDict(
    "AssociatedTargetNetworkTypeDef",
    {
        "NetworkId": str,
        "NetworkType": Literal["vpc"],
    },
    total=False,
)

AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Code": AssociationStatusCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredAthenaIntegrationTypeDef = TypedDict(
    "_RequiredAthenaIntegrationTypeDef",
    {
        "IntegrationResultS3DestinationArn": str,
        "PartitionLoadFrequency": PartitionLoadFrequencyType,
    },
)
_OptionalAthenaIntegrationTypeDef = TypedDict(
    "_OptionalAthenaIntegrationTypeDef",
    {
        "PartitionStartDate": Union[datetime, str],
        "PartitionEndDate": Union[datetime, str],
    },
    total=False,
)


class AthenaIntegrationTypeDef(
    _RequiredAthenaIntegrationTypeDef, _OptionalAthenaIntegrationTypeDef
):
    pass


_RequiredAttachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_RequiredAttachClassicLinkVpcRequestInstanceTypeDef",
    {
        "Groups": List[str],
        "VpcId": str,
    },
)
_OptionalAttachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_OptionalAttachClassicLinkVpcRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachClassicLinkVpcRequestInstanceTypeDef(
    _RequiredAttachClassicLinkVpcRequestInstanceTypeDef,
    _OptionalAttachClassicLinkVpcRequestInstanceTypeDef,
):
    pass


_RequiredAttachClassicLinkVpcRequestTypeDef = TypedDict(
    "_RequiredAttachClassicLinkVpcRequestTypeDef",
    {
        "Groups": List[str],
        "InstanceId": str,
        "VpcId": str,
    },
)
_OptionalAttachClassicLinkVpcRequestTypeDef = TypedDict(
    "_OptionalAttachClassicLinkVpcRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachClassicLinkVpcRequestTypeDef(
    _RequiredAttachClassicLinkVpcRequestTypeDef, _OptionalAttachClassicLinkVpcRequestTypeDef
):
    pass


_RequiredAttachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_RequiredAttachClassicLinkVpcRequestVpcTypeDef",
    {
        "Groups": List[str],
        "InstanceId": str,
    },
)
_OptionalAttachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_OptionalAttachClassicLinkVpcRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachClassicLinkVpcRequestVpcTypeDef(
    _RequiredAttachClassicLinkVpcRequestVpcTypeDef, _OptionalAttachClassicLinkVpcRequestVpcTypeDef
):
    pass


AttachClassicLinkVpcResultResponseTypeDef = TypedDict(
    "AttachClassicLinkVpcResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_RequiredAttachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalAttachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_OptionalAttachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachInternetGatewayRequestInternetGatewayTypeDef(
    _RequiredAttachInternetGatewayRequestInternetGatewayTypeDef,
    _OptionalAttachInternetGatewayRequestInternetGatewayTypeDef,
):
    pass


_RequiredAttachInternetGatewayRequestTypeDef = TypedDict(
    "_RequiredAttachInternetGatewayRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
    },
)
_OptionalAttachInternetGatewayRequestTypeDef = TypedDict(
    "_OptionalAttachInternetGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachInternetGatewayRequestTypeDef(
    _RequiredAttachInternetGatewayRequestTypeDef, _OptionalAttachInternetGatewayRequestTypeDef
):
    pass


_RequiredAttachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_RequiredAttachInternetGatewayRequestVpcTypeDef",
    {
        "InternetGatewayId": str,
    },
)
_OptionalAttachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_OptionalAttachInternetGatewayRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachInternetGatewayRequestVpcTypeDef(
    _RequiredAttachInternetGatewayRequestVpcTypeDef, _OptionalAttachInternetGatewayRequestVpcTypeDef
):
    pass


_RequiredAttachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_RequiredAttachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
    },
)
_OptionalAttachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_OptionalAttachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
        "NetworkCardIndex": int,
    },
    total=False,
)


class AttachNetworkInterfaceRequestNetworkInterfaceTypeDef(
    _RequiredAttachNetworkInterfaceRequestNetworkInterfaceTypeDef,
    _OptionalAttachNetworkInterfaceRequestNetworkInterfaceTypeDef,
):
    pass


_RequiredAttachNetworkInterfaceRequestTypeDef = TypedDict(
    "_RequiredAttachNetworkInterfaceRequestTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
        "NetworkInterfaceId": str,
    },
)
_OptionalAttachNetworkInterfaceRequestTypeDef = TypedDict(
    "_OptionalAttachNetworkInterfaceRequestTypeDef",
    {
        "DryRun": bool,
        "NetworkCardIndex": int,
    },
    total=False,
)


class AttachNetworkInterfaceRequestTypeDef(
    _RequiredAttachNetworkInterfaceRequestTypeDef, _OptionalAttachNetworkInterfaceRequestTypeDef
):
    pass


AttachNetworkInterfaceResultResponseTypeDef = TypedDict(
    "AttachNetworkInterfaceResultResponseTypeDef",
    {
        "AttachmentId": str,
        "NetworkCardIndex": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachVolumeRequestInstanceTypeDef = TypedDict(
    "_RequiredAttachVolumeRequestInstanceTypeDef",
    {
        "Device": str,
        "VolumeId": str,
    },
)
_OptionalAttachVolumeRequestInstanceTypeDef = TypedDict(
    "_OptionalAttachVolumeRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachVolumeRequestInstanceTypeDef(
    _RequiredAttachVolumeRequestInstanceTypeDef, _OptionalAttachVolumeRequestInstanceTypeDef
):
    pass


_RequiredAttachVolumeRequestTypeDef = TypedDict(
    "_RequiredAttachVolumeRequestTypeDef",
    {
        "Device": str,
        "InstanceId": str,
        "VolumeId": str,
    },
)
_OptionalAttachVolumeRequestTypeDef = TypedDict(
    "_OptionalAttachVolumeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachVolumeRequestTypeDef(
    _RequiredAttachVolumeRequestTypeDef, _OptionalAttachVolumeRequestTypeDef
):
    pass


_RequiredAttachVolumeRequestVolumeTypeDef = TypedDict(
    "_RequiredAttachVolumeRequestVolumeTypeDef",
    {
        "Device": str,
        "InstanceId": str,
    },
)
_OptionalAttachVolumeRequestVolumeTypeDef = TypedDict(
    "_OptionalAttachVolumeRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachVolumeRequestVolumeTypeDef(
    _RequiredAttachVolumeRequestVolumeTypeDef, _OptionalAttachVolumeRequestVolumeTypeDef
):
    pass


_RequiredAttachVpnGatewayRequestTypeDef = TypedDict(
    "_RequiredAttachVpnGatewayRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
    },
)
_OptionalAttachVpnGatewayRequestTypeDef = TypedDict(
    "_OptionalAttachVpnGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class AttachVpnGatewayRequestTypeDef(
    _RequiredAttachVpnGatewayRequestTypeDef, _OptionalAttachVpnGatewayRequestTypeDef
):
    pass


AttachVpnGatewayResultResponseTypeDef = TypedDict(
    "AttachVpnGatewayResultResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeBooleanValueTypeDef = TypedDict(
    "AttributeBooleanValueTypeDef",
    {
        "Value": bool,
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

AuthorizationRuleTypeDef = TypedDict(
    "AuthorizationRuleTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Description": str,
        "GroupId": str,
        "AccessAll": bool,
        "DestinationCidr": str,
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
    },
    total=False,
)

_RequiredAuthorizeClientVpnIngressRequestTypeDef = TypedDict(
    "_RequiredAuthorizeClientVpnIngressRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
    },
)
_OptionalAuthorizeClientVpnIngressRequestTypeDef = TypedDict(
    "_OptionalAuthorizeClientVpnIngressRequestTypeDef",
    {
        "AccessGroupId": str,
        "AuthorizeAllGroups": bool,
        "Description": str,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)


class AuthorizeClientVpnIngressRequestTypeDef(
    _RequiredAuthorizeClientVpnIngressRequestTypeDef,
    _OptionalAuthorizeClientVpnIngressRequestTypeDef,
):
    pass


AuthorizeClientVpnIngressResultResponseTypeDef = TypedDict(
    "AuthorizeClientVpnIngressResultResponseTypeDef",
    {
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeSecurityGroupEgressRequestSecurityGroupTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressRequestSecurityGroupTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)

_RequiredAuthorizeSecurityGroupEgressRequestTypeDef = TypedDict(
    "_RequiredAuthorizeSecurityGroupEgressRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalAuthorizeSecurityGroupEgressRequestTypeDef = TypedDict(
    "_OptionalAuthorizeSecurityGroupEgressRequestTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)


class AuthorizeSecurityGroupEgressRequestTypeDef(
    _RequiredAuthorizeSecurityGroupEgressRequestTypeDef,
    _OptionalAuthorizeSecurityGroupEgressRequestTypeDef,
):
    pass


AuthorizeSecurityGroupIngressRequestSecurityGroupTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestSecurityGroupTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
    },
    total=False,
)

AuthorizeSecurityGroupIngressRequestTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupId": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
    },
    total=False,
)

AvailabilityZoneMessageTypeDef = TypedDict(
    "AvailabilityZoneMessageTypeDef",
    {
        "Message": str,
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "State": AvailabilityZoneStateType,
        "OptInStatus": AvailabilityZoneOptInStatusType,
        "Messages": List["AvailabilityZoneMessageTypeDef"],
        "RegionName": str,
        "ZoneName": str,
        "ZoneId": str,
        "GroupName": str,
        "NetworkBorderGroup": str,
        "ZoneType": str,
        "ParentZoneName": str,
        "ParentZoneId": str,
    },
    total=False,
)

AvailableCapacityTypeDef = TypedDict(
    "AvailableCapacityTypeDef",
    {
        "AvailableInstanceCapacity": List["InstanceCapacityTypeDef"],
        "AvailableVCpus": int,
    },
    total=False,
)

BlobAttributeValueTypeDef = TypedDict(
    "BlobAttributeValueTypeDef",
    {
        "Value": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "EbsBlockDeviceTypeDef",
        "NoDevice": str,
    },
    total=False,
)

_RequiredBundleInstanceRequestTypeDef = TypedDict(
    "_RequiredBundleInstanceRequestTypeDef",
    {
        "InstanceId": str,
        "Storage": "StorageTypeDef",
    },
)
_OptionalBundleInstanceRequestTypeDef = TypedDict(
    "_OptionalBundleInstanceRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class BundleInstanceRequestTypeDef(
    _RequiredBundleInstanceRequestTypeDef, _OptionalBundleInstanceRequestTypeDef
):
    pass


BundleInstanceResultResponseTypeDef = TypedDict(
    "BundleInstanceResultResponseTypeDef",
    {
        "BundleTask": "BundleTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BundleTaskErrorTypeDef = TypedDict(
    "BundleTaskErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

BundleTaskTypeDef = TypedDict(
    "BundleTaskTypeDef",
    {
        "BundleId": str,
        "BundleTaskError": "BundleTaskErrorTypeDef",
        "InstanceId": str,
        "Progress": str,
        "StartTime": datetime,
        "State": BundleTaskStateType,
        "Storage": "StorageTypeDef",
        "UpdateTime": datetime,
    },
    total=False,
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": str,
        "Description": str,
        "StatusMessage": str,
        "State": ByoipCidrStateType,
    },
    total=False,
)

_RequiredCancelBundleTaskRequestTypeDef = TypedDict(
    "_RequiredCancelBundleTaskRequestTypeDef",
    {
        "BundleId": str,
    },
)
_OptionalCancelBundleTaskRequestTypeDef = TypedDict(
    "_OptionalCancelBundleTaskRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CancelBundleTaskRequestTypeDef(
    _RequiredCancelBundleTaskRequestTypeDef, _OptionalCancelBundleTaskRequestTypeDef
):
    pass


CancelBundleTaskResultResponseTypeDef = TypedDict(
    "CancelBundleTaskResultResponseTypeDef",
    {
        "BundleTask": "BundleTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelCapacityReservationRequestTypeDef = TypedDict(
    "_RequiredCancelCapacityReservationRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalCancelCapacityReservationRequestTypeDef = TypedDict(
    "_OptionalCancelCapacityReservationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CancelCapacityReservationRequestTypeDef(
    _RequiredCancelCapacityReservationRequestTypeDef,
    _OptionalCancelCapacityReservationRequestTypeDef,
):
    pass


CancelCapacityReservationResultResponseTypeDef = TypedDict(
    "CancelCapacityReservationResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelConversionRequestTypeDef = TypedDict(
    "_RequiredCancelConversionRequestTypeDef",
    {
        "ConversionTaskId": str,
    },
)
_OptionalCancelConversionRequestTypeDef = TypedDict(
    "_OptionalCancelConversionRequestTypeDef",
    {
        "DryRun": bool,
        "ReasonMessage": str,
    },
    total=False,
)


class CancelConversionRequestTypeDef(
    _RequiredCancelConversionRequestTypeDef, _OptionalCancelConversionRequestTypeDef
):
    pass


CancelExportTaskRequestTypeDef = TypedDict(
    "CancelExportTaskRequestTypeDef",
    {
        "ExportTaskId": str,
    },
)

CancelImportTaskRequestTypeDef = TypedDict(
    "CancelImportTaskRequestTypeDef",
    {
        "CancelReason": str,
        "DryRun": bool,
        "ImportTaskId": str,
    },
    total=False,
)

CancelImportTaskResultResponseTypeDef = TypedDict(
    "CancelImportTaskResultResponseTypeDef",
    {
        "ImportTaskId": str,
        "PreviousState": str,
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelReservedInstancesListingRequestTypeDef = TypedDict(
    "CancelReservedInstancesListingRequestTypeDef",
    {
        "ReservedInstancesListingId": str,
    },
)

CancelReservedInstancesListingResultResponseTypeDef = TypedDict(
    "CancelReservedInstancesListingResultResponseTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSpotFleetRequestsErrorItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorItemTypeDef",
    {
        "Error": "CancelSpotFleetRequestsErrorTypeDef",
        "SpotFleetRequestId": str,
    },
    total=False,
)

CancelSpotFleetRequestsErrorTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorTypeDef",
    {
        "Code": CancelBatchErrorCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredCancelSpotFleetRequestsRequestTypeDef = TypedDict(
    "_RequiredCancelSpotFleetRequestsRequestTypeDef",
    {
        "SpotFleetRequestIds": List[str],
        "TerminateInstances": bool,
    },
)
_OptionalCancelSpotFleetRequestsRequestTypeDef = TypedDict(
    "_OptionalCancelSpotFleetRequestsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CancelSpotFleetRequestsRequestTypeDef(
    _RequiredCancelSpotFleetRequestsRequestTypeDef, _OptionalCancelSpotFleetRequestsRequestTypeDef
):
    pass


CancelSpotFleetRequestsResponseResponseTypeDef = TypedDict(
    "CancelSpotFleetRequestsResponseResponseTypeDef",
    {
        "SuccessfulFleetRequests": List["CancelSpotFleetRequestsSuccessItemTypeDef"],
        "UnsuccessfulFleetRequests": List["CancelSpotFleetRequestsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSpotFleetRequestsSuccessItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    {
        "CurrentSpotFleetRequestState": BatchStateType,
        "PreviousSpotFleetRequestState": BatchStateType,
        "SpotFleetRequestId": str,
    },
    total=False,
)

_RequiredCancelSpotInstanceRequestsRequestTypeDef = TypedDict(
    "_RequiredCancelSpotInstanceRequestsRequestTypeDef",
    {
        "SpotInstanceRequestIds": List[str],
    },
)
_OptionalCancelSpotInstanceRequestsRequestTypeDef = TypedDict(
    "_OptionalCancelSpotInstanceRequestsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CancelSpotInstanceRequestsRequestTypeDef(
    _RequiredCancelSpotInstanceRequestsRequestTypeDef,
    _OptionalCancelSpotInstanceRequestsRequestTypeDef,
):
    pass


CancelSpotInstanceRequestsResultResponseTypeDef = TypedDict(
    "CancelSpotInstanceRequestsResultResponseTypeDef",
    {
        "CancelledSpotInstanceRequests": List["CancelledSpotInstanceRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelledSpotInstanceRequestTypeDef = TypedDict(
    "CancelledSpotInstanceRequestTypeDef",
    {
        "SpotInstanceRequestId": str,
        "State": CancelSpotInstanceRequestStateType,
    },
    total=False,
)

CapacityReservationGroupTypeDef = TypedDict(
    "CapacityReservationGroupTypeDef",
    {
        "GroupArn": str,
        "OwnerId": str,
    },
    total=False,
)

CapacityReservationOptionsRequestTypeDef = TypedDict(
    "CapacityReservationOptionsRequestTypeDef",
    {
        "UsageStrategy": Literal["use-capacity-reservations-first"],
    },
    total=False,
)

CapacityReservationOptionsTypeDef = TypedDict(
    "CapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": Literal["use-capacity-reservations-first"],
    },
    total=False,
)

CapacityReservationSpecificationResponseTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
    },
    total=False,
)

CapacityReservationSpecificationTypeDef = TypedDict(
    "CapacityReservationSpecificationTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetTypeDef",
    },
    total=False,
)

CapacityReservationTargetResponseTypeDef = TypedDict(
    "CapacityReservationTargetResponseTypeDef",
    {
        "CapacityReservationId": str,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

CapacityReservationTargetTypeDef = TypedDict(
    "CapacityReservationTargetTypeDef",
    {
        "CapacityReservationId": str,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

CapacityReservationTypeDef = TypedDict(
    "CapacityReservationTypeDef",
    {
        "CapacityReservationId": str,
        "OwnerId": str,
        "CapacityReservationArn": str,
        "AvailabilityZoneId": str,
        "InstanceType": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "AvailabilityZone": str,
        "Tenancy": CapacityReservationTenancyType,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "EbsOptimized": bool,
        "EphemeralStorage": bool,
        "State": CapacityReservationStateType,
        "StartDate": datetime,
        "EndDate": datetime,
        "EndDateType": EndDateTypeType,
        "InstanceMatchCriteria": InstanceMatchCriteriaType,
        "CreateDate": datetime,
        "Tags": List["TagTypeDef"],
        "OutpostArn": str,
    },
    total=False,
)

CarrierGatewayTypeDef = TypedDict(
    "CarrierGatewayTypeDef",
    {
        "CarrierGatewayId": str,
        "VpcId": str,
        "State": CarrierGatewayStateType,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CertificateAuthenticationRequestTypeDef = TypedDict(
    "CertificateAuthenticationRequestTypeDef",
    {
        "ClientRootCertificateChainArn": str,
    },
    total=False,
)

CertificateAuthenticationTypeDef = TypedDict(
    "CertificateAuthenticationTypeDef",
    {
        "ClientRootCertificateChain": str,
    },
    total=False,
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)

CidrBlockTypeDef = TypedDict(
    "CidrBlockTypeDef",
    {
        "CidrBlock": str,
    },
    total=False,
)

ClassicLinkDnsSupportTypeDef = TypedDict(
    "ClassicLinkDnsSupportTypeDef",
    {
        "ClassicLinkDnsSupported": bool,
        "VpcId": str,
    },
    total=False,
)

ClassicLinkInstanceTypeDef = TypedDict(
    "ClassicLinkInstanceTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "InstanceId": str,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

ClassicLoadBalancerTypeDef = TypedDict(
    "ClassicLoadBalancerTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ClassicLoadBalancersConfigTypeDef = TypedDict(
    "ClassicLoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancers": List["ClassicLoadBalancerTypeDef"],
    },
    total=False,
)

ClientCertificateRevocationListStatusTypeDef = TypedDict(
    "ClientCertificateRevocationListStatusTypeDef",
    {
        "Code": ClientCertificateRevocationListStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientConnectOptionsTypeDef = TypedDict(
    "ClientConnectOptionsTypeDef",
    {
        "Enabled": bool,
        "LambdaFunctionArn": str,
    },
    total=False,
)

ClientConnectResponseOptionsTypeDef = TypedDict(
    "ClientConnectResponseOptionsTypeDef",
    {
        "Enabled": bool,
        "LambdaFunctionArn": str,
        "Status": "ClientVpnEndpointAttributeStatusTypeDef",
    },
    total=False,
)

ClientDataTypeDef = TypedDict(
    "ClientDataTypeDef",
    {
        "Comment": str,
        "UploadEnd": Union[datetime, str],
        "UploadSize": float,
        "UploadStart": Union[datetime, str],
    },
    total=False,
)

ClientVpnAuthenticationRequestTypeDef = TypedDict(
    "ClientVpnAuthenticationRequestTypeDef",
    {
        "Type": ClientVpnAuthenticationTypeType,
        "ActiveDirectory": "DirectoryServiceAuthenticationRequestTypeDef",
        "MutualAuthentication": "CertificateAuthenticationRequestTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationRequestTypeDef",
    },
    total=False,
)

ClientVpnAuthenticationTypeDef = TypedDict(
    "ClientVpnAuthenticationTypeDef",
    {
        "Type": ClientVpnAuthenticationTypeType,
        "ActiveDirectory": "DirectoryServiceAuthenticationTypeDef",
        "MutualAuthentication": "CertificateAuthenticationTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationTypeDef",
    },
    total=False,
)

ClientVpnAuthorizationRuleStatusTypeDef = TypedDict(
    "ClientVpnAuthorizationRuleStatusTypeDef",
    {
        "Code": ClientVpnAuthorizationRuleStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnConnectionStatusTypeDef = TypedDict(
    "ClientVpnConnectionStatusTypeDef",
    {
        "Code": ClientVpnConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnConnectionTypeDef = TypedDict(
    "ClientVpnConnectionTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Timestamp": str,
        "ConnectionId": str,
        "Username": str,
        "ConnectionEstablishedTime": str,
        "IngressBytes": str,
        "EgressBytes": str,
        "IngressPackets": str,
        "EgressPackets": str,
        "ClientIp": str,
        "CommonName": str,
        "Status": "ClientVpnConnectionStatusTypeDef",
        "ConnectionEndTime": str,
        "PostureComplianceStatuses": List[str],
    },
    total=False,
)

ClientVpnEndpointAttributeStatusTypeDef = TypedDict(
    "ClientVpnEndpointAttributeStatusTypeDef",
    {
        "Code": ClientVpnEndpointAttributeStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnEndpointStatusTypeDef = TypedDict(
    "ClientVpnEndpointStatusTypeDef",
    {
        "Code": ClientVpnEndpointStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnEndpointTypeDef = TypedDict(
    "ClientVpnEndpointTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Description": str,
        "Status": "ClientVpnEndpointStatusTypeDef",
        "CreationTime": str,
        "DeletionTime": str,
        "DnsName": str,
        "ClientCidrBlock": str,
        "DnsServers": List[str],
        "SplitTunnel": bool,
        "VpnProtocol": Literal["openvpn"],
        "TransportProtocol": TransportProtocolType,
        "VpnPort": int,
        "AssociatedTargetNetworks": List["AssociatedTargetNetworkTypeDef"],
        "ServerCertificateArn": str,
        "AuthenticationOptions": List["ClientVpnAuthenticationTypeDef"],
        "ConnectionLogOptions": "ConnectionLogResponseOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "SelfServicePortalUrl": str,
        "ClientConnectOptions": "ClientConnectResponseOptionsTypeDef",
    },
    total=False,
)

ClientVpnRouteStatusTypeDef = TypedDict(
    "ClientVpnRouteStatusTypeDef",
    {
        "Code": ClientVpnRouteStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnRouteTypeDef = TypedDict(
    "ClientVpnRouteTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidr": str,
        "TargetSubnet": str,
        "Type": str,
        "Origin": str,
        "Status": "ClientVpnRouteStatusTypeDef",
        "Description": str,
    },
    total=False,
)

CoipAddressUsageTypeDef = TypedDict(
    "CoipAddressUsageTypeDef",
    {
        "AllocationId": str,
        "AwsAccountId": str,
        "AwsService": str,
        "CoIp": str,
    },
    total=False,
)

CoipPoolTypeDef = TypedDict(
    "CoipPoolTypeDef",
    {
        "PoolId": str,
        "PoolCidrs": List[str],
        "LocalGatewayRouteTableId": str,
        "Tags": List["TagTypeDef"],
        "PoolArn": str,
    },
    total=False,
)

_RequiredConfirmProductInstanceRequestTypeDef = TypedDict(
    "_RequiredConfirmProductInstanceRequestTypeDef",
    {
        "InstanceId": str,
        "ProductCode": str,
    },
)
_OptionalConfirmProductInstanceRequestTypeDef = TypedDict(
    "_OptionalConfirmProductInstanceRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ConfirmProductInstanceRequestTypeDef(
    _RequiredConfirmProductInstanceRequestTypeDef, _OptionalConfirmProductInstanceRequestTypeDef
):
    pass


ConfirmProductInstanceResultResponseTypeDef = TypedDict(
    "ConfirmProductInstanceResultResponseTypeDef",
    {
        "OwnerId": str,
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionLogOptionsTypeDef = TypedDict(
    "ConnectionLogOptionsTypeDef",
    {
        "Enabled": bool,
        "CloudwatchLogGroup": str,
        "CloudwatchLogStream": str,
    },
    total=False,
)

ConnectionLogResponseOptionsTypeDef = TypedDict(
    "ConnectionLogResponseOptionsTypeDef",
    {
        "Enabled": bool,
        "CloudwatchLogGroup": str,
        "CloudwatchLogStream": str,
    },
    total=False,
)

ConnectionNotificationTypeDef = TypedDict(
    "ConnectionNotificationTypeDef",
    {
        "ConnectionNotificationId": str,
        "ServiceId": str,
        "VpcEndpointId": str,
        "ConnectionNotificationType": Literal["Topic"],
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
        "ConnectionNotificationState": ConnectionNotificationStateType,
    },
    total=False,
)

ConversionTaskTypeDef = TypedDict(
    "ConversionTaskTypeDef",
    {
        "ConversionTaskId": str,
        "ExpirationTime": str,
        "ImportInstance": "ImportInstanceTaskDetailsTypeDef",
        "ImportVolume": "ImportVolumeTaskDetailsTypeDef",
        "State": ConversionTaskStateType,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredCopyFpgaImageRequestTypeDef = TypedDict(
    "_RequiredCopyFpgaImageRequestTypeDef",
    {
        "SourceFpgaImageId": str,
        "SourceRegion": str,
    },
)
_OptionalCopyFpgaImageRequestTypeDef = TypedDict(
    "_OptionalCopyFpgaImageRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "Name": str,
        "ClientToken": str,
    },
    total=False,
)


class CopyFpgaImageRequestTypeDef(
    _RequiredCopyFpgaImageRequestTypeDef, _OptionalCopyFpgaImageRequestTypeDef
):
    pass


CopyFpgaImageResultResponseTypeDef = TypedDict(
    "CopyFpgaImageResultResponseTypeDef",
    {
        "FpgaImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyImageRequestTypeDef = TypedDict(
    "_RequiredCopyImageRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
    },
)
_OptionalCopyImageRequestTypeDef = TypedDict(
    "_OptionalCopyImageRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DestinationOutpostArn": str,
        "DryRun": bool,
    },
    total=False,
)


class CopyImageRequestTypeDef(_RequiredCopyImageRequestTypeDef, _OptionalCopyImageRequestTypeDef):
    pass


CopyImageResultResponseTypeDef = TypedDict(
    "CopyImageResultResponseTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopySnapshotRequestSnapshotTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestSnapshotTypeDef",
    {
        "SourceRegion": str,
    },
)
_OptionalCopySnapshotRequestSnapshotTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestSnapshotTypeDef",
    {
        "Description": str,
        "DestinationOutpostArn": str,
        "DestinationRegion": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "PresignedUrl": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CopySnapshotRequestSnapshotTypeDef(
    _RequiredCopySnapshotRequestSnapshotTypeDef, _OptionalCopySnapshotRequestSnapshotTypeDef
):
    pass


_RequiredCopySnapshotRequestTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestTypeDef",
    {
        "SourceRegion": str,
        "SourceSnapshotId": str,
    },
)
_OptionalCopySnapshotRequestTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestTypeDef",
    {
        "Description": str,
        "DestinationOutpostArn": str,
        "DestinationRegion": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "PresignedUrl": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CopySnapshotRequestTypeDef(
    _RequiredCopySnapshotRequestTypeDef, _OptionalCopySnapshotRequestTypeDef
):
    pass


CopySnapshotResultResponseTypeDef = TypedDict(
    "CopySnapshotResultResponseTypeDef",
    {
        "SnapshotId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CpuOptionsRequestTypeDef = TypedDict(
    "CpuOptionsRequestTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
    },
    total=False,
)

CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
    },
    total=False,
)

_RequiredCreateCapacityReservationRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityReservationRequestTypeDef",
    {
        "InstanceType": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "InstanceCount": int,
    },
)
_OptionalCreateCapacityReservationRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityReservationRequestTypeDef",
    {
        "ClientToken": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tenancy": CapacityReservationTenancyType,
        "EbsOptimized": bool,
        "EphemeralStorage": bool,
        "EndDate": Union[datetime, str],
        "EndDateType": EndDateTypeType,
        "InstanceMatchCriteria": InstanceMatchCriteriaType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "OutpostArn": str,
    },
    total=False,
)


class CreateCapacityReservationRequestTypeDef(
    _RequiredCreateCapacityReservationRequestTypeDef,
    _OptionalCreateCapacityReservationRequestTypeDef,
):
    pass


CreateCapacityReservationResultResponseTypeDef = TypedDict(
    "CreateCapacityReservationResultResponseTypeDef",
    {
        "CapacityReservation": "CapacityReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCarrierGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateCarrierGatewayRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateCarrierGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateCarrierGatewayRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)


class CreateCarrierGatewayRequestTypeDef(
    _RequiredCreateCarrierGatewayRequestTypeDef, _OptionalCreateCarrierGatewayRequestTypeDef
):
    pass


CreateCarrierGatewayResultResponseTypeDef = TypedDict(
    "CreateCarrierGatewayResultResponseTypeDef",
    {
        "CarrierGateway": "CarrierGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClientVpnEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateClientVpnEndpointRequestTypeDef",
    {
        "ClientCidrBlock": str,
        "ServerCertificateArn": str,
        "AuthenticationOptions": List["ClientVpnAuthenticationRequestTypeDef"],
        "ConnectionLogOptions": "ConnectionLogOptionsTypeDef",
    },
)
_OptionalCreateClientVpnEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateClientVpnEndpointRequestTypeDef",
    {
        "DnsServers": List[str],
        "TransportProtocol": TransportProtocolType,
        "VpnPort": int,
        "Description": str,
        "SplitTunnel": bool,
        "DryRun": bool,
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "SelfServicePortal": SelfServicePortalType,
        "ClientConnectOptions": "ClientConnectOptionsTypeDef",
    },
    total=False,
)


class CreateClientVpnEndpointRequestTypeDef(
    _RequiredCreateClientVpnEndpointRequestTypeDef, _OptionalCreateClientVpnEndpointRequestTypeDef
):
    pass


CreateClientVpnEndpointResultResponseTypeDef = TypedDict(
    "CreateClientVpnEndpointResultResponseTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Status": "ClientVpnEndpointStatusTypeDef",
        "DnsName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClientVpnRouteRequestTypeDef = TypedDict(
    "_RequiredCreateClientVpnRouteRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
        "TargetVpcSubnetId": str,
    },
)
_OptionalCreateClientVpnRouteRequestTypeDef = TypedDict(
    "_OptionalCreateClientVpnRouteRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)


class CreateClientVpnRouteRequestTypeDef(
    _RequiredCreateClientVpnRouteRequestTypeDef, _OptionalCreateClientVpnRouteRequestTypeDef
):
    pass


CreateClientVpnRouteResultResponseTypeDef = TypedDict(
    "CreateClientVpnRouteResultResponseTypeDef",
    {
        "Status": "ClientVpnRouteStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomerGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateCustomerGatewayRequestTypeDef",
    {
        "BgpAsn": int,
        "Type": Literal["ipsec.1"],
    },
)
_OptionalCreateCustomerGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateCustomerGatewayRequestTypeDef",
    {
        "PublicIp": str,
        "CertificateArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DeviceName": str,
        "DryRun": bool,
    },
    total=False,
)


class CreateCustomerGatewayRequestTypeDef(
    _RequiredCreateCustomerGatewayRequestTypeDef, _OptionalCreateCustomerGatewayRequestTypeDef
):
    pass


CreateCustomerGatewayResultResponseTypeDef = TypedDict(
    "CreateCustomerGatewayResultResponseTypeDef",
    {
        "CustomerGateway": "CustomerGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDefaultSubnetRequestTypeDef = TypedDict(
    "_RequiredCreateDefaultSubnetRequestTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalCreateDefaultSubnetRequestTypeDef = TypedDict(
    "_OptionalCreateDefaultSubnetRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateDefaultSubnetRequestTypeDef(
    _RequiredCreateDefaultSubnetRequestTypeDef, _OptionalCreateDefaultSubnetRequestTypeDef
):
    pass


CreateDefaultSubnetResultResponseTypeDef = TypedDict(
    "CreateDefaultSubnetResultResponseTypeDef",
    {
        "Subnet": "SubnetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDefaultVpcRequestTypeDef = TypedDict(
    "CreateDefaultVpcRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

CreateDefaultVpcResultResponseTypeDef = TypedDict(
    "CreateDefaultVpcResultResponseTypeDef",
    {
        "Vpc": "VpcTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDhcpOptionsRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateDhcpOptionsRequestServiceResourceTypeDef",
    {
        "DhcpConfigurations": List["NewDhcpConfigurationTypeDef"],
    },
)
_OptionalCreateDhcpOptionsRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateDhcpOptionsRequestServiceResourceTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateDhcpOptionsRequestServiceResourceTypeDef(
    _RequiredCreateDhcpOptionsRequestServiceResourceTypeDef,
    _OptionalCreateDhcpOptionsRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateDhcpOptionsRequestTypeDef = TypedDict(
    "_RequiredCreateDhcpOptionsRequestTypeDef",
    {
        "DhcpConfigurations": List["NewDhcpConfigurationTypeDef"],
    },
)
_OptionalCreateDhcpOptionsRequestTypeDef = TypedDict(
    "_OptionalCreateDhcpOptionsRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateDhcpOptionsRequestTypeDef(
    _RequiredCreateDhcpOptionsRequestTypeDef, _OptionalCreateDhcpOptionsRequestTypeDef
):
    pass


CreateDhcpOptionsResultResponseTypeDef = TypedDict(
    "CreateDhcpOptionsResultResponseTypeDef",
    {
        "DhcpOptions": "DhcpOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEgressOnlyInternetGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateEgressOnlyInternetGatewayRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateEgressOnlyInternetGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateEgressOnlyInternetGatewayRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateEgressOnlyInternetGatewayRequestTypeDef(
    _RequiredCreateEgressOnlyInternetGatewayRequestTypeDef,
    _OptionalCreateEgressOnlyInternetGatewayRequestTypeDef,
):
    pass


CreateEgressOnlyInternetGatewayResultResponseTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayResultResponseTypeDef",
    {
        "ClientToken": str,
        "EgressOnlyInternetGateway": "EgressOnlyInternetGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetErrorTypeDef = TypedDict(
    "CreateFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

CreateFleetInstanceTypeDef = TypedDict(
    "CreateFleetInstanceTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "InstanceIds": List[str],
        "InstanceType": InstanceTypeType,
        "Platform": Literal["Windows"],
    },
    total=False,
)

_RequiredCreateFleetRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestTypeDef",
    {
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigRequestTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationRequestTypeDef",
    },
)
_OptionalCreateFleetRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "SpotOptions": "SpotOptionsRequestTypeDef",
        "OnDemandOptions": "OnDemandOptionsRequestTypeDef",
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicyType,
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetTypeType,
        "ValidFrom": Union[datetime, str],
        "ValidUntil": Union[datetime, str],
        "ReplaceUnhealthyInstances": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateFleetRequestTypeDef(
    _RequiredCreateFleetRequestTypeDef, _OptionalCreateFleetRequestTypeDef
):
    pass


CreateFleetResultResponseTypeDef = TypedDict(
    "CreateFleetResultResponseTypeDef",
    {
        "FleetId": str,
        "Errors": List["CreateFleetErrorTypeDef"],
        "Instances": List["CreateFleetInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowLogsRequestTypeDef = TypedDict(
    "_RequiredCreateFlowLogsRequestTypeDef",
    {
        "ResourceIds": List[str],
        "ResourceType": FlowLogsResourceTypeType,
        "TrafficType": TrafficTypeType,
    },
)
_OptionalCreateFlowLogsRequestTypeDef = TypedDict(
    "_OptionalCreateFlowLogsRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "DeliverLogsPermissionArn": str,
        "LogGroupName": str,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": str,
        "LogFormat": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "MaxAggregationInterval": int,
    },
    total=False,
)


class CreateFlowLogsRequestTypeDef(
    _RequiredCreateFlowLogsRequestTypeDef, _OptionalCreateFlowLogsRequestTypeDef
):
    pass


CreateFlowLogsResultResponseTypeDef = TypedDict(
    "CreateFlowLogsResultResponseTypeDef",
    {
        "ClientToken": str,
        "FlowLogIds": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFpgaImageRequestTypeDef = TypedDict(
    "_RequiredCreateFpgaImageRequestTypeDef",
    {
        "InputStorageLocation": "StorageLocationTypeDef",
    },
)
_OptionalCreateFpgaImageRequestTypeDef = TypedDict(
    "_OptionalCreateFpgaImageRequestTypeDef",
    {
        "DryRun": bool,
        "LogsStorageLocation": "StorageLocationTypeDef",
        "Description": str,
        "Name": str,
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateFpgaImageRequestTypeDef(
    _RequiredCreateFpgaImageRequestTypeDef, _OptionalCreateFpgaImageRequestTypeDef
):
    pass


CreateFpgaImageResultResponseTypeDef = TypedDict(
    "CreateFpgaImageResultResponseTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRequestInstanceTypeDef = TypedDict(
    "_RequiredCreateImageRequestInstanceTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateImageRequestInstanceTypeDef = TypedDict(
    "_OptionalCreateImageRequestInstanceTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "NoReboot": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateImageRequestInstanceTypeDef(
    _RequiredCreateImageRequestInstanceTypeDef, _OptionalCreateImageRequestInstanceTypeDef
):
    pass


_RequiredCreateImageRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
    },
)
_OptionalCreateImageRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "NoReboot": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateImageRequestTypeDef(
    _RequiredCreateImageRequestTypeDef, _OptionalCreateImageRequestTypeDef
):
    pass


CreateImageResultResponseTypeDef = TypedDict(
    "CreateImageResultResponseTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceExportTaskRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceExportTaskRequestTypeDef",
    {
        "ExportToS3Task": "ExportToS3TaskSpecificationTypeDef",
        "InstanceId": str,
        "TargetEnvironment": ExportEnvironmentType,
    },
)
_OptionalCreateInstanceExportTaskRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceExportTaskRequestTypeDef",
    {
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateInstanceExportTaskRequestTypeDef(
    _RequiredCreateInstanceExportTaskRequestTypeDef, _OptionalCreateInstanceExportTaskRequestTypeDef
):
    pass


CreateInstanceExportTaskResultResponseTypeDef = TypedDict(
    "CreateInstanceExportTaskResultResponseTypeDef",
    {
        "ExportTask": "ExportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInternetGatewayRequestServiceResourceTypeDef = TypedDict(
    "CreateInternetGatewayRequestServiceResourceTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

CreateInternetGatewayRequestTypeDef = TypedDict(
    "CreateInternetGatewayRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

CreateInternetGatewayResultResponseTypeDef = TypedDict(
    "CreateInternetGatewayResultResponseTypeDef",
    {
        "InternetGateway": "InternetGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateKeyPairRequestServiceResourceTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalCreateKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateKeyPairRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateKeyPairRequestServiceResourceTypeDef(
    _RequiredCreateKeyPairRequestServiceResourceTypeDef,
    _OptionalCreateKeyPairRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateKeyPairRequestTypeDef = TypedDict(
    "_RequiredCreateKeyPairRequestTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalCreateKeyPairRequestTypeDef = TypedDict(
    "_OptionalCreateKeyPairRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateKeyPairRequestTypeDef(
    _RequiredCreateKeyPairRequestTypeDef, _OptionalCreateKeyPairRequestTypeDef
):
    pass


_RequiredCreateLaunchTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchTemplateRequestTypeDef",
    {
        "LaunchTemplateName": str,
        "LaunchTemplateData": "RequestLaunchTemplateDataTypeDef",
    },
)
_OptionalCreateLaunchTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchTemplateRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "VersionDescription": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateLaunchTemplateRequestTypeDef(
    _RequiredCreateLaunchTemplateRequestTypeDef, _OptionalCreateLaunchTemplateRequestTypeDef
):
    pass


CreateLaunchTemplateResultResponseTypeDef = TypedDict(
    "CreateLaunchTemplateResultResponseTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "Warning": "ValidationWarningTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLaunchTemplateVersionRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchTemplateVersionRequestTypeDef",
    {
        "LaunchTemplateData": "RequestLaunchTemplateDataTypeDef",
    },
)
_OptionalCreateLaunchTemplateVersionRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchTemplateVersionRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "SourceVersion": str,
        "VersionDescription": str,
    },
    total=False,
)


class CreateLaunchTemplateVersionRequestTypeDef(
    _RequiredCreateLaunchTemplateVersionRequestTypeDef,
    _OptionalCreateLaunchTemplateVersionRequestTypeDef,
):
    pass


CreateLaunchTemplateVersionResultResponseTypeDef = TypedDict(
    "CreateLaunchTemplateVersionResultResponseTypeDef",
    {
        "LaunchTemplateVersion": "LaunchTemplateVersionTypeDef",
        "Warning": "ValidationWarningTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocalGatewayRouteRequestTypeDef = TypedDict(
    "_RequiredCreateLocalGatewayRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
    },
)
_OptionalCreateLocalGatewayRouteRequestTypeDef = TypedDict(
    "_OptionalCreateLocalGatewayRouteRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateLocalGatewayRouteRequestTypeDef(
    _RequiredCreateLocalGatewayRouteRequestTypeDef, _OptionalCreateLocalGatewayRouteRequestTypeDef
):
    pass


CreateLocalGatewayRouteResultResponseTypeDef = TypedDict(
    "CreateLocalGatewayRouteResultResponseTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocalGatewayRouteTableVpcAssociationRequestTypeDef = TypedDict(
    "_RequiredCreateLocalGatewayRouteTableVpcAssociationRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "VpcId": str,
    },
)
_OptionalCreateLocalGatewayRouteTableVpcAssociationRequestTypeDef = TypedDict(
    "_OptionalCreateLocalGatewayRouteTableVpcAssociationRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateLocalGatewayRouteTableVpcAssociationRequestTypeDef(
    _RequiredCreateLocalGatewayRouteTableVpcAssociationRequestTypeDef,
    _OptionalCreateLocalGatewayRouteTableVpcAssociationRequestTypeDef,
):
    pass


CreateLocalGatewayRouteTableVpcAssociationResultResponseTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationResultResponseTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateManagedPrefixListRequestTypeDef = TypedDict(
    "_RequiredCreateManagedPrefixListRequestTypeDef",
    {
        "PrefixListName": str,
        "MaxEntries": int,
        "AddressFamily": str,
    },
)
_OptionalCreateManagedPrefixListRequestTypeDef = TypedDict(
    "_OptionalCreateManagedPrefixListRequestTypeDef",
    {
        "DryRun": bool,
        "Entries": List["AddPrefixListEntryTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)


class CreateManagedPrefixListRequestTypeDef(
    _RequiredCreateManagedPrefixListRequestTypeDef, _OptionalCreateManagedPrefixListRequestTypeDef
):
    pass


CreateManagedPrefixListResultResponseTypeDef = TypedDict(
    "CreateManagedPrefixListResultResponseTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNatGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateNatGatewayRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateNatGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateNatGatewayRequestTypeDef",
    {
        "AllocationId": str,
        "ClientToken": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ConnectivityType": ConnectivityTypeType,
    },
    total=False,
)


class CreateNatGatewayRequestTypeDef(
    _RequiredCreateNatGatewayRequestTypeDef, _OptionalCreateNatGatewayRequestTypeDef
):
    pass


CreateNatGatewayResultResponseTypeDef = TypedDict(
    "CreateNatGatewayResultResponseTypeDef",
    {
        "ClientToken": str,
        "NatGateway": "NatGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_RequiredCreateNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalCreateNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_OptionalCreateNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)


class CreateNetworkAclEntryRequestNetworkAclTypeDef(
    _RequiredCreateNetworkAclEntryRequestNetworkAclTypeDef,
    _OptionalCreateNetworkAclEntryRequestNetworkAclTypeDef,
):
    pass


_RequiredCreateNetworkAclEntryRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkAclEntryRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalCreateNetworkAclEntryRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkAclEntryRequestTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)


class CreateNetworkAclEntryRequestTypeDef(
    _RequiredCreateNetworkAclEntryRequestTypeDef, _OptionalCreateNetworkAclEntryRequestTypeDef
):
    pass


_RequiredCreateNetworkAclRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateNetworkAclRequestServiceResourceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateNetworkAclRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateNetworkAclRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateNetworkAclRequestServiceResourceTypeDef(
    _RequiredCreateNetworkAclRequestServiceResourceTypeDef,
    _OptionalCreateNetworkAclRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateNetworkAclRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkAclRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateNetworkAclRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkAclRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateNetworkAclRequestTypeDef(
    _RequiredCreateNetworkAclRequestTypeDef, _OptionalCreateNetworkAclRequestTypeDef
):
    pass


CreateNetworkAclRequestVpcTypeDef = TypedDict(
    "CreateNetworkAclRequestVpcTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateNetworkAclResultResponseTypeDef = TypedDict(
    "CreateNetworkAclResultResponseTypeDef",
    {
        "NetworkAcl": "NetworkAclTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInsightsPathRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInsightsPathRequestTypeDef",
    {
        "Source": str,
        "Destination": str,
        "Protocol": ProtocolType,
        "ClientToken": str,
    },
)
_OptionalCreateNetworkInsightsPathRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInsightsPathRequestTypeDef",
    {
        "SourceIp": str,
        "DestinationIp": str,
        "DestinationPort": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateNetworkInsightsPathRequestTypeDef(
    _RequiredCreateNetworkInsightsPathRequestTypeDef,
    _OptionalCreateNetworkInsightsPathRequestTypeDef,
):
    pass


CreateNetworkInsightsPathResultResponseTypeDef = TypedDict(
    "CreateNetworkInsightsPathResultResponseTypeDef",
    {
        "NetworkInsightsPath": "NetworkInsightsPathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInterfacePermissionRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInterfacePermissionRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Permission": InterfacePermissionTypeType,
    },
)
_OptionalCreateNetworkInterfacePermissionRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInterfacePermissionRequestTypeDef",
    {
        "AwsAccountId": str,
        "AwsService": str,
        "DryRun": bool,
    },
    total=False,
)


class CreateNetworkInterfacePermissionRequestTypeDef(
    _RequiredCreateNetworkInterfacePermissionRequestTypeDef,
    _OptionalCreateNetworkInterfacePermissionRequestTypeDef,
):
    pass


CreateNetworkInterfacePermissionResultResponseTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionResultResponseTypeDef",
    {
        "InterfacePermission": "NetworkInterfacePermissionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInterfaceRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateNetworkInterfaceRequestServiceResourceTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateNetworkInterfaceRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateNetworkInterfaceRequestServiceResourceTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "InterfaceType": NetworkInterfaceCreationTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)


class CreateNetworkInterfaceRequestServiceResourceTypeDef(
    _RequiredCreateNetworkInterfaceRequestServiceResourceTypeDef,
    _OptionalCreateNetworkInterfaceRequestServiceResourceTypeDef,
):
    pass


CreateNetworkInterfaceRequestSubnetTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestSubnetTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "InterfaceType": NetworkInterfaceCreationTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

_RequiredCreateNetworkInterfaceRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInterfaceRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateNetworkInterfaceRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInterfaceRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "InterfaceType": NetworkInterfaceCreationTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)


class CreateNetworkInterfaceRequestTypeDef(
    _RequiredCreateNetworkInterfaceRequestTypeDef, _OptionalCreateNetworkInterfaceRequestTypeDef
):
    pass


CreateNetworkInterfaceResultResponseTypeDef = TypedDict(
    "CreateNetworkInterfaceResultResponseTypeDef",
    {
        "NetworkInterface": "NetworkInterfaceTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlacementGroupRequestServiceResourceTypeDef = TypedDict(
    "CreatePlacementGroupRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "GroupName": str,
        "Strategy": PlacementStrategyType,
        "PartitionCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreatePlacementGroupRequestTypeDef = TypedDict(
    "CreatePlacementGroupRequestTypeDef",
    {
        "DryRun": bool,
        "GroupName": str,
        "Strategy": PlacementStrategyType,
        "PartitionCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreatePlacementGroupResultResponseTypeDef = TypedDict(
    "CreatePlacementGroupResultResponseTypeDef",
    {
        "PlacementGroup": "PlacementGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplaceRootVolumeTaskRequestTypeDef = TypedDict(
    "_RequiredCreateReplaceRootVolumeTaskRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalCreateReplaceRootVolumeTaskRequestTypeDef = TypedDict(
    "_OptionalCreateReplaceRootVolumeTaskRequestTypeDef",
    {
        "SnapshotId": str,
        "ClientToken": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateReplaceRootVolumeTaskRequestTypeDef(
    _RequiredCreateReplaceRootVolumeTaskRequestTypeDef,
    _OptionalCreateReplaceRootVolumeTaskRequestTypeDef,
):
    pass


CreateReplaceRootVolumeTaskResultResponseTypeDef = TypedDict(
    "CreateReplaceRootVolumeTaskResultResponseTypeDef",
    {
        "ReplaceRootVolumeTask": "ReplaceRootVolumeTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReservedInstancesListingRequestTypeDef = TypedDict(
    "CreateReservedInstancesListingRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceCount": int,
        "PriceSchedules": List["PriceScheduleSpecificationTypeDef"],
        "ReservedInstancesId": str,
    },
)

CreateReservedInstancesListingResultResponseTypeDef = TypedDict(
    "CreateReservedInstancesListingResultResponseTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRestoreImageTaskRequestTypeDef = TypedDict(
    "_RequiredCreateRestoreImageTaskRequestTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
    },
)
_OptionalCreateRestoreImageTaskRequestTypeDef = TypedDict(
    "_OptionalCreateRestoreImageTaskRequestTypeDef",
    {
        "Name": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateRestoreImageTaskRequestTypeDef(
    _RequiredCreateRestoreImageTaskRequestTypeDef, _OptionalCreateRestoreImageTaskRequestTypeDef
):
    pass


CreateRestoreImageTaskResultResponseTypeDef = TypedDict(
    "CreateRestoreImageTaskResultResponseTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRouteRequestRouteTableTypeDef = TypedDict(
    "CreateRouteRequestRouteTableTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

_RequiredCreateRouteRequestTypeDef = TypedDict(
    "_RequiredCreateRouteRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalCreateRouteRequestTypeDef = TypedDict(
    "_OptionalCreateRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)


class CreateRouteRequestTypeDef(
    _RequiredCreateRouteRequestTypeDef, _OptionalCreateRouteRequestTypeDef
):
    pass


CreateRouteResultResponseTypeDef = TypedDict(
    "CreateRouteResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateRouteTableRequestServiceResourceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateRouteTableRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateRouteTableRequestServiceResourceTypeDef(
    _RequiredCreateRouteTableRequestServiceResourceTypeDef,
    _OptionalCreateRouteTableRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateRouteTableRequestTypeDef = TypedDict(
    "_RequiredCreateRouteTableRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateRouteTableRequestTypeDef = TypedDict(
    "_OptionalCreateRouteTableRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateRouteTableRequestTypeDef(
    _RequiredCreateRouteTableRequestTypeDef, _OptionalCreateRouteTableRequestTypeDef
):
    pass


CreateRouteTableRequestVpcTypeDef = TypedDict(
    "CreateRouteTableRequestVpcTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateRouteTableResultResponseTypeDef = TypedDict(
    "CreateRouteTableResultResponseTypeDef",
    {
        "RouteTable": "RouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityGroupRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSecurityGroupRequestServiceResourceTypeDef",
    {
        "Description": str,
        "GroupName": str,
    },
)
_OptionalCreateSecurityGroupRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSecurityGroupRequestServiceResourceTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateSecurityGroupRequestServiceResourceTypeDef(
    _RequiredCreateSecurityGroupRequestServiceResourceTypeDef,
    _OptionalCreateSecurityGroupRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateSecurityGroupRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityGroupRequestTypeDef",
    {
        "Description": str,
        "GroupName": str,
    },
)
_OptionalCreateSecurityGroupRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityGroupRequestTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateSecurityGroupRequestTypeDef(
    _RequiredCreateSecurityGroupRequestTypeDef, _OptionalCreateSecurityGroupRequestTypeDef
):
    pass


_RequiredCreateSecurityGroupRequestVpcTypeDef = TypedDict(
    "_RequiredCreateSecurityGroupRequestVpcTypeDef",
    {
        "Description": str,
        "GroupName": str,
    },
)
_OptionalCreateSecurityGroupRequestVpcTypeDef = TypedDict(
    "_OptionalCreateSecurityGroupRequestVpcTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateSecurityGroupRequestVpcTypeDef(
    _RequiredCreateSecurityGroupRequestVpcTypeDef, _OptionalCreateSecurityGroupRequestVpcTypeDef
):
    pass


CreateSecurityGroupResultResponseTypeDef = TypedDict(
    "CreateSecurityGroupResultResponseTypeDef",
    {
        "GroupId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestServiceResourceTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalCreateSnapshotRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestServiceResourceTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateSnapshotRequestServiceResourceTypeDef(
    _RequiredCreateSnapshotRequestServiceResourceTypeDef,
    _OptionalCreateSnapshotRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalCreateSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateSnapshotRequestTypeDef(
    _RequiredCreateSnapshotRequestTypeDef, _OptionalCreateSnapshotRequestTypeDef
):
    pass


CreateSnapshotRequestVolumeTypeDef = TypedDict(
    "CreateSnapshotRequestVolumeTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

_RequiredCreateSnapshotsRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotsRequestTypeDef",
    {
        "InstanceSpecification": "InstanceSpecificationTypeDef",
    },
)
_OptionalCreateSnapshotsRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotsRequestTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "CopyTagsFromSource": Literal["volume"],
    },
    total=False,
)


class CreateSnapshotsRequestTypeDef(
    _RequiredCreateSnapshotsRequestTypeDef, _OptionalCreateSnapshotsRequestTypeDef
):
    pass


CreateSnapshotsResultResponseTypeDef = TypedDict(
    "CreateSnapshotsResultResponseTypeDef",
    {
        "Snapshots": List["SnapshotInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSpotDatafeedSubscriptionRequestTypeDef = TypedDict(
    "_RequiredCreateSpotDatafeedSubscriptionRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateSpotDatafeedSubscriptionRequestTypeDef = TypedDict(
    "_OptionalCreateSpotDatafeedSubscriptionRequestTypeDef",
    {
        "DryRun": bool,
        "Prefix": str,
    },
    total=False,
)


class CreateSpotDatafeedSubscriptionRequestTypeDef(
    _RequiredCreateSpotDatafeedSubscriptionRequestTypeDef,
    _OptionalCreateSpotDatafeedSubscriptionRequestTypeDef,
):
    pass


CreateSpotDatafeedSubscriptionResultResponseTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionResultResponseTypeDef",
    {
        "SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStoreImageTaskRequestTypeDef = TypedDict(
    "_RequiredCreateStoreImageTaskRequestTypeDef",
    {
        "ImageId": str,
        "Bucket": str,
    },
)
_OptionalCreateStoreImageTaskRequestTypeDef = TypedDict(
    "_OptionalCreateStoreImageTaskRequestTypeDef",
    {
        "S3ObjectTags": List["S3ObjectTagTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateStoreImageTaskRequestTypeDef(
    _RequiredCreateStoreImageTaskRequestTypeDef, _OptionalCreateStoreImageTaskRequestTypeDef
):
    pass


CreateStoreImageTaskResultResponseTypeDef = TypedDict(
    "CreateStoreImageTaskResultResponseTypeDef",
    {
        "ObjectKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubnetRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSubnetRequestServiceResourceTypeDef",
    {
        "CidrBlock": str,
        "VpcId": str,
    },
)
_OptionalCreateSubnetRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSubnetRequestServiceResourceTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Ipv6CidrBlock": str,
        "OutpostArn": str,
        "DryRun": bool,
    },
    total=False,
)


class CreateSubnetRequestServiceResourceTypeDef(
    _RequiredCreateSubnetRequestServiceResourceTypeDef,
    _OptionalCreateSubnetRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateSubnetRequestTypeDef = TypedDict(
    "_RequiredCreateSubnetRequestTypeDef",
    {
        "CidrBlock": str,
        "VpcId": str,
    },
)
_OptionalCreateSubnetRequestTypeDef = TypedDict(
    "_OptionalCreateSubnetRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Ipv6CidrBlock": str,
        "OutpostArn": str,
        "DryRun": bool,
    },
    total=False,
)


class CreateSubnetRequestTypeDef(
    _RequiredCreateSubnetRequestTypeDef, _OptionalCreateSubnetRequestTypeDef
):
    pass


_RequiredCreateSubnetRequestVpcTypeDef = TypedDict(
    "_RequiredCreateSubnetRequestVpcTypeDef",
    {
        "CidrBlock": str,
    },
)
_OptionalCreateSubnetRequestVpcTypeDef = TypedDict(
    "_OptionalCreateSubnetRequestVpcTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Ipv6CidrBlock": str,
        "OutpostArn": str,
        "DryRun": bool,
    },
    total=False,
)


class CreateSubnetRequestVpcTypeDef(
    _RequiredCreateSubnetRequestVpcTypeDef, _OptionalCreateSubnetRequestVpcTypeDef
):
    pass


CreateSubnetResultResponseTypeDef = TypedDict(
    "CreateSubnetResultResponseTypeDef",
    {
        "Subnet": "SubnetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTagsRequestDhcpOptionsTypeDef = TypedDict(
    "_RequiredCreateTagsRequestDhcpOptionsTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestDhcpOptionsTypeDef = TypedDict(
    "_OptionalCreateTagsRequestDhcpOptionsTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestDhcpOptionsTypeDef(
    _RequiredCreateTagsRequestDhcpOptionsTypeDef, _OptionalCreateTagsRequestDhcpOptionsTypeDef
):
    pass


_RequiredCreateTagsRequestImageTypeDef = TypedDict(
    "_RequiredCreateTagsRequestImageTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestImageTypeDef = TypedDict(
    "_OptionalCreateTagsRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestImageTypeDef(
    _RequiredCreateTagsRequestImageTypeDef, _OptionalCreateTagsRequestImageTypeDef
):
    pass


_RequiredCreateTagsRequestInstanceTypeDef = TypedDict(
    "_RequiredCreateTagsRequestInstanceTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestInstanceTypeDef = TypedDict(
    "_OptionalCreateTagsRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestInstanceTypeDef(
    _RequiredCreateTagsRequestInstanceTypeDef, _OptionalCreateTagsRequestInstanceTypeDef
):
    pass


_RequiredCreateTagsRequestInternetGatewayTypeDef = TypedDict(
    "_RequiredCreateTagsRequestInternetGatewayTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestInternetGatewayTypeDef = TypedDict(
    "_OptionalCreateTagsRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestInternetGatewayTypeDef(
    _RequiredCreateTagsRequestInternetGatewayTypeDef,
    _OptionalCreateTagsRequestInternetGatewayTypeDef,
):
    pass


_RequiredCreateTagsRequestNetworkAclTypeDef = TypedDict(
    "_RequiredCreateTagsRequestNetworkAclTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestNetworkAclTypeDef = TypedDict(
    "_OptionalCreateTagsRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestNetworkAclTypeDef(
    _RequiredCreateTagsRequestNetworkAclTypeDef, _OptionalCreateTagsRequestNetworkAclTypeDef
):
    pass


_RequiredCreateTagsRequestNetworkInterfaceTypeDef = TypedDict(
    "_RequiredCreateTagsRequestNetworkInterfaceTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestNetworkInterfaceTypeDef = TypedDict(
    "_OptionalCreateTagsRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestNetworkInterfaceTypeDef(
    _RequiredCreateTagsRequestNetworkInterfaceTypeDef,
    _OptionalCreateTagsRequestNetworkInterfaceTypeDef,
):
    pass


_RequiredCreateTagsRequestRouteTableTypeDef = TypedDict(
    "_RequiredCreateTagsRequestRouteTableTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestRouteTableTypeDef = TypedDict(
    "_OptionalCreateTagsRequestRouteTableTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestRouteTableTypeDef(
    _RequiredCreateTagsRequestRouteTableTypeDef, _OptionalCreateTagsRequestRouteTableTypeDef
):
    pass


_RequiredCreateTagsRequestSecurityGroupTypeDef = TypedDict(
    "_RequiredCreateTagsRequestSecurityGroupTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestSecurityGroupTypeDef = TypedDict(
    "_OptionalCreateTagsRequestSecurityGroupTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestSecurityGroupTypeDef(
    _RequiredCreateTagsRequestSecurityGroupTypeDef, _OptionalCreateTagsRequestSecurityGroupTypeDef
):
    pass


_RequiredCreateTagsRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateTagsRequestServiceResourceTypeDef",
    {
        "Resources": List[str],
        "Tags": List["TagTypeDef"],
    },
)
_OptionalCreateTagsRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateTagsRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestServiceResourceTypeDef(
    _RequiredCreateTagsRequestServiceResourceTypeDef,
    _OptionalCreateTagsRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateTagsRequestSnapshotTypeDef = TypedDict(
    "_RequiredCreateTagsRequestSnapshotTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestSnapshotTypeDef = TypedDict(
    "_OptionalCreateTagsRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestSnapshotTypeDef(
    _RequiredCreateTagsRequestSnapshotTypeDef, _OptionalCreateTagsRequestSnapshotTypeDef
):
    pass


_RequiredCreateTagsRequestSubnetTypeDef = TypedDict(
    "_RequiredCreateTagsRequestSubnetTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestSubnetTypeDef = TypedDict(
    "_OptionalCreateTagsRequestSubnetTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestSubnetTypeDef(
    _RequiredCreateTagsRequestSubnetTypeDef, _OptionalCreateTagsRequestSubnetTypeDef
):
    pass


_RequiredCreateTagsRequestTypeDef = TypedDict(
    "_RequiredCreateTagsRequestTypeDef",
    {
        "Resources": List[Any],
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestTypeDef = TypedDict(
    "_OptionalCreateTagsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestTypeDef(
    _RequiredCreateTagsRequestTypeDef, _OptionalCreateTagsRequestTypeDef
):
    pass


_RequiredCreateTagsRequestVolumeTypeDef = TypedDict(
    "_RequiredCreateTagsRequestVolumeTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestVolumeTypeDef = TypedDict(
    "_OptionalCreateTagsRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestVolumeTypeDef(
    _RequiredCreateTagsRequestVolumeTypeDef, _OptionalCreateTagsRequestVolumeTypeDef
):
    pass


_RequiredCreateTagsRequestVpcTypeDef = TypedDict(
    "_RequiredCreateTagsRequestVpcTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestVpcTypeDef = TypedDict(
    "_OptionalCreateTagsRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class CreateTagsRequestVpcTypeDef(
    _RequiredCreateTagsRequestVpcTypeDef, _OptionalCreateTagsRequestVpcTypeDef
):
    pass


CreateTrafficMirrorFilterRequestTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRequestTypeDef",
    {
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

CreateTrafficMirrorFilterResultResponseTypeDef = TypedDict(
    "CreateTrafficMirrorFilterResultResponseTypeDef",
    {
        "TrafficMirrorFilter": "TrafficMirrorFilterTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficMirrorFilterRuleRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficMirrorFilterRuleRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
    },
)
_OptionalCreateTrafficMirrorFilterRuleRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficMirrorFilterRuleRequestTypeDef",
    {
        "DestinationPortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "Protocol": int,
        "Description": str,
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)


class CreateTrafficMirrorFilterRuleRequestTypeDef(
    _RequiredCreateTrafficMirrorFilterRuleRequestTypeDef,
    _OptionalCreateTrafficMirrorFilterRuleRequestTypeDef,
):
    pass


CreateTrafficMirrorFilterRuleResultResponseTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleResultResponseTypeDef",
    {
        "TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficMirrorSessionRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficMirrorSessionRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "SessionNumber": int,
    },
)
_OptionalCreateTrafficMirrorSessionRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficMirrorSessionRequestTypeDef",
    {
        "PacketLength": int,
        "VirtualNetworkId": int,
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)


class CreateTrafficMirrorSessionRequestTypeDef(
    _RequiredCreateTrafficMirrorSessionRequestTypeDef,
    _OptionalCreateTrafficMirrorSessionRequestTypeDef,
):
    pass


CreateTrafficMirrorSessionResultResponseTypeDef = TypedDict(
    "CreateTrafficMirrorSessionResultResponseTypeDef",
    {
        "TrafficMirrorSession": "TrafficMirrorSessionTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficMirrorTargetRequestTypeDef = TypedDict(
    "CreateTrafficMirrorTargetRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "NetworkLoadBalancerArn": str,
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

CreateTrafficMirrorTargetResultResponseTypeDef = TypedDict(
    "CreateTrafficMirrorTargetResultResponseTypeDef",
    {
        "TrafficMirrorTarget": "TrafficMirrorTargetTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayConnectPeerRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
    },
)
_OptionalCreateTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayConnectPeerRequestTypeDef",
    {
        "TransitGatewayAddress": str,
        "BgpOptions": "TransitGatewayConnectRequestBgpOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayConnectPeerRequestTypeDef(
    _RequiredCreateTransitGatewayConnectPeerRequestTypeDef,
    _OptionalCreateTransitGatewayConnectPeerRequestTypeDef,
):
    pass


CreateTransitGatewayConnectPeerResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayConnectPeerResultResponseTypeDef",
    {
        "TransitGatewayConnectPeer": "TransitGatewayConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayConnectRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    {
        "Protocol": Literal["gre"],
    },
)

_RequiredCreateTransitGatewayConnectRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayConnectRequestTypeDef",
    {
        "TransportTransitGatewayAttachmentId": str,
        "Options": "CreateTransitGatewayConnectRequestOptionsTypeDef",
    },
)
_OptionalCreateTransitGatewayConnectRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayConnectRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayConnectRequestTypeDef(
    _RequiredCreateTransitGatewayConnectRequestTypeDef,
    _OptionalCreateTransitGatewayConnectRequestTypeDef,
):
    pass


CreateTransitGatewayConnectResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayConnectResultResponseTypeDef",
    {
        "TransitGatewayConnect": "TransitGatewayConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    {
        "Igmpv2Support": Igmpv2SupportValueType,
        "StaticSourcesSupport": StaticSourcesSupportValueType,
        "AutoAcceptSharedAssociations": AutoAcceptSharedAssociationsValueType,
    },
    total=False,
)

_RequiredCreateTransitGatewayMulticastDomainRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayMulticastDomainRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalCreateTransitGatewayMulticastDomainRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayMulticastDomainRequestTypeDef",
    {
        "Options": "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayMulticastDomainRequestTypeDef(
    _RequiredCreateTransitGatewayMulticastDomainRequestTypeDef,
    _OptionalCreateTransitGatewayMulticastDomainRequestTypeDef,
):
    pass


CreateTransitGatewayMulticastDomainResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainResultResponseTypeDef",
    {
        "TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "TransitGatewayId": str,
        "PeerTransitGatewayId": str,
        "PeerAccountId": str,
        "PeerRegion": str,
    },
)
_OptionalCreateTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayPeeringAttachmentRequestTypeDef(
    _RequiredCreateTransitGatewayPeeringAttachmentRequestTypeDef,
    _OptionalCreateTransitGatewayPeeringAttachmentRequestTypeDef,
):
    pass


CreateTransitGatewayPeeringAttachmentResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentResultResponseTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayPrefixListReferenceRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayPrefixListReferenceRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
    },
)
_OptionalCreateTransitGatewayPrefixListReferenceRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayPrefixListReferenceRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayPrefixListReferenceRequestTypeDef(
    _RequiredCreateTransitGatewayPrefixListReferenceRequestTypeDef,
    _OptionalCreateTransitGatewayPrefixListReferenceRequestTypeDef,
):
    pass


CreateTransitGatewayPrefixListReferenceResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayPrefixListReferenceResultResponseTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayRequestTypeDef = TypedDict(
    "CreateTransitGatewayRequestTypeDef",
    {
        "Description": str,
        "Options": "TransitGatewayRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

CreateTransitGatewayResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayResultResponseTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayRouteRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalCreateTransitGatewayRouteRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayRouteRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayRouteRequestTypeDef(
    _RequiredCreateTransitGatewayRouteRequestTypeDef,
    _OptionalCreateTransitGatewayRouteRequestTypeDef,
):
    pass


CreateTransitGatewayRouteResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayRouteResultResponseTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayRouteTableRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalCreateTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayRouteTableRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayRouteTableRequestTypeDef(
    _RequiredCreateTransitGatewayRouteTableRequestTypeDef,
    _OptionalCreateTransitGatewayRouteTableRequestTypeDef,
):
    pass


CreateTransitGatewayRouteTableResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableResultResponseTypeDef",
    {
        "TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": DnsSupportValueType,
        "Ipv6Support": Ipv6SupportValueType,
        "ApplianceModeSupport": ApplianceModeSupportValueType,
    },
    total=False,
)

_RequiredCreateTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "TransitGatewayId": str,
        "VpcId": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "Options": "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class CreateTransitGatewayVpcAttachmentRequestTypeDef(
    _RequiredCreateTransitGatewayVpcAttachmentRequestTypeDef,
    _OptionalCreateTransitGatewayVpcAttachmentRequestTypeDef,
):
    pass


CreateTransitGatewayVpcAttachmentResultResponseTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentResultResponseTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVolumePermissionModificationsTypeDef = TypedDict(
    "CreateVolumePermissionModificationsTypeDef",
    {
        "Add": List["CreateVolumePermissionTypeDef"],
        "Remove": List["CreateVolumePermissionTypeDef"],
    },
    total=False,
)

CreateVolumePermissionTypeDef = TypedDict(
    "CreateVolumePermissionTypeDef",
    {
        "Group": Literal["all"],
        "UserId": str,
    },
    total=False,
)

_RequiredCreateVolumeRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateVolumeRequestServiceResourceTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalCreateVolumeRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateVolumeRequestServiceResourceTypeDef",
    {
        "Encrypted": bool,
        "Iops": int,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "VolumeType": VolumeTypeType,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "MultiAttachEnabled": bool,
        "Throughput": int,
    },
    total=False,
)


class CreateVolumeRequestServiceResourceTypeDef(
    _RequiredCreateVolumeRequestServiceResourceTypeDef,
    _OptionalCreateVolumeRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateVolumeRequestTypeDef = TypedDict(
    "_RequiredCreateVolumeRequestTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalCreateVolumeRequestTypeDef = TypedDict(
    "_OptionalCreateVolumeRequestTypeDef",
    {
        "Encrypted": bool,
        "Iops": int,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "VolumeType": VolumeTypeType,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "MultiAttachEnabled": bool,
        "Throughput": int,
    },
    total=False,
)


class CreateVolumeRequestTypeDef(
    _RequiredCreateVolumeRequestTypeDef, _OptionalCreateVolumeRequestTypeDef
):
    pass


_RequiredCreateVpcEndpointConnectionNotificationRequestTypeDef = TypedDict(
    "_RequiredCreateVpcEndpointConnectionNotificationRequestTypeDef",
    {
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
    },
)
_OptionalCreateVpcEndpointConnectionNotificationRequestTypeDef = TypedDict(
    "_OptionalCreateVpcEndpointConnectionNotificationRequestTypeDef",
    {
        "DryRun": bool,
        "ServiceId": str,
        "VpcEndpointId": str,
        "ClientToken": str,
    },
    total=False,
)


class CreateVpcEndpointConnectionNotificationRequestTypeDef(
    _RequiredCreateVpcEndpointConnectionNotificationRequestTypeDef,
    _OptionalCreateVpcEndpointConnectionNotificationRequestTypeDef,
):
    pass


CreateVpcEndpointConnectionNotificationResultResponseTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationResultResponseTypeDef",
    {
        "ConnectionNotification": "ConnectionNotificationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateVpcEndpointRequestTypeDef",
    {
        "VpcId": str,
        "ServiceName": str,
    },
)
_OptionalCreateVpcEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateVpcEndpointRequestTypeDef",
    {
        "DryRun": bool,
        "VpcEndpointType": VpcEndpointTypeType,
        "PolicyDocument": str,
        "RouteTableIds": List[str],
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "ClientToken": str,
        "PrivateDnsEnabled": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateVpcEndpointRequestTypeDef(
    _RequiredCreateVpcEndpointRequestTypeDef, _OptionalCreateVpcEndpointRequestTypeDef
):
    pass


CreateVpcEndpointResultResponseTypeDef = TypedDict(
    "CreateVpcEndpointResultResponseTypeDef",
    {
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcEndpointServiceConfigurationRequestTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationRequestTypeDef",
    {
        "DryRun": bool,
        "AcceptanceRequired": bool,
        "PrivateDnsName": str,
        "NetworkLoadBalancerArns": List[str],
        "GatewayLoadBalancerArns": List[str],
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcEndpointServiceConfigurationResultResponseTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationResultResponseTypeDef",
    {
        "ServiceConfiguration": "ServiceConfigurationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringConnectionRequestServiceResourceTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "PeerOwnerId": str,
        "PeerVpcId": str,
        "VpcId": str,
        "PeerRegion": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcPeeringConnectionRequestTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestTypeDef",
    {
        "DryRun": bool,
        "PeerOwnerId": str,
        "PeerVpcId": str,
        "VpcId": str,
        "PeerRegion": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcPeeringConnectionRequestVpcTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestVpcTypeDef",
    {
        "DryRun": bool,
        "PeerOwnerId": str,
        "PeerVpcId": str,
        "PeerRegion": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcPeeringConnectionResultResponseTypeDef = TypedDict(
    "CreateVpcPeeringConnectionResultResponseTypeDef",
    {
        "VpcPeeringConnection": "VpcPeeringConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateVpcRequestServiceResourceTypeDef",
    {
        "CidrBlock": str,
    },
)
_OptionalCreateVpcRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateVpcRequestServiceResourceTypeDef",
    {
        "AmazonProvidedIpv6CidrBlock": bool,
        "Ipv6Pool": str,
        "Ipv6CidrBlock": str,
        "DryRun": bool,
        "InstanceTenancy": TenancyType,
        "Ipv6CidrBlockNetworkBorderGroup": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateVpcRequestServiceResourceTypeDef(
    _RequiredCreateVpcRequestServiceResourceTypeDef, _OptionalCreateVpcRequestServiceResourceTypeDef
):
    pass


_RequiredCreateVpcRequestTypeDef = TypedDict(
    "_RequiredCreateVpcRequestTypeDef",
    {
        "CidrBlock": str,
    },
)
_OptionalCreateVpcRequestTypeDef = TypedDict(
    "_OptionalCreateVpcRequestTypeDef",
    {
        "AmazonProvidedIpv6CidrBlock": bool,
        "Ipv6Pool": str,
        "Ipv6CidrBlock": str,
        "DryRun": bool,
        "InstanceTenancy": TenancyType,
        "Ipv6CidrBlockNetworkBorderGroup": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateVpcRequestTypeDef(_RequiredCreateVpcRequestTypeDef, _OptionalCreateVpcRequestTypeDef):
    pass


CreateVpcResultResponseTypeDef = TypedDict(
    "CreateVpcResultResponseTypeDef",
    {
        "Vpc": "VpcTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpnConnectionRequestTypeDef = TypedDict(
    "_RequiredCreateVpnConnectionRequestTypeDef",
    {
        "CustomerGatewayId": str,
        "Type": str,
    },
)
_OptionalCreateVpnConnectionRequestTypeDef = TypedDict(
    "_OptionalCreateVpnConnectionRequestTypeDef",
    {
        "VpnGatewayId": str,
        "TransitGatewayId": str,
        "DryRun": bool,
        "Options": "VpnConnectionOptionsSpecificationTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class CreateVpnConnectionRequestTypeDef(
    _RequiredCreateVpnConnectionRequestTypeDef, _OptionalCreateVpnConnectionRequestTypeDef
):
    pass


CreateVpnConnectionResultResponseTypeDef = TypedDict(
    "CreateVpnConnectionResultResponseTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpnConnectionRouteRequestTypeDef = TypedDict(
    "CreateVpnConnectionRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)

_RequiredCreateVpnGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateVpnGatewayRequestTypeDef",
    {
        "Type": Literal["ipsec.1"],
    },
)
_OptionalCreateVpnGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateVpnGatewayRequestTypeDef",
    {
        "AvailabilityZone": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AmazonSideAsn": int,
        "DryRun": bool,
    },
    total=False,
)


class CreateVpnGatewayRequestTypeDef(
    _RequiredCreateVpnGatewayRequestTypeDef, _OptionalCreateVpnGatewayRequestTypeDef
):
    pass


CreateVpnGatewayResultResponseTypeDef = TypedDict(
    "CreateVpnGatewayResultResponseTypeDef",
    {
        "VpnGateway": "VpnGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreditSpecificationRequestTypeDef = TypedDict(
    "CreditSpecificationRequestTypeDef",
    {
        "CpuCredits": str,
    },
)

CreditSpecificationTypeDef = TypedDict(
    "CreditSpecificationTypeDef",
    {
        "CpuCredits": str,
    },
    total=False,
)

CustomerGatewayTypeDef = TypedDict(
    "CustomerGatewayTypeDef",
    {
        "BgpAsn": str,
        "CustomerGatewayId": str,
        "IpAddress": str,
        "CertificateArn": str,
        "State": str,
        "Type": str,
        "DeviceName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteCarrierGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteCarrierGatewayRequestTypeDef",
    {
        "CarrierGatewayId": str,
    },
)
_OptionalDeleteCarrierGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteCarrierGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteCarrierGatewayRequestTypeDef(
    _RequiredDeleteCarrierGatewayRequestTypeDef, _OptionalDeleteCarrierGatewayRequestTypeDef
):
    pass


DeleteCarrierGatewayResultResponseTypeDef = TypedDict(
    "DeleteCarrierGatewayResultResponseTypeDef",
    {
        "CarrierGateway": "CarrierGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClientVpnEndpointRequestTypeDef = TypedDict(
    "_RequiredDeleteClientVpnEndpointRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDeleteClientVpnEndpointRequestTypeDef = TypedDict(
    "_OptionalDeleteClientVpnEndpointRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteClientVpnEndpointRequestTypeDef(
    _RequiredDeleteClientVpnEndpointRequestTypeDef, _OptionalDeleteClientVpnEndpointRequestTypeDef
):
    pass


DeleteClientVpnEndpointResultResponseTypeDef = TypedDict(
    "DeleteClientVpnEndpointResultResponseTypeDef",
    {
        "Status": "ClientVpnEndpointStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClientVpnRouteRequestTypeDef = TypedDict(
    "_RequiredDeleteClientVpnRouteRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
    },
)
_OptionalDeleteClientVpnRouteRequestTypeDef = TypedDict(
    "_OptionalDeleteClientVpnRouteRequestTypeDef",
    {
        "TargetVpcSubnetId": str,
        "DryRun": bool,
    },
    total=False,
)


class DeleteClientVpnRouteRequestTypeDef(
    _RequiredDeleteClientVpnRouteRequestTypeDef, _OptionalDeleteClientVpnRouteRequestTypeDef
):
    pass


DeleteClientVpnRouteResultResponseTypeDef = TypedDict(
    "DeleteClientVpnRouteResultResponseTypeDef",
    {
        "Status": "ClientVpnRouteStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCustomerGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteCustomerGatewayRequestTypeDef",
    {
        "CustomerGatewayId": str,
    },
)
_OptionalDeleteCustomerGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteCustomerGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteCustomerGatewayRequestTypeDef(
    _RequiredDeleteCustomerGatewayRequestTypeDef, _OptionalDeleteCustomerGatewayRequestTypeDef
):
    pass


DeleteDhcpOptionsRequestDhcpOptionsTypeDef = TypedDict(
    "DeleteDhcpOptionsRequestDhcpOptionsTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteDhcpOptionsRequestTypeDef = TypedDict(
    "_RequiredDeleteDhcpOptionsRequestTypeDef",
    {
        "DhcpOptionsId": str,
    },
)
_OptionalDeleteDhcpOptionsRequestTypeDef = TypedDict(
    "_OptionalDeleteDhcpOptionsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteDhcpOptionsRequestTypeDef(
    _RequiredDeleteDhcpOptionsRequestTypeDef, _OptionalDeleteDhcpOptionsRequestTypeDef
):
    pass


_RequiredDeleteEgressOnlyInternetGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteEgressOnlyInternetGatewayRequestTypeDef",
    {
        "EgressOnlyInternetGatewayId": str,
    },
)
_OptionalDeleteEgressOnlyInternetGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteEgressOnlyInternetGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteEgressOnlyInternetGatewayRequestTypeDef(
    _RequiredDeleteEgressOnlyInternetGatewayRequestTypeDef,
    _OptionalDeleteEgressOnlyInternetGatewayRequestTypeDef,
):
    pass


DeleteEgressOnlyInternetGatewayResultResponseTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayResultResponseTypeDef",
    {
        "ReturnCode": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetErrorItemTypeDef = TypedDict(
    "DeleteFleetErrorItemTypeDef",
    {
        "Error": "DeleteFleetErrorTypeDef",
        "FleetId": str,
    },
    total=False,
)

DeleteFleetErrorTypeDef = TypedDict(
    "DeleteFleetErrorTypeDef",
    {
        "Code": DeleteFleetErrorCodeType,
        "Message": str,
    },
    total=False,
)

DeleteFleetSuccessItemTypeDef = TypedDict(
    "DeleteFleetSuccessItemTypeDef",
    {
        "CurrentFleetState": FleetStateCodeType,
        "PreviousFleetState": FleetStateCodeType,
        "FleetId": str,
    },
    total=False,
)

_RequiredDeleteFleetsRequestTypeDef = TypedDict(
    "_RequiredDeleteFleetsRequestTypeDef",
    {
        "FleetIds": List[str],
        "TerminateInstances": bool,
    },
)
_OptionalDeleteFleetsRequestTypeDef = TypedDict(
    "_OptionalDeleteFleetsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteFleetsRequestTypeDef(
    _RequiredDeleteFleetsRequestTypeDef, _OptionalDeleteFleetsRequestTypeDef
):
    pass


DeleteFleetsResultResponseTypeDef = TypedDict(
    "DeleteFleetsResultResponseTypeDef",
    {
        "SuccessfulFleetDeletions": List["DeleteFleetSuccessItemTypeDef"],
        "UnsuccessfulFleetDeletions": List["DeleteFleetErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFlowLogsRequestTypeDef = TypedDict(
    "_RequiredDeleteFlowLogsRequestTypeDef",
    {
        "FlowLogIds": List[str],
    },
)
_OptionalDeleteFlowLogsRequestTypeDef = TypedDict(
    "_OptionalDeleteFlowLogsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteFlowLogsRequestTypeDef(
    _RequiredDeleteFlowLogsRequestTypeDef, _OptionalDeleteFlowLogsRequestTypeDef
):
    pass


DeleteFlowLogsResultResponseTypeDef = TypedDict(
    "DeleteFlowLogsResultResponseTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFpgaImageRequestTypeDef = TypedDict(
    "_RequiredDeleteFpgaImageRequestTypeDef",
    {
        "FpgaImageId": str,
    },
)
_OptionalDeleteFpgaImageRequestTypeDef = TypedDict(
    "_OptionalDeleteFpgaImageRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteFpgaImageRequestTypeDef(
    _RequiredDeleteFpgaImageRequestTypeDef, _OptionalDeleteFpgaImageRequestTypeDef
):
    pass


DeleteFpgaImageResultResponseTypeDef = TypedDict(
    "DeleteFpgaImageResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "DeleteInternetGatewayRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteInternetGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteInternetGatewayRequestTypeDef",
    {
        "InternetGatewayId": str,
    },
)
_OptionalDeleteInternetGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteInternetGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteInternetGatewayRequestTypeDef(
    _RequiredDeleteInternetGatewayRequestTypeDef, _OptionalDeleteInternetGatewayRequestTypeDef
):
    pass


DeleteKeyPairRequestKeyPairInfoTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairInfoTypeDef",
    {
        "KeyPairId": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteKeyPairRequestKeyPairTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairTypeDef",
    {
        "KeyPairId": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteKeyPairRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestTypeDef",
    {
        "KeyName": str,
        "KeyPairId": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteLaunchTemplateRequestTypeDef = TypedDict(
    "DeleteLaunchTemplateRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
    },
    total=False,
)

DeleteLaunchTemplateResultResponseTypeDef = TypedDict(
    "DeleteLaunchTemplateResultResponseTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLaunchTemplateVersionsRequestTypeDef = TypedDict(
    "_RequiredDeleteLaunchTemplateVersionsRequestTypeDef",
    {
        "Versions": List[str],
    },
)
_OptionalDeleteLaunchTemplateVersionsRequestTypeDef = TypedDict(
    "_OptionalDeleteLaunchTemplateVersionsRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
    },
    total=False,
)


class DeleteLaunchTemplateVersionsRequestTypeDef(
    _RequiredDeleteLaunchTemplateVersionsRequestTypeDef,
    _OptionalDeleteLaunchTemplateVersionsRequestTypeDef,
):
    pass


DeleteLaunchTemplateVersionsResponseErrorItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
        "ResponseError": "ResponseErrorTypeDef",
    },
    total=False,
)

DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
    },
    total=False,
)

DeleteLaunchTemplateVersionsResultResponseTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResultResponseTypeDef",
    {
        "SuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef"
        ],
        "UnsuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLocalGatewayRouteRequestTypeDef = TypedDict(
    "_RequiredDeleteLocalGatewayRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalDeleteLocalGatewayRouteRequestTypeDef = TypedDict(
    "_OptionalDeleteLocalGatewayRouteRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteLocalGatewayRouteRequestTypeDef(
    _RequiredDeleteLocalGatewayRouteRequestTypeDef, _OptionalDeleteLocalGatewayRouteRequestTypeDef
):
    pass


DeleteLocalGatewayRouteResultResponseTypeDef = TypedDict(
    "DeleteLocalGatewayRouteResultResponseTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef = TypedDict(
    "_RequiredDeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
    },
)
_OptionalDeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef = TypedDict(
    "_OptionalDeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef(
    _RequiredDeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef,
    _OptionalDeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef,
):
    pass


DeleteLocalGatewayRouteTableVpcAssociationResultResponseTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationResultResponseTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteManagedPrefixListRequestTypeDef = TypedDict(
    "_RequiredDeleteManagedPrefixListRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalDeleteManagedPrefixListRequestTypeDef = TypedDict(
    "_OptionalDeleteManagedPrefixListRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteManagedPrefixListRequestTypeDef(
    _RequiredDeleteManagedPrefixListRequestTypeDef, _OptionalDeleteManagedPrefixListRequestTypeDef
):
    pass


DeleteManagedPrefixListResultResponseTypeDef = TypedDict(
    "DeleteManagedPrefixListResultResponseTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNatGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteNatGatewayRequestTypeDef",
    {
        "NatGatewayId": str,
    },
)
_OptionalDeleteNatGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteNatGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNatGatewayRequestTypeDef(
    _RequiredDeleteNatGatewayRequestTypeDef, _OptionalDeleteNatGatewayRequestTypeDef
):
    pass


DeleteNatGatewayResultResponseTypeDef = TypedDict(
    "DeleteNatGatewayResultResponseTypeDef",
    {
        "NatGatewayId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_RequiredDeleteNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "Egress": bool,
        "RuleNumber": int,
    },
)
_OptionalDeleteNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_OptionalDeleteNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkAclEntryRequestNetworkAclTypeDef(
    _RequiredDeleteNetworkAclEntryRequestNetworkAclTypeDef,
    _OptionalDeleteNetworkAclEntryRequestNetworkAclTypeDef,
):
    pass


_RequiredDeleteNetworkAclEntryRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkAclEntryRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "RuleNumber": int,
    },
)
_OptionalDeleteNetworkAclEntryRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkAclEntryRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkAclEntryRequestTypeDef(
    _RequiredDeleteNetworkAclEntryRequestTypeDef, _OptionalDeleteNetworkAclEntryRequestTypeDef
):
    pass


DeleteNetworkAclRequestNetworkAclTypeDef = TypedDict(
    "DeleteNetworkAclRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteNetworkAclRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkAclRequestTypeDef",
    {
        "NetworkAclId": str,
    },
)
_OptionalDeleteNetworkAclRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkAclRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkAclRequestTypeDef(
    _RequiredDeleteNetworkAclRequestTypeDef, _OptionalDeleteNetworkAclRequestTypeDef
):
    pass


_RequiredDeleteNetworkInsightsAnalysisRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInsightsAnalysisRequestTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
    },
)
_OptionalDeleteNetworkInsightsAnalysisRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInsightsAnalysisRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkInsightsAnalysisRequestTypeDef(
    _RequiredDeleteNetworkInsightsAnalysisRequestTypeDef,
    _OptionalDeleteNetworkInsightsAnalysisRequestTypeDef,
):
    pass


DeleteNetworkInsightsAnalysisResultResponseTypeDef = TypedDict(
    "DeleteNetworkInsightsAnalysisResultResponseTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkInsightsPathRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInsightsPathRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
    },
)
_OptionalDeleteNetworkInsightsPathRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInsightsPathRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkInsightsPathRequestTypeDef(
    _RequiredDeleteNetworkInsightsPathRequestTypeDef,
    _OptionalDeleteNetworkInsightsPathRequestTypeDef,
):
    pass


DeleteNetworkInsightsPathResultResponseTypeDef = TypedDict(
    "DeleteNetworkInsightsPathResultResponseTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkInterfacePermissionRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInterfacePermissionRequestTypeDef",
    {
        "NetworkInterfacePermissionId": str,
    },
)
_OptionalDeleteNetworkInterfacePermissionRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInterfacePermissionRequestTypeDef",
    {
        "Force": bool,
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkInterfacePermissionRequestTypeDef(
    _RequiredDeleteNetworkInterfacePermissionRequestTypeDef,
    _OptionalDeleteNetworkInterfacePermissionRequestTypeDef,
):
    pass


DeleteNetworkInterfacePermissionResultResponseTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "DeleteNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteNetworkInterfaceRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInterfaceRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalDeleteNetworkInterfaceRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInterfaceRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteNetworkInterfaceRequestTypeDef(
    _RequiredDeleteNetworkInterfaceRequestTypeDef, _OptionalDeleteNetworkInterfaceRequestTypeDef
):
    pass


DeletePlacementGroupRequestPlacementGroupTypeDef = TypedDict(
    "DeletePlacementGroupRequestPlacementGroupTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeletePlacementGroupRequestTypeDef = TypedDict(
    "_RequiredDeletePlacementGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalDeletePlacementGroupRequestTypeDef = TypedDict(
    "_OptionalDeletePlacementGroupRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeletePlacementGroupRequestTypeDef(
    _RequiredDeletePlacementGroupRequestTypeDef, _OptionalDeletePlacementGroupRequestTypeDef
):
    pass


DeleteQueuedReservedInstancesErrorTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesErrorTypeDef",
    {
        "Code": DeleteQueuedReservedInstancesErrorCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredDeleteQueuedReservedInstancesRequestTypeDef = TypedDict(
    "_RequiredDeleteQueuedReservedInstancesRequestTypeDef",
    {
        "ReservedInstancesIds": List[str],
    },
)
_OptionalDeleteQueuedReservedInstancesRequestTypeDef = TypedDict(
    "_OptionalDeleteQueuedReservedInstancesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteQueuedReservedInstancesRequestTypeDef(
    _RequiredDeleteQueuedReservedInstancesRequestTypeDef,
    _OptionalDeleteQueuedReservedInstancesRequestTypeDef,
):
    pass


DeleteQueuedReservedInstancesResultResponseTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesResultResponseTypeDef",
    {
        "SuccessfulQueuedPurchaseDeletions": List["SuccessfulQueuedPurchaseDeletionTypeDef"],
        "FailedQueuedPurchaseDeletions": List["FailedQueuedPurchaseDeletionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRouteRequestRouteTypeDef = TypedDict(
    "DeleteRouteRequestRouteTypeDef",
    {
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteRouteRequestTypeDef = TypedDict(
    "_RequiredDeleteRouteRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalDeleteRouteRequestTypeDef = TypedDict(
    "_OptionalDeleteRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
    },
    total=False,
)


class DeleteRouteRequestTypeDef(
    _RequiredDeleteRouteRequestTypeDef, _OptionalDeleteRouteRequestTypeDef
):
    pass


DeleteRouteTableRequestRouteTableTypeDef = TypedDict(
    "DeleteRouteTableRequestRouteTableTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteRouteTableRequestTypeDef = TypedDict(
    "_RequiredDeleteRouteTableRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalDeleteRouteTableRequestTypeDef = TypedDict(
    "_OptionalDeleteRouteTableRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteRouteTableRequestTypeDef(
    _RequiredDeleteRouteTableRequestTypeDef, _OptionalDeleteRouteTableRequestTypeDef
):
    pass


DeleteSecurityGroupRequestSecurityGroupTypeDef = TypedDict(
    "DeleteSecurityGroupRequestSecurityGroupTypeDef",
    {
        "GroupName": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteSecurityGroupRequestTypeDef = TypedDict(
    "DeleteSecurityGroupRequestTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteSnapshotRequestSnapshotTypeDef = TypedDict(
    "DeleteSnapshotRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteSnapshotRequestTypeDef = TypedDict(
    "_RequiredDeleteSnapshotRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalDeleteSnapshotRequestTypeDef = TypedDict(
    "_OptionalDeleteSnapshotRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteSnapshotRequestTypeDef(
    _RequiredDeleteSnapshotRequestTypeDef, _OptionalDeleteSnapshotRequestTypeDef
):
    pass


DeleteSpotDatafeedSubscriptionRequestTypeDef = TypedDict(
    "DeleteSpotDatafeedSubscriptionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DeleteSubnetRequestSubnetTypeDef = TypedDict(
    "DeleteSubnetRequestSubnetTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteSubnetRequestTypeDef = TypedDict(
    "_RequiredDeleteSubnetRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalDeleteSubnetRequestTypeDef = TypedDict(
    "_OptionalDeleteSubnetRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteSubnetRequestTypeDef(
    _RequiredDeleteSubnetRequestTypeDef, _OptionalDeleteSubnetRequestTypeDef
):
    pass


DeleteTagsRequestTagTypeDef = TypedDict(
    "DeleteTagsRequestTagTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteTagsRequestTypeDef = TypedDict(
    "_RequiredDeleteTagsRequestTypeDef",
    {
        "Resources": List[Any],
    },
)
_OptionalDeleteTagsRequestTypeDef = TypedDict(
    "_OptionalDeleteTagsRequestTypeDef",
    {
        "DryRun": bool,
        "Tags": Optional[List["TagTypeDef"]],
    },
    total=False,
)


class DeleteTagsRequestTypeDef(
    _RequiredDeleteTagsRequestTypeDef, _OptionalDeleteTagsRequestTypeDef
):
    pass


_RequiredDeleteTrafficMirrorFilterRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorFilterRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
    },
)
_OptionalDeleteTrafficMirrorFilterRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorFilterRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTrafficMirrorFilterRequestTypeDef(
    _RequiredDeleteTrafficMirrorFilterRequestTypeDef,
    _OptionalDeleteTrafficMirrorFilterRequestTypeDef,
):
    pass


DeleteTrafficMirrorFilterResultResponseTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterResultResponseTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrafficMirrorFilterRuleRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorFilterRuleRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
    },
)
_OptionalDeleteTrafficMirrorFilterRuleRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorFilterRuleRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTrafficMirrorFilterRuleRequestTypeDef(
    _RequiredDeleteTrafficMirrorFilterRuleRequestTypeDef,
    _OptionalDeleteTrafficMirrorFilterRuleRequestTypeDef,
):
    pass


DeleteTrafficMirrorFilterRuleResultResponseTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleResultResponseTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrafficMirrorSessionRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorSessionRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
    },
)
_OptionalDeleteTrafficMirrorSessionRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorSessionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTrafficMirrorSessionRequestTypeDef(
    _RequiredDeleteTrafficMirrorSessionRequestTypeDef,
    _OptionalDeleteTrafficMirrorSessionRequestTypeDef,
):
    pass


DeleteTrafficMirrorSessionResultResponseTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionResultResponseTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrafficMirrorTargetRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorTargetRequestTypeDef",
    {
        "TrafficMirrorTargetId": str,
    },
)
_OptionalDeleteTrafficMirrorTargetRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorTargetRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTrafficMirrorTargetRequestTypeDef(
    _RequiredDeleteTrafficMirrorTargetRequestTypeDef,
    _OptionalDeleteTrafficMirrorTargetRequestTypeDef,
):
    pass


DeleteTrafficMirrorTargetResultResponseTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetResultResponseTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayConnectPeerRequestTypeDef",
    {
        "TransitGatewayConnectPeerId": str,
    },
)
_OptionalDeleteTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayConnectPeerRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayConnectPeerRequestTypeDef(
    _RequiredDeleteTransitGatewayConnectPeerRequestTypeDef,
    _OptionalDeleteTransitGatewayConnectPeerRequestTypeDef,
):
    pass


DeleteTransitGatewayConnectPeerResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayConnectPeerResultResponseTypeDef",
    {
        "TransitGatewayConnectPeer": "TransitGatewayConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayConnectRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayConnectRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDeleteTransitGatewayConnectRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayConnectRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayConnectRequestTypeDef(
    _RequiredDeleteTransitGatewayConnectRequestTypeDef,
    _OptionalDeleteTransitGatewayConnectRequestTypeDef,
):
    pass


DeleteTransitGatewayConnectResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayConnectResultResponseTypeDef",
    {
        "TransitGatewayConnect": "TransitGatewayConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayMulticastDomainRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayMulticastDomainRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
    },
)
_OptionalDeleteTransitGatewayMulticastDomainRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayMulticastDomainRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayMulticastDomainRequestTypeDef(
    _RequiredDeleteTransitGatewayMulticastDomainRequestTypeDef,
    _OptionalDeleteTransitGatewayMulticastDomainRequestTypeDef,
):
    pass


DeleteTransitGatewayMulticastDomainResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainResultResponseTypeDef",
    {
        "TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDeleteTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayPeeringAttachmentRequestTypeDef(
    _RequiredDeleteTransitGatewayPeeringAttachmentRequestTypeDef,
    _OptionalDeleteTransitGatewayPeeringAttachmentRequestTypeDef,
):
    pass


DeleteTransitGatewayPeeringAttachmentResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentResultResponseTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayPrefixListReferenceRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayPrefixListReferenceRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
    },
)
_OptionalDeleteTransitGatewayPrefixListReferenceRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayPrefixListReferenceRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayPrefixListReferenceRequestTypeDef(
    _RequiredDeleteTransitGatewayPrefixListReferenceRequestTypeDef,
    _OptionalDeleteTransitGatewayPrefixListReferenceRequestTypeDef,
):
    pass


DeleteTransitGatewayPrefixListReferenceResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayPrefixListReferenceResultResponseTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalDeleteTransitGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayRequestTypeDef(
    _RequiredDeleteTransitGatewayRequestTypeDef, _OptionalDeleteTransitGatewayRequestTypeDef
):
    pass


DeleteTransitGatewayResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayResultResponseTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRouteRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRouteRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "DestinationCidrBlock": str,
    },
)
_OptionalDeleteTransitGatewayRouteRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRouteRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayRouteRequestTypeDef(
    _RequiredDeleteTransitGatewayRouteRequestTypeDef,
    _OptionalDeleteTransitGatewayRouteRequestTypeDef,
):
    pass


DeleteTransitGatewayRouteResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayRouteResultResponseTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRouteTableRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalDeleteTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRouteTableRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayRouteTableRequestTypeDef(
    _RequiredDeleteTransitGatewayRouteTableRequestTypeDef,
    _OptionalDeleteTransitGatewayRouteTableRequestTypeDef,
):
    pass


DeleteTransitGatewayRouteTableResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableResultResponseTypeDef",
    {
        "TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDeleteTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteTransitGatewayVpcAttachmentRequestTypeDef(
    _RequiredDeleteTransitGatewayVpcAttachmentRequestTypeDef,
    _OptionalDeleteTransitGatewayVpcAttachmentRequestTypeDef,
):
    pass


DeleteTransitGatewayVpcAttachmentResultResponseTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentResultResponseTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVolumeRequestTypeDef = TypedDict(
    "_RequiredDeleteVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDeleteVolumeRequestTypeDef = TypedDict(
    "_OptionalDeleteVolumeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVolumeRequestTypeDef(
    _RequiredDeleteVolumeRequestTypeDef, _OptionalDeleteVolumeRequestTypeDef
):
    pass


DeleteVolumeRequestVolumeTypeDef = TypedDict(
    "DeleteVolumeRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteVpcEndpointConnectionNotificationsRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointConnectionNotificationsRequestTypeDef",
    {
        "ConnectionNotificationIds": List[str],
    },
)
_OptionalDeleteVpcEndpointConnectionNotificationsRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointConnectionNotificationsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpcEndpointConnectionNotificationsRequestTypeDef(
    _RequiredDeleteVpcEndpointConnectionNotificationsRequestTypeDef,
    _OptionalDeleteVpcEndpointConnectionNotificationsRequestTypeDef,
):
    pass


DeleteVpcEndpointConnectionNotificationsResultResponseTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsResultResponseTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcEndpointServiceConfigurationsRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointServiceConfigurationsRequestTypeDef",
    {
        "ServiceIds": List[str],
    },
)
_OptionalDeleteVpcEndpointServiceConfigurationsRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointServiceConfigurationsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpcEndpointServiceConfigurationsRequestTypeDef(
    _RequiredDeleteVpcEndpointServiceConfigurationsRequestTypeDef,
    _OptionalDeleteVpcEndpointServiceConfigurationsRequestTypeDef,
):
    pass


DeleteVpcEndpointServiceConfigurationsResultResponseTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsResultResponseTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcEndpointsRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointsRequestTypeDef",
    {
        "VpcEndpointIds": List[str],
    },
)
_OptionalDeleteVpcEndpointsRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpcEndpointsRequestTypeDef(
    _RequiredDeleteVpcEndpointsRequestTypeDef, _OptionalDeleteVpcEndpointsRequestTypeDef
):
    pass


DeleteVpcEndpointsResultResponseTypeDef = TypedDict(
    "DeleteVpcEndpointsResultResponseTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcPeeringConnectionRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcPeeringConnectionRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalDeleteVpcPeeringConnectionRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcPeeringConnectionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpcPeeringConnectionRequestTypeDef(
    _RequiredDeleteVpcPeeringConnectionRequestTypeDef,
    _OptionalDeleteVpcPeeringConnectionRequestTypeDef,
):
    pass


DeleteVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DeleteVpcPeeringConnectionResultResponseTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDeleteVpcRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpcRequestTypeDef(_RequiredDeleteVpcRequestTypeDef, _OptionalDeleteVpcRequestTypeDef):
    pass


DeleteVpcRequestVpcTypeDef = TypedDict(
    "DeleteVpcRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteVpnConnectionRequestTypeDef = TypedDict(
    "_RequiredDeleteVpnConnectionRequestTypeDef",
    {
        "VpnConnectionId": str,
    },
)
_OptionalDeleteVpnConnectionRequestTypeDef = TypedDict(
    "_OptionalDeleteVpnConnectionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpnConnectionRequestTypeDef(
    _RequiredDeleteVpnConnectionRequestTypeDef, _OptionalDeleteVpnConnectionRequestTypeDef
):
    pass


DeleteVpnConnectionRouteRequestTypeDef = TypedDict(
    "DeleteVpnConnectionRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)

_RequiredDeleteVpnGatewayRequestTypeDef = TypedDict(
    "_RequiredDeleteVpnGatewayRequestTypeDef",
    {
        "VpnGatewayId": str,
    },
)
_OptionalDeleteVpnGatewayRequestTypeDef = TypedDict(
    "_OptionalDeleteVpnGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeleteVpnGatewayRequestTypeDef(
    _RequiredDeleteVpnGatewayRequestTypeDef, _OptionalDeleteVpnGatewayRequestTypeDef
):
    pass


_RequiredDeprovisionByoipCidrRequestTypeDef = TypedDict(
    "_RequiredDeprovisionByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalDeprovisionByoipCidrRequestTypeDef = TypedDict(
    "_OptionalDeprovisionByoipCidrRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeprovisionByoipCidrRequestTypeDef(
    _RequiredDeprovisionByoipCidrRequestTypeDef, _OptionalDeprovisionByoipCidrRequestTypeDef
):
    pass


DeprovisionByoipCidrResultResponseTypeDef = TypedDict(
    "DeprovisionByoipCidrResultResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterImageRequestImageTypeDef = TypedDict(
    "DeregisterImageRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeregisterImageRequestTypeDef = TypedDict(
    "_RequiredDeregisterImageRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDeregisterImageRequestTypeDef = TypedDict(
    "_OptionalDeregisterImageRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DeregisterImageRequestTypeDef(
    _RequiredDeregisterImageRequestTypeDef, _OptionalDeregisterImageRequestTypeDef
):
    pass


DeregisterInstanceEventNotificationAttributesRequestTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesRequestTypeDef",
    {
        "DryRun": bool,
        "InstanceTagAttribute": "DeregisterInstanceTagAttributeRequestTypeDef",
    },
    total=False,
)

DeregisterInstanceEventNotificationAttributesResultResponseTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesResultResponseTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "DeregisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": bool,
        "InstanceTagKeys": List[str],
    },
    total=False,
)

DeregisterTransitGatewayMulticastGroupMembersRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "GroupIpAddress": str,
        "NetworkInterfaceIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DeregisterTransitGatewayMulticastGroupMembersResultResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersResultResponseTypeDef",
    {
        "DeregisteredMulticastGroupMembers": "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTransitGatewayMulticastGroupSourcesRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "GroupIpAddress": str,
        "NetworkInterfaceIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DeregisterTransitGatewayMulticastGroupSourcesResultResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesResultResponseTypeDef",
    {
        "DeregisteredMulticastGroupSources": "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestTypeDef",
    {
        "AttributeNames": List[AccountAttributeNameType],
        "DryRun": bool,
    },
    total=False,
)

DescribeAccountAttributesResultResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResultResponseTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesAttributeRequestTypeDef = TypedDict(
    "DescribeAddressesAttributeRequestTypeDef",
    {
        "AllocationIds": List[str],
        "Attribute": Literal["domain-name"],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

DescribeAddressesAttributeResultResponseTypeDef = TypedDict(
    "DescribeAddressesAttributeResultResponseTypeDef",
    {
        "Addresses": List["AddressAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesRequestTypeDef = TypedDict(
    "DescribeAddressesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "PublicIps": List[str],
        "AllocationIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeAddressesResultResponseTypeDef = TypedDict(
    "DescribeAddressesResultResponseTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregateIdFormatRequestTypeDef = TypedDict(
    "DescribeAggregateIdFormatRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DescribeAggregateIdFormatResultResponseTypeDef = TypedDict(
    "DescribeAggregateIdFormatResultResponseTypeDef",
    {
        "UseLongIdsAggregated": bool,
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityZonesRequestTypeDef = TypedDict(
    "DescribeAvailabilityZonesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "ZoneNames": List[str],
        "ZoneIds": List[str],
        "AllAvailabilityZones": bool,
        "DryRun": bool,
    },
    total=False,
)

DescribeAvailabilityZonesResultResponseTypeDef = TypedDict(
    "DescribeAvailabilityZonesResultResponseTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBundleTasksRequestTypeDef = TypedDict(
    "DescribeBundleTasksRequestTypeDef",
    {
        "BundleIds": List[str],
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeBundleTasksResultResponseTypeDef = TypedDict(
    "DescribeBundleTasksResultResponseTypeDef",
    {
        "BundleTasks": List["BundleTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeByoipCidrsRequestTypeDef = TypedDict(
    "_RequiredDescribeByoipCidrsRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalDescribeByoipCidrsRequestTypeDef = TypedDict(
    "_OptionalDescribeByoipCidrsRequestTypeDef",
    {
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)


class DescribeByoipCidrsRequestTypeDef(
    _RequiredDescribeByoipCidrsRequestTypeDef, _OptionalDescribeByoipCidrsRequestTypeDef
):
    pass


DescribeByoipCidrsResultResponseTypeDef = TypedDict(
    "DescribeByoipCidrsResultResponseTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityReservationsRequestTypeDef = TypedDict(
    "DescribeCapacityReservationsRequestTypeDef",
    {
        "CapacityReservationIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeCapacityReservationsResultResponseTypeDef = TypedDict(
    "DescribeCapacityReservationsResultResponseTypeDef",
    {
        "NextToken": str,
        "CapacityReservations": List["CapacityReservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCarrierGatewaysRequestTypeDef = TypedDict(
    "DescribeCarrierGatewaysRequestTypeDef",
    {
        "CarrierGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeCarrierGatewaysResultResponseTypeDef = TypedDict(
    "DescribeCarrierGatewaysResultResponseTypeDef",
    {
        "CarrierGateways": List["CarrierGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClassicLinkInstancesRequestTypeDef = TypedDict(
    "DescribeClassicLinkInstancesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "InstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeClassicLinkInstancesResultResponseTypeDef = TypedDict(
    "DescribeClassicLinkInstancesResultResponseTypeDef",
    {
        "Instances": List["ClassicLinkInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnAuthorizationRulesRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnAuthorizationRulesRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnAuthorizationRulesRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnAuthorizationRulesRequestTypeDef",
    {
        "DryRun": bool,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
    },
    total=False,
)


class DescribeClientVpnAuthorizationRulesRequestTypeDef(
    _RequiredDescribeClientVpnAuthorizationRulesRequestTypeDef,
    _OptionalDescribeClientVpnAuthorizationRulesRequestTypeDef,
):
    pass


DescribeClientVpnAuthorizationRulesResultResponseTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesResultResponseTypeDef",
    {
        "AuthorizationRules": List["AuthorizationRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnConnectionsRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnConnectionsRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnConnectionsRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnConnectionsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)


class DescribeClientVpnConnectionsRequestTypeDef(
    _RequiredDescribeClientVpnConnectionsRequestTypeDef,
    _OptionalDescribeClientVpnConnectionsRequestTypeDef,
):
    pass


DescribeClientVpnConnectionsResultResponseTypeDef = TypedDict(
    "DescribeClientVpnConnectionsResultResponseTypeDef",
    {
        "Connections": List["ClientVpnConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnEndpointsRequestTypeDef = TypedDict(
    "DescribeClientVpnEndpointsRequestTypeDef",
    {
        "ClientVpnEndpointIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeClientVpnEndpointsResultResponseTypeDef = TypedDict(
    "DescribeClientVpnEndpointsResultResponseTypeDef",
    {
        "ClientVpnEndpoints": List["ClientVpnEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnRoutesRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnRoutesRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnRoutesRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnRoutesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class DescribeClientVpnRoutesRequestTypeDef(
    _RequiredDescribeClientVpnRoutesRequestTypeDef, _OptionalDescribeClientVpnRoutesRequestTypeDef
):
    pass


DescribeClientVpnRoutesResultResponseTypeDef = TypedDict(
    "DescribeClientVpnRoutesResultResponseTypeDef",
    {
        "Routes": List["ClientVpnRouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnTargetNetworksRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnTargetNetworksRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnTargetNetworksRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnTargetNetworksRequestTypeDef",
    {
        "AssociationIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class DescribeClientVpnTargetNetworksRequestTypeDef(
    _RequiredDescribeClientVpnTargetNetworksRequestTypeDef,
    _OptionalDescribeClientVpnTargetNetworksRequestTypeDef,
):
    pass


DescribeClientVpnTargetNetworksResultResponseTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksResultResponseTypeDef",
    {
        "ClientVpnTargetNetworks": List["TargetNetworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCoipPoolsRequestTypeDef = TypedDict(
    "DescribeCoipPoolsRequestTypeDef",
    {
        "PoolIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeCoipPoolsResultResponseTypeDef = TypedDict(
    "DescribeCoipPoolsResultResponseTypeDef",
    {
        "CoipPools": List["CoipPoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConversionTasksRequestTypeDef = TypedDict(
    "DescribeConversionTasksRequestTypeDef",
    {
        "ConversionTaskIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeConversionTasksResultResponseTypeDef = TypedDict(
    "DescribeConversionTasksResultResponseTypeDef",
    {
        "ConversionTasks": List["ConversionTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomerGatewaysRequestTypeDef = TypedDict(
    "DescribeCustomerGatewaysRequestTypeDef",
    {
        "CustomerGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeCustomerGatewaysResultResponseTypeDef = TypedDict(
    "DescribeCustomerGatewaysResultResponseTypeDef",
    {
        "CustomerGateways": List["CustomerGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDhcpOptionsRequestTypeDef = TypedDict(
    "DescribeDhcpOptionsRequestTypeDef",
    {
        "DhcpOptionsIds": List[str],
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeDhcpOptionsResultResponseTypeDef = TypedDict(
    "DescribeDhcpOptionsResultResponseTypeDef",
    {
        "DhcpOptions": List["DhcpOptionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEgressOnlyInternetGatewaysRequestTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysRequestTypeDef",
    {
        "DryRun": bool,
        "EgressOnlyInternetGatewayIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEgressOnlyInternetGatewaysResultResponseTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysResultResponseTypeDef",
    {
        "EgressOnlyInternetGateways": List["EgressOnlyInternetGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticGpusRequestTypeDef = TypedDict(
    "DescribeElasticGpusRequestTypeDef",
    {
        "ElasticGpuIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeElasticGpusResultResponseTypeDef = TypedDict(
    "DescribeElasticGpusResultResponseTypeDef",
    {
        "ElasticGpuSet": List["ElasticGpusTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportImageTasksRequestTypeDef = TypedDict(
    "DescribeExportImageTasksRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "ExportImageTaskIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeExportImageTasksResultResponseTypeDef = TypedDict(
    "DescribeExportImageTasksResultResponseTypeDef",
    {
        "ExportImageTasks": List["ExportImageTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestTypeDef",
    {
        "ExportTaskIds": List[str],
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeExportTasksResultResponseTypeDef = TypedDict(
    "DescribeExportTasksResultResponseTypeDef",
    {
        "ExportTasks": List["ExportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": FastSnapshotRestoreStateCodeType,
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

DescribeFastSnapshotRestoresRequestTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeFastSnapshotRestoresResultResponseTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresResultResponseTypeDef",
    {
        "FastSnapshotRestores": List["DescribeFastSnapshotRestoreSuccessItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetErrorTypeDef = TypedDict(
    "DescribeFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredDescribeFleetHistoryRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetHistoryRequestTypeDef",
    {
        "FleetId": str,
        "StartTime": Union[datetime, str],
    },
)
_OptionalDescribeFleetHistoryRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetHistoryRequestTypeDef",
    {
        "DryRun": bool,
        "EventType": FleetEventTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeFleetHistoryRequestTypeDef(
    _RequiredDescribeFleetHistoryRequestTypeDef, _OptionalDescribeFleetHistoryRequestTypeDef
):
    pass


DescribeFleetHistoryResultResponseTypeDef = TypedDict(
    "DescribeFleetHistoryResultResponseTypeDef",
    {
        "HistoryRecords": List["HistoryRecordEntryTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "FleetId": str,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetInstancesRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetInstancesRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetInstancesRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetInstancesRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)


class DescribeFleetInstancesRequestTypeDef(
    _RequiredDescribeFleetInstancesRequestTypeDef, _OptionalDescribeFleetInstancesRequestTypeDef
):
    pass


DescribeFleetInstancesResultResponseTypeDef = TypedDict(
    "DescribeFleetInstancesResultResponseTypeDef",
    {
        "ActiveInstances": List["ActiveInstanceTypeDef"],
        "NextToken": str,
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetsInstancesTypeDef = TypedDict(
    "DescribeFleetsInstancesTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "InstanceIds": List[str],
        "InstanceType": InstanceTypeType,
        "Platform": Literal["Windows"],
    },
    total=False,
)

DescribeFleetsRequestTypeDef = TypedDict(
    "DescribeFleetsRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "FleetIds": List[str],
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeFleetsResultResponseTypeDef = TypedDict(
    "DescribeFleetsResultResponseTypeDef",
    {
        "NextToken": str,
        "Fleets": List["FleetDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowLogsRequestTypeDef = TypedDict(
    "DescribeFlowLogsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "FlowLogIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFlowLogsResultResponseTypeDef = TypedDict(
    "DescribeFlowLogsResultResponseTypeDef",
    {
        "FlowLogs": List["FlowLogTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFpgaImageAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeFpgaImageAttributeRequestTypeDef",
    {
        "FpgaImageId": str,
        "Attribute": FpgaImageAttributeNameType,
    },
)
_OptionalDescribeFpgaImageAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeFpgaImageAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeFpgaImageAttributeRequestTypeDef(
    _RequiredDescribeFpgaImageAttributeRequestTypeDef,
    _OptionalDescribeFpgaImageAttributeRequestTypeDef,
):
    pass


DescribeFpgaImageAttributeResultResponseTypeDef = TypedDict(
    "DescribeFpgaImageAttributeResultResponseTypeDef",
    {
        "FpgaImageAttribute": "FpgaImageAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFpgaImagesRequestTypeDef = TypedDict(
    "DescribeFpgaImagesRequestTypeDef",
    {
        "DryRun": bool,
        "FpgaImageIds": List[str],
        "Owners": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeFpgaImagesResultResponseTypeDef = TypedDict(
    "DescribeFpgaImagesResultResponseTypeDef",
    {
        "FpgaImages": List["FpgaImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostReservationOfferingsRequestTypeDef = TypedDict(
    "DescribeHostReservationOfferingsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxDuration": int,
        "MaxResults": int,
        "MinDuration": int,
        "NextToken": str,
        "OfferingId": str,
    },
    total=False,
)

DescribeHostReservationOfferingsResultResponseTypeDef = TypedDict(
    "DescribeHostReservationOfferingsResultResponseTypeDef",
    {
        "NextToken": str,
        "OfferingSet": List["HostOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostReservationsRequestTypeDef = TypedDict(
    "DescribeHostReservationsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "HostReservationIdSet": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeHostReservationsResultResponseTypeDef = TypedDict(
    "DescribeHostReservationsResultResponseTypeDef",
    {
        "HostReservationSet": List["HostReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostsRequestTypeDef = TypedDict(
    "DescribeHostsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "HostIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeHostsResultResponseTypeDef = TypedDict(
    "DescribeHostsResultResponseTypeDef",
    {
        "Hosts": List["HostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIamInstanceProfileAssociationsRequestTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsRequestTypeDef",
    {
        "AssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeIamInstanceProfileAssociationsResultResponseTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsResultResponseTypeDef",
    {
        "IamInstanceProfileAssociations": List["IamInstanceProfileAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdFormatRequestTypeDef = TypedDict(
    "DescribeIdFormatRequestTypeDef",
    {
        "Resource": str,
    },
    total=False,
)

DescribeIdFormatResultResponseTypeDef = TypedDict(
    "DescribeIdFormatResultResponseTypeDef",
    {
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeIdentityIdFormatRequestTypeDef = TypedDict(
    "_RequiredDescribeIdentityIdFormatRequestTypeDef",
    {
        "PrincipalArn": str,
    },
)
_OptionalDescribeIdentityIdFormatRequestTypeDef = TypedDict(
    "_OptionalDescribeIdentityIdFormatRequestTypeDef",
    {
        "Resource": str,
    },
    total=False,
)


class DescribeIdentityIdFormatRequestTypeDef(
    _RequiredDescribeIdentityIdFormatRequestTypeDef, _OptionalDescribeIdentityIdFormatRequestTypeDef
):
    pass


DescribeIdentityIdFormatResultResponseTypeDef = TypedDict(
    "DescribeIdentityIdFormatResultResponseTypeDef",
    {
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageAttributeRequestImageTypeDef = TypedDict(
    "_RequiredDescribeImageAttributeRequestImageTypeDef",
    {
        "Attribute": ImageAttributeNameType,
    },
)
_OptionalDescribeImageAttributeRequestImageTypeDef = TypedDict(
    "_OptionalDescribeImageAttributeRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeImageAttributeRequestImageTypeDef(
    _RequiredDescribeImageAttributeRequestImageTypeDef,
    _OptionalDescribeImageAttributeRequestImageTypeDef,
):
    pass


_RequiredDescribeImageAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeImageAttributeRequestTypeDef",
    {
        "Attribute": ImageAttributeNameType,
        "ImageId": str,
    },
)
_OptionalDescribeImageAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeImageAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeImageAttributeRequestTypeDef(
    _RequiredDescribeImageAttributeRequestTypeDef, _OptionalDescribeImageAttributeRequestTypeDef
):
    pass


DescribeImagesRequestTypeDef = TypedDict(
    "DescribeImagesRequestTypeDef",
    {
        "ExecutableUsers": List[str],
        "Filters": List["FilterTypeDef"],
        "ImageIds": List[str],
        "Owners": List[str],
        "IncludeDeprecated": bool,
        "DryRun": bool,
    },
    total=False,
)

DescribeImagesResultResponseTypeDef = TypedDict(
    "DescribeImagesResultResponseTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportImageTasksRequestTypeDef = TypedDict(
    "DescribeImportImageTasksRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "ImportTaskIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImportImageTasksResultResponseTypeDef = TypedDict(
    "DescribeImportImageTasksResultResponseTypeDef",
    {
        "ImportImageTasks": List["ImportImageTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportSnapshotTasksRequestTypeDef = TypedDict(
    "DescribeImportSnapshotTasksRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "ImportTaskIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImportSnapshotTasksResultResponseTypeDef = TypedDict(
    "DescribeImportSnapshotTasksResultResponseTypeDef",
    {
        "ImportSnapshotTasks": List["ImportSnapshotTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_RequiredDescribeInstanceAttributeRequestInstanceTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
    },
)
_OptionalDescribeInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_OptionalDescribeInstanceAttributeRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeInstanceAttributeRequestInstanceTypeDef(
    _RequiredDescribeInstanceAttributeRequestInstanceTypeDef,
    _OptionalDescribeInstanceAttributeRequestInstanceTypeDef,
):
    pass


_RequiredDescribeInstanceAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeInstanceAttributeRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
    },
)
_OptionalDescribeInstanceAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeInstanceAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeInstanceAttributeRequestTypeDef(
    _RequiredDescribeInstanceAttributeRequestTypeDef,
    _OptionalDescribeInstanceAttributeRequestTypeDef,
):
    pass


DescribeInstanceCreditSpecificationsRequestTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "InstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceCreditSpecificationsResultResponseTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsResultResponseTypeDef",
    {
        "InstanceCreditSpecifications": List["InstanceCreditSpecificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceEventNotificationAttributesRequestTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DescribeInstanceEventNotificationAttributesResultResponseTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesResultResponseTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStatusRequestTypeDef = TypedDict(
    "DescribeInstanceStatusRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "InstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
        "IncludeAllInstances": bool,
    },
    total=False,
)

DescribeInstanceStatusResultResponseTypeDef = TypedDict(
    "DescribeInstanceStatusResultResponseTypeDef",
    {
        "InstanceStatuses": List["InstanceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypeOfferingsRequestTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsRequestTypeDef",
    {
        "DryRun": bool,
        "LocationType": LocationTypeType,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceTypeOfferingsResultResponseTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsResultResponseTypeDef",
    {
        "InstanceTypeOfferings": List["InstanceTypeOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypesRequestTypeDef = TypedDict(
    "DescribeInstanceTypesRequestTypeDef",
    {
        "DryRun": bool,
        "InstanceTypes": List[InstanceTypeType],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceTypesResultResponseTypeDef = TypedDict(
    "DescribeInstanceTypesResultResponseTypeDef",
    {
        "InstanceTypes": List["InstanceTypeInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesRequestTypeDef = TypedDict(
    "DescribeInstancesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "InstanceIds": List[str],
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstancesResultResponseTypeDef = TypedDict(
    "DescribeInstancesResultResponseTypeDef",
    {
        "Reservations": List["ReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInternetGatewaysRequestTypeDef = TypedDict(
    "DescribeInternetGatewaysRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "InternetGatewayIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeInternetGatewaysResultResponseTypeDef = TypedDict(
    "DescribeInternetGatewaysResultResponseTypeDef",
    {
        "InternetGateways": List["InternetGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpv6PoolsRequestTypeDef = TypedDict(
    "DescribeIpv6PoolsRequestTypeDef",
    {
        "PoolIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeIpv6PoolsResultResponseTypeDef = TypedDict(
    "DescribeIpv6PoolsResultResponseTypeDef",
    {
        "Ipv6Pools": List["Ipv6PoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyPairsRequestTypeDef = TypedDict(
    "DescribeKeyPairsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "KeyNames": List[str],
        "KeyPairIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeKeyPairsResultResponseTypeDef = TypedDict(
    "DescribeKeyPairsResultResponseTypeDef",
    {
        "KeyPairs": List["KeyPairInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchTemplateVersionsRequestTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Versions": List[str],
        "MinVersion": str,
        "MaxVersion": str,
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeLaunchTemplateVersionsResultResponseTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsResultResponseTypeDef",
    {
        "LaunchTemplateVersions": List["LaunchTemplateVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchTemplatesRequestTypeDef = TypedDict(
    "DescribeLaunchTemplatesRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateIds": List[str],
        "LaunchTemplateNames": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeLaunchTemplatesResultResponseTypeDef = TypedDict(
    "DescribeLaunchTemplatesResultResponseTypeDef",
    {
        "LaunchTemplates": List["LaunchTemplateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultResponseTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultResponseTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociations": List[
            "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTableVpcAssociationsRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayRouteTableVpcAssociationsResultResponseTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsResultResponseTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociations": List[
            "LocalGatewayRouteTableVpcAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTablesRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesRequestTypeDef",
    {
        "LocalGatewayRouteTableIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayRouteTablesResultResponseTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesResultResponseTypeDef",
    {
        "LocalGatewayRouteTables": List["LocalGatewayRouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayVirtualInterfaceGroupsRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayVirtualInterfaceGroupsResultResponseTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsResultResponseTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroups": List["LocalGatewayVirtualInterfaceGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayVirtualInterfacesRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayVirtualInterfacesResultResponseTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesResultResponseTypeDef",
    {
        "LocalGatewayVirtualInterfaces": List["LocalGatewayVirtualInterfaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewaysRequestTypeDef = TypedDict(
    "DescribeLocalGatewaysRequestTypeDef",
    {
        "LocalGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewaysResultResponseTypeDef = TypedDict(
    "DescribeLocalGatewaysResultResponseTypeDef",
    {
        "LocalGateways": List["LocalGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedPrefixListsRequestTypeDef = TypedDict(
    "DescribeManagedPrefixListsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "PrefixListIds": List[str],
    },
    total=False,
)

DescribeManagedPrefixListsResultResponseTypeDef = TypedDict(
    "DescribeManagedPrefixListsResultResponseTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List["ManagedPrefixListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMovingAddressesRequestTypeDef = TypedDict(
    "DescribeMovingAddressesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "PublicIps": List[str],
    },
    total=False,
)

DescribeMovingAddressesResultResponseTypeDef = TypedDict(
    "DescribeMovingAddressesResultResponseTypeDef",
    {
        "MovingAddressStatuses": List["MovingAddressStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNatGatewaysRequestTypeDef = TypedDict(
    "DescribeNatGatewaysRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NatGatewayIds": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeNatGatewaysResultResponseTypeDef = TypedDict(
    "DescribeNatGatewaysResultResponseTypeDef",
    {
        "NatGateways": List["NatGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkAclsRequestTypeDef = TypedDict(
    "DescribeNetworkAclsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NetworkAclIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeNetworkAclsResultResponseTypeDef = TypedDict(
    "DescribeNetworkAclsResultResponseTypeDef",
    {
        "NetworkAcls": List["NetworkAclTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAnalysesRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesRequestTypeDef",
    {
        "NetworkInsightsAnalysisIds": List[str],
        "NetworkInsightsPathId": str,
        "AnalysisStartTime": Union[datetime, str],
        "AnalysisEndTime": Union[datetime, str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeNetworkInsightsAnalysesResultResponseTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesResultResponseTypeDef",
    {
        "NetworkInsightsAnalyses": List["NetworkInsightsAnalysisTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsPathsRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsRequestTypeDef",
    {
        "NetworkInsightsPathIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeNetworkInsightsPathsResultResponseTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsResultResponseTypeDef",
    {
        "NetworkInsightsPaths": List["NetworkInsightsPathTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    {
        "Attribute": NetworkInterfaceAttributeType,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDescribeNetworkInterfaceAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeNetworkInterfaceAttributeRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalDescribeNetworkInterfaceAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeNetworkInterfaceAttributeRequestTypeDef",
    {
        "Attribute": NetworkInterfaceAttributeType,
        "DryRun": bool,
    },
    total=False,
)


class DescribeNetworkInterfaceAttributeRequestTypeDef(
    _RequiredDescribeNetworkInterfaceAttributeRequestTypeDef,
    _OptionalDescribeNetworkInterfaceAttributeRequestTypeDef,
):
    pass


DescribeNetworkInterfaceAttributeResultResponseTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeResultResponseTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "Description": "AttributeValueTypeDef",
        "Groups": List["GroupIdentifierTypeDef"],
        "NetworkInterfaceId": str,
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfacePermissionsRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsRequestTypeDef",
    {
        "NetworkInterfacePermissionIds": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeNetworkInterfacePermissionsResultResponseTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsResultResponseTypeDef",
    {
        "NetworkInterfacePermissions": List["NetworkInterfacePermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfacesRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NetworkInterfaceIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeNetworkInterfacesResultResponseTypeDef = TypedDict(
    "DescribeNetworkInterfacesResultResponseTypeDef",
    {
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlacementGroupsRequestTypeDef = TypedDict(
    "DescribePlacementGroupsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "GroupNames": List[str],
        "GroupIds": List[str],
    },
    total=False,
)

DescribePlacementGroupsResultResponseTypeDef = TypedDict(
    "DescribePlacementGroupsResultResponseTypeDef",
    {
        "PlacementGroups": List["PlacementGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrefixListsRequestTypeDef = TypedDict(
    "DescribePrefixListsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "PrefixListIds": List[str],
    },
    total=False,
)

DescribePrefixListsResultResponseTypeDef = TypedDict(
    "DescribePrefixListsResultResponseTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List["PrefixListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrincipalIdFormatRequestTypeDef = TypedDict(
    "DescribePrincipalIdFormatRequestTypeDef",
    {
        "DryRun": bool,
        "Resources": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribePrincipalIdFormatResultResponseTypeDef = TypedDict(
    "DescribePrincipalIdFormatResultResponseTypeDef",
    {
        "Principals": List["PrincipalIdFormatTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublicIpv4PoolsRequestTypeDef = TypedDict(
    "DescribePublicIpv4PoolsRequestTypeDef",
    {
        "PoolIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribePublicIpv4PoolsResultResponseTypeDef = TypedDict(
    "DescribePublicIpv4PoolsResultResponseTypeDef",
    {
        "PublicIpv4Pools": List["PublicIpv4PoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionsRequestTypeDef = TypedDict(
    "DescribeRegionsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "RegionNames": List[str],
        "DryRun": bool,
        "AllRegions": bool,
    },
    total=False,
)

DescribeRegionsResultResponseTypeDef = TypedDict(
    "DescribeRegionsResultResponseTypeDef",
    {
        "Regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplaceRootVolumeTasksRequestTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksRequestTypeDef",
    {
        "ReplaceRootVolumeTaskIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeReplaceRootVolumeTasksResultResponseTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksResultResponseTypeDef",
    {
        "ReplaceRootVolumeTasks": List["ReplaceRootVolumeTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesListingsRequestTypeDef = TypedDict(
    "DescribeReservedInstancesListingsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "ReservedInstancesId": str,
        "ReservedInstancesListingId": str,
    },
    total=False,
)

DescribeReservedInstancesListingsResultResponseTypeDef = TypedDict(
    "DescribeReservedInstancesListingsResultResponseTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesModificationsRequestTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "ReservedInstancesModificationIds": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeReservedInstancesModificationsResultResponseTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsResultResponseTypeDef",
    {
        "NextToken": str,
        "ReservedInstancesModifications": List["ReservedInstancesModificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesOfferingsRequestTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Filters": List["FilterTypeDef"],
        "IncludeMarketplace": bool,
        "InstanceType": InstanceTypeType,
        "MaxDuration": int,
        "MaxInstanceCount": int,
        "MinDuration": int,
        "OfferingClass": OfferingClassTypeType,
        "ProductDescription": RIProductDescriptionType,
        "ReservedInstancesOfferingIds": List[str],
        "DryRun": bool,
        "InstanceTenancy": TenancyType,
        "MaxResults": int,
        "NextToken": str,
        "OfferingType": OfferingTypeValuesType,
    },
    total=False,
)

DescribeReservedInstancesOfferingsResultResponseTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsResultResponseTypeDef",
    {
        "ReservedInstancesOfferings": List["ReservedInstancesOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesRequestTypeDef = TypedDict(
    "DescribeReservedInstancesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "OfferingClass": OfferingClassTypeType,
        "ReservedInstancesIds": List[str],
        "DryRun": bool,
        "OfferingType": OfferingTypeValuesType,
    },
    total=False,
)

DescribeReservedInstancesResultResponseTypeDef = TypedDict(
    "DescribeReservedInstancesResultResponseTypeDef",
    {
        "ReservedInstances": List["ReservedInstancesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteTablesRequestTypeDef = TypedDict(
    "DescribeRouteTablesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "RouteTableIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRouteTablesResultResponseTypeDef = TypedDict(
    "DescribeRouteTablesResultResponseTypeDef",
    {
        "RouteTables": List["RouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScheduledInstanceAvailabilityRequestTypeDef = TypedDict(
    "_RequiredDescribeScheduledInstanceAvailabilityRequestTypeDef",
    {
        "FirstSlotStartTimeRange": "SlotDateTimeRangeRequestTypeDef",
        "Recurrence": "ScheduledInstanceRecurrenceRequestTypeDef",
    },
)
_OptionalDescribeScheduledInstanceAvailabilityRequestTypeDef = TypedDict(
    "_OptionalDescribeScheduledInstanceAvailabilityRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "MaxSlotDurationInHours": int,
        "MinSlotDurationInHours": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeScheduledInstanceAvailabilityRequestTypeDef(
    _RequiredDescribeScheduledInstanceAvailabilityRequestTypeDef,
    _OptionalDescribeScheduledInstanceAvailabilityRequestTypeDef,
):
    pass


DescribeScheduledInstanceAvailabilityResultResponseTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityResultResponseTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceAvailabilitySet": List["ScheduledInstanceAvailabilityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledInstancesRequestTypeDef = TypedDict(
    "DescribeScheduledInstancesRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ScheduledInstanceIds": List[str],
        "SlotStartTimeRange": "SlotStartTimeRangeRequestTypeDef",
    },
    total=False,
)

DescribeScheduledInstancesResultResponseTypeDef = TypedDict(
    "DescribeScheduledInstancesResultResponseTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSecurityGroupReferencesRequestTypeDef = TypedDict(
    "_RequiredDescribeSecurityGroupReferencesRequestTypeDef",
    {
        "GroupId": List[str],
    },
)
_OptionalDescribeSecurityGroupReferencesRequestTypeDef = TypedDict(
    "_OptionalDescribeSecurityGroupReferencesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeSecurityGroupReferencesRequestTypeDef(
    _RequiredDescribeSecurityGroupReferencesRequestTypeDef,
    _OptionalDescribeSecurityGroupReferencesRequestTypeDef,
):
    pass


DescribeSecurityGroupReferencesResultResponseTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesResultResponseTypeDef",
    {
        "SecurityGroupReferenceSet": List["SecurityGroupReferenceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityGroupsRequestTypeDef = TypedDict(
    "DescribeSecurityGroupsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "GroupIds": List[str],
        "GroupNames": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSecurityGroupsResultResponseTypeDef = TypedDict(
    "DescribeSecurityGroupsResultResponseTypeDef",
    {
        "SecurityGroups": List["SecurityGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_RequiredDescribeSnapshotAttributeRequestSnapshotTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
    },
)
_OptionalDescribeSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_OptionalDescribeSnapshotAttributeRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeSnapshotAttributeRequestSnapshotTypeDef(
    _RequiredDescribeSnapshotAttributeRequestSnapshotTypeDef,
    _OptionalDescribeSnapshotAttributeRequestSnapshotTypeDef,
):
    pass


_RequiredDescribeSnapshotAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeSnapshotAttributeRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
    },
)
_OptionalDescribeSnapshotAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeSnapshotAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeSnapshotAttributeRequestTypeDef(
    _RequiredDescribeSnapshotAttributeRequestTypeDef,
    _OptionalDescribeSnapshotAttributeRequestTypeDef,
):
    pass


DescribeSnapshotAttributeResultResponseTypeDef = TypedDict(
    "DescribeSnapshotAttributeResultResponseTypeDef",
    {
        "CreateVolumePermissions": List["CreateVolumePermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "OwnerIds": List[str],
        "RestorableByUserIds": List[str],
        "SnapshotIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeSnapshotsResultResponseTypeDef = TypedDict(
    "DescribeSnapshotsResultResponseTypeDef",
    {
        "Snapshots": List["SnapshotResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotDatafeedSubscriptionRequestTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DescribeSpotDatafeedSubscriptionResultResponseTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionResultResponseTypeDef",
    {
        "SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSpotFleetInstancesRequestTypeDef = TypedDict(
    "_RequiredDescribeSpotFleetInstancesRequestTypeDef",
    {
        "SpotFleetRequestId": str,
    },
)
_OptionalDescribeSpotFleetInstancesRequestTypeDef = TypedDict(
    "_OptionalDescribeSpotFleetInstancesRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeSpotFleetInstancesRequestTypeDef(
    _RequiredDescribeSpotFleetInstancesRequestTypeDef,
    _OptionalDescribeSpotFleetInstancesRequestTypeDef,
):
    pass


DescribeSpotFleetInstancesResponseResponseTypeDef = TypedDict(
    "DescribeSpotFleetInstancesResponseResponseTypeDef",
    {
        "ActiveInstances": List["ActiveInstanceTypeDef"],
        "NextToken": str,
        "SpotFleetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSpotFleetRequestHistoryRequestTypeDef = TypedDict(
    "_RequiredDescribeSpotFleetRequestHistoryRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "StartTime": Union[datetime, str],
    },
)
_OptionalDescribeSpotFleetRequestHistoryRequestTypeDef = TypedDict(
    "_OptionalDescribeSpotFleetRequestHistoryRequestTypeDef",
    {
        "DryRun": bool,
        "EventType": EventTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeSpotFleetRequestHistoryRequestTypeDef(
    _RequiredDescribeSpotFleetRequestHistoryRequestTypeDef,
    _OptionalDescribeSpotFleetRequestHistoryRequestTypeDef,
):
    pass


DescribeSpotFleetRequestHistoryResponseResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryResponseResponseTypeDef",
    {
        "HistoryRecords": List["HistoryRecordTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "SpotFleetRequestId": str,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotFleetRequestsRequestTypeDef = TypedDict(
    "DescribeSpotFleetRequestsRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "SpotFleetRequestIds": List[str],
    },
    total=False,
)

DescribeSpotFleetRequestsResponseResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestsResponseResponseTypeDef",
    {
        "NextToken": str,
        "SpotFleetRequestConfigs": List["SpotFleetRequestConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotInstanceRequestsRequestTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "SpotInstanceRequestIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSpotInstanceRequestsResultResponseTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsResultResponseTypeDef",
    {
        "SpotInstanceRequests": List["SpotInstanceRequestTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotPriceHistoryRequestTypeDef = TypedDict(
    "DescribeSpotPriceHistoryRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "AvailabilityZone": str,
        "DryRun": bool,
        "EndTime": Union[datetime, str],
        "InstanceTypes": List[InstanceTypeType],
        "MaxResults": int,
        "NextToken": str,
        "ProductDescriptions": List[str],
        "StartTime": Union[datetime, str],
    },
    total=False,
)

DescribeSpotPriceHistoryResultResponseTypeDef = TypedDict(
    "DescribeSpotPriceHistoryResultResponseTypeDef",
    {
        "NextToken": str,
        "SpotPriceHistory": List["SpotPriceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStaleSecurityGroupsRequestTypeDef = TypedDict(
    "_RequiredDescribeStaleSecurityGroupsRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDescribeStaleSecurityGroupsRequestTypeDef = TypedDict(
    "_OptionalDescribeStaleSecurityGroupsRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeStaleSecurityGroupsRequestTypeDef(
    _RequiredDescribeStaleSecurityGroupsRequestTypeDef,
    _OptionalDescribeStaleSecurityGroupsRequestTypeDef,
):
    pass


DescribeStaleSecurityGroupsResultResponseTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsResultResponseTypeDef",
    {
        "NextToken": str,
        "StaleSecurityGroupSet": List["StaleSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStoreImageTasksRequestTypeDef = TypedDict(
    "DescribeStoreImageTasksRequestTypeDef",
    {
        "ImageIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeStoreImageTasksResultResponseTypeDef = TypedDict(
    "DescribeStoreImageTasksResultResponseTypeDef",
    {
        "StoreImageTaskResults": List["StoreImageTaskResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubnetsRequestTypeDef = TypedDict(
    "DescribeSubnetsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "SubnetIds": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSubnetsResultResponseTypeDef = TypedDict(
    "DescribeSubnetsResultResponseTypeDef",
    {
        "Subnets": List["SubnetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestTypeDef = TypedDict(
    "DescribeTagsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTagsResultResponseTypeDef = TypedDict(
    "DescribeTagsResultResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorFiltersRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersRequestTypeDef",
    {
        "TrafficMirrorFilterIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTrafficMirrorFiltersResultResponseTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersResultResponseTypeDef",
    {
        "TrafficMirrorFilters": List["TrafficMirrorFilterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorSessionsRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsRequestTypeDef",
    {
        "TrafficMirrorSessionIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTrafficMirrorSessionsResultResponseTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsResultResponseTypeDef",
    {
        "TrafficMirrorSessions": List["TrafficMirrorSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorTargetsRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsRequestTypeDef",
    {
        "TrafficMirrorTargetIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTrafficMirrorTargetsResultResponseTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsResultResponseTypeDef",
    {
        "TrafficMirrorTargets": List["TrafficMirrorTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayAttachmentsRequestTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayAttachmentsResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsResultResponseTypeDef",
    {
        "TransitGatewayAttachments": List["TransitGatewayAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayConnectPeersRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersRequestTypeDef",
    {
        "TransitGatewayConnectPeerIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayConnectPeersResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersResultResponseTypeDef",
    {
        "TransitGatewayConnectPeers": List["TransitGatewayConnectPeerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayConnectsRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayConnectsResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsResultResponseTypeDef",
    {
        "TransitGatewayConnects": List["TransitGatewayConnectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayMulticastDomainsRequestTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsRequestTypeDef",
    {
        "TransitGatewayMulticastDomainIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayMulticastDomainsResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsResultResponseTypeDef",
    {
        "TransitGatewayMulticastDomains": List["TransitGatewayMulticastDomainTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayPeeringAttachmentsRequestTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayPeeringAttachmentsResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsResultResponseTypeDef",
    {
        "TransitGatewayPeeringAttachments": List["TransitGatewayPeeringAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayRouteTablesRequestTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesRequestTypeDef",
    {
        "TransitGatewayRouteTableIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayRouteTablesResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesResultResponseTypeDef",
    {
        "TransitGatewayRouteTables": List["TransitGatewayRouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayVpcAttachmentsRequestTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayVpcAttachmentsResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsResultResponseTypeDef",
    {
        "TransitGatewayVpcAttachments": List["TransitGatewayVpcAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewaysRequestTypeDef = TypedDict(
    "DescribeTransitGatewaysRequestTypeDef",
    {
        "TransitGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewaysResultResponseTypeDef = TypedDict(
    "DescribeTransitGatewaysResultResponseTypeDef",
    {
        "TransitGateways": List["TransitGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrunkInterfaceAssociationsRequestTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsRequestTypeDef",
    {
        "AssociationIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeTrunkInterfaceAssociationsResultResponseTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsResultResponseTypeDef",
    {
        "InterfaceAssociations": List["TrunkInterfaceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVolumeAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeVolumeAttributeRequestTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
        "VolumeId": str,
    },
)
_OptionalDescribeVolumeAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeVolumeAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeVolumeAttributeRequestTypeDef(
    _RequiredDescribeVolumeAttributeRequestTypeDef, _OptionalDescribeVolumeAttributeRequestTypeDef
):
    pass


_RequiredDescribeVolumeAttributeRequestVolumeTypeDef = TypedDict(
    "_RequiredDescribeVolumeAttributeRequestVolumeTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
    },
)
_OptionalDescribeVolumeAttributeRequestVolumeTypeDef = TypedDict(
    "_OptionalDescribeVolumeAttributeRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeVolumeAttributeRequestVolumeTypeDef(
    _RequiredDescribeVolumeAttributeRequestVolumeTypeDef,
    _OptionalDescribeVolumeAttributeRequestVolumeTypeDef,
):
    pass


DescribeVolumeAttributeResultResponseTypeDef = TypedDict(
    "DescribeVolumeAttributeResultResponseTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "VolumeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumeStatusRequestTypeDef = TypedDict(
    "DescribeVolumeStatusRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "VolumeIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeVolumeStatusRequestVolumeTypeDef = TypedDict(
    "DescribeVolumeStatusRequestVolumeTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeVolumeStatusResultResponseTypeDef = TypedDict(
    "DescribeVolumeStatusResultResponseTypeDef",
    {
        "NextToken": str,
        "VolumeStatuses": List["VolumeStatusItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesModificationsRequestTypeDef = TypedDict(
    "DescribeVolumesModificationsRequestTypeDef",
    {
        "DryRun": bool,
        "VolumeIds": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVolumesModificationsResultResponseTypeDef = TypedDict(
    "DescribeVolumesModificationsResultResponseTypeDef",
    {
        "VolumesModifications": List["VolumeModificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestTypeDef = TypedDict(
    "DescribeVolumesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VolumeIds": List[str],
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVolumesResultResponseTypeDef = TypedDict(
    "DescribeVolumesResultResponseTypeDef",
    {
        "Volumes": List["VolumeResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVpcAttributeRequestTypeDef = TypedDict(
    "_RequiredDescribeVpcAttributeRequestTypeDef",
    {
        "Attribute": VpcAttributeNameType,
        "VpcId": str,
    },
)
_OptionalDescribeVpcAttributeRequestTypeDef = TypedDict(
    "_OptionalDescribeVpcAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeVpcAttributeRequestTypeDef(
    _RequiredDescribeVpcAttributeRequestTypeDef, _OptionalDescribeVpcAttributeRequestTypeDef
):
    pass


_RequiredDescribeVpcAttributeRequestVpcTypeDef = TypedDict(
    "_RequiredDescribeVpcAttributeRequestVpcTypeDef",
    {
        "Attribute": VpcAttributeNameType,
    },
)
_OptionalDescribeVpcAttributeRequestVpcTypeDef = TypedDict(
    "_OptionalDescribeVpcAttributeRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DescribeVpcAttributeRequestVpcTypeDef(
    _RequiredDescribeVpcAttributeRequestVpcTypeDef, _OptionalDescribeVpcAttributeRequestVpcTypeDef
):
    pass


DescribeVpcAttributeResultResponseTypeDef = TypedDict(
    "DescribeVpcAttributeResultResponseTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcClassicLinkDnsSupportRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "VpcIds": List[str],
    },
    total=False,
)

DescribeVpcClassicLinkDnsSupportResultResponseTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportResultResponseTypeDef",
    {
        "NextToken": str,
        "Vpcs": List["ClassicLinkDnsSupportTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcClassicLinkRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "VpcIds": List[str],
    },
    total=False,
)

DescribeVpcClassicLinkResultResponseTypeDef = TypedDict(
    "DescribeVpcClassicLinkResultResponseTypeDef",
    {
        "Vpcs": List["VpcClassicLinkTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointConnectionNotificationsRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsRequestTypeDef",
    {
        "DryRun": bool,
        "ConnectionNotificationId": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointConnectionNotificationsResultResponseTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsResultResponseTypeDef",
    {
        "ConnectionNotificationSet": List["ConnectionNotificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointConnectionsRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointConnectionsResultResponseTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsResultResponseTypeDef",
    {
        "VpcEndpointConnections": List["VpcEndpointConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServiceConfigurationsRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsRequestTypeDef",
    {
        "DryRun": bool,
        "ServiceIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointServiceConfigurationsResultResponseTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsResultResponseTypeDef",
    {
        "ServiceConfigurations": List["ServiceConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVpcEndpointServicePermissionsRequestTypeDef = TypedDict(
    "_RequiredDescribeVpcEndpointServicePermissionsRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalDescribeVpcEndpointServicePermissionsRequestTypeDef = TypedDict(
    "_OptionalDescribeVpcEndpointServicePermissionsRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeVpcEndpointServicePermissionsRequestTypeDef(
    _RequiredDescribeVpcEndpointServicePermissionsRequestTypeDef,
    _OptionalDescribeVpcEndpointServicePermissionsRequestTypeDef,
):
    pass


DescribeVpcEndpointServicePermissionsResultResponseTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsResultResponseTypeDef",
    {
        "AllowedPrincipals": List["AllowedPrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServicesRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServicesRequestTypeDef",
    {
        "DryRun": bool,
        "ServiceNames": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointServicesResultResponseTypeDef = TypedDict(
    "DescribeVpcEndpointServicesResultResponseTypeDef",
    {
        "ServiceNames": List[str],
        "ServiceDetails": List["ServiceDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointsRequestTypeDef = TypedDict(
    "DescribeVpcEndpointsRequestTypeDef",
    {
        "DryRun": bool,
        "VpcEndpointIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointsResultResponseTypeDef = TypedDict(
    "DescribeVpcEndpointsResultResponseTypeDef",
    {
        "VpcEndpoints": List["VpcEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "VpcPeeringConnectionIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVpcPeeringConnectionsResultResponseTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsResultResponseTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcsRequestTypeDef = TypedDict(
    "DescribeVpcsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VpcIds": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVpcsResultResponseTypeDef = TypedDict(
    "DescribeVpcsResultResponseTypeDef",
    {
        "Vpcs": List["VpcTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpnConnectionsRequestTypeDef = TypedDict(
    "DescribeVpnConnectionsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VpnConnectionIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeVpnConnectionsResultResponseTypeDef = TypedDict(
    "DescribeVpnConnectionsResultResponseTypeDef",
    {
        "VpnConnections": List["VpnConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpnGatewaysRequestTypeDef = TypedDict(
    "DescribeVpnGatewaysRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VpnGatewayIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeVpnGatewaysResultResponseTypeDef = TypedDict(
    "DescribeVpnGatewaysResultResponseTypeDef",
    {
        "VpnGateways": List["VpnGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_RequiredDetachClassicLinkVpcRequestInstanceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDetachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_OptionalDetachClassicLinkVpcRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachClassicLinkVpcRequestInstanceTypeDef(
    _RequiredDetachClassicLinkVpcRequestInstanceTypeDef,
    _OptionalDetachClassicLinkVpcRequestInstanceTypeDef,
):
    pass


_RequiredDetachClassicLinkVpcRequestTypeDef = TypedDict(
    "_RequiredDetachClassicLinkVpcRequestTypeDef",
    {
        "InstanceId": str,
        "VpcId": str,
    },
)
_OptionalDetachClassicLinkVpcRequestTypeDef = TypedDict(
    "_OptionalDetachClassicLinkVpcRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachClassicLinkVpcRequestTypeDef(
    _RequiredDetachClassicLinkVpcRequestTypeDef, _OptionalDetachClassicLinkVpcRequestTypeDef
):
    pass


_RequiredDetachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_RequiredDetachClassicLinkVpcRequestVpcTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDetachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_OptionalDetachClassicLinkVpcRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachClassicLinkVpcRequestVpcTypeDef(
    _RequiredDetachClassicLinkVpcRequestVpcTypeDef, _OptionalDetachClassicLinkVpcRequestVpcTypeDef
):
    pass


DetachClassicLinkVpcResultResponseTypeDef = TypedDict(
    "DetachClassicLinkVpcResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_RequiredDetachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDetachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_OptionalDetachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachInternetGatewayRequestInternetGatewayTypeDef(
    _RequiredDetachInternetGatewayRequestInternetGatewayTypeDef,
    _OptionalDetachInternetGatewayRequestInternetGatewayTypeDef,
):
    pass


_RequiredDetachInternetGatewayRequestTypeDef = TypedDict(
    "_RequiredDetachInternetGatewayRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
    },
)
_OptionalDetachInternetGatewayRequestTypeDef = TypedDict(
    "_OptionalDetachInternetGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachInternetGatewayRequestTypeDef(
    _RequiredDetachInternetGatewayRequestTypeDef, _OptionalDetachInternetGatewayRequestTypeDef
):
    pass


_RequiredDetachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_RequiredDetachInternetGatewayRequestVpcTypeDef",
    {
        "InternetGatewayId": str,
    },
)
_OptionalDetachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_OptionalDetachInternetGatewayRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachInternetGatewayRequestVpcTypeDef(
    _RequiredDetachInternetGatewayRequestVpcTypeDef, _OptionalDetachInternetGatewayRequestVpcTypeDef
):
    pass


_RequiredDetachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_RequiredDetachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "AttachmentId": str,
    },
)
_OptionalDetachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_OptionalDetachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)


class DetachNetworkInterfaceRequestNetworkInterfaceTypeDef(
    _RequiredDetachNetworkInterfaceRequestNetworkInterfaceTypeDef,
    _OptionalDetachNetworkInterfaceRequestNetworkInterfaceTypeDef,
):
    pass


_RequiredDetachNetworkInterfaceRequestTypeDef = TypedDict(
    "_RequiredDetachNetworkInterfaceRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
_OptionalDetachNetworkInterfaceRequestTypeDef = TypedDict(
    "_OptionalDetachNetworkInterfaceRequestTypeDef",
    {
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)


class DetachNetworkInterfaceRequestTypeDef(
    _RequiredDetachNetworkInterfaceRequestTypeDef, _OptionalDetachNetworkInterfaceRequestTypeDef
):
    pass


_RequiredDetachVolumeRequestInstanceTypeDef = TypedDict(
    "_RequiredDetachVolumeRequestInstanceTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDetachVolumeRequestInstanceTypeDef = TypedDict(
    "_OptionalDetachVolumeRequestInstanceTypeDef",
    {
        "Device": str,
        "Force": bool,
        "DryRun": bool,
    },
    total=False,
)


class DetachVolumeRequestInstanceTypeDef(
    _RequiredDetachVolumeRequestInstanceTypeDef, _OptionalDetachVolumeRequestInstanceTypeDef
):
    pass


_RequiredDetachVolumeRequestTypeDef = TypedDict(
    "_RequiredDetachVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDetachVolumeRequestTypeDef = TypedDict(
    "_OptionalDetachVolumeRequestTypeDef",
    {
        "Device": str,
        "Force": bool,
        "InstanceId": str,
        "DryRun": bool,
    },
    total=False,
)


class DetachVolumeRequestTypeDef(
    _RequiredDetachVolumeRequestTypeDef, _OptionalDetachVolumeRequestTypeDef
):
    pass


DetachVolumeRequestVolumeTypeDef = TypedDict(
    "DetachVolumeRequestVolumeTypeDef",
    {
        "Device": str,
        "Force": bool,
        "InstanceId": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDetachVpnGatewayRequestTypeDef = TypedDict(
    "_RequiredDetachVpnGatewayRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
    },
)
_OptionalDetachVpnGatewayRequestTypeDef = TypedDict(
    "_OptionalDetachVpnGatewayRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DetachVpnGatewayRequestTypeDef(
    _RequiredDetachVpnGatewayRequestTypeDef, _OptionalDetachVpnGatewayRequestTypeDef
):
    pass


DhcpConfigurationTypeDef = TypedDict(
    "DhcpConfigurationTypeDef",
    {
        "Key": str,
        "Values": List["AttributeValueTypeDef"],
    },
    total=False,
)

DhcpOptionsTypeDef = TypedDict(
    "DhcpOptionsTypeDef",
    {
        "DhcpConfigurations": List["DhcpConfigurationTypeDef"],
        "DhcpOptionsId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DirectoryServiceAuthenticationRequestTypeDef = TypedDict(
    "DirectoryServiceAuthenticationRequestTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

DirectoryServiceAuthenticationTypeDef = TypedDict(
    "DirectoryServiceAuthenticationTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

DisableEbsEncryptionByDefaultRequestTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableEbsEncryptionByDefaultResultResponseTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultResultResponseTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": str,
        "FastSnapshotRestoreStateErrors": List["DisableFastSnapshotRestoreStateErrorItemTypeDef"],
    },
    total=False,
)

DisableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": str,
        "Error": "DisableFastSnapshotRestoreStateErrorTypeDef",
    },
    total=False,
)

DisableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

DisableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": FastSnapshotRestoreStateCodeType,
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

_RequiredDisableFastSnapshotRestoresRequestTypeDef = TypedDict(
    "_RequiredDisableFastSnapshotRestoresRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "SourceSnapshotIds": List[str],
    },
)
_OptionalDisableFastSnapshotRestoresRequestTypeDef = TypedDict(
    "_OptionalDisableFastSnapshotRestoresRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisableFastSnapshotRestoresRequestTypeDef(
    _RequiredDisableFastSnapshotRestoresRequestTypeDef,
    _OptionalDisableFastSnapshotRestoresRequestTypeDef,
):
    pass


DisableFastSnapshotRestoresResultResponseTypeDef = TypedDict(
    "DisableFastSnapshotRestoresResultResponseTypeDef",
    {
        "Successful": List["DisableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["DisableFastSnapshotRestoreErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableImageDeprecationRequestTypeDef = TypedDict(
    "_RequiredDisableImageDeprecationRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDisableImageDeprecationRequestTypeDef = TypedDict(
    "_OptionalDisableImageDeprecationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisableImageDeprecationRequestTypeDef(
    _RequiredDisableImageDeprecationRequestTypeDef, _OptionalDisableImageDeprecationRequestTypeDef
):
    pass


DisableImageDeprecationResultResponseTypeDef = TypedDict(
    "DisableImageDeprecationResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableSerialConsoleAccessRequestTypeDef = TypedDict(
    "DisableSerialConsoleAccessRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableSerialConsoleAccessResultResponseTypeDef = TypedDict(
    "DisableSerialConsoleAccessResultResponseTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableTransitGatewayRouteTablePropagationRequestTypeDef = TypedDict(
    "_RequiredDisableTransitGatewayRouteTablePropagationRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDisableTransitGatewayRouteTablePropagationRequestTypeDef = TypedDict(
    "_OptionalDisableTransitGatewayRouteTablePropagationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisableTransitGatewayRouteTablePropagationRequestTypeDef(
    _RequiredDisableTransitGatewayRouteTablePropagationRequestTypeDef,
    _OptionalDisableTransitGatewayRouteTablePropagationRequestTypeDef,
):
    pass


DisableTransitGatewayRouteTablePropagationResultResponseTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationResultResponseTypeDef",
    {
        "Propagation": "TransitGatewayPropagationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableVgwRoutePropagationRequestTypeDef = TypedDict(
    "_RequiredDisableVgwRoutePropagationRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
    },
)
_OptionalDisableVgwRoutePropagationRequestTypeDef = TypedDict(
    "_OptionalDisableVgwRoutePropagationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisableVgwRoutePropagationRequestTypeDef(
    _RequiredDisableVgwRoutePropagationRequestTypeDef,
    _OptionalDisableVgwRoutePropagationRequestTypeDef,
):
    pass


DisableVpcClassicLinkDnsSupportRequestTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportRequestTypeDef",
    {
        "VpcId": str,
    },
    total=False,
)

DisableVpcClassicLinkDnsSupportResultResponseTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableVpcClassicLinkRequestTypeDef = TypedDict(
    "_RequiredDisableVpcClassicLinkRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDisableVpcClassicLinkRequestTypeDef = TypedDict(
    "_OptionalDisableVpcClassicLinkRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisableVpcClassicLinkRequestTypeDef(
    _RequiredDisableVpcClassicLinkRequestTypeDef, _OptionalDisableVpcClassicLinkRequestTypeDef
):
    pass


DisableVpcClassicLinkRequestVpcTypeDef = TypedDict(
    "DisableVpcClassicLinkRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableVpcClassicLinkResultResponseTypeDef = TypedDict(
    "DisableVpcClassicLinkResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAddressRequestClassicAddressTypeDef = TypedDict(
    "DisassociateAddressRequestClassicAddressTypeDef",
    {
        "AssociationId": str,
        "PublicIp": str,
        "DryRun": bool,
    },
    total=False,
)

DisassociateAddressRequestNetworkInterfaceAssociationTypeDef = TypedDict(
    "DisassociateAddressRequestNetworkInterfaceAssociationTypeDef",
    {
        "PublicIp": str,
        "DryRun": bool,
    },
    total=False,
)

DisassociateAddressRequestTypeDef = TypedDict(
    "DisassociateAddressRequestTypeDef",
    {
        "AssociationId": str,
        "PublicIp": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDisassociateClientVpnTargetNetworkRequestTypeDef = TypedDict(
    "_RequiredDisassociateClientVpnTargetNetworkRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationId": str,
    },
)
_OptionalDisassociateClientVpnTargetNetworkRequestTypeDef = TypedDict(
    "_OptionalDisassociateClientVpnTargetNetworkRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateClientVpnTargetNetworkRequestTypeDef(
    _RequiredDisassociateClientVpnTargetNetworkRequestTypeDef,
    _OptionalDisassociateClientVpnTargetNetworkRequestTypeDef,
):
    pass


DisassociateClientVpnTargetNetworkResultResponseTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkResultResponseTypeDef",
    {
        "AssociationId": str,
        "Status": "AssociationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateEnclaveCertificateIamRoleRequestTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleRequestTypeDef",
    {
        "CertificateArn": str,
        "RoleArn": str,
        "DryRun": bool,
    },
    total=False,
)

DisassociateEnclaveCertificateIamRoleResultResponseTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateIamInstanceProfileRequestTypeDef = TypedDict(
    "DisassociateIamInstanceProfileRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateIamInstanceProfileResultResponseTypeDef = TypedDict(
    "DisassociateIamInstanceProfileResultResponseTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRouteTableRequestRouteTableAssociationTypeDef = TypedDict(
    "DisassociateRouteTableRequestRouteTableAssociationTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDisassociateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_RequiredDisassociateRouteTableRequestServiceResourceTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDisassociateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_OptionalDisassociateRouteTableRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateRouteTableRequestServiceResourceTypeDef(
    _RequiredDisassociateRouteTableRequestServiceResourceTypeDef,
    _OptionalDisassociateRouteTableRequestServiceResourceTypeDef,
):
    pass


_RequiredDisassociateRouteTableRequestTypeDef = TypedDict(
    "_RequiredDisassociateRouteTableRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDisassociateRouteTableRequestTypeDef = TypedDict(
    "_OptionalDisassociateRouteTableRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateRouteTableRequestTypeDef(
    _RequiredDisassociateRouteTableRequestTypeDef, _OptionalDisassociateRouteTableRequestTypeDef
):
    pass


DisassociateSubnetCidrBlockRequestTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateSubnetCidrBlockResultResponseTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockResultResponseTypeDef",
    {
        "Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef",
        "SubnetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTransitGatewayMulticastDomainRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DisassociateTransitGatewayMulticastDomainResultResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainResultResponseTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_RequiredDisassociateTransitGatewayRouteTableRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDisassociateTransitGatewayRouteTableRequestTypeDef = TypedDict(
    "_OptionalDisassociateTransitGatewayRouteTableRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class DisassociateTransitGatewayRouteTableRequestTypeDef(
    _RequiredDisassociateTransitGatewayRouteTableRequestTypeDef,
    _OptionalDisassociateTransitGatewayRouteTableRequestTypeDef,
):
    pass


DisassociateTransitGatewayRouteTableResultResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableResultResponseTypeDef",
    {
        "Association": "TransitGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateTrunkInterfaceRequestTypeDef = TypedDict(
    "_RequiredDisassociateTrunkInterfaceRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDisassociateTrunkInterfaceRequestTypeDef = TypedDict(
    "_OptionalDisassociateTrunkInterfaceRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)


class DisassociateTrunkInterfaceRequestTypeDef(
    _RequiredDisassociateTrunkInterfaceRequestTypeDef,
    _OptionalDisassociateTrunkInterfaceRequestTypeDef,
):
    pass


DisassociateTrunkInterfaceResultResponseTypeDef = TypedDict(
    "DisassociateTrunkInterfaceResultResponseTypeDef",
    {
        "Return": bool,
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateVpcCidrBlockRequestTypeDef = TypedDict(
    "DisassociateVpcCidrBlockRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateVpcCidrBlockResultResponseTypeDef = TypedDict(
    "DisassociateVpcCidrBlockResultResponseTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskImageDescriptionTypeDef = TypedDict(
    "DiskImageDescriptionTypeDef",
    {
        "Checksum": str,
        "Format": DiskImageFormatType,
        "ImportManifestUrl": str,
        "Size": int,
    },
    total=False,
)

DiskImageDetailTypeDef = TypedDict(
    "DiskImageDetailTypeDef",
    {
        "Bytes": int,
        "Format": DiskImageFormatType,
        "ImportManifestUrl": str,
    },
)

DiskImageTypeDef = TypedDict(
    "DiskImageTypeDef",
    {
        "Description": str,
        "Image": "DiskImageDetailTypeDef",
        "Volume": "VolumeDetailTypeDef",
    },
    total=False,
)

DiskImageVolumeDescriptionTypeDef = TypedDict(
    "DiskImageVolumeDescriptionTypeDef",
    {
        "Id": str,
        "Size": int,
    },
    total=False,
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "SizeInGB": int,
        "Count": int,
        "Type": DiskTypeType,
    },
    total=False,
)

DnsEntryTypeDef = TypedDict(
    "DnsEntryTypeDef",
    {
        "DnsName": str,
        "HostedZoneId": str,
    },
    total=False,
)

DnsServersOptionsModifyStructureTypeDef = TypedDict(
    "DnsServersOptionsModifyStructureTypeDef",
    {
        "CustomDnsServers": List[str],
        "Enabled": bool,
    },
    total=False,
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "DeleteOnTermination": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "KmsKeyId": str,
        "Throughput": int,
        "OutpostArn": str,
        "Encrypted": bool,
    },
    total=False,
)

EbsInfoTypeDef = TypedDict(
    "EbsInfoTypeDef",
    {
        "EbsOptimizedSupport": EbsOptimizedSupportType,
        "EncryptionSupport": EbsEncryptionSupportType,
        "EbsOptimizedInfo": "EbsOptimizedInfoTypeDef",
        "NvmeSupport": EbsNvmeSupportType,
    },
    total=False,
)

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "DeleteOnTermination": bool,
        "VolumeId": str,
    },
    total=False,
)

EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "AttachTime": datetime,
        "DeleteOnTermination": bool,
        "Status": AttachmentStatusType,
        "VolumeId": str,
    },
    total=False,
)

EbsOptimizedInfoTypeDef = TypedDict(
    "EbsOptimizedInfoTypeDef",
    {
        "BaselineBandwidthInMbps": int,
        "BaselineThroughputInMBps": float,
        "BaselineIops": int,
        "MaximumBandwidthInMbps": int,
        "MaximumThroughputInMBps": float,
        "MaximumIops": int,
    },
    total=False,
)

EfaInfoTypeDef = TypedDict(
    "EfaInfoTypeDef",
    {
        "MaximumEfaInterfaces": int,
    },
    total=False,
)

EgressOnlyInternetGatewayTypeDef = TypedDict(
    "EgressOnlyInternetGatewayTypeDef",
    {
        "Attachments": List["InternetGatewayAttachmentTypeDef"],
        "EgressOnlyInternetGatewayId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticGpuAssociationTypeDef = TypedDict(
    "ElasticGpuAssociationTypeDef",
    {
        "ElasticGpuId": str,
        "ElasticGpuAssociationId": str,
        "ElasticGpuAssociationState": str,
        "ElasticGpuAssociationTime": str,
    },
    total=False,
)

ElasticGpuHealthTypeDef = TypedDict(
    "ElasticGpuHealthTypeDef",
    {
        "Status": ElasticGpuStatusType,
    },
    total=False,
)

ElasticGpuSpecificationResponseTypeDef = TypedDict(
    "ElasticGpuSpecificationResponseTypeDef",
    {
        "Type": str,
    },
    total=False,
)

ElasticGpuSpecificationTypeDef = TypedDict(
    "ElasticGpuSpecificationTypeDef",
    {
        "Type": str,
    },
)

ElasticGpusTypeDef = TypedDict(
    "ElasticGpusTypeDef",
    {
        "ElasticGpuId": str,
        "AvailabilityZone": str,
        "ElasticGpuType": str,
        "ElasticGpuHealth": "ElasticGpuHealthTypeDef",
        "ElasticGpuState": Literal["ATTACHED"],
        "InstanceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticInferenceAcceleratorAssociationTypeDef = TypedDict(
    "ElasticInferenceAcceleratorAssociationTypeDef",
    {
        "ElasticInferenceAcceleratorArn": str,
        "ElasticInferenceAcceleratorAssociationId": str,
        "ElasticInferenceAcceleratorAssociationState": str,
        "ElasticInferenceAcceleratorAssociationTime": datetime,
    },
    total=False,
)

_RequiredElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
    },
)
_OptionalElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalElasticInferenceAcceleratorTypeDef",
    {
        "Count": int,
    },
    total=False,
)


class ElasticInferenceAcceleratorTypeDef(
    _RequiredElasticInferenceAcceleratorTypeDef, _OptionalElasticInferenceAcceleratorTypeDef
):
    pass


EnableEbsEncryptionByDefaultRequestTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableEbsEncryptionByDefaultResultResponseTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultResultResponseTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": str,
        "FastSnapshotRestoreStateErrors": List["EnableFastSnapshotRestoreStateErrorItemTypeDef"],
    },
    total=False,
)

EnableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": str,
        "Error": "EnableFastSnapshotRestoreStateErrorTypeDef",
    },
    total=False,
)

EnableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

EnableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": FastSnapshotRestoreStateCodeType,
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

_RequiredEnableFastSnapshotRestoresRequestTypeDef = TypedDict(
    "_RequiredEnableFastSnapshotRestoresRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "SourceSnapshotIds": List[str],
    },
)
_OptionalEnableFastSnapshotRestoresRequestTypeDef = TypedDict(
    "_OptionalEnableFastSnapshotRestoresRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class EnableFastSnapshotRestoresRequestTypeDef(
    _RequiredEnableFastSnapshotRestoresRequestTypeDef,
    _OptionalEnableFastSnapshotRestoresRequestTypeDef,
):
    pass


EnableFastSnapshotRestoresResultResponseTypeDef = TypedDict(
    "EnableFastSnapshotRestoresResultResponseTypeDef",
    {
        "Successful": List["EnableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["EnableFastSnapshotRestoreErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableImageDeprecationRequestTypeDef = TypedDict(
    "_RequiredEnableImageDeprecationRequestTypeDef",
    {
        "ImageId": str,
        "DeprecateAt": Union[datetime, str],
    },
)
_OptionalEnableImageDeprecationRequestTypeDef = TypedDict(
    "_OptionalEnableImageDeprecationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class EnableImageDeprecationRequestTypeDef(
    _RequiredEnableImageDeprecationRequestTypeDef, _OptionalEnableImageDeprecationRequestTypeDef
):
    pass


EnableImageDeprecationResultResponseTypeDef = TypedDict(
    "EnableImageDeprecationResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableSerialConsoleAccessRequestTypeDef = TypedDict(
    "EnableSerialConsoleAccessRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableSerialConsoleAccessResultResponseTypeDef = TypedDict(
    "EnableSerialConsoleAccessResultResponseTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableTransitGatewayRouteTablePropagationRequestTypeDef = TypedDict(
    "_RequiredEnableTransitGatewayRouteTablePropagationRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalEnableTransitGatewayRouteTablePropagationRequestTypeDef = TypedDict(
    "_OptionalEnableTransitGatewayRouteTablePropagationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class EnableTransitGatewayRouteTablePropagationRequestTypeDef(
    _RequiredEnableTransitGatewayRouteTablePropagationRequestTypeDef,
    _OptionalEnableTransitGatewayRouteTablePropagationRequestTypeDef,
):
    pass


EnableTransitGatewayRouteTablePropagationResultResponseTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationResultResponseTypeDef",
    {
        "Propagation": "TransitGatewayPropagationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableVgwRoutePropagationRequestTypeDef = TypedDict(
    "_RequiredEnableVgwRoutePropagationRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
    },
)
_OptionalEnableVgwRoutePropagationRequestTypeDef = TypedDict(
    "_OptionalEnableVgwRoutePropagationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class EnableVgwRoutePropagationRequestTypeDef(
    _RequiredEnableVgwRoutePropagationRequestTypeDef,
    _OptionalEnableVgwRoutePropagationRequestTypeDef,
):
    pass


_RequiredEnableVolumeIORequestTypeDef = TypedDict(
    "_RequiredEnableVolumeIORequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalEnableVolumeIORequestTypeDef = TypedDict(
    "_OptionalEnableVolumeIORequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class EnableVolumeIORequestTypeDef(
    _RequiredEnableVolumeIORequestTypeDef, _OptionalEnableVolumeIORequestTypeDef
):
    pass


EnableVolumeIORequestVolumeTypeDef = TypedDict(
    "EnableVolumeIORequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableVpcClassicLinkDnsSupportRequestTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportRequestTypeDef",
    {
        "VpcId": str,
    },
    total=False,
)

EnableVpcClassicLinkDnsSupportResultResponseTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableVpcClassicLinkRequestTypeDef = TypedDict(
    "_RequiredEnableVpcClassicLinkRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalEnableVpcClassicLinkRequestTypeDef = TypedDict(
    "_OptionalEnableVpcClassicLinkRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class EnableVpcClassicLinkRequestTypeDef(
    _RequiredEnableVpcClassicLinkRequestTypeDef, _OptionalEnableVpcClassicLinkRequestTypeDef
):
    pass


EnableVpcClassicLinkRequestVpcTypeDef = TypedDict(
    "EnableVpcClassicLinkRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableVpcClassicLinkResultResponseTypeDef = TypedDict(
    "EnableVpcClassicLinkResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnclaveOptionsRequestTypeDef = TypedDict(
    "EnclaveOptionsRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

EnclaveOptionsTypeDef = TypedDict(
    "EnclaveOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

EventInformationTypeDef = TypedDict(
    "EventInformationTypeDef",
    {
        "EventDescription": str,
        "EventSubType": str,
        "InstanceId": str,
    },
    total=False,
)

ExplanationTypeDef = TypedDict(
    "ExplanationTypeDef",
    {
        "Acl": "AnalysisComponentTypeDef",
        "AclRule": "AnalysisAclRuleTypeDef",
        "Address": str,
        "Addresses": List[str],
        "AttachedTo": "AnalysisComponentTypeDef",
        "AvailabilityZones": List[str],
        "Cidrs": List[str],
        "Component": "AnalysisComponentTypeDef",
        "CustomerGateway": "AnalysisComponentTypeDef",
        "Destination": "AnalysisComponentTypeDef",
        "DestinationVpc": "AnalysisComponentTypeDef",
        "Direction": str,
        "ExplanationCode": str,
        "IngressRouteTable": "AnalysisComponentTypeDef",
        "InternetGateway": "AnalysisComponentTypeDef",
        "LoadBalancerArn": str,
        "ClassicLoadBalancerListener": "AnalysisLoadBalancerListenerTypeDef",
        "LoadBalancerListenerPort": int,
        "LoadBalancerTarget": "AnalysisLoadBalancerTargetTypeDef",
        "LoadBalancerTargetGroup": "AnalysisComponentTypeDef",
        "LoadBalancerTargetGroups": List["AnalysisComponentTypeDef"],
        "LoadBalancerTargetPort": int,
        "ElasticLoadBalancerListener": "AnalysisComponentTypeDef",
        "MissingComponent": str,
        "NatGateway": "AnalysisComponentTypeDef",
        "NetworkInterface": "AnalysisComponentTypeDef",
        "PacketField": str,
        "VpcPeeringConnection": "AnalysisComponentTypeDef",
        "Port": int,
        "PortRanges": List["PortRangeTypeDef"],
        "PrefixList": "AnalysisComponentTypeDef",
        "Protocols": List[str],
        "RouteTableRoute": "AnalysisRouteTableRouteTypeDef",
        "RouteTable": "AnalysisComponentTypeDef",
        "SecurityGroup": "AnalysisComponentTypeDef",
        "SecurityGroupRule": "AnalysisSecurityGroupRuleTypeDef",
        "SecurityGroups": List["AnalysisComponentTypeDef"],
        "SourceVpc": "AnalysisComponentTypeDef",
        "State": str,
        "Subnet": "AnalysisComponentTypeDef",
        "SubnetRouteTable": "AnalysisComponentTypeDef",
        "Vpc": "AnalysisComponentTypeDef",
        "VpcEndpoint": "AnalysisComponentTypeDef",
        "VpnConnection": "AnalysisComponentTypeDef",
        "VpnGateway": "AnalysisComponentTypeDef",
    },
    total=False,
)

_RequiredExportClientVpnClientCertificateRevocationListRequestTypeDef = TypedDict(
    "_RequiredExportClientVpnClientCertificateRevocationListRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalExportClientVpnClientCertificateRevocationListRequestTypeDef = TypedDict(
    "_OptionalExportClientVpnClientCertificateRevocationListRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ExportClientVpnClientCertificateRevocationListRequestTypeDef(
    _RequiredExportClientVpnClientCertificateRevocationListRequestTypeDef,
    _OptionalExportClientVpnClientCertificateRevocationListRequestTypeDef,
):
    pass


ExportClientVpnClientCertificateRevocationListResultResponseTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListResultResponseTypeDef",
    {
        "CertificateRevocationList": str,
        "Status": "ClientCertificateRevocationListStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportClientVpnClientConfigurationRequestTypeDef = TypedDict(
    "_RequiredExportClientVpnClientConfigurationRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalExportClientVpnClientConfigurationRequestTypeDef = TypedDict(
    "_OptionalExportClientVpnClientConfigurationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ExportClientVpnClientConfigurationRequestTypeDef(
    _RequiredExportClientVpnClientConfigurationRequestTypeDef,
    _OptionalExportClientVpnClientConfigurationRequestTypeDef,
):
    pass


ExportClientVpnClientConfigurationResultResponseTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationResultResponseTypeDef",
    {
        "ClientConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportImageRequestTypeDef = TypedDict(
    "_RequiredExportImageRequestTypeDef",
    {
        "DiskImageFormat": DiskImageFormatType,
        "ImageId": str,
        "S3ExportLocation": "ExportTaskS3LocationRequestTypeDef",
    },
)
_OptionalExportImageRequestTypeDef = TypedDict(
    "_OptionalExportImageRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "DryRun": bool,
        "RoleName": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class ExportImageRequestTypeDef(
    _RequiredExportImageRequestTypeDef, _OptionalExportImageRequestTypeDef
):
    pass


ExportImageResultResponseTypeDef = TypedDict(
    "ExportImageResultResponseTypeDef",
    {
        "Description": str,
        "DiskImageFormat": DiskImageFormatType,
        "ExportImageTaskId": str,
        "ImageId": str,
        "RoleName": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportImageTaskTypeDef = TypedDict(
    "ExportImageTaskTypeDef",
    {
        "Description": str,
        "ExportImageTaskId": str,
        "ImageId": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredExportTaskS3LocationRequestTypeDef = TypedDict(
    "_RequiredExportTaskS3LocationRequestTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalExportTaskS3LocationRequestTypeDef = TypedDict(
    "_OptionalExportTaskS3LocationRequestTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)


class ExportTaskS3LocationRequestTypeDef(
    _RequiredExportTaskS3LocationRequestTypeDef, _OptionalExportTaskS3LocationRequestTypeDef
):
    pass


ExportTaskS3LocationTypeDef = TypedDict(
    "ExportTaskS3LocationTypeDef",
    {
        "S3Bucket": str,
        "S3Prefix": str,
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "Description": str,
        "ExportTaskId": str,
        "ExportToS3Task": "ExportToS3TaskTypeDef",
        "InstanceExportDetails": "InstanceExportDetailsTypeDef",
        "State": ExportTaskStateType,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ExportToS3TaskSpecificationTypeDef = TypedDict(
    "ExportToS3TaskSpecificationTypeDef",
    {
        "ContainerFormat": Literal["ova"],
        "DiskImageFormat": DiskImageFormatType,
        "S3Bucket": str,
        "S3Prefix": str,
    },
    total=False,
)

ExportToS3TaskTypeDef = TypedDict(
    "ExportToS3TaskTypeDef",
    {
        "ContainerFormat": Literal["ova"],
        "DiskImageFormat": DiskImageFormatType,
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

_RequiredExportTransitGatewayRoutesRequestTypeDef = TypedDict(
    "_RequiredExportTransitGatewayRoutesRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "S3Bucket": str,
    },
)
_OptionalExportTransitGatewayRoutesRequestTypeDef = TypedDict(
    "_OptionalExportTransitGatewayRoutesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)


class ExportTransitGatewayRoutesRequestTypeDef(
    _RequiredExportTransitGatewayRoutesRequestTypeDef,
    _OptionalExportTransitGatewayRoutesRequestTypeDef,
):
    pass


ExportTransitGatewayRoutesResultResponseTypeDef = TypedDict(
    "ExportTransitGatewayRoutesResultResponseTypeDef",
    {
        "S3Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedQueuedPurchaseDeletionTypeDef = TypedDict(
    "FailedQueuedPurchaseDeletionTypeDef",
    {
        "Error": "DeleteQueuedReservedInstancesErrorTypeDef",
        "ReservedInstancesId": str,
    },
    total=False,
)

FederatedAuthenticationRequestTypeDef = TypedDict(
    "FederatedAuthenticationRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "SelfServiceSAMLProviderArn": str,
    },
    total=False,
)

FederatedAuthenticationTypeDef = TypedDict(
    "FederatedAuthenticationTypeDef",
    {
        "SamlProviderArn": str,
        "SelfServiceSamlProviderArn": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

FleetDataTypeDef = TypedDict(
    "FleetDataTypeDef",
    {
        "ActivityStatus": FleetActivityStatusType,
        "CreateTime": datetime,
        "FleetId": str,
        "FleetState": FleetStateCodeType,
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicyType,
        "FulfilledCapacity": float,
        "FulfilledOnDemandCapacity": float,
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationTypeDef",
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetTypeType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "SpotOptions": "SpotOptionsTypeDef",
        "OnDemandOptions": "OnDemandOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "Errors": List["DescribeFleetErrorTypeDef"],
        "Instances": List["DescribeFleetsInstancesTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateConfigRequestTypeDef = TypedDict(
    "FleetLaunchTemplateConfigRequestTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationRequestTypeDef",
        "Overrides": List["FleetLaunchTemplateOverridesRequestTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateConfigTypeDef = TypedDict(
    "FleetLaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": List["FleetLaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateOverridesRequestTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesRequestTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "MaxPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "Placement": "PlacementTypeDef",
    },
    total=False,
)

FleetLaunchTemplateOverridesTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "MaxPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "Placement": "PlacementResponseTypeDef",
    },
    total=False,
)

FleetLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

FleetLaunchTemplateSpecificationTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

FleetSpotCapacityRebalanceRequestTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceRequestTypeDef",
    {
        "ReplacementStrategy": Literal["launch"],
    },
    total=False,
)

FleetSpotCapacityRebalanceTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": Literal["launch"],
    },
    total=False,
)

FleetSpotMaintenanceStrategiesRequestTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    {
        "CapacityRebalance": "FleetSpotCapacityRebalanceRequestTypeDef",
    },
    total=False,
)

FleetSpotMaintenanceStrategiesTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": "FleetSpotCapacityRebalanceTypeDef",
    },
    total=False,
)

FlowLogTypeDef = TypedDict(
    "FlowLogTypeDef",
    {
        "CreationTime": datetime,
        "DeliverLogsErrorMessage": str,
        "DeliverLogsPermissionArn": str,
        "DeliverLogsStatus": str,
        "FlowLogId": str,
        "FlowLogStatus": str,
        "LogGroupName": str,
        "ResourceId": str,
        "TrafficType": TrafficTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": str,
        "LogFormat": str,
        "Tags": List["TagTypeDef"],
        "MaxAggregationInterval": int,
    },
    total=False,
)

FpgaDeviceInfoTypeDef = TypedDict(
    "FpgaDeviceInfoTypeDef",
    {
        "Name": str,
        "Manufacturer": str,
        "Count": int,
        "MemoryInfo": "FpgaDeviceMemoryInfoTypeDef",
    },
    total=False,
)

FpgaDeviceMemoryInfoTypeDef = TypedDict(
    "FpgaDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

FpgaImageAttributeTypeDef = TypedDict(
    "FpgaImageAttributeTypeDef",
    {
        "FpgaImageId": str,
        "Name": str,
        "Description": str,
        "LoadPermissions": List["LoadPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
    },
    total=False,
)

FpgaImageStateTypeDef = TypedDict(
    "FpgaImageStateTypeDef",
    {
        "Code": FpgaImageStateCodeType,
        "Message": str,
    },
    total=False,
)

FpgaImageTypeDef = TypedDict(
    "FpgaImageTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "Name": str,
        "Description": str,
        "ShellVersion": str,
        "PciId": "PciIdTypeDef",
        "State": "FpgaImageStateTypeDef",
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "OwnerId": str,
        "OwnerAlias": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "Tags": List["TagTypeDef"],
        "Public": bool,
        "DataRetentionSupport": bool,
    },
    total=False,
)

FpgaInfoTypeDef = TypedDict(
    "FpgaInfoTypeDef",
    {
        "Fpgas": List["FpgaDeviceInfoTypeDef"],
        "TotalFpgaMemoryInMiB": int,
    },
    total=False,
)

GetAssociatedEnclaveCertificateIamRolesRequestTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesRequestTypeDef",
    {
        "CertificateArn": str,
        "DryRun": bool,
    },
    total=False,
)

GetAssociatedEnclaveCertificateIamRolesResultResponseTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesResultResponseTypeDef",
    {
        "AssociatedRoles": List["AssociatedRoleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAssociatedIpv6PoolCidrsRequestTypeDef = TypedDict(
    "_RequiredGetAssociatedIpv6PoolCidrsRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalGetAssociatedIpv6PoolCidrsRequestTypeDef = TypedDict(
    "_OptionalGetAssociatedIpv6PoolCidrsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)


class GetAssociatedIpv6PoolCidrsRequestTypeDef(
    _RequiredGetAssociatedIpv6PoolCidrsRequestTypeDef,
    _OptionalGetAssociatedIpv6PoolCidrsRequestTypeDef,
):
    pass


GetAssociatedIpv6PoolCidrsResultResponseTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsResultResponseTypeDef",
    {
        "Ipv6CidrAssociations": List["Ipv6CidrAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCapacityReservationUsageRequestTypeDef = TypedDict(
    "_RequiredGetCapacityReservationUsageRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalGetCapacityReservationUsageRequestTypeDef = TypedDict(
    "_OptionalGetCapacityReservationUsageRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)


class GetCapacityReservationUsageRequestTypeDef(
    _RequiredGetCapacityReservationUsageRequestTypeDef,
    _OptionalGetCapacityReservationUsageRequestTypeDef,
):
    pass


GetCapacityReservationUsageResultResponseTypeDef = TypedDict(
    "GetCapacityReservationUsageResultResponseTypeDef",
    {
        "NextToken": str,
        "CapacityReservationId": str,
        "InstanceType": str,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "State": CapacityReservationStateType,
        "InstanceUsages": List["InstanceUsageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCoipPoolUsageRequestTypeDef = TypedDict(
    "_RequiredGetCoipPoolUsageRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalGetCoipPoolUsageRequestTypeDef = TypedDict(
    "_OptionalGetCoipPoolUsageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class GetCoipPoolUsageRequestTypeDef(
    _RequiredGetCoipPoolUsageRequestTypeDef, _OptionalGetCoipPoolUsageRequestTypeDef
):
    pass


GetCoipPoolUsageResultResponseTypeDef = TypedDict(
    "GetCoipPoolUsageResultResponseTypeDef",
    {
        "CoipPoolId": str,
        "CoipAddressUsages": List["CoipAddressUsageTypeDef"],
        "LocalGatewayRouteTableId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConsoleOutputRequestInstanceTypeDef = TypedDict(
    "GetConsoleOutputRequestInstanceTypeDef",
    {
        "DryRun": bool,
        "Latest": bool,
    },
    total=False,
)

_RequiredGetConsoleOutputRequestTypeDef = TypedDict(
    "_RequiredGetConsoleOutputRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetConsoleOutputRequestTypeDef = TypedDict(
    "_OptionalGetConsoleOutputRequestTypeDef",
    {
        "DryRun": bool,
        "Latest": bool,
    },
    total=False,
)


class GetConsoleOutputRequestTypeDef(
    _RequiredGetConsoleOutputRequestTypeDef, _OptionalGetConsoleOutputRequestTypeDef
):
    pass


GetConsoleOutputResultResponseTypeDef = TypedDict(
    "GetConsoleOutputResultResponseTypeDef",
    {
        "InstanceId": str,
        "Output": str,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConsoleScreenshotRequestTypeDef = TypedDict(
    "_RequiredGetConsoleScreenshotRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetConsoleScreenshotRequestTypeDef = TypedDict(
    "_OptionalGetConsoleScreenshotRequestTypeDef",
    {
        "DryRun": bool,
        "WakeUp": bool,
    },
    total=False,
)


class GetConsoleScreenshotRequestTypeDef(
    _RequiredGetConsoleScreenshotRequestTypeDef, _OptionalGetConsoleScreenshotRequestTypeDef
):
    pass


GetConsoleScreenshotResultResponseTypeDef = TypedDict(
    "GetConsoleScreenshotResultResponseTypeDef",
    {
        "ImageData": str,
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDefaultCreditSpecificationRequestTypeDef = TypedDict(
    "_RequiredGetDefaultCreditSpecificationRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
    },
)
_OptionalGetDefaultCreditSpecificationRequestTypeDef = TypedDict(
    "_OptionalGetDefaultCreditSpecificationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class GetDefaultCreditSpecificationRequestTypeDef(
    _RequiredGetDefaultCreditSpecificationRequestTypeDef,
    _OptionalGetDefaultCreditSpecificationRequestTypeDef,
):
    pass


GetDefaultCreditSpecificationResultResponseTypeDef = TypedDict(
    "GetDefaultCreditSpecificationResultResponseTypeDef",
    {
        "InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEbsDefaultKmsKeyIdRequestTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetEbsDefaultKmsKeyIdResultResponseTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdResultResponseTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEbsEncryptionByDefaultRequestTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetEbsEncryptionByDefaultResultResponseTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultResultResponseTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFlowLogsIntegrationTemplateRequestTypeDef = TypedDict(
    "_RequiredGetFlowLogsIntegrationTemplateRequestTypeDef",
    {
        "FlowLogId": str,
        "ConfigDeliveryS3DestinationArn": str,
        "IntegrateServices": "IntegrateServicesTypeDef",
    },
)
_OptionalGetFlowLogsIntegrationTemplateRequestTypeDef = TypedDict(
    "_OptionalGetFlowLogsIntegrationTemplateRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class GetFlowLogsIntegrationTemplateRequestTypeDef(
    _RequiredGetFlowLogsIntegrationTemplateRequestTypeDef,
    _OptionalGetFlowLogsIntegrationTemplateRequestTypeDef,
):
    pass


GetFlowLogsIntegrationTemplateResultResponseTypeDef = TypedDict(
    "GetFlowLogsIntegrationTemplateResultResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGroupsForCapacityReservationRequestTypeDef = TypedDict(
    "_RequiredGetGroupsForCapacityReservationRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalGetGroupsForCapacityReservationRequestTypeDef = TypedDict(
    "_OptionalGetGroupsForCapacityReservationRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)


class GetGroupsForCapacityReservationRequestTypeDef(
    _RequiredGetGroupsForCapacityReservationRequestTypeDef,
    _OptionalGetGroupsForCapacityReservationRequestTypeDef,
):
    pass


GetGroupsForCapacityReservationResultResponseTypeDef = TypedDict(
    "GetGroupsForCapacityReservationResultResponseTypeDef",
    {
        "NextToken": str,
        "CapacityReservationGroups": List["CapacityReservationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostReservationPurchasePreviewRequestTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewRequestTypeDef",
    {
        "HostIdSet": List[str],
        "OfferingId": str,
    },
)

GetHostReservationPurchasePreviewResultResponseTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewResultResponseTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLaunchTemplateDataRequestTypeDef = TypedDict(
    "_RequiredGetLaunchTemplateDataRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetLaunchTemplateDataRequestTypeDef = TypedDict(
    "_OptionalGetLaunchTemplateDataRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class GetLaunchTemplateDataRequestTypeDef(
    _RequiredGetLaunchTemplateDataRequestTypeDef, _OptionalGetLaunchTemplateDataRequestTypeDef
):
    pass


GetLaunchTemplateDataResultResponseTypeDef = TypedDict(
    "GetLaunchTemplateDataResultResponseTypeDef",
    {
        "LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetManagedPrefixListAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetManagedPrefixListAssociationsRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalGetManagedPrefixListAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetManagedPrefixListAssociationsRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetManagedPrefixListAssociationsRequestTypeDef(
    _RequiredGetManagedPrefixListAssociationsRequestTypeDef,
    _OptionalGetManagedPrefixListAssociationsRequestTypeDef,
):
    pass


GetManagedPrefixListAssociationsResultResponseTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsResultResponseTypeDef",
    {
        "PrefixListAssociations": List["PrefixListAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetManagedPrefixListEntriesRequestTypeDef = TypedDict(
    "_RequiredGetManagedPrefixListEntriesRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalGetManagedPrefixListEntriesRequestTypeDef = TypedDict(
    "_OptionalGetManagedPrefixListEntriesRequestTypeDef",
    {
        "DryRun": bool,
        "TargetVersion": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetManagedPrefixListEntriesRequestTypeDef(
    _RequiredGetManagedPrefixListEntriesRequestTypeDef,
    _OptionalGetManagedPrefixListEntriesRequestTypeDef,
):
    pass


GetManagedPrefixListEntriesResultResponseTypeDef = TypedDict(
    "GetManagedPrefixListEntriesResultResponseTypeDef",
    {
        "Entries": List["PrefixListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPasswordDataRequestInstanceTypeDef = TypedDict(
    "GetPasswordDataRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredGetPasswordDataRequestTypeDef = TypedDict(
    "_RequiredGetPasswordDataRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetPasswordDataRequestTypeDef = TypedDict(
    "_OptionalGetPasswordDataRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class GetPasswordDataRequestTypeDef(
    _RequiredGetPasswordDataRequestTypeDef, _OptionalGetPasswordDataRequestTypeDef
):
    pass


GetPasswordDataResultResponseTypeDef = TypedDict(
    "GetPasswordDataResultResponseTypeDef",
    {
        "InstanceId": str,
        "PasswordData": str,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservedInstancesExchangeQuoteRequestTypeDef = TypedDict(
    "_RequiredGetReservedInstancesExchangeQuoteRequestTypeDef",
    {
        "ReservedInstanceIds": List[str],
    },
)
_OptionalGetReservedInstancesExchangeQuoteRequestTypeDef = TypedDict(
    "_OptionalGetReservedInstancesExchangeQuoteRequestTypeDef",
    {
        "DryRun": bool,
        "TargetConfigurations": List["TargetConfigurationRequestTypeDef"],
    },
    total=False,
)


class GetReservedInstancesExchangeQuoteRequestTypeDef(
    _RequiredGetReservedInstancesExchangeQuoteRequestTypeDef,
    _OptionalGetReservedInstancesExchangeQuoteRequestTypeDef,
):
    pass


GetReservedInstancesExchangeQuoteResultResponseTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteResultResponseTypeDef",
    {
        "CurrencyCode": str,
        "IsValidExchange": bool,
        "OutputReservedInstancesWillExpireAt": datetime,
        "PaymentDue": str,
        "ReservedInstanceValueRollup": "ReservationValueTypeDef",
        "ReservedInstanceValueSet": List["ReservedInstanceReservationValueTypeDef"],
        "TargetConfigurationValueRollup": "ReservationValueTypeDef",
        "TargetConfigurationValueSet": List["TargetReservationValueTypeDef"],
        "ValidationFailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSerialConsoleAccessStatusRequestTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetSerialConsoleAccessStatusResultResponseTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusResultResponseTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayAttachmentPropagationsRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayAttachmentPropagationsRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalGetTransitGatewayAttachmentPropagationsRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayAttachmentPropagationsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class GetTransitGatewayAttachmentPropagationsRequestTypeDef(
    _RequiredGetTransitGatewayAttachmentPropagationsRequestTypeDef,
    _OptionalGetTransitGatewayAttachmentPropagationsRequestTypeDef,
):
    pass


GetTransitGatewayAttachmentPropagationsResultResponseTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsResultResponseTypeDef",
    {
        "TransitGatewayAttachmentPropagations": List["TransitGatewayAttachmentPropagationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayMulticastDomainAssociationsRequestTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

GetTransitGatewayMulticastDomainAssociationsResultResponseTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsResultResponseTypeDef",
    {
        "MulticastDomainAssociations": List["TransitGatewayMulticastDomainAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayPrefixListReferencesRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayPrefixListReferencesRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalGetTransitGatewayPrefixListReferencesRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayPrefixListReferencesRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class GetTransitGatewayPrefixListReferencesRequestTypeDef(
    _RequiredGetTransitGatewayPrefixListReferencesRequestTypeDef,
    _OptionalGetTransitGatewayPrefixListReferencesRequestTypeDef,
):
    pass


GetTransitGatewayPrefixListReferencesResultResponseTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesResultResponseTypeDef",
    {
        "TransitGatewayPrefixListReferences": List["TransitGatewayPrefixListReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayRouteTableAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayRouteTableAssociationsRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalGetTransitGatewayRouteTableAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayRouteTableAssociationsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class GetTransitGatewayRouteTableAssociationsRequestTypeDef(
    _RequiredGetTransitGatewayRouteTableAssociationsRequestTypeDef,
    _OptionalGetTransitGatewayRouteTableAssociationsRequestTypeDef,
):
    pass


GetTransitGatewayRouteTableAssociationsResultResponseTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsResultResponseTypeDef",
    {
        "Associations": List["TransitGatewayRouteTableAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayRouteTablePropagationsRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayRouteTablePropagationsRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalGetTransitGatewayRouteTablePropagationsRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayRouteTablePropagationsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class GetTransitGatewayRouteTablePropagationsRequestTypeDef(
    _RequiredGetTransitGatewayRouteTablePropagationsRequestTypeDef,
    _OptionalGetTransitGatewayRouteTablePropagationsRequestTypeDef,
):
    pass


GetTransitGatewayRouteTablePropagationsResultResponseTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsResultResponseTypeDef",
    {
        "TransitGatewayRouteTablePropagations": List["TransitGatewayRouteTablePropagationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GpuDeviceInfoTypeDef = TypedDict(
    "GpuDeviceInfoTypeDef",
    {
        "Name": str,
        "Manufacturer": str,
        "Count": int,
        "MemoryInfo": "GpuDeviceMemoryInfoTypeDef",
    },
    total=False,
)

GpuDeviceMemoryInfoTypeDef = TypedDict(
    "GpuDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {
        "Gpus": List["GpuDeviceInfoTypeDef"],
        "TotalGpuMemoryInMiB": int,
    },
    total=False,
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
    total=False,
)

HibernationOptionsRequestTypeDef = TypedDict(
    "HibernationOptionsRequestTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

HibernationOptionsTypeDef = TypedDict(
    "HibernationOptionsTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

HistoryRecordEntryTypeDef = TypedDict(
    "HistoryRecordEntryTypeDef",
    {
        "EventInformation": "EventInformationTypeDef",
        "EventType": FleetEventTypeType,
        "Timestamp": datetime,
    },
    total=False,
)

HistoryRecordTypeDef = TypedDict(
    "HistoryRecordTypeDef",
    {
        "EventInformation": "EventInformationTypeDef",
        "EventType": EventTypeType,
        "Timestamp": datetime,
    },
    total=False,
)

HostInstanceTypeDef = TypedDict(
    "HostInstanceTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "OwnerId": str,
    },
    total=False,
)

HostOfferingTypeDef = TypedDict(
    "HostOfferingTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "OfferingId": str,
        "PaymentOption": PaymentOptionType,
        "UpfrontPrice": str,
    },
    total=False,
)

HostPropertiesTypeDef = TypedDict(
    "HostPropertiesTypeDef",
    {
        "Cores": int,
        "InstanceType": str,
        "InstanceFamily": str,
        "Sockets": int,
        "TotalVCpus": int,
    },
    total=False,
)

HostReservationTypeDef = TypedDict(
    "HostReservationTypeDef",
    {
        "Count": int,
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "End": datetime,
        "HostIdSet": List[str],
        "HostReservationId": str,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "OfferingId": str,
        "PaymentOption": PaymentOptionType,
        "Start": datetime,
        "State": ReservationStateType,
        "UpfrontPrice": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "AutoPlacement": AutoPlacementType,
        "AvailabilityZone": str,
        "AvailableCapacity": "AvailableCapacityTypeDef",
        "ClientToken": str,
        "HostId": str,
        "HostProperties": "HostPropertiesTypeDef",
        "HostReservationId": str,
        "Instances": List["HostInstanceTypeDef"],
        "State": AllocationStateType,
        "AllocationTime": datetime,
        "ReleaseTime": datetime,
        "Tags": List["TagTypeDef"],
        "HostRecovery": HostRecoveryType,
        "AllowsMultipleInstanceTypes": AllowsMultipleInstanceTypesType,
        "OwnerId": str,
        "AvailabilityZoneId": str,
        "MemberOfServiceLinkedResourceGroup": bool,
    },
    total=False,
)

IKEVersionsListValueTypeDef = TypedDict(
    "IKEVersionsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

IKEVersionsRequestListValueTypeDef = TypedDict(
    "IKEVersionsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

IamInstanceProfileAssociationTypeDef = TypedDict(
    "IamInstanceProfileAssociationTypeDef",
    {
        "AssociationId": str,
        "InstanceId": str,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "State": IamInstanceProfileAssociationStateType,
        "Timestamp": datetime,
    },
    total=False,
)

IamInstanceProfileSpecificationTypeDef = TypedDict(
    "IamInstanceProfileSpecificationTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": str,
        "Id": str,
    },
    total=False,
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": int,
        "Type": int,
    },
    total=False,
)

IdFormatTypeDef = TypedDict(
    "IdFormatTypeDef",
    {
        "Deadline": datetime,
        "Resource": str,
        "UseLongIds": bool,
    },
    total=False,
)

ImageAttributeResponseTypeDef = TypedDict(
    "ImageAttributeResponseTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "LaunchPermissions": List["LaunchPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "Description": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "RamdiskId": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "BootMode": "AttributeValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDiskContainerTypeDef = TypedDict(
    "ImageDiskContainerTypeDef",
    {
        "Description": str,
        "DeviceName": str,
        "Format": str,
        "SnapshotId": str,
        "Url": str,
        "UserBucket": "UserBucketTypeDef",
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Architecture": ArchitectureValuesType,
        "CreationDate": str,
        "ImageId": str,
        "ImageLocation": str,
        "ImageType": ImageTypeValuesType,
        "Public": bool,
        "KernelId": str,
        "OwnerId": str,
        "Platform": Literal["Windows"],
        "PlatformDetails": str,
        "UsageOperation": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": str,
        "State": ImageStateType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "EnaSupport": bool,
        "Hypervisor": HypervisorTypeType,
        "ImageOwnerAlias": str,
        "Name": str,
        "RootDeviceName": str,
        "RootDeviceType": DeviceTypeType,
        "SriovNetSupport": str,
        "StateReason": "StateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VirtualizationType": VirtualizationTypeType,
        "BootMode": BootModeValuesType,
        "DeprecationTime": str,
    },
    total=False,
)

_RequiredImportClientVpnClientCertificateRevocationListRequestTypeDef = TypedDict(
    "_RequiredImportClientVpnClientCertificateRevocationListRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "CertificateRevocationList": str,
    },
)
_OptionalImportClientVpnClientCertificateRevocationListRequestTypeDef = TypedDict(
    "_OptionalImportClientVpnClientCertificateRevocationListRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ImportClientVpnClientCertificateRevocationListRequestTypeDef(
    _RequiredImportClientVpnClientCertificateRevocationListRequestTypeDef,
    _OptionalImportClientVpnClientCertificateRevocationListRequestTypeDef,
):
    pass


ImportClientVpnClientCertificateRevocationListResultResponseTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportImageLicenseConfigurationRequestTypeDef = TypedDict(
    "ImportImageLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

ImportImageLicenseConfigurationResponseTypeDef = TypedDict(
    "ImportImageLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

ImportImageRequestTypeDef = TypedDict(
    "ImportImageRequestTypeDef",
    {
        "Architecture": str,
        "ClientData": "ClientDataTypeDef",
        "ClientToken": str,
        "Description": str,
        "DiskContainers": List["ImageDiskContainerTypeDef"],
        "DryRun": bool,
        "Encrypted": bool,
        "Hypervisor": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "RoleName": str,
        "LicenseSpecifications": List["ImportImageLicenseConfigurationRequestTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

ImportImageResultResponseTypeDef = TypedDict(
    "ImportImageResultResponseTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportImageTaskTypeDef = TypedDict(
    "ImportImageTaskTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
    },
    total=False,
)

ImportInstanceLaunchSpecificationTypeDef = TypedDict(
    "ImportInstanceLaunchSpecificationTypeDef",
    {
        "AdditionalInfo": str,
        "Architecture": ArchitectureValuesType,
        "GroupIds": List[str],
        "GroupNames": List[str],
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "InstanceType": InstanceTypeType,
        "Monitoring": bool,
        "Placement": "PlacementTypeDef",
        "PrivateIpAddress": str,
        "SubnetId": str,
        "UserData": "UserDataTypeDef",
    },
    total=False,
)

_RequiredImportInstanceRequestTypeDef = TypedDict(
    "_RequiredImportInstanceRequestTypeDef",
    {
        "Platform": Literal["Windows"],
    },
)
_OptionalImportInstanceRequestTypeDef = TypedDict(
    "_OptionalImportInstanceRequestTypeDef",
    {
        "Description": str,
        "DiskImages": List["DiskImageTypeDef"],
        "DryRun": bool,
        "LaunchSpecification": "ImportInstanceLaunchSpecificationTypeDef",
    },
    total=False,
)


class ImportInstanceRequestTypeDef(
    _RequiredImportInstanceRequestTypeDef, _OptionalImportInstanceRequestTypeDef
):
    pass


ImportInstanceResultResponseTypeDef = TypedDict(
    "ImportInstanceResultResponseTypeDef",
    {
        "ConversionTask": "ConversionTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportInstanceTaskDetailsTypeDef = TypedDict(
    "ImportInstanceTaskDetailsTypeDef",
    {
        "Description": str,
        "InstanceId": str,
        "Platform": Literal["Windows"],
        "Volumes": List["ImportInstanceVolumeDetailItemTypeDef"],
    },
    total=False,
)

ImportInstanceVolumeDetailItemTypeDef = TypedDict(
    "ImportInstanceVolumeDetailItemTypeDef",
    {
        "AvailabilityZone": str,
        "BytesConverted": int,
        "Description": str,
        "Image": "DiskImageDescriptionTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Volume": "DiskImageVolumeDescriptionTypeDef",
    },
    total=False,
)

_RequiredImportKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_RequiredImportKeyPairRequestServiceResourceTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_OptionalImportKeyPairRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class ImportKeyPairRequestServiceResourceTypeDef(
    _RequiredImportKeyPairRequestServiceResourceTypeDef,
    _OptionalImportKeyPairRequestServiceResourceTypeDef,
):
    pass


_RequiredImportKeyPairRequestTypeDef = TypedDict(
    "_RequiredImportKeyPairRequestTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportKeyPairRequestTypeDef = TypedDict(
    "_OptionalImportKeyPairRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class ImportKeyPairRequestTypeDef(
    _RequiredImportKeyPairRequestTypeDef, _OptionalImportKeyPairRequestTypeDef
):
    pass


ImportKeyPairResultResponseTypeDef = TypedDict(
    "ImportKeyPairResultResponseTypeDef",
    {
        "KeyFingerprint": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSnapshotRequestTypeDef = TypedDict(
    "ImportSnapshotRequestTypeDef",
    {
        "ClientData": "ClientDataTypeDef",
        "ClientToken": str,
        "Description": str,
        "DiskContainer": "SnapshotDiskContainerTypeDef",
        "DryRun": bool,
        "Encrypted": bool,
        "KmsKeyId": str,
        "RoleName": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

ImportSnapshotResultResponseTypeDef = TypedDict(
    "ImportSnapshotResultResponseTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSnapshotTaskTypeDef = TypedDict(
    "ImportSnapshotTaskTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredImportVolumeRequestTypeDef = TypedDict(
    "_RequiredImportVolumeRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Image": "DiskImageDetailTypeDef",
        "Volume": "VolumeDetailTypeDef",
    },
)
_OptionalImportVolumeRequestTypeDef = TypedDict(
    "_OptionalImportVolumeRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
    },
    total=False,
)


class ImportVolumeRequestTypeDef(
    _RequiredImportVolumeRequestTypeDef, _OptionalImportVolumeRequestTypeDef
):
    pass


ImportVolumeResultResponseTypeDef = TypedDict(
    "ImportVolumeResultResponseTypeDef",
    {
        "ConversionTask": "ConversionTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportVolumeTaskDetailsTypeDef = TypedDict(
    "ImportVolumeTaskDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "BytesConverted": int,
        "Description": str,
        "Image": "DiskImageDescriptionTypeDef",
        "Volume": "DiskImageVolumeDescriptionTypeDef",
    },
    total=False,
)

InferenceAcceleratorInfoTypeDef = TypedDict(
    "InferenceAcceleratorInfoTypeDef",
    {
        "Accelerators": List["InferenceDeviceInfoTypeDef"],
    },
    total=False,
)

InferenceDeviceInfoTypeDef = TypedDict(
    "InferenceDeviceInfoTypeDef",
    {
        "Count": int,
        "Name": str,
        "Manufacturer": str,
    },
    total=False,
)

InstanceAttributeResponseTypeDef = TypedDict(
    "InstanceAttributeResponseTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "EnclaveOptions": "EnclaveOptionsTypeDef",
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "InstanceId": str,
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": "AttributeValueTypeDef",
        "RootDeviceName": "AttributeValueTypeDef",
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "AttributeValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceBlockDeviceMappingSpecificationTypeDef = TypedDict(
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    {
        "DeviceName": str,
        "Ebs": "EbsInstanceBlockDeviceSpecificationTypeDef",
        "NoDevice": str,
        "VirtualName": str,
    },
    total=False,
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "Ebs": "EbsInstanceBlockDeviceTypeDef",
    },
    total=False,
)

InstanceCapacityTypeDef = TypedDict(
    "InstanceCapacityTypeDef",
    {
        "AvailableCapacity": int,
        "InstanceType": str,
        "TotalCapacity": int,
    },
    total=False,
)

InstanceCountTypeDef = TypedDict(
    "InstanceCountTypeDef",
    {
        "InstanceCount": int,
        "State": ListingStateType,
    },
    total=False,
)

InstanceCreditSpecificationRequestTypeDef = TypedDict(
    "InstanceCreditSpecificationRequestTypeDef",
    {
        "InstanceId": str,
        "CpuCredits": str,
    },
    total=False,
)

InstanceCreditSpecificationTypeDef = TypedDict(
    "InstanceCreditSpecificationTypeDef",
    {
        "InstanceId": str,
        "CpuCredits": str,
    },
    total=False,
)

InstanceDeleteTagsRequestTypeDef = TypedDict(
    "InstanceDeleteTagsRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

InstanceExportDetailsTypeDef = TypedDict(
    "InstanceExportDetailsTypeDef",
    {
        "InstanceId": str,
        "TargetEnvironment": ExportEnvironmentType,
    },
    total=False,
)

InstanceFamilyCreditSpecificationTypeDef = TypedDict(
    "InstanceFamilyCreditSpecificationTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "CpuCredits": str,
    },
    total=False,
)

InstanceIpv6AddressRequestTypeDef = TypedDict(
    "InstanceIpv6AddressRequestTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

InstanceIpv6AddressTypeDef = TypedDict(
    "InstanceIpv6AddressTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

InstanceMarketOptionsRequestTypeDef = TypedDict(
    "InstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": Literal["spot"],
        "SpotOptions": "SpotMarketOptionsTypeDef",
    },
    total=False,
)

InstanceMetadataOptionsRequestTypeDef = TypedDict(
    "InstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
    },
    total=False,
)

InstanceMetadataOptionsResponseTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseTypeDef",
    {
        "State": InstanceMetadataOptionsStateType,
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
    },
    total=False,
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "InstanceId": str,
        "Monitoring": "MonitoringTypeDef",
    },
    total=False,
)

InstanceNetworkInterfaceAssociationTypeDef = TypedDict(
    "InstanceNetworkInterfaceAssociationTypeDef",
    {
        "CarrierIp": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
    },
    total=False,
)

InstanceNetworkInterfaceAttachmentTypeDef = TypedDict(
    "InstanceNetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "Status": AttachmentStatusType,
        "NetworkCardIndex": int,
    },
    total=False,
)

InstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "AssociateCarrierIpAddress": bool,
        "InterfaceType": str,
        "NetworkCardIndex": int,
    },
    total=False,
)

InstanceNetworkInterfaceTypeDef = TypedDict(
    "InstanceNetworkInterfaceTypeDef",
    {
        "Association": "InstanceNetworkInterfaceAssociationTypeDef",
        "Attachment": "InstanceNetworkInterfaceAttachmentTypeDef",
        "Description": str,
        "Groups": List["GroupIdentifierTypeDef"],
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "MacAddress": str,
        "NetworkInterfaceId": str,
        "OwnerId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["InstancePrivateIpAddressTypeDef"],
        "SourceDestCheck": bool,
        "Status": NetworkInterfaceStatusType,
        "SubnetId": str,
        "VpcId": str,
        "InterfaceType": str,
    },
    total=False,
)

InstancePrivateIpAddressTypeDef = TypedDict(
    "InstancePrivateIpAddressTypeDef",
    {
        "Association": "InstanceNetworkInterfaceAssociationTypeDef",
        "Primary": bool,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

InstanceSpecificationTypeDef = TypedDict(
    "InstanceSpecificationTypeDef",
    {
        "InstanceId": str,
        "ExcludeBootVolume": bool,
    },
    total=False,
)

InstanceStateChangeTypeDef = TypedDict(
    "InstanceStateChangeTypeDef",
    {
        "CurrentState": "InstanceStateTypeDef",
        "InstanceId": str,
        "PreviousState": "InstanceStateTypeDef",
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "Code": int,
        "Name": InstanceStateNameType,
    },
    total=False,
)

InstanceStatusDetailsTypeDef = TypedDict(
    "InstanceStatusDetailsTypeDef",
    {
        "ImpairedSince": datetime,
        "Name": Literal["reachability"],
        "Status": StatusTypeType,
    },
    total=False,
)

InstanceStatusEventTypeDef = TypedDict(
    "InstanceStatusEventTypeDef",
    {
        "InstanceEventId": str,
        "Code": EventCodeType,
        "Description": str,
        "NotAfter": datetime,
        "NotBefore": datetime,
        "NotBeforeDeadline": datetime,
    },
    total=False,
)

InstanceStatusSummaryTypeDef = TypedDict(
    "InstanceStatusSummaryTypeDef",
    {
        "Details": List["InstanceStatusDetailsTypeDef"],
        "Status": SummaryStatusType,
    },
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "AvailabilityZone": str,
        "OutpostArn": str,
        "Events": List["InstanceStatusEventTypeDef"],
        "InstanceId": str,
        "InstanceState": "InstanceStateTypeDef",
        "InstanceStatus": "InstanceStatusSummaryTypeDef",
        "SystemStatus": "InstanceStatusSummaryTypeDef",
    },
    total=False,
)

InstanceStorageInfoTypeDef = TypedDict(
    "InstanceStorageInfoTypeDef",
    {
        "TotalSizeInGB": int,
        "Disks": List["DiskInfoTypeDef"],
        "NvmeSupport": EphemeralNvmeSupportType,
    },
    total=False,
)

InstanceTagNotificationAttributeTypeDef = TypedDict(
    "InstanceTagNotificationAttributeTypeDef",
    {
        "InstanceTagKeys": List[str],
        "IncludeAllTagsOfInstance": bool,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AmiLaunchIndex": int,
        "ImageId": str,
        "InstanceId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "LaunchTime": datetime,
        "Monitoring": "MonitoringTypeDef",
        "Placement": "PlacementTypeDef",
        "Platform": Literal["Windows"],
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "RamdiskId": str,
        "State": "InstanceStateTypeDef",
        "StateTransitionReason": str,
        "SubnetId": str,
        "VpcId": str,
        "Architecture": ArchitectureValuesType,
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "ClientToken": str,
        "EbsOptimized": bool,
        "EnaSupport": bool,
        "Hypervisor": HypervisorTypeType,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "InstanceLifecycle": InstanceLifecycleTypeType,
        "ElasticGpuAssociations": List["ElasticGpuAssociationTypeDef"],
        "ElasticInferenceAcceleratorAssociations": List[
            "ElasticInferenceAcceleratorAssociationTypeDef"
        ],
        "NetworkInterfaces": List["InstanceNetworkInterfaceTypeDef"],
        "OutpostArn": str,
        "RootDeviceName": str,
        "RootDeviceType": DeviceTypeType,
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "SourceDestCheck": bool,
        "SpotInstanceRequestId": str,
        "SriovNetSupport": str,
        "StateReason": "StateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VirtualizationType": VirtualizationTypeType,
        "CpuOptions": "CpuOptionsTypeDef",
        "CapacityReservationId": str,
        "CapacityReservationSpecification": "CapacityReservationSpecificationResponseTypeDef",
        "HibernationOptions": "HibernationOptionsTypeDef",
        "Licenses": List["LicenseConfigurationTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsResponseTypeDef",
        "EnclaveOptions": "EnclaveOptionsTypeDef",
        "BootMode": BootModeValuesType,
    },
    total=False,
)

InstanceTypeInfoTypeDef = TypedDict(
    "InstanceTypeInfoTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "CurrentGeneration": bool,
        "FreeTierEligible": bool,
        "SupportedUsageClasses": List[UsageClassTypeType],
        "SupportedRootDeviceTypes": List[RootDeviceTypeType],
        "SupportedVirtualizationTypes": List[VirtualizationTypeType],
        "BareMetal": bool,
        "Hypervisor": InstanceTypeHypervisorType,
        "ProcessorInfo": "ProcessorInfoTypeDef",
        "VCpuInfo": "VCpuInfoTypeDef",
        "MemoryInfo": "MemoryInfoTypeDef",
        "InstanceStorageSupported": bool,
        "InstanceStorageInfo": "InstanceStorageInfoTypeDef",
        "EbsInfo": "EbsInfoTypeDef",
        "NetworkInfo": "NetworkInfoTypeDef",
        "GpuInfo": "GpuInfoTypeDef",
        "FpgaInfo": "FpgaInfoTypeDef",
        "PlacementGroupInfo": "PlacementGroupInfoTypeDef",
        "InferenceAcceleratorInfo": "InferenceAcceleratorInfoTypeDef",
        "HibernationSupported": bool,
        "BurstablePerformanceSupported": bool,
        "DedicatedHostsSupported": bool,
        "AutoRecoverySupported": bool,
        "SupportedBootModes": List[BootModeTypeType],
    },
    total=False,
)

InstanceTypeOfferingTypeDef = TypedDict(
    "InstanceTypeOfferingTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "LocationType": LocationTypeType,
        "Location": str,
    },
    total=False,
)

InstanceUsageTypeDef = TypedDict(
    "InstanceUsageTypeDef",
    {
        "AccountId": str,
        "UsedInstanceCount": int,
    },
    total=False,
)

IntegrateServicesTypeDef = TypedDict(
    "IntegrateServicesTypeDef",
    {
        "AthenaIntegrations": List["AthenaIntegrationTypeDef"],
    },
    total=False,
)

InternetGatewayAttachmentTypeDef = TypedDict(
    "InternetGatewayAttachmentTypeDef",
    {
        "State": AttachmentStatusType,
        "VpcId": str,
    },
    total=False,
)

InternetGatewayTypeDef = TypedDict(
    "InternetGatewayTypeDef",
    {
        "Attachments": List["InternetGatewayAttachmentTypeDef"],
        "InternetGatewayId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "IpProtocol": str,
        "IpRanges": List["IpRangeTypeDef"],
        "Ipv6Ranges": List["Ipv6RangeTypeDef"],
        "PrefixListIds": List["PrefixListIdTypeDef"],
        "ToPort": int,
        "UserIdGroupPairs": List["UserIdGroupPairTypeDef"],
    },
    total=False,
)

IpRangeTypeDef = TypedDict(
    "IpRangeTypeDef",
    {
        "CidrIp": str,
        "Description": str,
    },
    total=False,
)

Ipv6CidrAssociationTypeDef = TypedDict(
    "Ipv6CidrAssociationTypeDef",
    {
        "Ipv6Cidr": str,
        "AssociatedResource": str,
    },
    total=False,
)

Ipv6CidrBlockTypeDef = TypedDict(
    "Ipv6CidrBlockTypeDef",
    {
        "Ipv6CidrBlock": str,
    },
    total=False,
)

Ipv6PoolTypeDef = TypedDict(
    "Ipv6PoolTypeDef",
    {
        "PoolId": str,
        "Description": str,
        "PoolCidrBlocks": List["PoolCidrBlockTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

Ipv6RangeTypeDef = TypedDict(
    "Ipv6RangeTypeDef",
    {
        "CidrIpv6": str,
        "Description": str,
    },
    total=False,
)

KeyPairInfoTypeDef = TypedDict(
    "KeyPairInfoTypeDef",
    {
        "KeyPairId": str,
        "KeyFingerprint": str,
        "KeyName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

KeyPairResponseTypeDef = TypedDict(
    "KeyPairResponseTypeDef",
    {
        "KeyFingerprint": str,
        "KeyMaterial": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LastErrorTypeDef = TypedDict(
    "LastErrorTypeDef",
    {
        "Message": str,
        "Code": str,
    },
    total=False,
)

LaunchPermissionModificationsTypeDef = TypedDict(
    "LaunchPermissionModificationsTypeDef",
    {
        "Add": List["LaunchPermissionTypeDef"],
        "Remove": List["LaunchPermissionTypeDef"],
    },
    total=False,
)

LaunchPermissionTypeDef = TypedDict(
    "LaunchPermissionTypeDef",
    {
        "Group": Literal["all"],
        "UserId": str,
    },
    total=False,
)

LaunchSpecificationTypeDef = TypedDict(
    "LaunchSpecificationTypeDef",
    {
        "UserData": str,
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SubnetId": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
    },
    total=False,
)

LaunchTemplateAndOverridesResponseTypeDef = TypedDict(
    "LaunchTemplateAndOverridesResponseTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": "FleetLaunchTemplateOverridesTypeDef",
    },
    total=False,
)

LaunchTemplateBlockDeviceMappingRequestTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "LaunchTemplateEbsBlockDeviceRequestTypeDef",
        "NoDevice": str,
    },
    total=False,
)

LaunchTemplateBlockDeviceMappingTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "LaunchTemplateEbsBlockDeviceTypeDef",
        "NoDevice": str,
    },
    total=False,
)

LaunchTemplateCapacityReservationSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetTypeDef",
    },
    total=False,
)

LaunchTemplateCapacityReservationSpecificationResponseTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
    },
    total=False,
)

LaunchTemplateConfigTypeDef = TypedDict(
    "LaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": List["LaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

LaunchTemplateCpuOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsRequestTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
    },
    total=False,
)

LaunchTemplateCpuOptionsTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
    },
    total=False,
)

LaunchTemplateEbsBlockDeviceRequestTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    {
        "Encrypted": bool,
        "DeleteOnTermination": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "Throughput": int,
    },
    total=False,
)

LaunchTemplateEbsBlockDeviceTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceTypeDef",
    {
        "Encrypted": bool,
        "DeleteOnTermination": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "Throughput": int,
    },
    total=False,
)

LaunchTemplateElasticInferenceAcceleratorResponseTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    {
        "Type": str,
        "Count": int,
    },
    total=False,
)

_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
    },
)
_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef",
    {
        "Count": int,
    },
    total=False,
)


class LaunchTemplateElasticInferenceAcceleratorTypeDef(
    _RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef,
    _OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef,
):
    pass


LaunchTemplateEnclaveOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LaunchTemplateEnclaveOptionsTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LaunchTemplateHibernationOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

LaunchTemplateHibernationOptionsTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

LaunchTemplateIamInstanceProfileSpecificationTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

LaunchTemplateInstanceMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": Literal["spot"],
        "SpotOptions": "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    },
    total=False,
)

LaunchTemplateInstanceMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    {
        "MarketType": Literal["spot"],
        "SpotOptions": "LaunchTemplateSpotMarketOptionsTypeDef",
    },
    total=False,
)

LaunchTemplateInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": LaunchTemplateHttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": LaunchTemplateInstanceMetadataEndpointStateType,
    },
    total=False,
)

LaunchTemplateInstanceMetadataOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    {
        "State": LaunchTemplateInstanceMetadataOptionsStateType,
        "HttpTokens": LaunchTemplateHttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": LaunchTemplateInstanceMetadataEndpointStateType,
    },
    total=False,
)

LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressRequestTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "NetworkCardIndex": int,
    },
    total=False,
)

LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "NetworkCardIndex": int,
    },
    total=False,
)

LaunchTemplateLicenseConfigurationRequestTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LaunchTemplateLicenseConfigurationTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "SpotPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
    },
    total=False,
)

LaunchTemplatePlacementRequestTypeDef = TypedDict(
    "LaunchTemplatePlacementRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
    },
    total=False,
)

LaunchTemplatePlacementTypeDef = TypedDict(
    "LaunchTemplatePlacementTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

LaunchTemplateSpotMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": SpotInstanceTypeType,
        "BlockDurationMinutes": int,
        "ValidUntil": Union[datetime, str],
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

LaunchTemplateSpotMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": SpotInstanceTypeType,
        "BlockDurationMinutes": int,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

LaunchTemplateTagSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateTagSpecificationTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "CreateTime": datetime,
        "CreatedBy": str,
        "DefaultVersionNumber": int,
        "LatestVersionNumber": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateVersionTypeDef = TypedDict(
    "LaunchTemplateVersionTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
        "VersionDescription": str,
        "CreateTime": datetime,
        "CreatedBy": str,
        "DefaultVersion": bool,
        "LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef",
    },
    total=False,
)

LaunchTemplatesMonitoringRequestTypeDef = TypedDict(
    "LaunchTemplatesMonitoringRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LaunchTemplatesMonitoringTypeDef = TypedDict(
    "LaunchTemplatesMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LicenseConfigurationRequestTypeDef = TypedDict(
    "LicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LoadBalancersConfigTypeDef = TypedDict(
    "LoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancersConfig": "ClassicLoadBalancersConfigTypeDef",
        "TargetGroupsConfig": "TargetGroupsConfigTypeDef",
    },
    total=False,
)

LoadPermissionModificationsTypeDef = TypedDict(
    "LoadPermissionModificationsTypeDef",
    {
        "Add": List["LoadPermissionRequestTypeDef"],
        "Remove": List["LoadPermissionRequestTypeDef"],
    },
    total=False,
)

LoadPermissionRequestTypeDef = TypedDict(
    "LoadPermissionRequestTypeDef",
    {
        "Group": Literal["all"],
        "UserId": str,
    },
    total=False,
)

LoadPermissionTypeDef = TypedDict(
    "LoadPermissionTypeDef",
    {
        "UserId": str,
        "Group": Literal["all"],
    },
    total=False,
)

LocalGatewayRouteTableTypeDef = TypedDict(
    "LocalGatewayRouteTableTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "LocalGatewayId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "LocalGatewayId": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTableVpcAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "LocalGatewayId": str,
        "VpcId": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTypeDef = TypedDict(
    "LocalGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "Type": LocalGatewayRouteTypeType,
        "State": LocalGatewayRouteStateType,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "OwnerId": str,
    },
    total=False,
)

LocalGatewayTypeDef = TypedDict(
    "LocalGatewayTypeDef",
    {
        "LocalGatewayId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayVirtualInterfaceGroupTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupId": str,
        "LocalGatewayVirtualInterfaceIds": List[str],
        "LocalGatewayId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayVirtualInterfaceTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceTypeDef",
    {
        "LocalGatewayVirtualInterfaceId": str,
        "LocalGatewayId": str,
        "Vlan": int,
        "LocalAddress": str,
        "PeerAddress": str,
        "LocalBgpAsn": int,
        "PeerBgpAsn": int,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ManagedPrefixListTypeDef = TypedDict(
    "ManagedPrefixListTypeDef",
    {
        "PrefixListId": str,
        "AddressFamily": str,
        "State": PrefixListStateType,
        "StateMessage": str,
        "PrefixListArn": str,
        "PrefixListName": str,
        "MaxEntries": int,
        "Version": int,
        "Tags": List["TagTypeDef"],
        "OwnerId": str,
    },
    total=False,
)

MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

_RequiredModifyAddressAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyAddressAttributeRequestTypeDef",
    {
        "AllocationId": str,
    },
)
_OptionalModifyAddressAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyAddressAttributeRequestTypeDef",
    {
        "DomainName": str,
        "DryRun": bool,
    },
    total=False,
)


class ModifyAddressAttributeRequestTypeDef(
    _RequiredModifyAddressAttributeRequestTypeDef, _OptionalModifyAddressAttributeRequestTypeDef
):
    pass


ModifyAddressAttributeResultResponseTypeDef = TypedDict(
    "ModifyAddressAttributeResultResponseTypeDef",
    {
        "Address": "AddressAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyAvailabilityZoneGroupRequestTypeDef = TypedDict(
    "_RequiredModifyAvailabilityZoneGroupRequestTypeDef",
    {
        "GroupName": str,
        "OptInStatus": ModifyAvailabilityZoneOptInStatusType,
    },
)
_OptionalModifyAvailabilityZoneGroupRequestTypeDef = TypedDict(
    "_OptionalModifyAvailabilityZoneGroupRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyAvailabilityZoneGroupRequestTypeDef(
    _RequiredModifyAvailabilityZoneGroupRequestTypeDef,
    _OptionalModifyAvailabilityZoneGroupRequestTypeDef,
):
    pass


ModifyAvailabilityZoneGroupResultResponseTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyCapacityReservationRequestTypeDef = TypedDict(
    "_RequiredModifyCapacityReservationRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalModifyCapacityReservationRequestTypeDef = TypedDict(
    "_OptionalModifyCapacityReservationRequestTypeDef",
    {
        "InstanceCount": int,
        "EndDate": Union[datetime, str],
        "EndDateType": EndDateTypeType,
        "Accept": bool,
        "DryRun": bool,
    },
    total=False,
)


class ModifyCapacityReservationRequestTypeDef(
    _RequiredModifyCapacityReservationRequestTypeDef,
    _OptionalModifyCapacityReservationRequestTypeDef,
):
    pass


ModifyCapacityReservationResultResponseTypeDef = TypedDict(
    "ModifyCapacityReservationResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClientVpnEndpointRequestTypeDef = TypedDict(
    "_RequiredModifyClientVpnEndpointRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalModifyClientVpnEndpointRequestTypeDef = TypedDict(
    "_OptionalModifyClientVpnEndpointRequestTypeDef",
    {
        "ServerCertificateArn": str,
        "ConnectionLogOptions": "ConnectionLogOptionsTypeDef",
        "DnsServers": "DnsServersOptionsModifyStructureTypeDef",
        "VpnPort": int,
        "Description": str,
        "SplitTunnel": bool,
        "DryRun": bool,
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "SelfServicePortal": SelfServicePortalType,
        "ClientConnectOptions": "ClientConnectOptionsTypeDef",
    },
    total=False,
)


class ModifyClientVpnEndpointRequestTypeDef(
    _RequiredModifyClientVpnEndpointRequestTypeDef, _OptionalModifyClientVpnEndpointRequestTypeDef
):
    pass


ModifyClientVpnEndpointResultResponseTypeDef = TypedDict(
    "ModifyClientVpnEndpointResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDefaultCreditSpecificationRequestTypeDef = TypedDict(
    "_RequiredModifyDefaultCreditSpecificationRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "CpuCredits": str,
    },
)
_OptionalModifyDefaultCreditSpecificationRequestTypeDef = TypedDict(
    "_OptionalModifyDefaultCreditSpecificationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyDefaultCreditSpecificationRequestTypeDef(
    _RequiredModifyDefaultCreditSpecificationRequestTypeDef,
    _OptionalModifyDefaultCreditSpecificationRequestTypeDef,
):
    pass


ModifyDefaultCreditSpecificationResultResponseTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationResultResponseTypeDef",
    {
        "InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEbsDefaultKmsKeyIdRequestTypeDef = TypedDict(
    "_RequiredModifyEbsDefaultKmsKeyIdRequestTypeDef",
    {
        "KmsKeyId": str,
    },
)
_OptionalModifyEbsDefaultKmsKeyIdRequestTypeDef = TypedDict(
    "_OptionalModifyEbsDefaultKmsKeyIdRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyEbsDefaultKmsKeyIdRequestTypeDef(
    _RequiredModifyEbsDefaultKmsKeyIdRequestTypeDef, _OptionalModifyEbsDefaultKmsKeyIdRequestTypeDef
):
    pass


ModifyEbsDefaultKmsKeyIdResultResponseTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdResultResponseTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyFleetRequestTypeDef = TypedDict(
    "_RequiredModifyFleetRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalModifyFleetRequestTypeDef = TypedDict(
    "_OptionalModifyFleetRequestTypeDef",
    {
        "DryRun": bool,
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicyType,
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigRequestTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationRequestTypeDef",
    },
    total=False,
)


class ModifyFleetRequestTypeDef(
    _RequiredModifyFleetRequestTypeDef, _OptionalModifyFleetRequestTypeDef
):
    pass


ModifyFleetResultResponseTypeDef = TypedDict(
    "ModifyFleetResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyFpgaImageAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyFpgaImageAttributeRequestTypeDef",
    {
        "FpgaImageId": str,
    },
)
_OptionalModifyFpgaImageAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyFpgaImageAttributeRequestTypeDef",
    {
        "DryRun": bool,
        "Attribute": FpgaImageAttributeNameType,
        "OperationType": OperationTypeType,
        "UserIds": List[str],
        "UserGroups": List[str],
        "ProductCodes": List[str],
        "LoadPermission": "LoadPermissionModificationsTypeDef",
        "Description": str,
        "Name": str,
    },
    total=False,
)


class ModifyFpgaImageAttributeRequestTypeDef(
    _RequiredModifyFpgaImageAttributeRequestTypeDef, _OptionalModifyFpgaImageAttributeRequestTypeDef
):
    pass


ModifyFpgaImageAttributeResultResponseTypeDef = TypedDict(
    "ModifyFpgaImageAttributeResultResponseTypeDef",
    {
        "FpgaImageAttribute": "FpgaImageAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyHostsRequestTypeDef = TypedDict(
    "_RequiredModifyHostsRequestTypeDef",
    {
        "HostIds": List[str],
    },
)
_OptionalModifyHostsRequestTypeDef = TypedDict(
    "_OptionalModifyHostsRequestTypeDef",
    {
        "AutoPlacement": AutoPlacementType,
        "HostRecovery": HostRecoveryType,
        "InstanceType": str,
        "InstanceFamily": str,
    },
    total=False,
)


class ModifyHostsRequestTypeDef(
    _RequiredModifyHostsRequestTypeDef, _OptionalModifyHostsRequestTypeDef
):
    pass


ModifyHostsResultResponseTypeDef = TypedDict(
    "ModifyHostsResultResponseTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIdFormatRequestTypeDef = TypedDict(
    "ModifyIdFormatRequestTypeDef",
    {
        "Resource": str,
        "UseLongIds": bool,
    },
)

ModifyIdentityIdFormatRequestTypeDef = TypedDict(
    "ModifyIdentityIdFormatRequestTypeDef",
    {
        "PrincipalArn": str,
        "Resource": str,
        "UseLongIds": bool,
    },
)

ModifyImageAttributeRequestImageTypeDef = TypedDict(
    "ModifyImageAttributeRequestImageTypeDef",
    {
        "Attribute": str,
        "Description": "AttributeValueTypeDef",
        "LaunchPermission": "LaunchPermissionModificationsTypeDef",
        "OperationType": OperationTypeType,
        "ProductCodes": List[str],
        "UserGroups": List[str],
        "UserIds": List[str],
        "Value": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredModifyImageAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyImageAttributeRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalModifyImageAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyImageAttributeRequestTypeDef",
    {
        "Attribute": str,
        "Description": "AttributeValueTypeDef",
        "LaunchPermission": "LaunchPermissionModificationsTypeDef",
        "OperationType": OperationTypeType,
        "ProductCodes": List[str],
        "UserGroups": List[str],
        "UserIds": List[str],
        "Value": str,
        "DryRun": bool,
    },
    total=False,
)


class ModifyImageAttributeRequestTypeDef(
    _RequiredModifyImageAttributeRequestTypeDef, _OptionalModifyImageAttributeRequestTypeDef
):
    pass


ModifyInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "ModifyInstanceAttributeRequestInstanceTypeDef",
    {
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "Attribute": InstanceAttributeNameType,
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingSpecificationTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "Groups": List[str],
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "Kernel": "AttributeValueTypeDef",
        "Ramdisk": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "BlobAttributeValueTypeDef",
        "Value": str,
    },
    total=False,
)

_RequiredModifyInstanceAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceAttributeRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstanceAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceAttributeRequestTypeDef",
    {
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "Attribute": InstanceAttributeNameType,
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingSpecificationTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "Groups": List[str],
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "Kernel": "AttributeValueTypeDef",
        "Ramdisk": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "BlobAttributeValueTypeDef",
        "Value": str,
    },
    total=False,
)


class ModifyInstanceAttributeRequestTypeDef(
    _RequiredModifyInstanceAttributeRequestTypeDef, _OptionalModifyInstanceAttributeRequestTypeDef
):
    pass


_RequiredModifyInstanceCapacityReservationAttributesRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceCapacityReservationAttributesRequestTypeDef",
    {
        "InstanceId": str,
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
    },
)
_OptionalModifyInstanceCapacityReservationAttributesRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceCapacityReservationAttributesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyInstanceCapacityReservationAttributesRequestTypeDef(
    _RequiredModifyInstanceCapacityReservationAttributesRequestTypeDef,
    _OptionalModifyInstanceCapacityReservationAttributesRequestTypeDef,
):
    pass


ModifyInstanceCapacityReservationAttributesResultResponseTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceCreditSpecificationRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceCreditSpecificationRequestTypeDef",
    {
        "InstanceCreditSpecifications": List["InstanceCreditSpecificationRequestTypeDef"],
    },
)
_OptionalModifyInstanceCreditSpecificationRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceCreditSpecificationRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)


class ModifyInstanceCreditSpecificationRequestTypeDef(
    _RequiredModifyInstanceCreditSpecificationRequestTypeDef,
    _OptionalModifyInstanceCreditSpecificationRequestTypeDef,
):
    pass


ModifyInstanceCreditSpecificationResultResponseTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationResultResponseTypeDef",
    {
        "SuccessfulInstanceCreditSpecifications": List[
            "SuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "UnsuccessfulInstanceCreditSpecifications": List[
            "UnsuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceEventStartTimeRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceEventStartTimeRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceEventId": str,
        "NotBefore": Union[datetime, str],
    },
)
_OptionalModifyInstanceEventStartTimeRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceEventStartTimeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyInstanceEventStartTimeRequestTypeDef(
    _RequiredModifyInstanceEventStartTimeRequestTypeDef,
    _OptionalModifyInstanceEventStartTimeRequestTypeDef,
):
    pass


ModifyInstanceEventStartTimeResultResponseTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeResultResponseTypeDef",
    {
        "Event": "InstanceStatusEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceMetadataOptionsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
        "DryRun": bool,
    },
    total=False,
)


class ModifyInstanceMetadataOptionsRequestTypeDef(
    _RequiredModifyInstanceMetadataOptionsRequestTypeDef,
    _OptionalModifyInstanceMetadataOptionsRequestTypeDef,
):
    pass


ModifyInstanceMetadataOptionsResultResponseTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsResultResponseTypeDef",
    {
        "InstanceId": str,
        "InstanceMetadataOptions": "InstanceMetadataOptionsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstancePlacementRequestTypeDef = TypedDict(
    "_RequiredModifyInstancePlacementRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstancePlacementRequestTypeDef = TypedDict(
    "_OptionalModifyInstancePlacementRequestTypeDef",
    {
        "Affinity": AffinityType,
        "GroupName": str,
        "HostId": str,
        "Tenancy": HostTenancyType,
        "PartitionNumber": int,
        "HostResourceGroupArn": str,
    },
    total=False,
)


class ModifyInstancePlacementRequestTypeDef(
    _RequiredModifyInstancePlacementRequestTypeDef, _OptionalModifyInstancePlacementRequestTypeDef
):
    pass


ModifyInstancePlacementResultResponseTypeDef = TypedDict(
    "ModifyInstancePlacementResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLaunchTemplateRequestTypeDef = TypedDict(
    "ModifyLaunchTemplateRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "DefaultVersion": str,
    },
    total=False,
)

ModifyLaunchTemplateResultResponseTypeDef = TypedDict(
    "ModifyLaunchTemplateResultResponseTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyManagedPrefixListRequestTypeDef = TypedDict(
    "_RequiredModifyManagedPrefixListRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalModifyManagedPrefixListRequestTypeDef = TypedDict(
    "_OptionalModifyManagedPrefixListRequestTypeDef",
    {
        "DryRun": bool,
        "CurrentVersion": int,
        "PrefixListName": str,
        "AddEntries": List["AddPrefixListEntryTypeDef"],
        "RemoveEntries": List["RemovePrefixListEntryTypeDef"],
    },
    total=False,
)


class ModifyManagedPrefixListRequestTypeDef(
    _RequiredModifyManagedPrefixListRequestTypeDef, _OptionalModifyManagedPrefixListRequestTypeDef
):
    pass


ModifyManagedPrefixListResultResponseTypeDef = TypedDict(
    "ModifyManagedPrefixListResultResponseTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef = TypedDict(
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentChangesTypeDef",
        "Description": "AttributeValueTypeDef",
        "DryRun": bool,
        "Groups": List[str],
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

_RequiredModifyNetworkInterfaceAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyNetworkInterfaceAttributeRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalModifyNetworkInterfaceAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyNetworkInterfaceAttributeRequestTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentChangesTypeDef",
        "Description": "AttributeValueTypeDef",
        "DryRun": bool,
        "Groups": List[str],
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
    },
    total=False,
)


class ModifyNetworkInterfaceAttributeRequestTypeDef(
    _RequiredModifyNetworkInterfaceAttributeRequestTypeDef,
    _OptionalModifyNetworkInterfaceAttributeRequestTypeDef,
):
    pass


_RequiredModifyReservedInstancesRequestTypeDef = TypedDict(
    "_RequiredModifyReservedInstancesRequestTypeDef",
    {
        "ReservedInstancesIds": List[str],
        "TargetConfigurations": List["ReservedInstancesConfigurationTypeDef"],
    },
)
_OptionalModifyReservedInstancesRequestTypeDef = TypedDict(
    "_OptionalModifyReservedInstancesRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class ModifyReservedInstancesRequestTypeDef(
    _RequiredModifyReservedInstancesRequestTypeDef, _OptionalModifyReservedInstancesRequestTypeDef
):
    pass


ModifyReservedInstancesResultResponseTypeDef = TypedDict(
    "ModifyReservedInstancesResultResponseTypeDef",
    {
        "ReservedInstancesModificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "ModifySnapshotAttributeRequestSnapshotTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "CreateVolumePermission": "CreateVolumePermissionModificationsTypeDef",
        "GroupNames": List[str],
        "OperationType": OperationTypeType,
        "UserIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

_RequiredModifySnapshotAttributeRequestTypeDef = TypedDict(
    "_RequiredModifySnapshotAttributeRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalModifySnapshotAttributeRequestTypeDef = TypedDict(
    "_OptionalModifySnapshotAttributeRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "CreateVolumePermission": "CreateVolumePermissionModificationsTypeDef",
        "GroupNames": List[str],
        "OperationType": OperationTypeType,
        "UserIds": List[str],
        "DryRun": bool,
    },
    total=False,
)


class ModifySnapshotAttributeRequestTypeDef(
    _RequiredModifySnapshotAttributeRequestTypeDef, _OptionalModifySnapshotAttributeRequestTypeDef
):
    pass


_RequiredModifySpotFleetRequestRequestTypeDef = TypedDict(
    "_RequiredModifySpotFleetRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
    },
)
_OptionalModifySpotFleetRequestRequestTypeDef = TypedDict(
    "_OptionalModifySpotFleetRequestRequestTypeDef",
    {
        "ExcessCapacityTerminationPolicy": ExcessCapacityTerminationPolicyType,
        "LaunchTemplateConfigs": List["LaunchTemplateConfigTypeDef"],
        "TargetCapacity": int,
        "OnDemandTargetCapacity": int,
    },
    total=False,
)


class ModifySpotFleetRequestRequestTypeDef(
    _RequiredModifySpotFleetRequestRequestTypeDef, _OptionalModifySpotFleetRequestRequestTypeDef
):
    pass


ModifySpotFleetRequestResponseResponseTypeDef = TypedDict(
    "ModifySpotFleetRequestResponseResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifySubnetAttributeRequestTypeDef = TypedDict(
    "_RequiredModifySubnetAttributeRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalModifySubnetAttributeRequestTypeDef = TypedDict(
    "_OptionalModifySubnetAttributeRequestTypeDef",
    {
        "AssignIpv6AddressOnCreation": "AttributeBooleanValueTypeDef",
        "MapPublicIpOnLaunch": "AttributeBooleanValueTypeDef",
        "MapCustomerOwnedIpOnLaunch": "AttributeBooleanValueTypeDef",
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)


class ModifySubnetAttributeRequestTypeDef(
    _RequiredModifySubnetAttributeRequestTypeDef, _OptionalModifySubnetAttributeRequestTypeDef
):
    pass


_RequiredModifyTrafficMirrorFilterNetworkServicesRequestTypeDef = TypedDict(
    "_RequiredModifyTrafficMirrorFilterNetworkServicesRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
    },
)
_OptionalModifyTrafficMirrorFilterNetworkServicesRequestTypeDef = TypedDict(
    "_OptionalModifyTrafficMirrorFilterNetworkServicesRequestTypeDef",
    {
        "AddNetworkServices": List[Literal["amazon-dns"]],
        "RemoveNetworkServices": List[Literal["amazon-dns"]],
        "DryRun": bool,
    },
    total=False,
)


class ModifyTrafficMirrorFilterNetworkServicesRequestTypeDef(
    _RequiredModifyTrafficMirrorFilterNetworkServicesRequestTypeDef,
    _OptionalModifyTrafficMirrorFilterNetworkServicesRequestTypeDef,
):
    pass


ModifyTrafficMirrorFilterNetworkServicesResultResponseTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesResultResponseTypeDef",
    {
        "TrafficMirrorFilter": "TrafficMirrorFilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTrafficMirrorFilterRuleRequestTypeDef = TypedDict(
    "_RequiredModifyTrafficMirrorFilterRuleRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
    },
)
_OptionalModifyTrafficMirrorFilterRuleRequestTypeDef = TypedDict(
    "_OptionalModifyTrafficMirrorFilterRuleRequestTypeDef",
    {
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "DestinationPortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "Protocol": int,
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "Description": str,
        "RemoveFields": List[TrafficMirrorFilterRuleFieldType],
        "DryRun": bool,
    },
    total=False,
)


class ModifyTrafficMirrorFilterRuleRequestTypeDef(
    _RequiredModifyTrafficMirrorFilterRuleRequestTypeDef,
    _OptionalModifyTrafficMirrorFilterRuleRequestTypeDef,
):
    pass


ModifyTrafficMirrorFilterRuleResultResponseTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleResultResponseTypeDef",
    {
        "TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTrafficMirrorSessionRequestTypeDef = TypedDict(
    "_RequiredModifyTrafficMirrorSessionRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
    },
)
_OptionalModifyTrafficMirrorSessionRequestTypeDef = TypedDict(
    "_OptionalModifyTrafficMirrorSessionRequestTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "PacketLength": int,
        "SessionNumber": int,
        "VirtualNetworkId": int,
        "Description": str,
        "RemoveFields": List[TrafficMirrorSessionFieldType],
        "DryRun": bool,
    },
    total=False,
)


class ModifyTrafficMirrorSessionRequestTypeDef(
    _RequiredModifyTrafficMirrorSessionRequestTypeDef,
    _OptionalModifyTrafficMirrorSessionRequestTypeDef,
):
    pass


ModifyTrafficMirrorSessionResultResponseTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionResultResponseTypeDef",
    {
        "TrafficMirrorSession": "TrafficMirrorSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayOptionsTypeDef",
    {
        "AddTransitGatewayCidrBlocks": List[str],
        "RemoveTransitGatewayCidrBlocks": List[str],
        "VpnEcmpSupport": VpnEcmpSupportValueType,
        "DnsSupport": DnsSupportValueType,
        "AutoAcceptSharedAttachments": AutoAcceptSharedAttachmentsValueType,
        "DefaultRouteTableAssociation": DefaultRouteTableAssociationValueType,
        "AssociationDefaultRouteTableId": str,
        "DefaultRouteTablePropagation": DefaultRouteTablePropagationValueType,
        "PropagationDefaultRouteTableId": str,
    },
    total=False,
)

_RequiredModifyTransitGatewayPrefixListReferenceRequestTypeDef = TypedDict(
    "_RequiredModifyTransitGatewayPrefixListReferenceRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
    },
)
_OptionalModifyTransitGatewayPrefixListReferenceRequestTypeDef = TypedDict(
    "_OptionalModifyTransitGatewayPrefixListReferenceRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)


class ModifyTransitGatewayPrefixListReferenceRequestTypeDef(
    _RequiredModifyTransitGatewayPrefixListReferenceRequestTypeDef,
    _OptionalModifyTransitGatewayPrefixListReferenceRequestTypeDef,
):
    pass


ModifyTransitGatewayPrefixListReferenceResultResponseTypeDef = TypedDict(
    "ModifyTransitGatewayPrefixListReferenceResultResponseTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTransitGatewayRequestTypeDef = TypedDict(
    "_RequiredModifyTransitGatewayRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalModifyTransitGatewayRequestTypeDef = TypedDict(
    "_OptionalModifyTransitGatewayRequestTypeDef",
    {
        "Description": str,
        "Options": "ModifyTransitGatewayOptionsTypeDef",
        "DryRun": bool,
    },
    total=False,
)


class ModifyTransitGatewayRequestTypeDef(
    _RequiredModifyTransitGatewayRequestTypeDef, _OptionalModifyTransitGatewayRequestTypeDef
):
    pass


ModifyTransitGatewayResultResponseTypeDef = TypedDict(
    "ModifyTransitGatewayResultResponseTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": DnsSupportValueType,
        "Ipv6Support": Ipv6SupportValueType,
        "ApplianceModeSupport": ApplianceModeSupportValueType,
    },
    total=False,
)

_RequiredModifyTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_RequiredModifyTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalModifyTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_OptionalModifyTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "AddSubnetIds": List[str],
        "RemoveSubnetIds": List[str],
        "Options": "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
        "DryRun": bool,
    },
    total=False,
)


class ModifyTransitGatewayVpcAttachmentRequestTypeDef(
    _RequiredModifyTransitGatewayVpcAttachmentRequestTypeDef,
    _OptionalModifyTransitGatewayVpcAttachmentRequestTypeDef,
):
    pass


ModifyTransitGatewayVpcAttachmentResultResponseTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentResultResponseTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVolumeAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyVolumeAttributeRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalModifyVolumeAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyVolumeAttributeRequestTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
    },
    total=False,
)


class ModifyVolumeAttributeRequestTypeDef(
    _RequiredModifyVolumeAttributeRequestTypeDef, _OptionalModifyVolumeAttributeRequestTypeDef
):
    pass


ModifyVolumeAttributeRequestVolumeTypeDef = TypedDict(
    "ModifyVolumeAttributeRequestVolumeTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
    },
    total=False,
)

_RequiredModifyVolumeRequestTypeDef = TypedDict(
    "_RequiredModifyVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalModifyVolumeRequestTypeDef = TypedDict(
    "_OptionalModifyVolumeRequestTypeDef",
    {
        "DryRun": bool,
        "Size": int,
        "VolumeType": VolumeTypeType,
        "Iops": int,
        "Throughput": int,
        "MultiAttachEnabled": bool,
    },
    total=False,
)


class ModifyVolumeRequestTypeDef(
    _RequiredModifyVolumeRequestTypeDef, _OptionalModifyVolumeRequestTypeDef
):
    pass


ModifyVolumeResultResponseTypeDef = TypedDict(
    "ModifyVolumeResultResponseTypeDef",
    {
        "VolumeModification": "VolumeModificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcAttributeRequestTypeDef = TypedDict(
    "_RequiredModifyVpcAttributeRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalModifyVpcAttributeRequestTypeDef = TypedDict(
    "_OptionalModifyVpcAttributeRequestTypeDef",
    {
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
    },
    total=False,
)


class ModifyVpcAttributeRequestTypeDef(
    _RequiredModifyVpcAttributeRequestTypeDef, _OptionalModifyVpcAttributeRequestTypeDef
):
    pass


ModifyVpcAttributeRequestVpcTypeDef = TypedDict(
    "ModifyVpcAttributeRequestVpcTypeDef",
    {
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

_RequiredModifyVpcEndpointConnectionNotificationRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointConnectionNotificationRequestTypeDef",
    {
        "ConnectionNotificationId": str,
    },
)
_OptionalModifyVpcEndpointConnectionNotificationRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointConnectionNotificationRequestTypeDef",
    {
        "DryRun": bool,
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
    },
    total=False,
)


class ModifyVpcEndpointConnectionNotificationRequestTypeDef(
    _RequiredModifyVpcEndpointConnectionNotificationRequestTypeDef,
    _OptionalModifyVpcEndpointConnectionNotificationRequestTypeDef,
):
    pass


ModifyVpcEndpointConnectionNotificationResultResponseTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationResultResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointRequestTypeDef",
    {
        "VpcEndpointId": str,
    },
)
_OptionalModifyVpcEndpointRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointRequestTypeDef",
    {
        "DryRun": bool,
        "ResetPolicy": bool,
        "PolicyDocument": str,
        "AddRouteTableIds": List[str],
        "RemoveRouteTableIds": List[str],
        "AddSubnetIds": List[str],
        "RemoveSubnetIds": List[str],
        "AddSecurityGroupIds": List[str],
        "RemoveSecurityGroupIds": List[str],
        "PrivateDnsEnabled": bool,
    },
    total=False,
)


class ModifyVpcEndpointRequestTypeDef(
    _RequiredModifyVpcEndpointRequestTypeDef, _OptionalModifyVpcEndpointRequestTypeDef
):
    pass


ModifyVpcEndpointResultResponseTypeDef = TypedDict(
    "ModifyVpcEndpointResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointServiceConfigurationRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointServiceConfigurationRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalModifyVpcEndpointServiceConfigurationRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointServiceConfigurationRequestTypeDef",
    {
        "DryRun": bool,
        "PrivateDnsName": str,
        "RemovePrivateDnsName": bool,
        "AcceptanceRequired": bool,
        "AddNetworkLoadBalancerArns": List[str],
        "RemoveNetworkLoadBalancerArns": List[str],
        "AddGatewayLoadBalancerArns": List[str],
        "RemoveGatewayLoadBalancerArns": List[str],
    },
    total=False,
)


class ModifyVpcEndpointServiceConfigurationRequestTypeDef(
    _RequiredModifyVpcEndpointServiceConfigurationRequestTypeDef,
    _OptionalModifyVpcEndpointServiceConfigurationRequestTypeDef,
):
    pass


ModifyVpcEndpointServiceConfigurationResultResponseTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointServicePermissionsRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointServicePermissionsRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalModifyVpcEndpointServicePermissionsRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointServicePermissionsRequestTypeDef",
    {
        "DryRun": bool,
        "AddAllowedPrincipals": List[str],
        "RemoveAllowedPrincipals": List[str],
    },
    total=False,
)


class ModifyVpcEndpointServicePermissionsRequestTypeDef(
    _RequiredModifyVpcEndpointServicePermissionsRequestTypeDef,
    _OptionalModifyVpcEndpointServicePermissionsRequestTypeDef,
):
    pass


ModifyVpcEndpointServicePermissionsResultResponseTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsResultResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcPeeringConnectionOptionsRequestTypeDef = TypedDict(
    "_RequiredModifyVpcPeeringConnectionOptionsRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalModifyVpcPeeringConnectionOptionsRequestTypeDef = TypedDict(
    "_OptionalModifyVpcPeeringConnectionOptionsRequestTypeDef",
    {
        "AccepterPeeringConnectionOptions": "PeeringConnectionOptionsRequestTypeDef",
        "DryRun": bool,
        "RequesterPeeringConnectionOptions": "PeeringConnectionOptionsRequestTypeDef",
    },
    total=False,
)


class ModifyVpcPeeringConnectionOptionsRequestTypeDef(
    _RequiredModifyVpcPeeringConnectionOptionsRequestTypeDef,
    _OptionalModifyVpcPeeringConnectionOptionsRequestTypeDef,
):
    pass


ModifyVpcPeeringConnectionOptionsResultResponseTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsResultResponseTypeDef",
    {
        "AccepterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "RequesterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcTenancyRequestTypeDef = TypedDict(
    "_RequiredModifyVpcTenancyRequestTypeDef",
    {
        "VpcId": str,
        "InstanceTenancy": Literal["default"],
    },
)
_OptionalModifyVpcTenancyRequestTypeDef = TypedDict(
    "_OptionalModifyVpcTenancyRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyVpcTenancyRequestTypeDef(
    _RequiredModifyVpcTenancyRequestTypeDef, _OptionalModifyVpcTenancyRequestTypeDef
):
    pass


ModifyVpcTenancyResultResponseTypeDef = TypedDict(
    "ModifyVpcTenancyResultResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnConnectionOptionsRequestTypeDef = TypedDict(
    "_RequiredModifyVpnConnectionOptionsRequestTypeDef",
    {
        "VpnConnectionId": str,
    },
)
_OptionalModifyVpnConnectionOptionsRequestTypeDef = TypedDict(
    "_OptionalModifyVpnConnectionOptionsRequestTypeDef",
    {
        "LocalIpv4NetworkCidr": str,
        "RemoteIpv4NetworkCidr": str,
        "LocalIpv6NetworkCidr": str,
        "RemoteIpv6NetworkCidr": str,
        "DryRun": bool,
    },
    total=False,
)


class ModifyVpnConnectionOptionsRequestTypeDef(
    _RequiredModifyVpnConnectionOptionsRequestTypeDef,
    _OptionalModifyVpnConnectionOptionsRequestTypeDef,
):
    pass


ModifyVpnConnectionOptionsResultResponseTypeDef = TypedDict(
    "ModifyVpnConnectionOptionsResultResponseTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnConnectionRequestTypeDef = TypedDict(
    "_RequiredModifyVpnConnectionRequestTypeDef",
    {
        "VpnConnectionId": str,
    },
)
_OptionalModifyVpnConnectionRequestTypeDef = TypedDict(
    "_OptionalModifyVpnConnectionRequestTypeDef",
    {
        "TransitGatewayId": str,
        "CustomerGatewayId": str,
        "VpnGatewayId": str,
        "DryRun": bool,
    },
    total=False,
)


class ModifyVpnConnectionRequestTypeDef(
    _RequiredModifyVpnConnectionRequestTypeDef, _OptionalModifyVpnConnectionRequestTypeDef
):
    pass


ModifyVpnConnectionResultResponseTypeDef = TypedDict(
    "ModifyVpnConnectionResultResponseTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnTunnelCertificateRequestTypeDef = TypedDict(
    "_RequiredModifyVpnTunnelCertificateRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
    },
)
_OptionalModifyVpnTunnelCertificateRequestTypeDef = TypedDict(
    "_OptionalModifyVpnTunnelCertificateRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyVpnTunnelCertificateRequestTypeDef(
    _RequiredModifyVpnTunnelCertificateRequestTypeDef,
    _OptionalModifyVpnTunnelCertificateRequestTypeDef,
):
    pass


ModifyVpnTunnelCertificateResultResponseTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateResultResponseTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnTunnelOptionsRequestTypeDef = TypedDict(
    "_RequiredModifyVpnTunnelOptionsRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "TunnelOptions": "ModifyVpnTunnelOptionsSpecificationTypeDef",
    },
)
_OptionalModifyVpnTunnelOptionsRequestTypeDef = TypedDict(
    "_OptionalModifyVpnTunnelOptionsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ModifyVpnTunnelOptionsRequestTypeDef(
    _RequiredModifyVpnTunnelOptionsRequestTypeDef, _OptionalModifyVpnTunnelOptionsRequestTypeDef
):
    pass


ModifyVpnTunnelOptionsResultResponseTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsResultResponseTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DPDTimeoutSeconds": int,
        "DPDTimeoutAction": str,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersRequestListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersRequestListValueTypeDef"],
        "IKEVersions": List["IKEVersionsRequestListValueTypeDef"],
        "StartupAction": str,
    },
    total=False,
)

MonitorInstancesRequestInstanceTypeDef = TypedDict(
    "MonitorInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredMonitorInstancesRequestTypeDef = TypedDict(
    "_RequiredMonitorInstancesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalMonitorInstancesRequestTypeDef = TypedDict(
    "_OptionalMonitorInstancesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class MonitorInstancesRequestTypeDef(
    _RequiredMonitorInstancesRequestTypeDef, _OptionalMonitorInstancesRequestTypeDef
):
    pass


MonitorInstancesResultResponseTypeDef = TypedDict(
    "MonitorInstancesResultResponseTypeDef",
    {
        "InstanceMonitorings": List["InstanceMonitoringTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringTypeDef = TypedDict(
    "MonitoringTypeDef",
    {
        "State": MonitoringStateType,
    },
    total=False,
)

_RequiredMoveAddressToVpcRequestTypeDef = TypedDict(
    "_RequiredMoveAddressToVpcRequestTypeDef",
    {
        "PublicIp": str,
    },
)
_OptionalMoveAddressToVpcRequestTypeDef = TypedDict(
    "_OptionalMoveAddressToVpcRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class MoveAddressToVpcRequestTypeDef(
    _RequiredMoveAddressToVpcRequestTypeDef, _OptionalMoveAddressToVpcRequestTypeDef
):
    pass


MoveAddressToVpcResultResponseTypeDef = TypedDict(
    "MoveAddressToVpcResultResponseTypeDef",
    {
        "AllocationId": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MovingAddressStatusTypeDef = TypedDict(
    "MovingAddressStatusTypeDef",
    {
        "MoveStatus": MoveStatusType,
        "PublicIp": str,
    },
    total=False,
)

NatGatewayAddressTypeDef = TypedDict(
    "NatGatewayAddressTypeDef",
    {
        "AllocationId": str,
        "NetworkInterfaceId": str,
        "PrivateIp": str,
        "PublicIp": str,
    },
    total=False,
)

NatGatewayTypeDef = TypedDict(
    "NatGatewayTypeDef",
    {
        "CreateTime": datetime,
        "DeleteTime": datetime,
        "FailureCode": str,
        "FailureMessage": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "NatGatewayId": str,
        "ProvisionedBandwidth": "ProvisionedBandwidthTypeDef",
        "State": NatGatewayStateType,
        "SubnetId": str,
        "VpcId": str,
        "Tags": List["TagTypeDef"],
        "ConnectivityType": ConnectivityTypeType,
    },
    total=False,
)

NetworkAclAssociationTypeDef = TypedDict(
    "NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": str,
        "NetworkAclId": str,
        "SubnetId": str,
    },
    total=False,
)

NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
    total=False,
)

NetworkAclTypeDef = TypedDict(
    "NetworkAclTypeDef",
    {
        "Associations": List["NetworkAclAssociationTypeDef"],
        "Entries": List["NetworkAclEntryTypeDef"],
        "IsDefault": bool,
        "NetworkAclId": str,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
        "OwnerId": str,
    },
    total=False,
)

NetworkCardInfoTypeDef = TypedDict(
    "NetworkCardInfoTypeDef",
    {
        "NetworkCardIndex": int,
        "NetworkPerformance": str,
        "MaximumNetworkInterfaces": int,
    },
    total=False,
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "NetworkPerformance": str,
        "MaximumNetworkInterfaces": int,
        "MaximumNetworkCards": int,
        "DefaultNetworkCardIndex": int,
        "NetworkCards": List["NetworkCardInfoTypeDef"],
        "Ipv4AddressesPerInterface": int,
        "Ipv6AddressesPerInterface": int,
        "Ipv6Supported": bool,
        "EnaSupport": EnaSupportType,
        "EfaSupported": bool,
        "EfaInfo": "EfaInfoTypeDef",
    },
    total=False,
)

NetworkInsightsAnalysisTypeDef = TypedDict(
    "NetworkInsightsAnalysisTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "NetworkInsightsAnalysisArn": str,
        "NetworkInsightsPathId": str,
        "FilterInArns": List[str],
        "StartDate": datetime,
        "Status": AnalysisStatusType,
        "StatusMessage": str,
        "NetworkPathFound": bool,
        "ForwardPathComponents": List["PathComponentTypeDef"],
        "ReturnPathComponents": List["PathComponentTypeDef"],
        "Explanations": List["ExplanationTypeDef"],
        "AlternatePathHints": List["AlternatePathHintTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NetworkInsightsPathTypeDef = TypedDict(
    "NetworkInsightsPathTypeDef",
    {
        "NetworkInsightsPathId": str,
        "NetworkInsightsPathArn": str,
        "CreatedDate": datetime,
        "Source": str,
        "Destination": str,
        "SourceIp": str,
        "DestinationIp": str,
        "Protocol": ProtocolType,
        "DestinationPort": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NetworkInterfaceAssociationTypeDef = TypedDict(
    "NetworkInterfaceAssociationTypeDef",
    {
        "AllocationId": str,
        "AssociationId": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
        "CustomerOwnedIp": str,
        "CarrierIp": str,
    },
    total=False,
)

NetworkInterfaceAttachmentChangesTypeDef = TypedDict(
    "NetworkInterfaceAttachmentChangesTypeDef",
    {
        "AttachmentId": str,
        "DeleteOnTermination": bool,
    },
    total=False,
)

NetworkInterfaceAttachmentTypeDef = TypedDict(
    "NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "NetworkCardIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": AttachmentStatusType,
    },
    total=False,
)

NetworkInterfaceIpv6AddressTypeDef = TypedDict(
    "NetworkInterfaceIpv6AddressTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

NetworkInterfacePermissionStateTypeDef = TypedDict(
    "NetworkInterfacePermissionStateTypeDef",
    {
        "State": NetworkInterfacePermissionStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

NetworkInterfacePermissionTypeDef = TypedDict(
    "NetworkInterfacePermissionTypeDef",
    {
        "NetworkInterfacePermissionId": str,
        "NetworkInterfaceId": str,
        "AwsAccountId": str,
        "AwsService": str,
        "Permission": InterfacePermissionTypeType,
        "PermissionState": "NetworkInterfacePermissionStateTypeDef",
    },
    total=False,
)

NetworkInterfacePrivateIpAddressTypeDef = TypedDict(
    "NetworkInterfacePrivateIpAddressTypeDef",
    {
        "Association": "NetworkInterfaceAssociationTypeDef",
        "Primary": bool,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Association": "NetworkInterfaceAssociationTypeDef",
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "AvailabilityZone": str,
        "Description": str,
        "Groups": List["GroupIdentifierTypeDef"],
        "InterfaceType": NetworkInterfaceTypeType,
        "Ipv6Addresses": List["NetworkInterfaceIpv6AddressTypeDef"],
        "MacAddress": str,
        "NetworkInterfaceId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["NetworkInterfacePrivateIpAddressTypeDef"],
        "RequesterId": str,
        "RequesterManaged": bool,
        "SourceDestCheck": bool,
        "Status": NetworkInterfaceStatusType,
        "SubnetId": str,
        "TagSet": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

NewDhcpConfigurationTypeDef = TypedDict(
    "NewDhcpConfigurationTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

OnDemandOptionsRequestTypeDef = TypedDict(
    "OnDemandOptionsRequestTypeDef",
    {
        "AllocationStrategy": FleetOnDemandAllocationStrategyType,
        "CapacityReservationOptions": "CapacityReservationOptionsRequestTypeDef",
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

OnDemandOptionsTypeDef = TypedDict(
    "OnDemandOptionsTypeDef",
    {
        "AllocationStrategy": FleetOnDemandAllocationStrategyType,
        "CapacityReservationOptions": "CapacityReservationOptionsTypeDef",
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
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

PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "SequenceNumber": int,
        "AclRule": "AnalysisAclRuleTypeDef",
        "Component": "AnalysisComponentTypeDef",
        "DestinationVpc": "AnalysisComponentTypeDef",
        "OutboundHeader": "AnalysisPacketHeaderTypeDef",
        "InboundHeader": "AnalysisPacketHeaderTypeDef",
        "RouteTableRoute": "AnalysisRouteTableRouteTypeDef",
        "SecurityGroupRule": "AnalysisSecurityGroupRuleTypeDef",
        "SourceVpc": "AnalysisComponentTypeDef",
        "Subnet": "AnalysisComponentTypeDef",
        "Vpc": "AnalysisComponentTypeDef",
    },
    total=False,
)

PciIdTypeDef = TypedDict(
    "PciIdTypeDef",
    {
        "DeviceId": str,
        "VendorId": str,
        "SubsystemId": str,
        "SubsystemVendorId": str,
    },
    total=False,
)

PeeringAttachmentStatusTypeDef = TypedDict(
    "PeeringAttachmentStatusTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

PeeringConnectionOptionsRequestTypeDef = TypedDict(
    "PeeringConnectionOptionsRequestTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

PeeringConnectionOptionsTypeDef = TypedDict(
    "PeeringConnectionOptionsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

PeeringTgwInfoTypeDef = TypedDict(
    "PeeringTgwInfoTypeDef",
    {
        "TransitGatewayId": str,
        "OwnerId": str,
        "Region": str,
    },
    total=False,
)

Phase1DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase1DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase1EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase1EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase1IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase1IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase2DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase2EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

PlacementGroupInfoTypeDef = TypedDict(
    "PlacementGroupInfoTypeDef",
    {
        "SupportedStrategies": List[PlacementGroupStrategyType],
    },
    total=False,
)

PlacementGroupTypeDef = TypedDict(
    "PlacementGroupTypeDef",
    {
        "GroupName": str,
        "State": PlacementGroupStateType,
        "Strategy": PlacementStrategyType,
        "PartitionCount": int,
        "GroupId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

PlacementResponseTypeDef = TypedDict(
    "PlacementResponseTypeDef",
    {
        "GroupName": str,
    },
    total=False,
)

PlacementTypeDef = TypedDict(
    "PlacementTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "PartitionNumber": int,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
    },
    total=False,
)

PoolCidrBlockTypeDef = TypedDict(
    "PoolCidrBlockTypeDef",
    {
        "Cidr": str,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "From": int,
        "To": int,
    },
    total=False,
)

PrefixListAssociationTypeDef = TypedDict(
    "PrefixListAssociationTypeDef",
    {
        "ResourceId": str,
        "ResourceOwner": str,
    },
    total=False,
)

PrefixListEntryTypeDef = TypedDict(
    "PrefixListEntryTypeDef",
    {
        "Cidr": str,
        "Description": str,
    },
    total=False,
)

PrefixListIdTypeDef = TypedDict(
    "PrefixListIdTypeDef",
    {
        "Description": str,
        "PrefixListId": str,
    },
    total=False,
)

PrefixListTypeDef = TypedDict(
    "PrefixListTypeDef",
    {
        "Cidrs": List[str],
        "PrefixListId": str,
        "PrefixListName": str,
    },
    total=False,
)

PriceScheduleSpecificationTypeDef = TypedDict(
    "PriceScheduleSpecificationTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Price": float,
        "Term": int,
    },
    total=False,
)

PriceScheduleTypeDef = TypedDict(
    "PriceScheduleTypeDef",
    {
        "Active": bool,
        "CurrencyCode": Literal["USD"],
        "Price": float,
        "Term": int,
    },
    total=False,
)

PricingDetailTypeDef = TypedDict(
    "PricingDetailTypeDef",
    {
        "Count": int,
        "Price": float,
    },
    total=False,
)

PrincipalIdFormatTypeDef = TypedDict(
    "PrincipalIdFormatTypeDef",
    {
        "Arn": str,
        "Statuses": List["IdFormatTypeDef"],
    },
    total=False,
)

PrivateDnsDetailsTypeDef = TypedDict(
    "PrivateDnsDetailsTypeDef",
    {
        "PrivateDnsName": str,
    },
    total=False,
)

PrivateDnsNameConfigurationTypeDef = TypedDict(
    "PrivateDnsNameConfigurationTypeDef",
    {
        "State": DnsNameStateType,
        "Type": str,
        "Value": str,
        "Name": str,
    },
    total=False,
)

PrivateIpAddressSpecificationTypeDef = TypedDict(
    "PrivateIpAddressSpecificationTypeDef",
    {
        "Primary": bool,
        "PrivateIpAddress": str,
    },
    total=False,
)

ProcessorInfoTypeDef = TypedDict(
    "ProcessorInfoTypeDef",
    {
        "SupportedArchitectures": List[ArchitectureTypeType],
        "SustainedClockSpeedInGhz": float,
    },
    total=False,
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "ProductCodeId": str,
        "ProductCodeType": ProductCodeValuesType,
    },
    total=False,
)

PropagatingVgwTypeDef = TypedDict(
    "PropagatingVgwTypeDef",
    {
        "GatewayId": str,
    },
    total=False,
)

_RequiredProvisionByoipCidrRequestTypeDef = TypedDict(
    "_RequiredProvisionByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalProvisionByoipCidrRequestTypeDef = TypedDict(
    "_OptionalProvisionByoipCidrRequestTypeDef",
    {
        "CidrAuthorizationContext": "CidrAuthorizationContextTypeDef",
        "PubliclyAdvertisable": bool,
        "Description": str,
        "DryRun": bool,
        "PoolTagSpecifications": List["TagSpecificationTypeDef"],
        "MultiRegion": bool,
    },
    total=False,
)


class ProvisionByoipCidrRequestTypeDef(
    _RequiredProvisionByoipCidrRequestTypeDef, _OptionalProvisionByoipCidrRequestTypeDef
):
    pass


ProvisionByoipCidrResultResponseTypeDef = TypedDict(
    "ProvisionByoipCidrResultResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedBandwidthTypeDef = TypedDict(
    "ProvisionedBandwidthTypeDef",
    {
        "ProvisionTime": datetime,
        "Provisioned": str,
        "RequestTime": datetime,
        "Requested": str,
        "Status": str,
    },
    total=False,
)

PtrUpdateStatusTypeDef = TypedDict(
    "PtrUpdateStatusTypeDef",
    {
        "Value": str,
        "Status": str,
        "Reason": str,
    },
    total=False,
)

PublicIpv4PoolRangeTypeDef = TypedDict(
    "PublicIpv4PoolRangeTypeDef",
    {
        "FirstAddress": str,
        "LastAddress": str,
        "AddressCount": int,
        "AvailableAddressCount": int,
    },
    total=False,
)

PublicIpv4PoolTypeDef = TypedDict(
    "PublicIpv4PoolTypeDef",
    {
        "PoolId": str,
        "Description": str,
        "PoolAddressRanges": List["PublicIpv4PoolRangeTypeDef"],
        "TotalAddressCount": int,
        "TotalAvailableAddressCount": int,
        "NetworkBorderGroup": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredPurchaseHostReservationRequestTypeDef = TypedDict(
    "_RequiredPurchaseHostReservationRequestTypeDef",
    {
        "HostIdSet": List[str],
        "OfferingId": str,
    },
)
_OptionalPurchaseHostReservationRequestTypeDef = TypedDict(
    "_OptionalPurchaseHostReservationRequestTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "LimitPrice": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class PurchaseHostReservationRequestTypeDef(
    _RequiredPurchaseHostReservationRequestTypeDef, _OptionalPurchaseHostReservationRequestTypeDef
):
    pass


PurchaseHostReservationResultResponseTypeDef = TypedDict(
    "PurchaseHostReservationResultResponseTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseRequestTypeDef = TypedDict(
    "PurchaseRequestTypeDef",
    {
        "InstanceCount": int,
        "PurchaseToken": str,
    },
)

_RequiredPurchaseReservedInstancesOfferingRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedInstancesOfferingRequestTypeDef",
    {
        "InstanceCount": int,
        "ReservedInstancesOfferingId": str,
    },
)
_OptionalPurchaseReservedInstancesOfferingRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedInstancesOfferingRequestTypeDef",
    {
        "DryRun": bool,
        "LimitPrice": "ReservedInstanceLimitPriceTypeDef",
        "PurchaseTime": Union[datetime, str],
    },
    total=False,
)


class PurchaseReservedInstancesOfferingRequestTypeDef(
    _RequiredPurchaseReservedInstancesOfferingRequestTypeDef,
    _OptionalPurchaseReservedInstancesOfferingRequestTypeDef,
):
    pass


PurchaseReservedInstancesOfferingResultResponseTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingResultResponseTypeDef",
    {
        "ReservedInstancesId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPurchaseScheduledInstancesRequestTypeDef = TypedDict(
    "_RequiredPurchaseScheduledInstancesRequestTypeDef",
    {
        "PurchaseRequests": List["PurchaseRequestTypeDef"],
    },
)
_OptionalPurchaseScheduledInstancesRequestTypeDef = TypedDict(
    "_OptionalPurchaseScheduledInstancesRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)


class PurchaseScheduledInstancesRequestTypeDef(
    _RequiredPurchaseScheduledInstancesRequestTypeDef,
    _OptionalPurchaseScheduledInstancesRequestTypeDef,
):
    pass


PurchaseScheduledInstancesResultResponseTypeDef = TypedDict(
    "PurchaseScheduledInstancesResultResponseTypeDef",
    {
        "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseTypeDef = TypedDict(
    "PurchaseTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "HostIdSet": List[str],
        "HostReservationId": str,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "PaymentOption": PaymentOptionType,
        "UpfrontPrice": str,
    },
    total=False,
)

RebootInstancesRequestInstanceTypeDef = TypedDict(
    "RebootInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredRebootInstancesRequestTypeDef = TypedDict(
    "_RequiredRebootInstancesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalRebootInstancesRequestTypeDef = TypedDict(
    "_OptionalRebootInstancesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RebootInstancesRequestTypeDef(
    _RequiredRebootInstancesRequestTypeDef, _OptionalRebootInstancesRequestTypeDef
):
    pass


RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "Amount": float,
        "Frequency": Literal["Hourly"],
    },
    total=False,
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "Endpoint": str,
        "RegionName": str,
        "OptInStatus": str,
    },
    total=False,
)

_RequiredRegisterImageRequestServiceResourceTypeDef = TypedDict(
    "_RequiredRegisterImageRequestServiceResourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalRegisterImageRequestServiceResourceTypeDef = TypedDict(
    "_OptionalRegisterImageRequestServiceResourceTypeDef",
    {
        "ImageLocation": str,
        "Architecture": ArchitectureValuesType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "EnaSupport": bool,
        "KernelId": str,
        "BillingProducts": List[str],
        "RamdiskId": str,
        "RootDeviceName": str,
        "SriovNetSupport": str,
        "VirtualizationType": str,
        "BootMode": BootModeValuesType,
    },
    total=False,
)


class RegisterImageRequestServiceResourceTypeDef(
    _RequiredRegisterImageRequestServiceResourceTypeDef,
    _OptionalRegisterImageRequestServiceResourceTypeDef,
):
    pass


_RequiredRegisterImageRequestTypeDef = TypedDict(
    "_RequiredRegisterImageRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalRegisterImageRequestTypeDef = TypedDict(
    "_OptionalRegisterImageRequestTypeDef",
    {
        "ImageLocation": str,
        "Architecture": ArchitectureValuesType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "EnaSupport": bool,
        "KernelId": str,
        "BillingProducts": List[str],
        "RamdiskId": str,
        "RootDeviceName": str,
        "SriovNetSupport": str,
        "VirtualizationType": str,
        "BootMode": BootModeValuesType,
    },
    total=False,
)


class RegisterImageRequestTypeDef(
    _RequiredRegisterImageRequestTypeDef, _OptionalRegisterImageRequestTypeDef
):
    pass


RegisterImageResultResponseTypeDef = TypedDict(
    "RegisterImageResultResponseTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterInstanceEventNotificationAttributesRequestTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesRequestTypeDef",
    {
        "DryRun": bool,
        "InstanceTagAttribute": "RegisterInstanceTagAttributeRequestTypeDef",
    },
    total=False,
)

RegisterInstanceEventNotificationAttributesResultResponseTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesResultResponseTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "RegisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": bool,
        "InstanceTagKeys": List[str],
    },
    total=False,
)

RegisterTransitGatewayMulticastGroupMembersRequestTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "GroupIpAddress": str,
        "NetworkInterfaceIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

RegisterTransitGatewayMulticastGroupMembersResultResponseTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersResultResponseTypeDef",
    {
        "RegisteredMulticastGroupMembers": "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTransitGatewayMulticastGroupSourcesRequestTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "GroupIpAddress": str,
        "NetworkInterfaceIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

RegisterTransitGatewayMulticastGroupSourcesResultResponseTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesResultResponseTypeDef",
    {
        "RegisteredMulticastGroupSources": "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectTransitGatewayMulticastDomainAssociationsRequestTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

RejectTransitGatewayMulticastDomainAssociationsResultResponseTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsResultResponseTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_RequiredRejectTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalRejectTransitGatewayPeeringAttachmentRequestTypeDef = TypedDict(
    "_OptionalRejectTransitGatewayPeeringAttachmentRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RejectTransitGatewayPeeringAttachmentRequestTypeDef(
    _RequiredRejectTransitGatewayPeeringAttachmentRequestTypeDef,
    _OptionalRejectTransitGatewayPeeringAttachmentRequestTypeDef,
):
    pass


RejectTransitGatewayPeeringAttachmentResultResponseTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentResultResponseTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_RequiredRejectTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalRejectTransitGatewayVpcAttachmentRequestTypeDef = TypedDict(
    "_OptionalRejectTransitGatewayVpcAttachmentRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RejectTransitGatewayVpcAttachmentRequestTypeDef(
    _RequiredRejectTransitGatewayVpcAttachmentRequestTypeDef,
    _OptionalRejectTransitGatewayVpcAttachmentRequestTypeDef,
):
    pass


RejectTransitGatewayVpcAttachmentResultResponseTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentResultResponseTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectVpcEndpointConnectionsRequestTypeDef = TypedDict(
    "_RequiredRejectVpcEndpointConnectionsRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": List[str],
    },
)
_OptionalRejectVpcEndpointConnectionsRequestTypeDef = TypedDict(
    "_OptionalRejectVpcEndpointConnectionsRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RejectVpcEndpointConnectionsRequestTypeDef(
    _RequiredRejectVpcEndpointConnectionsRequestTypeDef,
    _OptionalRejectVpcEndpointConnectionsRequestTypeDef,
):
    pass


RejectVpcEndpointConnectionsResultResponseTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsResultResponseTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectVpcPeeringConnectionRequestTypeDef = TypedDict(
    "_RequiredRejectVpcPeeringConnectionRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalRejectVpcPeeringConnectionRequestTypeDef = TypedDict(
    "_OptionalRejectVpcPeeringConnectionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RejectVpcPeeringConnectionRequestTypeDef(
    _RequiredRejectVpcPeeringConnectionRequestTypeDef,
    _OptionalRejectVpcPeeringConnectionRequestTypeDef,
):
    pass


RejectVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef = TypedDict(
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

RejectVpcPeeringConnectionResultResponseTypeDef = TypedDict(
    "RejectVpcPeeringConnectionResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReleaseAddressRequestClassicAddressTypeDef = TypedDict(
    "ReleaseAddressRequestClassicAddressTypeDef",
    {
        "AllocationId": str,
        "PublicIp": str,
        "NetworkBorderGroup": str,
        "DryRun": bool,
    },
    total=False,
)

ReleaseAddressRequestTypeDef = TypedDict(
    "ReleaseAddressRequestTypeDef",
    {
        "AllocationId": str,
        "PublicIp": str,
        "NetworkBorderGroup": str,
        "DryRun": bool,
    },
    total=False,
)

ReleaseAddressRequestVpcAddressTypeDef = TypedDict(
    "ReleaseAddressRequestVpcAddressTypeDef",
    {
        "AllocationId": str,
        "PublicIp": str,
        "NetworkBorderGroup": str,
        "DryRun": bool,
    },
    total=False,
)

ReleaseHostsRequestTypeDef = TypedDict(
    "ReleaseHostsRequestTypeDef",
    {
        "HostIds": List[str],
    },
)

ReleaseHostsResultResponseTypeDef = TypedDict(
    "ReleaseHostsResultResponseTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePrefixListEntryTypeDef = TypedDict(
    "RemovePrefixListEntryTypeDef",
    {
        "Cidr": str,
    },
)

ReplaceIamInstanceProfileAssociationRequestTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationRequestTypeDef",
    {
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "AssociationId": str,
    },
)

ReplaceIamInstanceProfileAssociationResultResponseTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationResultResponseTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceNetworkAclAssociationRequestNetworkAclTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclAssociationRequestNetworkAclTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalReplaceNetworkAclAssociationRequestNetworkAclTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclAssociationRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ReplaceNetworkAclAssociationRequestNetworkAclTypeDef(
    _RequiredReplaceNetworkAclAssociationRequestNetworkAclTypeDef,
    _OptionalReplaceNetworkAclAssociationRequestNetworkAclTypeDef,
):
    pass


_RequiredReplaceNetworkAclAssociationRequestTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclAssociationRequestTypeDef",
    {
        "AssociationId": str,
        "NetworkAclId": str,
    },
)
_OptionalReplaceNetworkAclAssociationRequestTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclAssociationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ReplaceNetworkAclAssociationRequestTypeDef(
    _RequiredReplaceNetworkAclAssociationRequestTypeDef,
    _OptionalReplaceNetworkAclAssociationRequestTypeDef,
):
    pass


ReplaceNetworkAclAssociationResultResponseTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationResultResponseTypeDef",
    {
        "NewAssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalReplaceNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)


class ReplaceNetworkAclEntryRequestNetworkAclTypeDef(
    _RequiredReplaceNetworkAclEntryRequestNetworkAclTypeDef,
    _OptionalReplaceNetworkAclEntryRequestNetworkAclTypeDef,
):
    pass


_RequiredReplaceNetworkAclEntryRequestTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclEntryRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalReplaceNetworkAclEntryRequestTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclEntryRequestTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)


class ReplaceNetworkAclEntryRequestTypeDef(
    _RequiredReplaceNetworkAclEntryRequestTypeDef, _OptionalReplaceNetworkAclEntryRequestTypeDef
):
    pass


ReplaceRootVolumeTaskTypeDef = TypedDict(
    "ReplaceRootVolumeTaskTypeDef",
    {
        "ReplaceRootVolumeTaskId": str,
        "InstanceId": str,
        "TaskState": ReplaceRootVolumeTaskStateType,
        "StartTime": str,
        "CompleteTime": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ReplaceRouteRequestRouteTypeDef = TypedDict(
    "ReplaceRouteRequestRouteTypeDef",
    {
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "LocalTarget": bool,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

_RequiredReplaceRouteRequestTypeDef = TypedDict(
    "_RequiredReplaceRouteRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalReplaceRouteRequestTypeDef = TypedDict(
    "_OptionalReplaceRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "LocalTarget": bool,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)


class ReplaceRouteRequestTypeDef(
    _RequiredReplaceRouteRequestTypeDef, _OptionalReplaceRouteRequestTypeDef
):
    pass


_RequiredReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef = TypedDict(
    "_RequiredReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef = TypedDict(
    "_OptionalReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef(
    _RequiredReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef,
    _OptionalReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef,
):
    pass


_RequiredReplaceRouteTableAssociationRequestTypeDef = TypedDict(
    "_RequiredReplaceRouteTableAssociationRequestTypeDef",
    {
        "AssociationId": str,
        "RouteTableId": str,
    },
)
_OptionalReplaceRouteTableAssociationRequestTypeDef = TypedDict(
    "_OptionalReplaceRouteTableAssociationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ReplaceRouteTableAssociationRequestTypeDef(
    _RequiredReplaceRouteTableAssociationRequestTypeDef,
    _OptionalReplaceRouteTableAssociationRequestTypeDef,
):
    pass


ReplaceRouteTableAssociationResultResponseTypeDef = TypedDict(
    "ReplaceRouteTableAssociationResultResponseTypeDef",
    {
        "NewAssociationId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceTransitGatewayRouteRequestTypeDef = TypedDict(
    "_RequiredReplaceTransitGatewayRouteRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalReplaceTransitGatewayRouteRequestTypeDef = TypedDict(
    "_OptionalReplaceTransitGatewayRouteRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)


class ReplaceTransitGatewayRouteRequestTypeDef(
    _RequiredReplaceTransitGatewayRouteRequestTypeDef,
    _OptionalReplaceTransitGatewayRouteRequestTypeDef,
):
    pass


ReplaceTransitGatewayRouteResultResponseTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteResultResponseTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReportInstanceStatusRequestInstanceTypeDef = TypedDict(
    "_RequiredReportInstanceStatusRequestInstanceTypeDef",
    {
        "ReasonCodes": List[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
    },
)
_OptionalReportInstanceStatusRequestInstanceTypeDef = TypedDict(
    "_OptionalReportInstanceStatusRequestInstanceTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
    },
    total=False,
)


class ReportInstanceStatusRequestInstanceTypeDef(
    _RequiredReportInstanceStatusRequestInstanceTypeDef,
    _OptionalReportInstanceStatusRequestInstanceTypeDef,
):
    pass


_RequiredReportInstanceStatusRequestTypeDef = TypedDict(
    "_RequiredReportInstanceStatusRequestTypeDef",
    {
        "Instances": List[str],
        "ReasonCodes": List[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
    },
)
_OptionalReportInstanceStatusRequestTypeDef = TypedDict(
    "_OptionalReportInstanceStatusRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
    },
    total=False,
)


class ReportInstanceStatusRequestTypeDef(
    _RequiredReportInstanceStatusRequestTypeDef, _OptionalReportInstanceStatusRequestTypeDef
):
    pass


RequestLaunchTemplateDataTypeDef = TypedDict(
    "RequestLaunchTemplateDataTypeDef",
    {
        "KernelId": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
        "BlockDeviceMappings": List["LaunchTemplateBlockDeviceMappingRequestTypeDef"],
        "NetworkInterfaces": List[
            "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef"
        ],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KeyName": str,
        "Monitoring": "LaunchTemplatesMonitoringRequestTypeDef",
        "Placement": "LaunchTemplatePlacementRequestTypeDef",
        "RamDiskId": str,
        "DisableApiTermination": bool,
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "UserData": str,
        "TagSpecifications": List["LaunchTemplateTagSpecificationRequestTypeDef"],
        "ElasticGpuSpecifications": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["LaunchTemplateElasticInferenceAcceleratorTypeDef"],
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "InstanceMarketOptions": "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "LaunchTemplateCpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
        "LicenseSpecifications": List["LaunchTemplateLicenseConfigurationRequestTypeDef"],
        "HibernationOptions": "LaunchTemplateHibernationOptionsRequestTypeDef",
        "MetadataOptions": "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "LaunchTemplateEnclaveOptionsRequestTypeDef",
    },
    total=False,
)

_RequiredRequestSpotFleetRequestTypeDef = TypedDict(
    "_RequiredRequestSpotFleetRequestTypeDef",
    {
        "SpotFleetRequestConfig": "SpotFleetRequestConfigDataTypeDef",
    },
)
_OptionalRequestSpotFleetRequestTypeDef = TypedDict(
    "_OptionalRequestSpotFleetRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RequestSpotFleetRequestTypeDef(
    _RequiredRequestSpotFleetRequestTypeDef, _OptionalRequestSpotFleetRequestTypeDef
):
    pass


RequestSpotFleetResponseResponseTypeDef = TypedDict(
    "RequestSpotFleetResponseResponseTypeDef",
    {
        "SpotFleetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestSpotInstancesRequestTypeDef = TypedDict(
    "RequestSpotInstancesRequestTypeDef",
    {
        "AvailabilityZoneGroup": str,
        "BlockDurationMinutes": int,
        "ClientToken": str,
        "DryRun": bool,
        "InstanceCount": int,
        "LaunchGroup": str,
        "LaunchSpecification": "RequestSpotLaunchSpecificationTypeDef",
        "SpotPrice": str,
        "Type": SpotInstanceTypeType,
        "ValidFrom": Union[datetime, str],
        "ValidUntil": Union[datetime, str],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

RequestSpotInstancesResultResponseTypeDef = TypedDict(
    "RequestSpotInstancesResultResponseTypeDef",
    {
        "SpotInstanceRequests": List["SpotInstanceRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestSpotLaunchSpecificationTypeDef = TypedDict(
    "RequestSpotLaunchSpecificationTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SubnetId": str,
        "UserData": str,
    },
    total=False,
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "OwnerId": str,
        "RequesterId": str,
        "ReservationId": str,
    },
    total=False,
)

ReservationValueTypeDef = TypedDict(
    "ReservationValueTypeDef",
    {
        "HourlyPrice": str,
        "RemainingTotalValue": str,
        "RemainingUpfrontValue": str,
    },
    total=False,
)

ReservedInstanceLimitPriceTypeDef = TypedDict(
    "ReservedInstanceLimitPriceTypeDef",
    {
        "Amount": float,
        "CurrencyCode": Literal["USD"],
    },
    total=False,
)

ReservedInstanceReservationValueTypeDef = TypedDict(
    "ReservedInstanceReservationValueTypeDef",
    {
        "ReservationValue": "ReservationValueTypeDef",
        "ReservedInstanceId": str,
    },
    total=False,
)

ReservedInstancesConfigurationTypeDef = TypedDict(
    "ReservedInstancesConfigurationTypeDef",
    {
        "AvailabilityZone": str,
        "InstanceCount": int,
        "InstanceType": InstanceTypeType,
        "Platform": str,
        "Scope": scopeType,
    },
    total=False,
)

ReservedInstancesIdTypeDef = TypedDict(
    "ReservedInstancesIdTypeDef",
    {
        "ReservedInstancesId": str,
    },
    total=False,
)

ReservedInstancesListingTypeDef = TypedDict(
    "ReservedInstancesListingTypeDef",
    {
        "ClientToken": str,
        "CreateDate": datetime,
        "InstanceCounts": List["InstanceCountTypeDef"],
        "PriceSchedules": List["PriceScheduleTypeDef"],
        "ReservedInstancesId": str,
        "ReservedInstancesListingId": str,
        "Status": ListingStatusType,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "UpdateDate": datetime,
    },
    total=False,
)

ReservedInstancesModificationResultTypeDef = TypedDict(
    "ReservedInstancesModificationResultTypeDef",
    {
        "ReservedInstancesId": str,
        "TargetConfiguration": "ReservedInstancesConfigurationTypeDef",
    },
    total=False,
)

ReservedInstancesModificationTypeDef = TypedDict(
    "ReservedInstancesModificationTypeDef",
    {
        "ClientToken": str,
        "CreateDate": datetime,
        "EffectiveDate": datetime,
        "ModificationResults": List["ReservedInstancesModificationResultTypeDef"],
        "ReservedInstancesIds": List["ReservedInstancesIdTypeDef"],
        "ReservedInstancesModificationId": str,
        "Status": str,
        "StatusMessage": str,
        "UpdateDate": datetime,
    },
    total=False,
)

ReservedInstancesOfferingTypeDef = TypedDict(
    "ReservedInstancesOfferingTypeDef",
    {
        "AvailabilityZone": str,
        "Duration": int,
        "FixedPrice": float,
        "InstanceType": InstanceTypeType,
        "ProductDescription": RIProductDescriptionType,
        "ReservedInstancesOfferingId": str,
        "UsagePrice": float,
        "CurrencyCode": Literal["USD"],
        "InstanceTenancy": TenancyType,
        "Marketplace": bool,
        "OfferingClass": OfferingClassTypeType,
        "OfferingType": OfferingTypeValuesType,
        "PricingDetails": List["PricingDetailTypeDef"],
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "Scope": scopeType,
    },
    total=False,
)

ReservedInstancesTypeDef = TypedDict(
    "ReservedInstancesTypeDef",
    {
        "AvailabilityZone": str,
        "Duration": int,
        "End": datetime,
        "FixedPrice": float,
        "InstanceCount": int,
        "InstanceType": InstanceTypeType,
        "ProductDescription": RIProductDescriptionType,
        "ReservedInstancesId": str,
        "Start": datetime,
        "State": ReservedInstanceStateType,
        "UsagePrice": float,
        "CurrencyCode": Literal["USD"],
        "InstanceTenancy": TenancyType,
        "OfferingClass": OfferingClassTypeType,
        "OfferingType": OfferingTypeValuesType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "Scope": scopeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredResetAddressAttributeRequestTypeDef = TypedDict(
    "_RequiredResetAddressAttributeRequestTypeDef",
    {
        "AllocationId": str,
        "Attribute": Literal["domain-name"],
    },
)
_OptionalResetAddressAttributeRequestTypeDef = TypedDict(
    "_OptionalResetAddressAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetAddressAttributeRequestTypeDef(
    _RequiredResetAddressAttributeRequestTypeDef, _OptionalResetAddressAttributeRequestTypeDef
):
    pass


ResetAddressAttributeResultResponseTypeDef = TypedDict(
    "ResetAddressAttributeResultResponseTypeDef",
    {
        "Address": "AddressAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetEbsDefaultKmsKeyIdRequestTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

ResetEbsDefaultKmsKeyIdResultResponseTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdResultResponseTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetFpgaImageAttributeRequestTypeDef = TypedDict(
    "_RequiredResetFpgaImageAttributeRequestTypeDef",
    {
        "FpgaImageId": str,
    },
)
_OptionalResetFpgaImageAttributeRequestTypeDef = TypedDict(
    "_OptionalResetFpgaImageAttributeRequestTypeDef",
    {
        "DryRun": bool,
        "Attribute": Literal["loadPermission"],
    },
    total=False,
)


class ResetFpgaImageAttributeRequestTypeDef(
    _RequiredResetFpgaImageAttributeRequestTypeDef, _OptionalResetFpgaImageAttributeRequestTypeDef
):
    pass


ResetFpgaImageAttributeResultResponseTypeDef = TypedDict(
    "ResetFpgaImageAttributeResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetImageAttributeRequestImageTypeDef = TypedDict(
    "_RequiredResetImageAttributeRequestImageTypeDef",
    {
        "Attribute": Literal["launchPermission"],
    },
)
_OptionalResetImageAttributeRequestImageTypeDef = TypedDict(
    "_OptionalResetImageAttributeRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetImageAttributeRequestImageTypeDef(
    _RequiredResetImageAttributeRequestImageTypeDef, _OptionalResetImageAttributeRequestImageTypeDef
):
    pass


_RequiredResetImageAttributeRequestTypeDef = TypedDict(
    "_RequiredResetImageAttributeRequestTypeDef",
    {
        "Attribute": Literal["launchPermission"],
        "ImageId": str,
    },
)
_OptionalResetImageAttributeRequestTypeDef = TypedDict(
    "_OptionalResetImageAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetImageAttributeRequestTypeDef(
    _RequiredResetImageAttributeRequestTypeDef, _OptionalResetImageAttributeRequestTypeDef
):
    pass


_RequiredResetInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_RequiredResetInstanceAttributeRequestInstanceTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
    },
)
_OptionalResetInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_OptionalResetInstanceAttributeRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetInstanceAttributeRequestInstanceTypeDef(
    _RequiredResetInstanceAttributeRequestInstanceTypeDef,
    _OptionalResetInstanceAttributeRequestInstanceTypeDef,
):
    pass


_RequiredResetInstanceAttributeRequestTypeDef = TypedDict(
    "_RequiredResetInstanceAttributeRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
    },
)
_OptionalResetInstanceAttributeRequestTypeDef = TypedDict(
    "_OptionalResetInstanceAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetInstanceAttributeRequestTypeDef(
    _RequiredResetInstanceAttributeRequestTypeDef, _OptionalResetInstanceAttributeRequestTypeDef
):
    pass


ResetNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef = TypedDict(
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
        "SourceDestCheck": str,
    },
    total=False,
)

_RequiredResetNetworkInterfaceAttributeRequestTypeDef = TypedDict(
    "_RequiredResetNetworkInterfaceAttributeRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalResetNetworkInterfaceAttributeRequestTypeDef = TypedDict(
    "_OptionalResetNetworkInterfaceAttributeRequestTypeDef",
    {
        "DryRun": bool,
        "SourceDestCheck": str,
    },
    total=False,
)


class ResetNetworkInterfaceAttributeRequestTypeDef(
    _RequiredResetNetworkInterfaceAttributeRequestTypeDef,
    _OptionalResetNetworkInterfaceAttributeRequestTypeDef,
):
    pass


_RequiredResetSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_RequiredResetSnapshotAttributeRequestSnapshotTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
    },
)
_OptionalResetSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_OptionalResetSnapshotAttributeRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetSnapshotAttributeRequestSnapshotTypeDef(
    _RequiredResetSnapshotAttributeRequestSnapshotTypeDef,
    _OptionalResetSnapshotAttributeRequestSnapshotTypeDef,
):
    pass


_RequiredResetSnapshotAttributeRequestTypeDef = TypedDict(
    "_RequiredResetSnapshotAttributeRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
    },
)
_OptionalResetSnapshotAttributeRequestTypeDef = TypedDict(
    "_OptionalResetSnapshotAttributeRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class ResetSnapshotAttributeRequestTypeDef(
    _RequiredResetSnapshotAttributeRequestTypeDef, _OptionalResetSnapshotAttributeRequestTypeDef
):
    pass


ResponseErrorTypeDef = TypedDict(
    "ResponseErrorTypeDef",
    {
        "Code": LaunchTemplateErrorCodeType,
        "Message": str,
    },
    total=False,
)

ResponseLaunchTemplateDataTypeDef = TypedDict(
    "ResponseLaunchTemplateDataTypeDef",
    {
        "KernelId": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
        "BlockDeviceMappings": List["LaunchTemplateBlockDeviceMappingTypeDef"],
        "NetworkInterfaces": List["LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KeyName": str,
        "Monitoring": "LaunchTemplatesMonitoringTypeDef",
        "Placement": "LaunchTemplatePlacementTypeDef",
        "RamDiskId": str,
        "DisableApiTermination": bool,
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "UserData": str,
        "TagSpecifications": List["LaunchTemplateTagSpecificationTypeDef"],
        "ElasticGpuSpecifications": List["ElasticGpuSpecificationResponseTypeDef"],
        "ElasticInferenceAccelerators": List[
            "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef"
        ],
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "InstanceMarketOptions": "LaunchTemplateInstanceMarketOptionsTypeDef",
        "CreditSpecification": "CreditSpecificationTypeDef",
        "CpuOptions": "LaunchTemplateCpuOptionsTypeDef",
        "CapacityReservationSpecification": "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
        "LicenseSpecifications": List["LaunchTemplateLicenseConfigurationTypeDef"],
        "HibernationOptions": "LaunchTemplateHibernationOptionsTypeDef",
        "MetadataOptions": "LaunchTemplateInstanceMetadataOptionsTypeDef",
        "EnclaveOptions": "LaunchTemplateEnclaveOptionsTypeDef",
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

_RequiredRestoreAddressToClassicRequestTypeDef = TypedDict(
    "_RequiredRestoreAddressToClassicRequestTypeDef",
    {
        "PublicIp": str,
    },
)
_OptionalRestoreAddressToClassicRequestTypeDef = TypedDict(
    "_OptionalRestoreAddressToClassicRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RestoreAddressToClassicRequestTypeDef(
    _RequiredRestoreAddressToClassicRequestTypeDef, _OptionalRestoreAddressToClassicRequestTypeDef
):
    pass


RestoreAddressToClassicResultResponseTypeDef = TypedDict(
    "RestoreAddressToClassicResultResponseTypeDef",
    {
        "PublicIp": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreManagedPrefixListVersionRequestTypeDef = TypedDict(
    "_RequiredRestoreManagedPrefixListVersionRequestTypeDef",
    {
        "PrefixListId": str,
        "PreviousVersion": int,
        "CurrentVersion": int,
    },
)
_OptionalRestoreManagedPrefixListVersionRequestTypeDef = TypedDict(
    "_OptionalRestoreManagedPrefixListVersionRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class RestoreManagedPrefixListVersionRequestTypeDef(
    _RequiredRestoreManagedPrefixListVersionRequestTypeDef,
    _OptionalRestoreManagedPrefixListVersionRequestTypeDef,
):
    pass


RestoreManagedPrefixListVersionResultResponseTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionResultResponseTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRevokeClientVpnIngressRequestTypeDef = TypedDict(
    "_RequiredRevokeClientVpnIngressRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
    },
)
_OptionalRevokeClientVpnIngressRequestTypeDef = TypedDict(
    "_OptionalRevokeClientVpnIngressRequestTypeDef",
    {
        "AccessGroupId": str,
        "RevokeAllGroups": bool,
        "DryRun": bool,
    },
    total=False,
)


class RevokeClientVpnIngressRequestTypeDef(
    _RequiredRevokeClientVpnIngressRequestTypeDef, _OptionalRevokeClientVpnIngressRequestTypeDef
):
    pass


RevokeClientVpnIngressResultResponseTypeDef = TypedDict(
    "RevokeClientVpnIngressResultResponseTypeDef",
    {
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeSecurityGroupEgressRequestSecurityGroupTypeDef = TypedDict(
    "RevokeSecurityGroupEgressRequestSecurityGroupTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)

_RequiredRevokeSecurityGroupEgressRequestTypeDef = TypedDict(
    "_RequiredRevokeSecurityGroupEgressRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalRevokeSecurityGroupEgressRequestTypeDef = TypedDict(
    "_OptionalRevokeSecurityGroupEgressRequestTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)


class RevokeSecurityGroupEgressRequestTypeDef(
    _RequiredRevokeSecurityGroupEgressRequestTypeDef,
    _OptionalRevokeSecurityGroupEgressRequestTypeDef,
):
    pass


RevokeSecurityGroupEgressResultResponseTypeDef = TypedDict(
    "RevokeSecurityGroupEgressResultResponseTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List["IpPermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeSecurityGroupIngressRequestSecurityGroupTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestSecurityGroupTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
    },
    total=False,
)

RevokeSecurityGroupIngressRequestTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupId": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
    },
    total=False,
)

RevokeSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "RevokeSecurityGroupIngressResultResponseTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List["IpPermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RouteTableAssociationStateTypeDef = TypedDict(
    "RouteTableAssociationStateTypeDef",
    {
        "State": RouteTableAssociationStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

RouteTableAssociationTypeDef = TypedDict(
    "RouteTableAssociationTypeDef",
    {
        "Main": bool,
        "RouteTableAssociationId": str,
        "RouteTableId": str,
        "SubnetId": str,
        "GatewayId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
    },
    total=False,
)

RouteTableTypeDef = TypedDict(
    "RouteTableTypeDef",
    {
        "Associations": List["RouteTableAssociationTypeDef"],
        "PropagatingVgws": List["PropagatingVgwTypeDef"],
        "RouteTableId": str,
        "Routes": List["RouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VpcId": str,
        "OwnerId": str,
    },
    total=False,
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": RouteOriginType,
        "State": RouteStateType,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

RunInstancesMonitoringEnabledTypeDef = TypedDict(
    "RunInstancesMonitoringEnabledTypeDef",
    {
        "Enabled": bool,
    },
)

_RequiredRunInstancesRequestServiceResourceTypeDef = TypedDict(
    "_RequiredRunInstancesRequestServiceResourceTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
    },
)
_OptionalRunInstancesRequestServiceResourceTypeDef = TypedDict(
    "_OptionalRunInstancesRequestServiceResourceTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "Placement": "PlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "SubnetId": str,
        "UserData": str,
        "AdditionalInfo": str,
        "ClientToken": str,
        "DisableApiTermination": bool,
        "DryRun": bool,
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "PrivateIpAddress": str,
        "ElasticGpuSpecification": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["ElasticInferenceAcceleratorTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceMarketOptions": "InstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "CpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "HibernationOptions": "HibernationOptionsRequestTypeDef",
        "LicenseSpecifications": List["LicenseConfigurationRequestTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "EnclaveOptionsRequestTypeDef",
    },
    total=False,
)


class RunInstancesRequestServiceResourceTypeDef(
    _RequiredRunInstancesRequestServiceResourceTypeDef,
    _OptionalRunInstancesRequestServiceResourceTypeDef,
):
    pass


_RequiredRunInstancesRequestSubnetTypeDef = TypedDict(
    "_RequiredRunInstancesRequestSubnetTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
    },
)
_OptionalRunInstancesRequestSubnetTypeDef = TypedDict(
    "_OptionalRunInstancesRequestSubnetTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "Placement": "PlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "UserData": str,
        "AdditionalInfo": str,
        "ClientToken": str,
        "DisableApiTermination": bool,
        "DryRun": bool,
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "PrivateIpAddress": str,
        "ElasticGpuSpecification": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["ElasticInferenceAcceleratorTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceMarketOptions": "InstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "CpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "HibernationOptions": "HibernationOptionsRequestTypeDef",
        "LicenseSpecifications": List["LicenseConfigurationRequestTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "EnclaveOptionsRequestTypeDef",
    },
    total=False,
)


class RunInstancesRequestSubnetTypeDef(
    _RequiredRunInstancesRequestSubnetTypeDef, _OptionalRunInstancesRequestSubnetTypeDef
):
    pass


_RequiredRunInstancesRequestTypeDef = TypedDict(
    "_RequiredRunInstancesRequestTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
    },
)
_OptionalRunInstancesRequestTypeDef = TypedDict(
    "_OptionalRunInstancesRequestTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "Placement": "PlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "SubnetId": str,
        "UserData": str,
        "AdditionalInfo": str,
        "ClientToken": str,
        "DisableApiTermination": bool,
        "DryRun": bool,
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "PrivateIpAddress": str,
        "ElasticGpuSpecification": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["ElasticInferenceAcceleratorTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceMarketOptions": "InstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "CpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "HibernationOptions": "HibernationOptionsRequestTypeDef",
        "LicenseSpecifications": List["LicenseConfigurationRequestTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "EnclaveOptionsRequestTypeDef",
    },
    total=False,
)


class RunInstancesRequestTypeDef(
    _RequiredRunInstancesRequestTypeDef, _OptionalRunInstancesRequestTypeDef
):
    pass


_RequiredRunScheduledInstancesRequestTypeDef = TypedDict(
    "_RequiredRunScheduledInstancesRequestTypeDef",
    {
        "LaunchSpecification": "ScheduledInstancesLaunchSpecificationTypeDef",
        "ScheduledInstanceId": str,
    },
)
_OptionalRunScheduledInstancesRequestTypeDef = TypedDict(
    "_OptionalRunScheduledInstancesRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
        "InstanceCount": int,
    },
    total=False,
)


class RunScheduledInstancesRequestTypeDef(
    _RequiredRunScheduledInstancesRequestTypeDef, _OptionalRunScheduledInstancesRequestTypeDef
):
    pass


RunScheduledInstancesResultResponseTypeDef = TypedDict(
    "RunScheduledInstancesResultResponseTypeDef",
    {
        "InstanceIdSet": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ObjectTagTypeDef = TypedDict(
    "S3ObjectTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

S3StorageTypeDef = TypedDict(
    "S3StorageTypeDef",
    {
        "AWSAccessKeyId": str,
        "Bucket": str,
        "Prefix": str,
        "UploadPolicy": Union[bytes, IO[bytes], StreamingBody],
        "UploadPolicySignature": str,
    },
    total=False,
)

ScheduledInstanceAvailabilityTypeDef = TypedDict(
    "ScheduledInstanceAvailabilityTypeDef",
    {
        "AvailabilityZone": str,
        "AvailableInstanceCount": int,
        "FirstSlotStartTime": datetime,
        "HourlyPrice": str,
        "InstanceType": str,
        "MaxTermDurationInDays": int,
        "MinTermDurationInDays": int,
        "NetworkPlatform": str,
        "Platform": str,
        "PurchaseToken": str,
        "Recurrence": "ScheduledInstanceRecurrenceTypeDef",
        "SlotDurationInHours": int,
        "TotalScheduledInstanceHours": int,
    },
    total=False,
)

ScheduledInstanceRecurrenceRequestTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceRequestTypeDef",
    {
        "Frequency": str,
        "Interval": int,
        "OccurrenceDays": List[int],
        "OccurrenceRelativeToEnd": bool,
        "OccurrenceUnit": str,
    },
    total=False,
)

ScheduledInstanceRecurrenceTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceTypeDef",
    {
        "Frequency": str,
        "Interval": int,
        "OccurrenceDaySet": List[int],
        "OccurrenceRelativeToEnd": bool,
        "OccurrenceUnit": str,
    },
    total=False,
)

ScheduledInstanceTypeDef = TypedDict(
    "ScheduledInstanceTypeDef",
    {
        "AvailabilityZone": str,
        "CreateDate": datetime,
        "HourlyPrice": str,
        "InstanceCount": int,
        "InstanceType": str,
        "NetworkPlatform": str,
        "NextSlotStartTime": datetime,
        "Platform": str,
        "PreviousSlotEndTime": datetime,
        "Recurrence": "ScheduledInstanceRecurrenceTypeDef",
        "ScheduledInstanceId": str,
        "SlotDurationInHours": int,
        "TermEndDate": datetime,
        "TermStartDate": datetime,
        "TotalScheduledInstanceHours": int,
    },
    total=False,
)

ScheduledInstancesBlockDeviceMappingTypeDef = TypedDict(
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "Ebs": "ScheduledInstancesEbsTypeDef",
        "NoDevice": str,
        "VirtualName": str,
    },
    total=False,
)

ScheduledInstancesEbsTypeDef = TypedDict(
    "ScheduledInstancesEbsTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
    },
    total=False,
)

ScheduledInstancesIamInstanceProfileTypeDef = TypedDict(
    "ScheduledInstancesIamInstanceProfileTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

ScheduledInstancesIpv6AddressTypeDef = TypedDict(
    "ScheduledInstancesIpv6AddressTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

_RequiredScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "_RequiredScheduledInstancesLaunchSpecificationTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "_OptionalScheduledInstancesLaunchSpecificationTypeDef",
    {
        "BlockDeviceMappings": List["ScheduledInstancesBlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "ScheduledInstancesIamInstanceProfileTypeDef",
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "ScheduledInstancesMonitoringTypeDef",
        "NetworkInterfaces": List["ScheduledInstancesNetworkInterfaceTypeDef"],
        "Placement": "ScheduledInstancesPlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "UserData": str,
    },
    total=False,
)


class ScheduledInstancesLaunchSpecificationTypeDef(
    _RequiredScheduledInstancesLaunchSpecificationTypeDef,
    _OptionalScheduledInstancesLaunchSpecificationTypeDef,
):
    pass


ScheduledInstancesMonitoringTypeDef = TypedDict(
    "ScheduledInstancesMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ScheduledInstancesNetworkInterfaceTypeDef = TypedDict(
    "ScheduledInstancesNetworkInterfaceTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["ScheduledInstancesIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddressConfigs": List["ScheduledInstancesPrivateIpAddressConfigTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
    total=False,
)

ScheduledInstancesPlacementTypeDef = TypedDict(
    "ScheduledInstancesPlacementTypeDef",
    {
        "AvailabilityZone": str,
        "GroupName": str,
    },
    total=False,
)

ScheduledInstancesPrivateIpAddressConfigTypeDef = TypedDict(
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    {
        "Primary": bool,
        "PrivateIpAddress": str,
    },
    total=False,
)

_RequiredSearchLocalGatewayRoutesRequestTypeDef = TypedDict(
    "_RequiredSearchLocalGatewayRoutesRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "Filters": List["FilterTypeDef"],
    },
)
_OptionalSearchLocalGatewayRoutesRequestTypeDef = TypedDict(
    "_OptionalSearchLocalGatewayRoutesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)


class SearchLocalGatewayRoutesRequestTypeDef(
    _RequiredSearchLocalGatewayRoutesRequestTypeDef, _OptionalSearchLocalGatewayRoutesRequestTypeDef
):
    pass


SearchLocalGatewayRoutesResultResponseTypeDef = TypedDict(
    "SearchLocalGatewayRoutesResultResponseTypeDef",
    {
        "Routes": List["LocalGatewayRouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchTransitGatewayMulticastGroupsRequestTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

SearchTransitGatewayMulticastGroupsResultResponseTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsResultResponseTypeDef",
    {
        "MulticastGroups": List["TransitGatewayMulticastGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchTransitGatewayRoutesRequestTypeDef = TypedDict(
    "_RequiredSearchTransitGatewayRoutesRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": List["FilterTypeDef"],
    },
)
_OptionalSearchTransitGatewayRoutesRequestTypeDef = TypedDict(
    "_OptionalSearchTransitGatewayRoutesRequestTypeDef",
    {
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)


class SearchTransitGatewayRoutesRequestTypeDef(
    _RequiredSearchTransitGatewayRoutesRequestTypeDef,
    _OptionalSearchTransitGatewayRoutesRequestTypeDef,
):
    pass


SearchTransitGatewayRoutesResultResponseTypeDef = TypedDict(
    "SearchTransitGatewayRoutesResultResponseTypeDef",
    {
        "Routes": List["TransitGatewayRouteTypeDef"],
        "AdditionalRoutesAvailable": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
    },
    total=False,
)

SecurityGroupReferenceTypeDef = TypedDict(
    "SecurityGroupReferenceTypeDef",
    {
        "GroupId": str,
        "ReferencingVpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "OwnerId": str,
        "GroupId": str,
        "IpPermissionsEgress": List["IpPermissionTypeDef"],
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

_RequiredSendDiagnosticInterruptRequestTypeDef = TypedDict(
    "_RequiredSendDiagnosticInterruptRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSendDiagnosticInterruptRequestTypeDef = TypedDict(
    "_OptionalSendDiagnosticInterruptRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class SendDiagnosticInterruptRequestTypeDef(
    _RequiredSendDiagnosticInterruptRequestTypeDef, _OptionalSendDiagnosticInterruptRequestTypeDef
):
    pass


ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "ServiceType": List["ServiceTypeDetailTypeDef"],
        "ServiceId": str,
        "ServiceName": str,
        "ServiceState": ServiceStateType,
        "AvailabilityZones": List[str],
        "AcceptanceRequired": bool,
        "ManagesVpcEndpoints": bool,
        "NetworkLoadBalancerArns": List[str],
        "GatewayLoadBalancerArns": List[str],
        "BaseEndpointDnsNames": List[str],
        "PrivateDnsName": str,
        "PrivateDnsNameConfiguration": "PrivateDnsNameConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ServiceDetailTypeDef = TypedDict(
    "ServiceDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceType": List["ServiceTypeDetailTypeDef"],
        "AvailabilityZones": List[str],
        "Owner": str,
        "BaseEndpointDnsNames": List[str],
        "PrivateDnsName": str,
        "PrivateDnsNames": List["PrivateDnsDetailsTypeDef"],
        "VpcEndpointPolicySupported": bool,
        "AcceptanceRequired": bool,
        "ManagesVpcEndpoints": bool,
        "Tags": List["TagTypeDef"],
        "PrivateDnsNameVerificationState": DnsNameStateType,
    },
    total=False,
)

ServiceResourceClassicAddressRequestTypeDef = TypedDict(
    "ServiceResourceClassicAddressRequestTypeDef",
    {
        "public_ip": str,
    },
)

ServiceResourceDhcpOptionsRequestTypeDef = TypedDict(
    "ServiceResourceDhcpOptionsRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceImageRequestTypeDef = TypedDict(
    "ServiceResourceImageRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceInstanceRequestTypeDef = TypedDict(
    "ServiceResourceInstanceRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceInternetGatewayRequestTypeDef = TypedDict(
    "ServiceResourceInternetGatewayRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceKeyPairRequestTypeDef = TypedDict(
    "ServiceResourceKeyPairRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceNetworkAclRequestTypeDef = TypedDict(
    "ServiceResourceNetworkAclRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceNetworkInterfaceAssociationRequestTypeDef = TypedDict(
    "ServiceResourceNetworkInterfaceAssociationRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceNetworkInterfaceRequestTypeDef = TypedDict(
    "ServiceResourceNetworkInterfaceRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourcePlacementGroupRequestTypeDef = TypedDict(
    "ServiceResourcePlacementGroupRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceRouteRequestTypeDef = TypedDict(
    "ServiceResourceRouteRequestTypeDef",
    {
        "route_table_id": str,
        "destination_cidr_block": str,
    },
)

ServiceResourceRouteTableAssociationRequestTypeDef = TypedDict(
    "ServiceResourceRouteTableAssociationRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceRouteTableRequestTypeDef = TypedDict(
    "ServiceResourceRouteTableRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSecurityGroupRequestTypeDef = TypedDict(
    "ServiceResourceSecurityGroupRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSnapshotRequestTypeDef = TypedDict(
    "ServiceResourceSnapshotRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSubnetRequestTypeDef = TypedDict(
    "ServiceResourceSubnetRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceTagRequestTypeDef = TypedDict(
    "ServiceResourceTagRequestTypeDef",
    {
        "resource_id": str,
        "key": str,
        "value": str,
    },
)

ServiceResourceVolumeRequestTypeDef = TypedDict(
    "ServiceResourceVolumeRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceVpcAddressRequestTypeDef = TypedDict(
    "ServiceResourceVpcAddressRequestTypeDef",
    {
        "allocation_id": str,
    },
)

ServiceResourceVpcPeeringConnectionRequestTypeDef = TypedDict(
    "ServiceResourceVpcPeeringConnectionRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceVpcRequestTypeDef = TypedDict(
    "ServiceResourceVpcRequestTypeDef",
    {
        "id": str,
    },
)

ServiceTypeDetailTypeDef = TypedDict(
    "ServiceTypeDetailTypeDef",
    {
        "ServiceType": ServiceTypeType,
    },
    total=False,
)

SlotDateTimeRangeRequestTypeDef = TypedDict(
    "SlotDateTimeRangeRequestTypeDef",
    {
        "EarliestTime": Union[datetime, str],
        "LatestTime": Union[datetime, str],
    },
)

SlotStartTimeRangeRequestTypeDef = TypedDict(
    "SlotStartTimeRangeRequestTypeDef",
    {
        "EarliestTime": Union[datetime, str],
        "LatestTime": Union[datetime, str],
    },
    total=False,
)

SnapshotDetailTypeDef = TypedDict(
    "SnapshotDetailTypeDef",
    {
        "Description": str,
        "DeviceName": str,
        "DiskImageSize": float,
        "Format": str,
        "Progress": str,
        "SnapshotId": str,
        "Status": str,
        "StatusMessage": str,
        "Url": str,
        "UserBucket": "UserBucketDetailsTypeDef",
    },
    total=False,
)

SnapshotDiskContainerTypeDef = TypedDict(
    "SnapshotDiskContainerTypeDef",
    {
        "Description": str,
        "Format": str,
        "Url": str,
        "UserBucket": "UserBucketTypeDef",
    },
    total=False,
)

SnapshotInfoTypeDef = TypedDict(
    "SnapshotInfoTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "Encrypted": bool,
        "VolumeId": str,
        "State": SnapshotStateType,
        "VolumeSize": int,
        "StartTime": datetime,
        "Progress": str,
        "OwnerId": str,
        "SnapshotId": str,
        "OutpostArn": str,
    },
    total=False,
)

SnapshotResponseTypeDef = TypedDict(
    "SnapshotResponseTypeDef",
    {
        "DataEncryptionKeyId": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OwnerId": str,
        "Progress": str,
        "SnapshotId": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "StateMessage": str,
        "VolumeId": str,
        "VolumeSize": int,
        "OwnerAlias": str,
        "OutpostArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotTaskDetailTypeDef = TypedDict(
    "SnapshotTaskDetailTypeDef",
    {
        "Description": str,
        "DiskImageSize": float,
        "Encrypted": bool,
        "Format": str,
        "KmsKeyId": str,
        "Progress": str,
        "SnapshotId": str,
        "Status": str,
        "StatusMessage": str,
        "Url": str,
        "UserBucket": "UserBucketDetailsTypeDef",
    },
    total=False,
)

SpotCapacityRebalanceTypeDef = TypedDict(
    "SpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": Literal["launch"],
    },
    total=False,
)

SpotDatafeedSubscriptionTypeDef = TypedDict(
    "SpotDatafeedSubscriptionTypeDef",
    {
        "Bucket": str,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "OwnerId": str,
        "Prefix": str,
        "State": DatafeedSubscriptionStateType,
    },
    total=False,
)

SpotFleetLaunchSpecificationTypeDef = TypedDict(
    "SpotFleetLaunchSpecificationTypeDef",
    {
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "SpotFleetMonitoringTypeDef",
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SpotPrice": str,
        "SubnetId": str,
        "UserData": str,
        "WeightedCapacity": float,
        "TagSpecifications": List["SpotFleetTagSpecificationTypeDef"],
    },
    total=False,
)

SpotFleetMonitoringTypeDef = TypedDict(
    "SpotFleetMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_RequiredSpotFleetRequestConfigDataTypeDef",
    {
        "IamFleetRole": str,
        "TargetCapacity": int,
    },
)
_OptionalSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_OptionalSpotFleetRequestConfigDataTypeDef",
    {
        "AllocationStrategy": AllocationStrategyType,
        "OnDemandAllocationStrategy": OnDemandAllocationStrategyType,
        "SpotMaintenanceStrategies": "SpotMaintenanceStrategiesTypeDef",
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": ExcessCapacityTerminationPolicyType,
        "FulfilledCapacity": float,
        "OnDemandFulfilledCapacity": float,
        "LaunchSpecifications": List["SpotFleetLaunchSpecificationTypeDef"],
        "LaunchTemplateConfigs": List["LaunchTemplateConfigTypeDef"],
        "SpotPrice": str,
        "OnDemandTargetCapacity": int,
        "OnDemandMaxTotalPrice": str,
        "SpotMaxTotalPrice": str,
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetTypeType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
        "LoadBalancersConfig": "LoadBalancersConfigTypeDef",
        "InstancePoolsToUseCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class SpotFleetRequestConfigDataTypeDef(
    _RequiredSpotFleetRequestConfigDataTypeDef, _OptionalSpotFleetRequestConfigDataTypeDef
):
    pass


SpotFleetRequestConfigTypeDef = TypedDict(
    "SpotFleetRequestConfigTypeDef",
    {
        "ActivityStatus": ActivityStatusType,
        "CreateTime": datetime,
        "SpotFleetRequestConfig": "SpotFleetRequestConfigDataTypeDef",
        "SpotFleetRequestId": str,
        "SpotFleetRequestState": BatchStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotFleetTagSpecificationTypeDef = TypedDict(
    "SpotFleetTagSpecificationTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotInstanceRequestTypeDef = TypedDict(
    "SpotInstanceRequestTypeDef",
    {
        "ActualBlockHourlyPrice": str,
        "AvailabilityZoneGroup": str,
        "BlockDurationMinutes": int,
        "CreateTime": datetime,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "InstanceId": str,
        "LaunchGroup": str,
        "LaunchSpecification": "LaunchSpecificationTypeDef",
        "LaunchedAvailabilityZone": str,
        "ProductDescription": RIProductDescriptionType,
        "SpotInstanceRequestId": str,
        "SpotPrice": str,
        "State": SpotInstanceStateType,
        "Status": "SpotInstanceStatusTypeDef",
        "Tags": List["TagTypeDef"],
        "Type": SpotInstanceTypeType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

SpotInstanceStateFaultTypeDef = TypedDict(
    "SpotInstanceStateFaultTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

SpotInstanceStatusTypeDef = TypedDict(
    "SpotInstanceStatusTypeDef",
    {
        "Code": str,
        "Message": str,
        "UpdateTime": datetime,
    },
    total=False,
)

SpotMaintenanceStrategiesTypeDef = TypedDict(
    "SpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": "SpotCapacityRebalanceTypeDef",
    },
    total=False,
)

SpotMarketOptionsTypeDef = TypedDict(
    "SpotMarketOptionsTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": SpotInstanceTypeType,
        "BlockDurationMinutes": int,
        "ValidUntil": Union[datetime, str],
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

SpotOptionsRequestTypeDef = TypedDict(
    "SpotOptionsRequestTypeDef",
    {
        "AllocationStrategy": SpotAllocationStrategyType,
        "MaintenanceStrategies": "FleetSpotMaintenanceStrategiesRequestTypeDef",
        "InstanceInterruptionBehavior": SpotInstanceInterruptionBehaviorType,
        "InstancePoolsToUseCount": int,
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

SpotOptionsTypeDef = TypedDict(
    "SpotOptionsTypeDef",
    {
        "AllocationStrategy": SpotAllocationStrategyType,
        "MaintenanceStrategies": "FleetSpotMaintenanceStrategiesTypeDef",
        "InstanceInterruptionBehavior": SpotInstanceInterruptionBehaviorType,
        "InstancePoolsToUseCount": int,
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

SpotPlacementTypeDef = TypedDict(
    "SpotPlacementTypeDef",
    {
        "AvailabilityZone": str,
        "GroupName": str,
        "Tenancy": TenancyType,
    },
    total=False,
)

SpotPriceTypeDef = TypedDict(
    "SpotPriceTypeDef",
    {
        "AvailabilityZone": str,
        "InstanceType": InstanceTypeType,
        "ProductDescription": RIProductDescriptionType,
        "SpotPrice": str,
        "Timestamp": datetime,
    },
    total=False,
)

StaleIpPermissionTypeDef = TypedDict(
    "StaleIpPermissionTypeDef",
    {
        "FromPort": int,
        "IpProtocol": str,
        "IpRanges": List[str],
        "PrefixListIds": List[str],
        "ToPort": int,
        "UserIdGroupPairs": List["UserIdGroupPairTypeDef"],
    },
    total=False,
)

StaleSecurityGroupTypeDef = TypedDict(
    "StaleSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupId": str,
        "GroupName": str,
        "StaleIpPermissions": List["StaleIpPermissionTypeDef"],
        "StaleIpPermissionsEgress": List["StaleIpPermissionTypeDef"],
        "VpcId": str,
    },
    total=False,
)

StartInstancesRequestInstanceTypeDef = TypedDict(
    "StartInstancesRequestInstanceTypeDef",
    {
        "AdditionalInfo": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredStartInstancesRequestTypeDef = TypedDict(
    "_RequiredStartInstancesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalStartInstancesRequestTypeDef = TypedDict(
    "_OptionalStartInstancesRequestTypeDef",
    {
        "AdditionalInfo": str,
        "DryRun": bool,
    },
    total=False,
)


class StartInstancesRequestTypeDef(
    _RequiredStartInstancesRequestTypeDef, _OptionalStartInstancesRequestTypeDef
):
    pass


StartInstancesResultResponseTypeDef = TypedDict(
    "StartInstancesResultResponseTypeDef",
    {
        "StartingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartNetworkInsightsAnalysisRequestTypeDef = TypedDict(
    "_RequiredStartNetworkInsightsAnalysisRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ClientToken": str,
    },
)
_OptionalStartNetworkInsightsAnalysisRequestTypeDef = TypedDict(
    "_OptionalStartNetworkInsightsAnalysisRequestTypeDef",
    {
        "FilterInArns": List[str],
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class StartNetworkInsightsAnalysisRequestTypeDef(
    _RequiredStartNetworkInsightsAnalysisRequestTypeDef,
    _OptionalStartNetworkInsightsAnalysisRequestTypeDef,
):
    pass


StartNetworkInsightsAnalysisResultResponseTypeDef = TypedDict(
    "StartNetworkInsightsAnalysisResultResponseTypeDef",
    {
        "NetworkInsightsAnalysis": "NetworkInsightsAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartVpcEndpointServicePrivateDnsVerificationRequestTypeDef = TypedDict(
    "_RequiredStartVpcEndpointServicePrivateDnsVerificationRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalStartVpcEndpointServicePrivateDnsVerificationRequestTypeDef = TypedDict(
    "_OptionalStartVpcEndpointServicePrivateDnsVerificationRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class StartVpcEndpointServicePrivateDnsVerificationRequestTypeDef(
    _RequiredStartVpcEndpointServicePrivateDnsVerificationRequestTypeDef,
    _OptionalStartVpcEndpointServicePrivateDnsVerificationRequestTypeDef,
):
    pass


StartVpcEndpointServicePrivateDnsVerificationResultResponseTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationResultResponseTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StateReasonTypeDef = TypedDict(
    "StateReasonTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

StopInstancesRequestInstanceTypeDef = TypedDict(
    "StopInstancesRequestInstanceTypeDef",
    {
        "Hibernate": bool,
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)

_RequiredStopInstancesRequestTypeDef = TypedDict(
    "_RequiredStopInstancesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalStopInstancesRequestTypeDef = TypedDict(
    "_OptionalStopInstancesRequestTypeDef",
    {
        "Hibernate": bool,
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)


class StopInstancesRequestTypeDef(
    _RequiredStopInstancesRequestTypeDef, _OptionalStopInstancesRequestTypeDef
):
    pass


StopInstancesResultResponseTypeDef = TypedDict(
    "StopInstancesResultResponseTypeDef",
    {
        "StoppingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
    total=False,
)

StorageTypeDef = TypedDict(
    "StorageTypeDef",
    {
        "S3": "S3StorageTypeDef",
    },
    total=False,
)

StoreImageTaskResultTypeDef = TypedDict(
    "StoreImageTaskResultTypeDef",
    {
        "AmiId": str,
        "TaskStartTime": datetime,
        "Bucket": str,
        "S3objectKey": str,
        "ProgressPercentage": int,
        "StoreTaskState": str,
        "StoreTaskFailureReason": str,
    },
    total=False,
)

SubnetAssociationTypeDef = TypedDict(
    "SubnetAssociationTypeDef",
    {
        "SubnetId": str,
        "State": TransitGatewayMulitcastDomainAssociationStateType,
    },
    total=False,
)

SubnetCidrBlockStateTypeDef = TypedDict(
    "SubnetCidrBlockStateTypeDef",
    {
        "State": SubnetCidrBlockStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

SubnetIpv6CidrBlockAssociationTypeDef = TypedDict(
    "SubnetIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "Ipv6CidrBlockState": "SubnetCidrBlockStateTypeDef",
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "AvailableIpAddressCount": int,
        "CidrBlock": str,
        "DefaultForAz": bool,
        "MapPublicIpOnLaunch": bool,
        "MapCustomerOwnedIpOnLaunch": bool,
        "CustomerOwnedIpv4Pool": str,
        "State": SubnetStateType,
        "SubnetId": str,
        "VpcId": str,
        "OwnerId": str,
        "AssignIpv6AddressOnCreation": bool,
        "Ipv6CidrBlockAssociationSet": List["SubnetIpv6CidrBlockAssociationTypeDef"],
        "Tags": List["TagTypeDef"],
        "SubnetArn": str,
        "OutpostArn": str,
    },
    total=False,
)

SuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

SuccessfulQueuedPurchaseDeletionTypeDef = TypedDict(
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    {
        "ReservedInstancesId": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "Key": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "Value": str,
    },
    total=False,
)

TagSpecificationTypeDef = TypedDict(
    "TagSpecificationTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


_RequiredTargetCapacitySpecificationRequestTypeDef = TypedDict(
    "_RequiredTargetCapacitySpecificationRequestTypeDef",
    {
        "TotalTargetCapacity": int,
    },
)
_OptionalTargetCapacitySpecificationRequestTypeDef = TypedDict(
    "_OptionalTargetCapacitySpecificationRequestTypeDef",
    {
        "OnDemandTargetCapacity": int,
        "SpotTargetCapacity": int,
        "DefaultTargetCapacityType": DefaultTargetCapacityTypeType,
    },
    total=False,
)


class TargetCapacitySpecificationRequestTypeDef(
    _RequiredTargetCapacitySpecificationRequestTypeDef,
    _OptionalTargetCapacitySpecificationRequestTypeDef,
):
    pass


TargetCapacitySpecificationTypeDef = TypedDict(
    "TargetCapacitySpecificationTypeDef",
    {
        "TotalTargetCapacity": int,
        "OnDemandTargetCapacity": int,
        "SpotTargetCapacity": int,
        "DefaultTargetCapacityType": DefaultTargetCapacityTypeType,
    },
    total=False,
)

_RequiredTargetConfigurationRequestTypeDef = TypedDict(
    "_RequiredTargetConfigurationRequestTypeDef",
    {
        "OfferingId": str,
    },
)
_OptionalTargetConfigurationRequestTypeDef = TypedDict(
    "_OptionalTargetConfigurationRequestTypeDef",
    {
        "InstanceCount": int,
    },
    total=False,
)


class TargetConfigurationRequestTypeDef(
    _RequiredTargetConfigurationRequestTypeDef, _OptionalTargetConfigurationRequestTypeDef
):
    pass


TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "InstanceCount": int,
        "OfferingId": str,
    },
    total=False,
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

TargetGroupsConfigTypeDef = TypedDict(
    "TargetGroupsConfigTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
    },
    total=False,
)

TargetNetworkTypeDef = TypedDict(
    "TargetNetworkTypeDef",
    {
        "AssociationId": str,
        "VpcId": str,
        "TargetNetworkId": str,
        "ClientVpnEndpointId": str,
        "Status": "AssociationStatusTypeDef",
        "SecurityGroups": List[str],
    },
    total=False,
)

TargetReservationValueTypeDef = TypedDict(
    "TargetReservationValueTypeDef",
    {
        "ReservationValue": "ReservationValueTypeDef",
        "TargetConfiguration": "TargetConfigurationTypeDef",
    },
    total=False,
)

_RequiredTerminateClientVpnConnectionsRequestTypeDef = TypedDict(
    "_RequiredTerminateClientVpnConnectionsRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalTerminateClientVpnConnectionsRequestTypeDef = TypedDict(
    "_OptionalTerminateClientVpnConnectionsRequestTypeDef",
    {
        "ConnectionId": str,
        "Username": str,
        "DryRun": bool,
    },
    total=False,
)


class TerminateClientVpnConnectionsRequestTypeDef(
    _RequiredTerminateClientVpnConnectionsRequestTypeDef,
    _OptionalTerminateClientVpnConnectionsRequestTypeDef,
):
    pass


TerminateClientVpnConnectionsResultResponseTypeDef = TypedDict(
    "TerminateClientVpnConnectionsResultResponseTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Username": str,
        "ConnectionStatuses": List["TerminateConnectionStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TerminateConnectionStatusTypeDef = TypedDict(
    "TerminateConnectionStatusTypeDef",
    {
        "ConnectionId": str,
        "PreviousStatus": "ClientVpnConnectionStatusTypeDef",
        "CurrentStatus": "ClientVpnConnectionStatusTypeDef",
    },
    total=False,
)

TerminateInstancesRequestInstanceTypeDef = TypedDict(
    "TerminateInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredTerminateInstancesRequestTypeDef = TypedDict(
    "_RequiredTerminateInstancesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalTerminateInstancesRequestTypeDef = TypedDict(
    "_OptionalTerminateInstancesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class TerminateInstancesRequestTypeDef(
    _RequiredTerminateInstancesRequestTypeDef, _OptionalTerminateInstancesRequestTypeDef
):
    pass


TerminateInstancesResultResponseTypeDef = TypedDict(
    "TerminateInstancesResultResponseTypeDef",
    {
        "TerminatingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrafficMirrorFilterRuleTypeDef = TypedDict(
    "TrafficMirrorFilterRuleTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "Protocol": int,
        "DestinationPortRange": "TrafficMirrorPortRangeTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeTypeDef",
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "Description": str,
    },
    total=False,
)

TrafficMirrorFilterTypeDef = TypedDict(
    "TrafficMirrorFilterTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "IngressFilterRules": List["TrafficMirrorFilterRuleTypeDef"],
        "EgressFilterRules": List["TrafficMirrorFilterRuleTypeDef"],
        "NetworkServices": List[Literal["amazon-dns"]],
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrafficMirrorPortRangeRequestTypeDef = TypedDict(
    "TrafficMirrorPortRangeRequestTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

TrafficMirrorPortRangeTypeDef = TypedDict(
    "TrafficMirrorPortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

TrafficMirrorSessionTypeDef = TypedDict(
    "TrafficMirrorSessionTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "NetworkInterfaceId": str,
        "OwnerId": str,
        "PacketLength": int,
        "SessionNumber": int,
        "VirtualNetworkId": int,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrafficMirrorTargetTypeDef = TypedDict(
    "TrafficMirrorTargetTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "NetworkInterfaceId": str,
        "NetworkLoadBalancerArn": str,
        "Type": TrafficMirrorTargetTypeType,
        "Description": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayAssociationTypeDef = TypedDict(
    "TransitGatewayAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayAttachmentAssociationTypeDef = TypedDict(
    "TransitGatewayAttachmentAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayAttachmentBgpConfigurationTypeDef = TypedDict(
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    {
        "TransitGatewayAsn": int,
        "PeerAsn": int,
        "TransitGatewayAddress": str,
        "PeerAddress": str,
        "BgpStatus": BgpStatusType,
    },
    total=False,
)

TransitGatewayAttachmentPropagationTypeDef = TypedDict(
    "TransitGatewayAttachmentPropagationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayPropagationStateType,
    },
    total=False,
)

TransitGatewayAttachmentTypeDef = TypedDict(
    "TransitGatewayAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "TransitGatewayOwnerId": str,
        "ResourceOwnerId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceId": str,
        "State": TransitGatewayAttachmentStateType,
        "Association": "TransitGatewayAttachmentAssociationTypeDef",
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayConnectOptionsTypeDef = TypedDict(
    "TransitGatewayConnectOptionsTypeDef",
    {
        "Protocol": Literal["gre"],
    },
    total=False,
)

TransitGatewayConnectPeerConfigurationTypeDef = TypedDict(
    "TransitGatewayConnectPeerConfigurationTypeDef",
    {
        "TransitGatewayAddress": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
        "Protocol": Literal["gre"],
        "BgpConfigurations": List["TransitGatewayAttachmentBgpConfigurationTypeDef"],
    },
    total=False,
)

TransitGatewayConnectPeerTypeDef = TypedDict(
    "TransitGatewayConnectPeerTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayConnectPeerId": str,
        "State": TransitGatewayConnectPeerStateType,
        "CreationTime": datetime,
        "ConnectPeerConfiguration": "TransitGatewayConnectPeerConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayConnectRequestBgpOptionsTypeDef = TypedDict(
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    {
        "PeerAsn": int,
    },
    total=False,
)

TransitGatewayConnectTypeDef = TypedDict(
    "TransitGatewayConnectTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransportTransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "State": TransitGatewayAttachmentStateType,
        "CreationTime": datetime,
        "Options": "TransitGatewayConnectOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastDeregisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DeregisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastDeregisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DeregisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastDomainAssociationTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceOwnerId": str,
        "Subnet": "SubnetAssociationTypeDef",
    },
    total=False,
)

TransitGatewayMulticastDomainAssociationsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceOwnerId": str,
        "Subnets": List["SubnetAssociationTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastDomainOptionsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainOptionsTypeDef",
    {
        "Igmpv2Support": Igmpv2SupportValueType,
        "StaticSourcesSupport": StaticSourcesSupportValueType,
        "AutoAcceptSharedAssociations": AutoAcceptSharedAssociationsValueType,
    },
    total=False,
)

TransitGatewayMulticastDomainTypeDef = TypedDict(
    "TransitGatewayMulticastDomainTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayId": str,
        "TransitGatewayMulticastDomainArn": str,
        "OwnerId": str,
        "Options": "TransitGatewayMulticastDomainOptionsTypeDef",
        "State": TransitGatewayMulticastDomainStateType,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastGroupTypeDef = TypedDict(
    "TransitGatewayMulticastGroupTypeDef",
    {
        "GroupIpAddress": str,
        "TransitGatewayAttachmentId": str,
        "SubnetId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceOwnerId": str,
        "NetworkInterfaceId": str,
        "GroupMember": bool,
        "GroupSource": bool,
        "MemberType": MembershipTypeType,
        "SourceType": MembershipTypeType,
    },
    total=False,
)

TransitGatewayMulticastRegisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "RegisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastRegisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "RegisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayOptionsTypeDef = TypedDict(
    "TransitGatewayOptionsTypeDef",
    {
        "AmazonSideAsn": int,
        "TransitGatewayCidrBlocks": List[str],
        "AutoAcceptSharedAttachments": AutoAcceptSharedAttachmentsValueType,
        "DefaultRouteTableAssociation": DefaultRouteTableAssociationValueType,
        "AssociationDefaultRouteTableId": str,
        "DefaultRouteTablePropagation": DefaultRouteTablePropagationValueType,
        "PropagationDefaultRouteTableId": str,
        "VpnEcmpSupport": VpnEcmpSupportValueType,
        "DnsSupport": DnsSupportValueType,
        "MulticastSupport": MulticastSupportValueType,
    },
    total=False,
)

TransitGatewayPeeringAttachmentTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "RequesterTgwInfo": "PeeringTgwInfoTypeDef",
        "AccepterTgwInfo": "PeeringTgwInfoTypeDef",
        "Status": "PeeringAttachmentStatusTypeDef",
        "State": TransitGatewayAttachmentStateType,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayPrefixListAttachmentTypeDef = TypedDict(
    "TransitGatewayPrefixListAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceId": str,
    },
    total=False,
)

TransitGatewayPrefixListReferenceTypeDef = TypedDict(
    "TransitGatewayPrefixListReferenceTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "PrefixListOwnerId": str,
        "State": TransitGatewayPrefixListReferenceStateType,
        "Blackhole": bool,
        "TransitGatewayAttachment": "TransitGatewayPrefixListAttachmentTypeDef",
    },
    total=False,
)

TransitGatewayPropagationTypeDef = TypedDict(
    "TransitGatewayPropagationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayPropagationStateType,
    },
    total=False,
)

TransitGatewayRequestOptionsTypeDef = TypedDict(
    "TransitGatewayRequestOptionsTypeDef",
    {
        "AmazonSideAsn": int,
        "AutoAcceptSharedAttachments": AutoAcceptSharedAttachmentsValueType,
        "DefaultRouteTableAssociation": DefaultRouteTableAssociationValueType,
        "DefaultRouteTablePropagation": DefaultRouteTablePropagationValueType,
        "VpnEcmpSupport": VpnEcmpSupportValueType,
        "DnsSupport": DnsSupportValueType,
        "MulticastSupport": MulticastSupportValueType,
        "TransitGatewayCidrBlocks": List[str],
    },
    total=False,
)

TransitGatewayRouteAttachmentTypeDef = TypedDict(
    "TransitGatewayRouteAttachmentTypeDef",
    {
        "ResourceId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
    },
    total=False,
)

TransitGatewayRouteTableAssociationTypeDef = TypedDict(
    "TransitGatewayRouteTableAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayRouteTablePropagationTypeDef = TypedDict(
    "TransitGatewayRouteTablePropagationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayPropagationStateType,
    },
    total=False,
)

TransitGatewayRouteTableTypeDef = TypedDict(
    "TransitGatewayRouteTableTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayId": str,
        "State": TransitGatewayRouteTableStateType,
        "DefaultAssociationRouteTable": bool,
        "DefaultPropagationRouteTable": bool,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayRouteTypeDef = TypedDict(
    "TransitGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "PrefixListId": str,
        "TransitGatewayAttachments": List["TransitGatewayRouteAttachmentTypeDef"],
        "Type": TransitGatewayRouteTypeType,
        "State": TransitGatewayRouteStateType,
    },
    total=False,
)

TransitGatewayTypeDef = TypedDict(
    "TransitGatewayTypeDef",
    {
        "TransitGatewayId": str,
        "TransitGatewayArn": str,
        "State": TransitGatewayStateType,
        "OwnerId": str,
        "Description": str,
        "CreationTime": datetime,
        "Options": "TransitGatewayOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayVpcAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    {
        "DnsSupport": DnsSupportValueType,
        "Ipv6Support": Ipv6SupportValueType,
        "ApplianceModeSupport": ApplianceModeSupportValueType,
    },
    total=False,
)

TransitGatewayVpcAttachmentTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "VpcId": str,
        "VpcOwnerId": str,
        "State": TransitGatewayAttachmentStateType,
        "SubnetIds": List[str],
        "CreationTime": datetime,
        "Options": "TransitGatewayVpcAttachmentOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrunkInterfaceAssociationTypeDef = TypedDict(
    "TrunkInterfaceAssociationTypeDef",
    {
        "AssociationId": str,
        "BranchInterfaceId": str,
        "TrunkInterfaceId": str,
        "InterfaceProtocol": InterfaceProtocolTypeType,
        "VlanId": int,
        "GreKey": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TunnelOptionTypeDef = TypedDict(
    "TunnelOptionTypeDef",
    {
        "OutsideIpAddress": str,
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DpdTimeoutSeconds": int,
        "DpdTimeoutAction": str,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersListValueTypeDef"],
        "IkeVersions": List["IKEVersionsListValueTypeDef"],
        "StartupAction": str,
    },
    total=False,
)

UnassignIpv6AddressesRequestTypeDef = TypedDict(
    "UnassignIpv6AddressesRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Ipv6Addresses": List[str],
    },
)

UnassignIpv6AddressesResultResponseTypeDef = TypedDict(
    "UnassignIpv6AddressesResultResponseTypeDef",
    {
        "NetworkInterfaceId": str,
        "UnassignedIpv6Addresses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnassignPrivateIpAddressesRequestNetworkInterfaceTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    {
        "PrivateIpAddresses": List[str],
    },
)

UnassignPrivateIpAddressesRequestTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "PrivateIpAddresses": List[str],
    },
)

UnmonitorInstancesRequestInstanceTypeDef = TypedDict(
    "UnmonitorInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredUnmonitorInstancesRequestTypeDef = TypedDict(
    "_RequiredUnmonitorInstancesRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalUnmonitorInstancesRequestTypeDef = TypedDict(
    "_OptionalUnmonitorInstancesRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class UnmonitorInstancesRequestTypeDef(
    _RequiredUnmonitorInstancesRequestTypeDef, _OptionalUnmonitorInstancesRequestTypeDef
):
    pass


UnmonitorInstancesResultResponseTypeDef = TypedDict(
    "UnmonitorInstancesResultResponseTypeDef",
    {
        "InstanceMonitorings": List["InstanceMonitoringTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    {
        "Code": UnsuccessfulInstanceCreditSpecificationErrorCodeType,
        "Message": str,
    },
    total=False,
)

UnsuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": str,
        "Error": "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    },
    total=False,
)

UnsuccessfulItemErrorTypeDef = TypedDict(
    "UnsuccessfulItemErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

UnsuccessfulItemTypeDef = TypedDict(
    "UnsuccessfulItemTypeDef",
    {
        "Error": "UnsuccessfulItemErrorTypeDef",
        "ResourceId": str,
    },
    total=False,
)

_RequiredUpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef",
    {
        "IpPermissions": List["IpPermissionTypeDef"],
    },
)
_OptionalUpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef",
    {
        "DryRun": bool,
        "GroupId": str,
        "GroupName": str,
    },
    total=False,
)


class UpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef(
    _RequiredUpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef,
    _OptionalUpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef,
):
    pass


UpdateSecurityGroupRuleDescriptionsEgressResultResponseTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef = TypedDict(
    "_RequiredUpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef",
    {
        "IpPermissions": List["IpPermissionTypeDef"],
    },
)
_OptionalUpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef = TypedDict(
    "_OptionalUpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef",
    {
        "DryRun": bool,
        "GroupId": str,
        "GroupName": str,
    },
    total=False,
)


class UpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef(
    _RequiredUpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef,
    _OptionalUpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef,
):
    pass


UpdateSecurityGroupRuleDescriptionsIngressResultResponseTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressResultResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserBucketDetailsTypeDef = TypedDict(
    "UserBucketDetailsTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

UserBucketTypeDef = TypedDict(
    "UserBucketTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "Data": str,
    },
    total=False,
)

UserIdGroupPairTypeDef = TypedDict(
    "UserIdGroupPairTypeDef",
    {
        "Description": str,
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

VCpuInfoTypeDef = TypedDict(
    "VCpuInfoTypeDef",
    {
        "DefaultVCpus": int,
        "DefaultCores": int,
        "DefaultThreadsPerCore": int,
        "ValidCores": List[int],
        "ValidThreadsPerCore": List[int],
    },
    total=False,
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "Errors": List["ValidationErrorTypeDef"],
    },
    total=False,
)

VgwTelemetryTypeDef = TypedDict(
    "VgwTelemetryTypeDef",
    {
        "AcceptedRouteCount": int,
        "LastStatusChange": datetime,
        "OutsideIpAddress": str,
        "Status": TelemetryStatusType,
        "StatusMessage": str,
        "CertificateArn": str,
    },
    total=False,
)

VolumeAttachmentResponseTypeDef = TypedDict(
    "VolumeAttachmentResponseTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": VolumeAttachmentStateType,
        "VolumeId": str,
        "DeleteOnTermination": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeDetailTypeDef = TypedDict(
    "VolumeDetailTypeDef",
    {
        "Size": int,
    },
)

VolumeModificationTypeDef = TypedDict(
    "VolumeModificationTypeDef",
    {
        "VolumeId": str,
        "ModificationState": VolumeModificationStateType,
        "StatusMessage": str,
        "TargetSize": int,
        "TargetIops": int,
        "TargetVolumeType": VolumeTypeType,
        "TargetThroughput": int,
        "TargetMultiAttachEnabled": bool,
        "OriginalSize": int,
        "OriginalIops": int,
        "OriginalVolumeType": VolumeTypeType,
        "OriginalThroughput": int,
        "OriginalMultiAttachEnabled": bool,
        "Progress": int,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

VolumeResponseTypeDef = TypedDict(
    "VolumeResponseTypeDef",
    {
        "Attachments": List["VolumeAttachmentResponseTypeDef"],
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "State": VolumeStateType,
        "VolumeId": str,
        "Iops": int,
        "Tags": List["TagTypeDef"],
        "VolumeType": VolumeTypeType,
        "FastRestored": bool,
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeStatusActionTypeDef = TypedDict(
    "VolumeStatusActionTypeDef",
    {
        "Code": str,
        "Description": str,
        "EventId": str,
        "EventType": str,
    },
    total=False,
)

VolumeStatusAttachmentStatusTypeDef = TypedDict(
    "VolumeStatusAttachmentStatusTypeDef",
    {
        "IoPerformance": str,
        "InstanceId": str,
    },
    total=False,
)

VolumeStatusDetailsTypeDef = TypedDict(
    "VolumeStatusDetailsTypeDef",
    {
        "Name": VolumeStatusNameType,
        "Status": str,
    },
    total=False,
)

VolumeStatusEventTypeDef = TypedDict(
    "VolumeStatusEventTypeDef",
    {
        "Description": str,
        "EventId": str,
        "EventType": str,
        "NotAfter": datetime,
        "NotBefore": datetime,
        "InstanceId": str,
    },
    total=False,
)

VolumeStatusInfoTypeDef = TypedDict(
    "VolumeStatusInfoTypeDef",
    {
        "Details": List["VolumeStatusDetailsTypeDef"],
        "Status": VolumeStatusInfoStatusType,
    },
    total=False,
)

VolumeStatusItemTypeDef = TypedDict(
    "VolumeStatusItemTypeDef",
    {
        "Actions": List["VolumeStatusActionTypeDef"],
        "AvailabilityZone": str,
        "OutpostArn": str,
        "Events": List["VolumeStatusEventTypeDef"],
        "VolumeId": str,
        "VolumeStatus": "VolumeStatusInfoTypeDef",
        "AttachmentStatuses": List["VolumeStatusAttachmentStatusTypeDef"],
    },
    total=False,
)

VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "State": AttachmentStatusType,
        "VpcId": str,
    },
    total=False,
)

VpcCidrBlockAssociationTypeDef = TypedDict(
    "VpcCidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "CidrBlock": str,
        "CidrBlockState": "VpcCidrBlockStateTypeDef",
    },
    total=False,
)

VpcCidrBlockStateTypeDef = TypedDict(
    "VpcCidrBlockStateTypeDef",
    {
        "State": VpcCidrBlockStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

VpcClassicLinkTypeDef = TypedDict(
    "VpcClassicLinkTypeDef",
    {
        "ClassicLinkEnabled": bool,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

VpcEndpointConnectionTypeDef = TypedDict(
    "VpcEndpointConnectionTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointId": str,
        "VpcEndpointOwner": str,
        "VpcEndpointState": StateType,
        "CreationTimestamp": datetime,
        "DnsEntries": List["DnsEntryTypeDef"],
        "NetworkLoadBalancerArns": List[str],
        "GatewayLoadBalancerArns": List[str],
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcEndpointType": VpcEndpointTypeType,
        "VpcId": str,
        "ServiceName": str,
        "State": StateType,
        "PolicyDocument": str,
        "RouteTableIds": List[str],
        "SubnetIds": List[str],
        "Groups": List["SecurityGroupIdentifierTypeDef"],
        "PrivateDnsEnabled": bool,
        "RequesterManaged": bool,
        "NetworkInterfaceIds": List[str],
        "DnsEntries": List["DnsEntryTypeDef"],
        "CreationTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "OwnerId": str,
        "LastError": "LastErrorTypeDef",
    },
    total=False,
)

VpcIpv6CidrBlockAssociationTypeDef = TypedDict(
    "VpcIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "Ipv6CidrBlockState": "VpcCidrBlockStateTypeDef",
        "NetworkBorderGroup": str,
        "Ipv6Pool": str,
    },
    total=False,
)

VpcPeeringConnectionOptionsDescriptionTypeDef = TypedDict(
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

VpcPeeringConnectionStateReasonTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonTypeDef",
    {
        "Code": VpcPeeringConnectionStateReasonCodeType,
        "Message": str,
    },
    total=False,
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "AccepterVpcInfo": "VpcPeeringConnectionVpcInfoTypeDef",
        "ExpirationTime": datetime,
        "RequesterVpcInfo": "VpcPeeringConnectionVpcInfoTypeDef",
        "Status": "VpcPeeringConnectionStateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

VpcPeeringConnectionVpcInfoTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoTypeDef",
    {
        "CidrBlock": str,
        "Ipv6CidrBlockSet": List["Ipv6CidrBlockTypeDef"],
        "CidrBlockSet": List["CidrBlockTypeDef"],
        "OwnerId": str,
        "PeeringOptions": "VpcPeeringConnectionOptionsDescriptionTypeDef",
        "VpcId": str,
        "Region": str,
    },
    total=False,
)

VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "CidrBlock": str,
        "DhcpOptionsId": str,
        "State": VpcStateType,
        "VpcId": str,
        "OwnerId": str,
        "InstanceTenancy": TenancyType,
        "Ipv6CidrBlockAssociationSet": List["VpcIpv6CidrBlockAssociationTypeDef"],
        "CidrBlockAssociationSet": List["VpcCidrBlockAssociationTypeDef"],
        "IsDefault": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpnConnectionOptionsSpecificationTypeDef = TypedDict(
    "VpnConnectionOptionsSpecificationTypeDef",
    {
        "EnableAcceleration": bool,
        "StaticRoutesOnly": bool,
        "TunnelInsideIpVersion": TunnelInsideIpVersionType,
        "TunnelOptions": List["VpnTunnelOptionsSpecificationTypeDef"],
        "LocalIpv4NetworkCidr": str,
        "RemoteIpv4NetworkCidr": str,
        "LocalIpv6NetworkCidr": str,
        "RemoteIpv6NetworkCidr": str,
    },
    total=False,
)

VpnConnectionOptionsTypeDef = TypedDict(
    "VpnConnectionOptionsTypeDef",
    {
        "EnableAcceleration": bool,
        "StaticRoutesOnly": bool,
        "LocalIpv4NetworkCidr": str,
        "RemoteIpv4NetworkCidr": str,
        "LocalIpv6NetworkCidr": str,
        "RemoteIpv6NetworkCidr": str,
        "TunnelInsideIpVersion": TunnelInsideIpVersionType,
        "TunnelOptions": List["TunnelOptionTypeDef"],
    },
    total=False,
)

VpnConnectionTypeDef = TypedDict(
    "VpnConnectionTypeDef",
    {
        "CustomerGatewayConfiguration": str,
        "CustomerGatewayId": str,
        "Category": str,
        "State": VpnStateType,
        "Type": Literal["ipsec.1"],
        "VpnConnectionId": str,
        "VpnGatewayId": str,
        "TransitGatewayId": str,
        "Options": "VpnConnectionOptionsTypeDef",
        "Routes": List["VpnStaticRouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VgwTelemetry": List["VgwTelemetryTypeDef"],
    },
    total=False,
)

VpnGatewayTypeDef = TypedDict(
    "VpnGatewayTypeDef",
    {
        "AvailabilityZone": str,
        "State": VpnStateType,
        "Type": Literal["ipsec.1"],
        "VpcAttachments": List["VpcAttachmentTypeDef"],
        "VpnGatewayId": str,
        "AmazonSideAsn": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpnStaticRouteTypeDef = TypedDict(
    "VpnStaticRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "Source": Literal["Static"],
        "State": VpnStateType,
    },
    total=False,
)

VpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DPDTimeoutSeconds": int,
        "DPDTimeoutAction": str,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersRequestListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersRequestListValueTypeDef"],
        "IKEVersions": List["IKEVersionsRequestListValueTypeDef"],
        "StartupAction": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWithdrawByoipCidrRequestTypeDef = TypedDict(
    "_RequiredWithdrawByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalWithdrawByoipCidrRequestTypeDef = TypedDict(
    "_OptionalWithdrawByoipCidrRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class WithdrawByoipCidrRequestTypeDef(
    _RequiredWithdrawByoipCidrRequestTypeDef, _OptionalWithdrawByoipCidrRequestTypeDef
):
    pass


WithdrawByoipCidrResultResponseTypeDef = TypedDict(
    "WithdrawByoipCidrResultResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
