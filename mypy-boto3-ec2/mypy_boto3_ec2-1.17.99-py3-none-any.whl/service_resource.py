"""
Type annotations for ec2 service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ec2 import EC2ServiceResource
    import mypy_boto3_ec2.service_resource as ec2_resources

    resource: EC2ServiceResource = boto3.resource("ec2")

    my_classic_address: ec2_resources.ClassicAddress = resource.ClassicAddress(...)
    my_dhcp_options: ec2_resources.DhcpOptions = resource.DhcpOptions(...)
    my_image: ec2_resources.Image = resource.Image(...)
    my_instance: ec2_resources.Instance = resource.Instance(...)
    my_internet_gateway: ec2_resources.InternetGateway = resource.InternetGateway(...)
    my_key_pair: ec2_resources.KeyPair = resource.KeyPair(...)
    my_key_pair_info: ec2_resources.KeyPairInfo = resource.KeyPairInfo(...)
    my_network_acl: ec2_resources.NetworkAcl = resource.NetworkAcl(...)
    my_network_interface: ec2_resources.NetworkInterface = resource.NetworkInterface(...)
    my_network_interface_association: ec2_resources.NetworkInterfaceAssociation = resource.NetworkInterfaceAssociation(...)
    my_placement_group: ec2_resources.PlacementGroup = resource.PlacementGroup(...)
    my_route: ec2_resources.Route = resource.Route(...)
    my_route_table: ec2_resources.RouteTable = resource.RouteTable(...)
    my_route_table_association: ec2_resources.RouteTableAssociation = resource.RouteTableAssociation(...)
    my_security_group: ec2_resources.SecurityGroup = resource.SecurityGroup(...)
    my_snapshot: ec2_resources.Snapshot = resource.Snapshot(...)
    my_subnet: ec2_resources.Subnet = resource.Subnet(...)
    my_tag: ec2_resources.Tag = resource.Tag(...)
    my_volume: ec2_resources.Volume = resource.Volume(...)
    my_vpc: ec2_resources.Vpc = resource.Vpc(...)
    my_vpc_peering_connection: ec2_resources.VpcPeeringConnection = resource.VpcPeeringConnection(...)
    my_vpc_address: ec2_resources.VpcAddress = resource.VpcAddress(...)
```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, Iterator, List, Optional, Union

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from botocore.response import StreamingBody

from .literals import (
    ArchitectureValuesType,
    BootModeValuesType,
    ImageAttributeNameType,
    InstanceAttributeNameType,
    InstanceTypeType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    OperationTypeType,
    PlacementStrategyType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    RuleActionType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    TenancyType,
    VolumeAttributeNameType,
    VolumeTypeType,
    VpcAttributeNameType,
)
from .type_defs import (
    AcceptVpcPeeringConnectionResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    BlobAttributeValueTypeDef,
    BlockDeviceMappingTypeDef,
    CapacityReservationSpecificationTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreditSpecificationRequestTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnclaveOptionsRequestTypeDef,
    FilterTypeDef,
    GetConsoleOutputResultTypeDef,
    GetPasswordDataResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    IpPermissionTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    MonitorInstancesResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    StartInstancesResultTypeDef,
    StopInstancesResultTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TerminateInstancesResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    VolumeAttachmentTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EC2ServiceResource",
    "ClassicAddress",
    "DhcpOptions",
    "Image",
    "Instance",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "Snapshot",
    "Subnet",
    "Tag",
    "Volume",
    "Vpc",
    "VpcPeeringConnection",
    "VpcAddress",
    "ServiceResourceClassicAddressesCollection",
    "ServiceResourceDhcpOptionsSetsCollection",
    "ServiceResourceImagesCollection",
    "ServiceResourceInstancesCollection",
    "ServiceResourceInternetGatewaysCollection",
    "ServiceResourceKeyPairsCollection",
    "ServiceResourceNetworkAclsCollection",
    "ServiceResourceNetworkInterfacesCollection",
    "ServiceResourcePlacementGroupsCollection",
    "ServiceResourceRouteTablesCollection",
    "ServiceResourceSecurityGroupsCollection",
    "ServiceResourceSnapshotsCollection",
    "ServiceResourceSubnetsCollection",
    "ServiceResourceVolumesCollection",
    "ServiceResourceVpcAddressesCollection",
    "ServiceResourceVpcPeeringConnectionsCollection",
    "ServiceResourceVpcsCollection",
    "InstanceVolumesCollection",
    "InstanceVpcAddressesCollection",
    "PlacementGroupInstancesCollection",
    "SubnetInstancesCollection",
    "SubnetNetworkInterfacesCollection",
    "VolumeSnapshotsCollection",
    "VpcAcceptedVpcPeeringConnectionsCollection",
    "VpcInstancesCollection",
    "VpcInternetGatewaysCollection",
    "VpcNetworkAclsCollection",
    "VpcNetworkInterfacesCollection",
    "VpcRequestedVpcPeeringConnectionsCollection",
    "VpcRouteTablesCollection",
    "VpcSecurityGroupsCollection",
    "VpcSubnetsCollection",
)


class ServiceResourceClassicAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceclassicaddressescollection)
    """

    def all(self) -> "ServiceResourceClassicAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceClassicAddressesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceClassicAddressesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceClassicAddressesCollection":
        pass

    def pages(self) -> Iterator[List["ClassicAddress"]]:
        pass

    def __iter__(self) -> Iterator["ClassicAddress"]:
        pass


class ServiceResourceDhcpOptionsSetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcedhcpoptionssetscollection)
    """

    def all(self) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def pages(self) -> Iterator[List["DhcpOptions"]]:
        pass

    def __iter__(self) -> Iterator["DhcpOptions"]:
        pass


class ServiceResourceImagesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.images)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceimagescollection)
    """

    def all(self) -> "ServiceResourceImagesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        IncludeDeprecated: bool = None,
        DryRun: bool = None
    ) -> "ServiceResourceImagesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceImagesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceImagesCollection":
        pass

    def pages(self) -> Iterator[List["Image"]]:
        pass

    def __iter__(self) -> Iterator["Image"]:
        pass


class ServiceResourceInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceinstancescollection)
    """

    def all(self) -> "ServiceResourceInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "ServiceResourceInstancesCollection":
        pass

    def create_tags(self, *, DryRun: bool = None) -> None:
        pass

    def monitor(self, *, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, *, DryRun: bool = None) -> None:
        pass

    def start(
        self, *, AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, *, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, *, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, *, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "ServiceResourceInstancesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class ServiceResourceInternetGatewaysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceinternetgatewayscollection)
    """

    def all(self) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def pages(self) -> Iterator[List["InternetGateway"]]:
        pass

    def __iter__(self) -> Iterator["InternetGateway"]:
        pass


class ServiceResourceKeyPairsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcekeypairscollection)
    """

    def all(self) -> "ServiceResourceKeyPairsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceKeyPairsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceKeyPairsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceKeyPairsCollection":
        pass

    def pages(self) -> Iterator[List["KeyPairInfo"]]:
        pass

    def __iter__(self) -> Iterator["KeyPairInfo"]:
        pass


class ServiceResourceNetworkAclsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.network_acls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcenetworkaclscollection)
    """

    def all(self) -> "ServiceResourceNetworkAclsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceNetworkAclsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceNetworkAclsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceNetworkAclsCollection":
        pass

    def pages(self) -> Iterator[List["NetworkAcl"]]:
        pass

    def __iter__(self) -> Iterator["NetworkAcl"]:
        pass


class ServiceResourceNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcenetworkinterfacescollection)
    """

    def all(self) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def pages(self) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(self) -> Iterator["NetworkInterface"]:
        pass


class ServiceResourcePlacementGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceplacementgroupscollection)
    """

    def all(self) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
        GroupIds: List[str] = None
    ) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def pages(self) -> Iterator[List["PlacementGroup"]]:
        pass

    def __iter__(self) -> Iterator["PlacementGroup"]:
        pass


class ServiceResourceRouteTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.route_tables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceroutetablescollection)
    """

    def all(self) -> "ServiceResourceRouteTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceRouteTablesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceRouteTablesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceRouteTablesCollection":
        pass

    def pages(self) -> Iterator[List["RouteTable"]]:
        pass

    def __iter__(self) -> Iterator["RouteTable"]:
        pass


class ServiceResourceSecurityGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.security_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcesecuritygroupscollection)
    """

    def all(self) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def pages(self) -> Iterator[List["SecurityGroup"]]:
        pass

    def __iter__(self) -> Iterator["SecurityGroup"]:
        pass


class ServiceResourceSnapshotsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.snapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcesnapshotscollection)
    """

    def all(self) -> "ServiceResourceSnapshotsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceSnapshotsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSnapshotsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSnapshotsCollection":
        pass

    def pages(self) -> Iterator[List["Snapshot"]]:
        pass

    def __iter__(self) -> Iterator["Snapshot"]:
        pass


class ServiceResourceSubnetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.subnets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcesubnetscollection)
    """

    def all(self) -> "ServiceResourceSubnetsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceSubnetsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSubnetsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSubnetsCollection":
        pass

    def pages(self) -> Iterator[List["Subnet"]]:
        pass

    def __iter__(self) -> Iterator["Subnet"]:
        pass


class ServiceResourceVolumesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.volumes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevolumescollection)
    """

    def all(self) -> "ServiceResourceVolumesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "ServiceResourceVolumesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVolumesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVolumesCollection":
        pass

    def pages(self) -> Iterator[List["Volume"]]:
        pass

    def __iter__(self) -> Iterator["Volume"]:
        pass


class ServiceResourceVpcAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevpcaddressescollection)
    """

    def all(self) -> "ServiceResourceVpcAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> "ServiceResourceVpcAddressesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVpcAddressesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVpcAddressesCollection":
        pass

    def pages(self) -> Iterator[List["VpcAddress"]]:
        pass

    def __iter__(self) -> Iterator["VpcAddress"]:
        pass


class ServiceResourceVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevpcpeeringconnectionscollection)
    """

    def all(self) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def pages(self) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(self) -> Iterator["VpcPeeringConnection"]:
        pass


class ServiceResourceVpcsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.vpcs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevpcscollection)
    """

    def all(self) -> "ServiceResourceVpcsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "ServiceResourceVpcsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVpcsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVpcsCollection":
        pass

    def pages(self) -> Iterator[List["Vpc"]]:
        pass

    def __iter__(self) -> Iterator["Vpc"]:
        pass


class InstanceVolumesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.volumes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancevolumescollection)
    """

    def all(self) -> "InstanceVolumesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "InstanceVolumesCollection":
        pass

    def limit(self, count: int) -> "InstanceVolumesCollection":
        pass

    def page_size(self, count: int) -> "InstanceVolumesCollection":
        pass

    def pages(self) -> Iterator[List["Volume"]]:
        pass

    def __iter__(self) -> Iterator["Volume"]:
        pass


class InstanceVpcAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.vpc_addresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancevpcaddressescollection)
    """

    def all(self) -> "InstanceVpcAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> "InstanceVpcAddressesCollection":
        pass

    def limit(self, count: int) -> "InstanceVpcAddressesCollection":
        pass

    def page_size(self, count: int) -> "InstanceVpcAddressesCollection":
        pass

    def pages(self) -> Iterator[List["VpcAddress"]]:
        pass

    def __iter__(self) -> Iterator["VpcAddress"]:
        pass


class PlacementGroupInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.PlacementGroup.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupinstancescollection)
    """

    def all(self) -> "PlacementGroupInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "PlacementGroupInstancesCollection":
        pass

    def create_tags(self, *, DryRun: bool = None) -> None:
        pass

    def monitor(self, *, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, *, DryRun: bool = None) -> None:
        pass

    def start(
        self, *, AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, *, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, *, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, *, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "PlacementGroupInstancesCollection":
        pass

    def page_size(self, count: int) -> "PlacementGroupInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class SubnetInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetinstancescollection)
    """

    def all(self) -> "SubnetInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "SubnetInstancesCollection":
        pass

    def create_tags(self, *, DryRun: bool = None) -> None:
        pass

    def monitor(self, *, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, *, DryRun: bool = None) -> None:
        pass

    def start(
        self, *, AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, *, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, *, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, *, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "SubnetInstancesCollection":
        pass

    def page_size(self, count: int) -> "SubnetInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class SubnetNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.network_interfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetnetworkinterfacescollection)
    """

    def all(self) -> "SubnetNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "SubnetNetworkInterfacesCollection":
        pass

    def limit(self, count: int) -> "SubnetNetworkInterfacesCollection":
        pass

    def page_size(self, count: int) -> "SubnetNetworkInterfacesCollection":
        pass

    def pages(self) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(self) -> Iterator["NetworkInterface"]:
        pass


class VolumeSnapshotsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.snapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumesnapshotscollection)
    """

    def all(self) -> "VolumeSnapshotsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> "VolumeSnapshotsCollection":
        pass

    def limit(self, count: int) -> "VolumeSnapshotsCollection":
        pass

    def page_size(self, count: int) -> "VolumeSnapshotsCollection":
        pass

    def pages(self) -> Iterator[List["Snapshot"]]:
        pass

    def __iter__(self) -> Iterator["Snapshot"]:
        pass


class VpcAcceptedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.accepted_vpc_peering_connections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcacceptedvpcpeeringconnectionscollection)
    """

    def all(self) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def limit(self, count: int) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def page_size(self, count: int) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def pages(self) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(self) -> Iterator["VpcPeeringConnection"]:
        pass


class VpcInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcinstancescollection)
    """

    def all(self) -> "VpcInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> "VpcInstancesCollection":
        pass

    def create_tags(self, *, DryRun: bool = None) -> None:
        pass

    def monitor(self, *, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, *, DryRun: bool = None) -> None:
        pass

    def start(
        self, *, AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, *, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, *, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, *, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "VpcInstancesCollection":
        pass

    def page_size(self, count: int) -> "VpcInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class VpcInternetGatewaysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.internet_gateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcinternetgatewayscollection)
    """

    def all(self) -> "VpcInternetGatewaysCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcInternetGatewaysCollection":
        pass

    def limit(self, count: int) -> "VpcInternetGatewaysCollection":
        pass

    def page_size(self, count: int) -> "VpcInternetGatewaysCollection":
        pass

    def pages(self) -> Iterator[List["InternetGateway"]]:
        pass

    def __iter__(self) -> Iterator["InternetGateway"]:
        pass


class VpcNetworkAclsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.network_acls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcnetworkaclscollection)
    """

    def all(self) -> "VpcNetworkAclsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcNetworkAclsCollection":
        pass

    def limit(self, count: int) -> "VpcNetworkAclsCollection":
        pass

    def page_size(self, count: int) -> "VpcNetworkAclsCollection":
        pass

    def pages(self) -> Iterator[List["NetworkAcl"]]:
        pass

    def __iter__(self) -> Iterator["NetworkAcl"]:
        pass


class VpcNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.network_interfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcnetworkinterfacescollection)
    """

    def all(self) -> "VpcNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcNetworkInterfacesCollection":
        pass

    def limit(self, count: int) -> "VpcNetworkInterfacesCollection":
        pass

    def page_size(self, count: int) -> "VpcNetworkInterfacesCollection":
        pass

    def pages(self) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(self) -> Iterator["NetworkInterface"]:
        pass


class VpcRequestedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.requested_vpc_peering_connections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcrequestedvpcpeeringconnectionscollection)
    """

    def all(self) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def limit(self, count: int) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def page_size(self, count: int) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def pages(self) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(self) -> Iterator["VpcPeeringConnection"]:
        pass


class VpcRouteTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.route_tables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcroutetablescollection)
    """

    def all(self) -> "VpcRouteTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcRouteTablesCollection":
        pass

    def limit(self, count: int) -> "VpcRouteTablesCollection":
        pass

    def page_size(self, count: int) -> "VpcRouteTablesCollection":
        pass

    def pages(self) -> Iterator[List["RouteTable"]]:
        pass

    def __iter__(self) -> Iterator["RouteTable"]:
        pass


class VpcSecurityGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.security_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcsecuritygroupscollection)
    """

    def all(self) -> "VpcSecurityGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcSecurityGroupsCollection":
        pass

    def limit(self, count: int) -> "VpcSecurityGroupsCollection":
        pass

    def page_size(self, count: int) -> "VpcSecurityGroupsCollection":
        pass

    def pages(self) -> Iterator[List["SecurityGroup"]]:
        pass

    def __iter__(self) -> Iterator["SecurityGroup"]:
        pass


class VpcSubnetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.subnets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcsubnetscollection)
    """

    def all(self) -> "VpcSubnetsCollection":
        pass

    def filter(  # type: ignore
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> "VpcSubnetsCollection":
        pass

    def limit(self, count: int) -> "VpcSubnetsCollection":
        pass

    def page_size(self, count: int) -> "VpcSubnetsCollection":
        pass

    def pages(self) -> Iterator[List["Subnet"]]:
        pass

    def __iter__(self) -> Iterator["Subnet"]:
        pass


class ClassicAddress(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddress)
    """

    instance_id: str
    allocation_id: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    carrier_ip: str
    public_ip: str

    def associate(
        self,
        *,
        AllocationId: str = None,
        InstanceId: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None
    ) -> AssociateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ClassicAddress.associate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressassociate-method)
        """

    def disassociate(
        self, *, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ClassicAddress.disassociate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressdisassociate-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ClassicAddress.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ClassicAddress.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressload-method)
        """

    def release(
        self,
        *,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ClassicAddress.release)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressrelease-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ClassicAddress.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressreload-method)
        """


_ClassicAddress = ClassicAddress


class KeyPair(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.KeyPair)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypair)
    """

    key_fingerprint: str
    key_material: str
    key_name: str
    key_pair_id: str
    tags: List[Any]
    name: str

    def delete(self, *, KeyPairId: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.KeyPair.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.KeyPair.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairget_available_subresources-method)
        """


_KeyPair = KeyPair


class KeyPairInfo(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.KeyPairInfo)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfo)
    """

    key_pair_id: str
    key_fingerprint: str
    key_name: str
    tags: List[Any]
    name: str

    def delete(self, *, KeyPairId: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.KeyPairInfo.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfodelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.KeyPairInfo.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfoget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.KeyPairInfo.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfoload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.KeyPairInfo.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinforeload-method)
        """


_KeyPairInfo = KeyPairInfo


class NetworkInterfaceAssociation(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociation)
    """

    carrier_ip: str
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str
    address: "VpcAddress"

    def delete(self, *, PublicIp: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationreload-method)
        """


_NetworkInterfaceAssociation = NetworkInterfaceAssociation


class PlacementGroup(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroup)
    """

    group_name: str
    state: str
    strategy: str
    partition_count: int
    group_id: str
    tags: List[Any]
    name: str
    instances: PlacementGroupInstancesCollection

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.PlacementGroup.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.PlacementGroup.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.PlacementGroup.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.PlacementGroup.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupreload-method)
        """


_PlacementGroup = PlacementGroup


class Tag(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Tag)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tag)
    """

    resource_type: str
    resource_id: str
    key: str
    value: str

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Tag.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Tag.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Tag.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Tag.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagreload-method)
        """


_Tag = Tag


class VpcPeeringConnection(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnection)
    """

    accepter_vpc_info: Dict[str, Any]
    expiration_time: datetime
    requester_vpc_info: Dict[str, Any]
    status: Dict[str, Any]
    tags: List[Any]
    vpc_peering_connection_id: str
    id: str
    accepter_vpc: "Vpc"
    requester_vpc: "Vpc"

    def accept(self, *, DryRun: bool = None) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.accept)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionaccept-method)
        """

    def delete(self, *, DryRun: bool = None) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectiondelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionload-method)
        """

    def reject(self, *, DryRun: bool = None) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.reject)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionreject-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionreload-method)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcPeeringConnection.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionwait_until_exists-method)
        """


_VpcPeeringConnection = VpcPeeringConnection


class VpcAddress(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddress)
    """

    instance_id: str
    public_ip: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    carrier_ip: str
    allocation_id: str
    association: "NetworkInterfaceAssociation"

    def associate(
        self,
        *,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None
    ) -> AssociateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcAddress.associate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressassociate-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcAddress.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcAddress.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressload-method)
        """

    def release(
        self,
        *,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcAddress.release)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressrelease-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.VpcAddress.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressreload-method)
        """


_VpcAddress = VpcAddress


class DhcpOptions(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptions)
    """

    dhcp_configurations: List[Any]
    dhcp_options_id: str
    owner_id: str
    tags: List[Any]
    id: str

    def associate_with_vpc(self, *, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.DhcpOptions.associate_with_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsassociate_with_vpc-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionscreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.DhcpOptions.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.DhcpOptions.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.DhcpOptions.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.DhcpOptions.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsreload-method)
        """


_DhcpOptions = DhcpOptions


class Image(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Image)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#image)
    """

    architecture: str
    creation_date: str
    image_id: str
    image_location: str
    image_type: str
    public: bool
    kernel_id: str
    owner_id: str
    platform: str
    platform_details: str
    usage_operation: str
    product_codes: List[Any]
    ramdisk_id: str
    state: str
    block_device_mappings: List[Any]
    description: str
    ena_support: bool
    hypervisor: str
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    boot_mode: str
    deprecation_time: str
    id: str

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagecreate_tags-method)
        """

    def deregister(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.deregister)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagederegister-method)
        """

    def describe_attribute(
        self, *, Attribute: ImageAttributeNameType, DryRun: bool = None
    ) -> ImageAttributeTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagedescribe_attribute-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imageget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imageload-method)
        """

    def modify_attribute(
        self,
        *,
        Attribute: str = None,
        Description: "AttributeValueTypeDef" = None,
        LaunchPermission: LaunchPermissionModificationsTypeDef = None,
        OperationType: OperationTypeType = None,
        ProductCodes: List[str] = None,
        UserGroups: List[str] = None,
        UserIds: List[str] = None,
        Value: str = None,
        DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagemodify_attribute-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagereload-method)
        """

    def reset_attribute(
        self, *, Attribute: Literal["launchPermission"], DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagereset_attribute-method)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Image.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagewait_until_exists-method)
        """


_Image = Image


class InternetGateway(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgateway)
    """

    attachments: List[Any]
    internet_gateway_id: str
    owner_id: str
    tags: List[Any]
    id: str

    def attach_to_vpc(self, *, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.attach_to_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayattach_to_vpc-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewaycreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewaydelete-method)
        """

    def detach_from_vpc(self, *, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.detach_from_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewaydetach_from_vpc-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.InternetGateway.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayreload-method)
        """


_InternetGateway = InternetGateway


class NetworkAcl(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkacl)
    """

    associations: List[Any]
    entries: List[Any]
    is_default: bool
    network_acl_id: str
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str
    vpc: "Vpc"

    def create_entry(
        self,
        *,
        Egress: bool,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
        Ipv6CidrBlock: str = None,
        PortRange: "PortRangeTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.create_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclcreate_entry-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclcreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkacldelete-method)
        """

    def delete_entry(self, *, Egress: bool, RuleNumber: int, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.delete_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkacldelete_entry-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclreload-method)
        """

    def replace_association(
        self, *, AssociationId: str, DryRun: bool = None
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.replace_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclreplace_association-method)
        """

    def replace_entry(
        self,
        *,
        Egress: bool,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
        Ipv6CidrBlock: str = None,
        PortRange: "PortRangeTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkAcl.replace_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclreplace_entry-method)
        """


_NetworkAcl = NetworkAcl


class NetworkInterface(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterface)
    """

    association_attribute: Dict[str, Any]
    attachment: Dict[str, Any]
    availability_zone: str
    description: str
    groups: List[Any]
    interface_type: str
    ipv6_addresses: List[Any]
    mac_address: str
    network_interface_id: str
    outpost_arn: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List[Any]
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: str
    subnet_id: str
    tag_set: List[Any]
    vpc_id: str
    id: str
    association: "NetworkInterfaceAssociation"
    subnet: "Subnet"
    vpc: "Vpc"

    def assign_private_ip_addresses(
        self,
        *,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.assign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassign_private_ip_addresses-method)
        """

    def attach(
        self,
        *,
        DeviceIndex: int,
        InstanceId: str,
        DryRun: bool = None,
        NetworkCardIndex: int = None
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.attach)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceattach-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacecreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacedelete-method)
        """

    def describe_attribute(
        self, *, Attribute: NetworkInterfaceAttributeType = None, DryRun: bool = None
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacedescribe_attribute-method)
        """

    def detach(self, *, AttachmentId: str, DryRun: bool = None, Force: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.detach)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacedetach-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceload-method)
        """

    def modify_attribute(
        self,
        *,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
        Description: "AttributeValueTypeDef" = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacemodify_attribute-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacereload-method)
        """

    def reset_attribute(self, *, DryRun: bool = None, SourceDestCheck: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacereset_attribute-method)
        """

    def unassign_private_ip_addresses(self, *, PrivateIpAddresses: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.NetworkInterface.unassign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceunassign_private_ip_addresses-method)
        """


_NetworkInterface = NetworkInterface


class Route(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Route)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#route)
    """

    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    transit_gateway_id: str
    local_gateway_id: str
    carrier_gateway_id: str
    network_interface_id: str
    origin: str
    state: str
    vpc_peering_connection_id: str
    route_table_id: str
    destination_cidr_block: str

    def RouteTable(self) -> "_RouteTable":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Route.RouteTable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routeroutetable-method)
        """

    def delete(
        self,
        *,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Route.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routedelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Route.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routeget_available_subresources-method)
        """

    def replace(
        self,
        *,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
        VpcEndpointId: str = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        LocalTarget: bool = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        CarrierGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Route.replace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routereplace-method)
        """


_Route = Route


class RouteTableAssociation(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociation)
    """

    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    gateway_id: str
    association_state: Dict[str, Any]
    id: str
    route_table: "RouteTable"
    subnet: "Subnet"

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTableAssociation.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociationdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTableAssociation.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociationget_available_subresources-method)
        """

    def replace_subnet(self, *, RouteTableId: str, DryRun: bool = None) -> "_RouteTableAssociation":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTableAssociation.replace_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociationreplace_subnet-method)
        """


_RouteTableAssociation = RouteTableAssociation


class SecurityGroup(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroup)
    """

    description: str
    group_name: str
    ip_permissions: List[Any]
    owner_id: str
    group_id: str
    ip_permissions_egress: List[Any]
    tags: List[Any]
    vpc_id: str
    id: str

    def authorize_egress(
        self,
        *,
        DryRun: bool = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.authorize_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupauthorize_egress-method)
        """

    def authorize_ingress(
        self,
        *,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.authorize_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupauthorize_ingress-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupcreate_tags-method)
        """

    def delete(self, *, GroupName: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupreload-method)
        """

    def revoke_egress(
        self,
        *,
        DryRun: bool = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.revoke_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygrouprevoke_egress-method)
        """

    def revoke_ingress(
        self,
        *,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.SecurityGroup.revoke_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygrouprevoke_ingress-method)
        """


_SecurityGroup = SecurityGroup


class Snapshot(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Snapshot)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshot)
    """

    data_encryption_key_id: str
    description: str
    encrypted: bool
    kms_key_id: str
    owner_id: str
    progress: str
    snapshot_id: str
    start_time: datetime
    state: str
    state_message: str
    volume_id: str
    volume_size: int
    owner_alias: str
    outpost_arn: str
    tags: List[Any]
    id: str
    volume: "Volume"

    def copy(
        self,
        *,
        SourceRegion: str,
        Description: str = None,
        DestinationOutpostArn: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CopySnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotcopy-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotcreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotdelete-method)
        """

    def describe_attribute(
        self, *, Attribute: SnapshotAttributeNameType, DryRun: bool = None
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotdescribe_attribute-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotload-method)
        """

    def modify_attribute(
        self,
        *,
        Attribute: SnapshotAttributeNameType = None,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: OperationTypeType = None,
        UserIds: List[str] = None,
        DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotmodify_attribute-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotreload-method)
        """

    def reset_attribute(self, *, Attribute: SnapshotAttributeNameType, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotreset_attribute-method)
        """

    def wait_until_completed(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Snapshot.wait_until_completed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotwait_until_completed-method)
        """


_Snapshot = Snapshot


class Instance(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Instance)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instance)
    """

    ami_launch_index: int
    image_id: str
    instance_id: str
    instance_type: str
    kernel_id: str
    key_name: str
    launch_time: datetime
    monitoring: Dict[str, Any]
    placement: Dict[str, Any]
    platform: str
    private_dns_name: str
    private_ip_address: str
    product_codes: List[Any]
    public_dns_name: str
    public_ip_address: str
    ramdisk_id: str
    state: Dict[str, Any]
    state_transition_reason: str
    subnet_id: str
    vpc_id: str
    architecture: str
    block_device_mappings: List[Any]
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: str
    iam_instance_profile: Dict[str, Any]
    instance_lifecycle: str
    elastic_gpu_associations: List[Any]
    elastic_inference_accelerator_associations: List[Any]
    network_interfaces_attribute: List[Any]
    outpost_arn: str
    root_device_name: str
    root_device_type: str
    security_groups: List[Any]
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    cpu_options: Dict[str, Any]
    capacity_reservation_id: str
    capacity_reservation_specification: Dict[str, Any]
    hibernation_options: Dict[str, Any]
    licenses: List[Any]
    metadata_options: Dict[str, Any]
    enclave_options: Dict[str, Any]
    boot_mode: str
    id: str
    classic_address: "ClassicAddress"
    image: "Image"
    key_pair: "KeyPairInfo"
    network_interfaces: "NetworkInterface"
    placement_group: "PlacementGroup"
    subnet: "Subnet"
    vpc: "Vpc"
    volumes: InstanceVolumesCollection
    vpc_addresses: InstanceVpcAddressesCollection

    def attach_classic_link_vpc(
        self, *, Groups: List[str], VpcId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.attach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceattach_classic_link_vpc-method)
        """

    def attach_volume(
        self, *, Device: str, VolumeId: str, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.attach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceattach_volume-method)
        """

    def console_output(
        self, *, DryRun: bool = None, Latest: bool = None
    ) -> GetConsoleOutputResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.console_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceconsole_output-method)
        """

    def create_image(
        self,
        *,
        Name: str,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _Image:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancecreate_image-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancecreate_tags-method)
        """

    def delete_tags(self, Tags: List[TagTypeDef] = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedelete_tags-method)
        """

    def describe_attribute(
        self, *, Attribute: InstanceAttributeNameType, DryRun: bool = None
    ) -> InstanceAttributeTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedescribe_attribute-method)
        """

    def detach_classic_link_vpc(
        self, *, VpcId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.detach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedetach_classic_link_vpc-method)
        """

    def detach_volume(
        self, *, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.detach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedetach_volume-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceload-method)
        """

    def modify_attribute(
        self,
        *,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
        Attribute: InstanceAttributeNameType = None,
        BlockDeviceMappings: List[InstanceBlockDeviceMappingSpecificationTypeDef] = None,
        DisableApiTermination: "AttributeBooleanValueTypeDef" = None,
        DryRun: bool = None,
        EbsOptimized: "AttributeBooleanValueTypeDef" = None,
        EnaSupport: "AttributeBooleanValueTypeDef" = None,
        Groups: List[str] = None,
        InstanceInitiatedShutdownBehavior: "AttributeValueTypeDef" = None,
        InstanceType: "AttributeValueTypeDef" = None,
        Kernel: "AttributeValueTypeDef" = None,
        Ramdisk: "AttributeValueTypeDef" = None,
        SriovNetSupport: "AttributeValueTypeDef" = None,
        UserData: BlobAttributeValueTypeDef = None,
        Value: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancemodify_attribute-method)
        """

    def monitor(self, *, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancemonitor-method)
        """

    def password_data(self, *, DryRun: bool = None) -> GetPasswordDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.password_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancepassword_data-method)
        """

    def reboot(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.reboot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereboot-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereload-method)
        """

    def report_status(
        self,
        *,
        ReasonCodes: List[ReportInstanceReasonCodesType],
        Status: ReportStatusTypeType,
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.report_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereport_status-method)
        """

    def reset_attribute(self, *, Attribute: InstanceAttributeNameType, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset_attribute-method)
        """

    def reset_kernel(self, *, Attribute: InstanceAttributeNameType, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.reset_kernel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset_kernel-method)
        """

    def reset_ramdisk(self, *, Attribute: InstanceAttributeNameType, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.reset_ramdisk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset_ramdisk-method)
        """

    def reset_source_dest_check(
        self, *, Attribute: InstanceAttributeNameType, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.reset_source_dest_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset_source_dest_check-method)
        """

    def start(
        self, *, AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.start)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancestart-method)
        """

    def stop(
        self, *, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.stop)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancestop-method)
        """

    def terminate(self, *, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.terminate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceterminate-method)
        """

    def unmonitor(self, *, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.unmonitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceunmonitor-method)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait_until_exists-method)
        """

    def wait_until_running(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.wait_until_running)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait_until_running-method)
        """

    def wait_until_stopped(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.wait_until_stopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait_until_stopped-method)
        """

    def wait_until_terminated(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Instance.wait_until_terminated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait_until_terminated-method)
        """


_Instance = Instance


class Volume(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Volume)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volume)
    """

    attachments: List[Any]
    availability_zone: str
    create_time: datetime
    encrypted: bool
    kms_key_id: str
    outpost_arn: str
    size: int
    snapshot_id: str
    state: str
    volume_id: str
    iops: int
    tags: List[Any]
    volume_type: str
    fast_restored: bool
    multi_attach_enabled: bool
    throughput: int
    id: str
    snapshots: VolumeSnapshotsCollection

    def attach_to_instance(
        self, *, Device: str, InstanceId: str, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.attach_to_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeattach_to_instance-method)
        """

    def create_snapshot(
        self,
        *,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> _Snapshot:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumecreate_snapshot-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumecreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedelete-method)
        """

    def describe_attribute(
        self, *, Attribute: VolumeAttributeNameType, DryRun: bool = None
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedescribe_attribute-method)
        """

    def describe_status(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.describe_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedescribe_status-method)
        """

    def detach_from_instance(
        self, *, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.detach_from_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedetach_from_instance-method)
        """

    def enable_io(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.enable_io)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeenable_io-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeload-method)
        """

    def modify_attribute(
        self, *, AutoEnableIO: "AttributeBooleanValueTypeDef" = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumemodify_attribute-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Volume.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumereload-method)
        """


_Volume = Volume


class RouteTable(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.RouteTable)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetable)
    """

    associations_attribute: List[Any]
    propagating_vgws: List[Any]
    route_table_id: str
    routes_attribute: List[Any]
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str
    associations: "RouteTableAssociation"
    routes: "Route"
    vpc: "Vpc"

    def associate_with_subnet(
        self, *, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> _RouteTableAssociation:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.associate_with_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociate_with_subnet-method)
        """

    def create_route(
        self,
        *,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
        VpcEndpointId: str = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        CarrierGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None
    ) -> _Route:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.create_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetablecreate_route-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetablecreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetabledelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.RouteTable.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetablereload-method)
        """


_RouteTable = RouteTable


class Subnet(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Subnet)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnet)
    """

    availability_zone: str
    availability_zone_id: str
    available_ip_address_count: int
    cidr_block: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    map_customer_owned_ip_on_launch: bool
    customer_owned_ipv4_pool: str
    state: str
    subnet_id: str
    vpc_id: str
    owner_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List[Any]
    tags: List[Any]
    subnet_arn: str
    outpost_arn: str
    id: str
    vpc: "Vpc"
    instances: SubnetInstancesCollection
    network_interfaces: SubnetNetworkInterfacesCollection

    def create_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        ImageId: str = None,
        InstanceType: InstanceTypeType = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
        Placement: "PlacementTypeDef" = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
        InstanceInitiatedShutdownBehavior: ShutdownBehaviorType = None,
        NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
        ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
        CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
        CpuOptions: CpuOptionsRequestTypeDef = None,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
        HibernationOptions: HibernationOptionsRequestTypeDef = None,
        LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = None
    ) -> List[_Instance]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.create_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetcreate_instances-method)
        """

    def create_network_interface(
        self,
        *,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: NetworkInterfaceCreationTypeType = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> _NetworkInterface:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.create_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetcreate_network_interface-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetcreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetdelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Subnet.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetreload-method)
        """


_Subnet = Subnet


class Vpc(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Vpc)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpc)
    """

    cidr_block: str
    dhcp_options_id: str
    state: str
    vpc_id: str
    owner_id: str
    instance_tenancy: str
    ipv6_cidr_block_association_set: List[Any]
    cidr_block_association_set: List[Any]
    is_default: bool
    tags: List[Any]
    id: str
    dhcp_options: "DhcpOptions"
    accepted_vpc_peering_connections: VpcAcceptedVpcPeeringConnectionsCollection
    instances: VpcInstancesCollection
    internet_gateways: VpcInternetGatewaysCollection
    network_acls: VpcNetworkAclsCollection
    network_interfaces: VpcNetworkInterfacesCollection
    requested_vpc_peering_connections: VpcRequestedVpcPeeringConnectionsCollection
    route_tables: VpcRouteTablesCollection
    security_groups: VpcSecurityGroupsCollection
    subnets: VpcSubnetsCollection

    def associate_dhcp_options(self, *, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.associate_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcassociate_dhcp_options-method)
        """

    def attach_classic_link_instance(
        self, *, Groups: List[str], InstanceId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.attach_classic_link_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcattach_classic_link_instance-method)
        """

    def attach_internet_gateway(self, *, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.attach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcattach_internet_gateway-method)
        """

    def create_network_acl(
        self, *, DryRun: bool = None, TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _NetworkAcl:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.create_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate_network_acl-method)
        """

    def create_route_table(
        self, *, DryRun: bool = None, TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _RouteTable:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.create_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate_route_table-method)
        """

    def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> _SecurityGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.create_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate_security_group-method)
        """

    def create_subnet(
        self,
        *,
        CidrBlock: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None
    ) -> _Subnet:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.create_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate_subnet-method)
        """

    def create_tags(self, *, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate_tags-method)
        """

    def delete(self, *, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdelete-method)
        """

    def describe_attribute(
        self, *, Attribute: VpcAttributeNameType, DryRun: bool = None
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdescribe_attribute-method)
        """

    def detach_classic_link_instance(
        self, *, InstanceId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.detach_classic_link_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdetach_classic_link_instance-method)
        """

    def detach_internet_gateway(self, *, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.detach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdetach_internet_gateway-method)
        """

    def disable_classic_link(self, *, DryRun: bool = None) -> DisableVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.disable_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdisable_classic_link-method)
        """

    def enable_classic_link(self, *, DryRun: bool = None) -> EnableVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.enable_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcenable_classic_link-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcload-method)
        """

    def modify_attribute(
        self,
        *,
        EnableDnsHostnames: "AttributeBooleanValueTypeDef" = None,
        EnableDnsSupport: "AttributeBooleanValueTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcmodify_attribute-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcreload-method)
        """

    def request_vpc_peering_connection(
        self,
        *,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        PeerRegion: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _VpcPeeringConnection:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.request_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcrequest_vpc_peering_connection-method)
        """

    def wait_until_available(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.wait_until_available)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcwait_until_available-method)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.Vpc.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcwait_until_exists-method)
        """


_Vpc = Vpc


class EC2ServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html)
    """

    classic_addresses: ServiceResourceClassicAddressesCollection
    dhcp_options_sets: ServiceResourceDhcpOptionsSetsCollection
    images: ServiceResourceImagesCollection
    instances: ServiceResourceInstancesCollection
    internet_gateways: ServiceResourceInternetGatewaysCollection
    key_pairs: ServiceResourceKeyPairsCollection
    network_acls: ServiceResourceNetworkAclsCollection
    network_interfaces: ServiceResourceNetworkInterfacesCollection
    placement_groups: ServiceResourcePlacementGroupsCollection
    route_tables: ServiceResourceRouteTablesCollection
    security_groups: ServiceResourceSecurityGroupsCollection
    snapshots: ServiceResourceSnapshotsCollection
    subnets: ServiceResourceSubnetsCollection
    volumes: ServiceResourceVolumesCollection
    vpc_addresses: ServiceResourceVpcAddressesCollection
    vpc_peering_connections: ServiceResourceVpcPeeringConnectionsCollection
    vpcs: ServiceResourceVpcsCollection

    def ClassicAddress(self, public_ip: str) -> _ClassicAddress:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceclassicaddress-method)
        """

    def DhcpOptions(self, id: str) -> _DhcpOptions:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcedhcpoptions-method)
        """

    def Image(self, id: str) -> _Image:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceimage-method)
        """

    def Instance(self, id: str) -> _Instance:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceinstance-method)
        """

    def InternetGateway(self, id: str) -> _InternetGateway:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceinternetgateway-method)
        """

    def KeyPair(self, name: str) -> _KeyPairInfo:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcekeypair-method)
        """

    def NetworkAcl(self, id: str) -> _NetworkAcl:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcenetworkacl-method)
        """

    def NetworkInterface(self, id: str) -> _NetworkInterface:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcenetworkinterface-method)
        """

    def NetworkInterfaceAssociation(self, id: str) -> _NetworkInterfaceAssociation:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcenetworkinterfaceassociation-method)
        """

    def PlacementGroup(self, name: str) -> _PlacementGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceplacementgroup-method)
        """

    def Route(self, route_table_id: str, destination_cidr_block: str) -> _Route:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceroute-method)
        """

    def RouteTable(self, id: str) -> _RouteTable:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceroutetable-method)
        """

    def RouteTableAssociation(self, id: str) -> _RouteTableAssociation:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceroutetableassociation-method)
        """

    def SecurityGroup(self, id: str) -> _SecurityGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcesecuritygroup-method)
        """

    def Snapshot(self, id: str) -> _Snapshot:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcesnapshot-method)
        """

    def Subnet(self, id: str) -> _Subnet:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcesubnet-method)
        """

    def Tag(self, resource_id: str, key: str, value: str) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcetag-method)
        """

    def Volume(self, id: str) -> _Volume:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevolume-method)
        """

    def Vpc(self, id: str) -> _Vpc:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.Vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevpc-method)
        """

    def VpcAddress(self, allocation_id: str) -> _VpcAddress:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevpcaddress-method)
        """

    def VpcPeeringConnection(self, id: str) -> _VpcPeeringConnection:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevpcpeeringconnection-method)
        """

    def create_dhcp_options(
        self,
        *,
        DhcpConfigurations: List[NewDhcpConfigurationTypeDef],
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> _DhcpOptions:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_dhcp_options-method)
        """

    def create_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        ImageId: str = None,
        InstanceType: InstanceTypeType = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
        Placement: "PlacementTypeDef" = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        SubnetId: str = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
        InstanceInitiatedShutdownBehavior: ShutdownBehaviorType = None,
        NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
        ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
        CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
        CpuOptions: CpuOptionsRequestTypeDef = None,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
        HibernationOptions: HibernationOptionsRequestTypeDef = None,
        LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = None
    ) -> List[_Instance]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_instances-method)
        """

    def create_internet_gateway(
        self, *, TagSpecifications: List["TagSpecificationTypeDef"] = None, DryRun: bool = None
    ) -> _InternetGateway:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_internet_gateway-method)
        """

    def create_key_pair(
        self,
        *,
        KeyName: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _KeyPair:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_key_pair-method)
        """

    def create_network_acl(
        self,
        *,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _NetworkAcl:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_network_acl-method)
        """

    def create_network_interface(
        self,
        *,
        SubnetId: str,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: NetworkInterfaceCreationTypeType = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> _NetworkInterface:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_network_interface-method)
        """

    def create_placement_group(
        self,
        *,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: PlacementStrategyType = None,
        PartitionCount: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _PlacementGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_placement_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_placement_group-method)
        """

    def create_route_table(
        self,
        *,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _RouteTable:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_route_table-method)
        """

    def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        VpcId: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> _SecurityGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_security_group-method)
        """

    def create_snapshot(
        self,
        *,
        VolumeId: str,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> _Snapshot:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_snapshot-method)
        """

    def create_subnet(
        self,
        *,
        CidrBlock: str,
        VpcId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None
    ) -> _Subnet:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_subnet-method)
        """

    def create_tags(
        self, *, Resources: List[str], Tags: List["TagTypeDef"], DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_tags-method)
        """

    def create_volume(
        self,
        *,
        AvailabilityZone: str,
        Encrypted: bool = None,
        Iops: int = None,
        KmsKeyId: str = None,
        OutpostArn: str = None,
        Size: int = None,
        SnapshotId: str = None,
        VolumeType: VolumeTypeType = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        MultiAttachEnabled: bool = None,
        Throughput: int = None
    ) -> _Volume:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_volume-method)
        """

    def create_vpc(
        self,
        *,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
        DryRun: bool = None,
        InstanceTenancy: TenancyType = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _Vpc:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_vpc-method)
        """

    def create_vpc_peering_connection(
        self,
        *,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _VpcPeeringConnection:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate_vpc_peering_connection-method)
        """

    def disassociate_route_table(self, *, AssociationId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.disassociate_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcedisassociate_route_table-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceget_available_subresources-method)
        """

    def import_key_pair(
        self,
        *,
        KeyName: str,
        PublicKeyMaterial: Union[bytes, IO[bytes], StreamingBody],
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _KeyPairInfo:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.import_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceimport_key_pair-method)
        """

    def register_image(
        self,
        *,
        Name: str,
        ImageLocation: str = None,
        Architecture: ArchitectureValuesType = None,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        EnaSupport: bool = None,
        KernelId: str = None,
        BillingProducts: List[str] = None,
        RamdiskId: str = None,
        RootDeviceName: str = None,
        SriovNetSupport: str = None,
        VirtualizationType: str = None,
        BootMode: BootModeValuesType = None
    ) -> _Image:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2.html#EC2.ServiceResource.register_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceregister_image-method)
        """
