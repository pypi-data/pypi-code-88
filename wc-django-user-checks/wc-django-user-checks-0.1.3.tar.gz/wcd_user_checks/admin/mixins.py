from ..cases import send_checks_changed
from ..discovery import get_registry
from ..utils import fix_check


__all__ = 'AdminBaseMixin',


class AdminBaseMixin:
    readonly_fields = (
        'user', 'reason', 'meta', 'is_passed', 'created_at', 'updated_at',
    )
    readonly_fields_on_create = ()

    def get_readonly_fields(self, request, obj = None):
        if obj is None:
            return self.readonly_fields_on_create

        return super().get_readonly_fields(request, obj=obj)

    def save_model(self, request, obj, form, change):
        obj = fix_check(get_registry(), obj)
        super().save_model(request, obj, form, change)
        send_checks_changed([obj])
