r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size


__all__ = ["ShelfReason", "ShelfReasonSchema"]
__pdoc__ = {
    "ShelfReasonSchema.resource": False,
    "ShelfReason": False,
}


class ShelfReasonSchema(ResourceSchema):
    """The fields of the ShelfReason object"""

    code = fields.Str(data_key="code")
    r""" Error code """

    message = fields.Str(data_key="message")
    r""" Error message """

    @property
    def resource(self):
        return ShelfReason

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


class ShelfReason(Resource):

    _schema = ShelfReasonSchema
