r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["DiskErrorInfoReason", "DiskErrorInfoReasonSchema"]
__pdoc__ = {
    "DiskErrorInfoReasonSchema.resource": False,
    "DiskErrorInfoReason": False,
}


class DiskErrorInfoReasonSchema(ResourceSchema):
    """The fields of the DiskErrorInfoReason object"""

    code = fields.Str(data_key="code")
    r""" Provides an error code. """

    message = fields.Str(data_key="message")
    r""" Provides an error message detailing the error state of this disk.

Example: not responding """

    @property
    def resource(self):
        return DiskErrorInfoReason

    gettable_fields = [
        "code",
        "message",
    ]
    """code,message,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class DiskErrorInfoReason(Resource):

    _schema = DiskErrorInfoReasonSchema
