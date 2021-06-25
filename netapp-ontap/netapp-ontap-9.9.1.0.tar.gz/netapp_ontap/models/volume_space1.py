r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["VolumeSpace1", "VolumeSpace1Schema"]
__pdoc__ = {
    "VolumeSpace1Schema.resource": False,
    "VolumeSpace1": False,
}


class VolumeSpace1Schema(ResourceSchema):
    """The fields of the VolumeSpace1 object"""

    afs_total = Size(data_key="afs_total")
    r""" Total size of AFS, excluding snap-reserve, in bytes. """

    available = Size(data_key="available")
    r""" The available space, in bytes. """

    available_percent = Size(data_key="available_percent")
    r""" The space available, as a percent. """

    block_storage_inactive_user_data = Size(data_key="block_storage_inactive_user_data")
    r""" The size that is physically used in the block storage of the volume and has a cold temperature. In bytes. This parameter is only supported if the volume is in an aggregate that is either attached to a cloud store or could be attached to a cloud store. """

    block_storage_inactive_user_data_percent = Size(data_key="block_storage_inactive_user_data_percent")
    r""" Percentage of size that is physically used in the performance tier of the volume. """

    capacity_tier_footprint = Size(data_key="capacity_tier_footprint")
    r""" Space used by capacity tier for this volume in the FabricPool aggregate, in bytes. """

    footprint = Size(data_key="footprint")
    r""" Data used for this volume in the aggregate, in bytes. """

    fractional_reserve = Size(data_key="fractional_reserve")
    r""" Used to change the amount of space reserved for overwrites of reserved objects in a volume. """

    full_threshold_percent = Size(data_key="full_threshold_percent")
    r""" Volume full threshold percentage at which EMS warnings can be sent. """

    local_tier_footprint = Size(data_key="local_tier_footprint")
    r""" Space used by the local tier for this volume in the aggregate, in bytes. """

    logical_space = fields.Nested("netapp_ontap.models.volume_space1_logical_space.VolumeSpace1LogicalSpaceSchema", unknown=EXCLUDE, data_key="logical_space")
    r""" The logical_space field of the volume_space1. """

    metadata = Size(data_key="metadata")
    r""" Space used by the volume metadata in the aggregate, in bytes. """

    nearly_full_threshold_percent = Size(data_key="nearly_full_threshold_percent")
    r""" Volume nearly full threshold percentage at which EMS warnings can be sent. """

    over_provisioned = Size(data_key="over_provisioned")
    r""" The amount of space not available for this volume in the aggregate, in bytes. """

    overwrite_reserve = Size(data_key="overwrite_reserve")
    r""" Reserved space for overwrites, in bytes. """

    overwrite_reserve_used = Size(data_key="overwrite_reserve_used")
    r""" Overwrite logical reserve space used, in bytes. """

    percent_used = Size(data_key="percent_used")
    r""" Percentage of the volume size that is used. """

    performance_tier_footprint = Size(data_key="performance_tier_footprint")
    r""" Space used by the performance tier for this volume in the FabricPool aggregate, in bytes. """

    size = Size(data_key="size")
    r""" Total provisioned size. The default size is equal to the minimum size of 20MB, in bytes. """

    size_available_for_snapshots = Size(data_key="size_available_for_snapshots")
    r""" Available space for Snapshot copies from snap-reserve, in bytes. """

    snapshot = fields.Nested("netapp_ontap.models.volume_space1_snapshot.VolumeSpace1SnapshotSchema", unknown=EXCLUDE, data_key="snapshot")
    r""" The snapshot field of the volume_space1. """

    total_footprint = Size(data_key="total_footprint")
    r""" Data and metadata used for this volume in the aggregate, in bytes. """

    used = Size(data_key="used")
    r""" The virtual space used (includes volume reserves) before storage efficiency, in bytes. """

    used_by_afs = Size(data_key="used_by_afs")
    r""" The space used by Active Filesystem, in bytes. """

    @property
    def resource(self):
        return VolumeSpace1

    gettable_fields = [
        "afs_total",
        "available",
        "available_percent",
        "block_storage_inactive_user_data",
        "block_storage_inactive_user_data_percent",
        "capacity_tier_footprint",
        "footprint",
        "fractional_reserve",
        "full_threshold_percent",
        "local_tier_footprint",
        "logical_space",
        "metadata",
        "nearly_full_threshold_percent",
        "over_provisioned",
        "overwrite_reserve",
        "overwrite_reserve_used",
        "percent_used",
        "performance_tier_footprint",
        "size",
        "size_available_for_snapshots",
        "snapshot",
        "total_footprint",
        "used",
        "used_by_afs",
    ]
    """afs_total,available,available_percent,block_storage_inactive_user_data,block_storage_inactive_user_data_percent,capacity_tier_footprint,footprint,fractional_reserve,full_threshold_percent,local_tier_footprint,logical_space,metadata,nearly_full_threshold_percent,over_provisioned,overwrite_reserve,overwrite_reserve_used,percent_used,performance_tier_footprint,size,size_available_for_snapshots,snapshot,total_footprint,used,used_by_afs,"""

    patchable_fields = [
        "afs_total",
        "available_percent",
        "fractional_reserve",
        "full_threshold_percent",
        "logical_space",
        "nearly_full_threshold_percent",
        "size",
        "snapshot",
        "used_by_afs",
    ]
    """afs_total,available_percent,fractional_reserve,full_threshold_percent,logical_space,nearly_full_threshold_percent,size,snapshot,used_by_afs,"""

    postable_fields = [
        "afs_total",
        "available_percent",
        "fractional_reserve",
        "full_threshold_percent",
        "logical_space",
        "nearly_full_threshold_percent",
        "size",
        "snapshot",
        "used_by_afs",
    ]
    """afs_total,available_percent,fractional_reserve,full_threshold_percent,logical_space,nearly_full_threshold_percent,size,snapshot,used_by_afs,"""


class VolumeSpace1(Resource):

    _schema = VolumeSpace1Schema
