r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["DiskOutageReason", "DiskOutageReasonSchema"]
__pdoc__ = {
    "DiskOutageReasonSchema.resource": False,
    "DiskOutageReason": False,
}


class DiskOutageReasonSchema(ResourceSchema):
    """The fields of the DiskOutageReason object"""

    code = fields.Str(data_key="code")
    r""" This field provides the error code explaining why a disk failed.

Example: 721081 """

    message = fields.Str(data_key="message")
    r""" This field provides the error message explaining why a disk failed.

Example: not responding """

    @property
    def resource(self):
        return DiskOutageReason

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


class DiskOutageReason(Resource):

    _schema = DiskOutageReasonSchema
