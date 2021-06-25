r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["VolumeSpace1Snapshot", "VolumeSpace1SnapshotSchema"]
__pdoc__ = {
    "VolumeSpace1SnapshotSchema.resource": False,
    "VolumeSpace1Snapshot": False,
}


class VolumeSpace1SnapshotSchema(ResourceSchema):
    """The fields of the VolumeSpace1Snapshot object"""

    autodelete_enabled = fields.Boolean(data_key="autodelete_enabled")
    r""" Specifies whether Snapshot copy autodelete is currently enabled on this volume. """

    reserve_percent = Size(data_key="reserve_percent")
    r""" The space that has been set aside as a reserve for Snapshot copy usage, in percent. """

    reserve_size = Size(data_key="reserve_size")
    r""" Size in the volume that has been set aside as a reserve for Snapshot copy usage, in bytes. """

    space_used_percent = Size(data_key="space_used_percent")
    r""" Percentage of snapshot reserve size that has been used. """

    used = Size(data_key="used")
    r""" The total space used by Snapshot copies in the volume, in bytes. """

    @property
    def resource(self):
        return VolumeSpace1Snapshot

    gettable_fields = [
        "reserve_percent",
        "reserve_size",
        "space_used_percent",
        "used",
    ]
    """reserve_percent,reserve_size,space_used_percent,used,"""

    patchable_fields = [
        "autodelete_enabled",
        "reserve_percent",
    ]
    """autodelete_enabled,reserve_percent,"""

    postable_fields = [
        "reserve_percent",
    ]
    """reserve_percent,"""


class VolumeSpace1Snapshot(Resource):

    _schema = VolumeSpace1SnapshotSchema
