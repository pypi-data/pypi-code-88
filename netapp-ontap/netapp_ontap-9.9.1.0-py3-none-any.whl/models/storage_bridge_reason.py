r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["StorageBridgeReason", "StorageBridgeReasonSchema"]
__pdoc__ = {
    "StorageBridgeReasonSchema.resource": False,
    "StorageBridgeReason": False,
}


class StorageBridgeReasonSchema(ResourceSchema):
    """The fields of the StorageBridgeReason object"""

    code = fields.Str(data_key="code")
    r""" The code field of the storage_bridge_reason. """

    message = fields.Str(data_key="message")
    r""" The message field of the storage_bridge_reason. """

    @property
    def resource(self):
        return StorageBridgeReason

    gettable_fields = [
        "code",
        "message",
    ]
    """code,message,"""

    patchable_fields = [
        "code",
        "message",
    ]
    """code,message,"""

    postable_fields = [
        "code",
        "message",
    ]
    """code,message,"""


class StorageBridgeReason(Resource):

    _schema = StorageBridgeReasonSchema
