from ._op_item_type_registry import op_register_item_type
from ._op_items_base import OPAbstractItem
from .item_section import OPSection, OPSectionField
from ..py_op_exceptions import OPInvalidItemException


class OPAddressField(OPSectionField):

    def __init__(self, field_dict):
        super().__init__(field_dict)

        if self.field_type != "address":
            raise OPInvalidItemException("Address field malformed")

        if self.label != "address":
            raise OPInvalidItemException("Address field malformed")

        if self.field_name != "address":
            raise OPInvalidItemException("Address field malformed")

        if not isinstance(self.value, dict):
            raise OPInvalidItemException("Address field malformed")

        for required in ["city", "country", "state", "street", "zip"]:
            if required not in self.value:
                raise OPInvalidItemException("Address field malformed")

class OPAddressSection(OPSection):
    def __init__(self, section_dict):
        super().__init__(section_dict)
        address_field = self.fields
