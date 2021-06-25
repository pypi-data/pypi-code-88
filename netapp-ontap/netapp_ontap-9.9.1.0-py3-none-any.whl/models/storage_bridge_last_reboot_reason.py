r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["StorageBridgeLastRebootReason", "StorageBridgeLastRebootReasonSchema"]
__pdoc__ = {
    "StorageBridgeLastRebootReasonSchema.resource": False,
    "StorageBridgeLastRebootReason": False,
}


class StorageBridgeLastRebootReasonSchema(ResourceSchema):
    """The fields of the StorageBridgeLastRebootReason object"""

    code = fields.Str(data_key="code")
    r""" This field provides the error code explaining why did the bridge reboot.

Example: 39321683 """

    message = fields.Str(data_key="message")
    r""" This field provides the error message explaining why did the bridge reboot.

Example: FirmwareRestart Command """

    @property
    def resource(self):
        return StorageBridgeLastRebootReason

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


class StorageBridgeLastRebootReason(Resource):

    _schema = StorageBridgeLastRebootReasonSchema
